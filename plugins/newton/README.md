# Newton (plugin)

This is the Claude Code / Cowork plugin for Newton — a reasoning and sparring partner mode.

**For the full product pitch, capability matrix, and cross-tool install guide, see the [repository root README](../../README.md).**

## Install (Claude Code / Cowork)

From Claude Code or Cowork:

```
/plugin marketplace add PBNZ/newton-skill
/plugin install newton@newton-skill
```

Updates land automatically via `/plugin update`.

For other surfaces (Claude.ai Skills settings, Claude API, Copilot/Cursor/Codex/Gemini CLI/Windsurf, and anything else Agent-Skills-compatible), see the repo-root README.

## Invocation

Newton only activates when you explicitly summon it by name:

- `Newton: help me think through [X]`
- `Newton — does this plan hold up?`
- `Newton, research [X] for me`
- `Newton, quick: [X]` — quick-start mode (principles applied, ceremony skipped)

Full invocation and quick-start guidance lives in [`skills/newton/SKILL.md`](skills/newton/SKILL.md).

## Related work and influences

Newton's **"Simplicity in what's produced"** and **"Editing existing work — surgical changes only"** principles adapt material from [`andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) by Jiayuan (`forrestchang`), which distils Andrej Karpathy's public observations on LLM coding pitfalls into a set of Claude Code guidelines. That upstream project is MIT-licensed; its licence text, a section-by-section breakdown of what Newton derives from it, and the three attribution layers (Karpathy → upstream authors → Newton as integrator) are preserved in this repository's [NOTICE](../../NOTICE.md) file.

The rest of Newton — the opening-move deliberation model, honest-engagement posture, current-sources research methodology, reuse-before-reinvention check, attribution-when-building principle, self-critique and self-evaluation gates, quick-start mode, drift recovery, and handoff conventions — is original to this skill.

## Licence

Apache-2.0. See [LICENSE](../../LICENSE).

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md).
