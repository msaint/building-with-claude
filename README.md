# Building with Claude: 12 weeks

A public record of 12 weeks rebuilding my engineering skills around Claude: shipping real tools for consumer-brand operators, teaching founders to build with Claude, and writing about what I learn.

I was a startup CTO and API product lead in San Francisco, then co-founded Jade Leaf Matcha and grew it into the #1 matcha brand in the US. Since 2022 I've been investing in AI companies. This repo is me getting back to building.

Live progress: https://claude.ai/artifact/EYMT3aQDYaopkYHMyDDzoK

## What's here

| Folder | Contents |
| --- | --- |
| `builds/` | Each project, with a README written as a case study: problem, design, numbers, what failed |
| `essays/` | Weekly essays on AI research, safety, and what they mean for builders |
| `reviews/` | Weekly reviews of my work against a public rubric, warts included |
| `LEARNING_LOG.md` | Daily log of what I built, learned, and got stuck on |
| `progress/` | Data for the live progress site, refreshed every Friday |
| `RUBRIC.md` | How I score progress, and the score history |
| `evals/` | Evals on both sides: a closed-book quiz that tests me, and an eval suite that tests my AI tutor |
| `CURRICULUM.md` | The plan |

## Builds

| Week | Build | Status |
| --- | --- | --- |
| 1 | CLI tool | Not started |
| 2–4 | Claims safeguard for supplement and food brands: policy, detection, interventions, metrics | Not started |
| 5–8 | CPG operator agent and MCP server, red-teamed against prompt injection | Not started |
| 9–12 | Safeguards product spec, plus a founder workshop | Not started |

## How this repo works

Claude Code acts as tutor and pair programmer. `CLAUDE.md` sets the tutor rules, and the commands in `.claude/commands/` run planning, check-ins, quizzes and reviews. A scheduled task reviews each week against the rubric and writes the result to `reviews/`.
