# Week 1 review: Retool

**Reviewed:** Fri 23 Oct 2026, by the scheduled Friday reviewer, as a Safeguards PM hiring manager would read the public repo.

## Verdict: gate missed

Work that isn't pushed doesn't count, and almost nothing was pushed this week.

**Evidence (`git log --since="7 days ago"`):**

- The only commit dated inside week 1 (Mon 19 Oct onward) is `d45aaeb Week 1 plan` (PLAN.md and 3 quiz questions).
- The other commits in the window (16 to 18 Oct) are week 0 setup: curriculum retarget, eval key handling, progress data.
- `builds/` is empty. There is no `builds/listing-audit/`, no CLI, no `--model` flag, no 20-listing benchmark, no README.
- `essays/` is empty. No essay ("How a policy becomes detection") and no milestone post.
- `LEARNING_LOG.md` has no week 1 entries; the last entry is week 0 (15 Oct). No hours, agent hours or tutor ratings were logged.
- `evals/signals.md` has no rows. The Monday task to book an Amazon seller for Thursday left no trace.
- `evals/results/` holds only `.gitkeep`: no quiz, no tutor eval report.

The gate asks Marc to explain cost, latency and quality tradeoffs between model tiers **with measured numbers**. There are no measured numbers anywhere in the repo, so the gate can't be passed, whatever was learned offline. The missing quiz counts against it as well.

If work exists locally, this verdict stands until it is pushed. A reviewer at Anthropic sees only the public repo.

## Rubric scores (public work only)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Technical currency | 1 | No code, benchmark or token/cost/latency number was published this week. |
| Judgment | 1 | The plan's tutor check ("one feature you decided not to build" and the cost of a wrong finding) has no public answer, and the Wednesday scope cut wasn't taken or recorded. |
| Founder empathy | 1 | No seller session and no rows in `evals/signals.md`. |
| Communication | 1 | No README, essay or milestone post shipped. |
| Mission literacy | 1 | None of the three readings has an `/explain-back` record or written output. |

These scores describe what is public. They are not a judgment of Marc's ability, and one shipped week will move every one of them.

## Safeguards dimension

Week 1 deliberately keeps claims compliance out of scope, so a written policy, threat model and precision/recall by category are **not yet due** (weeks 2 to 4). What week 1 did call for was a baseline: a written 10-rule spec, hand labels for agreement with each tier, and a dollar or hours cost for a wrong audit finding. None of these exist. That missing baseline matters most going into week 2. The claims safeguard needs labeled data and an explicit cost per error type, and week 1 was the low-stakes place to practise both.

- Written policy / rule spec: **missing** (was due: the 10-rule spec)
- Threat model: not due
- Precision and recall by category: not due; tier agreement with labels was due and is **missing**
- Explicit cost per error type: **missing** (was a tutor check)
- Blind-spot measure: not due

## Evals

- **Learner quiz:** no quiz was taken this week (`evals/results/learner.csv` does not exist). This counts against the gate.
- **Tutor evals:** not run this week. There was no `EVALS_ANTHROPIC_API_KEY` in the review environment and no tutor eval report in `evals/results/`. There are 22 cases in `evals/tutor/cases.jsonl` across 12 categories; pass rate unknown.
- **Tutor rating:** no ratings logged this week; the average is not available.
- **Tutor misses:** none reported in the log.
- **Outside signals:** no new rows in `evals/signals.md`.

## Top three fixes for next week

1. **Ship a cut-down `listing-audit` by Monday night, before starting week 2.** Use 10 listings, not 20; all three tiers; one table with tokens, cost, p50 latency and agreement with your hand labels; and a README with problem, design, numbers and what failed. Push it even if it's rough. Week 2's claims safeguard is built on exactly this harness, so skipping it costs you more later.
2. **Push and log every working session.** Commit at the end of each session and run `/log` with hours, agent hours and a tutor rating, even when the day was mostly reading. A week with zero commits after Monday can't be told apart from a week with zero work. Hiring managers will read commit history as evidence of how you work with agents.
3. **Book the seller session today, for week 2.** Send one message to a Jade Leaf alum or portfolio founder now, with a date. Outside signals carry the most weight in this rubric, and week 2's gate needs operators outside your companies. Also take the closed-book quiz over the weekend and run `/eval` on your Mac, then push `evals/results/`.

## One thing that is strong

The evaluation setup from week 0 is unusual and directly relevant to Safeguards. The repo has 22 tutor eval cases in 12 categories, including three `no_answer_leak` cases that test whether the tutor hands over answers, plus a separate closed-book learner quiz. Evaluating the AI system that evaluates you is the habit a Safeguards PM needs: measure the tool, not just its outputs. Note that this predates week 1 and is not scored here.

## Proposed tutor fixes

None. No tutor eval cases were run and no tutor misses were reported. One observation for Marc to consider, not a CLAUDE.md change: the scope-check rule ("say so by Wednesday and propose a cut") only fires when a session happens. If no session happened mid-week, nothing prompted the cut. A short scheduled Wednesday check-in would cover that gap.
