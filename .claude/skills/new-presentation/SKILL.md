---
name: new-presentation
description: Scaffold a new self-contained slide-deck presentation in its own folder, reusing the synvert xgeeks deck design system, and publish it via GitHub Pages. Use when the user asks to "create a new presentation/deck/slides", "start a new slide deck", or names a presentation to spin up. Takes the presentation name as input.
---

# New presentation

Creates a new slide deck under `presentations/<slug>/index.html`, carrying the exact deck
styling from the root [index.html](../../../index.html), then publishes it through the existing
GitHub Pages Action.

## Inputs

- **name** (required) — the human title of the presentation (e.g. "Q3 Pipeline Review").
- Optional: `slug`, `eyebrow`, `subtitle`, `description`, `date`, `kicker-label`, `kicker-sub`.

If the user only gives a name, that's enough — sensible defaults fill the rest. Derive the date
from the current date if the user doesn't specify one.

## Steps

1. **Scaffold the folder.** From the repo root, run the generator (it slugifies the name, creates
   a separate folder, and refuses to overwrite an existing deck):

   ```bash
   python3 .claude/skills/new-presentation/create.py --name "<NAME>" --date "<YYYY-MM-DD>"
   ```

   Pass any optional flags the user provided. The script prints the created path and the live URL.

2. **Fill in real content.** The scaffold is a 3-slide starter (cover → content → close). Edit
   `presentations/<slug>/index.html` to add the user's actual slides. **Match the deck design
   system exactly** — tokens, fonts (Jost / Fraunces italic for emphasis / DM Mono labels), the
   `slide` → `chrome` → `frame` → `slide__bottom` skeleton, and the component vocabulary
   (`.card`, `.kpi`, `.lanes`, `.grid-*`, etc.). The full reference is in the **"Presentation
   styling"** section of [CLAUDE.md](../../../CLAUDE.md); follow it. When you add or remove slides
   you MUST also update: the `.deck-progress` nav entries, every `chrome__pageno` count, and the
   `/ NNN` total + cover slide count.

3. **Respect the PII boundary.** This repo is public and Google-indexable. Company + role only —
   never personal contact PII, per-deal values, contract contents, or meeting notes. See
   [CLAUDE.md](../../../CLAUDE.md).

4. **Publish (only when the user asks to publish/commit/push).** No workflow change is needed: the
   Pages deploy in [.github/workflows/pages.yml](../../../.github/workflows/pages.yml) uploads the
   whole repo root (`path: .`), so any new `presentations/<slug>/` folder is published
   automatically. To publish, commit and push to `main` (branch first if on `main` and house rules
   require it) — that triggers the deploy. Confirm the workflow still uploads `path: .`; if it were
   ever scoped to specific paths, add `presentations/` so the deck ships.

   ```bash
   git add presentations/<slug> && git commit -m "Add presentation: <NAME>" && git push
   ```

   Then give the user the live URL:
   `https://fabiosampaio-91.github.io/kcd-sponsor-engagement/presentations/<slug>/`

## Notes

- The deck stays **self-contained**: all CSS/JS is inline in the generated `index.html`; the only
  external dependency is the Google Fonts `<link>`. Don't link `assets/styles.css` (that's the
  document-view stylesheet for `analysis.html`, a different design system).
- `template.html` in this skill folder is the source for the styling and is a verbatim copy of the
  root deck's `<style>` + `<script>` blocks. If the root deck's design system changes and you want
  new presentations to inherit it, regenerate `template.html` from the updated `index.html`.
