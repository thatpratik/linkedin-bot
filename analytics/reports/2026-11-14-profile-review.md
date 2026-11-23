# LinkedIn profile review — big-tech (FAANG/MAANG) focus

- Reviewed: 2026-11-14
- Basis: the profile PDF export supplied on 2026-11-12 and the four post
  screenshots. The live profile was not opened (project rule: no automation
  on linkedin.com). The export does not show the banner, Featured section,
  recommendations, endorsements or the "Open to work" setting, so those are
  unscored.
- Rule kept: every rewrite uses only facts already on the profile or
  confirmed in chat. Missing numbers are `{{...}}` placeholders, not guesses.

## Score

Rubric: `.claude/skills/li-profile/rubric.json`, read for a recruiter or
hiring manager rather than a customer.

| Item | Score | Why |
|---|---|---|
| Headline | 7/12 | Describes the work and uses the space, but has no proof and no searchable stack terms. |
| About, first two lines | 3/10 | Opens with "I'm a Software Engineer who enjoys solving complex problems". Nothing a recruiter can use before "see more". |
| About, body | 4/10 | About 2,300 characters in one block; paragraph breaks are missing ("stack.Over", "important.I thrive"). Says "12+ years" (it is 14). One number in the whole text. |
| Photo | 5/6 | Professional headshot, face clear (from the post screenshots). |
| Current role | 5/10 | Good scope paragraph, then ten bullets, mostly duties. "50,000 users" appears three times; no other outcome number. Title reads "Software Engineer" while the headline says Senior. |
| Experience depth | 5/8 | Recent roles detailed and strong. The two oldest roles are long, dated and loosely written. |
| Skills | 2/6 | Top three are Azure Cosmos DB, Azure Functions and "Vector". None is what a big-tech recruiter searches for. |
| Activity | 8/10 | Posted today; before that, little technical activity. |
| Contact | 4/6 | Custom URL and email. GitHub handle differs from the other account in use; a personal Google Docs link is listed. |
| Featured | not visible | |
| Banner | not visible | |
| Recommendations | not visible | |
| **Visible total** | **43/78** | |

## What matters most for big tech

1. **Lead with the largest scale, not the most recent.** Big-tech screens
   read for scale and scope. 50,000 users is modest by that standard. The
   strongest scale signals are further down: a digital wallet used across
   180+ countries (Mastercard Masterpass), a drilling platform rendering
   millions of live data points, and a tech-lead role over 10+ engineers in a
   60+ engineer programme. The About section should surface these.
2. **Outcomes with numbers in the current role.** The Centrica entry does
   this well (about 90% less manual research, 8 hours a week per user). The
   FOSS entry, which recruiters read first, does not. "Optimize application
   performance" needs a before and after.
3. **Fix the title mismatch.** Headline says Senior Software Engineer, the
   FOSS entry says Software Engineer. Automated filters and recruiters read
   the entry.
4. **Make the level legible.** For senior/staff levels, reviewers look for
   ownership of ambiguous problems, cross-team influence and technical
   direction. You have evidence (designing a frontend from the ground up,
   leading architecture, mentoring 10+). It is spread across bullets rather
   than stated.
5. **Searchable terms.** Recruiters search by skill. TypeScript, Angular,
   React, Python, system design and distributed systems should be in the
   headline, About and top skills.
6. **Trim the old roles.** 2012–2016 should be two lines each.
7. **Polish is the smaller half.** A sharper profile raises the odds of a
   recruiter message. The offer still depends on coding and system-design
   interviews, which no profile change affects.

## Rewrites

### Title (current role)
Change the FOSS entry to "Senior Software Engineer" (confirmed by the user
on 2026-11-12 as the correct title).

### Headline (220 characters max) — three options

1. Senior Software Engineer | Frontend architecture for data-intensive platforms | Built RAG and LLM products end to end | TypeScript, Angular, React, Python, Azure
   (160 characters)
2. Senior Software Engineer, Frontend and AI | Led 10+ engineers on a carbon intelligence platform | Real-time UIs for millions of data points | TypeScript, Angular, Azure
   (166 characters)
3. Senior Software Engineer | 14 years building large-scale web platforms: payments, energy, industrial analytics | Frontend architecture, distributed systems, applied AI
   (165 characters)

Recommended: 1 for a frontend/full-stack target, 2 if aiming at lead or
staff-level roles.

### About (about 1,350 characters)

```text
I build the frontends of large, data-heavy platforms, and more recently the AI features inside them. 14 years across payments, energy, industrial analytics and insurance.

Some of the work:

Scale. Frontend features for Mastercard's Masterpass digital wallet, used in 180+ countries. Today I lead frontend engineering for a SaaS platform with 50,000+ users worldwide.

Real time. Introduced WebSocket streaming and canvas-based rendering on a drilling operations platform, so engineers could work with millions of live data points in the browser.

Applied AI. Designed and built a RAG-based lead discovery platform in a two-engineer team (Next.js, FastAPI, Azure OpenAI, Azure AI Search). It cut manual research by about 90%.

Leadership. Technical lead for 10+ frontend engineers on a carbon emissions platform, inside a 60+ engineer global programme. Designed that frontend from the ground up.

How I work: the problem comes before the stack. I've moved from ASP.NET to Angular to Python and LLM systems because the work called for it. I like design reviews, architecture discussions and getting other engineers unblocked.

Technologies: TypeScript, Angular, React, Next.js, Nx, Python, FastAPI, C#, Azure (Functions, Cosmos DB, AI Search), RAG, WebSockets.
```

Optional last line, only if you want it public (your employer can read it):
"Open to senior and staff-level roles in frontend, full-stack and applied AI."

### Current role (FOSS) — scope line plus four bullets

```text
Lead frontend engineering for a cloud-native SaaS platform that food manufacturers use to manage analytical instruments and monitor production with near real-time measurement data. 50,000+ users worldwide.

- Own the frontend architecture of an Angular application with 100+ reusable components, shared as libraries across {{number}} applications.
- Cut {{metric, e.g. load time or render time}} from {{before}} to {{after}} for data-intensive views by {{what you did}}.
- Shipped AI-powered features with backend and data teams: predictive analytics, anomaly detection and automated report generation.
- Set frontend standards and mentor {{number}} engineers through design and code reviews; part of architecture decisions across the Azure microservices platform.
```

The placeholders need your real figures, and anything about the current
employer should stay within what you are allowed to say publicly.

### Older roles
Compress Silicus and Atos Syntel to one or two lines each, for example:

```text
Silicus: Built a sales and marketing portal for the real-estate sector with AngularJS, C# and ASP.NET Web API.
Atos Syntel: Built online insurance quote portals for Allstate (auto, home, renters, motorcycle) with ASP.NET, C# and AngularJS.
```

### Top three skills
Replace Azure Cosmos DB / Azure Functions / Vector with the three you want
to be found for. Suggested for a frontend-leaning target: TypeScript,
Angular (or React, if that is the target), System Design. For an applied-AI
target: Python, Retrieval-Augmented Generation, System Design.

### Smaller fixes
- "12+ years" → 14 years, everywhere.
- Contact section: check that the personal Google Docs link is meant to be
  public, and that the listed GitHub account is the one with your best work.
- Not visible in the export, worth checking yourself: a banner that is not
  the default, a Featured section (today's post is a candidate), and two or
  three recent recommendations from leads or peers at SLB or Centrica that
  name a specific outcome.

## Applied AI version (target chosen by the user, 2026-11-14)

These replace the headline, About, FOSS bullets and top skills above. The
title fix, older-role compression and smaller fixes still apply.

### How this target changes the profile
- The lead-discovery platform becomes the centrepiece. It is your only
  end-to-end LLM system on record, and it has real numbers.
- Your 14 years of product engineering become the differentiator, not the
  headline: applied-AI teams need people who can ship a model inside a
  reliable product.
- Frontend detail (component counts, Nx, canvas rendering) moves down. It
  stays as proof of engineering depth.

### Headline — three options

1. Senior Software Engineer, Applied AI | Built a RAG lead-discovery platform end to end (about 90% less manual research) | LLM features in production SaaS | Python, TypeScript, Azure OpenAI
   (187 characters)
2. Senior Software Engineer | Applied AI and product engineering | RAG, semantic search, long-running LLM workflows | 14 years shipping large-scale platforms | Python, TypeScript, Azure
   (182 characters)
3. Applied AI Engineer | RAG pipelines, retrieval quality, async LLM workflows | Full stack from Next.js to FastAPI and Azure AI Search | 14 years in product engineering
   (166 characters)

Recommended: 1. It keeps your real title, names the target, and carries a
number. Option 3 uses "Applied AI Engineer" as a self-description, which is
not a title you have held.

### About (about 1,450 characters)

```text
I build AI features that people rely on at work, and the product around them. 14 years in software, most recently on LLM systems.

The project I'd point to first: a lead discovery platform I designed and built in a two-engineer team. It crawls company websites, embeds and indexes them in Azure AI Search, and answers questions over them with Azure OpenAI. A search runs from 10 minutes to an hour, so everything is asynchronous: queued, up to 10 at a time, with a notification at the end. It cut manual prospect research by about 90% and saved around 8 hours per user per week.

Inside it I worked on chunking strategy, retrieval quality, prompts and cloud cost.

Today I lead frontend engineering for a SaaS platform with 50,000+ users, where I integrate predictive analytics, anomaly detection and automated report generation into the product.

What I add to an AI team is the product side. Real-time interfaces over millions of data points. Frontend work on Mastercard's Masterpass wallet, used in 180+ countries. Technical lead for 10+ engineers. A model only matters once it sits inside something people can depend on.

Python, FastAPI, TypeScript, Next.js, Angular, Azure OpenAI, Azure AI Search, Cosmos DB, Azure Functions, RAG, embeddings, semantic search.
```

Optional additions, each needing your OK:
- "Day to day I work in Claude Code and build my own agent skills." (touches
  how you work at your current employer)
- "Open to applied AI roles." (your employer can read it)

### Current role (FOSS) — AI first

```text
Lead frontend engineering for a cloud-native SaaS platform that food manufacturers use to manage analytical instruments and monitor production with near real-time measurement data. 50,000+ users worldwide.

- Integrated AI-powered capabilities into the product: predictive analytics, anomaly detection and automated report generation. {{your part: what you designed or built, and one outcome}}
- Own the frontend architecture of an Angular application with 100+ reusable components.
- Cut {{metric}} from {{before}} to {{after}} for data-intensive views by {{what you did}}.
- Mentor {{number}} engineers and take part in architecture decisions across the Azure microservices platform.
```

### Centrica entry
Already your strongest. Two changes: open with the outcome ("Cut manual
prospect research by about 90% for enterprise marketing teams by building
..."), and add, if true, how retrieval quality was measured:
`{{how you evaluated retrieval or answer quality, and what improved}}`.

### Top three skills
Retrieval-Augmented Generation (RAG), Python, Large Language Models (LLM).
Keep System Design and TypeScript in the next five.

### Gaps an applied-AI screen will probe
Your profile currently says nothing about these. Add them only where you
have real experience:

- **Evaluation.** How you knew retrieval or answers were good: test sets,
  metrics, human review. This is the most common applied-AI interview topic
  and the profile's biggest silence.
- **Scale of the AI system.** Documents indexed, searches per week, users,
  cost per search.
- **Operating it.** Monitoring, failure handling, cost control, model or
  prompt changes after launch.
- **Agents.** Your crewAI certificates and your own skills are the only
  agent evidence; a small public project would carry more weight.
- **Public proof.** A Featured item: a write-up or repository of something
  you built with RAG or agents. Today's post is a start.

### Effect on the content plan
For this target, the Agentic AI pillar should carry more of your posts, and
the strongest future post is the one already in the backlog: "What tuning
chunking actually changed in a RAG pipeline".

## Open questions
- Level: senior or staff?
- Real numbers for the FOSS bullets.
- Whether to state openness to new roles publicly.
