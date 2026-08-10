#!/usr/bin/env python3
"""
render.py — render an HTML carousel to 1080x1350 PNGs with headless Chrome.

Usage:
  python3 render.py slides.html            # -> slides-01.png, slides-02.png, ...
  python3 render.py slides.html --out dir/

The HTML file contains all slides as .slide elements; each render pass opens the
file with ?slide=N and the page's JS displays only that slide (see slide template).

Chrome/Chromium is auto-detected; override with CHROME=/path/to/chrome.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys

CHROME_CANDIDATES = [
    os.environ.get("CHROME"),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/opt/pw-browsers/chromium",
    shutil.which("chromium"),
    shutil.which("google-chrome"),
    shutil.which("chromium-browser"),
]


def chrome_bin():
    for c in CHROME_CANDIDATES:
        if c and os.path.exists(c):
            return c
    sys.exit("Chrome/Chromium not found — set CHROME=/path/to/chrome")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--out", default=".", help="output directory")
    args = ap.parse_args()

    with open(args.html) as f:
        html = f.read()
    # Each slide may declare data-span="N" (one composition sliced across N
    # consecutive pages) and/or a format class instead of the default 4:5
    # carousel page (1080x1350): "reel" (9:16, 1080x1920), "yt" (16:9,
    # 1920x1080 video frame), "card" (6x4in postcard at 300dpi, 1800x1200), or
    # "banner" (YouTube channel art, 2560x1440 — safe area is the center
    # 1546x423), or "thumb" (YouTube video thumbnail, 1280x720).
    slides = []
    for m in re.finditer(r'<div class="slide([^"]*)"([^>]*)>', html):
        sp = re.search(r'data-span="(\d+)"', m.group(2))
        w, h = 1080, 1350
        if re.search(r'\breel\b', m.group(1)):
            w, h = 1080, 1920
        elif re.search(r'\byt\b', m.group(1)):
            w, h = 1920, 1080
        elif re.search(r'\bcard\b', m.group(1)):
            w, h = 1800, 1200
        elif re.search(r'\bbanner\b', m.group(1)):
            w, h = 2560, 1440
        elif re.search(r'\bthumb\b', m.group(1)):
            w, h = 1280, 720
        slides.append((int(sp.group(1)) if sp else 1, w, h))
    if not slides:
        sys.exit("No .slide elements found")

    os.makedirs(args.out, exist_ok=True)
    base = os.path.splitext(os.path.basename(args.html))[0]
    src = os.path.abspath(args.html)
    chrome = chrome_bin()

    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow not installed. Run: pip install pillow")

    # Render taller (and, for spans, wider) than the slide, then crop to exact
    # 1080x1350 pages — headless Chrome's viewport doesn't reliably equal
    # --window-size, and span slides are sliced into seamless adjacent frames.
    page = 0
    for i, (span, w, h) in enumerate(slides, 1):
        shot = os.path.join(args.out, f"_shot-{i:02d}.png")
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--window-size={w * span},{h + 150}", f"--screenshot={shot}",
                        "--virtual-time-budget=2000",
                        f"file://{src}?slide={i}"],
                       check=True, capture_output=True)
        img = Image.open(shot)
        for k in range(span):
            page += 1
            out = os.path.join(args.out, f"{base}-{page:02d}.png")
            img.crop((k * w, 0, (k + 1) * w, h)).save(out)
            print(f"  {out}  ({w}x{h}" + (f", span {k + 1}/{span})" if span > 1 else ")"))
        os.remove(shot)
    print(f"{len(slides)} compositions -> {page} pages")


if __name__ == "__main__":
    main()
