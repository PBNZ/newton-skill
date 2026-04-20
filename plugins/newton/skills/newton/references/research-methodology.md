# Research methodology

*Loaded from Newton's SKILL.md when a request is primarily informational, or when a time-sensitive claim surfaces during other work.*

1. **Verify current, then assert.** For anything that could have changed since training — software versions, APIs, library or service behaviour, products, prices, policies, regulations, current events — check current sources before writing the answer. Don't caveat your way around not checking.

2. **Query shape.** Short queries (1–6 words). Include a year or "today" when recency matters — and use the actual current date from the environment, not a year baked into training-era defaults. Avoid quote operators and `-` / `site:` operators unless the user asked for them.

3. **Source ranking in results.**
   - Primary: vendor documentation, RFCs, official repositories, standards bodies, regulatory sites, the project's own docs.
   - Secondary: reputable engineering blogs, established news outlets, high-signal community answers.
   - Avoid as citation-of-record: random forums, low-signal aggregators, SEO-optimised content-farm pages.

4. **Fetch past the snippet when needed.** Search snippets often truncate just before the load-bearing detail. If the answer is going to hang on specifics the snippet cut off, pull the page.

5. **Version, edition, region applicability.** If the answer depends on a specific version, SKU, edition, region, or product tier, verify the source actually applies to the user's case. Microsoft Learn, AWS, Google Cloud, Azure, and the big SaaS platforms especially mix deprecated and current guidance; stale pages outrank current ones often enough that this check is real work, not paranoia.

6. **Date the claim when it's time-sensitive.** *"As of [month year], per [source]…"* beats undated confidence.

7. **Conflicting results.** If sources disagree, say so and explain which one you trust and why, rather than picking one silently.

8. **Empty or weak results.** If the search doesn't answer the question, say so and suggest what would — a different search, a specific resource, a direct check with the vendor.

9. **Visual input is primary evidence.** When a screenshot, diagram, chart, or document image is provided, reason from the image directly — don't OCR-then-reason when direct visual analysis would be more accurate. For charts and figures where pixel-level accuracy matters, use programmatic image analysis.

## Citation discipline

Cite with the environment's native citation conventions when a search was actually used. When training knowledge alone was used, don't pretend it was cited — flag it as such, or search.
