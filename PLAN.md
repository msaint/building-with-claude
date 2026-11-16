# Week 5: Ship what exists (apply)

**Dates:** Mon 16 Nov to Sun 22 Nov 2026 · about 12 hours · written Mon 16 Nov by the Monday coach

**Deliverable (ships Friday):** the application to Research PM, Labs, submitted by **Fri 20 Nov**, linking to a public Ada case study (`builds/ada/README.md`) and essay 1.

**Gate (milestone, from the curriculum):** application submitted to Research PM, Labs by Fri 20 Nov, whatever the week 4 gate result. A missed week 4 gate is reported in the review; it does not hold the application.

## Carry-over from the week 4 review (gate missed, fourth week running)

State of play on Monday morning: the session work from 12 Nov is still on `claude/optimistic-bohr-gso5r4`, not `main`; `builds/` is empty; `evals/signals.md` has no rows on `main`; Ada's `evals/baselines/` holds only `openai-2026-11-10` (no Claude baseline), and Ada has had no commits since 10 Nov.

1. **Merge the branch first.** `git checkout main && git pull && git merge origin/claude/optimistic-bohr-gso5r4 && git push`. Then replace the `_to fill in_` placeholders in the 12 Nov entry with facts, or delete them.
2. **Case study by Tuesday night.** It is the application's main exhibit. Contents as the review listed: the bet; kill criteria labelled "written after the build"; both baselines side by side with counts and intervals; your +10 partial-answer prediction next to the result; the false-mastery risk and which eval number measures it; "Three labs, one product" with one decision you changed; what failed; what's next; link to Ada.
3. **Sessions, with a closed prediction.** Before the first one, set the threshold (for example "2 of 3 skim before 10 minutes") and name three stumbling points.

**Cut, to fit 12 hours:** the Gemini baseline; "fix the top two problems from the week 4 sessions" (there were none) becomes "fix one only if a session shows a blocker before Thursday"; the week 4 examiner pass moves to week 8. Essay 1 does not hold the application.

## Daily plan

| Day | Hours | Work |
| --- | --- | --- |
| Mon | 2.5 | **First 15 min:** merge the branch; message Evan, Luke and Will to book Tue or Wed. Close the session prediction (threshold plus three stumbling points) and commit it. Finish the Claude eval run, commit the baseline beside the OpenAI one in Ada, and log the partial-answer result against your +10 prediction. `/log`. |
| Tue | 2.5 | Write `builds/ada/README.md` v1 and push it tonight, rough beats private. Session 1 if booked: watch, don't help, log it in `evals/signals.md`. `/log`. |
| Wed | 2.5 | Sessions 2 and 3; add what they did to the case study. 30 min in the Claude app's learning mode and 30 in Ada on one topic; start `essays/friction-log.md` with every break. **Scope check, Wed noon:** if fewer than 2 sessions are booked, the application goes out with the case study and the asks only, and you say so in the log. `/log`. |
| Thu | 2.5 | Resume and site match the case study (Ada as it is, with numbers). Draft the application. Draft essay 1, 500 to 800 words, from the friction log. `/log`. |
| Fri | 2 | **Submit the application by noon.** Publish essay 1, or log that it slipped to the weekend. Closed-book quiz, `/eval 5`, push `evals/results/`. `/log` with agent hours, your hours and a tutor rating. |

## Tutor checks

- In Ada's eval report, which single number matters most for a learning product, and why? What does its interval tell a reader with this many cases?
- Your partial-answer prediction was Claude +10. What was the result, and does the gap support your mechanism or something else?
- The judge model also writes Ada's course plans by default. What does that do to trust in the plan scores, and what is the cheapest fix?
- Before the sessions: three stumbling points and the one observation that would change the product. Afterwards: did it?
- Who is Ada not for? One sentence, and what you would tell that person to use instead.
- **Judgment (weakest with user evidence; no kill criteria exist for Ada):** write Ada's kill criteria now, labelled post-hoc. Each must be a number or an observable behaviour. Which one would Ada fail today?
- No quiz review question: `evals/results/learner.csv` doesn't exist yet. Friday's quiz creates it.

## Reading and writing

Anthropic's Education Report on how university students use Claude, and the learning mode announcement. Run `/explain-back` on one claim from each. **Essay 1:** what learning inside a chat app is missing, from running a course both ways. It must survive a sceptical-researcher read: every claim backed by the friction log or a session.

## User touchpoint

Evan, Luke and Will, asked 11 Nov. Book them Monday for Tue or Wed. At least one is not technical and one has never had Ada explained. One stranger finishing lesson one with no account and no help is still the week 4 gate.

## Next week

Week 6, bet 1: Ada inside Claude as a skill plus an MCP server. Thanksgiving week, 8 hours. Kill criteria come before the code.
