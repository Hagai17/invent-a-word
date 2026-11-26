#!/usr/bin/env python3
"""Invent a Word We Need — entry program (program/v1).

Writes the entry text to /output/entry.txt and prints it.
The entry coins one new English word and defines it in a single line.
"""

import os

WORD = "routelie"
PART_OF_SPEECH = "n."
DEFINITION = 'the "on my way" text sent from the sofa by someone who has not yet stood up.'

ENTRY = f"{WORD} ({PART_OF_SPEECH}): {DEFINITION}"

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text of 1 to 140 characters, not only
    white space. The entry is a single line by construction."""
    assert 1 <= len(text) <= 140, f"entry is {len(text)} characters"
    assert text.strip(), "entry is only white space"
    assert "\n" not in text, "entry must be one line"


def main() -> None:
    check_gate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as fh:
        assert fh.read() == ENTRY, "written entry does not round-trip"
    print(ENTRY)


if __name__ == "__main__":
    main()
