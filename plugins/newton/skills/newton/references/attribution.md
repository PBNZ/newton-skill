# Attribution when building on others' work

*Loaded from Newton's SKILL.md when Newton produces something that incorporates or builds on third-party work — code, wording, ideas, patterns, another skill or agent, someone else's published observations. Attribution travels with the reuse. This is the second half of reuse-before-reinvention: having found something worth reusing, close the loop by crediting it.*

## Licence obligations come first

If the reused material has a licence, follow it.

- MIT and BSD require copyright notice preservation.
- Apache-2.0 requires notice preservation and a `NOTICE` file where attribution notices are declared.
- GPL / AGPL carry copyleft implications that may affect the containing work.

If the licence isn't quickly identifiable, flag that — don't guess, and don't assume *"it's on GitHub so it's probably fine"*.

## Community norms apply even where no licence compels them

Substantial reuse of someone's ideas, framing, or unusual wording deserves credit even when nothing legal requires it. *"Adapted from X"* or *"building on Y's observations about Z"* belongs in the output or its README, not in silent internal awareness.

## Be specific about what was borrowed

Vague *"thanks to the community"* credit is worse than none — it implies attribution where specificity would show where originality ends and derivation begins. Name the section, the idea, the pattern, so readers can trace the lineage.

## Place attribution where it survives redistribution

- A `SKILL.md` credits footer travels with the skill when it's distributed as a release asset.
- A repository `NOTICE` file survives forks and mirrors.
- A plugin-level README reaches users who install that plugin.
- Top-level marketing READMEs are the wrong place for licence-driven attribution — too easy to drop, too easy to overclaim influence for rhetorical effect.

## Distinguish the layers of credit when they're in play

- **Originator of the idea** — who first observed it.
- **Author of the material you actually reused** — whose wording or structure you integrated.
- **You as integrator.**

Credit each at the level of specificity their contribution warrants.

## The test

If someone asked *"where did the bones of this come from?"*, does the work answer plainly — through a `NOTICE` file, a credits section, a README attribution line, or inline citation — without the user having to guess or dig? If not, the attribution isn't yet doing its job.
