#!/usr/bin/env python3
"""Regenerate tool-specific rule files from the canonical SKILL.md.

Single source of truth: plugins/newton/skills/newton/SKILL.md

Emits under tool-rules/:
- .cursorrules                — Cursor workspace rules
- .windsurfrules              — Windsurf workspace rules
- .clinerules                 — Cline workspace rules
- copilot-instructions.md     — GitHub Copilot (copy to .github/ on install)
- README.md                   — explains provenance and install mapping

Each generated file carries a banner pointing back at the canonical source
so a reader opening one of them in the wild knows where to send fixes.

Run locally before committing any SKILL.md change:

    python3 scripts/generate-rule-files.py

CI (sync-rules.yml) runs the same command and fails the build if the
working tree is dirty afterwards — i.e., the committed tool-rules/* files
are stale relative to the current SKILL.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "plugins" / "newton" / "skills" / "newton"
SKILL_PATH = SKILL_DIR / "SKILL.md"
REFERENCES_DIR = SKILL_DIR / "references"
OUT_DIR = REPO_ROOT / "tool-rules"

# Filenames emitted under tool-rules/. Keys are labels used in README.md.
TOOL_FILES: dict[str, str] = {
    "Cursor": ".cursorrules",
    "Windsurf": ".windsurfrules",
    "Cline": ".clinerules",
    "GitHub Copilot": "copilot-instructions.md",
}

BANNER = """<!--
GENERATED FILE — DO NOT EDIT DIRECTLY.

Source of truth: plugins/newton/skills/newton/SKILL.md
                 plus plugins/newton/skills/newton/references/*.md
Regenerate with:  python3 scripts/generate-rule-files.py
CI check:         .github/workflows/sync-rules.yml

If you want to change Newton's behaviour, edit SKILL.md (or the appropriate
reference file under references/) and rerun the generator. Direct edits to
this file will be overwritten on the next sync.

The Claude Code plugin loads SKILL.md on its own and pulls reference files
only when the current turn needs them (progressive disclosure). The
non-Claude-Code tools that read this generated file don't do progressive
disclosure, so the references are inlined here to keep behaviour parity.
-->

"""

REFERENCE_SEPARATOR = (
    "\n\n---\n\n"
    "<!-- Inlined from plugins/newton/skills/newton/references/{filename} -->\n\n"
)

README_TEMPLATE = """# Generated tool-rule files

The files in this directory are **generated** from the canonical Newton
skill definition at `plugins/newton/skills/newton/SKILL.md`, with the
reference files under `plugins/newton/skills/newton/references/` inlined
below the main body. Do not edit them directly — edits here are
overwritten on the next sync.

To change Newton's behaviour, edit `SKILL.md` (or the appropriate
reference file) and run:

    python3 scripts/generate-rule-files.py

CI (`.github/workflows/sync-rules.yml`) fails the build on pull requests
and pushes to `main` if `tool-rules/*` is out of sync with the canonical
sources.

## Install mapping

| Tool             | Copy this file into your project as      |
|------------------|------------------------------------------|
{install_rows}

## Why references are inlined

The Claude Code plugin loads `SKILL.md` on its own and pulls reference
files only when the current turn needs them (progressive disclosure).
The non-Claude-Code tools that read the files in this directory don't do
progressive disclosure — they load whatever is in the file once per
session — so the references are inlined here to keep behaviour parity
across surfaces.

## Why committed + generated

Keeping the regenerated files in the repo means tools that read them at
runtime (Cursor reading `.cursorrules` from a workspace, Copilot reading
`.github/copilot-instructions.md`) don't need a build step. The trade-off
is that contributors must rerun the generator when editing `SKILL.md` or
any reference; CI enforces that rule so stale rule files can't land on
`main`.
"""


def strip_frontmatter(text: str) -> str:
    """Drop YAML frontmatter (if present) and return the body only."""
    if not text.startswith("---"):
        return text
    lines = text.splitlines(keepends=True)
    if lines[0].strip() != "---":
        return text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "".join(lines[i + 1 :]).lstrip("\n")
    # No closing fence — treat whole file as body (don't silently truncate).
    return text


def install_mapping() -> dict[str, str]:
    """Per-tool install instructions used in the README table."""
    return {
        "Cursor": "`.cursorrules` at workspace root",
        "Windsurf": "`.windsurfrules` at workspace root",
        "Cline": "`.clinerules` at workspace root",
        "GitHub Copilot": "`.github/copilot-instructions.md`",
    }


def render_readme() -> str:
    mapping = install_mapping()
    rows = "\n".join(
        f"| {tool:<16} | {target:<40} |"
        for tool, target in mapping.items()
    )
    return README_TEMPLATE.format(install_rows=rows)


def collect_references() -> str:
    """Inline every non-empty references/*.md file, sorted by filename.

    Each reference is prefixed with a separator + comment naming its source
    file so the concatenated output stays readable and its provenance is
    obvious to anyone opening the generated rule file in the wild.
    """
    if not REFERENCES_DIR.is_dir():
        return ""

    parts: list[str] = []
    for ref_path in sorted(REFERENCES_DIR.glob("*.md")):
        raw = ref_path.read_text(encoding="utf-8")
        ref_body = strip_frontmatter(raw).strip()
        if not ref_body:
            # Skip empty or frontmatter-only stubs.
            continue
        parts.append(REFERENCE_SEPARATOR.format(filename=ref_path.name))
        parts.append(ref_body)
        parts.append("\n")
    return "".join(parts)


def main() -> int:
    if not SKILL_PATH.exists():
        print(f"error: canonical SKILL.md missing at {SKILL_PATH}", file=sys.stderr)
        return 1

    skill_text = SKILL_PATH.read_text(encoding="utf-8")
    body = strip_frontmatter(skill_text).rstrip() + "\n"
    references_block = collect_references()
    combined = body + references_block

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    written: list[str] = []
    for _tool, filename in TOOL_FILES.items():
        out_path = OUT_DIR / filename
        out_path.write_text(BANNER + combined, encoding="utf-8")
        written.append(str(out_path.relative_to(REPO_ROOT)))

    readme_path = OUT_DIR / "README.md"
    readme_path.write_text(render_readme(), encoding="utf-8")
    written.append(str(readme_path.relative_to(REPO_ROOT)))

    for rel in written:
        print(f"wrote {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
