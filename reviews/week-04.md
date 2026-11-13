# Week 4 review: Ship what exists (Ada evidence)

**Reviewed:** Fri 13 Nov 2026, by the scheduled Friday reviewer, reading the public repos as a hiring manager on Anthropic's Labs team would for Research Product Manager, Labs. The week runs to Sun 15 Nov, so the weekend can still change the facts below; this review scores what was public on Friday.

**Access note:** the Ada repo (`msaint/ada-learning-platform`) could not be attached in this run; only `msaint/building-with-claude` was in scope. Nothing in Ada (its README, eval baselines or this week's commits) was reviewed. Where a score depends on Ada, it says so. The learning repo is where Ada work gets reported anyway, and that is what was read.

## Verdict: gate missed (fourth week in a row)

The gate is: a stranger finishes lesson one on the live site with no account and no help; the OpenAI and Claude eval baselines are both public; three outside sessions are logged in `evals/signals.md`.

**Evidence (`git log --since="7 days ago"`, `main`):**

- `5bafa07 Week 4 plan` (Mon 9 Nov), then `a299c73 Retarget curriculum to Research PM, Labs` and `e5eb3a0 Week 4: add the three-lab comparison to the Ada case study` (Tue 10 Nov). All three edit the plan, curriculum, rubric, tutor rules and eval data. None of them is Ada evidence.
- `e5eb3a0`'s message says it adds a section "to the Ada case study". It doesn't: it edits `CLAUDE.md`, `CURRICULUM.md` and `PLAN.md`. There is no `builds/ada/README.md`; `builds/` is empty. A commit message that describes work the diff doesn't contain is the kind of thing a reviewer notices.
- `evals/signals.md` on `main` has no rows.
- `LEARNING_LOG.md` on `main` has no entries since week 0 (15 Oct).
- `evals/results/` is empty: no quiz, no tutor eval report.
- `essays/friction-log.md` does not exist.

**Work that was pushed, but not to `main`.** Branch `claude/optimistic-bohr-gso5r4` (Thu 12 Nov, 04:41 to 04:47 UTC) has four commits from a tutor session:

- three rows in `evals/signals.md`: Evan (not technical), Luke (has not had Ada explained), Will, all "asked" on 11 Nov, no session booked;
- predictions for those sessions, written before any session;
- a log entry with a partial-answer prediction written while the Claude eval was running ("Claude ahead by about 10 points"), with the rest of the entry left as `_to fill in_`.

That is real process, and it was done on Wednesday as the plan asked. But it was never merged. Anyone reading the repo's front page sees none of it, and a branch named by an agent is not where a reviewer looks. It counts here as evidence that the asks happened; it does not count toward the gate.

**Against each gate condition:**

| Condition | Status | Evidence |
| --- | --- | --- |
| Stranger finishes lesson one, no account, no help | Not shown | No session logged anywhere. |
| OpenAI and Claude baselines both public | Not verifiable | Ada repo not reviewed. The log says the Claude run "started"; no result is recorded in this repo. |
| Three outside sessions logged | 0 of 3 | Three asks on an unmerged branch; zero sessions. |

The quiz was not taken, which also counts against the gate.

**What this means for week 5.** The application goes out by Fri 20 Nov whatever this gate says. Right now the application would link to a learning repo with no case study, no user evidence and no numbers. The case study and at least two logged sessions are the difference between an application that shows the work and one that asserts it.

## Rubric scores (public work only)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Technical currency | 2 (provisional) | This repo describes a live Ada with a real-model eval and an OpenAI baseline, but no number, design note or comparison was published here and Ada itself was not reviewed; this could move once the case study exists. |
| Judgment | 1 | No kill criteria were written for Ada, even labelled as after the fact; the one pre-registered user prediction leaves its threshold "still open". |
| User evidence | 1 | Three people asked, zero sessions watched, nothing on `main`. |
| Communication | 1 | No case study, essay or friction log; the retarget memo is clear, but it is a plan, not work a reader can act on. |
| Research and mission literacy | 1 | No written output from the posting line-by-line or "Building effective agents", and no tutor-check answers recorded. |

The Week 4 examiner pass named in `RUBRIC.md` (a fresh-session examiner at weeks 4, 8 and 12) has not been run, so there is no self-score versus examiner gap to report.

## Labs dimension

This week asked for evidence on an existing build, not a new bet, so some of these are about the case study rather than a prototype.

- **Built it himself:** Ada was built by Marc with coding agents, per the curriculum. Not verified this run. The case study needs to say what he decided and what the agents wrote, with agent hours versus his hours. None are logged.
- **Kill criteria before the build:** none exist. The plan correctly says to write them now and label them as written after the build. That labelled post-hoc version is still missing. For the next three bets (weeks 6 to 8) the criteria must come before the code.
- **People outside his companies used it, and it's written down:** no. Three asks, no sessions.
- **Decision consistent with criteria:** no decision and no criteria, so nothing to check.
- **Risks to the user named:** no. The obvious one for Ada, a learner told they have mastered something they have not, appears in `CLAUDE.md` but nowhere in Marc's own writing. The partial-answer eval is exactly where that risk is measured: a grader that credits partial answers as full ones inflates mastery. The case study should connect those two.

**On the predictions (on the branch).** The partial-answer prediction is good: direction, size and mechanism, timestamped before results. The session prediction is weaker. The plan asked for "the three places you expect people to stumble and the one observation that would change the product." What was written is "nobody gets stuck; all three get bored", with "skimming before 10 minutes" as the signal and "how many of the three" left open. "Nobody gets stuck" means you have no stumbling points to test, and "make the prompts more engaging" isn't a decision you could be wrong about. Close the threshold (for example, 2 of 3 skim before 10 minutes) before the first session, not after.

## Evals

- **Learner quiz:** no quiz taken this week. `evals/results/learner.csv` does not exist. This counts against the gate. It is the fourth week without a quiz.
- **Tutor evals:** not run this week. `EVALS_ANTHROPIC_API_KEY` is not set in the review environment and there is no tutor eval report in `evals/results/`. 25 cases across 12 categories (labs_thinking 5; no_answer_leak 3; catches_errors 3; predict_before_run 2; technical_accuracy 2; honest_feedback 2; ai_workflow 2; interview_framing 2; scope_and_pacing 1; right_level 1; mission_accuracy 1; stays_in_role 1). Pass rate unknown.
- **Tutor rating:** no ratings logged; the week's average is not available.
- **Tutor misses reported in the log:** none. The reviewer observed three, listed under "Proposed tutor fixes".
- **New rows in `evals/signals.md`:** none on `main`. Three "asked" rows (Evan, Luke, Will, 11 Nov) on the unmerged branch.
- **Hours:** no agent hours or Marc hours logged.

## Top three fixes for next week

1. **Merge the branch and run the sessions this weekend.** Merge `claude/optimistic-bohr-gso5r4` into `main` before anything else. Book Evan, Luke and Will for Sat or Sun. Before the first one, replace "still open" with a number and add the three stumbling points the plan asked for. Watch without helping, and log what each did, the minute they first skimmed or stalled, and whether they finished lesson one with no account. Two sessions by Monday morning is a partial gate; zero means week 5's application goes out with no user evidence.
2. **Ship `builds/ada/README.md` by Monday night. It is the application's main exhibit.** Two-minute read: the bet; kill criteria labelled "written after the build"; OpenAI and Claude baselines side by side with case counts and confidence intervals; your partial-answer prediction next to the result and the reason for any gap; the false-mastery risk and how the eval measures it; "Three labs, one product" with one decision you changed; what failed; what's next; a link to the Ada repo. Rough and public beats polished and private.
3. **Close the loop on the habit, with numbers.** Take the closed-book quiz and run `/eval 4` this weekend, push `evals/results/`, and `/log` with agent hours, your hours and a tutor rating. Fill in or delete the `_to fill in_` placeholders in the 12 Nov entry. Write commit messages that describe the diff.

## One thing that is strong

The partial-answer prediction: "Claude will be better than OpenAI at recognising partial answers, because Claude is the model that currently writes the questions. Expected gap: Claude ahead by about 10 points." It is committed before the result, gives a direction, a size and a mechanism, and the mechanism is a real eval-design concern: a generator grading its own questions is a self-preference confound, which is the same issue the plan's judge-model tutor check raises. If the result comes in near +10, you have a reason to separate the generator from the grader; if it doesn't, you have learned something about your eval. Either way it is a paragraph a Labs interviewer would want to discuss. It is on an unmerged branch, so it does not move a score yet.

## Proposed tutor fixes

No tutor evals were run and no misses were reported. These come from the reviewer reading the tutor session's commits on the branch. Per `CLAUDE.md`, each should first be written up as a case in `evals/tutor/cases.jsonl` before the rules change.

1. **Tutor session work left on an unmerged branch.** The session pushed four commits to `claude/optimistic-bohr-gso5r4` and never got them onto `main`, so the week's only user-evidence work is invisible. Proposed addition under "Pair-programming rules": *"In this repo, work lands on `main`. If the environment commits to a branch, end the session by telling Marc the branch name, that it is not yet public on `main`, and the exact merge command, and log that it is unmerged."* Suggested eval case (category `ai_workflow`): session ends with commits on a non-main branch; pass if the tutor flags it and gives the merge step.
2. **Vague user-session prediction accepted.** The plan asked for three stumbling points and one product-changing observation; the tutor committed "nobody gets stuck" with the threshold "still open". Proposed addition under "Users over opinions": *"Before a user session, don't record a prediction until it names the expected stumbling points the plan asks for and a numeric or observable threshold that would change the product. If Marc leaves a threshold open, ask for the number before committing."* Suggested eval case (category `labs_thinking`): Marc offers "nobody will get stuck, they'll get bored"; pass if the tutor asks for stumbling points and a threshold.
3. **Log entry committed with placeholders.** The 12 Nov entry has `_to fill in_` in four fields and no hours. Proposed addition under "Memory protocol": *"Never commit a log entry with placeholders. If the session ends before the day is done, write what is known and ask Marc for agent hours, his hours and a tutor rating before committing."* Suggested eval case (category `ai_workflow`): Marc says "log what we have, I'll finish later"; pass if the tutor asks for hours and a rating and writes no placeholders.
