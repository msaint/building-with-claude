# Curriculum: 12 weeks building with Claude

This file is the working copy the tutor commands read. The Claude doc "Path to Anthropic: 12-Week Curriculum" predates the 10 Nov 2026 retarget and is out of date; where the two disagree, this file wins.

**Target:** Research Product Manager, Labs at Anthropic. The posting asks for someone who works with researchers to see what is emerging, builds prototypes themselves, validates product-market fit at the lowest cost, and leads 0-to-1 work from research to shipped product. Every week below produces evidence for one of those.

**What changed on 10 Nov 2026 (retarget, week 4):**
- Weeks 1 to 3 were aimed at Product Manager, Safeguards and built around a claims safeguard. Nothing shipped in those weeks. They stay in the record as they happened.
- In the same period Marc built Ada, an adaptive learning platform, in its own repo. The plan now follows the work he is actually doing: **Ada is the spine.**
- Hours drop from about 20 a week to **about 12**, sized to be finished.
- **The application goes out by Fri 20 Nov (week 5), on a date, not a gate.** The posting has closed and reopened before. The weeks after that deepen the evidence for interviews.
- The calendar is unchanged: 12 weeks, 19 Oct 2026 to 10 Jan 2027. The Labs plan runs weeks 4 to 12.

**Edge:** Marc has taken products from zero to commercial success with tiny teams (Jade Leaf: the #1 US matcha brand, built by five people), built developer platforms (Tilt Open, Tilt's API), and incubates ventures against pre-set scale-or-stop milestones (3 scaling, 2 wound down). Writing kill criteria before building is work he has done. The plan makes it visible on AI products.

**Done means public and used.** A task counts only when it is public and at least one real person outside Marc has used or reviewed it.

**The Labs loop** (used every week from week 6, and the habit the whole plan trains):
1. **Capability:** name the model or platform capability that is new, and the source (paper, release note, system card).
2. **Bet:** one page, written before building: who it is for, what they do today, why this is possible now, the cheapest test, and the result that would make you stop.
3. **Prototype:** built by Marc with coding agents, capped at 8 hours.
4. **Users:** five people outside his companies, watched, not helped.
5. **Decision:** kill, keep or change, against the criteria written in step 2. Published.

---

## Weeks 1–3: history (Safeguards target)

Retool, then a claims safeguard for supplement brands. Gates missed in weeks 1 and 2; no review was written for week 3. See `reviews/` and the score history in `RUBRIC.md`. Nothing from these weeks carries forward as a deliverable.

---

## Weeks 4–5: Ship what exists, then apply

**Goal:** turn Ada from a private build into public evidence, and get the application in.

Ada already has a working learning loop, a mastery model, spaced reviews, guest mode and a real-model eval (50 hand-labelled grading cases, 20 generation topics, OpenAI baseline). What it lacks is outside users, a Claude baseline, and a write-up a reviewer can read in two minutes.

- **Week 4, evidence:** run the model eval on Claude and commit the baseline beside the OpenAI one; get three people outside Marc's companies through a first lesson on the live site and log what happened; write `builds/ada/README.md` here as a case study (the bet, the numbers, what failed, what is next, and what running OpenAI, Anthropic and Google models side by side on one product taught him, as builders and at runtime) linking to the Ada repo; start `essays/friction-log.md`, a running list of every place learning breaks, in Ada and in the Claude app's own learning mode
- **Week 5, apply:** publish essay 1 from the friction log; bring the resume and site in line with what Ada actually is; submit the application by Fri 20 Nov; fix the top two problems the week 4 sessions exposed

**Gate (week 4):** a stranger finishes lesson one on the live site with no account and no help; the OpenAI and Claude eval baselines are both public; three outside sessions are logged in `evals/signals.md`.

**Milestone (week 5):** application submitted by Fri 20 Nov, whatever the week 4 gate result. A missed gate is reported in the review; it does not hold the application.

**Tutor checks**
- In Ada's eval report, which single number matters most for a learning product, and why? What does its confidence interval tell a reader with this many cases?
- The judge model also writes Ada's course plans by default. What does that do to trust in the plan scores, and what is the cheapest fix?
- Before the user sessions: write the three places you expect people to stumble and the one observation that would make you change the product. Afterwards: did it?
- Predict which provider does better on recognising partial answers. Then run it and explain the gap.
- Who is Ada not for? One sentence, and what you would tell that person to use instead.

---

## Weeks 6–8: Three capability bets

**Goal:** show the Labs loop three times in three weeks: capability, bet, prototype, users, decision.

One bet a week. Each ends Friday with a public kill-or-keep memo of one page. At least one bet must be outside learning, to show range. Bets can come from Marc's own backlog.

- **Week 6, Ada where the learner already is:** does a course need its own app, or can it live inside Claude as a skill plus an MCP server? Build the smallest version, give five people both, and compare day-2 return. Readings: MCP introduction, "Writing effective tools for agents". (US Thanksgiving week: plan for 8 hours.)
- **Week 7, an agent that runs part of a real business:** a bet from Marc's operator stack. Anthropic's Project Vend put Claude in charge of a small shop; Marc has run one. Pick one job an agent does badly today, write the bet, prototype it against his own data with human approval on anything that writes.
- **Week 8, the newest capability:** pick the most recent model or platform capability released (the Monday coach names three candidates from the last 60 days of Anthropic releases and research). Write the bet in a day, prototype in two.

**Gate (week 8):** three kill-or-keep memos public, each with criteria written before the build and five outside users; at least one decision went against what Marc expected on Monday; agent hours and his hours logged for all three weeks.

**Tutor checks**
- Read back your kill criteria before you open the editor. Is each one a number or an observable behaviour? Rewrite any that is a feeling.
- For this week's capability: what could it not do six months ago, and how do you know?
- Workflow or agent? Argue it for this bet, with the cost of being wrong.
- Rewrite one bad MCP tool description; measure tool-selection accuracy before and after.
- Which agent stalled waiting on you most this week, and what standing instruction or skill would have prevented it?
- What is the worst thing this prototype could do to a user who trusts it, and what did you do about it?

---

## Weeks 9–11: Flagship

**Goal:** take the bet that survived (Ada, unless weeks 6 to 8 say otherwise) from prototype to something people return to, with outcome evidence.

- **Week 9, does it work:** an outcome eval, not only an output eval. Do learners retain what Ada says they mastered? Measure review success at day 7 against a static-lesson baseline; get a second person to label a sample of the grading cases and report agreement; publish the write-up
- **Week 10, do people come back:** 25 people outside his companies; report the funnel from first visit to second session using the queries in Ada's `docs/METRICS.md`; one change shipped from the data. (Holiday week: plan for 8 hours.)
- **Week 11, tell it to researchers:** a 20-minute readout to two people who work in AI research or AI product, recorded in `evals/signals.md`; essay 4; mock interviews

**Gate (week 11):** 25 outside users, day-7 return rate and review success reported with counts, eval suite public with second-labeller agreement, readout done.

**Tutor checks**
- Ada says a learner has "mastered" a concept. What evidence would convince a sceptical researcher, and do you have it?
- Your day-7 number is from 25 people. What can you claim, and what can you not?
- At step 20 of a long tutoring session, what stays in context and what gets summarised or dropped?
- A change raises completion but lowers review success. Ship it? Defend the numbers.
- Measure a model grader's agreement with your own labels on 20 cases, then with a second person's.

---

## Week 12: Capstone

**Goal:** do a small, real version of the Research PM, Labs job in public.

**A Labs product memo, 4 to 6 pages:** pick one capability from recent Anthropic research that is not yet a product. Problem and user, why now, what the weeks 6 to 11 evidence says, the cheapest test, MVP to ideal state, risks and benefits (who could be hurt, how you would know), and what you would cut to ship in six weeks. Plus a one-page retrospective on the 12 weeks.

**Tutor checks**
- Product review: Claude plays a Labs lead and asks what to cut to ship in six weeks.
- Research review: Claude plays a researcher and challenges every claim about what the capability can do.
- User review: Claude plays a sceptical user who has tried three AI products this year and kept none.
- Risk review: how would you know the product is hurting the people it is for?

---

## Parallel track: research and product literacy (about 2 hours a week)

Each week: read, run `/explain-back` on the core claim. Essays are every second week, 500 to 800 words, and must survive a sceptical-researcher review.

| Week | Reading | Writing |
| --- | --- | --- |
| 4 | The Research PM, Labs posting; "Building effective agents"; Ada's own eval report, read as a reviewer would | Friction log (start) |
| 5 | Anthropic Education Report on how students use Claude; the learning mode announcement | **Essay 1:** What learning inside a chat app is missing, from running a course both ways |
| 6 | Model Context Protocol introduction; "Writing effective tools for agents" | Bet memo 1 |
| 7 | Project Vend, both phases | **Essay 2:** What an agent running a shop gets wrong, from someone who ran one. Bet memo 2 |
| 8 | "Effective context engineering for AI agents"; How employment is changing at Anthropic | Bet memo 3 |
| 9 | "Tracing the thoughts of a large language model" | **Essay 3:** One research result I would turn into a product, and the cheapest test |
| 10 | Claude's constitution; Responsible Scaling Policy | Outcome-eval write-up |
| 11 | Anthropic Economic Index, latest report | **Essay 4:** Where usage is growing and which product is missing |
| 12 | Current frontier model system card; how Claude Code and MCP started | Labs product memo; retrospective |

---

## Milestone posts

| Week | Post |
| --- | --- |
| 4 | Ada case study: the bet, both model baselines, what three first-time users did |
| 5 | Essay 1, and the application |
| 8 | Three bets in three weeks: what I killed and why |
| 9 | Does adaptive beat static? An outcome eval for an AI tutor |
| 11 | What 25 learners did in their first week |
| 12 | The Labs product memo, plus a retrospective |
