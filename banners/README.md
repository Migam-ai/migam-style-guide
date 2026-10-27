# Profile banners

White-background social banners built from two canonical assets:

- `SVG/migam-logo-horizontal-white-outline.svg` (outline variant) or
  `SVG/migam-logo-horizontal-fullcolor.svg` (fullcolor variant)
- `SVG/migam-sign-language-gradient.svg`

Layout: pure white field, horizontal lockup with the sign-language symbol
directly to its right, the pair centred in the area a platform's profile
picture does not cover (it overlaps the bottom-left of every banner below).
Nothing else — no enclosing shape behind the symbol, no rule, no tint.

The symbol is set at 85% of the lockup height. The build asserts it stays
above the 48 px minimum width and keeps its clear space at every size.

## Sizes

| File stem | Size | Symbol | Use |
|---|---|---|---|
| `migam-banner-linkedin-profile-1584x396` | 1584 × 396 | 129 px | LinkedIn personal profile background |
| `migam-banner-linkedin-company-1128x191` | 1128 × 191 | 88 px | LinkedIn company page cover |
| `migam-banner-x-header-1500x500` | 1500 × 500 | 129 px | X / Twitter header |
| `migam-banner-facebook-cover-1640x664` | 1640 × 664 | 141 px | Facebook page cover |

Each comes as `.svg`, `.png` (1×) and `@2x.png`, in two variants:

- **`-outline`** — white wordmark with a black keyline, as requested. The source
  keyline is `stroke-width="2"` on a 2316-unit artboard, which scales to well
  under half a pixel in a banner, so the build thickens it to `9` to keep the
  letterforms visible on white. Use when you want the lighter, outlined look.
- **`-fullcolor`** — same layout with the solid black wordmark. Higher contrast;
  safer default for small renderings and for LinkedIn's mobile crop.

## Rebuilding

```
python banners/build-banners.py   # regenerates the SVGs from SVG/
```

Knobs at the top: `SIGN_REL` (symbol size relative to the lockup), `GAP_REL`
(space between lockup and symbol, relative to symbol width), and the per-size
fractions in `SIZES` for lockup width, edge padding and profile-picture
clearance. PNGs were rasterised with headless Chrome at 1× and 2×.
