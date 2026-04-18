#!/usr/bin/env python3
"""Validate every SKILL.md under plugins/*/skills/*/.

Checks:
- File starts with YAML frontmatter delimited by '---'.
- Frontmatter is valid YAML.
- Required fields: name, description.
- 'name' matches the skill directory name.
- 'description' is present and non-empty.

Single-plugin repo note: glob pattern handles N skills. In this repo we
expect exactly one SKILL.md (plugins/newton/skills/newton/SKILL.md).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml  # type: ignore[import-untyped]

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"


def fail(path: Path, msg: str) -> None:
    print(f"::error file={path.relative_to(REPO_ROOT)}::{msg}", file=sys.stderr)
    sys.exit(1)


def extract_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_yaml, body). Raises ValueError if no frontmatter."""
    if not text.startswith("---"):
        raise ValueError("file does not start with '---' frontmatter marker")

    # Find the closing '---' on its own line.
    lines = text.splitlines()
    if lines[0].strip() != "---":
        raise ValueError("first line must be exactly '---'")

    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        raise ValueError("no closing '---' for frontmatter block")

    return "\n".join(lines[1:end_idx]), "\n".join(lines[end_idx + 1 :])


def main() -> None:
    if not PLUGINS_DIR.exists():
        print("OK  no plugins/ directory yet")
        return

    skill_files = sorted(PLUGINS_DIR.glob("*/skills/*/SKILL.md"))
    if not skill_files:
        print(f"WARN  no SKILL.md files found under {PLUGINS_DIR.relative_to(REPO_ROOT)}")
        return

    for skill_path in skill_files:
        skill_dir_name = skill_path.parent.name
        text = skill_path.read_text(encoding="utf-8")

        try:
            fm_yaml, body = extract_frontmatter(text)
        except ValueError as exc:
            fail(skill_path, f"frontmatter error: {exc}")

        try:
            fm = yaml.safe_load(fm_yaml)
        except yaml.YAMLError as exc:
            fail(skill_path, f"invalid YAML frontmatter: {exc}")

        if not isinstance(fm, dict):
            fail(skill_path, "frontmatter must be a YAML mapping")

        name = fm.get("name")
        if not isinstance(name, str) or not name.strip():
            fail(skill_path, "missing or empty 'name' in frontmatter")

        if name != skill_dir_name:
            fail(
                skill_path,
                f"frontmatter 'name' ({name!r}) does not match skill directory name "
                f"({skill_dir_name!r})",
            )

        description = fm.get("description")
        if not isinstance(description, str) or not description.strip():
            fail(skill_path, "missing or empty 'description' in frontmatter")

        if not body.strip():
            fail(skill_path, "SKILL.md has no body content after frontmatter")

        print(f"OK  {skill_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
