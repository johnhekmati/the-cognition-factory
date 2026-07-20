"""
One-pass pixel scrub for Android product gallery screenshots.
Source: mobile-app-feedback/screenshots. Always originals → product/*.jpg.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SRC = Path(r"C:\Users\theco\Downloads\mobile-app-feedback\screenshots")
OUT = Path(r"C:\Grok\tcf-site\assets\images\product")
FONT = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT), size)


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
) -> None:
    draw = ImageDraw.Draw(im)
    draw.rectangle(box, fill=bg)
    draw.text((box[0], box[1] + y_nudge), text, font=font(size, bold), fill=fill)


def scrub_chat(im: Image.Image) -> Image.Image:
    # Header title "Grok" only (avatar circle left of ~x250 stays)
    paint(
        im,
        (248, 158, 380, 212),
        "Assistant",
        size=32,
        bold=True,
        fill=(245, 248, 250),
        bg=(10, 19, 26),
        y_nudge=6,
    )
    # Full placeholder inside the input pill (text band ~y2180–2220)
    paint(
        im,
        (248, 2175, 655, 2225),
        "Message Assistant...",
        size=24,
        bold=False,
        fill=(110, 120, 130),
        bg=(22, 32, 41),
        y_nudge=6,
    )
    return im


JOBS = [
    # No scrub needed — clean marketing surfaces
    ("10362.jpg", "tcf-android-deep.jpg", None),
    ("10366.jpg", "tcf-android-practice.jpg", None),
    ("10369.jpg", "tcf-android-save.jpg", None),
    ("10371.jpg", "tcf-android-shell.jpg", None),
    ("10364.jpg", "tcf-android-chat.jpg", scrub_chat),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_name, out_name, scrub in JOBS:
        im = Image.open(SRC / src_name).convert("RGB")
        if scrub:
            im = scrub(im)
        out = OUT / out_name
        im.save(out, "JPEG", quality=92, optimize=True, subsampling=0)
        print(f"OK {src_name} -> {out_name} {im.size}")


if __name__ == "__main__":
    main()
