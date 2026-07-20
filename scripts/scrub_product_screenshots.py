"""
One-pass pixel scrub of product gallery screenshots.

Always starts from original Windows PNG captures — never from a previously
edited marketing JPG — so UI chrome stays sharp. Covers only scrub boxes and
redraws clean labels with Segoe UI (no generative image model).
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SRC = Path(r"C:\Users\theco\Pictures\Screenshots")
OUT = Path(r"C:\Grok\tcf-site\assets\images\product")

FONT_REG = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


def paint(
    im: Image.Image,
    box: tuple[int, int, int, int],
    text: str,
    *,
    size: int,
    bold: bool,
    fill: tuple[int, int, int],
    bg: tuple[int, int, int],
    y_nudge: int = 0,
    x_nudge: int = 0,
) -> None:
    """Solid cover then sharp redraw. No blur, no model."""
    draw = ImageDraw.Draw(im)
    draw.rectangle(box, fill=bg)
    fnt = font(size, bold=bold)
    draw.text((box[0] + x_nudge, box[1] + y_nudge), text, font=fnt, fill=fill)


# Top-right profile chip: keep people icon; replace display name only.
# Measured on 1919-wide W11 captures (2026-07-19): text ~x1195–1310.
NAME_CHIP_BG = (10, 15, 26)
NAME_CHIP_FILL = (168, 172, 180)  # muted bar label, close to native


def scrub_name_chip(im: Image.Image, *, y0: int = 11, y1: int = 36, x0: int = 1194, x1: int = 1314) -> None:
    """Replace top-bar display name with neutral 'Learner' (sharp one-pass)."""
    paint(
        im,
        (x0, y0, x1, y1),
        "Learner",
        size=13,
        bold=False,
        fill=NAME_CHIP_FILL,
        bg=NAME_CHIP_BG,
        y_nudge=1,
    )


def scrub_deep(im: Image.Image) -> Image.Image:
    scrub_name_chip(im, y0=12, y1=36)
    # Chat title only — tight box so subtitle below stays native
    paint(
        im,
        (1040, 63, 1145, 88),
        "Assistant",
        size=16,
        bold=True,
        fill=(236, 240, 245),
        bg=(11, 19, 26),
        y_nudge=0,
    )
    # Input placeholder
    paint(
        im,
        (1083, 968, 1225, 990),
        "Message Assistant...",
        size=13,
        bold=False,
        fill=(118, 132, 145),
        bg=(21, 32, 40),
        y_nudge=-1,
    )
    return im


def scrub_aae(im: Image.Image) -> Image.Image:
    scrub_name_chip(im, y0=10, y1=33)
    # Full helper line redraw (avoids partial-word surgery)
    paint(
        im,
        (112, 417, 752, 448),
        "Load course materials into Assistant, then mark Correct or Incorrect as you practice. Miss = you skipped or",
        size=11,
        bold=False,
        fill=(168, 150, 105),
        bg=(58, 46, 28),
        y_nudge=3,
    )
    # Library pill title only (keep "17 courses" line below intact)
    paint(
        im,
        (126, 534, 262, 556),
        "Accounting",
        size=13,
        bold=True,
        fill=(220, 225, 235),
        bg=(13, 18, 32),
        y_nudge=1,
    )
    return im


def scrub_save(im: Image.Image) -> Image.Image:
    scrub_name_chip(im, y0=7, y1=30)
    paint(
        im,
        (1040, 58, 1145, 83),
        "Assistant",
        size=16,
        bold=True,
        fill=(236, 240, 245),
        bg=(12, 14, 28),
        y_nudge=0,
    )
    paint(
        im,
        (1123, 960, 1265, 984),
        "Message Assistant...",
        size=13,
        bold=False,
        fill=(145, 135, 175),
        bg=(22, 18, 36),
        y_nudge=-1,
    )
    return im


def scrub_help(im: Image.Image) -> Image.Image:
    # Help capture: name chip slightly left / shorter
    scrub_name_chip(im, y0=9, y1=28, x0=1174, x1=1294)
    # Full step-4 line (y ~900 on original)
    paint(
        im,
        (410, 898, 820, 922),
        "4. Talk with Assistant in the side panel (sparkles button)",
        size=14,
        bold=False,
        fill=(196, 200, 206),
        bg=(13, 18, 32),
        y_nudge=0,
    )
    return im


JOBS = [
    ("Screenshot 2026-07-19 200002.png", "tcf-desktop-app-mockup.jpg", scrub_deep),
    ("Screenshot 2026-07-19 200406.png", "tcf-practice-aae-screenshot.jpg", scrub_aae),
    ("Screenshot 2026-07-19 200524.png", "tcf-save-place-screenshot.jpg", scrub_save),
    ("Screenshot 2026-07-19 200740.png", "tcf-settings-help-screenshot.jpg", scrub_help),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_name, out_name, scrub in JOBS:
        src = SRC / src_name
        im = Image.open(src).convert("RGBA")
        base = Image.new("RGB", im.size, (5, 8, 16))
        base.paste(im, mask=im.split()[-1])
        scrubbed = scrub(base)
        out = OUT / out_name
        # High-quality JPEG, no chroma subsampling (keeps UI edges clean)
        scrubbed.save(out, "JPEG", quality=95, optimize=True, subsampling=0)
        print(f"OK {src_name} -> {out_name} {scrubbed.size}")


if __name__ == "__main__":
    main()
