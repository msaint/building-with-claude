# Evals: checking quality on both sides

Two things can go wrong in this curriculum: I might not actually be learning, or my tutor might not actually be teaching well. These evals check both, every week, with numbers.

| Side | Question | How it's measured | Cadence |
| --- | --- | --- | --- |
| Learner (me) | Do I know it closed-book, and do I still know it weeks later? | `learner/quiz.py`: closed-book quiz, model-graded against key points, with spaced repetition of weak topics | Every Friday, before the review |
| Learner (me) | Does my work hold up? | Each build's own eval suite, plus `ruff` and `pytest` | Every commit to a build |
| Learner (me) | Does it hold up to outsiders? | Founders who used each build, and what they said | Logged weekly in `signals.md` |
| Tutor (Claude) | Does the tutor follow its own rules? | `tutor/run_tutor_evals.py`: 22 scenarios testing answer leaks, predict-before-run, catching errors, accuracy, honest feedback, pacing, AI workflow, safeguards thinking, and interview framing | Weekly, and whenever `CLAUDE.md` changes |
| Tutor (Claude) | Did the tutor actually help, in real sessions? | My 1–5 session rating and any flagged miss, recorded with `/log` | Every session |
| Both | Is the grader itself trustworthy? | I hand-grade 10 quiz answers and 10 tutor replies; measure agreement with the model grader | Weeks 4 and 8 |

## Setup

```bash
uv sync                      # installs the anthropic SDK
export ANTHROPIC_API_KEY=... # keep it in .env, never commit it
uv run python evals/tutor/run_tutor_evals.py --dry-run
uv run python evals/learner/quiz.py --week 1 --dry-run
```

Model names default to the current Sonnet tier for the tutor and Opus tier for the grader. Override with `TUTOR_MODEL` and `GRADER_MODEL` if they change.

## Rules that keep the evals honest

- **Closed book.** Take quizzes without Claude, notes, or the question bank open. A quiz I cheat on measures nothing.
- **Don't train to the test.** Read the question bank only to add new questions, ideally after you've been quizzed on the old ones.
- **Different grader from tutor.** The grader uses a separate prompt and a stronger model than the tutor, and never sees the tutor's reasoning.
- **Fix the tutor with evals, not vibes.** When a real session goes badly, write it up as a new case in `tutor/cases.jsonl` first, confirm it fails, then change `CLAUDE.md` and confirm it passes without breaking others.
- **Audit the grader.** At weeks 4 and 8, hand-grade 20 items and compute agreement. Below 80% agreement, fix the criteria before trusting any scores.

## Adding to the evals

- Each week, add 2–3 questions to `learner/question_bank.jsonl` for the next week's topics, with 3–5 key points each.
- Every flagged miss from `/log` becomes a tutor case.
- By week 12 this folder is a portfolio piece on its own: an eval suite for an AI tutor, built and improved with real data.
