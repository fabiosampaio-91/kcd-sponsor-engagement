<div align="center">

# 🖥️ synvert xgeeks · Presentations

**A multi-presentation repo — every folder is one self-contained slide deck, served via GitHub Pages.**

[![Live](https://img.shields.io/badge/live-github_pages-00EBB6?style=flat-square)](https://fabiosampaio-91.github.io/xgeeks-presentations/)
[![Build](https://img.shields.io/badge/build-none_·_static_html-002E33?style=flat-square)](#-how-it-works)
[![Brand](https://img.shields.io/badge/brand-techno_green-00EBB6?style=flat-square)](#-design-systems)

[**▶ Open the gallery**](https://fabiosampaio-91.github.io/xgeeks-presentations/)

</div>

---

## 🎞️ Presentations

> **Adding a deck?** Add one row below, keep it alphabetical by folder. Row format:
> `| [Title](folder/) | description | slides · occasion | [deck](https://.../folder/) · [analysis](https://.../folder/analysis.html) |`

| Deck | What it is | Size | Live |
|---|---|---|---|
| [**KCD Porto · A Strategic Asset**](kcd-porto-strategic/) | The leadership case for KCD Porto 2026: how synvert xgeeks turned Iberia's #1 Cloud Native + DevOps event into a positioning engine, BD channel, talent magnet, and brand amplifier. | 12 slides · KCD Porto 2026 | [deck](https://fabiosampaio-91.github.io/xgeeks-presentations/kcd-porto-strategic/) · [analysis](https://fabiosampaio-91.github.io/xgeeks-presentations/kcd-porto-strategic/analysis.html) |
| [**KCD → Pipeline**](kcd-sponsor-engagement/) | Turning KCD sponsor relationships into engineering pipeline — a dual-track, many-doors, vendor-neutral BD plan anchored to KCD Porto 2026. | 18 slides · KCD Porto 2026 | [deck](https://fabiosampaio-91.github.io/xgeeks-presentations/kcd-sponsor-engagement/) · [analysis](https://fabiosampaio-91.github.io/xgeeks-presentations/kcd-sponsor-engagement/analysis.html) |
<!-- NEW DECK ROW GOES HERE — copy the format from the note above -->

---

## ✨ How it works

Pure **static site — no build step, no dependencies, no `package.json`, no framework.** Hand-written
HTML/CSS/vanilla JS. Edit a file, commit, push — that's the whole pipeline. GitHub Pages
([`.github/workflows/pages.yml`](.github/workflows/pages.yml)) uploads the repo root verbatim on every
push to `main`, so `<folder>/` is live at `https://fabiosampaio-91.github.io/xgeeks-presentations/<folder>/`.

Every presentation ships **two self-contained files** that cross-link to each other:

| File | What it is |
|---|---|
| `index.html` | The **slide deck** — dark, full-viewport scroll-snap slides, keyboard nav. |
| `analysis.html` | The **long-form document view** — light/dark, sticky-TOC; argues the full case behind the deck. |

---

## 🗂️ Repo layout

```
_template/                  Blank deck — copy to start a new presentation
  index.html                  Blank slide deck (dark)
  analysis.html               Blank long-form document view (light/dark, sticky-TOC)
<deck-slug>/                Each folder is one self-contained presentation
  index.html                  The deck
  analysis.html               Long-form companion
index.html                  Root gallery — links to every deck
CLAUDE.md                   Working rules / design system for editing this repo
```

---

## ➕ Add a new presentation

**Easiest — ask Claude Code:** _"create a new <topic> presentation"_ runs the
[`new-presentation`](.claude/skills/new-presentation/SKILL.md) skill, which scaffolds both files,
adds the gallery card, updates this table, and opens the deck.

**By hand:**

1. `cp -r _template <deck-slug>` (lowercase-hyphenated folder name).
2. Edit `<deck-slug>/index.html` — `<title>`, `<meta description>`, chrome labels, slides, `.deck-progress` nav.
3. Edit `<deck-slug>/analysis.html` — hero, TOC entries, `<section id>` content.
4. Remove the `<!-- EDIT: ... -->` comments once content is real.
5. Add a `.deck-card` to the root [`index.html`](index.html) gallery and a row to the table above.
6. Commit & push — it deploys automatically.

> **Never** move CSS/JS out of the inline `<style>`/`<script>` blocks — each deck must open standalone.

---

## 🎨 Design systems

xgeeks palette only — **Techno Green `#00EBB6`**, **Dark Space `#002E33`**, **coral `#FF966E`**, greys.
The deck and the analysis view are **two separate design systems** — don't cross-contaminate (different
tokens, fonts, layout). Full token list and component vocabulary live in [`CLAUDE.md`](CLAUDE.md).

| | `index.html` (deck) | `analysis.html` (document) |
|---|---|---|
| Theme | Dark only | Light + dark (`prefers-color-scheme`) |
| Fonts | Jost / Fraunces / DM Mono | System sans + serif body |
| Layout | Scroll-snap slides | Sticky-TOC + content column |

---

## 💻 Local preview

```bash
python3 -m http.server      # then open http://localhost:8000/<deck-slug>/
```

Or just open the file directly — every deck is self-contained: `open <deck-slug>/index.html`.

---

## 🔒 Public repo — the one rule that matters

This repo is **public and Google-indexable.** Never commit signatory/contact PII, signed-contract
contents, per-deal pricing, internal cost numbers, or meeting notes — anything pushed may be cached
even after deletion. Name a **company and a role**, never an individual's contact details. The boundary
is also enforced by [`.gitignore`](.gitignore); when in doubt, leave it out. See [`CLAUDE.md`](CLAUDE.md).
