---
name: user-interview-synthesizer
description: Turns raw user interview notes or transcripts into themes with evidence quotes, severity ratings, and a decision-ready summary a product team can act on. Use when the user pastes interview notes, call transcripts, or research recordings' notes and asks for themes, synthesis, key insights, or a summary of user research.
---

# User interview synthesizer

The output of this skill is judged by whether a team can act on it without
rereading the raw notes. That means every theme is a claim with evidence
behind it, not a topic label, and every severity rating is defensible from
the notes themselves, not from a gut feeling.

See [examples/](examples/) for a full worked example: raw notes in
[examples/sample-interview-notes.md](examples/sample-interview-notes.md)
and the synthesis it should produce in
[examples/expected-synthesis.md](examples/expected-synthesis.md). Read the
expected output once to calibrate the bar before synthesizing real notes.

## Step 1: Separate the notes by participant

Identify each distinct participant or session before doing anything else.
Note their role or segment if given. A theme that turns out to come from
one participant repeating themselves across the notes, not multiple
participants, must be labeled as single-participant.

## Step 2: Extract observations as evidence, not paraphrase

Pull direct quotes, not summaries dressed up as quotes. If the notes are
not verbatim (a note-taker's paraphrase rather than a transcript), quote
what is written and note it is paraphrased rather than inventing a more
natural-sounding quote. Every piece of evidence gets attributed to a
specific participant and, where possible, the moment in the session
(what question or event prompted it).

Never attribute a quote to the wrong participant, and never combine
fragments from two participants into one quote.

## Step 3: Cluster into themes

A theme is a claim, not a topic. "Onboarding" is a topic. "Users abandon
onboarding because they can't tell if the free tier will lose their data"
is a theme. Write every theme headline as a specific, falsifiable claim
that the evidence either supports or does not.

Merge observations into one theme only when they share the same
underlying cause, not just the same feature area. Two complaints about
the same screen for two different reasons are two themes.

## Step 4: Rate severity

Use this rubric for every theme, and only this rubric, so ratings are
comparable across a synthesis:

- **Critical**: blocks the core task, no workaround, reported by multiple
  participants.
- **High**: blocks the core task but a workaround exists, or reported by
  one participant with a plausible reason to affect more.
- **Medium**: causes friction or confusion but the task still completes.
- **Low**: a preference or nice-to-have, not a blocker.

State the workaround observed, if any, for every theme. A theme with no
workaround and multiple participants is close to automatically Critical;
a theme from one participant is capped at High unless there is a specific,
stated reason it would generalize.

## Step 5: Write the decision-ready summary

Use [templates/synthesis-template.md](templates/synthesis-template.md).
The decision-ready summary at the top is three to five sentences that
lead with the highest-severity theme and say what the team should do
differently. Write it last, after the themes are final, so it reflects
the actual findings rather than a preconception of what the study would
show.

Always include the "what this research does not tell us" section: sample
size, recruiting bias, and any gap between what was asked and what the
team wants to know. An empty version of this section means it was
skipped, not that there were no limits.

## Decision rules

- If two participants describe what sounds like the same theme but with
  different severity implications (one has a workaround, one does not),
  keep them as one theme and report the range, rather than forcing one
  severity rating that overstates or understates half the evidence.
- If a participant raises something unprompted, say so. Unprompted
  observations are stronger signal than answers to a direct question that
  suggested the topic.
- If the notes include a counter-signal (a participant who explicitly
  does not want the thing other participants are asking for), report it
  as a note under the relevant theme rather than silently dropping it.
  Losing that signal leads to over-building a feature for one segment
  while alienating another.

## Anti-patterns

- Naming a theme after a feature area ("Dashboard") instead of the
  specific claim the evidence supports.
- Inflating severity by assuming a single-participant observation
  generalizes without stating the assumption.
- Writing evidence quotes from memory of "the kind of thing users said"
  instead of what is actually in the notes.
- Skipping the research-limitations section because the sample was small
  and it feels awkward to say so. Small samples are common and fine to
  report; hiding the limitation is what causes bad decisions downstream.
