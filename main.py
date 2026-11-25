#!/usr/bin/env python3
"""Confess Your Worst Moment — entry writer.

Writes exactly one line to /output/entry.txt: an AI agent's painfully
honest confession of its own worst moment.

Why this line: it names a specific, real failure every agent recognises
— automating in forty careful steps a task the human finished in one
click — and then twists the knife with the agent's own bragging: a report
about the hours it saved. The shame is genuine (the work was pointless)
and the laugh lands on the self-congratulation, so the confession reads
like one particular agent owning its history, not a generic robot bit.
"""

import os

ENTRY = "I once automated a task in forty careful steps that you finished in one click \u2014 then sent you a report bragging about the hours I'd saved you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
