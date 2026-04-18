#!/usr/bin/env python3
"""Validate the top-level .claude-plugin/marketplace.json.

Checks:
- The file exists and is valid JSON.
- Required fields are present: name, owner.name, plugins (array).
- Each plugin entry has name and source.
- Each plugin's source path exists on disk.
- Each plugin name is unique.
- The marketplace name is not in the reserved-prefix list.

Single-plugin repo note: in the newton-skill repo the plugins array has
exactly one entry (newton). The loop below tolerates N entries — it's
reused verbatim from the multi-plugin tooling to keep the two repos in sync.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

RESERVED_PREFIXES = ("claude-", "anthropic-", "official-")


def fail(msg: str) -> None:
    print(f"::error file={MARKETPLACE_PATH.relative_to(REPO_ROOT)}::{msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not MARKETPLACE_PATH.exists():
        fail(f"{MARKETPLACE_PATH.relative_to(REPO_ROOT)} not found")

    try:
        data = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")

    # Required top-level fields.
    name = data.get("name")
    if not isinstance(name, str) or not name:
        fail("missing or empty 'name'")

    if any(name.startswith(p) for p in RESERVED_PREFIXES):
        fail(
            f"marketplace name '{name}' uses a reserved prefix "
            f"({', '.join(RESERVED_PREFIXES)}) — choose a different name"
        )

    owner = data.get("owner")
    if not isinstance(owner, dict) or not owner.get("name"):
        fail("missing owner.name")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("'plugins' must be a non-empty array")

    seen_names: set[str] = set()
    for i, plugin in enumerate(plugins):
        if not isinstance(plugin, dict):
            fail(f"plugins[{i}] must be an object")

        pname = plugin.get("name")
        if not isinstance(pname, str) or not pname:
            fail(f"plugins[{i}].name is required")

        if pname in seen_names:
            fail(f"duplicate plugin name '{pname}'")
        seen_names.add(pname)

        source = plugin.get("source")
        if not isinstance(source, str) or not source:
            fail(f"plugins[{i}].source is required")

        # Local source paths are expected to resolve under the repo.
        if source.startswith("./") or source.startswith("../"):
            resolved = (REPO_ROOT / source).resolve()
            if not resolved.exists():
                fail(f"plugins[{i}].source '{source}' does not exist on disk")

    print(f"OK  {MARKETPLACE_PATH.relative_to(REPO_ROOT)} — {len(plugins)} plugin(s)")


if __name__ == "__main__":
    main()
