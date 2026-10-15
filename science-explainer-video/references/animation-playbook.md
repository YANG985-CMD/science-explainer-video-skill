# Storyboard and evidence playbook

Read this when deciding what should move and how one explanation should lead into another.

This playbook supplies shared causal, evidence, and transition checks. In 无配音简约风, replace spoken beats and narration-driven timing with on-screen reading/action beats from [minimalist-no-voiceover.md](minimalist-no-voiceover.md). Do not require voice synthesis or a transcript band in that mode. This owner's default is a 3–4 minute edit with confirmed instrumental We Never; an explicit silent brief overrides the music default.

## Plan a scene around an observable operation

Use a scene record rather than a list of slide headings:

```yaml
question: Why does the model response differ from the reference?
carry_in: [reference_waveform, time_axis]
spoken_beat: We change a candidate parameter and compare the responses again.
operation: update parameter -> recompute model -> recompute residual -> update objective
carry_out: [reference_waveform, prediction_waveform, candidate_point]
evidence_type: principle illustration
fixed_conditions: other model parameters and the input record
source: derived model plus simulation configuration
```

For narrated mode, set the operation's timing from the recorded sentence. For minimalist mode, set it after the relevant sentence has become readable and allow time to observe the result. Use separate beats for selecting an interval, measuring the discrepancy, aggregating it, and applying an update. A single normalized progress number suffices for a short demo; a full video usually needs action timestamps.

## Continuity patterns

| Explanation | Visible action | Carry into the next shot |
| --- | --- | --- |
| Prediction and residual | Retain a reference curve; add a prediction; connect equal-time samples. | The same residuals become bars or an accumulated metric. |
| Parameter search | One candidate changes the computed response and objective together. | Shrink the waveforms; the same candidate becomes a point on the objective landscape. |
| Historical residual update | Enqueue real residual samples; highlight those used by the update. | Retain the queue when showing how the parameter changes the prediction. |
| Inverter/input compensation | Show commanded and realized input; mark their discrepancy. | Feed the corrected input into the same prediction model. |
| Sampling/discretization | Freeze sampling instants on the moving physical signal. | Retain the sample dots as the discrete update proceeds. |
| Coordinate transform | Retain one physical vector while axes rotate or change basis. | Match coordinate curves to that vector using consistent colors. |
| Staged mechanical identification | Show steady-speed torque balance before acceleration torque. | Reuse friction estimates when isolating inertia; state load assumptions. |

These are animation patterns. They do not prove that a named paper uses a particular formula; verify that independently.

## Transitions and visual substance

Build a visual inventory from the narration timeline before rendering. For every spoken beat, record the object, visible operation, changing state, and next view. Mark a beat for revision if its entire frame is only text, a formula, or a table. Replace it with the relevant physical device, signal trace, vector, or mechanism; keep explanatory labels short. A table may support a comparison when its values visibly drive the diagram beside it.

Use visual variety to explain, not to decorate. For example, follow a switch timing gap into the conducting diode, zoom into its missing voltage area, then link the resulting current distortion to its spectrum. Keep a source object visible when a new view needs context. Do not reuse the same large frame unchanged while narrating several different mechanisms.

For each chapter boundary and within-scene layout change, inspect decoded frames immediately before, during, and after the transition. Check the shared object's position and scale, signal colors, axis units, moving cursor, labels, caption band, and source note. Inspect the surrounding narrated segment as well: a clean midpoint image alone cannot prove a good transition.

Avoid blending two complete text layers into ghosted labels. Prefer a shared-object move or separate graphic-layer transition; for unrelated compositions, a short fade through dark can occur inside an existing narration pause. Hold the completed old view until the transition begins, and make the new view readable before its next spoken explanation. Draw explanatory captions once after composition; keep source/method footers in the companion document. Intentional fades must not turn into unexplained black flashes during speech.

Add a separate review item, “转场后是否重影”, for every scene or layout transition. Decode several frames after the transition has fully finished, including the start of the next spoken explanation, and watch the surrounding segment. Check that old labels, axes, captions, source notes, curves, and object silhouettes are gone unless deliberately carried forward. Distinguish a labeled scientific history trace from an unintended stale-frame trail. If an old layer persists or alpha accumulation doubles a current object, clear or replace the scene layers, re-encode the affected segment, and review it again. Record checked timestamps and the outcome in delivery checks; inspecting only the blended midpoint cannot satisfy this item.

Deliver only after the encoded transitions and the visual inventory pass this review; a storyboard or static contact sheet alone is insufficient.

## Cover and opening

Create a standalone PNG cover at the video's resolution and aspect ratio, and deliver it beside the encoded video. Use a short title and a representative scientific object or mechanism in the selected visual style; avoid a title-only table or production-status labels. The cover must also appear as the video's actual opening, not merely as player artwork or an external thumbnail.

A readable hold of about 2–3 seconds is a useful starting point; adapt it to title length and the user's brief. Use a clean shared-object change, cut, or brief fade through dark into the first explanation. Avoid crossfading complete text layers. Inspect the encoded first frame, cover hold, transition, and several fully settled frames of the first scene for readability and ghosting.

If inserting a cover before an existing edit, shift all downstream animation, on-screen text, and any narration or subtitle timing by the exact inserted duration. Check the first explanation and a later one for synchronization, and verify the resulting duration and successful full decode. In narrated mode, keep the approved voice and normal playback speed unless the user asks to change them. In minimalist mode, use only the confirmed instrumental music, with no speech or TTS; an explicit silent brief calls for no audio stream. Keep the finished edit within 3–4 minutes for this owner. Include cover-file, encoded-opening, and post-transition ghosting review results in the delivery checks.

## Literature sequence

Start from the baseline process already explained. Each paper modifies a visible place in it, so the audience understands why the modification matters.

- **Problem:** Identify the actual weakness, such as input bias, insufficient excitation, noise, or an unknown load.
- **Failure:** Show what it does to a prediction, residual, estimated parameter, or confidence measure.
- **Operation:** Animate the paper's actual added step. Use a brief abstraction only when details are unavailable, and identify the evidence limit.
- **Consequence:** Use source data for reported results. Use computed illustrative data for a conceptual demonstration, with a visible label.
- **Boundary:** Explain required data, hardware, excitation, or assumptions. Different experiments do not establish a universal ranking.

A transition sentence connects the next method to the visible weakness: “We can now compare candidates, but an inaccurate input voltage can bias every comparison. The next method addresses that input.”

## Quantitative scene record

Track: source/model, units, fixed conditions, varied inputs, preprocessing, equation assumptions, metric definition, and whether the data are synthetic or measured.

For illustrative interpolation, recompute the model at each displayed parameter when feasible. Interpolating two responses without recomputation may create a response that no candidate actually produces.

For objective landscapes, retain the metric definition and fixed parameters. Label log axes, normalization, or height compression. For validation, change the input or operating point and keep fitted parameters fixed; make that distinction visible.

## Glow modes

Use the mode chosen for the current video under the pre-production question in `SKILL.md`. The choice changes surface treatment; preserve the same scientific content, causal animation, color identities, subtitle layout, and approved voice.

- **Low glow:** use a dark matte background, crisp fine strokes, and muted accents from the chosen palette. Remove decorative glows on boxes, connectors, and text. Keep any halo around an active object barely visible. With a separate blurred glow layer, about 10% of its standard compositing opacity is a useful starting point; adjust or omit it after inspecting frames. Preserve core-stroke brightness and text contrast.
- **Standard glow:** use clearly visible strengthened line halos behind crisp active curves or points. Combine a narrow near halo with a broader soft halo while preserving the original stroke color and unblurred text. Keep intersections and nearby comparison curves distinguishable. The palette choice (金色强调 or 深蓝青金) is independent of glow and narration.

Inspect dense curve crossings, small labels, equations, and transitions in the selected mode. Store the choice with rendering settings and keep it consistent throughout the video; do not add an on-screen mode or production-status label.

## Caption and audio review

### Audience-facing text and provenance

Display text that explains the science or its basis. Do not put production-status strings such as “理想原理计算示意·正常速度·已确认男声”, “已确认音色”, or rendering/version details on the cover, in a persistent footer, in subtitles, or on the end card. Playback speed and voice selection belong in delivery notes if needed.

For this owner, do not render a bottom small-print row of provenance, method names, or citations, including “常规中心对齐 SVPWM 的 min/max 等价实现 [1,3]”. Preserve source titles, sections/figures and citations in the companion document. Put essential model conditions, units, or calculated-versus-measured distinctions in ordinary readable annotations beside the relevant diagram. Keep explanatory captions; an author/year may appear in main content when discussing that paper. Check the actual encoded lower edge after every scene change, including the cover and ending.

Compare actual encoded subtitles with the spoken sentence, especially at action boundaries. Prefer phrase-level audio alignment over proportional-character estimates. If only a rough timeline is available, inspect representative joins and identify the approximation.

### Subtitle numbers and units

Separate spoken narration from subtitle display text. A narrator may say “八点六六伏”; the subtitle displays `8.66 V`. Derive both from the same value, and normalize subtitle text before measuring width, wrapping lines, generating ASS/SRT/VTT, or burning captions into frames.

| Spoken Chinese | Subtitle display |
| --- | --- |
| 八点六六伏 | 8.66 V |
| 三十度 | 30° |
| 二十四伏 | 24 V |
| 百分之十五点四七 | 15.47% |
| 三十六点一微秒 | 36.1 μs |
| 负五伏 | −5 V |
| 六分之一 | 1/6 |
| 全零、一零零、一一零、全一（开关状态） | 000、100、110、111 |

Use a space between a number and a unit symbol such as `V`, `A`, `μs`, or `Hz`; keep angle and percent forms as `30°` and `15.47%`. Preserve the quantity's meaning, sign, precision, and context, including peak versus RMS and electrical versus mechanical angle. Do not turn “三相”, “两电平”, “零序”, “三次谐波”, or ordinary prose into digit substitutions. Switch-state bit strings retain leading zeros.

Before delivery, scan the final subtitle text for overlooked Chinese decimals, percentages, fractions, durations, and quantities next to units; review matches in context. Check the corresponding encoded frames and exported subtitle files, including signs, decimals, unit glyphs, and line bounds. A subtitle-only formatting edit should preserve narration audio and timing; regenerate the burned-in captions as well as the sidecar file.

Reserve a caption band before composing content. Measure text with the actual font, including CJK, math symbols, and units. Avoid placing sources, axes, or moving points in the subtitle band. Font fallback is not evidence of complete glyph coverage.

Use the speaker's authorized voice profile. The repository owner's explicitly published reference narrator is described in [voice-profile.md](voice-profile.md); other private profiles remain external to the distributable skill unless publishing is authorized. Preserve natural pitch, clarity, and breathing room. Playback-speed edits require synchronized video timing, audio tempo, and subtitle timestamps.

## Minimal demonstration model

The bundled example uses an ideal series resistor and capacitor driven by a 5 V step, initially uncharged. KCL gives `C dv/dt = (U - v)/R`. Separating variables with `v(0) = 0` gives `v(t) = U [1 - exp(-t/(RC))]`.

Reference values are R = 2 ohm and C = 0.4 F. Candidate R moves from 1 to 2 ohm while C stays fixed. At every frame the prediction is recomputed from that displayed R. Residual is prediction minus reference; MSE is mean squared residual over the same uniformly sampled 0–4 s interval, in V². The path is illustrative, not an optimization algorithm. It has no experiment or paper-performance claim.

The final objective plot uses the same reference, model, fixed C, and MSE. The RC example is silent and runs independently of the optional bundled reference narrator.
