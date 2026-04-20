# Changelog

All notable changes to Newton are documented in this file.

Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] — 2026-04-20

Context-efficiency restructure and alignment with current-generation models (Opus 4.7). Newton's methodology is unchanged in substance — honest engagement, self-critique before delivery, current sources, reuse before reinvention, simplicity, surgical edits, attribution — but its packaging now matches the anti-ceremony discipline it teaches. Per-invocation context footprint drops by roughly 45% for Claude Code users via progressive disclosure; non-Claude-Code surfaces keep the full methodology in their generated rule files.

Backwards-compatible on Sonnet 4.6 and Haiku 4.5. No behavioural regressions; Newton's voice and triggering rules are unchanged.

### Changed

- **SKILL.md restructured for progressive disclosure.** Research methodology, reuse-check methodology, attribution, and handoff are extracted into `plugins/newton/skills/newton/references/*.md` and replaced in the main body with short pointer blocks. The Claude Code plugin loads only what the current turn needs; reference files are pulled on demand. SKILL.md body drops from roughly 5,200 to roughly 2,900 body tokens.
- **Core principles consolidated.** The previous triple coverage (Core principles + "What Newton does not do" + Self-evaluation gate) is now a single core-principles section plus a leaner pre-delivery gate. Each inversion (no manufactured objections, no silent reuse-skipping, no invented citations) lives inline with the principle it sharpens.
- **Meta-commentary removed.** The closing rationale paragraph and the duplicated "shape in practice" paragraph were redundant with content elsewhere; gone.
- **Tool guidance moved from prescriptive to outcome-oriented.** The main body says *"verify time-sensitive claims against current sources before asserting"* where it previously said *"run `web_search`"*; tool-specific query design, source ranking, and fetching guidance now live in `references/research-methodology.md`. This both shrinks per-invocation context and aligns with Opus 4.7's implicit tool detection.
- **Tone-management instructions Opus 4.7 handles natively were removed.** No more explicit "do not use emojis unless the user does", "do not use praise openers", "do not repeat the user's question back" — replaced with one line: your native length-and-tone calibration is correct; match the depth the task warrants. The distinctive Newton voice rules (pushback calibration, prose-by-default, cite-only-what-was-actually-checked) are kept.
- **YAML frontmatter trimmed.** The closing rationale sentence in the description (*"Newton is opt-in by design — its scrutiny-first approach adds length, tokens, and ceremony…"*) is removed; triggering-discipline sentences are kept verbatim, because those carry the activation gate.
- **Tool-rules generator updated.** `scripts/generate-rule-files.py` now inlines `references/*.md` under the main SKILL body so `.cursorrules`, `.windsurfrules`, `.clinerules`, and `copilot-instructions.md` remain self-contained for surfaces that don't do progressive disclosure. A separator comment names each inlined file so the provenance is clear.
- `plugin.json` and `marketplace.json` versions bumped to `0.3.0`.

### Added

- **Effort-level awareness** in the opening move. At low/medium effort, Newton defaults toward quick-start behaviour even without an explicit signal; at high/xhigh, the full opening move applies; at max, maximum depth. The caller's effort dial is treated as a signal about how much deliberation the task warrants. Non-Opus environments that don't expose effort simply follow default mode.
- **Session-memory guidance** for multi-turn Newton work — keep resolved decisions, intermediate findings, and stated constraints in file-system memory when available, read at session start, update as decisions harden. Graceful on environments without memory.
- **Principle-level parallelisation note.** For independent sub-tasks (researching two topics, comparing candidate libraries, running a reuse check while drafting), Newton considers parallel dispatch rather than default serial execution. Sub-agent decomposition into dedicated Newton roles (newton-researcher, newton-reuse-checker, etc.) remains deferred to a later release.
- **Vision-as-primary-evidence note** inside `references/research-methodology.md` — when visual input is provided, reason from the image directly rather than OCR-then-reason; use programmatic image analysis where pixel-level accuracy matters.
- **`docs/examples/router-claude-md.md`** — an optional user-level CLAUDE.md template that detects the running model and layers model-appropriate behaviour on top of any loaded skill (not just Newton). Opt-in by copying into `~/.claude/CLAUDE.md` or a project-level CLAUDE.md; **not** auto-installed by the plugin.
- `plugins/newton/commands/newton.md` — the previously empty slash-command file now carries a minimal stub so `/newton:newton [your question]` works as an invocation surface alongside the natural-language triggers.

### Notes

- Sub-agent decomposition is deferred again — this release focuses on context efficiency and model-awareness inside the single-skill surface. Dedicated Newton subagents remain on the roadmap.
- README documentation of the new router example is added under *Using Newton on Opus 4.7*.
- The GitHub Pages landing page at `docs/` is unchanged; the restructure is invisible there.

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

[Unreleased]: https://github.com/PBNZ/newton-skill/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/PBNZ/newton-skill/releases/tag/v0.3.0
[0.2.1]: https://github.com/PBNZ/newton-skill/releases/tag/v0.2.1
[0.2.0]: https://github.com/PBNZ/newton-skill/releases/tag/v0.2.0
