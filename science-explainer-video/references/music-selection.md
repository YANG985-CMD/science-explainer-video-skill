# Content-based background music

The owner's 2026-10-15 request replaces the fixed WeNever default: **save the recommended tracks locally and automatically choose music to fit future video content**. Do not ask for a music choice for every video. Keep the separate style/glow/palette confirmation rules, the approved male voice, and minimalist 3–4 minute duration unchanged. An explicit track or silent / owner-adds-music instruction takes priority.

## Local catalog and selection

For the owner's installation, read the optional `references/owner-music-library.json`, then its `catalog` path. That catalog records actual full masters, hashes, duration, acquisition status, video-use conditions, attribution, topic rules and preferences. This owner file and the music library are private local resources. They are not included in the public skill. On another installation, supply an equivalent catalog with `--catalog`; do not assume the original owner's files are available.

Run `scripts/select_music.py --topic "FOC：旋转坐标系、波形和闭环控制" --mode minimalist`. Use `--mode narrated` when a narrator is present. The helper verifies master size/hash, filters unavailable or unresolved tracks, and returns an absolute file path, reason, source and any description credit. It does not download, purchase, render or publish. `--track-id` requires that exact usable track and fails rather than substituting; `--silent` returns no audio stream. The helper is a starting selection: audition against the storyboard and adjust among the available fitting tracks if the mood or musical phrasing conflicts with reading and observation time.

## Intended matching

| Content | Preferred character / candidate | Available fallback approach |
| --- | --- | --- |
| FOC, SPWM/SVPWM, PMSM, PPO, algorithms, waveforms | Regular electronic pulse; HOME — Resonance | The owner's clean WeNever for active minimalist animation; weaker melody under narration |
| Compliance, impedance/admittance, physical interaction | Calm movement and warmth; Tycho — A Walk | Signal to Noise when a restrained, reflective mood fits |
| Hardware, sampling, engineering signal chains | Restrained technology bed; Alexi Action — Documentary Background (Technology) | A fitting existing instrumental master, avoiding an excessively dramatic cue |
| Development, literature history, gradual insights | Reflective documentary arc; Scott Buckley — Signal to Noise | Full Mix for silent visual explanation; No Piano Melody for narration |
| A short opening or key turn | The xx — Intro when that exact cue is available and suitable | Use the main bed's opening; do not automatically add another song |

These are **matching preferences, not proof that all tracks were downloaded or licensed**. Consult current catalog status before use. Do not replace a requested recording with a same-title track, cover, remix or preview. Automatic choices must have a verified full local asset and recorded usable conditions. A purchased listening download or an artist's free album download does not by itself establish video-use permission. Pending entries stay cataloged but cannot be automatically selected. Report a real blocker concisely; do not turn routine video production into repeated music approvals.

## Editing and credit

- Normally use one continuous instrumental bed; do not change songs at every chapter. Select a musical section and a clean loop/crossfade if needed, with natural opening/ending fades. Align a major operation to an actual musical accent only when reading and observation holds remain comfortable.
- Keep the narrator intelligible in narrated mode: prefer less melodic alternatives and lower/duck the bed. Preserve the approved voice; this policy does not change the speaker.
- Inspect encoded audio coverage, full decode, clipping, joins and perceived level. Listen to representative edits and the ending for speech, watermarks or platform prompts. The owner's legacy WeNever must use the **clean file with the platform-voice tail removed**, not the older 192.84-second extraction. Verify the catalog hash.
- Put required music credit and modification notes in the delivery/source companion, ready to paste into the platform's video description. Do not add tiny source or production-status footers to video frames. For Scott Buckley, preserve the recorded CC-BY 4.0 attribution, including artist and official site; state editing/looping/fades when applied. Keep CC assets separate from MIT skill code.
- Record the actual track/version, hash, source interval, loop/edit points, gain/fades, credit and output video in each video's production companion. This is production evidence, not audience-facing copy.
- Keep original masters intact. Put render caches, waveforms, previews and edited temporary audio in the environment's task temporary directory. Do not publish new music files, private catalogs, local paths, accounts or download tokens to GitHub without a specific publication request.

## Extending the catalog

Add a track as auto-eligible only after obtaining the exact full recording, decoding it successfully, recording its duration/bytes/SHA-256, and resolving its video-use conditions. The catalog's `full_master` means a verified complete usable recording, not a promise of lossless studio quality. Label an official CC-licensed video audio extraction honestly, keep its original audio, and identify any MP3 compatibility conversion. Record and credit the actual CC BY version (3.0 or 4.0), not an assumed newer version. Separate acquisition status from rights status. Keep purchase-only, failed-download and preview entries visible as pending, with canonical source links and no fake audio paths. A successfully downloaded file may remain ineligible for automatic video use when its conditions are unresolved. Do not treat a hidden legacy license dialog as proof that a current preview is a full downloadable master. Preserve existing assets and unrelated preferences.
