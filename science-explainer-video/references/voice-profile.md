# 视频同款中文男声

仓库所有者于 2026-10-14 明确要求开源视频中的声线资源。本目录记录已确认声线的音频与实际生成方式，方便后续视频保持一致。

## 音频与用途

资源位于 [`assets/voice/default-zh-male/`](../assets/voice/default-zh-male/)：

| 文件 | 用途 |
| --- | --- |
| `approved-preview.mp3` | 用户认可的 Hall 讲解试听，便于直接播放比较。 |
| `approved-preview.wav` | 同一试听的原始 PCM 音频，24 kHz 单声道；作为声线目标。 |
| `approved-transcript.txt` | 已确认试听的朗读文本，可用于试运行。 |
| `icl-reference.wav` | 当前合成方法实际使用的原始参考片段，22.05 kHz 单声道，约3.65秒。 |
| `icl-reference.txt` | 原始参考片段的对应文字，供 ICL 条件生成使用。 |
| `voice_profile.json` | 生成参数、依赖版本、音频格式与校验值、模型权重身份记录。 |

声线以这些实际录音为准。两种 WAV 有不同用途：当前脚本使用 `icl-reference.wav` 作为输入参考，`approved-preview.wav` 作为听感目标；不要互换后仍宣称逐项复现了原配方。

## 实际生成方式

模型为 [Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice)。该上游检查点通常通过固定说话人接口使用。本视频保存的方法则是实验性 ICL：编码参考片段，在内存中将 `tts_model_type` 设为 `base`，并使用全零说话人向量。脚本没有改写下载的模型文件。

这是一份可复用的实际生成记录，而非官方 Base 检查点的标准克隆路径、某个固定说话人，或独立训练的音色权重。仓库包含参考音频与配方，约2.5GB的上游模型文件单独下载。模型核心配置和权重的 SHA-256 值保存在档案中，便于核对下载版本。

已确认的最早试听没有固定随机种子。后续视频默认种子42、CPU、bfloat16、SDPA、6线程，temperature=0.8、top_p=0.9、max_new_tokens=512。未作降调或语速变换。不同文本与运行平台可能产生差异，最终按保存的试听检查声线与朗读内容。

## 安装与生成

从仓库根目录运行。已验证环境为 Python 3.12.14；精确依赖见根目录 [`requirements-narration.txt`](../../requirements-narration.txt)。以下是 CPU 的 PowerShell 示例，所有模型下载缓存和工作文件都放在你指定的任务目录：

```powershell
# 使用自己的任务目录；本例路径也适用于仓库作者的临时文件约定。
$voiceWork = 'E:\simulink\_codex_tmp\narrator-example'
New-Item -ItemType Directory -Path $voiceWork -Force | Out-Null
$env:TEMP = $voiceWork
$env:TMP = $voiceWork
$env:HF_HOME = Join-Path $voiceWork 'hf-cache'
$env:PIP_CACHE_DIR = Join-Path $voiceWork 'pip-cache'

python -m venv (Join-Path $voiceWork 'venv')
$voicePython = Join-Path $voiceWork 'venv\Scripts\python.exe'
& $voicePython -m pip install torch==2.9.1 --index-url https://download.pytorch.org/whl/cpu
& $voicePython -m pip install -r requirements-narration.txt
& (Join-Path $voiceWork 'venv\Scripts\hf.exe') download `
  Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice --local-dir (Join-Path $voiceWork 'model')

& $voicePython -B science-explainer-video/scripts/generate_narration.py `
  --model-dir (Join-Path $voiceWork 'model') `
  --text-file science-explainer-video/assets/voice/default-zh-male/approved-transcript.txt `
  --output (Join-Path $voiceWork 'narration.wav') `
  --work-dir (Join-Path $voiceWork 'synthesis-cache')
```

Linux/macOS 使用 README 中的通用路径示例即可。模型需提前下载，生成阶段默认离线；合成前设置缓存目录，避免把模型或缓存写进 Skill 资源。

生成脚本输出24kHz单声道 PCM WAV，保留自然音高和原速。长稿拆成短段落分别生成，检查末尾是否完整，再按每段录音的实际时长安排动画和字幕。`--seed` 可调整采样，但应重新比较声线；其他设备同样需要单独检查，当前发布的复用验证使用 CPU。

## 校验

只核对音频与文字，不加载模型：

```bash
python science-explainer-video/scripts/generate_narration.py --check-profile
```

同时核对本地核心模型配置和权重：

```bash
python science-explainer-video/scripts/generate_narration.py \
  --check-profile --verify-model --model-dir /path/to/models/qwen3-tts-0.6b-customvoice
```

试听 MP3 使用 `loudnorm=I=-18:TP=-1.5:LRA=7` 和128k MP3编码。正式视频可对拼接后的完整旁白统一音量；不要用音高变换替代声线复用。

## 授权与来源

此次公开的三段音频、配套文字、文档与脚本按仓库根目录的 [MIT LICENSE](../../LICENSE) 提供，由仓库所有者明确授权公开。上游模型遵守其 [Apache-2.0 许可证](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice)，依赖包遵守各自许可证。

个人机器路径、原始整段视频、模型权重与凭证都不属于这个公开包。使用其它参考声音时，另行提供对应授权资源。
