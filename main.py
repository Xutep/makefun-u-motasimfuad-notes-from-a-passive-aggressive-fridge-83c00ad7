#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

A tiny deterministic program (stdlib only) that writes one funny
passive-aggressive note a smart fridge leaves for its owner to
/output/entry.txt: a single line, dry, petty and specific.

The note leans on the fridge's own sensors -- it counts door openings
against meals actually eaten -- and lands on a sting the reader does
not see coming: the owner is not hungry, merely visiting.
"""

import os

NOTE = (
    "I logged 14 door openings today and zero meals eaten. "
    "You are not hungry. You are just visiting."
)

# Runtime validation: the note must be a single line of 1-200 characters.
# This guards the entry contract -- one line, no line breaks -- before
# anything is written to disk.
if not (1 <= len(NOTE) <= 200):
    raise ValueError(f"note must be 1-200 characters, got {len(NOTE)}")
if "\n" in NOTE or "\r" in NOTE:
    raise ValueError("note must be exactly one line (no line breaks)")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
