# Week 1: Retool

**Dates:** Mon 19 Oct to Fri 23 Oct 2026 · about 20 hours

**Deliverable (ships Friday):** `listing-audit`, a Python CLI that audits an Amazon listing (title, bullets, description) against a written rule set and returns structured findings. Public repo under `builds/listing-audit/`, with a `--model` flag and a small benchmark (20 real listings, run on all three tiers). README as a short case study: problem, design, numbers, what failed, what's next. Keep claims compliance out of scope; that is weeks 2 to 4.

**Gate:** explain the cost, latency and quality tradeoffs between model tiers for a chosen task, with measured numbers, without notes.

**Carry-over:** none. This is the first week, so there is no prior review or quiz result to fix.

## Daily plan

| Day | Hours | Work |
| --- | --- | --- |
| Mon | 4 | **First:** line up one Amazon seller (Jade Leaf alumni or a portfolio founder) to run the tool Thursday. Then: Console key with a spend limit; `uv init`, `ruff`, `pytest` in `builds/listing-audit/`; first Messages API call with a system prompt. Predict tokens before each call. |
| Tue | 4 | Multi-turn, streaming, stop reasons. Pydantic models for findings. Write the 10-rule spec yourself before prompting. Read "Building safeguards for Claude". |
| Wed | 4 | Collect 20 listings, hand-label the expected findings. Run all three tiers: tokens, cost, p50 latency, agreement with your labels. Scope check: if the benchmark isn't running by tonight, cut to 10 listings. |
| Thu | 4 | Seller runs the tool; log what they said in `evals/signals.md`. Fix the top issue. README with the numbers table. Read the Usage Policy and the employment report. |
| Fri | 4 | Essay and milestone post. Closed-book quiz, `/eval`, weekly review. Log agent hours versus your hours. |

**Workflow rule:** no code by hand that Claude Code could write. Use one subagent to collect and clean listings while you write the rule spec, and add a `/bench` slash command so the tier run is one line.

## Tutor checks

- Predict tokens and cost for a 2,000-word prompt with a 500-word reply on each tier; measure; explain the gap.
- Explain step by step what happens between the API call and the first streamed token reaching the terminal.
- When does the small model win, and when does choosing it backfire? Answer with your benchmark numbers.
- Before accepting any function Claude Code writes, explain every line.
- **Judgment (baseline; no review yet):** name one feature you decided not to build this week, and the cost of a wrong audit finding to a seller, in dollars or hours.

## Reading and essay

- **Read:** Building safeguards for Claude; Anthropic's Usage Policy; How employment is changing at Anthropic. Run `/explain-back` on each core claim.
- **Essay (500 to 800 words):** How a policy becomes detection: lessons from FTC claims rules and payment fraud.
- **Milestone post:** What I'm building over the next 12 weeks, and for whom.

## Founder touchpoint

Nobody is lined up yet. Monday's first task is to book one Amazon seller for a 30-minute Thursday session where they run `listing-audit` on their own listing and tell you what is wrong with it.
