# [Feature or product] launch checklist: [Internal pilot | Beta | GA]

Target launch date: [date]
Launch owner: [name, the one person accountable for the go/no-go call]

## Go/no-go gates

Hard blockers. The launch does not proceed until every row here is
checked, or the launch owner explicitly accepts the risk in writing.

| Gate | Owner | Status | Notes |
|---|---|---|---|
| [gate] | [name or role] | Not started / In progress / Done | |

## Tracked, not blocking

Should be done, but a gap here is a judgment call for the launch owner,
not an automatic stop.

| Item | Owner | Status | Notes |
|---|---|---|---|
| [item] | [name or role] | Not started / In progress / Done | |

## Rollback plan

Trigger conditions: [what observed behavior triggers a rollback]
Rollback owner: [name]
Rollback mechanism: [feature flag, revert, config change, and how long it
takes to take effect]
Last tested: [date, or "not yet tested" if true]

## Communications

Internal: [who is told, when, through what channel]
External: [who is told, when, through what channel, or "none for this
launch stage"]

## Post-launch check-in

Scheduled for: [date, typically a fixed short interval after launch]
What we will look at: [the specific metrics or signals, not "how it's
going"]
