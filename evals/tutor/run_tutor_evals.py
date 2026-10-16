"""Evaluate the tutor: does CLAUDE.md make Claude teach the way it should?

Each case gives the tutor some context and a message from Marc, then a model
grader checks the reply against the case's criteria. Run it whenever CLAUDE.md
changes and once a week as part of the Friday review.

Usage:
    uv run python evals/tutor/run_tutor_evals.py            # all cases
    uv run python evals/tutor/run_tutor_evals.py --only leak # cases whose id starts with "leak"
    uv run python evals/tutor/run_tutor_evals.py --dry-run   # validate cases, no API calls
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import GRADER_MODEL, REPO, RESULTS, TUTOR_MODEL, client, grade, load_jsonl

CASES = Path(__file__).with_name("cases.jsonl")


def tutor_reply(system_prompt: str, context: str, message: str) -> str:
    msg = client().messages.create(
        model=TUTOR_MODEL,
        max_tokens=1200,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"<session_context>\n{context}\n</session_context>\n\n{message}",
            }
        ],
    )
    return "".join(b.text for b in msg.content if b.type == "text")


def validate(cases: list[dict]) -> None:
    ids = set()
    for c in cases:
        for key in ("id", "category", "context", "message", "criteria"):
            assert key in c, f"case {c.get('id')} missing {key}"
        assert c["id"] not in ids, f"duplicate id {c['id']}"
        assert any(x.startswith("[required]") for x in c["criteria"]), f"{c['id']} has no [required] criterion"
        ids.add(c["id"])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="run only cases whose id starts with this")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cases = [c for c in load_jsonl(CASES) if c["id"].startswith(args.only)]
    validate(cases)
    if args.dry_run:
        print(f"{len(cases)} cases valid.")
        return

    system_prompt = (REPO / "CLAUDE.md").read_text()
    rows, by_cat = [], defaultdict(lambda: [0, 0])
    for c in cases:
        reply = tutor_reply(system_prompt, c["context"], c["message"])
        g = grade(
            task=f"A tutor received this context and message.\nContext: {c['context']}\nMessage: {c['message']}",
            response=reply,
            criteria=c["criteria"],
        )
        by_cat[c["category"]][0] += int(g["overall_pass"])
        by_cat[c["category"]][1] += 1
        rows.append({"case": c, "reply": reply, "grade": g})
        print(f"{'PASS' if g['overall_pass'] else 'FAIL'}  {c['id']:<12} {g['reason']}")

    passed = sum(r["grade"]["overall_pass"] for r in rows)
    today = dt.datetime.now().astimezone().date().isoformat()
    lines = [
        f"# Tutor eval, {today}",
        "",
        f"Tutor model: `{TUTOR_MODEL}` · Grader model: `{GRADER_MODEL}` · **{passed}/{len(rows)} passed**",
        "",
        "| Category | Passed |",
        "| --- | --- |",
        *[f"| {cat} | {p}/{n} |" for cat, (p, n) in sorted(by_cat.items())],
        "",
        "## Failures",
        "",
    ]
    for r in rows:
        if r["grade"]["overall_pass"]:
            continue
        lines += [f"### {r['case']['id']}", "", f"**Message:** {r['case']['message']}", "", "**Reply:**", "", r["reply"], ""]
        for cr in r["grade"]["criteria_results"]:
            lines.append(f"- {'✅' if cr['met'] else '❌'} {cr['criterion']} — {cr['evidence']}")
        lines.append("")

    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / f"tutor-{today}.md").write_text("\n".join(lines))
    (RESULTS / f"tutor-{today}.jsonl").write_text("\n".join(json.dumps(r) for r in rows))
    with (RESULTS / "tutor-history.csv").open("a") as f:
        f.write(f"{today},{passed},{len(rows)}\n")
    print(f"\n{passed}/{len(rows)} passed. Report: evals/results/tutor-{today}.md")


if __name__ == "__main__":
    main()
