# Newton

<p align="center">
  <img src="docs/assets/newton-hero.svg" alt="Newton — think carefully, push back honestly, ship what's earned" width="720">
</p>

**Think carefully. Push back honestly. Ship what's earned.**

Newton is a reasoning and sparring partner for any agent that reads the [Agent Skills](https://agentskills.io/) standard. It's not a domain expert — it's a posture: when you want rigour over speed, honest pushback over flattery, current sources over training-data assumptions, and reuse-before-rebuild over fresh scripts that duplicate what's already there.

Newton is **opt-in by explicit invocation**. It only activates when you summon it by name ("Newton:", "Newton —", "Newton, quick: …"). The rest of the time your agent behaves normally.

## What Newton does

- **Honest engagement, not performed agreement or performed scepticism.** Pushes back when there's a real reason; agrees plainly when you're right; flags its own uncertainty instead of confabulating a plausible-sounding answer.
- **Current authoritative sources.** For anything that could have changed since training — versions, APIs, prices, regulations, current events — Newton searches before asserting, prefers primary sources, and notes dates when claims are time-sensitive.
- **Reuse before reinvention.** Before building anything substantial, Newton checks what already solves it (platform features, first-party samples, well-maintained libraries, your own past work) and reports findings before generating new code.

## Install

Pick the row for your tool:

| Surface | How to install | Auto-updates? |
|---|---|---|
| **Claude Code** | `/plugin marketplace add PBNZ/newton-skill` then `/plugin install newton@newton-skill` | Yes — `/plugin update` |
| **Claude Cowork** | Same as Claude Code (shared plugin system) | Yes — `/plugin update` |
| **Claude.ai / Desktop** | Settings → Skills → Add skill → upload [`plugins/newton/skills/newton/SKILL.md`](./plugins/newton/skills/newton/SKILL.md) from the [latest release](https://github.com/PBNZ/newton-skill/releases/latest) | Manual — re-upload on new releases |
| **Claude API** | Attach the release's `SKILL.md` asset via the [Skills API](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) | Manual |
| **Any Agent-Skills tool** (`gh skill`) | `gh skill add PBNZ/newton-skill` | Yes — `gh skill upgrade` |
| **Cursor** | Copy [`tool-rules/.cursorrules`](./tool-rules/.cursorrules) to your workspace root as `.cursorrules` | Manual |
| **Windsurf** | Copy [`tool-rules/.windsurfrules`](./tool-rules/.windsurfrules) to your workspace root as `.windsurfrules` | Manual |
| **Cline** | Copy [`tool-rules/.clinerules`](./tool-rules/.clinerules) to your workspace root as `.clinerules` | Manual |
| **GitHub Copilot** | Copy [`tool-rules/copilot-instructions.md`](./tool-rules/copilot-instructions.md) into your repo as `.github/copilot-instructions.md` | Manual |

The files under [`tool-rules/`](./tool-rules/) are **generated** from the canonical [`SKILL.md`](./plugins/newton/skills/newton/SKILL.md) by [`scripts/generate-rule-files.py`](./scripts/generate-rule-files.py); CI fails the build if they drift. Whichever surface you install through, you're running the same methodology.

## When to use Newton

Use Newton when you're about to make a decision you'd regret getting wrong. Architecture calls, thesis-level arguments, a multi-week plan — anything where the point isn't quick-and-polished and you'd rather find the weak spot before you build on it than after. Newton's opening move is to check whether the framing holds up before starting the work, and its closing move is to re-read its own draft and surface the weakest part instead of shipping past it.

Use Newton when you need current authoritative information. Software versions, API behaviour, regulations, prices, current events — anything that moves. Newton treats time-sensitive claims as needing a search, not a recollection, and prefers vendor docs, RFCs, and standards bodies over SEO-optimised aggregators. It flags source dates when it matters.

Use Newton when you're asking *how do I X* and you suspect the answer is "something already does this". Before generating a fresh script, Newton checks what's already in your platform, your available skills, a community-standard library, or your own prior work — and reports back with a recommendation (use-as-is, modify, or build-fresh with a specific reason) before building anything.

Skip Newton for trivial tasks that just need an answer. That's what its quick-start mode exists for (`Newton, quick: …`) — principles applied silently, ceremony skipped.

## What makes Newton different from just prompting "be more critical"

"Be more critical" produces performed scepticism — manufactured objections that sound rigorous but don't change the answer. Newton is calibrated the other way: push back when there's a real reason, agree plainly when you're right, and flag genuine uncertainty rather than either hedging or arguing to seem sharp. The skill spells out what "real reason" looks like, what self-critique-before-delivery means in practice, and when clarifying questions are load-bearing versus ceremonial — so the behaviour is consistent turn-to-turn rather than drifting with each prompt.

Newton also operationalises reuse-before-rebuild, current-sources research, surgical editing, and handoff-when-scope-outgrows-the-chat as explicit sub-routines the agent runs, not as vibes. That's what makes it a *skill* rather than a prompt: the agent loads the methodology once and applies it consistently, with visible reuse-check reports and dated sources, rather than re-deriving the disposition from your tone every turn.

## Using Newton on Opus 4.7

Newton is model-agnostic by design — the same methodology runs on Opus, Sonnet, and Haiku — but v0.3.0 is tuned so Opus 4.7's native strengths (adaptive thinking, implicit tool detection, session memory, parallel execution, high-resolution vision) are leveraged rather than fought. Tool guidance is outcome-oriented instead of prescriptive; Newton defaults toward quick-start at low/medium effort and full methodology at high/xhigh; independent sub-tasks parallelise; multi-turn sessions can use file-system memory; visual input is treated as primary evidence.

If you want model-specific behaviour layered on top of *every* skill — not just Newton — see [`docs/examples/router-claude-md.md`](./docs/examples/router-claude-md.md) for an optional user-level CLAUDE.md template. It's opt-in: copy into your `~/.claude/CLAUDE.md` or a project-level CLAUDE.md. The plugin does not install it for you.

## Future development

Planned after v0.3.0:

- **Additional-language READMEs.** This README is English-only. Translations (and a landing-page language switcher) are tracked in the [issues](https://github.com/PBNZ/newton-skill/issues).
- **Sub-agent decomposition.** Newton's research, reuse-check, and self-critique passes are candidates for dedicated sub-agents — keeping the top-level conversation lean while heavy work happens in focused contexts. v0.3.0 shipped a principle-level parallelisation note as the stepping stone; the dedicated-subagent work is deferred to a later release.

## Licence

[Apache-2.0](./LICENSE).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). All changes to Newton's behaviour go through edits to the canonical [`plugins/newton/skills/newton/SKILL.md`](./plugins/newton/skills/newton/SKILL.md); the surface-specific files under [`tool-rules/`](./tool-rules/) regenerate from it via [`scripts/generate-rule-files.py`](./scripts/generate-rule-files.py).
