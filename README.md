# Building with Claude: 12 weeks

A public record of 12 weeks rebuilding my engineering skills around Claude: prototyping AI products myself, putting them in front of real users, deciding what to keep and what to kill, and writing about what I learn.

I was a startup CTO and API product lead in San Francisco, then co-founded Jade Leaf Matcha and grew it into the #1 matcha brand in the US. Since 2022 I've been investing in AI companies. This repo is me getting back to building.

Live progress: https://claude.ai/artifact/EYMT3aQDYaopkYHMyDDzoK

## What's here

| Folder | Contents |
| --- | --- |
| `builds/` | A case study per build (the bet, design, numbers, what failed, the decision), linking to its own repo |
| `essays/` | Essays on AI research and what it makes possible, one-page bet memos, and a running friction log |
| `reviews/` | Weekly reviews of my work against a public rubric, warts included |
| `LEARNING_LOG.md` | Daily log of what I built, learned, and got stuck on |
| `progress/` | Data for the live progress site, refreshed every Friday |
| `RUBRIC.md` | How I score progress, and the score history |
| `evals/` | Evals on both sides: a closed-book quiz that tests me, and an eval suite that tests my AI tutor |
| `CURRICULUM.md` | The plan |

## Builds

| Week | Build | Status |
| --- | --- | --- |
| 1–3 | Earlier plan (a claims safeguard); retargeted on 10 Nov 2026 | Dropped, nothing shipped |
| 4–5 | [Ada](https://github.com/msaint/ada-learning-platform), an adaptive learning platform: both model baselines, first outside users, case study | In progress |
| 6–8 | Three capability bets, one a week, each with a public kill-or-keep memo | Not started |
| 9–11 | Flagship: the surviving bet, with an outcome eval and 25 outside users | Not started |
| 12 | A Labs-style product memo, plus a retrospective | Not started |

## How this repo works

Claude Code acts as tutor and pair programmer. `CLAUDE.md` sets the tutor rules, and the commands in `.claude/commands/` run planning, check-ins, quizzes and reviews. A scheduled task reviews each week against the rubric and writes the result to `reviews/`.
