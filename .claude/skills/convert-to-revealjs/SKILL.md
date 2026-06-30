---
name: convert-to-revealjs
description: Convert a scroll-snap HTML slide deck into a reveal.js presentation that preserves the full design system. Use this skill when the user asks to "convert to reveal.js", "make a reveal.js version", "convert the deck to reveal.js", "I need speaker notes", "convert slides to reveal.js", "create a reveal.js presentation from our deck", or wants the existing deck in a different navigation format (keyboard/touch/presenter mode). Always invoke proactively when the user mentions reveal.js, wants to export an existing deck, or is preparing for a live talk and needs a presentation framework.
---

# convert-to-revealjs

Delegate to the **`convert-to-revealjs` agent** — it owns the full process, all rules, and all pitfalls. The agent's system prompt is the single source of truth.

## What the agent does (summary)

1. Detects the audience profile (from handoff message or source deck inference)
2. Reads the source `<slug>/index.html`
3. Converts to reveal.js, preserving the full design system verbatim
4. Writes output to **`<slug>/revealjs/index.html`** (inside the source deck's folder)
5. Audits font sizes for projection readability
6. Asks if the user wants PDF export

## What changes vs. what stays

**Replaced:** scroll-snap navigation, arrow-key JS, IntersectionObserver, `.deck-progress` rail, `.chrome`/`.slide__bottom` overlays (→ speaker notes)

**Preserved:** all CSS tokens, component classes, font links, `.frame` content HTML, background gradients
