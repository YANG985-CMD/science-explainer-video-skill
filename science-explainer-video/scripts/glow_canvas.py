"""Small original Pillow helpers for continuous science animation.

Coordinates use a logical 1920 x 1080 canvas. Dependencies: Pillow.
No media, fonts, audio profiles, or model weights are bundled.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
import math
import subprocess
from typing import Iterable, Sequence

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
BG = (5, 11, 15)
WHITE = (235, 243, 239)
CYAN = (89, 221, 220)
GOLD = (255, 210, 120)
PINK = (232, 139, 167)
PURPLE = (177, 162, 244)
MUTED = (130, 156, 168)
FAINT = (38, 65, 76)
CAPTION_TOP = 934


def clamp(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def ease(value: float) -> float:
    p = clamp(value)
    return p * p * (3.0 - 2.0 * p)


def blend_color(color: Sequence[int], opacity: float) -> tuple[int, int, int]:
    p = clamp(opacity)
    return tuple(round(BG[k] + (color[k] - BG[k]) * p) for k in range(3))


@lru_cache(maxsize=48)
def load_font(path: str | None, size: int) -> ImageFont.FreeTypeFont:
    if path:
        return ImageFont.truetype(path, size)
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError as exc:
        raise ValueError("Provide --font with a font covering your displayed text.") from exc


class Canvas:
    """Crisp primitives with a separate low-resolution glow layer."""

    def __init__(self, font_path: str | None = None):
        self.font_path = font_path
        self.image = Image.new("RGB", (W, H), BG)
        self.draw = ImageDraw.Draw(self.image)
        self.glow = Image.new("RGB", (W // 2, H // 2))
        self.glow_draw = ImageDraw.Draw(self.glow)

    def text(self, xy, text, size=28, color=WHITE, anchor=None, opacity=1.0):
        self.draw.text(xy, text, font=load_font(self.font_path, size),
                       fill=blend_color(color, opacity), anchor=anchor)

    def line(self, points, color=CYAN, width=3, opacity=1.0, glow=True):
        points = [(float(x), float(y)) for x, y in points]
        if len(points) < 2:
            return
        self.draw.line(points, fill=blend_color(color, opacity), width=width,
                       joint="curve")
        if glow:
            self.glow_draw.line([(x / 2, y / 2) for x, y in points],
                                fill=tuple(round(v * clamp(opacity) * 0.65)
                                           for v in color),
                                width=max(1, width // 2 + 1), joint="curve")

    def dot(self, xy, color=WHITE, radius=5, opacity=1.0):
        x, y = xy
        self.draw.ellipse((x - radius, y - radius, x + radius, y + radius),
                          fill=blend_color(color, opacity))
        self.glow_draw.ellipse(((x - 2 * radius) / 2, (y - 2 * radius) / 2,
                                (x + 2 * radius) / 2, (y + 2 * radius) / 2),
                               fill=tuple(round(v * clamp(opacity) * 0.7)
                                          for v in color))

    def ring(self, xy, radius=65, color=FAINT, opacity=1.0):
        points = [(xy[0] + radius * math.cos(a),
                   xy[1] + radius * math.sin(a))
                  for a in [2 * math.pi * j / 80 for j in range(81)]]
        self.line(points, color, 2, opacity, glow=False)

    def caption(self, runs: Sequence[tuple[str, Sequence[int]]], size=35):
        """One measured line, physically separated from scientific content."""
        font = load_font(self.font_path, size)
        length = sum(font.getlength(text) for text, _ in runs)
        if length > W - 160:
            raise ValueError("Caption exceeds safe width; split the spoken phrase.")
        self.draw.rectangle((0, CAPTION_TOP, W, H), fill=BG)
        x = (W - length) / 2
        for text, color in runs:
            self.text((x, 978), text, size, color, "lm")
            x += font.getlength(text)

    def finish(self, width=W, height=H):
        broad = self.glow.filter(ImageFilter.GaussianBlur(7)).resize(
            (W, H), Image.Resampling.BILINEAR)
        narrow = self.glow.filter(ImageFilter.GaussianBlur(1.4)).resize(
            (W, H), Image.Resampling.BILINEAR)
        image = ImageChops.screen(ImageChops.screen(self.image, broad), narrow)
        # Nothing in the content layer may bleed into the reserved caption band.
        image.paste(self.image.crop((0, CAPTION_TOP, W, H)), (0, CAPTION_TOP))
        if (width, height) != (W, H):
            image = image.resize((width, height), Image.Resampling.LANCZOS)
        return image


def encode_frames(frames: Iterable[Image.Image], output: Path, ffmpeg: str,
                  width: int, height: int, fps: int, log_path: Path,
                  overwrite=False):
    """Encode RGB frames without a shell; the caller owns media validation."""
    if width <= 0 or height <= 0 or width % 2 or height % 2 or fps <= 0:
        raise ValueError("H.264 dimensions must be positive even integers; fps > 0.")
    output = Path(output)
    log_path = Path(log_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    command = [ffmpeg, "-y" if overwrite else "-n", "-hide_banner",
               "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{width}x{height}",
               "-r", str(fps), "-i", "pipe:0", "-an", "-c:v", "libx264",
               "-threads", "2", "-preset", "fast", "-crf", "19",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output)]
    with log_path.open("wb") as log:
        process = subprocess.Popen(command, stdin=subprocess.PIPE,
                                   stdout=log, stderr=log)
        try:
            for frame in frames:
                if frame.size != (width, height):
                    raise ValueError("Frame dimensions differ from encoder settings.")
                process.stdin.write(frame.convert("RGB").tobytes())
            process.stdin.close()
            return_code = process.wait()
        except Exception as exc:
            process.kill()
            process.wait()
            if isinstance(exc, BrokenPipeError):
                raise RuntimeError(log_path.read_text(errors="replace")[-2000:]) from exc
            raise
    if return_code:
        raise RuntimeError(log_path.read_text(errors="replace")[-2000:])
