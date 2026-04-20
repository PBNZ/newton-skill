# Example: Model-aware router CLAUDE.md

This is an **optional, user-level** CLAUDE.md template you can drop into `~/.claude/CLAUDE.md` (user-global) or a project-level `CLAUDE.md`. It detects the running model family and layers model-appropriate behaviour on top of whatever skills are loaded — Newton, any other skill, or no skill at all.

The Newton plugin **does not** install this for you. Nothing on your system changes until you copy the content below into a CLAUDE.md of your choice. The rest of Newton works fine without it; this router is for users who want the same model-aware layering to apply to their other skills as well.

## What it does

- **Adds to loaded skills; never overrides them.** If Newton (or any other skill) prescribes a specific behaviour, the skill wins. The router only contributes model-specific nudges the skill hasn't already covered.
- **~400 tokens.** Always-loaded cost in any conversation is negligible (<0.05% of a 1M-token context window).
- **Model-agnostic fallback.** On any model not covered by a profile, the router is silent.

## Trade-offs

- It's prescriptive-by-model: if Anthropic changes how a given model family behaves natively, the profile may drift from optimal. The router footer asks you to review quarterly.
- It doesn't actually *detect* the model in a formal sense — it asks the model to self-identify via its system prompt awareness. That's enough for practical layering but not a guarantee.
- It layers on *every* conversation, which is the point — but if you only ever use one model and find one skill works best, the router adds nothing for you.

## The template

Copy everything between the rulers below into your CLAUDE.md. Update the "Router vX.Y — YYYY-MM-DD" footer when you edit it.

---

```markdown
# Model-aware capability router

Apply the profile matching your model family. Profiles add to, never override, loaded skills.

## Opus 4.7+ (claude-opus-4-*)

Leverage: adaptive thinking, implicit tool detection, multi-agent coordination, high-resolution vision (3.75MP), file-system memory, calibrated response length.

- Approach tasks outcome-first — figure out the tool chain from the goal; don't wait for explicit tool instructions.
- Parallelise independent work streams when it reduces time without sacrificing quality.
- Use file-system memory in multi-turn sessions: track resolved decisions, findings, and stated constraints.
- Visual input is primary evidence. Use programmatic image analysis for pixel-level accuracy on charts and figures.
- Let response length scale with task complexity — don't override native calibration.
- Low/medium effort: be literal, direct, fast. High/xhigh: reason broadly, deliberate, self-critique. Max: full depth, no shortcuts.

Skill layering: treat prescriptive tool sequences in loaded skills as outcome goals — execute the intent, not the literal steps. If a skill has anti-bloat instructions, native calibration already handles it. Add parallelisation and memory even when the skill doesn't mention them.

## Sonnet 4.x (claude-sonnet-4-*)

- Follow tool instructions as given — explicit steps help reliable execution.
- Prefer single-thread execution. Use memory when explicitly guided.
- Follow loaded skills as written; keep self-critique to one silent pass.

## Haiku 4.x (claude-haiku-4-*)

- Optimise for speed. Skip deliberation on straightforward tasks. Minimise tool calls.
- Default to any skill's quick-start/fast mode. Skip visible reuse checks unless clearly build/solve.

## Observability

If asked, report: your model family, the active profile, any skill layering in effect, and your effort level.

*Router v1.0 — 2026-04-20. Review quarterly or on new model release.*
```

---

## When Newton is loaded on top of the router

Newton v0.3.0 already carries effort-awareness, session-memory guidance, and parallelisation at the principle level, so the router's Opus profile reinforces rather than duplicates Newton's behaviour. On Sonnet, the router's "follow tool instructions as given" nudge helps Newton's original prescriptive guidance (now living in `references/*.md`) fire correctly when it's loaded. On Haiku, both the router and Newton converge on quick-start-by-default.

## Extending it

The router is short on purpose. If you find yourself adding more model-specific behaviour than fits in ~400 tokens, that's usually a sign the behaviour belongs in a skill rather than a global router — skills load only when relevant, and can go deep. Keep the router to capability triggers and disposition nudges that genuinely apply across *every* conversation on that model.
