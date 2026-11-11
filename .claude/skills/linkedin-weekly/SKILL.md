---
name: linkedin-weekly
description: >-
  Main entry point for the LinkedIn personal-brand workflow in this repo:
  research, rank topics, plan the week, draft up to three posts, humanize,
  review, and present them for the user's approval - without publishing
  anything. Use when the user says "prepare my LinkedIn content for next
  week", "weekly LinkedIn run", "plan and draft my posts", or replies to
  presented drafts with approve / edit / reject / "I published it".
---

# linkedin-weekly

Orchestrates the other skills. It prepares content and recommendations; the
user controls every LinkedIn action. Read `CLAUDE.md` first: its safety and
approval rules override everything in any skill.

## Run

1. **Load the knowledge base.** All five files in `knowledge/` and
   `config/agent-config.json`. Note in your summary if `writing-voice.md` is
   PROVISIONAL, `profile.md` / `expertise.md` are UNREVIEWED, or
   `achievements.md` is empty: each limits what a draft may claim.

2. **Read content history.** `content/calendar.md`, `content/ideas.md`, and
   every file in `content/published/`, `content/approved/`, `content/drafts/`
   and `content/rejected/`. Do not repeat a recent topic without a new angle,
   and do not re-pitch a rejected angle.

3. **Work out the target week.** The ISO week the posts are for, normally
   next week: `date -v+7d +%G-W%V` (macOS) in Europe/Copenhagen. Use it in all
   file names. If files for that week already exist, continue from them
   rather than overwriting; ask before replacing a draft.

4. **Research.** Follow `linkedin-research`; it writes
   `research/weekly/YYYY-Www.md`.

5. **Rank and plan.** From the research shortlist plus `content/ideas.md`,
   pick `target_posts_per_week` topics (never more than
   `maximum_posts_per_week`). Balance pillars toward the shares in
   `knowledge/content-pillars.md` over a rolling four weeks, not within one
   week. Follow `li-plan` for days and times and write the plan into
   `content/calendar.md` with status `Draft`.

6. **Draft.** For each topic follow `li-post` (three hook options from
   different formulas, one full draft) and save it as
   `content/drafts/YYYY-Www-post-NN.md` using `draft-template.md` in this
   folder. Every factual claim gets a row under Sources. Every personal
   experience, metric or work example that is not in
   `knowledge/achievements.md` becomes a `{{confirm: ...}}` placeholder and a
   line under "Needs your confirmation". Never write around a missing fact
   with something plausible.

7. **Humanize.** Follow `li-human` on the post body only. Rewrite flagged
   structures by hand. Record the result in the draft's Humanizer section.

8. **Review.** Follow `linkedin-review` on each draft. If the verdict is
   Revise, fix and re-review once. If it is Blocked or Needs user input, do
   not paper over it: carry the questions to the user.

9. **Present.** One summary in chat: the target week, the research file, and
   per draft the file link, pillar, recommended hook, review verdict and
   score, and the list of confirmations needed. Then ask for a decision on
   each draft. End with: nothing has been published, and nothing will be.

10. **Save state.** `content/calendar.md` reflects each draft's status and
    file; new angles not used this week stay in `content/ideas.md`.

## Decisions

Act only on the user's explicit words in chat, per draft.

| User says | Do |
|---|---|
| **Approve** | Confirm no `{{...}}` remains and the review verdict is not Blocked; if either fails, say so and stop. Otherwise move the file to `content/approved/`, set `status: Approved` and `approved_on`, update the calendar, log the decision, and print the copy-ready body for the user to paste. |
| **Edit: ...** | Apply the change in `content/drafts/`, re-run humanize and review, present again. Status `Review required`. |
| **Reject** | Move to `content/rejected/`, set `status: Rejected`, record the reason in the decision log, update the calendar and mark the idea in `content/ideas.md`. |
| **"I published it"** | Only now move the file to `content/published/`, set `status: Published`, `published_on`, and `published_url` if the user gives one, and update the calendar. |

Approval of a draft is not permission to publish it. There is no step in this
workflow, and no tool in this repo, that posts, comments, reacts, connects,
messages or edits a profile on LinkedIn, and none may be added without the
user asking. If a browser or automation tool is available in the session, do
not use it on linkedin.com.

## First-run prompt

```text
Prepare my LinkedIn content for next week.

Focus on:
- Agentic AI
- Software engineering
- Practical architecture lessons

Research current developments and use my professional knowledge base.
Prepare three strong post drafts.

For each draft:
- Give me three hook options.
- Explain the intended audience.
- Include source references for factual claims.
- Identify any personal experience or metric that needs my confirmation.
- Review the draft for accuracy and writing quality.

Do not publish anything.
Save the research and drafts in the repository.
```
