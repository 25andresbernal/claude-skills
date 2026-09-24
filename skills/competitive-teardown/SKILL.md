---
name: competitive-teardown
description: Produces a structured teardown of a competitor product covering positioning, pricing, onboarding, core loop, gaps, what to steal, and what to avoid, based only on material the user provides or public pages they point to. Use when the user asks to analyze a competitor, do a competitive teardown, or compare their product against another company's.
---

# Competitive teardown

The single rule that matters more than the template: every claim in the
output must trace to something the user gave you or a page you were
explicitly pointed at and actually read. Anything else is a guess, and a
guess presented as a fact is worse than no teardown at all, because it
will get repeated as if it were verified.

## Step 1: Confirm what you have to work with

Before drafting, check what material is available:

- Screenshots, PDFs, or text the user pasted directly.
- Specific URLs the user gave you (their pricing page, their onboarding
  flow, a review site).
- If you have a browsing tool available and the user asked you to look
  something up, only visit pages the user named or that are one click
  from a page they named (for example, the pricing link from their
  homepage). Do not go searching the open web for claims to fill in gaps;
  that turns "based on what you gave me" into "based on what I found,"
  which the user did not ask for and cannot verify.

If the user names a competitor with no material and no URL, ask for at
least a homepage and pricing page link, or ask them to paste what they
want covered. Do not proceed from general knowledge of the competitor
alone. General knowledge of a product is frequently stale, and a teardown
built on stale knowledge reads as current when it is not.

## Step 2: Fill the template section by section

Use [templates/teardown-template.md](templates/teardown-template.md).
Start with the sources list at the top and keep it updated as you use
each source; the sources list is not decoration, it is what makes every
later claim checkable.

For each section, write only what the source material supports:

- **Positioning**: their stated claim, not your read of their strategy.
- **Pricing**: what is written, tier by tier. Anything inferred (for
  example, guessing what an "Enterprise, contact us" tier costs) gets
  marked `[UNVERIFIED]` inline, not stated as fact.
- **Onboarding**: only what was observed or shown in the material. If no
  onboarding material was provided, write "not covered, no source
  material provided" rather than describing a generic onboarding flow.
- **Core loop**: describe it as steps a user repeats, inferred from what
  the product does per the source material, not a feature list.
- **Gaps**: only from evidence (a missing feature visible in the material,
  a stated complaint if review sources were given). If no gap evidence
  exists, say so rather than inventing a plausible-sounding weakness.

## Step 3: Write "what to steal" and "what to avoid"

Every entry in these two sections must point back to a specific claim
made earlier in the teardown. If you cannot point to the section and
evidence that supports a "steal" or "avoid" entry, it does not belong in
the output. These sections are the most likely place for unsupported
opinion to creep in; hold them to the same sourcing bar as the rest.

## Step 4: Close with what's unverified

The "Unverified or out of scope" section is not optional. List anything
relevant that could not be confirmed: pricing not publicly listed,
architecture, team size, funding, user counts. This section exists so the
reader knows the boundary of what this teardown actually established.

## Decision rules

- If the source material conflicts with something you recall generally
  about the competitor (a price that seems out of date, a feature you
  believed they didn't have), trust the source material and note the
  discrepancy rather than silently going with prior knowledge or silently
  going with the source. Flag it: "source states X; this may have changed
  since general knowledge of this product was last current."
- If the user's own product is being compared, do not editorialize about
  which is better. State what each does per the material and let the
  "what to steal" and "what to avoid" sections carry the judgment,
  explicitly and with evidence.
- If a section has no supporting material at all, write that section as
  "not covered" rather than deleting it. A missing section that is
  clearly marked is more useful than one that quietly disappeared.

## Anti-patterns

- Presenting a guess about pricing, user counts, or architecture as a
  stated fact instead of marking it `[UNVERIFIED]`.
- Writing "their onboarding is bad" or "their UX is confusing" without
  citing the specific screen, step, or quote that supports it.
- Filling gaps in the material from general or training knowledge of the
  competitor without flagging that the information may be outdated.
- Treating a single negative review as a confirmed product-wide gap
  without noting it is one data point.
