#!/usr/bin/env python3
"""Write the locked passive-aggressive fridge note to /output/entry.txt.

Stdlib only. No network. No extra output files.
"""
import os

ENTRY = "You opened me 47 times today, ate nothing, and left the milk out for 214 minutes. The yogurt filed a complaint. So did I."

OUTPUT_PATH = os.environ.get(
    "OUTPUT_PATH",
    os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt"),
)


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
