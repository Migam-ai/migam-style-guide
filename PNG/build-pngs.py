"""Rasterise the SVG logo pack to transparent PNGs at 1x and 2x.

Sources: SVG/*.svg plus the three root logos. Output lands in PNG/ with the
same stem. 1x = the SVG's own viewBox size; @2x doubles it. Rendered with
headless Chromium (Playwright), same engine as the banner PNGs.
"""
import math, re, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT  = ROOT / "PNG"
OUT.mkdir(exist_ok=True)

SOURCES = sorted((ROOT / "SVG").glob("*.svg")) + [
    ROOT / "logo-migam-icon.svg",
    ROOT / "logo-migam-horizontal.svg",
    ROOT / "logo-migam-horizontal-white.svg",
]

def size(path):
    vb = re.search(r'viewBox="([^"]+)"', path.read_text(encoding="utf-8")).group(1)
    _, _, w, h = (float(v) for v in vb.replace(",", " ").split())
    return math.ceil(w), math.ceil(h)

with sync_playwright() as p:
    browser = p.chromium.launch()
    for src in SOURCES:
        w, h = size(src)
        for scale, suffix in ((1, ""), (2, "@2x")):
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
            page.goto(src.as_uri())
            dst = OUT / f"{src.stem}{suffix}.png"
            page.screenshot(path=str(dst), omit_background=True)
            page.close()
        print(f"{src.stem:45} {w}x{h}  ->  {w*2}x{h*2} @2x")
    browser.close()
