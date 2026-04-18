#!/usr/bin/env python3
"""Fail the build if private contact info slips into the repo.

Scans all tracked files (excluding the .git directory, the scripts directory
itself, and any vendored/third-party content) for patterns that look like
private contact info. This is a belt-and-braces check on top of review.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Anything that looks like a non-noreply email address.
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

# Directories / files to skip.
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
SKIP_FILES = {
    # The LICENCE text contains the apache.org URL and nothing else.
    "LICENSE",
}

# Literal strings that are allowed (structured URLs, not personal contacts).
ALLOWED_SUBSTRINGS = (
    "apache.org",
    "noreply.github.com",
    "users.noreply.github.com",
)


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        yield path


def main() -> None:
    failures: list[tuple[Path, int, str]] = []

    for path in iter_files(REPO_ROOT):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            # Skip binary files.
            continue

        for lineno, line in enumerate(text.splitlines(), start=1):
            for match in EMAIL.finditer(line):
                addr = match.group(0)
                if any(allowed in addr for allowed in ALLOWED_SUBSTRINGS):
                    continue
                failures.append((path, lineno, addr))

    if failures:
        for path, lineno, addr in failures:
            rel = path.relative_to(REPO_ROOT)
            print(
                f"::error file={rel},line={lineno}::"
                f"email-like string found: {addr!r} — remove or replace with a GitHub-native channel",
                file=sys.stderr,
            )
        sys.exit(1)

    print("OK  no private contact info detected")


if __name__ == "__main__":
    main()
