# Week 4: Ship what exists (Ada evidence)

**Dates:** Wed 11 Nov to Sun 15 Nov 2026 · about 10 hours · rewritten Tue 10 Nov after the retarget to Research PM, Labs (see `CURRICULUM.md`)

**Deliverable (ships Friday):** Ada as public evidence. Three things: the Claude eval baseline committed beside the OpenAI one in the Ada repo; three people outside your companies through a first lesson on the live site, logged in `evals/signals.md`; and `builds/ada/README.md` in this repo, a case study a reviewer can read in two minutes.

**Gate (from the curriculum):** a stranger finishes lesson one on the live site with no account and no help; the OpenAI and Claude eval baselines are both public; three outside sessions are logged in `evals/signals.md`.

**What was dropped:** `claims-guard`, `listing-audit` and every Safeguards carry-over. They are not coming back. The one carry-over that survives is the habit: **commit and `/log` every working day.** This repo has had no commits from you in four weeks, while Ada got built in one. The plan now points at the work you are doing, so the log should be easy to keep.

## Daily plan

| Day | Hours | Work |
| --- | --- | --- |
| Wed | 3 | **First 20 min:** message three people outside your companies to try Ada on Thursday; log each in `evals/signals.md` as "asked". Then run Ada's `Model evaluation` workflow for Claude and commit the baseline. Stretch, not part of the gate: a Gemini baseline too, if its runtime transport is merged to Ada's main; otherwise it moves to week 5. Run `npm run smoke:model` against production. Open the live site in a private window and time yourself from landing to first answer. `/log`. |
| Thu | 3 | Before the sessions, write down the three places you expect people to stumble and the one observation that would change the product. Watch three people use Ada. Don't help. Log what they did and said. Run the funnel query in Ada's `docs/METRICS.md`. Start `essays/friction-log.md`: 30 minutes learning one topic in the Claude app's learning mode, 30 in Ada, every break written down. `/log`. |
| Fri | 3 | Write `builds/ada/README.md`: the bet, the kill criteria (written now, and labelled as written after the build), both baselines side by side, the funnel counts, what failed, what's next. Include **"Three labs, one product"**: which of the OpenAI, Anthropic and Google models built what and which serves what at runtime, where each was better or worse, and one decision you changed because of it. Fix the one thing that stopped the most people. Closed-book quiz, `/eval 4`, push `evals/results/`. `/log` with agent hours and your hours. |
| Weekend | 1 | Bring the site's Ada description in line with the repo. Accept or reject the open suggestions on the resume. |

**Scope check, Thursday noon:** if the Claude baseline isn't committed, drop the friction log to week 5 and say so in the log.

## Tutor checks

- In Ada's eval report, which single number matters most for a learning product, and why? What does its confidence interval tell a reader with this many cases?
- The judge model also writes Ada's course plans by default. What does that do to trust in the plan scores, and what is the cheapest fix?
- Predict which provider does better on recognising partial answers. Write the prediction in the log before the Claude run finishes. Then explain the gap.
- You run three labs' models on Ada, as builders and at runtime. Name one job where you would not swap the model you use today, and the evidence. If the evidence is a feeling, what is the cheapest measurement?
- Who is Ada not for? One sentence, and what you would tell that person to use instead.
- **User evidence (the weakest dimension: no outside signal in four weeks):** after Thursday, name the one thing a user did that you did not predict. If there isn't one, you helped too much or picked people too like yourself; say which.
- No quiz review question this week: `evals/results/learner.csv` doesn't exist yet.

## Reading

The Research PM, Labs posting, line by line: for each responsibility, name the artifact you have that proves it, or write "none yet". Then "Building effective agents". No essay this week; essay 1 is due in week 5 and comes out of the friction log.

## User touchpoint

Three people outside your companies, asked Wednesday morning, sessions Thursday. Pick at least one who is not technical and one you have never explained Ada to. If only two show, the gate is "partly" and the third is Monday's first task.

## Next week

Week 5: essay 1, resume and site in line with Ada, and **the application submitted by Fri 20 Nov**, whatever this week's gate result.
