---
name: science-explainer-video
description: Create or revise science and engineering videos with continuous causal animation, choosing narrated explanation or a no-voiceover minimalist style. Use when principles, equations, algorithms, or paper improvements should unfold visibly instead of appearing as slide summaries.
---

# Continuous science explainer video

Produce a watchable video in which the viewer follows the same object from a phenomenon, through its mechanism, to an explanation. The defining style is **continuous causal animation**; a dark palette and the selected glow mode support it.

## Choose the video style

Keep two choices available; adding the second does not replace the first or change the approved narrator.

1. **男声讲解风 — narrated explanation:** the existing continuous diagrams with the user's approved voice; choose standard, low, or no glow according to the brief.
2. **无配音简约风 — no-voiceover minimalist:** concise on-screen prose and a spacious, direct main graphic carry the explanation. Produce no human speech or TTS. This owner supplies their own instrumental music, so deliver a silent edit with no music or sound effects unless explicitly requested. Read [references/minimalist-no-voiceover.md](references/minimalist-no-voiceover.md) before storyboarding this mode.

For a new video whose style is unspecified, ask once: “这次用哪种风格：原男声讲解风，还是无配音简约风（音乐你自行添加）？” An explicit style choice in the current brief answers this question. Preserve it for routine revisions. In minimalist mode, use the restrained surface treatment in its reference; an explicit low/no/standard-glow instruction overrides that preset. In narrated mode, ask the glow question below if the current brief has not answered it. Research and scripting may proceed while a needed style answer is pending.

## Preserve the brief

- Use the user's approved sample and constraints when available. Do not claim to have watched or heard a reference that has not actually been inspected.
- For a new narrated video with no explicit glow choice, ask: “这次视频是否使用低泛光模式（画面更朴素、线条更清晰）？” Offer low-glow, standard-glow, and no-glow choices. Ask again for a revision that changes the surface treatment, but preserve the chosen mode for routine edits. An explicit choice in the current brief counts as the answer; a previous video's choice alone does not. Wait for the answer before style-dependent previews or rendering. Selecting 无配音简约风 already selects its restrained visual preset unless the user says otherwise; do not add a redundant glow question.
- Default to normal playback speed. Change speed only when requested, keeping audio pitch and subtitle timing consistent.
- For a new standalone video, 1920 × 1080 landscape is a useful default; preserve the requested orientation and aspect ratio.
- In Chinese audience-facing explanations, prefer “我们” for shared reasoning. Use “我” when the speaker describes their own implementation, choices, and experiments. Preserve the intended perspective in other languages.
- A sample request calls for a representative sequence; a request to finish the video calls for the complete agreed scope.

## Explain by showing a chain of causes

1. Introduce an observable question with an object that returns later: a waveform, circuit, trajectory, rotating vector, or measurement.
2. Show a concrete failure or discrepancy. Give the viewer time to see it before naming the method.
3. Change one meaningful input or operation and show its corresponding consequence at the same moment.
4. Introduce an equation after its visual meaning is established. Highlight a term and the corresponding object together.
5. Carry an existing object into the next shot by moving, scaling, or transforming it. Use a short dissolve when continuity cannot be represented honestly.
6. Revisit the original question using the objects the viewer now understands.

For a paper or algorithm, animate **difficulty → visible failure → added operation → changed result → conditions and limits**. Author/year/method labels alone do not explain an improvement. Read [references/animation-playbook.md](references/animation-playbook.md) when designing the storyboard, transition, or literature sequence.

## Keep motion tied to meaning

- Maintain a persistent identity for each variable: color, label, units, and role. Dim context rather than erasing it on every shot.
- Build input, prediction, residual, and metric from the same simulation state or measured record. A changed parameter must change the rendered response through the model.
- A scanner links simultaneous values; a moving window links the selected interval to its aggregate; a trail shows the history of actual updates. Do not substitute decorative motion for these relations.
- Reveal information in useful increments. Stop moving a completed object when stillness helps the viewer compare it with the new one.
- Frame a parameter-space point as one candidate vector. If only two parameters vary, label the other fixed parameters. Indicate transforms such as a logarithmic error height.
- Do not silently interpolate reported measurements or algorithm iterates. Smooth motion may interpolate display position; label a continuous illustrative path when it does not reproduce the actual algorithm.

## Transitions and visual substance

The owner's standing requirement is: “视频检查一下转场，不要出现一张图只有字表的情况，要把图丰富起来。”

- Explain each spoken beat, or each on-screen explanatory beat in minimalist mode, with a meaningful non-text object: a mechanism, device, waveform, rotating vector, physical action, or data-linked graphic. A full-screen list, formula, or table alone does not satisfy this video style. Connect text and table values to a visible mechanism or changing response; use the selected mode's text hierarchy.
- Vary the view when it clarifies the next cause: whole system, local detail, time trace, frequency trace, or side-by-side comparison. Do not fill a passage with one repeated loop or add unrelated decorative motion.
- Inspect each scene change and each within-scene layout change in the actual encoded video before, during, and after the transition. Preserve object identity and avoid double labels, overlapping captions, clipped diagrams, unintended black flashes, and motion that resets without explanation.
- Explicitly check “转场后是否重影”: after the transition has ended, the new scene must contain no unintended remnants of the previous scene, doubled text or curves, or accumulating trails. Inspect several subsequent frames and the surrounding playback; correct any residual layers and recheck the encoded result before delivery.
- Do not blindly crossfade complete text-bearing frames. Carry a shared object across the change, transition graphic layers separately, or use a short fade through dark in a narration pause. Render captions and source labels once, and finish the transition before the next explanation needs its diagram. Read [references/animation-playbook.md](references/animation-playbook.md#transitions-and-visual-substance) for review details.

## Visual language

For narrated mode, use a near-black blue background, restrained fine lines, off-white reference objects, cyan active/model objects, gold comparisons/residuals, and optional pink/purple parameter colors. Minimalist mode uses the more limited palette and spacious composition in its reference. Preserve a user's approved palette.

In narrated mode, reserve a subtitle area separate from the scientific content. Keep equation labels and provenance out of it. Prefer one short line, or at most two lines where needed; split by spoken phrase and rendered width rather than only character count. In minimalist mode, compose short explanatory text as part of the scene instead of adding a second transcript band. Highlight a few terms with their object colors.

Keep audience-facing frames free of production-status text, including banners or footers such as “理想原理计算示意·正常速度·已确认男声”. Do not display playback-speed labels, voice-approval status, rendering details, or generic process descriptions in the cover, diagrams, subtitles, or end card. Keep those details in delivery notes when useful. Retain concise, scene-specific evidence/source notes, assumptions, and distinctions between calculated illustrations and measurements where they help the viewer interpret the content; see [references/animation-playbook.md](references/animation-playbook.md#audience-facing-text-and-provenance).

Write displayed quantities in captions, titles, and graphics with Arabic numerals and standard unit symbols, for example `8.66 V`, `30°`, `24 V`, and `15.47%`. Keep natural Chinese number pronunciation when narration is used; preserve terms such as “三相”, “零序”, and “三次谐波”. Normalize display text before wrapping or export, preserving values, signs, precision, and units; see [references/animation-playbook.md](references/animation-playbook.md#subtitle-numbers-and-units).

Glow should stay behind a crisp core stroke. It must not blur text, merge nearby curves, obscure intersections, or become the principal source of contrast. Avoid large card grids when a continuous canvas can show the relationship more clearly.

**Low-glow mode:** preserve the dark canvas and continuous causal animation, use crisp solid strokes and muted accent colors, and greatly reduce or omit decorative halos. Keep text and equations sharp without bloom, and maintain contrast through the core strokes. **Standard-glow mode:** retain restrained soft halos behind crisp strokes. Record the selected mode in production settings, not in audience-facing text; read [references/animation-playbook.md](references/animation-playbook.md#glow-modes) for rendering guidance.

The optional original Pillow helper [scripts/glow_canvas.py](scripts/glow_canvas.py) supplies a logical 1920 × 1080 canvas, soft glow, crisp lines, safe caption placement, and an ffmpeg pipe. [scripts/render_example.py](scripts/render_example.py) demonstrates a computed RC response, residual, parameter update, and objective plot. This minimal example is not a complete video generator or a substitute for subject-specific models.

## Narration and evidence

- Only in narrated mode, reuse the user's approved voice configuration and reference audio when authorized and available. Read their voice profile before synthesis; a generic “mature male” label is insufficient to recreate a confirmed voice. Do not replace the speaker silently or simulate a requested voice by lowering pitch. Minimalist mode skips voice synthesis and does not modify that profile.
- For this repository's bundled Chinese narrator, read [references/voice-profile.md](references/voice-profile.md) and [assets/voice/default-zh-male/voice_profile.json](assets/voice/default-zh-male/voice_profile.json). The owner has explicitly authorized these three reference audio files for public use. [scripts/generate_narration.py](scripts/generate_narration.py) reproduces the recorded experimental recipe with an explicit working directory; compare new narration with the approved preview and preserve the user's choice of another voice when given.
- Keep local voice paths, reference recordings, model weights, credentials, and private measurements out of a shared skill or repository unless the user specifically authorizes publishing them.
- Use the narration timeline to trigger narrated actions. In minimalist mode, build a timed reading-and-action storyboard instead; make the explanation work without listening. Keep time for observation and comparison; do not fill every pause with a new object.
- Distinguish **principle illustration**, **simulation**, **paper-reported results**, and **the speaker's own measurements** in narration and visible provenance. Read primary papers before stating their mechanisms or numerical improvements. When only an abstract is available, identify that limit and do not invent derivation details.
- Keep claim-to-source records with page/figure/section references for literature and input/configuration identifiers for experiments. Make sources available alongside the video; avoid narrating implementation metadata that does not help the viewer.

## Render and inspect

Keep intermediate audio, frames, caches, logs, and one-off scripts in the task's designated temporary directory. Respect environment-specific temporary-file rules; they override helper examples. Save deliverables to the requested output directory.

Generate a separate cover image for each finished video and include it as the opening segment of the encoded video, rather than only providing a thumbnail beside the file. Match the video's aspect ratio, selected glow mode, and visual language; use a concise audience-facing title with a meaningful subject graphic. Allow a short readable hold, then a clean transition into the explanation. Keep narration, burned-in captions, and exported subtitles synchronized when adding the opening. Read [references/animation-playbook.md](references/animation-playbook.md#cover-and-opening) for timing and verification.

Before the full render, inspect frames where labels are longest, objects cross, equations appear, and transitions begin/end. Check actual font coverage and caption width. Preview narrated segments with final narration and subtitles. Preview minimalist segments in silence and check that every claim is understandable, text is readable, and observation time is sufficient.

Deliver an encoded video, synchronized subtitles if useful, and a concise source/script companion. Verify the actual encoded file: resolution, aspect ratio, duration, successful full decode, audio presence when narrated, subtitle bounds, and representative transition/diagram frames. For quantitative scenes, check plotted values and displayed metrics against the data. A static contact sheet does not establish temporal synchronization.

For 无配音简约风, also verify that the delivered file has no unintended narration, music, or sound effects; prefer an MP4 with no audio stream while the owner is adding music later. Deliver the separate cover and a compact timed text/source companion. Export subtitles only when useful; the integrated reading text remains the primary explanation.

Check numeral and unit formatting in both burned-in captions and exported subtitle files before delivery; changing only the sidecar file does not update the video.

Inspect covers, persistent footers, diagrams, captions, and end cards for unnecessary production-status text; retain useful evidence and source notes.

Verify the separate cover file and the actual encoded opening, including its transition into the first scene. Record the explicit post-transition ghosting check alongside transition review; cover and opening review must pass before delivery.

Report material limitations honestly. Do not call a preview a complete video or say a check passed without running it.
