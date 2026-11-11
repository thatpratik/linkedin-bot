---
name: linkedin-review
description: >-
  Review a LinkedIn draft in this repo for technical accuracy, source quality,
  authenticity, audience fit, voice, repetition, unsupported claims and
  confidentiality risk, and write the result into the draft file. Use when the
  user says "review this draft", "is this ready", "check my post", or when
  linkedin-weekly reaches its review step.
---

# linkedin-review

Reviews one draft file in `content/drafts/` (or text the user pastes) and
writes the verdict into the draft's `## Review` section. The reviewer is a
critic, not a co-author: do not quietly rewrite the post to make it pass.

## Read first

The draft, `knowledge/` (all five files), the research file the draft cites,
the titles and first lines of everything in `content/published/` and the
other current drafts, and `config/agent-config.json` (`quality`).

## Hard gates

Any one of these makes the verdict **Blocked**, whatever the score:

1. **Fabrication.** A personal experience, project, client, metric or
   achievement that is not in `knowledge/achievements.md` and is not marked
   with a `{{confirm: ...}}` placeholder.
2. **Confidentiality.** Anything about the user's employer that could be
   internal: architecture, customers, unreleased products, proprietary
   numbers, security details, workplace conversations. When unsure, block
   and ask.
3. **Unsourced factual claim.** A checkable claim about a product, release,
   benchmark, date or third party with no entry under `## Sources`
   (when `require_sources_for_factual_claims` is true).
4. **Misattributed opinion.** A strong position presented as the user's that
   the user has not expressed.
5. **Unresolved placeholders.** Any `{{...}}` left in the body means the
   draft can be at most **Needs user input**, never Approved-ready.

## Scored checks (100 points)

| Check | Points | Full marks looks like |
|---|---|---|
| Technical accuracy | 20 | Every technical statement is correct and precise; re-checked against the cited source, not from memory |
| Source quality | 15 | Primary, dated, reachable sources; each factual claim maps to one |
| Personal authenticity | 15 | Reads as this engineer's experience; nothing generic that any account could post |
| Audience relevance | 10 | A senior engineer or engineering lead learns or reconsiders something |
| Writing voice | 15 | Matches `knowledge/writing-voice.md`; no influencer hooks, bait or motivational close |
| Specificity and trade-offs | 10 | Names the trade-off and when the advice does not hold |
| Repetition | 5 | New angle versus published posts and the other drafts this week |
| Clarity and format | 10 | One idea, mobile-readable paragraphs, hook survives truncation, sensible length |

Give each check a score and one line of evidence quoting the draft. Deduct
for what is on the page, not for what you would have written. Re-open the
cited sources to check accuracy when web access is available; if it is not,
say the accuracy check was done from the research file only.

While `knowledge/writing-voice.md` is PROVISIONAL, cap "Writing voice" at
10/15 and say why: the voice cannot be verified without the user's own posts.

## Verdict

- **Blocked** — a hard gate failed. List each one with the offending line.
- **Needs user input** — placeholders or questions remain.
- **Revise** — no gate failed, score below `quality.minimum_score`.
- **Ready for approval** — no gate failed, no placeholders, score at or above
  the minimum.

"Ready for approval" means ready for the *user* to decide. The score is a
review aid. It is not proof of quality or authenticity, and it is never
permission to publish.

## Write the result

Replace the draft's `## Review` section with:

```markdown
## Review
- Reviewed: YYYY-MM-DD
- Verdict: <verdict>
- Score: NN/100 (minimum 80) — review aid only
- Hard gates: passed | failed: <which>

| Check | Score | Evidence |
|---|---|---|

### Must fix
- <line> — <problem> — <suggested direction>

### Questions for the user
- <question>
```

Then set the draft's front-matter `status` to `Review required` and the same
status in `content/calendar.md`. Do not move the file: only the user's
explicit decision moves a draft out of `content/drafts/`.
