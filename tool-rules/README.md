# Generated tool-rule files

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
| Cursor           | `.cursorrules` at workspace root         |
| Windsurf         | `.windsurfrules` at workspace root       |
| Cline            | `.clinerules` at workspace root          |
| GitHub Copilot   | `.github/copilot-instructions.md`        |

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
