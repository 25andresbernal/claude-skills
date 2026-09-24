---
name: prd-drafter
description: Drafts a product requirements document by first interviewing the user for any missing inputs, then producing a structured PRD covering problem, users, success metrics, scope, non-goals, risks, and open questions. Use when the user asks for a PRD, a product requirements document, a feature spec, or says they need to write up a product idea for stakeholders.
---

# PRD drafter

A PRD is only useful if a stakeholder who was not in the room can read it
and know what ships, for whom, and how success will be judged. Most bad
PRDs fail on one of those three things, not on formatting. Your job is to
get those three things right before you worry about prose.

## Step 1: Gather inputs before drafting

Do not draft from a one-line request. Ask the user for whatever is missing
from this list, in one batch of numbered questions, not one question at a
time:

1. The problem, in the user's own words: what is broken, for whom, how
   often, and what it costs today.
2. The primary user for v1 (a role or behavior, not "everyone").
3. What success looks like: a metric, even a rough one, and a rough
   target or timeframe.
4. Anything that is explicitly out of scope or already decided against.
5. Known constraints: a deadline, a dependency, a team that has to sign
   off.

If the user says "just draft it" or clearly does not have an answer for
one of these, do not stall. Draft with what you have and mark the gap as
an open question in the PRD rather than inventing an answer. Never invent
a metric, a user count, or a competitive claim to fill a gap.

## Step 2: Draft using the template

Use [templates/prd-template.md](templates/prd-template.md) as the
structure. Follow it section by section:

- **Problem**: one paragraph, in the user's terms, with a cost (time,
  money, errors, churn risk) attached. If the cost is only anecdotal, say
  "anecdotal, not yet measured" rather than presenting a guess as data.
- **Users**: exactly one primary user for v1. If the user gives you three
  segments, ask which one this ships for first, or state your
  recommendation and flag it as a decision the user should confirm.
- **Success metrics**: every metric needs a direction and either a target
  or "unknown, needs instrumentation." Include at least one guardrail
  metric, something that should not get worse.
- **Scope**: user-facing outcomes ("users can export a CSV"), not
  implementation details ("add an export endpoint"). Implementation
  belongs in engineering's design doc, not the PRD.
- **Non-goals**: at least one entry. An empty non-goals section means a
  scoping decision was deferred, not that none was needed.
- **Risks and open questions**: every open question gets an owner. An
  open question with no owner will still be open at launch.

## Step 3: Check before presenting

Run the draft against
[reference/prd-quality-checklist.md](reference/prd-quality-checklist.md).
Fix anything that fails silently; do not hand the user a draft with a
known gap you could have closed yourself. Only surface an unresolved item
if it genuinely requires information only the user has.

## Decision rules

- A vague success metric ("increase engagement") is not acceptable output.
  Push back once: ask what engagement means in a number the user already
  tracks, or propose a concrete proxy metric and label it as a proposal.
- If the user gives you a solution instead of a problem ("we need a
  dashboard"), ask what breaks today without it. Write the problem
  section from that answer, not from the solution they asked for. The
  solution can still show up in scope.
- If two stakeholders would disagree about scope based on what the user
  told you, put the disagreement in the risks table instead of picking a
  side silently.

## Anti-patterns

- Writing a scope section that is a feature list with no rationale for
  why each item is in v1.
- Filling success metrics with only lagging, quarter-out numbers (revenue,
  churn) and no leading indicator the team can see within weeks.
- Treating "non-goals" as a restatement of scope in the negative. A good
  non-goal names something a reader would otherwise assume is included.
- Fabricating a user quote, a percentage, or a competitor detail because
  the draft "reads better" with one. Mark it VERIFY or leave it out.
