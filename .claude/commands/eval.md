---
description: Run the weekly evals on both sides and summarize them
argument-hint: <week number>
---

Week: $ARGUMENTS

1. Remind Marc the learner quiz is closed book, then tell him to run it himself in a terminal (it's interactive): `uv run python evals/learner/quiz.py --week $ARGUMENTS`. Wait until he says it's done. Do not help with the answers.
2. Run the tutor evals: `uv run python evals/tutor/run_tutor_evals.py`.
3. Read `evals/results/learner.csv`, the newest `evals/results/tutor-*.md`, this week's session ratings in `LEARNING_LOG.md`, and `evals/signals.md`.
4. Summarize in under 15 lines:
   - Learner: this week's quiz score, review-question score, and the weakest topic
   - Tutor: pass rate by category, every failed case, and the average session rating
   - Outside signals added this week
   - One change to make to Marc's plan, and one change to `CLAUDE.md` if a tutor case failed
5. For any failed tutor case, propose a specific edit to `CLAUDE.md`, but do not apply it until Marc agrees. After applying, rerun only that case with `--only <id>` and then the full suite to check nothing else broke.
