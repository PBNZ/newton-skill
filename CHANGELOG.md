# Changelog

All notable changes to Newton are documented in this file.

Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] — 2026-04-18

Initial public release as a standalone repository. Newton was previously distributed inside the `pbnz-skills` multi-plugin marketplace; this release migrates it to its own home at [`PBNZ/newton-skill`](https://github.com/PBNZ/newton-skill) so it can version, release, and be installed independently.

### Added

- **Standalone repository scaffolding.** Single-plugin marketplace layout with Newton as the only plugin, `plugins/newton/` tree following the [Agent Skills](https://agentskills.io/) convention, governance files (LICENSE, CODE_OF_CONDUCT, CONTRIBUTING, SECURITY) ported from `pbnz-skills`.
- **Canonical `SKILL.md`.** Full Newton methodology at `plugins/newton/skills/newton/SKILL.md`, including the opening-move protocol, core principles (honest engagement, self-critique before delivery, current authoritative sources, reuse before reinvention, simplicity in what's produced), clarifying-question discipline, research methodology, reuse-check methodology, surgical-edit rule, and handoff guidance.
- **Multi-tool install matrix.** README documents installation on Claude Code, Claude Cowork, Claude.ai / Desktop, the Claude API, the `gh skill` CLI, Cursor, Windsurf, Cline, and GitHub Copilot.
- **Generated tool-rule files** under `tool-rules/` for Cursor (`.cursorrules`), Windsurf (`.windsurfrules`), Cline (`.clinerules`), and Copilot (`copilot-instructions.md`). Each is generated from `SKILL.md` by `scripts/generate-rule-files.py`; CI fails the build if they drift.
- **CI pipelines.** `validate.yml` enforces marketplace / plugin / skill schema compliance and safety checks; `sync-rules.yml` enforces tool-rules ↔ `SKILL.md` parity; `release.yml` attaches `SKILL.md` to tagged GitHub releases.
- **`AGENTS.md`** at the repo root — pointer to the canonical skill, following the [Agentic AI Foundation](https://agentic.foundation/) convention.
- **Governance.** Apache-2.0 LICENSE, contributor guidelines, Code of Conduct (Contributor Covenant 2.1), security policy.

### Changed

- Newton now lives at [`PBNZ/newton-skill`](https://github.com/PBNZ/newton-skill) as the canonical home. The version inside `pbnz-skills` is deprecated in place — banners in the `pbnz-skills` Newton folder point here.

### Notes

- Sub-agent decomposition is deferred to v0.3.0.
- READMEs are English-only at v0.2.0. Translations and a landing-page language switcher are tracked in issues.

[Unreleased]: https://github.com/PBNZ/newton-skill/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/PBNZ/newton-skill/releases/tag/v0.2.0
