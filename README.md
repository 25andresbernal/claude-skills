# claude-skills

[![CI](https://github.com/25andresbernal/claude-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/25andresbernal/claude-skills/actions/workflows/ci.yml)

Five Claude Skills that package repeatable PM judgment: drafting a PRD,
synthesizing user interviews, writing an eval scorecard, building a launch
checklist, and running a competitive teardown.

## Why this exists

A PM who uses Claude daily ends up retyping the same instructions every
time: the same reminders about what a good PRD needs, the same rubric for
rating research severity, the same checklist gates for a launch. That
knowledge is worth more as a Skill than as a prompt typed from memory each
time, because a Skill is versioned, reviewable, and gets better with use
instead of drifting a little differently every conversation.

Each skill in this repo is a folder with a `SKILL.md` file plus whatever
templates, reference material, or worked examples it needs. Point Claude
Code or the Claude app at the folder and Claude uses it automatically when
the request matches.

## What each skill produces

| Skill | What it produces | Use it when |
|---|---|---|
| [prd-drafter](skills/prd-drafter/) | A structured PRD: problem, users, success metrics, scope, non-goals, risks, and open questions. Interviews for missing inputs first. | You have a product idea and need something a stakeholder can act on, not a paragraph of prose. |
| [user-interview-synthesizer](skills/user-interview-synthesizer/) | Themes with evidence quotes, a severity rating per theme, and a decision-ready summary. | You have raw interview notes or transcripts and need to know what to act on, not just a recap. |
| [eval-rubric-writer](skills/eval-rubric-writer/) | A `scorecard.yaml` and `cases.yaml`, schema-compatible with [agent-evals](https://github.com/25andresbernal/agent-evals). | You need to define what "good" means for an agent or feature and turn failure reports into regression tests. |
| [launch-checklist](skills/launch-checklist/) | A checklist with named owners, split into go/no-go gates and tracked items, tailored to internal pilot, beta, or GA. | You are planning a launch and need gates that match the actual risk of that launch stage. |
| [competitive-teardown](skills/competitive-teardown/) | A sourced teardown: positioning, pricing, onboarding, core loop, gaps, what to steal, what to avoid. | You need a competitor analysis grounded in material you actually have, not a guess dressed up as research. |

## Install

### Claude Code

Copy or symlink a skill folder into your personal skills directory
(`~/.claude/skills/`) to use it in every project, or into a project's
`.claude/skills/` to share it with a team through that repo.

```bash
git clone https://github.com/25andresbernal/claude-skills.git
cd claude-skills

# One skill, copied
mkdir -p ~/.claude/skills
cp -r skills/prd-drafter ~/.claude/skills/

# One skill, symlinked (updates when you pull this repo)
ln -s "$(pwd)/skills/prd-drafter" ~/.claude/skills/prd-drafter

# All five, in one line
cp -r skills/* ~/.claude/skills/
```

Restart Claude Code, or start a new session, and the skills are available.
Claude triggers each one automatically based on its `description`; you
can also invoke a skill by name if your Claude Code version supports slash
commands for skills.

### Claude app (claude.ai)

Custom Skills are uploaded as zip files under Settings > Features, and
require a plan with code execution enabled (Pro, Max, Team, or
Enterprise). Zip the folder for a single skill, keeping `SKILL.md` at the
root of the zip:

```bash
cd skills/prd-drafter
zip -r ../../prd-drafter.zip .
cd ../..
```

Repeat per skill (or loop over `skills/*/` with the same two commands),
then upload each zip from Settings > Features in the Claude app. Skills
uploaded to the Claude app are per-user; each teammate uploads their own
copy.

## How a skill is structured

Every skill here is a `SKILL.md` file with YAML frontmatter (`name`,
`description`) plus a markdown body of instructions, and most bundle a
`templates/` folder for output structure, a `reference/` folder for
detail that would bloat the main instructions, or an `examples/` folder
showing a worked input and expected output. This follows Anthropic's
progressive disclosure model: Claude reads the frontmatter first, the
full `SKILL.md` only when the skill is triggered, and bundled files only
when the instructions point to them. See the official docs for the
current format and rules: [Agent Skills
overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview),
[authoring best
practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices),
and [Skills in Claude
Code](https://code.claude.com/docs/en/skills).

## Example session

Using [prd-drafter](skills/prd-drafter/), synthetic transcript:

```
> I need a PRD for adding CSV export to our invoicing product.

I need a few things before I draft this:

1. What's broken today without CSV export? Who runs into it, and how
   often?
2. Who is the primary user for v1: bookkeepers pulling data into their
   own tools, accountants, someone else?
3. What would success look like? A number or a rough target is fine.
4. Anything already decided as out of scope?
5. Any deadline or dependency I should know about?

> 1. Users who run their own reconciliation in Excel keep asking support
> for a workaround, maybe 20 tickets a month. 2. Bookkeepers doing monthly
> reconciliation. 3. Not sure of a number, but fewer support tickets on
> this topic would be the signal. 4. No PDF export yet, that's separate.
> 5. Nothing firm.

Here's the draft PRD:

# CSV export PRD

## Problem

Bookkeepers who reconcile invoices in Excel have no way to get invoice
data out of the product except by hand-copying it, which drives
approximately 20 support tickets a month asking for a workaround. The
real cost is bookkeeper time re-entering data and the risk of transcription
errors in reconciliation.

## Users

Primary: bookkeepers doing monthly reconciliation.
Explicitly not for: this PRD does not cover PDF export, which is tracked
separately.

## Success metrics

| Metric | Current | Target | By when | How measured |
|---|---|---|---|---|
| CSV-export support tickets | ~20/month (baseline, anecdotal) | Reduced, exact target TBD | 60 days post-launch | Support ticket tags |

Guardrail metrics: page load time on the invoice list should not regress.

[...PRD continues with Scope, Non-goals, and Risks and open questions...]

One open item before this is final: we don't have a confirmed numeric
target for the ticket reduction, only "fewer." I've flagged that as an
open question with you as owner rather than inventing a number.
```

## Design decisions

A few choices worth knowing about, and the tradeoff behind each one.

- **Every skill interviews before it drafts, and refuses to fabricate an
  input it wasn't given.** The tradeoff is a slower first turn: the user
  answers questions instead of getting instant output. That is
  deliberate. A PRD or teardown built on invented metrics or guessed
  facts is worse than one that took two extra minutes to ground.
- **eval-rubric-writer's output is locked to the agent-evals schema, not
  a generic scorecard format.** A scorecard nobody can run is a scorecard
  nobody trusts. The tradeoff is that this skill is opinionated about one
  specific downstream tool rather than staying framework-agnostic.
- **Templates and reference material live in separate files, not inside
  SKILL.md.** This follows the documented progressive-disclosure pattern:
  Claude only loads a template or a schema reference when the task
  actually needs it, which keeps every SKILL.md focused and keeps the
  five skills from competing for context space with each other.
- **competitive-teardown refuses to fill gaps from general model
  knowledge about a named competitor.** Training knowledge about a
  specific product goes stale, and stale information stated confidently
  is worse than an honest "not covered, no source material provided."
- **validate_skills.py is stdlib-only Python, no dependencies.** A CI gate
  that can fail because a linting library changed its API is worse than
  no gate at all. This one only needs to keep running.

## Roadmap

- Add skills as real PM work surfaces patterns worth generalizing, in the
  same spirit as this repo's sibling,
  [enterprise-ai-playbook](https://github.com/25andresbernal/enterprise-ai-playbook).
- A shared glossary reference if terminology drifts across skills as more
  get added.
- Worked examples for the remaining skills, in the same input-and-expected-
  output format user-interview-synthesizer already uses.

## Contributing

Issues and pull requests are welcome. Before opening a pull request:

```bash
python scripts/validate_skills.py
```

Follow the structure of an existing skill: required frontmatter (`name`
matching the folder, a specific `description` stating what and when),
concrete decision rules, and an anti-patterns section, not generic advice.
No emojis, no em dashes, anywhere in the repository.

## License

MIT. See [LICENSE](LICENSE).
