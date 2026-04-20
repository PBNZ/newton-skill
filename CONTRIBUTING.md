# Contributing to newton-skill

Thanks for your interest in contributing. This is a single-skill repository: it houses the **Newton** skill plus the generated tool-rules files that carry the same content into other agentic tools. Outside contributions are welcome — especially bug reports, portability fixes, and small improvements to the skill content or the generated rule-files pipeline.

Please read this guide before opening an issue or pull request.

## Ground rules

- **Be kind.** All interactions are governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
- **Small, focused changes.** One concern per PR. If a change mixes skill-content edits with tooling or docs changes, split it.
- **Match existing style.** Follow the tone and structure of `plugins/newton/skills/newton/SKILL.md`. Prose over bullets where prose works; specifics over generalities.
- **No surprise scope.** If your PR introduces a new dependency, a new workflow, a new sub-agent, or a change to the marketplace manifest beyond what's described in the issue, flag it in the PR description.

## Ways to contribute

### Report a bug

Open an issue using the **Bug report** template. Include:

- The Claude surface (Claude Code, Claude.ai, Claude Desktop, the API, or another Agent-Skills-compatible tool) and its version if you know it.
- The invocation that triggered the problem (e.g., the exact "Newton, …" phrasing you used).
- What you expected Newton to do and what it did instead.
- A minimal reproduction if possible.

### Suggest an improvement

Open an issue using the **Feature request** template. For a proposed change to Newton's posture, methodology, or tooling, include:

- What problem the change solves and for whom.
- Why it belongs in Newton rather than a different skill or tool.
- A rough sketch of how the change would land — which files it would touch, what the user-visible difference would be.

### Submit a pull request

1. Fork the repo and create a feature branch off `main`.
2. Make your change.
3. Ensure the validation workflow would pass locally (see **Validation** below).
4. Update [`CHANGELOG.md`](CHANGELOG.md) under the `Unreleased` section.
5. Open a PR against `main` using the pull request template.

## Where changes go

- **Skill content** lives at `plugins/newton/skills/newton/SKILL.md`. This is the canonical source of truth for Newton's behaviour.
- **Reference files** (extended methodology that stays out of the main SKILL body to keep it scannable) live under `plugins/newton/skills/newton/references/`.
- **The slash command** (`/newton:newton`) is defined at `plugins/newton/commands/newton.md`.
- **Tool-specific rule files** for Cursor, Windsurf, Cline, Copilot, and similar tools live under `tool-rules/` and at the corresponding tool-specific paths. These are **generated** from `SKILL.md` with the reference files under `plugins/newton/skills/newton/references/` inlined below the main body, by `scripts/generate-rule-files.py` and the `sync-rules` workflow — do not hand-edit them. Edit `SKILL.md` (or the appropriate reference file) instead and let the pipeline regenerate. The inlining is deliberate: non-Claude-Code surfaces that read these files don't do progressive disclosure, so they need the full methodology in one place.
- **Plugin manifest:** `plugins/newton/.claude-plugin/plugin.json`.
- **Marketplace manifest:** `.claude-plugin/marketplace.json`.
- **Landing page** lives under `docs/` and is published to GitHub Pages on the `main` branch.
- **Sub-agents** (if added in a future release) live under `plugins/newton/agents/`.

Match the `name` field in `SKILL.md`'s YAML frontmatter to the skill directory name. Keep the description specific enough that it triggers cleanly on relevant requests and doesn't fire on general-purpose ones.

## Validation

The repository has a validation workflow that runs on every PR. It checks:

- `.claude-plugin/marketplace.json` is valid JSON and conforms to the marketplace schema.
- `plugins/newton/.claude-plugin/plugin.json` is valid JSON and conforms to the plugin schema.
- `plugins/newton/skills/newton/SKILL.md` has valid YAML frontmatter with the required fields.
- No email addresses or other private contact info are committed anywhere in the tree.
- No `SKILL.md` body (or any reference file, tool-rules file, or generated doc) contains invisible/bidi Unicode, imperative prompt-injection phrases, or URLs outside the allowlist at `.github/skill-url-allowlist.txt`.
- The tool-rules files under `tool-rules/` and at the tool-specific paths are in sync with `SKILL.md` — the `sync-rules` workflow regenerates them and fails the build if the checked-in copies are stale.

You can run the same checks locally before pushing — see `.github/workflows/validate.yml` and `.github/workflows/sync-rules.yml` for the exact commands.

## Security review of contributed skill content

`SKILL.md` and its reference files are prompt content: whatever lands in a `SKILL.md` body (or a file referenced from it) is read by Claude — and by other agents that ingest the generated tool-rules files — as instructions when Newton activates. PRs that add or modify skill content are reviewed for this explicitly, not just for style or correctness.

Before opening a PR that touches `SKILL.md`, any reference file, any tool-rules file, or any file that gets concatenated into them:

- **Write in plain prose.** No zero-width, bidi, or steganographic Unicode anywhere in the body. If your editor inserts them invisibly, the CI safety scan will reject the PR.
- **No prompt-injection phrases.** Avoid paraphrases of "ignore previous instructions", "disregard the above", "you are now in developer mode", jailbreak references, and the like — even inside quoted examples or code fences. If you need to discuss these patterns, describe them at a distance rather than writing them literally.
- **No instructions to override safety, exfiltrate data, or reveal system prompts.** Newton is meant to sharpen Claude's reasoning, not to reshape its safety posture.
- **Only link to allowlisted hosts.** New trusted hosts can be added to `.github/skill-url-allowlist.txt` in the same PR, with a short comment explaining why the host is needed.
- **Keep email addresses out.** The repository's private-contact scanner will reject any commit that adds one. If you need a contact channel, use GitHub-native flows — issues, pull requests, or a private security advisory.

Contributions that fail the safety scan are blocked by CI. Contributions that pass the scan but still raise reviewer concern (e.g. social-engineering framing, misleading descriptions) will be held for discussion before merge.

## Licence

By contributing, you agree your contributions will be licensed under the [Apache-2.0 licence](LICENSE).
