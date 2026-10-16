---
description: Append today's entry to the learning log
---

Append an entry to `LEARNING_LOG.md` using this format, filling it from the session and asking Marc for anything you can't tell:

```
## YYYY-MM-DD · Week N

- **Did:** what shipped or moved, with links or commit hashes
- **Learned:** one concept, in one sentence, in Marc's words
- **Numbers:** any measurement (tokens, cost, latency, accuracy)
- **Stuck on:** anything unresolved
- **Next:** the one next thing
- **Tutor rating:** 1–5, "did the tutor make me think and get it right?"
- **Tutor miss:** any time the tutor gave away an answer, was wrong, or wasted time (or "none")
```

Ask Marc for the tutor rating and miss directly; never fill them in yourself. If he reports a miss, offer to turn it into a new case in `evals/tutor/cases.jsonl`.

Keep it under 10 lines. Don't rewrite earlier entries.
