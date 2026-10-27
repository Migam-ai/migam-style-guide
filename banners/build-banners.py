"""Build Migam social banners from the canonical SVG assets.

Layout: white field, horizontal lockup with the sign-language symbol directly
to its right, the pair centred in the area the profile picture does not cover.
Nothing else: no enclosing shape behind the symbol, no rule, no tint.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT  = ROOT / "banners"
OUT.mkdir(exist_ok=True)

def inner(path):
    s = path.read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    body = re.sub(r'^.*?<svg[^>]*>', '', s, flags=re.S)
    body = re.sub(r'</svg>\s*$', '', body, flags=re.S)
    body = re.sub(r'<title>.*?</title>', '', body, flags=re.S)
    body = re.sub(r'<desc>.*?</desc>', '', body, flags=re.S)
    return vb, body.strip()

SIGN_VB, SIGN = inner(ROOT / "SVG" / "migam-sign-language-gradient.svg")
OUTL_VB, OUTL = inner(ROOT / "SVG" / "migam-logo-horizontal-white-outline.svg")
FULL_VB, FULL = inner(ROOT / "SVG" / "migam-logo-horizontal-fullcolor.svg")

# The shipped keyline is stroke-width 2 on a 2316-unit artboard: under half a
# pixel once the lockup is scaled into a banner. Thicken it so it reads on white.
OUTL_BANNER = OUTL.replace('stroke-width="2"', 'stroke-width="9"')

LOGO_AR = 2316.31 / 756.95   # 3.06
SIGN_AR = 512 / 429          # 1.19
SIGN_REL = 0.85              # symbol height as a fraction of lockup height
GAP_REL  = 0.45              # gap between lockup and symbol, as a fraction of symbol width

# avatar_clear = left strip the platform's profile picture overlaps.
SIZES = [
    # key,                 W,    H,   logo w frac, pad frac, avatar clear
    ("linkedin-profile",  1584,  396, 0.245, 0.055, 0.20),
    ("linkedin-company",  1128,  191, 0.235, 0.050, 0.18),
    ("x-header",          1500,  500, 0.260, 0.060, 0.17),
    ("facebook-cover",    1640,  664, 0.260, 0.060, 0.16),
]

TPL = """<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Migam">
  <title>Migam — {key} banner</title>
  <rect width="{W}" height="{H}" fill="#FFFFFF"/>

  <!-- horizontal lockup -->
  <svg x="{lx:.1f}" y="{ly:.1f}" width="{lw:.1f}" height="{lh:.1f}" viewBox="{LOGO_VB}" preserveAspectRatio="xMidYMid meet" overflow="visible">
{LOGO}
  </svg>

  <!-- sign-language symbol, set beside the lockup; no enclosure -->
  <svg x="{sx:.1f}" y="{sy:.1f}" width="{sw:.1f}" height="{sh:.1f}" viewBox="{SIGN_VB}" preserveAspectRatio="xMidYMid meet" overflow="visible">
{SIGN}
  </svg>
</svg>
"""

VARIANTS = {"outline": (OUTL_VB, OUTL_BANNER), "fullcolor": (FULL_VB, FULL)}

for key, W, H, lwf, padf, avf in SIZES:
    pad = W * padf

    lw = W * lwf
    lh = lw / LOGO_AR
    sh = lh * SIGN_REL
    sw = sh * SIGN_AR

    gap = sw * GAP_REL

    # centre lockup + symbol in the area the profile picture does not cover
    cluster = lw + gap + sw
    free_l, free_r = W * avf, W - pad
    lx = free_l + (free_r - free_l - cluster) / 2
    sx = lx + lw + gap
    ly = (H - lh) / 2
    sy = (H - sh) / 2

    assert sw >= 48, f"{key}: symbol {sw:.0f}px wide, below the 48px minimum"
    assert gap > sw * 0.10, f"{key}: symbol clear space violated"

    for vname, (vb, logo) in VARIANTS.items():
        svg = TPL.format(W=W, H=H, key=key, SIGN_VB=SIGN_VB, SIGN=SIGN, LOGO_VB=vb, LOGO=logo,
                         lx=lx, ly=ly, lw=lw, lh=lh, sx=sx, sy=sy, sw=sw, sh=sh)
        (OUT / f"migam-banner-{key}-{W}x{H}-{vname}.svg").write_text(svg, encoding="utf-8")
    print(f"{key:20} lockup {lw:.0f}x{lh:.0f}  symbol {sw:.0f}x{sh:.0f}")
