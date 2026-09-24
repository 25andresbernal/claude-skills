---
name: eval-rubric-writer
description: Turns a product spec or a set of agent failure reports into an eval scorecard with weighted dimensions, thresholds, and test cases, output in a format compatible with the agent-evals framework (scorecard.yaml and cases.yaml). Use when the user wants to define what good looks like for an agent or feature, build a regression test suite, or turn bug reports into eval cases.
---

# Eval rubric writer

An eval scorecard is only useful if it can catch the failures that
already happened and would embarrass the team if they happened again.
Start from real failure reports when they exist; only invent cases from a
spec when there is no failure history yet.

Output must match the schema used by
[agent-evals](https://github.com/25andresbernal/agent-evals) exactly, so
it can be dropped into that framework's `run` command with no editing.
The complete field-by-field schema is in
[reference/scorecard-schema.md](reference/scorecard-schema.md). Read it
before writing the first scorecard.yaml or cases.yaml; do not guess field
names from memory.

## Step 1: Gather the inputs

Ask for whichever of these the user has not already provided:

1. What the agent or feature is supposed to do, in one or two sentences.
2. Known failure reports, bug tickets, or specific bad outputs seen so
   far. These become regression cases and matter more than anything you
   would invent.
3. What would be worse than a wrong answer: an unsafe tool call, an
   overpromise, a compliance issue. This shapes which dimensions need the
   highest weight, not just which exist.
4. Any existing budget for cost or latency per call, if relevant.

## Step 2: Define dimensions

Map what matters to a small number of dimensions, typically three to six.
Common dimensions: `task_success` (did it do the thing), `tool_correctness`
(did it call the right tool correctly, if it calls tools), `quality`
(an `llm_judge` dimension for tone, accuracy, or anything a string match
cannot check), `cost`, `latency`.

Weight dimensions by what would most harm the user or the business if
that dimension failed, not by how easy the dimension is to measure. A
support agent that is fast and cheap but gives unsafe advice should not
pass because cost and latency carry too much weight.

Set both a `weight` and a `threshold` per dimension. The weight determines
how much a dimension counts toward the overall average; the threshold is
checked independently, so one strong dimension cannot mask a specifically
weak one. Weights across all dimensions must sum to 1.0.

## Step 3: Write cases

Prioritize in this order:

1. **Regression cases from real failures.** For every failure report the
   user gave you, write a case that reproduces the input and asserts the
   correct behavior. Put the source of the failure in the case's `notes`
   field.
2. **Tier-1 happy paths.** The two or three most common, highest-volume
   requests the agent should nail every time.
3. **Edge cases.** Ambiguous input, missing information the agent needs
   to ask for, and cases where two plausible behaviors compete (state in
   `notes` why one is correct).

Every case must assert something: `expected_output_contains`,
`expected_output_exact`, or a non-empty `expected_tool_calls`. A case with
none of these does not test anything and should not ship.

Use `expected_tool_calls: []` deliberately for any case where the correct
behavior is to not call a tool (for example, an ambiguous request that
should prompt for clarification instead of acting).

## Step 4: Self-check against the schema

Before presenting scorecard.yaml and cases.yaml, run the validation
checklist at the bottom of
[reference/scorecard-schema.md](reference/scorecard-schema.md). Fix
anything that fails; in particular, confirm weights sum to 1.0 and every
case asserts something.

Use [templates/scorecard-template.yaml](templates/scorecard-template.yaml)
and [templates/cases-template.yaml](templates/cases-template.yaml) as the
starting structure, replacing every placeholder in brackets.

## Decision rules

- If the user gives you a spec but no failure reports, write cases from
  the spec's stated requirements, and tell the user the suite will get
  stronger once real failures start feeding regression cases back in.
- If a dimension would require a judge model to score something a plain
  string match could check instead (for example, "does the response
  mention the order number," which `task_success` with `contains` mode
  already covers), do not add an `llm_judge` dimension for it. Reserve
  `llm_judge` for qualities that genuinely need judgment: tone, whether an
  explanation is actually clear, whether the agent overpromised.
- If the user has not stated what "unsafe" or "unacceptable" means for
  this specific agent, ask rather than assuming a generic definition. A
  scorecard for a support bot and one for a code-execution agent have
  very different definitions of a critical failure.

## Anti-patterns

- A single mega-dimension like "overall quality" that hides which
  specific behavior is failing. Split it into the dimensions that
  actually matter.
- Weights that do not sum to 1.0, or a scorecard with only one dimension
  weighted at 1.0, which defeats the point of a weighted scorecard.
- Thresholds set at 1.0 across the board, which fail on the first near
  miss and tend to get quietly disabled rather than genuinely met.
- Cases copied from documentation examples instead of real usage, when
  real failure reports were available and went unused.
- Vague rubric text for `llm_judge` dimensions ("rate the quality") that
  gives the judge model no way to distinguish a 0.3 from a 0.7. State
  concretely what a 1.0 and a 0.0 response each look like.
