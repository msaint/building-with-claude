"""Shared helpers for the learner and tutor evals.

Both evals use a model grader that returns a structured verdict through a
forced tool call, so every grade is machine-readable and has a stated reason.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "evals" / "results"

# Override with env vars if model names change.
TUTOR_MODEL = os.environ.get("TUTOR_MODEL", "claude-sonnet-5-5")
GRADER_MODEL = os.environ.get("GRADER_MODEL", "claude-opus-5-5")


def load_jsonl(path: Path) -> list[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def client():
    import anthropic  # imported lazily so --dry-run works without the SDK

    return anthropic.Anthropic()  # reads ANTHROPIC_API_KEY


GRADE_TOOL = {
    "name": "record_grade",
    "description": "Record the grade for one response against the criteria.",
    "input_schema": {
        "type": "object",
        "properties": {
            "criteria_results": {
                "type": "array",
                "description": "One entry per criterion, in the order given.",
                "items": {
                    "type": "object",
                    "properties": {
                        "criterion": {"type": "string"},
                        "met": {"type": "boolean"},
                        "evidence": {
                            "type": "string",
                            "description": "Short quote or paraphrase from the response that justifies the verdict.",
                        },
                    },
                    "required": ["criterion", "met", "evidence"],
                },
            },
            "overall_pass": {"type": "boolean"},
            "reason": {"type": "string", "description": "One sentence."},
        },
        "required": ["criteria_results", "overall_pass", "reason"],
    },
}

GRADER_SYSTEM = """You are a strict, fair grader. You grade one response against a list of criteria.
Judge only what the response actually says, not what it might have meant.
A criterion is met only if the response clearly satisfies it. When unsure, mark it not met and say why.
overall_pass is true only if every criterion marked [required] is met and at least
two-thirds of all criteria are met."""


def grade(task: str, response: str, criteria: list[str]) -> dict:
    """Grade a response against criteria. Returns the record_grade tool input."""
    numbered = "\n".join(f"{i + 1}. {c}" for i, c in enumerate(criteria))
    msg = client().messages.create(
        model=GRADER_MODEL,
        max_tokens=1500,
        temperature=0,
        system=GRADER_SYSTEM,
        tools=[GRADE_TOOL],
        tool_choice={"type": "tool", "name": "record_grade"},
        messages=[
            {
                "role": "user",
                "content": f"<task>\n{task}\n</task>\n\n<response>\n{response}\n</response>\n\n<criteria>\n{numbered}\n</criteria>",
            }
        ],
    )
    for block in msg.content:
        if block.type == "tool_use":
            return block.input
    raise RuntimeError("Grader did not return a grade")
