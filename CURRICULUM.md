# Curriculum: 12 weeks building with Claude

The full, illustrated version lives in the Claude doc "Path to Anthropic: 12-Week Curriculum." This file is the working copy the tutor commands read. If the two disagree, update this file.

**Assumptions:** about 20 hours a week. Primary target: Product Manager, Safeguards (Generalist). Secondary: Startup Partnerships, which shares most of the preparation. Also worth applying: Research PM, Labs, and Beneficial Deployments partnerships roles, if open. Applied AI Engineer is dropped as a target. Apply at the week 4 gate, not week 12.

**Context:** Anthropic's October 2026 report "How employment is changing at Anthropic" shows junior technical hiring falling sharply, go-to-market teams growing faster than technical ones, interviewers weighing AI tool use, judgment, autonomy, and customer and mission orientation more heavily, and "meta-work" (building skills, monitoring and reviewing agents) rising to 22% of sessions. The plan below is tuned to that.

**Edge:** Marc fought fraud at Tilt and Raisy, and turned FDA and FTC claims rules into product decisions at Jade Leaf. Policy, then detection, then intervention, then enforcement is work he has done. The plan makes it visible in an AI setting, and the fraud work is his lead interview story.

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

## Weeks 2–4: Build a safeguard

**Goal:** one polished public repo that works like a small Safeguards system: a written policy, detection, interventions and metrics, used by real operators. This is what he applies with.

**Build:** a claims safeguard for supplement and food brands. Reads a product page or label, flags risky claims under DSHEA and FTC rules, and chooses an intervention. It mirrors the Safeguards job at small scale: policy, detection, intervention, metrics.

**Design it before building it:**
- Policy spec: one page on what's allowed and what's risky, and why, with examples on both sides, written like a usage policy
- Harm categories with severity: disease claims, unsubstantiated structure and function claims, misleading testimonials, and so on
- Intervention ladder: allow, warn, suggest a rewrite, or block, and who sees each

- **Week 2, tool use and structured outputs:** tools, tool choice, parallel calls, tool errors; JSON schema outputs validated with Pydantic; vision and PDF input; v1 end to end
- **Week 3, production:** prompt caching (measure before and after); batch processing; rate limits, retries, cost per 1,000 reviews; retrieval versus long context, decided and justified in writing
- **Week 4, rigor and metrics:** apply the prompt engineering guide; hand-label 50+ real claims across every category, including borderline cases; report precision and recall by category; set thresholds using an explicit cost for each kind of error; measure blind spots with a held-out claim type the policy doesn't name; README as a case study (policy, design, metrics, tradeoffs, what failed)

**Gate (then apply):** repo public, two or more operators outside his companies have run it, README reports precision and recall by category and explains the threshold chosen.

**Tutor checks**
- Design the "check a claim" tool schema two ways; predict which the model calls more reliably; test both.
- Predict which of three prompt layouts gets cache hits; test; explain what breaks caching.
- Defend retrieval versus long context with a cost number.
- Write 10 adversarial claims designed to slip past the safeguard; fix what they expose.
- Sort 10 eval failures into categories before changing any prompt.
- A false positive costs a brand legitimate sales; a miss risks an FTC warning letter. Where does the threshold go, and how would he explain it to a policy lead in two sentences?

---

## Weeks 5–8: Flagship (agents, MCP, context, evals)

**Goal:** prove command of agent design, tool design, context management and evaluation.

**Build:** a CPG operator agent. An MCP server exposes Amazon SP-API and Shopify data as tools; an agent answers operator questions ("which SKUs are at stockout risk in 30 days, and why?") and drafts actions for human approval.

- **Week 5, agents:** "Building effective agents"; workflows versus agents; hand-written tool loop, then Claude Agent SDK; human approval on anything that writes
- **Week 6, MCP:** read the spec; build the server applying "Writing effective tools for agents"; test from Claude Code and the Claude app; installable in under 15 minutes
- **Week 7, context engineering:** read the context engineering post; memory, summarization, subagents; package one workflow as a skill; essay on the context-layer thesis
- **Week 8, evals:** 50–100 cases, code-graded where possible, model-graded where not; hand error analysis of 50 failures; compare two model tiers on quality versus cost; publish the write-up
- **Across weeks 5–8, agent orchestration:** run 2–3 agents in parallel on separate parts of the flagship, each in its own git worktree; write standing instructions and skills so agents stall less; log agent hours versus your hours weekly and publish the trend in the week 8 write-up; review agent output on a schedule rather than watching it work
- **Across weeks 5–8, red-team the agent:** it reads product listings, customer reviews and supplier emails, all text an attacker could control. Write a threat model; build 30+ prompt-injection and misuse attacks hidden in realistic data; add defenses (narrow tool permissions, human approval on writes, isolation of untrusted input, output checks); publish an injection-resistance eval with attack success and task success before and after, and what still gets through

**Gate:** a stranger installs it in under 15 minutes, three or more operators have used it, eval results are public, including injection resistance.

**Tutor checks**
- Without code, draw the agent loop including exactly where a human approves.
- For three founder use cases the tutor provides, argue workflow or agent.
- Rewrite a bad MCP tool description; measure tool-selection accuracy before and after.
- At step 20 of a long task, what stays in context and what gets summarized or dropped?
- Measure a model grader's agreement with his own labels on 20 cases.
- Which agent stalled waiting on him most this week, and what standing instruction or skill would have prevented it?
- One defense cuts attack success by 80% but also cuts legitimate task success by 30%. Ship it? Defend the numbers.

---

## Weeks 9–12: Capstone

**Goal:** do a small, real version of the Safeguards PM job, in public, and report on it as a member of that team would.

**Track A (main), a safeguards product spec:**
- Week 9: pick one real Anthropic surface and one risk (for example prompt injection against agents that use connectors, or sellers using Claude to generate illegal health claims at scale); write the threat model
- Week 10: design detections and interventions, using the week 2–8 builds as prototypes; define success metrics, blind-spot metrics, and the cost of each kind of error
- Week 11: write the eval plan and run a small version; review the spec with two people who have worked in trust and safety or fraud
- Week 12: publish a 3–5 page spec: problem, threat model, options with tradeoffs, MVP to ideal state, metrics, risks, what to test first

**Track B (light), a founder workshop:**
- One workshop for 6–10 founders on building with Claude safely: guardrails, evals, prompt injection
- A short field report on what founders get wrong about safety

**Tutor checks**
- Spec review: Claude plays a Safeguards engineering lead and asks what to cut to ship an MVP in six weeks.
- Policy review: Claude plays a policy lead and challenges the harm definitions and edge cases.
- Metrics review: how would he know the safeguard is failing silently?
- Workshop dry run: Claude plays a non-technical founder, a skeptical senior engineer, and an AI-native founder in a hurry.

---

## Parallel track: research and safety literacy (about 4 hours a week)

Each week: read, run `/explain-back` on the core claim, then publish a 500–800 word essay that survives a skeptical-researcher review.

| Week | Reading | Essay prompt |
| --- | --- | --- |
| 1 | Building safeguards for Claude; Anthropic's Usage Policy; How employment is changing at Anthropic | How a policy becomes detection: lessons from FTC claims rules and payment fraud |
| 2 | Responsible Scaling Policy; ASL-3 deployment safeguards report | What ASL-3 safeguards ask of a deployed product |
| 3 | Claude's constitution | Where model character ends and product safeguards begin |
| 4 | 3Blue1Brown neural network and transformer series | Explain a transformer to a CPG founder |
| 5 | Karpathy, Zero to Hero, through "Let's build GPT" (budget 8 hours) | What building a tiny model taught you about the big ones |
| 6 | Constitutional Classifiers, and the next-generation version | The real cost of a false positive: classifiers versus helpfulness |
| 7 | Anthropic threat intelligence reports, including the AI-orchestrated espionage case | What attackers actually do with AI, and what caught them |
| 8 | Agentic misalignment; prompt injection research | Guardrails for agents that act on untrusted data |
| 9 | Anthropic Economic Index; reread How employment is changing at Anthropic | Where AI use is growing, and where misuse risk concentrates |
| 10 | Current frontier model system card, safeguards sections | What a system card tells a builder, and what it doesn't |
| 11 | Introducing the Safeguards Research Team; US CAISI and UK AISI collaboration | How a lab works with outside red-teamers and governments |
| 12 | Recent Anthropic safeguards posts | Three emerging misuse risks, and the safeguard you would build for each |

---

## Milestone posts

| Week | Post |
| --- | --- |
| 1 | What I'm building over the next 12 weeks, and for whom |
| 4 | Launch: the claims safeguard, with precision and recall by category; plus a write-up of the AI tutor system as meta-work |
| 6 | Launch: the CPG operator MCP server |
| 8 | What evals caught that I would have missed |
| 10 | Red-teaming my own agent: what got through, and what stopped it |
| 12 | The safeguards spec, plus a retrospective |
