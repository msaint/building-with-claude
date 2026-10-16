# Curriculum: 12 weeks building with Claude

The full, illustrated version lives in the Claude doc "Path to Anthropic: 12-Week Curriculum." This file is the working copy the tutor commands read. If the two disagree, update this file.

**Assumptions:** about 20 hours a week. Primary target: Startup Partnerships. Secondary: Research PM, Labs. Stretch: Applied AI Engineer, Beneficial Deployments. Apply at the week 4 gate, not week 12.

**Done means public and used.** A task counts only when it is public and at least one real person outside Marc has used or reviewed it.

---

## Week 1: Retool

**Goal:** build and ship a small Claude-powered Python tool without looking anything up twice.

- Python from Ruby: `uv`, `ruff`, `pytest`; comprehensions, dataclasses and Pydantic, type hints, context managers; `asyncio` basics
- Claude API: Console key and spend limit; Messages API (system prompts, multi-turn, streaming, stop reasons); model tiers and their cost and latency; token counting and cost estimates
- Claude Code: CLAUDE.md, slash commands, skills, subagents, hooks. Rule: no code by hand that Claude Code could write.

**Deliverable:** a CLI tool solving a real problem in one of Marc's businesses (e.g. an Amazon listing auditor), public repo with README.

**Gate:** explain the cost, latency and quality tradeoffs between model tiers for a chosen task, with measured numbers, without notes.

**Tutor checks**
- Predict tokens and cost for a 2,000-word prompt with a 500-word reply on each tier; measure; explain the gap.
- Explain step by step what happens between the API call and the first streamed token reaching the terminal.
- When does the small model win, and when does choosing it backfire?
- Before accepting any function Claude Code writes, explain every line.

---

## Weeks 2–4: Build with Claude

**Goal:** one polished public repo with measured cost, latency and accuracy, used by a founder. This is what he applies with.

**Build:** a claims compliance reviewer for supplement and food brands. Reads a product page or label, flags risky claims under DSHEA and FTC rules, returns structured output with suggested rewrites.

- **Week 2, tool use and structured outputs:** tools, tool choice, parallel calls, tool errors; JSON schema outputs validated with Pydantic; vision and PDF input; v1 end to end
- **Week 3, production:** prompt caching (measure before and after); batch processing; rate limits, retries, cost per 1,000 reviews; retrieval versus long context, decided and justified in writing
- **Week 4, rigor:** apply the prompt engineering guide; hand-label 30–50 real claims as the first eval set; iterate and record accuracy per change; README as a case study

**Gate (then apply):** repo public, two or more operators outside his companies have run it, README reports measured numbers.

**Tutor checks**
- Design the "check a claim" tool schema two ways; predict which the model calls more reliably; test both.
- Predict which of three prompt layouts gets cache hits; test; explain what breaks caching.
- Defend retrieval versus long context with a cost number.
- Write 10 adversarial claims to fool the reviewer; fix what they expose.
- Sort 10 eval failures into categories before changing any prompt.

---

## Weeks 5–8: Flagship (agents, MCP, context, evals)

**Goal:** prove command of agent design, tool design, context management and evaluation.

**Build:** a CPG operator agent. An MCP server exposes Amazon SP-API and Shopify data as tools; an agent answers operator questions ("which SKUs are at stockout risk in 30 days, and why?") and drafts actions for human approval.

- **Week 5, agents:** "Building effective agents"; workflows versus agents; hand-written tool loop, then Claude Agent SDK; human approval on anything that writes
- **Week 6, MCP:** read the spec; build the server applying "Writing effective tools for agents"; test from Claude Code and the Claude app; installable in under 15 minutes
- **Week 7, context engineering:** read the context engineering post; memory, summarization, subagents; package one workflow as a skill; essay on the context-layer thesis
- **Week 8, evals:** 50–100 cases, code-graded where possible, model-graded where not; hand error analysis of 50 failures; compare two model tiers on quality versus cost; publish the write-up

**Gate:** a stranger installs it in under 15 minutes, three or more operators have used it, eval results are public.

**Tutor checks**
- Without code, draw the agent loop including exactly where a human approves.
- For three founder use cases the tutor provides, argue workflow or agent.
- Rewrite a bad MCP tool description; measure tool-selection accuracy before and after.
- At step 20 of a long task, what stays in context and what gets summarized or dropped?
- Measure a model grader's agreement with his own labels on 20 cases.

---

## Weeks 9–12: Capstone

**Track A (main), founder program pilot:**
- Week 9: "building with Claude" playbook for early-stage founders; recruit 8–12 founders
- Week 10: two hands-on workshops of about 3 hours, then weekly office hours
- Week 11: follow up; measure time to first prototype, what shipped, where they got stuck
- Week 12: publish the playbook and a field report: what blocks founders, and three program ideas to remove those blocks

**Track B (light, if pursuing Labs):**
- Week 9: pick a newly possible capability; three product hypotheses
- Week 10: cheapest prototype; 10 user sessions
- Week 11: iterate and instrument
- Week 12: one-page product memo plus a 3-minute demo

**Tutor checks**
- Dry-run each workshop with Claude playing a non-technical founder, a skeptical senior engineer, and an AI-native founder in a hurry.
- Field report review: as a head of startup partnerships, which recommendation would you fund first, and why?
- Labs memo review: as a researcher, is this capability genuinely new or a better wrapper?

---

## Parallel track: research and safety literacy (about 4 hours a week)

Each week: read, run `/explain-back` on the core claim, then publish a 500–800 word essay that survives a skeptical-researcher review.

| Week | Reading | Essay prompt |
| --- | --- | --- |
| 1 | Core Views on AI Safety; Anthropic's PBC structure | Why a safety-focused lab is also the right partner for startups |
| 2 | Responsible Scaling Policy | What the RSP means for a startup building on Claude |
| 3 | Claude's constitution | How a model's character should shape product design |
| 4 | 3Blue1Brown neural network and transformer series | Explain a transformer to a CPG founder |
| 5 | Karpathy, Zero to Hero, through "Let's build GPT" (budget 8 hours) | What building a tiny model taught you about the big ones |
| 6 | Constitutional AI paper; RLHF basics | How models are trained to be helpful and harmless |
| 7 | Scaling Monosemanticity; On the Biology of a Large Language Model | What interpretability could unlock for products |
| 8 | Alignment faking; agentic misalignment | Guardrails a startup shipping agents should build in |
| 9 | Anthropic Economic Index | Where AI is actually used, and what that means for founders |
| 10 | Current frontier model system card | What a system card tells a builder, and what it doesn't |
| 11–12 | Recent Anthropic research and engineering posts | Capability scan: three things newly possible, a product for each |

---

## Milestone posts

| Week | Post |
| --- | --- |
| 1 | What I'm building over the next 12 weeks, and for whom |
| 4 | Launch: the claims compliance reviewer, with cost and accuracy numbers |
| 6 | Launch: the CPG operator MCP server |
| 8 | What evals caught that I would have missed |
| 10 | Recap: teaching founders to build with Claude |
| 12 | The field report, plus a retrospective |
