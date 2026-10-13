---
name: science-explainer-video
description: Create or revise narrated science and engineering videos with dark, softly glowing diagrams and continuous causal animation. Use when principles, equations, algorithms, or paper improvements should unfold visibly instead of appearing as slide summaries.
---

# Continuous science explainer video

Produce a watchable video in which the viewer follows the same object from a phenomenon, through its mechanism, to an explanation. The defining style is **continuous causal animation**; a dark palette and glow support it.

## Preserve the brief

- Use the user's approved sample and constraints when available. Do not claim to have watched or heard a reference that has not actually been inspected.
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

## Visual language

Use a near-black blue background, restrained fine lines, off-white reference objects, cyan active/model objects, gold comparisons/residuals, and optional pink/purple parameter colors. These are starting points; preserve a user's approved palette.

Reserve a subtitle area separate from the scientific content. Keep equation labels and provenance out of it. Prefer one short line, or at most two lines where needed; split by spoken phrase and rendered width rather than only character count. Highlight a few terms with their object colors.

Glow should stay behind a crisp core stroke. It must not blur text, merge nearby curves, obscure intersections, or become the principal source of contrast. Avoid large card grids when a continuous canvas can show the relationship more clearly.

The optional original Pillow helper [scripts/glow_canvas.py](scripts/glow_canvas.py) supplies a logical 1920 × 1080 canvas, soft glow, crisp lines, safe caption placement, and an ffmpeg pipe. [scripts/render_example.py](scripts/render_example.py) demonstrates a computed RC response, residual, parameter update, and objective plot. This minimal example is not a complete video generator or a substitute for subject-specific models.

## Narration and evidence

- Reuse the user's approved voice configuration and reference audio when authorized and available. Read their voice profile before synthesis; a generic “mature male” label is insufficient to recreate a confirmed voice. Do not replace the speaker silently or simulate a requested voice by lowering pitch.
- Keep local voice paths, reference recordings, model weights, credentials, and private measurements out of a shared skill or repository unless the user specifically authorizes publishing them.
- Use the narration timeline to trigger explanatory actions. Keep time for observation and comparison; do not fill every pause with a new object.
- Distinguish **principle illustration**, **simulation**, **paper-reported results**, and **the speaker's own measurements** in narration and visible provenance. Read primary papers before stating their mechanisms or numerical improvements. When only an abstract is available, identify that limit and do not invent derivation details.
- Keep claim-to-source records with page/figure/section references for literature and input/configuration identifiers for experiments. Make sources available alongside the video; avoid narrating implementation metadata that does not help the viewer.

## Render and inspect

Keep intermediate audio, frames, caches, logs, and one-off scripts in the task's designated temporary directory. Respect environment-specific temporary-file rules; they override helper examples. Save deliverables to the requested output directory.

Before the full render, inspect frames where labels are longest, objects cross, equations appear, and transitions begin/end. Check actual font coverage and caption width. Preview a segment with final narration and visible subtitles to judge pacing.

Deliver an encoded video, synchronized subtitles if useful, and a concise source/script companion. Verify the actual encoded file: resolution, aspect ratio, duration, successful full decode, audio presence when narrated, subtitle bounds, and representative transition/diagram frames. For quantitative scenes, check plotted values and displayed metrics against the data. A static contact sheet does not establish temporal synchronization.

Report material limitations honestly. Do not call a preview a complete video or say a check passed without running it.
