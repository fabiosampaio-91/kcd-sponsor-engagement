# CLAUDE.md — kcd-sponsor-engagement

Working rules for any AI agent (or human) editing this repo. These override default behavior.

## What this repo is

The **public** GitHub Pages site for synvert xgeeks' KCD Sponsor → Business Development plan.
Live at: https://fabiosampaio-91.github.io/kcd-sponsor-engagement/

Pure **static site — no build step, no dependencies, no `package.json`, no framework.**
Hand-written HTML/CSS/vanilla JS plus aggregated, role-based markdown. Edit a file, commit,
push — that's the whole pipeline. Don't introduce a bundler, a package manager, or a JS
framework; nothing here needs one and the deploy ([.github/workflows/pages.yml](.github/workflows/pages.yml))
uploads the repo root verbatim.

## ⚠️ This repo is PUBLIC and Google-indexable — the one rule that matters most

**Never commit private or sensitive content.** Anything pushed here may be cached or indexed
even after deletion. Specifically, never add:

- **Signatory or contact PII** — personal names tied to roles, emails, phone numbers, LinkedIn
  URLs of sponsor contacts.
- **Signed-contract contents** or any document from the source `Sources/` folders.
- **Sponsor pricing / per-deal values, internal cost numbers, effort estimates.** The site
  carries only aggregated totals (e.g. "~€59K across 14 sponsors") and qualitative framing.
- **Meeting notes / transcripts.**

When naming an account, name the **company and a role** ("CEO", "Head of Digital Tech Office",
"engineering leadership") — never an individual's contact details. **If unsure, leave it out.**

The boundary is also enforced mechanically by [.gitignore](.gitignore) (`private/`, `*PRIVATE*`,
`*.xlsx`, `*.docx`) — never weaken those rules, and before committing, sanity-check the diff for
PII / pricing / contract content regardless.

### Public vs. private split

- The sensitive source-of-truth (signatory names, route-in contacts, per-deal values, the bench)
  lives **only** in the git-ignored `private/PRIVATE-account-playbook.md` and the private companion
  repo `kcd-sponsor-engagement-private`.
- The tracked [account-playbook.md](account-playbook.md) is the **public, redacted** version —
  roles only, no third-party PII. Don't confuse the two; never copy private content into the
  public file.

## File map

```
index.html          Slide-deck presentation (primary leadership view) — SELF-CONTAINED
analysis.html       Document view (full long-form plan) — uses shared assets/
assets/styles.css   Stylesheet for analysis.html ONLY (document view)
assets/nav.js       Sticky-TOC active-section highlighter for analysis.html ONLY
account-playbook.md  Public, redacted account playbook (roles only)
action-plan.md       Engagement action plan (public, aggregated)
bd-crm-spec.md       BD CRM spec — labels, fields, seed sources, CSV template
methodology.md       Inputs, research, sources, method
.github/workflows/pages.yml  Pages deploy (push to main → live)
private/             🔒 git-ignored — never published
```

## The two pages are different design systems — don't cross-contaminate

This is the easiest mistake to make. They share **no** CSS and have **separate** variable sets:

| | [index.html](index.html) | [analysis.html](analysis.html) |
|---|---|---|
| CSS/JS | Inline `<style>` + `<script>`, fully self-contained | External [assets/styles.css](assets/styles.css) + [assets/nav.js](assets/nav.js) |
| Theme | Dark only (`--bg:#03161a`) | Light + dark via `prefers-color-scheme` |
| Fonts | Google Fonts: Jost / Fraunces / DM Mono | System fonts (`-apple-system`, serif body) |
| Layout | Full-viewport scroll-snap slides (`.slide`/`.frame`) | Sticky-TOC + content column (`.layout`/`.toc`/`.content`) |

When editing one, keep its conventions; don't copy a class, variable, or font from the other.
Edits to `assets/` affect `analysis.html` only — `index.html` won't change.

## Brand

xgeeks palette only — **Techno Green `#00EBB6`**, **Dark Space `#002E33`**, **coral `#FF966E`**,
greys. Both pages already encode this in CSS variables (`--accent` / `--accent-bright` /
`--warm` etc.); reuse the existing variables rather than hard-coding new hex values. Keep it
simple and on-brand; no heavy branding work.

## Presentation styling ([index.html](index.html)) — the design system that generated the current deck

The slide deck has a deliberate, self-contained visual language. **Match it exactly** when adding
or editing slides — don't invent new tokens, fonts, or component shapes. Everything below lives in
the inline `<style>` block at the top of [index.html](index.html).

### Design tokens (CSS variables, dark theme)

```
Surfaces   --bg #03161a   --bg-2 #082023   --bg-3 #0d2a2e        (page → card → header rows)
Ink        --ink #fff  --ink-2 #c7d8d4  --ink-3 #7f9591  --ink-4 #4c6562   (heading→body→muted→faint)
Lines      --line #143034 (inner rules)   --line-2 #1f4247 (card borders)
Accent     --accent #00EBB6   --accent-dim #11b89a   --accent-deep #064a40
Warm       --warm #ff966e     Status: --good/--bad #f87171/--warn #fbbf24 (+ matching *-bg)
```

### Typography (Google Fonts, loaded in `<head>`)

- `--display` = **Jost** (sans) — headings, labels, most UI. Weights 300/400/500/600.
- `--serif` = **Fraunces** (italic) — used *only* for emphasis spans (`<em>`/`.accent`) inside
  display headings, KPI values, pull-quotes, and quoted message text. Italic serif against the
  sans is the signature move; don't overuse it.
- `--mono` = **DM Mono** — kickers, chrome, labels, page numbers, table headers. Always
  `text-transform:uppercase` with wide `letter-spacing` (0.1–0.22em).
- Headings use `clamp()` for fluid sizing (`h1.display` 40→90px, `h2.display` 28→58px), tight
  `letter-spacing:-0.025em`, `line-height:~1`.

### Slide skeleton — copy this structure for any new slide

```html
<!-- 0NN Title -->
<section class="slide" id="sNN">
  <div class="chrome">
    <div class="chrome__left">SECTION LABEL <span class="dot"></span> SUBLABEL</div>
    <div class="chrome__right"><span class="chrome__mark">synvert <b>xgeeks</b></span><span class="chrome__pageno">0NN / 018</span></div>
  </div>
  <div class="frame">
    <p class="kicker fade-up">Eyebrow line</p>
    <h2 class="display fade-up d1">Headline with <em>serif emphasis</em> and <span class="accent">accent</span>.</h2>
    <p class="subhead fade-up d2">…</p>
    <!-- content components, each with fade-up d1..d4 for staggered reveal -->
  </div>
  <div class="slide__bottom"><span>0NN · Section</span><span class="hint">Next teaser <span class="arrow"></span></span></div>
</section>
```

When you add a slide you must also: (1) add a `<a href="#sNN" data-target="sNN"><span>0NN</span></a>`
entry to the `.deck-progress` nav, and (2) update every `chrome__pageno` / `slide__bottom` count
and the cover's slide count if the total changes (currently **18 slides**, `/ 018`).

### Component vocabulary (use these; don't reinvent)

`.card` (+ `.is-accent` / `.is-warm`), `.kpi` (label + value + sub), `.grid-2/3/4`, `.lanes`/`.lane`
(`.a` warm = Track A, `.b` accent = Track B), `.rule-strip`, `.dt` (data table), `.smx` (state
matrix), `.schema` (route-in→target), `.bench`/`.person`, `.doors`/`.door`, `.tiers`/`.tier`,
`.board`/`.acct`, `.crm`, `.gantt`, `.msg`/`.pull-quote`, `.heat`/`.tag-pill` (status chips).
Cards/tables are `--bg-2` on a `--line-2` border, `border-radius:4–6px`, often with a thin accent
top-rule. Two-track colour code is consistent throughout: **warm = Track A / organizer**,
**accent green = Track B / business**.

### Motion & behavior

- Reveal animation: add `fade-up` (plus `d1`–`d4` for stagger) to elements; the inline
  IntersectionObserver script adds `.in` when the slide is ≥40% visible. Honors
  `prefers-reduced-motion`.
- Navigation: vertical `scroll-snap` slides + arrow-key handler + clickable `.deck-progress` rail
  on the right. Don't break scroll-snap (`scroll-snap-align:start` on `.slide`).
- Responsive collapse points are `1150px` and `700px` — grids fold to fewer columns; keep new
  components working there (test by narrowing the window).

### Hard rules for the deck

- **Keep it self-contained** — all CSS/JS stays inline in [index.html](index.html). Do **not** pull
  in `assets/styles.css`, add a `<link>` to external CSS, or split the JS out.
- The **only** external dependency is the Google Fonts `<link>`; don't add more.
- Reuse existing CSS variables and component classes; introduce a new class only when no existing
  one fits, and style it in the same idiom (tokens, radii, mono-uppercase labels).

## Conventions to match

- `analysis.html` sections are `<section id="...">` under `.content`; the TOC links to those IDs
  and [assets/nav.js](assets/nav.js) (IntersectionObserver) highlights the active one. Add a new
  section by adding both the `<section id>` and its matching `.toc a[href="#id"]` entry.
- Keep `<title>` and `<meta name="description">` accurate when content changes materially.
- Aggregated numbers and "company + role" phrasing only — see the PII rule above.

## How to update

1. Make the change here (or in the private source), keeping the public/private boundary.
2. Re-check the diff for any PII / pricing / contract content.
3. To preview locally, open the file in a browser or serve the root (e.g. `python3 -m http.server`).
4. Commit & push. GitHub Pages redeploys from `main` automatically.

Commit or push **only when asked.**
