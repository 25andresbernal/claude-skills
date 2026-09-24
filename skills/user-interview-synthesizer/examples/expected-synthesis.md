# Ledgerly payment reminders synthesis

Sessions analyzed: 4 (P1 graphic designer, P2 copywriter, P3 web
developer, P4 photographer)
Date range: single week (see interviewer notes)
Analyst: user-interview-synthesizer (worked example)

This is the expected output when
[sample-interview-notes.md](sample-interview-notes.md) is run through this
skill, shown so you can judge whether the skill is producing synthesis at
this level before you trust it on real notes.

## Decision-ready summary

The highest-priority problem is not the reminder feature itself, it is
that Ledgerly gives freelancers no way to see which invoices are overdue
without building their own tracking outside the app. Fix invoice
visibility first (a due-date sort or an overdue list on the dashboard);
the existing reminder toggle is secondary and currently undiscoverable
even to users who would want it. A smaller, separate opportunity is
cutting repeat data entry for retainer clients.

## Themes

### Theme 1: Freelancers can't tell which invoices are overdue without building their own tracking outside Ledgerly

Severity: Critical
Participants affected: 3 of 4 (P1, P3, P4)

Three of four participants described the same gap from different angles:
Ledgerly does not surface overdue status anywhere a user naturally looks.
P1 and P4 have no systematic workaround and only notice a late invoice
when the client brings it up or weeks have passed. P3 has built a manual
weekly export-and-sort process specifically to compensate.

Evidence:
- "I send the invoice and then I just... forget until the client emails
  me asking why I'm bugging them, except I never bugged them. I have no
  idea who's overdue unless I open a spreadsheet I keep on the side."
  (P1, describing current process)
- "Honestly by the time I notice an invoice is late it's been like three
  weeks." (P4, asked what currently happens with late invoices)
- "Ledgerly's dashboard doesn't sort by due date, only by invoice number,
  so I export to CSV every Monday and sort it myself in Excel." (P3,
  describing his weekly routine)

Workaround observed: P1 maintains a separate Google Sheet; P3 exports to
CSV and re-sorts weekly (about 10 minutes); P4 has no workaround and
discovers lateness by delay alone.

### Theme 2: The built-in reminder feature is undiscoverable and unverifiable, so users who want it don't trust or find it

Severity: High
Participants affected: 2 of 4 (P1, P2)

This is a distinct problem from Theme 1: a reminder feature already
exists, but it failed two different participants in two different ways.
P1 did not know it existed. P2 knew, tried it once, and had no way to
confirm it had actually sent anything, including missing the one UI
element (a "last sent" timestamp) that would have told her.

Evidence:
- "I didn't even know Ledgerly could send reminders until you just said
  that. Is that a real feature?" (P1, when asked about reminders)
- "I turned it on for one invoice and then never checked if it actually
  sent anything. No idea if it worked." (P2, describing her one attempt
  to use reminders)
- P2 did not notice the "last sent" timestamp field on the reminder
  settings screen until the interviewer pointed it out during the
  session.

Workaround observed: P2 manually re-sends the invoice PDF by email
instead of relying on the automated reminder.

Note: P3, who was not counted in this theme, said he prefers messaging
retainer clients personally over an automated reminder ("a robot email
feels cheap for a retainer client"). Any fix here should stay optional,
not force reminders on by default.

### Theme 3: Re-entering client details for repeat clients slows down invoice creation

Severity: Medium
Participants affected: 1 of 4 (P4, unprompted)

Only one participant raised this, and it was unprompted rather than in
response to a question about invoice creation. It is plausible this
affects other users with repeat clients, since P3 independently mentioned
having "several retainer clients," but that is an inference, not a
confirmed pattern; this sample cannot confirm prevalence beyond P4.

Evidence:
- "Every single time I have to retype the client's address. It's the same
  five clients." (P4, unprompted, while discussing the invoice creation
  flow)

Workaround observed: none reported; P4 re-enters details manually each
time.

## Severity rubric used

- Critical: blocks the core task, no workaround, reported by multiple
  participants.
- High: blocks the core task but a workaround exists, or reported by one
  participant with a plausible reason to affect more.
- Medium: causes friction or confusion but the task still completes.
- Low: a preference or nice-to-have, not a blocker.

## What this research does not tell us

All four participants were recruited from the Ledgerly beta mailing list,
which skews toward newer, feedback-engaged users; this sample says
nothing about long-tenure users who did not opt into feedback requests.
Four sessions is enough to surface candidate themes, not enough to size
them. Theme 3 in particular rests on a single participant and should be
validated with a few more sessions or usage data (how many invoices go to
repeat versus new clients) before it is prioritized.
