---
name: launch-checklist
description: Generates a launch checklist tailored to launch type, internal pilot, beta, or general availability, with named owners and explicit go/no-go gates for each stage. Use when the user is planning a product launch, rollout, or release and needs a checklist, launch plan, rollback plan, or go/no-go criteria.
---

# Launch checklist

A checklist with no owner on a row is a checklist that will still be
incomplete at launch. Every gate in the output needs a name or a role
attached, and every gate needs to be labeled as a hard blocker or a
tracked item, not left ambiguous.

## Step 1: Confirm launch type

Ask if it is not already stated. The three types below need meaningfully
different checklists; do not reuse a beta checklist for a GA launch or
the reverse.

- **Internal pilot**: employees or a small named group, not the public.
  Lightest checklist. Still needs internal comms and a feedback channel,
  does not need legal, compliance, or external comms.
- **Beta**: external users, but opted in, limited, or clearly labeled as
  beta. Needs a support runbook (what the support team does when a user
  hits a problem), a feedback channel, and a kill switch. Does not
  necessarily need full legal or compliance review, but ask if the
  product touches regulated data before assuming it does not.
- **General availability (GA)**: everyone. Needs the full set: legal or
  compliance review if the product touches user data, payments, or a
  regulated domain, monitoring and alerting in place before launch, a
  tested rollback path, an external comms plan, and on-call coverage for
  at least the first 48 to 72 hours.

## Step 2: Gather owners and inputs

Ask for whatever is missing:

1. Owner for each relevant function: engineering, support, and, for beta
   or GA, legal or compliance if applicable, and marketing or comms if
   there is external communication.
2. Whether a rollback mechanism exists (feature flag, config toggle, full
   revert) and whether it has been tested.
3. The specific success criteria or metrics that will be checked after
   launch, not "see how it goes."
4. Anything already known to be incomplete or risky, so it lands in the
   checklist rather than being discovered at launch.

If the user does not have an owner for a required gate, do not leave the
row blank. Write "unassigned, needs an owner before launch" so the gap is
visible rather than silently dropped.

## Step 3: Build the checklist

Use
[templates/launch-checklist-template.md](templates/launch-checklist-template.md).
Split items into two tables:

- **Go/no-go gates**: hard blockers. The launch does not proceed until
  every row is done, or the launch owner explicitly accepts the risk in
  writing (record that acceptance in the Notes column, do not just check
  the box).
- **Tracked, not blocking**: should be done, but a gap is a judgment call
  for the launch owner rather than an automatic stop.

Tailor which items are gates versus tracked based on launch type from
Step 1. For example, a tested rollback path is a gate for GA and should
usually be tracked-not-blocking for an internal pilot, where the blast
radius of a bad rollout is small.

Always fill in the rollback plan section, even for an internal pilot. "No
rollback needed, we will just turn the pilot off" is a valid answer, but
it should be written down rather than left blank.

## Decision rules

- A GA launch with no legal or compliance review and no stated reason one
  is unnecessary goes in the go/no-go gates table, not tracked-not-blocking.
- If the user asks for a checklist but has not told you whether the
  rollback mechanism has been tested, do not assume it has. Write "not
  yet tested" and put it in gates for GA, tracked for beta or pilot.
- If two people are named as owner for the same gate, ask who is
  accountable if it slips. A gate with two owners functions like a gate
  with none.

## Anti-patterns

- Items with no owner, or an owner written as "the team" instead of a
  name or role.
- Copying a GA-level checklist onto an internal pilot, which slows down a
  low-risk launch for no reason, or copying a pilot-level checklist onto
  a GA launch, which under-scopes real risk.
- A rollback plan section that says only "we can always roll back"
  without naming the mechanism, the owner, or how long it takes.
- A post-launch check-in with no specific metrics named, which in
  practice means no one checks anything.
