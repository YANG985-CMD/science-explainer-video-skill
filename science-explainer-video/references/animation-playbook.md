# Storyboard and evidence playbook

Read this when deciding what should move and how one explanation should lead into another.

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

Set the operation's timing from the recorded sentence. For multi-step narration, use separate beats for selecting an interval, measuring the discrepancy, aggregating it, and applying an update. A single normalized progress number suffices for a short demo; a full video usually needs action timestamps.

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

## Caption and audio review

### Audience-facing text and provenance

Display text that explains the science or its basis. Do not put production-status strings such as “理想原理计算示意·正常速度·已确认男声”, “已确认音色”, or rendering/version details on the cover, in a persistent footer, in subtitles, or on the end card. Playback speed and voice selection belong in delivery notes if needed.

Useful provenance may remain, for example “依据：理想两电平逆变器模型计算” or a paper's author, year, and figure number. State relevant assumptions or mark a specific numerical example as calculated when that prevents it being mistaken for a measurement. Use a concise source note near the relevant scene rather than a generic production banner. Check these areas in the actual encoded frames before delivery.

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
