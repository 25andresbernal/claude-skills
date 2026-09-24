# PRD quality checklist

Run every draft against this list before presenting it. Fix what fails
before showing the PRD to the user; do not ask the user to fix it for you
unless the fix requires information only they have.

## Problem

- [ ] States who has the problem and how often, not just that it exists.
- [ ] Describes the cost of the problem today (time, money, errors, risk),
      even if the cost is only roughly known.
- [ ] Does not already describe the solution. A problem statement that
      contains the word "should" or names a UI element is usually
      describing the fix, not the problem.

## Users

- [ ] Names exactly one primary user for v1. "Everyone" is not a primary
      user.
- [ ] The primary user is described by a role or behavior ("users who hit
      the free-tier limit mid-project"), not a demographic.

## Success metrics

- [ ] Every metric names a direction and either a target number or an
      explicit "unknown, needs instrumentation before launch."
- [ ] At least one metric is a leading indicator the team can see within
      weeks, not only a lagging outcome (revenue, churn) that takes a
      quarter to move.
- [ ] At least one guardrail metric exists, something that should not get
      worse. A PRD with only up-and-to-the-right metrics has not thought
      about what it might break.

## Scope and non-goals

- [ ] Every scope item is written as a user-facing outcome, not an
      implementation detail ("users can export a CSV," not "add an export
      endpoint").
- [ ] Non-goals section has at least one entry. A PRD with an empty
      non-goals section has not made a scoping decision, it has deferred
      one.
- [ ] Nothing in scope contradicts something in non-goals.

## Risks and open questions

- [ ] Every open question has an owner. An open question with no owner
      will still be open at launch.
- [ ] At least one risk considers what happens if the success metric does
      not move, not only technical or timeline risk.

## Numbers and claims

- [ ] No invented user counts, percentages, or revenue figures. Anything
      not confirmed by the user or supplied source material is marked
      flagged as unconfirmed or written qualitatively instead.
- [ ] No competitor or customer claims that were not in the input material.

## Overall

- [ ] A stakeholder who was not in the room could read this PRD and know
      what ships, who it is for, and how success will be judged, without
      asking a follow-up question about any of those three things.
