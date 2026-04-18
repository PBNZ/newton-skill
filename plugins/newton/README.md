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

## Licence

Apache-2.0. See [LICENSE](../../LICENSE).

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md).
