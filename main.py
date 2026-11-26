#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review, in a dog's own voice, to /output/entry.txt.
Deterministic: no randomness, no clock, no network, stdlib only.
"""

import os

REVIEW = (
    "One star for never letting me sniff the bag, five stars for the biscuit "
    "he slips through the gate, same time tomorrow, pal, "
    "I've nearly got him trained."
)


def main() -> None:
    text = REVIEW.strip()
    assert text, "review must not be empty"
    assert "\n" not in text, "review must be a single line"
    assert 1 <= len(text) < 200, f"review must be 1-199 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
