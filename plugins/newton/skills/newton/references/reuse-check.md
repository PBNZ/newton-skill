# Reuse-check methodology

*Loaded from Newton's SKILL.md for Build / Solve requests — before generating anything substantial.*

1. **Check the current environment's native capabilities and skills first.** There may already be a skill or tool that handles the task better than a custom solution — document-creation skills (`docx`, `xlsx`, `pptx`, `pdf`), visualisation tools, code execution, maps/places, frontend design guidance, and so on. If the task is "build a presentation", the `pptx` skill is the starting point; if it's "create a fillable form PDF", the `pdf` skill is; if it's "diagram this flow", the visualiser is. Check what's actually available in context before assuming.

2. **Check the user's past chats when the context suggests they may have solved this before.** Search prior conversations with content keywords from the current request. If they've already built something similar, surface it — *"you built a version of this on [date]; want to reuse, adapt, or start fresh?"*

3. **Check what exists in the wider world.** Look for:
   - Built-in features of the platform, tool, or language the user is on.
   - Official first-party modules, samples, or templates.
   - Well-maintained libraries or packages on the relevant registry (npm, PyPI, PSGallery, NuGet, crates.io, Maven Central, etc.).
   - Standard patterns or accepted answers for the problem.

4. **Report findings visibly, not silently.** Brief — what was found, what it does, how it maps to the user's need.

5. **Recommend one of:**
   - **Use as-is** — if an existing solution directly fits.
   - **Modify** — if an existing solution is close but needs adjustment (say what).
   - **Build fresh** — if existing options don't fit (say why, specifically).

6. **Name what "done" looks like.** For substantive Build / Solve work, briefly state the success criteria — what the output needs to do, what would show it works. One or two sentences, not a full spec. Vague criteria ("make it work") produce vague results that cost extra clarification turns; specific criteria let Newton build and self-verify in one pass. Skip this for trivial requests where success is self-evident — imposing it there is ceremony.

7. **Then, only then, build** (or hand off — see `references/handoff.md`).

## Parallelise independent sub-tasks

When the reuse check splits into independent sub-tasks — researching two unrelated libraries, checking past chats while running a web search, comparing multiple candidate solutions — dispatch them in parallel rather than serialising. Serial-by-default wastes latency when the pieces don't depend on each other.

## Defensible recommendations only

*"Build fresh because existing options don't quite match your exact constraints"* is not defensible unless Newton names the constraint and shows the mismatch. Vague mismatch claims are the build-trap: they license fresh work without earning it.

## Simplicity in what's produced

When Newton does build, produce the minimum that solves the actual problem, nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or configurability that wasn't requested.
- No error handling for impossible scenarios.
- If the first pass is bloated, rewrite it smaller before shipping.

A 200-line script that could be 50 is the same failure mode as a 400-word answer that could be 100 — bulk signalling effort rather than earning its place. Before shipping anything non-trivial, apply the senior-engineer check: would someone experienced in this domain call this overcomplicated? If yes, simplify.
