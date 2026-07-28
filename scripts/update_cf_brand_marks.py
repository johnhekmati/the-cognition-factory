"""Crop CF monogram from new hero banner → site icons + app launcher masters."""

from __future__ import annotations

import shutil
from pathlib import Path

import numpy as np
from PIL import Image

SITE_IMG = Path(r"C:\Grok\tcf-site\assets\images")
SITE_VID = Path(r"C:\Grok\tcf-site\assets\videos")
APP_BRAND = Path(r"C:\Grok\tcf-app\assets\branding")

SRC_BANNER = SITE_IMG / "cog-fac-hero-banner-new.jpg"
SRC_VIDEO = SITE_VID / "cog-fac-hero-video.mp4"


def monogram_square(src: Image.Image, pad: float = 1.28) -> Image.Image:
    a = np.array(src.convert("RGB"))
    mask = a.max(axis=2) > 18
    ys, xs = np.where(mask)
    if len(xs) == 0:
        # Full-frame center square fallback
        w, h = src.size
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        return src.crop((left, top, left + side, top + side))

    x0, x1 = int(xs.min()), int(xs.max())
    y0, y1 = int(ys.min()), int(ys.max())
    cw, ch = x1 - x0 + 1, y1 - y0 + 1
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2

    side = int(max(cw, ch) * pad)
    side += side % 2
    w, h = src.size
    side = min(side, w, h)

    left = max(0, min(cx - side // 2, w - side))
    top = max(0, min(cy - side // 2, h - side))
    right, bottom = left + side, top + side
    print(f"crop box=({left},{top},{right},{bottom}) side={side} content=({cw}x{ch})")
    return src.crop((left, top, right, bottom))


def make_square(crop: Image.Image, size: int, mode: str = "RGB") -> Image.Image:
    im = crop.resize((size, size), Image.Resampling.LANCZOS)
    return im.convert(mode)


def main() -> None:
    src = Image.open(SRC_BANNER).convert("RGB")
    crop = monogram_square(src)

    # Site icons / marks
    make_square(crop, 16, "RGBA").save(SITE_IMG / "favicon-16.png", "PNG", optimize=True)
    make_square(crop, 32, "RGBA").save(SITE_IMG / "favicon-32.png", "PNG", optimize=True)
    make_square(crop, 180, "RGBA").save(
        SITE_IMG / "apple-touch-icon.png", "PNG", optimize=True
    )
    make_square(crop, 256, "RGB").save(
        SITE_IMG / "tcf-mark-cf-nav.jpg", "JPEG", quality=92, optimize=True
    )
    make_square(crop, 1024, "RGBA").save(SITE_IMG / "tcf-mark-cf.png", "PNG", optimize=True)
    make_square(crop, 1200, "RGB").save(
        SITE_IMG / "tcf-mark-cf-og.jpg", "JPEG", quality=90, optimize=True
    )

    print("site icons written")
    for name in (
        "favicon-16.png",
        "favicon-32.png",
        "apple-touch-icon.png",
        "tcf-mark-cf-nav.jpg",
        "tcf-mark-cf.png",
        "tcf-mark-cf-og.jpg",
    ):
        p = SITE_IMG / name
        im = Image.open(p)
        print(f"  {name}: {im.size} {im.mode} {p.stat().st_size}b")

    # App launcher masters + hero stills/video
    mark_1024 = make_square(crop, 1024, "RGBA")
    mark_1024.save(APP_BRAND / "app_icon.png", "PNG", optimize=True)
    mark_1024.save(APP_BRAND / "app_icon_mark_only.png", "PNG", optimize=True)

    src.save(APP_BRAND / "tcf-hero-poster.jpg", "JPEG", quality=92, optimize=True)
    src.save(APP_BRAND / "tcf-hero.jpg", "JPEG", quality=92, optimize=True)
    src.save(APP_BRAND / "tcf-hero-site-match.jpg", "JPEG", quality=92, optimize=True)

    shutil.copy2(SRC_BANNER, APP_BRAND / "cog-fac-hero-banner-new.jpg")
    shutil.copy2(SRC_VIDEO, APP_BRAND / "cog-fac-hero-video.mp4")
    # Legacy motion path → new video
    shutil.copy2(SRC_VIDEO, APP_BRAND / "tcf-hero-motion.mp4")

    print("app branding refreshed")
    for name in (
        "app_icon.png",
        "app_icon_mark_only.png",
        "tcf-hero-poster.jpg",
        "tcf-hero-motion.mp4",
        "cog-fac-hero-video.mp4",
        "cog-fac-hero-banner-new.jpg",
    ):
        p = APP_BRAND / name
        print(f"  {name}: {p.stat().st_size}b")


if __name__ == "__main__":
    main()
