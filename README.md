# Migam Style Guide

The official visual language for **Migam** — colors, typography, components, and tone of
voice — packaged as **drop-in files for AI agents** that build Migam's internal apps and
presentations. Extracted from [migam.org](https://migam.org/) (homepage + subpages).

### 📖 Live style book → **https://migam-ai.github.io/migam-style-guide/**

Interactive reference with the live palette, type specimens in the real fonts, components,
voice examples, and one-click downloads of every file below.

---

## Files

| File | What it is |
|---|---|
| [`MIGAM_STYLE_GUIDE.md`](./MIGAM_STYLE_GUIDE.md) | **The main file.** Full guide: tokens, copy-paste components, type scale, voice & tone, do/don't. Paste this into an agent's context. |
| [`migam-tokens.css`](./migam-tokens.css) | CSS custom properties — import at your app root. |
| [`migam-tokens.json`](./migam-tokens.json) | Design tokens as JSON — for build pipelines / theme generators. |
| [`logo-migam-icon.svg`](./logo-migam-icon.svg) | **The Migam mark.** Drop into apps, decks, and docs as-is. Usage rules (clear space, min size, don'ts) in §1.1 of the guide. |
| [`migam-favicons/`](./migam-favicons/) | Favicon + app-icon set (`.ico`, square `.svg`, apple-touch, PWA 192/512, maskable, `site.webmanifest`). Copy to your app's web root — see §1.2. |

## Use it with an AI agent

**Option A — paste:** copy the contents of `MIGAM_STYLE_GUIDE.md` into the agent's system
prompt (or your `AGENTS.md` / `CLAUDE.md`).

**Option B — fetch the raw URL at runtime:**

```
https://raw.githubusercontent.com/Migam-ai/migam-style-guide/main/MIGAM_STYLE_GUIDE.md
https://raw.githubusercontent.com/Migam-ai/migam-style-guide/main/migam-tokens.css
https://raw.githubusercontent.com/Migam-ai/migam-style-guide/main/migam-tokens.json
https://raw.githubusercontent.com/Migam-ai/migam-style-guide/main/logo-migam-icon.svg
```

## At a glance

- **Logo:** `logo-migam-icon.svg` — use as-is, never recolored; its gradients are logo-only.
- **Icons:** `migam-favicons/` — favicon, apple-touch, PWA + maskable, manifest. Ready to ship.
- **Brand color:** teal `#0F6B68` on white / soft-mint backgrounds.
- **Accent:** orange `#EE7F2B` — primary CTA only, with dark text `#2B1503`.
- **Type:** Figtree (headings) + Hanken Grotesk (body), latin-ext subset for Polish.
- **Shape:** pill buttons (`radius: 999px`), rounded cards, teal-tinted shadows.
- **Voice:** direct, second-person, benefit-first, plain Polish. Accessibility is the ethic.
- **State colors:** error `#B3261E`, success `#2E9E63`.

## Notes

- Source of truth is the marketing site, [migam.org](https://migam.org/) — reflects what's
  shipping, not a formal brand manual. If an official brand book exists, reconcile against it.
- The flag colors on the site (`#C8102E`, `#012169`, …) belong to the **language switcher**
  only — they are **not** brand colors.
- Scope is migam.org. The product apps (`migam.ai`, `saas.migam.org`) may carry their own
  identity; audit separately before reusing this there.

## License

Proprietary — **internal Migam use only.** See [`LICENSE`](./LICENSE). Free to use and adapt
for Migam products, apps, and presentations; not for redistribution or use outside Migam.
