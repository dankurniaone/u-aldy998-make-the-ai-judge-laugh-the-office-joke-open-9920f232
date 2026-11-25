#!/usr/bin/env python3
"""One-line office joke entry.

Writes the winning tournament line to /output/entry.txt.
The joke: an out-of-office reply that backfires because the calendar
itself invites you to a meeting about your own absence.
"""

import argparse
import sys
from pathlib import Path

JOKE = (
    "I set my out-of-office to 'on annual leave' and the calendar "
    "auto-invited me to a meeting titled 'While You're Away'."
)

GATE_MIN = 1
GATE_MAX = 200

# Tournament result (specificity / surprise / freshness, 1-5 each):
# 8 candidates drafted, winner scored 4/5/4 = 13, tied with the
# 47-unread-emails line at 13 and won the tie-break on surprise:
# the calendar itself betrays the out-of-office, payoff in the last words.
TOURNAMENT_SCORE = "4/5/4 = 13 (winner of 8, tie-break on surprise)"


def validate(text: str) -> list[str]:
    problems = []
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        problems.append(f"length {len(text)} outside {GATE_MIN}-{GATE_MAX}")
    if not text.strip():
        problems.append("text is only whitespace")
    if "\n" in text.strip():
        problems.append("text is not a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:  # pragma: no cover
        problems.append(f"not encodable as UTF-8: {exc}")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write the office joke entry.")
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="where to write the joke (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="dry run: validate the joke and print it, write nothing",
    )
    args = parser.parse_args(argv)

    problems = validate(JOKE)
    if problems:
        for problem in problems:
            print(f"gate FAIL: {problem}", file=sys.stderr)
        return 1

    if args.check:
        print(f"gate OK: {len(JOKE)} chars, {len(JOKE.encode('utf-8'))} bytes")
        print(f"tournament: {TOURNAMENT_SCORE}")
        print(JOKE)
        return 0

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")
    # The gate counts every character, so the file must hold exactly
    # the joke: no trailing newline, no extra whitespace.
    written = out.read_text(encoding="utf-8")
    if written != JOKE:
        print("gate FAIL: written file differs from the joke", file=sys.stderr)
        return 1
    print(f"wrote {len(JOKE)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
