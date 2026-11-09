# Week 4: Build a safeguard (rigor and metrics, phase gate)

**Dates:** Mon 9 Nov to Fri 13 Nov 2026 · about 20 hours

**Deliverable (ships Friday):** `claims-guard` in `builds/claims-guard/`, public: your `POLICY.md` (3 categories), `claims.csv` with 30 hand-labeled real claims (10 per category, 2 borderline in each), a CLI that returns one validated allow/warn/block finding per claim, and a README case study with precision and recall by category (counts shown), the threshold you chose and why, cost per 1,000 reviews, and at least one outside operator's run.

**Gate (phase gate, from the curriculum, then apply):** repo public, two or more operators outside his companies have run it, README reports precision and recall by category and explains the threshold chosen. **Apply only on a passed gate.** If Friday's check is "partly", the application moves to a week 5 re-check; it does not go out on a missed gate.

**Carry-over (third week running):** no week 3 review was committed, and `git log` shows no commits in week 3 after Monday's plan: `builds/`, `essays/`, `evals/results/`, `evals/signals.md` and `LEARNING_LOG.md` are unchanged since week 0. The week 2 review's fixes all still stand:
1. **Ship `claims-guard` v0 by Tuesday night.** `POLICY.md` first, written by you, committed Monday. Push rough.
2. **Commit every working day** and `/log` with hours, agent hours and a tutor rating. A fourth silent week is the single worst signal the repo can send.
3. **Operator messages are Monday's first task**, two this time (the gate needs two), each logged in `evals/signals.md` as "asked".
4. Take the first closed-book quiz Friday and push `evals/results/`.

**Cut because you're behind (no extra hours):** 30 labels, not 50+. Prompt caching layouts, batch, and retrieval versus long context are dropped from this phase (cost per 1,000 reviews stays: one number from the usage fields). Retries shrink to one test: a claim that errors is reported as `error`, never `allow`. Held-out claim type, the tutor-system write-up and the grader audit move to week 5. No essay; the README is this week's writing, and the launch post is the README link plus three lines.

## Daily plan

| Day | Hours | Work |
| --- | --- | --- |
| Mon | 4 | **First 30 min:** message two supplement or food operators outside your companies; book Thursday; log both as "asked". Write `POLICY.md` yourself (definition, why it's risky, 2 examples each side, severity, intervention per category). **Commit tonight.** `/log`. Set up the Wednesday `/checkin` two reviews have suggested. |
| Tue | 4 | Label 30 real claims. v0 CLI end to end: Pydantic-validated findings, failure counts, the error-is-never-allow test. **Push tonight.** Two agents in parallel: one gathers candidate claims while you label, one scaffolds models and tests. |
| Wed | 4 | Run all 30. Precision and recall per category with the confusion counts. Sort every miss into a failure type *before* changing the prompt; one prompt revision, re-run, report both. **Scope check by noon:** if v0 isn't pushed, cut to 15 claims and say so in the log. |
| Thu | 4 | Operator session(s); log what they did and said. Cost per 1,000 reviews from measured tokens. Dollar cost of a false positive and a miss for one real brand, then the threshold. README case study. |
| Fri | 4 | Closed-book quiz, `/eval`, push `evals/results/`. Final README pass. `/log` agent hours vs your hours. Self-check the gate in one line. |

## Tutor checks

- Sort 10 eval failures into categories before changing any prompt. Which category would a prompt change not fix?
- A false positive costs a brand legitimate sales; a miss risks an FTC warning letter. Put a dollar figure on each for one real brand (Jade Leaf is fine). Where does the threshold go? Explain it to a policy lead in two sentences. Carried from week 2.
- With 10 claims per category, what is one miss worth in recall? What would you say in the README so a reader doesn't over-trust the numbers?
- Write 5 adversarial claims a seller would use to slip past your policy. How many get through? Fix one, and note the rest as known gaps.
- **Communication (all five dimensions tied at 1; judgment and founder empathy had the last two checks):** give the README's first paragraph to someone outside. Ask them to say back what the tool does and how often it catches disease claims. If they can't, rewrite it before Friday.
- No quiz review question this week: `evals/results/learner.csv` doesn't exist yet.

## Reading

Optional, only after Thursday's README is pushed: the first two 3Blue1Brown neural network videos. The week 4 essay (explain a transformer to a CPG founder) is cut.

## Founder touchpoint

Nobody lined up for three weeks; `evals/signals.md` is still empty. Monday's first task: two operators outside your companies, asked by message, booked for Thursday. A Jade Leaf alum and one portfolio founder are the fastest yeses. If only one runs it, the gate is "partly" and the second becomes week 5's first task.
