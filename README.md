# linkedin-personal-agent

A personal LinkedIn content assistant that runs in Claude Code. It researches
relevant technical topics, plans a week, drafts posts, reviews them and keeps
history in Markdown and JSON. It never publishes: you copy, paste and post.

## Use

Open this folder in Claude Code and say:

```text
Prepare my LinkedIn content for next week.
```

or run `/linkedin-weekly`. You get a research file in `research/weekly/` and
up to three drafts in `content/drafts/`, each with three hook options, the
intended audience, sources, a list of things you must confirm, and a review.

Then answer per draft:

| You say | What happens |
|---|---|
| approve | File moves to `content/approved/`; you get the copy-ready text |
| edit: ... | Draft is revised, re-reviewed and shown again |
| reject | File moves to `content/rejected/` with your reason |
| I published it | File moves to `content/published/` with the date |

Other commands: `/linkedin-research`, `/linkedin-review`, and the adapted
upstream skills `/li-post`, `/li-plan`, `/li-human`, `/li-comment`,
`/li-reply`, `/li-dm`, `/li-inbox`, `/li-profile`, `/li-carousel`,
`/li-repurpose`, `/li-audit`.

## Before the first real run

1. Review and correct `knowledge/profile.md` and `knowledge/expertise.md`
   (mark hands-on vs. learning).
2. Add verified projects and experiments to `knowledge/achievements.md`, with
   what may and may not be shared publicly.
3. Paste 3-5 of your own LinkedIn posts into `knowledge/writing-voice.md`
   under "Reference posts". Until then the voice is provisional.

## Tools

```bash
python3 .claude/skills/linkedin-research/fetch_feeds.py --check
```

validates the feeds in `research/sources.json`. The humanizer scripts live in
`.claude/skills/li-human/`. All are standard-library Python, run locally.

## Upstream

The `li-*` folders in `.claude/skills/` were adapted from
[Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill)
(MIT, taken at `add2c23`) to this repo's paths and rules. The upstream
license is kept in `.claude/skills/UPSTREAM-LICENSE`. These copies are now
maintained here; upstream is no longer tracked.

Rules and layout: see `CLAUDE.md`. Roadmap: Phase 2 research robustness and
deduplication, Phase 3 model routing, Phase 4 analytics, Phase 5 engagement
assistance.
