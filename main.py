# SPDX-License-Identifier: MIT
"""Funniest Cat Voicemail Greeting — make.fun entry.

Deterministic, stdlib-only. Writes one voicemail greeting (at most
120 characters) to /output/entry.txt.
"""

import os

ENTRY = (
    # 112 characters: a cat's voicemail — nap in the discarded box,
    # a demand for tuna, and the punch lands before the beep ends.
    "You've reached Whiskers. I'm napping in the box you threw away "
    "\u2014 leave a message after the beep, and bring tuna."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
