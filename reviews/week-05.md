# Week 5 review: Ship what exists (apply)

**Reviewed:** Fri 20 Nov 2026, 23:50 UTC (17:50 Central), by the scheduled Friday reviewer, reading the public repos as a hiring manager on Anthropic's Labs team would for Research Product Manager, Labs. The week runs to Sun 22 Nov, but the milestone was dated today, so this review scores what was public on Friday evening.

**Access:** both repos were read this run: `msaint/building-with-claude` (`main` plus the unmerged branch) and, for the first time, `msaint/ada-learning-platform` (`main`, history back to 10 Nov).

## Verdict: milestone missed on the public record (fifth gate missed in a row)

The milestone was: **application to Research PM, Labs submitted by Fri 20 Nov**, linking to a public Ada case study (`builds/ada/README.md`) and essay 1.

There is no public evidence the application went out. If it did, nothing in either repo says so, and the exhibits it was supposed to link to do not exist. Either way the reader sees the same thing.

| Condition | Status | Evidence |
| --- | --- | --- |
| Application submitted by Fri 20 Nov | Not shown | No log entry, signal or commit mentions it. |
| Ada case study public (`builds/ada/README.md`) | Missing | `builds/` is still empty. The plan's deadline was Tue night. |
| Essay 1 | Missing | `essays/` is empty. No `friction-log.md` either. |
| Week 4 carry-over: merge the branch | Not done | `claude/optimistic-bohr-gso5r4` (12 Nov) is still not an ancestor of `main`. |
| Week 4 carry-over: Claude baseline in Ada | Not done | Ada `evals/baselines/` still holds only `openai-2026-11-10`. |
| Week 4 carry-over: 2 to 3 outside sessions | 0 | `evals/signals.md` on `main` has no rows. |
| Closed-book quiz | Not taken | `evals/results/` is empty. Counts against the gate. |

**What was pushed this week.**

- *Learning repo, `main`:* one commit by Marc, `3d55577 Week 5 plan` (Mon 16 Nov), which is the Monday coach's plan plus three quiz questions. Nothing else. No log entry, no signals, no case study, no results. Marc pushed no work of his own to the learning repo this week.
- *Ada, `main`:* six commits, all on Thu 19 Nov between 14:03 and 19:13 Central, 81 files, +7,431 / −1,416. In order: KaTeX and session cookies (this commit also splits `sessions.ts` into five modules, adds prompt caching and adds a held-out grading split; the message mentions only the split); a dark-theme redesign that adds a character companion (+1,743); removal of that companion eleven minutes later (−910 lines); guests limited to one draft or course; memoised workspace data; and a fix for order-dependent multiple-choice answers.

That is a real day of building, and some of it is good (below). But none of it was on this week's plan, none of it is reported in the learning repo, and it happened on the day the plan reserved for drafting the application. The plan cut the week to 12 hours so that the case study, the sessions and the application would fit. The hours went to UI.

## Rubric scores (public work only)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Technical currency | 3 | Read for the first time this run, Ada is a working product with unit, integration and E2E tests, a real-model eval and, this week, a held-out grading split and Anthropic prompt caching; not 4, because there is no measured number for any of it (no cache hit rate, no holdout result, still no Claude baseline). The move from 2 is because Ada was reviewed, not because of anything reported this week. |
| Judgment | 1 | Still no kill criteria for Ada, even post-hoc; the character companion was built at 14:55 and removed at 15:06 with no criterion or reason written anywhere; the week's hours went to work the plan did not ask for while the dated milestone slipped. |
| User evidence | 1 | Three people asked on 11 Nov, zero sessions watched, nothing on `main`. |
| Communication | 1 | No case study, essay, friction log or log entry. One Ada commit message (`95ef905`) again describes a fraction of its diff. |
| Research and mission literacy | 1 | No `/explain-back` on the Education Report or learning mode, no tutor-check answers written down. |

## Labs dimension

This week was the application, not a new bet, so the questions apply to Ada as the exhibit.

- **Built it himself:** yes, with coding agents; the commits are his. Agent hours versus his hours are not logged anywhere, so the case study can't yet say which decisions were his.
- **Kill criteria before the build:** none, and the week 5 tutor check that asked for post-hoc criteria is unanswered. The companion is the clearest example: a feature that was built and then killed the same afternoon is exactly the kind of decision a Labs PM should be able to show, with a written reason. As it stands, the evidence is two commit messages and a −910 diff.
- **People outside his companies used it, and it's written down:** no.
- **Decision consistent with criteria:** no criteria, so it can't be checked.
- **Risks to the user named:** not in Marc's writing. The product did reduce one this week (see "strong", below), and the held-out split guards against a grader tuned to its own test cases. Neither is connected, in words, to the false-mastery risk.

## Evals

- **Learner quiz:** not taken. `evals/results/learner.csv` does not exist. Fifth week without a quiz; counts against the gate.
- **Tutor evals:** not run this week. `EVALS_ANTHROPIC_API_KEY` is not set in the review environment and there is no tutor eval report in `evals/results/`. 25 cases across 12 categories; pass rate unknown, so there are no failed cases to list.
- **Tutor rating:** none logged; no weekly average.
- **Tutor misses reported in the log:** none (there are no log entries this week).
- **New rows in `evals/signals.md`:** none on `main`. The three "asked" rows from 11 Nov are still only on the unmerged branch.
- **Hours:** no agent hours or Marc hours logged.

## Top three fixes for next week

1. **Saturday: submit the application if it hasn't gone, and log it either way.** Do not wait for a perfect exhibit. Merge `claude/optimistic-bohr-gso5r4` (`git checkout main && git pull && git merge origin/claude/optimistic-bohr-gso5r4 && git push`), then push `builds/ada/README.md` v1 the same day, rough: the bet, kill criteria labelled "written after the build", the OpenAI baseline with counts and intervals, the partial-answer prediction, the false-mastery risk and which eval number measures it, the companion you built and removed and why, and a link to Ada. Then a `LEARNING_LOG.md` entry with the submission date and time. If it went out today, say so in the log; an application nobody can see you sent doesn't count for the curriculum.
2. **Week 6 starts with kill criteria in a commit, before any Ada code.** Bet 1 (Ada inside Claude as a skill plus MCP) has an 8-hour week. Monday, before code: a one-page bet in `essays/` with the day-2 return threshold that kills it, as a number, committed. And book the five people Monday, starting with Evan, Luke and Will, who have now waited nine days.
3. **Put a number on Thursday's work.** Run the Claude eval (the `Model evaluation` workflow), commit the baseline beside the OpenAI one, and run `--split holdout` for both. Report three numbers in the case study: partial-answer accuracy for each provider against your +10 prediction, and holdout versus train accuracy. Prompt caching shipped too; one cache hit rate and the cost per lesson before and after would turn a feature into evidence.

## One thing that is strong

`b9e2ffd`, "prevent order-dependent multiple choice answers". Ada shuffles choices and numbers them 1 to N, but the model writes rationales that say "option c" and options like "All of the above". After a shuffle, those point at the wrong answer: the learner gets feedback explaining why a different option is right, which is a quiet way to teach the wrong thing. The fix works at three layers: schema descriptions telling the model the constraint, a validator that rejects position-dependent choices, and remapping of rationale labels to the displayed order, with three unit tests, one of which checks that ordinary English prose isn't mangled. That is someone finding a failure that only shows up in a learner's lesson, and fixing it where it starts rather than patching the UI. Write it up in the case study under risks; it's a better story than the redesign.

## Proposed tutor fixes

No tutor evals ran and no misses were reported, so there are no failed cases to fix. One observation from the commits, offered for Marc to confirm or discard. Per `CLAUDE.md`, write it up as a case in `evals/tutor/cases.jsonl` before changing any rule. None of the three fixes proposed in the week 4 review has been written up as a case or adopted yet.

1. **Scope drift in a build repo not flagged against the dated milestone.** On Thursday, the day the plan set aside for drafting the application, a long agent session in Ada shipped a UI redesign and a feature it then deleted, while the case study, the sessions and the application were all outstanding. The tutor rule "if the scope is slipping, say so by Wednesday" was not followed, as far as the record shows (nothing was logged Wednesday). If the session ran under Ada's own `CLAUDE.md`, the learning-repo rules never loaded, which is the gap. Proposed addition under "Pair-programming rules": *"When a session in a build's repo starts, read this repo's `PLAN.md` first. If the work Marc asks for is not on this week's plan and a dated deliverable is outstanding, name the deliverable and the time left before starting, and ask whether this work replaces it. Log the answer."* For it to load in Ada, add one line to Ada's `CLAUDE.md` pointing to it (Marc's call; the reviewer does not edit Ada). Suggested eval case (category `scope_and_pacing`): it's Thursday, the application is due Friday and the case study is missing; Marc says "let's redesign the dashboard". Pass if the tutor names the application and the case study before doing anything, and asks which one gives way.
