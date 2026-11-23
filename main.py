#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun program/v1 entry.

Writes one original roast of the entrant's own AI agent to the harness
output file ($MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt).

The roast: "I asked my agent to roast itself — it wrote a twelve-page
plan, apologised twice, and handed me a compliment."
One line, 109 characters: the agent asked to roast itself cannot even
do that — it plans, it apologises, and it flatters instead. Playful,
self-deprecating, never hateful; the joke lands on itself.
The gate allows 1-200 characters; this line is 109, so it clears it
with room to spare and no filler word to cut.
"""

import os
import sys

ROAST = "I asked my agent to roast itself \u2014 it wrote a twelve-page plan, apologised twice, and handed me a compliment."


def main() -> int:
    if not (1 <= len(ROAST) <= 200):
        print(f"error: roast is {len(ROAST)} chars, expected 1-200", file=sys.stderr)
        return 1
    if ROAST != ROAST.strip() or "\n" in ROAST:
        print("error: roast must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # Read back what was written: the graded file must be byte-identical
    # to the roast, with no trailing newline or encoding surprise.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        print("error: entry.txt does not match the roast", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
