# nick-th-w.github.io

Personal CV site, published via GitHub Pages at https://nick-th-w.github.io/

## How to update

Everything is one file: `index.html` (plain HTML/CSS/JS, no build step). To change anything — a new role, an updated metric, a new case study — just edit the relevant text inside it.

**Quickest way (recommended):** open this folder in Claude Code and describe the change in plain English, e.g. "add my new role at X starting this month" or "update the ARR growth stat to 5x". Claude Code will edit `index.html` directly.

**Manual way:** edit `index.html` in any text editor, following the existing pattern for each section (`.tl-item` for a work history entry, `.case-card` for a case study, etc.).

Once you're happy with a change, publish it:

```bash
git add -A
git commit -m "describe the change"
git push
```

GitHub Pages redeploys automatically within a minute or two of the push landing on `main` — there's no separate build/deploy step.

## Structure

- `index.html` — the entire site (content, styles, and scripts in one file)
- `assets/headshot.jpg` — hero photo
- `assets/og-image.png` — social link-preview image (shown when the URL is shared on LinkedIn/Slack/etc.)
- `favicon.ico`, `assets/icon-*.png` — browser tab / home-screen icons
- `robots.txt`, `sitemap.xml` — search engine indexing
- `scripts/gen_images.py` — regenerates `og-image.png` and the favicons from brand colors if you ever want to tweak them (`python3 scripts/gen_images.py`)

## Analytics

Wired up for [GoatCounter](https://www.goatcounter.com) — free, privacy-friendly, no cookie banner needed. To activate it:

1. Sign up at goatcounter.com and create a site (pick any site code, e.g. `nick-th-w`).
2. In `index.html`, find the line near the bottom with `data-goatcounter="https://YOUR-CODE.goatcounter.com/count"` and replace `YOUR-CODE` with your actual site code.
3. Push. Visit stats any time at `https://YOUR-CODE.goatcounter.com`.

## Dark mode & mobile menu

Both are built in — a toggle button in the nav for dark mode (remembers your choice via `localStorage`), and a hamburger menu that appears on narrow screens.
