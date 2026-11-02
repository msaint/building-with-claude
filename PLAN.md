# Week 3: Build a safeguard (production)

**Dates:** Mon 2 Nov to Fri 6 Nov 2026 · about 20 hours

**Deliverable (ships Friday):** `claims-guard` in `builds/claims-guard/`, running on the 15 labeled claims with production basics measured: prompt caching before and after (tokens, cost, p50 latency), retries on rate-limit and overload errors, a cost per 1,000 reviews, and a one-paragraph retrieval versus long context decision with a cost number. README results table includes all of it, plus one outside operator's run.

**Gate (phase gate, checked at week 4):** repo public, two or more operators outside his companies have run it, README reports precision and recall by category and explains the threshold chosen. **This week's bar:** v0 pushed by Tuesday night; by Friday, caching is measured with real numbers, cost per 1,000 reviews is in the README, and one outside operator has run it and is logged in `evals/signals.md`.

**Carry-over (week 2 review: gate missed, second week, nothing pushed):**
1. `listing-audit` is dropped for good. Its tier comparison returns as one table in `claims-guard` (15 claims, two tiers).
2. **Ship `claims-guard` v0 by Tuesday night:** your own one-page `POLICY.md` (3 categories), `claims.csv` with 15 hand-labeled real claims including 3 borderline, and a CLI that prints one validated finding per claim with failures counted. Push it rough. Caching and cost come only after v0 is pushed.
3. **Commit every working day**, even one file, and `/log` with hours, agent hours and a tutor rating.
4. **Operator message is Monday's first task**, logged in `evals/signals.md` as "asked".
5. Take the closed-book quiz Friday and push `evals/results/`.

**Cut because you're behind (no extra hours):** interventions are allow/warn/block only; rewrite suggestions move to week 4 or later. Batch processing becomes a written estimate, not a build. Vision and PDF input is dropped from this phase. Retrieval versus long context is a decision paragraph with a cost number, not two implementations. One essay only (the carried week 1 essay); the ASL-3 and constitution essays are cut, readings kept as a skim.

## Daily plan

| Day | Hours | Work |
| --- | --- | --- |
| Mon | 4 | **First:** message one supplement or food operator outside your companies; book 30 minutes Thursday; log "asked". Write `POLICY.md` yourself, no prompting. Commit it today. `/log`. |
| Tue | 4 | Hand-label 15 real claims (3 borderline). v0 CLI end to end with Pydantic validation and failure counts. **Push by tonight.** Two agents in parallel: one collects claims while you write labels, one scaffolds models and tests. |
| Wed | 4 | Prompt caching: predict, then measure three prompt layouts (cache hits, tokens, cost, latency). Retries with backoff. **Scope check:** if v0 wasn't pushed Tuesday, drop caching layouts to one and say so in the log. |
| Thu | 4 | Operator runs it on their own product page; log it. Cost per 1,000 reviews (cached vs uncached, two tiers). Retrieval vs long context paragraph. README results table. |
| Fri | 4 | Essay. Closed-book quiz, `/eval`, push `evals/results/`. Log agent hours vs your hours. |

## Tutor checks

- Predict which of three prompt layouts gets cache hits; test; explain what breaks caching.
- Defend retrieval versus long context with a cost number per 1,000 reviews.
- What does your code do on a 429 or 529, and after the last retry fails? Show the test. A dropped claim must never read as "allowed".
- A false positive costs a brand legitimate sales; a miss risks an FTC warning letter. Put a rough dollar figure on each for one real brand (Jade Leaf is fine) and say which way it pushes the threshold. Carried from week 2.
- **Judgment (tied lowest at 1; founder empathy had last week's check):** before Wednesday, write three lines in the log: what you are not building this week, why, and what evidence would make you add it back. Friday, check whether any of it came back without that evidence.

## Reading and essay

- **Read:** prompt caching docs; rate limits and errors docs. Skim the ASL-3 deployment safeguards report and Claude's constitution. Run `/explain-back` on what breaks a cache.
- **Essay (500 to 800 words, carried from week 1):** How a policy becomes detection: lessons from FTC claims rules and payment fraud. Use `POLICY.md` as the worked example; end with one paragraph on what you're building over 12 weeks, and for whom.

## Founder touchpoint

Still nobody lined up (`evals/signals.md` is empty for two weeks). Monday's first task: book one supplement or food operator outside your companies for Thursday. Week 4 needs two, so ask a second person the same day. Optional: set up a short Wednesday `/checkin` that reads `git log` and pings you if `builds/` hasn't changed.
