# Changelog

All notable changes to Newton are documented in this file.

Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] — 2026-04-19

Attribution layer for Newton's debt to upstream prior art. Behaviour of the skill when invoked is unchanged — frontmatter, name, description, and trigger rules are identical to `0.2.0`. What changes is that Newton now attributes derived work as part of normal operation, and the repository carries the licence and credit trail that should have landed with `0.2.0`.

### Added

- `NOTICE.md` at repo root — attribution and MIT licence preservation for material adapted from [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) by Jiayuan (`forrestchang`), which distils [Andrej Karpathy's public observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls. Includes a section-by-section breakdown of what Newton derives from upstream and a three-layer attribution structure (originator of ideas → upstream author → integrator).
- Newton skill: new **"Attribution when building on others' work"** principle in the Core principles section, covering licence obligations, community norms even without a licence, specificity about what was borrowed, placement that survives redistribution, and distinguishing the three layers of credit. Framed as the second half of *Reuse before reinvention*.
- Newton skill: self-evaluation gate item 10 — mandatory attribution check for any work that incorporates or builds on third-party material before delivery.
- Newton skill: Credits footer at the end of `SKILL.md` — names `andrej-karpathy-skills` as the source of the *Simplicity in what's produced* and *Editing existing work — surgical changes only* sections, with an absolute GitHub URL to `NOTICE.md` so attribution travels with the skill when distributed as a release asset.
- Plugin README (`plugins/newton/README.md`): "Related work and influences" section pointing at `NOTICE.md` via a relative link for repo-tree readers.

### Changed

- Newton skill grew a behavioural principle and a pre-delivery gate check — Newton now attributes derived work as part of normal operation, not just documents that it should. Frontmatter, name, description, and trigger rules are unchanged; invocation behaviour is identical.
- `plugin.json` and `marketplace.json` versions bumped to `0.2.1`.

### Provenance

- This attribution layer was first landed in `PBNZ/pbnz-skills` as its `0.2.0` release (2026-04-19) before `newton-skill` was established as Newton's canonical home. It is ported here so the authoritative Newton repository carries the same attribution trail. The `pbnz-skills` Newton entry is being retired in favour of a pointer to this repo; see that repository's `0.3.0` changelog entry for the retirement record.

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

[Unreleased]: https://github.com/PBNZ/newton-skill/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/PBNZ/newton-skill/releases/tag/v0.2.1
[0.2.0]: https://github.com/PBNZ/newton-skill/releases/tag/v0.2.0
