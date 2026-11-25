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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
