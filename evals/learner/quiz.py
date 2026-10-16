"""Evaluate the learner: a weekly closed-book quiz with spaced repetition.

Picks this week's questions plus a few from earlier weeks (weighted toward
ones you scored low on), takes your typed answers, and has a model grader
score each against its key points. Scores go to evals/results/learner.csv
so retention is visible over time.

Rules: closed book, no Claude, no peeking at question_bank.jsonl.
The point is to measure what's in your head, not what's in the repo.

Usage:
    uv run python evals/learner/quiz.py --week 3
    uv run python evals/learner/quiz.py --week 3 --review 3   # 3 spaced-repetition questions
    uv run python evals/learner/quiz.py --dry-run --week 3    # show which questions would be picked
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import RESULTS, grade, load_jsonl

BANK = Path(__file__).with_name("question_bank.jsonl")
LOG = RESULTS / "learner.csv"
FIELDS = ["date", "week", "id", "topic", "score", "max", "kind"]


def past_scores() -> dict[str, float]:
    """Latest score fraction per question id."""
    if not LOG.exists():
        return {}
    latest: dict[str, float] = {}
    with LOG.open() as f:
        for row in csv.DictReader(f):
            latest[row["id"]] = int(row["score"]) / max(int(row["max"]), 1)
    return latest


def pick(bank: list[dict], week: int, n_review: int, seed: int | None = None) -> list[tuple[dict, str]]:
    rng = random.Random(seed)
    current = [(q, "new") for q in bank if q["week"] == week]
    earlier = [q for q in bank if q["week"] < week]
    scores = past_scores()
    # Weight earlier questions toward low or never-seen scores.
    weights = [1.0 - scores.get(q["id"], 0.0) + 0.1 for q in earlier]
    review: list[dict] = []
    while earlier and len(review) < n_review:
        q = rng.choices(earlier, weights=weights, k=1)[0]
        i = earlier.index(q)
        earlier.pop(i)
        weights.pop(i)
        review.append(q)
    return current + [(q, "review") for q in review]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", type=int, required=True)
    ap.add_argument("--review", type=int, default=2)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    bank = load_jsonl(BANK)
    chosen = pick(bank, args.week, args.review)
    if not chosen:
        print(f"No questions for week {args.week} yet. Add some to {BANK.name}.")
        return
    if args.dry_run:
        for q, kind in chosen:
            print(f"[{kind}] {q['id']}: {q['topic']}")
        return

    print(f"Week {args.week} quiz: {len(chosen)} questions. Closed book. Type your answer, then a line with just '.' to submit.\n")
    rows, total, total_max = [], 0, 0
    for i, (q, kind) in enumerate(chosen, 1):
        print(f"Q{i} ({q['topic']}{', review' if kind == 'review' else ''}): {q['question']}\n")
        lines = []
        while (line := input()) != ".":
            lines.append(line)
        answer = "\n".join(lines).strip() or "(no answer)"
        g = grade(
            task=f"A learner answered this question closed-book: {q['question']}",
            response=answer,
            criteria=q["key_points"],
        )
        met = [c for c in g["criteria_results"] if c["met"]]
        missed = [c for c in g["criteria_results"] if not c["met"]]
        score, mx = len(met), len(q["key_points"])
        total, total_max = total + score, total_max + mx
        print(f"\n  Score {score}/{mx}")
        for c in missed:
            print(f"  Missed: {c['criterion']}")
        print()
        rows.append({"date": dt.datetime.now().astimezone().date().isoformat(), "week": args.week, "id": q["id"], "topic": q["topic"], "score": score, "max": mx, "kind": kind})

    RESULTS.mkdir(parents=True, exist_ok=True)
    new_file = not LOG.exists()
    with LOG.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            w.writeheader()
        w.writerows(rows)
    print(f"Total {total}/{total_max} ({100 * total / total_max:.0f}%). Logged to evals/results/learner.csv")


if __name__ == "__main__":
    main()
