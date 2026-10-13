"""Reuse the bundled, confirmed Chinese narrator's experimental ICL recipe."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import wave

DEFAULT_PROFILE = Path(__file__).resolve().parents[1] / 'assets' / 'voice' / 'default-zh-male'


def checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def load_profile(folder: Path) -> dict:
    profile = json.loads((folder / 'voice_profile.json').read_text(encoding='utf-8'))
    for asset in profile['audio_assets']:
        file = folder / asset['file']
        if file.stat().st_size != asset['bytes'] or checksum(file) != asset['sha256']:
            raise ValueError(f'Voice asset differs from the confirmed resource: {asset["file"]}')
        if file.suffix == '.wav':
            with wave.open(str(file), 'rb') as audio:
                actual = (audio.getframerate(), audio.getnchannels(), audio.getsampwidth(), audio.getnframes())
            expected = (asset['sample_rate_hz'], asset['channels'], asset['sample_width_bytes'], asset['frames'])
            if actual != expected:
                raise ValueError(f'Voice audio format differs from the manifest: {asset["file"]}')
    for key, text_key in [('reference_transcript_file', 'reference_transcript'),
                          ('approved_transcript_file', 'approved_transcript')]:
        if (folder / profile[key]).read_text(encoding='utf-8-sig').strip() != profile[text_key]:
            raise ValueError(f'Transcript differs from the manifest: {profile[key]}')
    return profile


def configure_work_dir(folder: Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    os.environ['TEMP'] = os.environ['TMP'] = str(folder)
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    for name, subfolder in {
        'HF_HOME': 'hf_cache', 'HF_HUB_CACHE': 'hf_cache/hub',
        'TORCH_HOME': 'torch_cache', 'TORCHINDUCTOR_CACHE_DIR': 'torch_inductor',
        'NUMBA_CACHE_DIR': 'numba_cache', 'MPLCONFIGDIR': 'mpl_cache',
        'GRADIO_TEMP_DIR': 'gradio', 'XDG_CACHE_HOME': 'cache',
    }.items():
        os.environ[name] = str(folder / subfolder)
    os.environ['HF_HUB_OFFLINE'] = os.environ['TRANSFORMERS_OFFLINE'] = '1'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile-dir', type=Path, default=DEFAULT_PROFILE)
    parser.add_argument('--check-profile', action='store_true', help='Verify packaged audio and transcripts; no model required.')
    parser.add_argument('--model-dir', type=Path, help='Local official 0.6B CustomVoice checkpoint; weights are downloaded separately.')
    parser.add_argument('--verify-model', action='store_true', help='Also compare model weights/configuration hashes with the recorded checkpoint.')
    parser.add_argument('--text-file', type=Path, help='UTF-8 narration text, one short passage per call.')
    parser.add_argument('--output', type=Path, help='Output PCM WAV path.')
    parser.add_argument('--work-dir', type=Path, help='Explicit scratch/cache directory; required for synthesis.')
    parser.add_argument('--seed', type=int, help='Override the saved default seed.')
    parser.add_argument('--device', default='cpu', help='Recorded and tested device: cpu. Other devices require a voice check.')
    args = parser.parse_args()
    profile_dir = args.profile_dir.resolve()
    profile = load_profile(profile_dir)
    if args.verify_model:
        if args.model_dir is None:
            parser.error('--verify-model requires --model-dir')
        for asset in profile['model_assets']:
            file = args.model_dir / asset['file']
            if file.stat().st_size != asset['bytes'] or checksum(file) != asset['sha256']:
                raise ValueError(f'Checkpoint differs from the recorded configuration: {asset["file"]}')
    if args.check_profile:
        print(json.dumps({'profile_id': profile['profile_id'], 'audio_integrity': 'passed',
                          'transcripts': 'passed', 'model_integrity': 'passed' if args.verify_model else 'not_requested'}, ensure_ascii=False))
        return
    for field in ('model_dir', 'text_file', 'output', 'work_dir'):
        if getattr(args, field) is None:
            parser.error(f'synthesis requires --{field.replace("_", "-")}')
    text = args.text_file.read_text(encoding='utf-8-sig').strip()
    if not text:
        parser.error('narration text is empty')
    work = args.work_dir.resolve()
    if work == profile_dir or profile_dir in work.parents:
        parser.error('--work-dir must be separate from the published voice profile')
    output = args.output.resolve()
    if output == profile_dir or profile_dir in output.parents:
        parser.error('--output must be separate from the published voice profile')
    configure_work_dir(work)
    config = json.loads((args.model_dir / 'config.json').read_text(encoding='utf-8'))
    if config.get('tts_model_type') != 'custom_voice' or config.get('tts_model_size') != '0b6':
        raise ValueError('This recipe requires Qwen3-TTS-12Hz-0.6B-CustomVoice.')
    import numpy as np
    import soundfile as sf
    import torch
    from transformers import set_seed
    from qwen_tts import Qwen3TTSModel
    from qwen_tts.inference.qwen3_tts_model import VoiceClonePromptItem

    generation = profile['generation']
    torch.set_num_threads(generation['cpu_threads'])
    seed = generation['seed'] if args.seed is None else args.seed
    set_seed(seed)
    model = Qwen3TTSModel.from_pretrained(str(args.model_dir.resolve()), device_map=args.device,
                                         dtype=torch.bfloat16, attn_implementation=generation['attention'])
    # Preserve the accepted experiment. This changes only the in-memory instance;
    # it is not the official Base checkpoint's supported voice-clone route.
    model.model.tts_model_type = generation['runtime_type_override']
    reference, sample_rate = sf.read(str(profile_dir / profile['reference_audio']))
    codes = model.model.speech_tokenizer.encode([reference], sr=sample_rate).audio_codes[0]
    prompt = VoiceClonePromptItem(
        ref_code=codes,
        ref_spk_embedding=torch.zeros(1, model.model.talker.config.hidden_size, dtype=model.model.dtype),
        x_vector_only_mode=False, icl_mode=True, ref_text=profile['reference_transcript'],
    )
    # Video production resets the seed for each passage after preparing the model
    # and reference prompt, so loading/tokenizing cannot consume its random state.
    set_seed(seed)
    with torch.inference_mode():
        waves, rate = model.generate_voice_clone(
            text=text, language=generation['language'], voice_clone_prompt=[prompt],
            max_new_tokens=generation['max_new_tokens'], temperature=generation['temperature'], top_p=generation['top_p'],
        )
    audio = waves[0]
    if len(audio) <= rate or not np.isfinite(audio).all() or float(np.max(np.abs(audio))) <= .01:
        raise ValueError('Generated narration is empty or invalid.')
    output.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(output), audio, rate, subtype='PCM_16')
    print(json.dumps({'output': str(output), 'duration_seconds': len(audio) / rate,
                      'sample_rate_hz': rate, 'seed': seed, 'profile_id': profile['profile_id'],
                      'method': generation['method'], 'work_dir': str(work)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
