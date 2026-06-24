#!/usr/bin/env python3
"""Scaffold a new self-contained slide-deck presentation in its own folder.

Copies the deck design system from template.html (kept in sync with the root
index.html styling) and substitutes the title / metadata placeholders.

Usage:
  create.py --name "Q3 Pipeline Review" [--slug q3-pipeline-review] \
            [--eyebrow "Internal strategy"] [--subtitle "..."] \
            [--description "..."] [--date 2026-06-24] \
            [--kicker-label "Q3 REVIEW"] [--kicker-sub "PIPELINE"]

Writes presentations/<slug>/index.html and refuses to overwrite an existing one.
Prints the relative path and the live GitHub Pages URL.
"""
import argparse
import html
import re
import sys
from pathlib import Path

REPO_BASE_URL = "https://fabiosampaio-91.github.io/kcd-sponsor-engagement"
SKILL_DIR = Path(__file__).resolve().parent


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def find_repo_root() -> Path:
    """Walk up from CWD to the dir containing index.html + .github (the repo root)."""
    cur = Path.cwd()
    for d in (cur, *cur.parents):
        if (d / "index.html").exists() and (d / ".github").is_dir():
            return d
    sys.exit("error: could not locate repo root (index.html + .github) from CWD")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True, help="Human title of the presentation")
    p.add_argument("--slug", help="Folder slug (default: slugified name)")
    p.add_argument("--eyebrow", default="Internal strategy · Leadership brief")
    p.add_argument("--subtitle", default="A one-line summary of what this deck argues — replace me.")
    p.add_argument("--description", help="Meta description (default: subtitle)")
    p.add_argument("--date", default="", help="Prepared date, e.g. 2026-06-24")
    p.add_argument("--kicker-label", dest="kicker_label", help="Chrome left label (default: NAME, upper)")
    p.add_argument("--kicker-sub", dest="kicker_sub", default="OVERVIEW")
    args = p.parse_args()

    name = args.name.strip()
    slug = args.slug or slugify(name)
    if not slug:
        sys.exit("error: name produced an empty slug; pass --slug explicitly")

    repo = find_repo_root()
    out_dir = repo / "presentations" / slug
    out_file = out_dir / "index.html"
    if out_file.exists():
        sys.exit(f"error: {out_file.relative_to(repo)} already exists — pick a different --slug")

    template = (SKILL_DIR / "template.html").read_text()

    subs = {
        "TITLE": html.escape(name),
        "DESCRIPTION": html.escape(args.description or args.subtitle),
        "EYEBROW": html.escape(args.eyebrow),
        "SUBTITLE": html.escape(args.subtitle),
        "DATE": html.escape(args.date),
        "KICKER_LABEL": html.escape(args.kicker_label or name.upper()),
        "KICKER_SUB": html.escape(args.kicker_sub),
    }
    out = template
    for key, val in subs.items():
        out = out.replace("{{" + key + "}}", val)

    leftover = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if leftover:
        sys.exit(f"error: unresolved placeholders remain: {sorted(set(leftover))}")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file.write_text(out)

    rel = out_file.relative_to(repo)
    print(f"created: {rel}")
    print(f"live:    {REPO_BASE_URL}/presentations/{slug}/")


if __name__ == "__main__":
    main()
