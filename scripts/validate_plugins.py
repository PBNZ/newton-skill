#!/usr/bin/env python3
"""Validate every plugins/<plugin>/.claude-plugin/plugin.json.

Checks:
- File is valid JSON.
- Required fields: name, description, version.
- 'version' looks like SemVer (major.minor.patch[-prerelease]).
- Plugin directory name matches manifest 'name'.
- If 'license' is set, it is a string.

Single-plugin repo note: glob pattern handles N plugins. In this repo we
expect exactly one manifest (plugins/newton/.claude-plugin/plugin.json).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


def fail(path: Path, msg: str) -> None:
    print(f"::error file={path.relative_to(REPO_ROOT)}::{msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not PLUGINS_DIR.exists():
        print(f"OK  no plugins/ directory yet")
        return

    manifests = sorted(PLUGINS_DIR.glob("*/.claude-plugin/plugin.json"))
    if not manifests:
        print(f"WARN  no plugin manifests found under {PLUGINS_DIR.relative_to(REPO_ROOT)}")
        return

    for manifest_path in manifests:
        plugin_dir = manifest_path.parent.parent
        plugin_dir_name = plugin_dir.name

        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(manifest_path, f"invalid JSON: {exc}")

        name = data.get("name")
        if not isinstance(name, str) or not name:
            fail(manifest_path, "missing or empty 'name'")

        if name != plugin_dir_name:
            fail(
                manifest_path,
                f"manifest 'name' ({name!r}) does not match directory name ({plugin_dir_name!r})",
            )

        description = data.get("description")
        if not isinstance(description, str) or not description.strip():
            fail(manifest_path, "missing or empty 'description'")

        version = data.get("version")
        if not isinstance(version, str) or not SEMVER.match(version):
            fail(manifest_path, f"'version' must be SemVer (got {version!r})")

        licence = data.get("license")
        if licence is not None and not isinstance(licence, str):
            fail(manifest_path, "'license' must be a string if present")

        author = data.get("author")
        if author is not None:
            if not isinstance(author, dict):
                fail(manifest_path, "'author' must be an object if present")
            if not author.get("name"):
                fail(manifest_path, "'author.name' is required when 'author' is present")

        print(f"OK  {manifest_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
