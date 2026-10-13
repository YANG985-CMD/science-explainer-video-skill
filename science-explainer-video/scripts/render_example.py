"""Silent original RC-response demonstration. All illustrated data are synthetic."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from glow_canvas import (Canvas, W, H, WHITE, CYAN, GOLD, PINK, MUTED,
                         FAINT, clamp, ease, encode_frames)

TIME = np.linspace(0.0, 4.0, 241)
STEP_V = 5.0
CAPACITANCE_F = 0.4
REFERENCE_R_OHM = 2.0


def response(r_ohm):
    return STEP_V * (1 - np.exp(-TIME / (r_ohm * CAPACITANCE_F)))


REFERENCE = response(REFERENCE_R_OHM)


def state(progress):
    # A narrated illustrative movement, not an invented optimization benchmark.
    r = 1.0 + ease((progress - 0.35) / 0.35)
    prediction = response(r)
    residual = prediction - REFERENCE
    return {"r": r, "prediction": prediction, "residual": residual,
            "mse": float(np.mean(residual ** 2))}


def points(values, rect, x_max=4.0, y_max=5.0):
    x, y, width, height = rect
    return list(zip(x + TIME / x_max * width, y + height - values / y_max * height))


def draw_frame(progress, args):
    data = state(progress)
    canvas = Canvas(args.font)
    canvas.text((80, 50), "SCIENCE / CONTINUOUS CAUSAL ANIMATION", 24, MUTED)
    canvas.text((1840, 50), "COMPUTED PRINCIPLE ILLUSTRATION", 22, MUTED, "ra")
    if progress < 0.22:
        heading = "Why do the two responses differ?"
        caption = [("Keep the ", WHITE), ("reference", WHITE),
                   (". Add a model with a candidate ", WHITE), ("resistance", PINK),
                   (".", WHITE)]
    elif progress < 0.35:
        heading = "Compare the same instant on both curves"
        caption = [("The ", WHITE), ("residual", GOLD),
                   (" is prediction minus reference at the same time.", WHITE)]
    elif progress < 0.70:
        heading = "Change resistance; recompute the response"
        caption = [("Changing ", WHITE), ("R", PINK),
                   (" changes the ", WHITE), ("prediction", CYAN),
                   (" and its ", WHITE), ("mean squared error", GOLD), (".", WHITE)]
    else:
        heading = "The same candidate becomes a point on the objective"
        caption = [("The ", WHITE), ("same model and reference", CYAN),
                   (" define every candidate's ", WHITE), ("error", GOLD), (".", WHITE)]
    canvas.text((W / 2, 145), heading, 42, WHITE, "mm")
    canvas.text((W / 2, 225), "5 V step  |  C = 0.4 F, fixed  |  Initially uncharged",
                27, MUTED, "mm")

    # Keep both curves and all time positions as the plot moves and scales.
    shrink = ease((progress - 0.70) / 0.16)
    large = np.array([185, 320, 1260, 405], dtype=float)
    small = np.array([155, 355, 780, 340], dtype=float)
    rect = large * (1 - shrink) + small * shrink
    x, y, width, height = rect
    canvas.line([(x, y), (x, y + height), (x + width, y + height)],
                FAINT, 1, glow=False)
    canvas.text((x - 20, y - 25), "v / V", 26, MUTED, "rm")
    for value in [0, 1, 2, 3, 4]:
        xx = x + value / 4 * width
        canvas.text((xx, y + height + 30), str(value), 24, MUTED, "mm")
    canvas.text((x + width + 20, y + height + 30), "s", 24, MUTED)
    for value in [0, 1, 2, 3, 4, 5]:
        canvas.text((x - 20, y + height - value / 5 * height),
                    str(value), 24, MUTED, "rm")
    reference_points = points(REFERENCE, rect)
    prediction_points = points(data["prediction"], rect)
    reveal = max(2, round(len(TIME) * ease(progress / 0.17)))
    canvas.line(reference_points[:reveal], WHITE, 3)
    canvas.line(prediction_points[:reveal], CYAN, 3)
    residual_opacity = ease((progress - 0.17) / 0.1)
    for index in range(0, reveal, 12):
        canvas.line([reference_points[index], prediction_points[index]],
                    GOLD, 2, residual_opacity * 0.45)
    if progress >= 0.17:
        index = min(len(TIME) - 1, round(clamp((progress - 0.17) / 0.55) * 240))
        xx = reference_points[index][0]
        canvas.line([(xx, y), (xx, y + height)], MUTED, 1, 0.3)
        canvas.line([reference_points[index], prediction_points[index]], GOLD, 4)
        canvas.dot(reference_points[index], WHITE)
        canvas.dot(prediction_points[index], CYAN)
    canvas.text((x + width * 0.58, y + height * 0.78), "reference", 26, WHITE)
    canvas.text((x + width * 0.58, y + height * 0.89), "prediction", 26, CYAN)

    if shrink < 1:
        canvas.ring((1660, 465), 90, FAINT, 1 - shrink)
        canvas.text((1660, 455), f'{data["mse"]:.4f}', 40, GOLD, "mm", 1 - shrink)
        canvas.text((1660, 502), "V^2", 25, MUTED, "mm", 1 - shrink)
        canvas.text((1660, 595), "Mean squared error", 27, GOLD, "mm", 1 - shrink)
    if shrink > 0:
        r_values = np.linspace(0.8, 3.2, 101)
        errors = np.mean((STEP_V * (1 - np.exp(-TIME[None, :] /
                         (r_values[:, None] * CAPACITANCE_F))) - REFERENCE) ** 2, axis=1)
        xmax, ymax, pw, ph = 1120, 700, 620, 330
        top = max(errors) * 1.05
        objective_points = list(zip(xmax + (r_values - 0.8) / 2.4 * pw,
                                    ymax - errors / top * ph))
        canvas.line([(xmax, ymax - ph), (xmax, ymax), (xmax + pw, ymax)],
                    FAINT, 1, shrink, glow=False)
        canvas.line(objective_points, GOLD, 3, shrink)
        candidate = (xmax + (data["r"] - 0.8) / 2.4 * pw,
                     ymax - data["mse"] / top * ph)
        canvas.dot(candidate, CYAN, 7, shrink)
        canvas.text((candidate[0] + 20, candidate[1] - 35), "same candidate", 25,
                    CYAN, opacity=shrink)
        canvas.text((xmax, ymax - ph - 45), "MSE / V^2", 26, GOLD, opacity=shrink)
        canvas.text((xmax + pw / 2, ymax + 66), "candidate R / ohm", 26, PINK,
                    "mm", shrink)
        for r_value in [1, 2, 3]:
            xx = xmax + (r_value - 0.8) / 2.4 * pw
            canvas.text((xx, ymax + 27), str(r_value), 22, MUTED, "mm", shrink)
    canvas.text((W / 2, 840), f'Candidate R = {data["r"]:.3f} ohm', 34, PINK, "mm")
    canvas.text((W / 2, 892), "Analytic RC step response; illustrative parameter path",
                23, MUTED, "mm")
    canvas.caption(caption, 32)
    canvas.text((80, 1040), "Synthetic data / no experimental or paper-performance claim",
                20, MUTED)
    canvas.text((1840, 1040), "NORMAL SPEED / SILENT EXAMPLE", 20, MUTED, "ra")
    canvas.line([(80, 1062), (1840, 1062)], FAINT, 2, glow=False)
    canvas.line([(80, 1062), (80 + 1760 * progress, 1062)], CYAN, 2, glow=False)
    return canvas.finish(args.width, args.height)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--ffmpeg", default="ffmpeg")
    parser.add_argument("--font")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--duration", type=float, default=12.0)
    parser.add_argument("--preview-only", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if not math.isfinite(args.duration) or args.duration <= 0 or args.fps <= 0:
        parser.error("duration and fps must be positive")
    if (args.width <= 0 or args.height <= 0 or args.width % 2 or args.height % 2
            or args.width * 9 != args.height * 16):
        parser.error("this landscape example requires positive even 16:9 dimensions")
    args.work_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for p in [0.12, 0.28, 0.51, 0.79, 0.95]:
        filename = f"preview_{round(p * 100):02d}.png"
        draw_frame(p, args).save(args.work_dir / filename)
        data = state(p)
        records.append({"progress": p, "resistance_ohm": data["r"],
                        "mse_v_squared": data["mse"], "frame": filename})
    (args.work_dir / "model-record.json").write_text(json.dumps({
        "model": "ideal RC capacitor step response, v(0)=0",
        "step_voltage_v": STEP_V, "fixed_capacitance_f": CAPACITANCE_F,
        "reference_resistance_ohm": REFERENCE_R_OHM,
        "time_interval_s": [0, 4], "sample_count": len(TIME),
        "evidence_type": "computed principle illustration", "states": records,
    }, indent=2), encoding="utf-8")
    if args.preview_only:
        print(f"Preview and model record written to {args.work_dir}")
        return
    frame_count = max(2, math.ceil(args.duration * args.fps))
    frames = (draw_frame(j / (frame_count - 1), args) for j in range(frame_count))
    encode_frames(frames, args.output, args.ffmpeg, args.width, args.height,
                  args.fps, args.work_dir / "encode.log", args.overwrite)
    print(f"Encoded {frame_count} frames to {args.output}")


if __name__ == "__main__":
    main()
