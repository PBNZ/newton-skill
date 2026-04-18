# NOTICE

This repository — **newton-skill** — is licensed under Apache-2.0 (see [LICENSE](LICENSE)).

Parts of it incorporate or build on third-party work that is redistributed or adapted under its own licence terms. This file records those dependencies so that attribution travels with the code, whether a user installs via this marketplace, a release asset, or directly from the repository tree.

## andrej-karpathy-skills (multica-ai)

The Newton skill (`plugins/newton/skills/newton/SKILL.md`) contains material adapted from the **andrej-karpathy-skills** repository.

- **Upstream repository:** <https://github.com/multica-ai/andrej-karpathy-skills>
- **Upstream author:** Jiayuan (GitHub: `forrestchang`)
- **Upstream licence (as declared):** MIT
- **Seed observations:** Andrej Karpathy — <https://x.com/karpathy/status/2015883857489522876>

### Sections in Newton derived from andrej-karpathy-skills

Newton adapts two principles from upstream's `CLAUDE.md`:

- Newton's **"Simplicity in what's produced"** section adapts the "Simplicity First" principle from upstream. The reuse includes near-verbatim wording of the bullet list ("No features beyond what was asked", "No abstractions for single-use code", "No 'flexibility' or configurability that wasn't requested", "No error handling for impossible scenarios") and the spirit of the "if you write 200 lines and it could be 50, rewrite it" rule.
- Newton's **"Editing existing work — surgical changes only"** section adapts the "Surgical Changes" principle from upstream, including the test *"every changed line must trace directly to the user's request"*.

Other Newton content — the opening-move deliberation model, honest-engagement posture, self-critique gate, reuse-before-reinvention methodology, attribution-when-building principle, handoff conventions, self-evaluation gate, drift recovery, and quick-start mode — is original to Newton or drawn from separate prior art, not from andrej-karpathy-skills.

### MIT licence text

At the time of integration, the upstream repository declared itself MIT-licensed in its README but did not include a standalone `LICENSE` file. The standard MIT grant is reproduced below, naming the upstream author as declared:

```
MIT License

Copyright (c) 2025 Jiayuan (forrestchang)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OF OR OTHER DEALINGS IN
THE SOFTWARE.
```

If the upstream authors publish a formal `LICENSE` file that differs from the standard MIT text above, this NOTICE will be updated to mirror it.

### Licence compatibility

Apache-2.0 (this repository) and MIT (upstream) are compatible: MIT-licensed material may be redistributed within an Apache-2.0 work provided the MIT copyright and permission notice travel with it. This NOTICE carries that forward for everyone downstream.

## Three attribution layers

For clarity about who contributed what:

1. **Andrej Karpathy** — original public observations on LLM coding pitfalls, posted on X. Not a contributor to this repository; credited as the source of the underlying ideas.
2. **Jiayuan / multica-ai (`forrestchang`)** — authored the `andrej-karpathy-skills` repository that distils Karpathy's observations into a set of Claude Code guidelines. The MIT grant above is theirs.
3. **PBNZ (this repository)** — integrates parts of those guidelines into the Newton skill, alongside separately-authored material, under Apache-2.0.
