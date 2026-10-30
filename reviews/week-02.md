# Week 2 review: Build a safeguard

**Reviewed:** Fri 30 Oct 2026, by the scheduled Friday reviewer, as a Safeguards PM hiring manager would read the public repo.

## Verdict: gate missed (second week in a row)

Work that isn't pushed doesn't count. The only commit this week is the plan.

**Evidence (`git log --since="7 days ago"`):**

- `0712e10 Week 2 plan` (Mon 26 Oct): `PLAN.md` and 3 questions added to the learner question bank. Nothing else after it.
- `376a42b Week 1 review` (Fri 23 Oct) is last week's scheduled review, not Marc's work.
- `builds/` holds only `.gitkeep`. There is no `builds/claims-guard/`, no `POLICY.md`, no CLI, no Pydantic models, no 15 labeled claims, no results table.
- The Monday carry-over, `builds/listing-audit/`, was not shipped either.
- `essays/` holds only `.gitkeep`. The essay carried from week 1 is still missing.
- `LEARNING_LOG.md` has no entries since week 0 (15 Oct). The plan's rule "commit and `/log` at the end of every session" left no trace: no hours, agent hours or tutor ratings.
- `evals/signals.md` has no rows. The Monday operator booking and the Thursday session left no record.
- `evals/results/` holds only `.gitkeep`: no quiz, no tutor eval report.

This week's bar was "v1 runs end to end on the 15 labeled claims, every output passes validation, and failures are counted and reported." None of it is public, and the missing quiz counts against it too.

**What this means for the week 4 phase gate.** The gate needs a public repo, two outside operators who have run the tool, and precision and recall by category with a chosen threshold. Two weeks in, there is no code, no labels and no operator booked. If week 3 also ships nothing, week 4 can't pass, and the "apply" milestone after it slips with it. You need to cut scope now, not add hours (see fix 1).

## Rubric scores (public work only)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Technical currency | 1 | No tool-use code, schema comparison, validation test or token/cost number was published. |
| Judgment | 1 | The plan made good cuts, but the Wednesday scope check ("if v1 isn't running, drop the rewrite suggestion") wasn't taken or recorded, and the week 1 carry-over stayed blocking. |
| Founder empathy | 1 | No operator session, no pre-written interview questions, and `evals/signals.md` is empty for the second week. |
| Communication | 1 | No README, policy or essay shipped. |
| Mission literacy | 1 | No `/explain-back` record or written output from the RSP skim or "Building safeguards for Claude". |

These scores describe the public repo, not Marc's ability. One shipped artifact would move three of them.

## Safeguards dimension

This is the first week where the safeguards work itself was due. Scored against what the week asked for:

- **Written policy (`POLICY.md`):** missing. Due this week: 3 harm categories (disease claims, unsubstantiated structure/function, misleading testimonials), allowed vs risky, 2 examples per side, severity, an intervention per category.
- **Threat model:** not due until week 5. This week did need a short note on who games a claims checker: sellers rewording claims to slip past it. That note is missing too.
- **Precision and recall by category:** formally due at week 4. This week needed the 15 hand-labeled claims and per-claim results to build on. Both are missing.
- **Explicit cost per error type:** missing. The tutor check asked for a rough dollar figure for a false positive (lost legitimate sales) and a miss (FTC warning letter risk) for one real brand, and which way that pushes the threshold. You have unusual standing to answer this from Jade Leaf. It's the single most interview-relevant paragraph in the plan.
- **Blind-spot measure:** not due (week 4: a held-out claim type).

A hiring manager would see two plans that are well shaped in safeguards terms (policy, then labels, then detection, then intervention) and no output yet. Right now the gap between plan quality and shipped work is the main signal the repo sends.

## Evals

- **Learner quiz:** no quiz taken this week (`evals/results/learner.csv` does not exist). This counts against the gate. It's the second week without a quiz.
- **Tutor evals:** not run this week. `EVALS_ANTHROPIC_API_KEY` is not set in the review environment and there is no tutor eval report in `evals/results/`. 22 cases across 12 categories; pass rate unknown.
- **Tutor rating:** no ratings logged; the week's average is not available.
- **Tutor misses:** none reported in the log.
- **Outside signals:** no new rows in `evals/signals.md`.

Minor housekeeping: `progress/shipped.json` describes the week 0 setup as "19 tutor eval cases, 20 quiz questions", but `cases.jsonl` now has 22 cases. Fix it when you next touch that file. It isn't public, so it's low priority.

## Top three fixes for next week

1. **Drop `listing-audit` for good and ship `claims-guard` v0 by Tuesday night.** The carry-over has blocked two weeks, so stop carrying it. Its model-tier comparison can come back later as one table inside `claims-guard` (run the 15 claims on two tiers). v0 means: `POLICY.md` written by you (one page, 3 categories), `claims.csv` with 15 hand-labeled real claims including 3 borderline ones, and a CLI that prints one validated finding per claim with failures counted. Push it rough. When `/plan-week` runs Monday, it should plan week 3 around finishing this, with caching and cost layered on only after v0 is pushed.
2. **Commit something every working day, even a single file.** Do `POLICY.md` first. It needs no code and is the highest-value artifact for a Safeguards PM reader. Then `/log` with hours, agent hours and a tutor rating. Two weeks of a silent repo now reads as a pattern, and commit history is how an Anthropic interviewer will judge how you work with agents.
3. **Send the operator message Monday morning, before anything else, and log it in `evals/signals.md` as "asked".** One Jade Leaf alum or portfolio founder, with a date in week 3. Week 4 needs two outside operators, so the first one needs to be booked this week. Also take the closed-book quiz this weekend and push `evals/results/`.

## One thing that is strong

The week 2 plan's tutor check on founder empathy is well designed: "write the three questions you'll ask the operator and the one answer that would make you change the design. Afterwards, record whether it changed." Writing down what would change your mind before the conversation is how you stop user research from becoming confirmation. It's the same pre-registration discipline a Safeguards team uses before launching a classifier. Keep it when the operator session finally happens. Note that this is still a plan, not shipped work, so it doesn't move any score.

## Proposed tutor fixes

None from evals: no tutor eval cases were run this week and no tutor misses were reported.

An observation for Marc, not a CLAUDE.md change: both missed weeks look the same. The plan is good, then the repo goes silent until Friday. CLAUDE.md's scope rule ("say so by Wednesday and propose a cut") only fires inside a tutor session. Last week's review suggested a scheduled Wednesday check-in to cover that gap, and nothing in the repo shows one was set up. If you want one, a short scheduled `/checkin` on Wednesday that reads `git log` and messages you when `builds/` hasn't changed would catch week 3 before Friday.
