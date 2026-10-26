# Week 2: Build a safeguard (tool use and structured outputs)

**Dates:** Mon 26 Oct to Fri 30 Oct 2026 · about 20 hours

**Deliverable (ships Friday):** `claims-guard` v1 in `builds/claims-guard/`. It has a one-page policy spec (`POLICY.md`) written like a usage policy, three harm categories with severity, and an intervention ladder (allow, warn, suggest rewrite, block). It also has a Python CLI that takes the text of a product page, calls a "check a claim" tool, and returns findings validated with Pydantic, one intervention per claim. Run it end to end on 15 hand-labeled real claims and put the results table in the README.

**Gate (phase gate, checked at week 4):** repo public, two or more operators outside his companies have run it, README reports precision and recall by category and explains the threshold chosen. **This week's bar:** v1 runs end to end on the 15 labeled claims, every output passes validation, and failures are counted and reported, never dropped.

**Carry-over (week 1 review: gate missed, nothing pushed):** ship the cut-down `listing-audit` **Monday, before any week 2 work**: 10 listings, 3 tiers, one table (tokens, cost, p50 latency, agreement with your labels), README with what failed. Push it rough. Then commit and `/log` at the end of every session this week, with hours, agent hours and a tutor rating.

**Cut because you're behind (no extra hours):** vision and PDF input moves to week 3. The policy covers 3 harm categories, not every one: disease claims, unsubstantiated structure/function claims, misleading testimonials. 15 labeled claims instead of 50 (week 4 grows it). Week 1's essay replaces week 2's: the ASL-3 essay moves to week 3, and the RSP reading shrinks to a skim. The week 1 milestone post becomes one paragraph in the essay.

## Daily plan

| Day | Hours | Work |
| --- | --- | --- |
| Mon | 4 | **First:** message one supplement or food operator (Jade Leaf alum or portfolio founder) and book a 30-minute Thursday slot. Then ship `listing-audit` (carry-over above), push, `/log`. |
| Tue | 4 | Write `POLICY.md` yourself before prompting: allowed vs risky, why, two examples each side per category, severity, intervention for each. Collect and hand-label 15 real claims, including 3 borderline ones. Write down the cost of a false positive and of a miss. |
| Wed | 4 | Tool use: design the check-a-claim tool two ways, `tool_choice`, tool errors, Pydantic validation, retry on failure. v1 end to end. **Scope check:** if v1 isn't running by tonight, drop the rewrite suggestion and ship allow/warn/block only. |
| Thu | 4 | Operator runs it on their own product page; log it in `evals/signals.md`. Fix the top issue. README: problem, policy, design, results table, what failed. |
| Fri | 4 | Essay. Closed-book quiz, `/eval`, push `evals/results/`. Log agent hours vs your hours. |

**Workflow rule:** run two agents in parallel on Tuesday: one collects and cleans real claims from public product pages while you write the policy, and one scaffolds the Pydantic models and tests. Review their output at a set time; don't watch them work.

## Tutor checks

- Design the "check a claim" tool schema two ways; predict which the model calls more reliably; test both on the 15 claims and report the numbers.
- What does your code do when the tool input fails validation, or the model returns no tool call? Show the test.
- Before any prompt change, sort every wrong finding from the 15 into categories.
- A false positive costs a brand legitimate sales; a miss risks an FTC warning letter. Put a rough dollar figure on each for one real brand, and say which way that pushes the threshold.
- **Founder empathy (weakest-scored dimension, tied at 1):** before Thursday's session, write the three questions you'll ask the operator and the one answer that would make you change the design. Afterwards, record whether it changed.

## Reading and essay

- **Read:** Responsible Scaling Policy (skim the ASL definitions only). Re-read "Building safeguards for Claude" next to your `POLICY.md`. Run `/explain-back` on how Anthropic moves from policy to detection.
- **Essay (500 to 800 words, carried from week 1):** How a policy becomes detection: lessons from FTC claims rules and payment fraud. Use `POLICY.md` as the worked example. End with one paragraph on what you're building over the 12 weeks, and for whom.

## Founder touchpoint

Nobody is lined up (`evals/signals.md` is empty). Monday's first task is to book one supplement or food operator outside your companies for a 30-minute Thursday session. They run `claims-guard` on their own product page, and you log what they said. This is the first of the two outside operators the week 4 gate needs.
