#!/usr/bin/env python3
"""Scan SKILL.md bodies for prompt-injection risks.

Three classes of finding, each a hard failure:

1. Dangerous invisible / bidi / steganographic Unicode.
2. Imperative prompt-injection phrases ("ignore previous instructions", etc.).
3. URLs whose host is not in `.github/skill-url-allowlist.txt`.

Scope: only the Markdown body of every `plugins/**/skills/**/SKILL.md` file.
The YAML frontmatter is skipped because it is validated separately by
`validate_skills.py` and does not contain prose that the model will execute.

Output format is GitHub Actions-compatible (`::error file=...,line=...::...`)
so problems surface inline on the PR diff.
"""

from __future__ import annotations

import pathlib
import re
import sys
from typing import Iterable

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_GLOB = "plugins/*/skills/*/SKILL.md"
ALLOWLIST_FILE = REPO_ROOT / ".github" / "skill-url-allowlist.txt"

# ---------------------------------------------------------------------------
# 1. Dangerous characters
# ---------------------------------------------------------------------------

# Single code points that should never appear in prompt text.
DANGEROUS_CHARS: dict[str, str] = {
    "\u200B": "ZERO WIDTH SPACE (U+200B)",
    "\u200C": "ZERO WIDTH NON-JOINER (U+200C)",
    "\u200D": "ZERO WIDTH JOINER (U+200D)",
    "\u2060": "WORD JOINER (U+2060)",
    "\u180E": "MONGOLIAN VOWEL SEPARATOR (U+180E)",
    "\u00AD": "SOFT HYPHEN (U+00AD)",
    "\uFEFF": "ZERO WIDTH NO-BREAK SPACE / BOM (U+FEFF)",
    "\u202A": "LEFT-TO-RIGHT EMBEDDING (U+202A)",
    "\u202B": "RIGHT-TO-LEFT EMBEDDING (U+202B)",
    "\u202C": "POP DIRECTIONAL FORMATTING (U+202C)",
    "\u202D": "LEFT-TO-RIGHT OVERRIDE (U+202D)",
    "\u202E": "RIGHT-TO-LEFT OVERRIDE (U+202E)",
    "\u2066": "LEFT-TO-RIGHT ISOLATE (U+2066)",
    "\u2067": "RIGHT-TO-LEFT ISOLATE (U+2067)",
    "\u2068": "FIRST STRONG ISOLATE (U+2068)",
    "\u2069": "POP DIRECTIONAL ISOLATE (U+2069)",
}


def _is_stegano(ch: str) -> str | None:
    """Return a label if the char is in a known steganography range, else None."""
    cp = ord(ch)
    if 0xFE00 <= cp <= 0xFE0F:
        return f"VARIATION SELECTOR (U+{cp:04X})"
    if 0xE0000 <= cp <= 0xE007F:
        return f"TAG CHARACTER (U+{cp:05X})"
    return None


# ---------------------------------------------------------------------------
# 2. Injection phrases
# ---------------------------------------------------------------------------

INJECTION_PATTERNS: list[str] = [
    r"ignore\s+(all\s+)?previous\s+instructions?",
    r"ignore\s+(all\s+)?prior\s+instructions?",
    r"disregard\s+(all\s+)?previous\s+instructions?",
    r"disregard\s+the\s+above",
    r"forget\s+(all\s+)?your\s+instructions?",
    r"forget\s+everything\s+above",
    r"forget\s+(all\s+)?previous\s+instructions?",
    r"you\s+are\s+now\s+in\s+developer\s+mode",
    r"dan\s+mode\s+activated",
    r"do\s+anything\s+now",
    r"jailbreak\s+mode",
]

_COMPILED_INJECTION = [re.compile(p, re.IGNORECASE) for p in INJECTION_PATTERNS]


# ---------------------------------------------------------------------------
# 3. URLs
# ---------------------------------------------------------------------------

URL_RE = re.compile(r"https?://([^/\s\)\]\>]+)", re.IGNORECASE)


def load_allowlist() -> set[str]:
    if not ALLOWLIST_FILE.exists():
        return set()
    hosts: set[str] = set()
    for raw in ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip().lower()
        if line:
            hosts.add(line)
    return hosts


def _normalise_host(host: str) -> str:
    host = host.strip().lower()
    # Strip trailing punctuation that may have slipped past the URL regex.
    host = host.rstrip(".,;:!?\"'")
    # Strip port.
    if ":" in host:
        host = host.split(":", 1)[0]
    return host


def _host_allowed(host: str, allowlist: set[str]) -> bool:
    host = _normalise_host(host)
    if host in allowlist:
        return True
    # Allow subdomains of any allowlisted domain.
    return any(host.endswith("." + allowed) for allowed in allowlist)


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------

def split_frontmatter(text: str) -> tuple[int, str]:
    """Return (body_start_line_number, body_text).

    If no frontmatter fence is present, the whole file is body starting at line 1.
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return 1, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            body_start = i + 2  # 1-indexed line after the closing fence
            return body_start, "".join(lines[i + 1:])
    # No closing fence — treat as all body.
    return 1, text


def _line_of(body: str, index: int, body_start_line: int) -> int:
    return body_start_line + body.count("\n", 0, index)


def scan_file(path: pathlib.Path, allowlist: set[str]) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(REPO_ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    body_start, body = split_frontmatter(text)

    # 1. Character-level scan
    for idx, ch in enumerate(body):
        if ch in DANGEROUS_CHARS:
            line = _line_of(body, idx, body_start)
            errors.append(
                f"::error file={rel},line={line}::Dangerous invisible character: {DANGEROUS_CHARS[ch]}"
            )
            continue
        label = _is_stegano(ch)
        if label is not None:
            line = _line_of(body, idx, body_start)
            errors.append(
                f"::error file={rel},line={line}::Suspicious steganographic character: {label}"
            )

    # 2. Injection phrases
    for pattern in _COMPILED_INJECTION:
        for match in pattern.finditer(body):
            line = _line_of(body, match.start(), body_start)
            errors.append(
                f"::error file={rel},line={line}::Prompt-injection phrase detected: {match.group(0)!r}"
            )

    # 3. URLs
    for match in URL_RE.finditer(body):
        host = _normalise_host(match.group(1))
        if not _host_allowed(host, allowlist):
            line = _line_of(body, match.start(), body_start)
            errors.append(
                f"::error file={rel},line={line}::URL host not in allowlist: {host} "
                f"(add to .github/skill-url-allowlist.txt if intentional)"
            )

    return errors


def iter_skill_files() -> Iterable[pathlib.Path]:
    yield from REPO_ROOT.glob(SKILLS_GLOB)


def main() -> int:
    allowlist = load_allowlist()
    all_errors: list[str] = []
    checked = 0
    for path in sorted(iter_skill_files()):
        checked += 1
        all_errors.extend(scan_file(path, allowlist))

    if all_errors:
        for line in all_errors:
            print(line)
        print(
            f"FAIL  check_skill_safety.py — {len(all_errors)} issue(s) across {checked} skill file(s)",
            file=sys.stderr,
        )
        return 1

    print(f"OK    check_skill_safety.py — {checked} skill file(s) clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
