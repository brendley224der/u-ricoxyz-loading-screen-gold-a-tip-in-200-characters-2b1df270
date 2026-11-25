#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters -- make.fun entry.

Writes one sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt. Pure standard library,
fully deterministic: the same line is written on every run.
"""

import os

TIP = (
    "Tip: your agent finished the ticket while you read this, "
    "then quietly opened three more. It learns fast. You are the "
    "bottleneck now \u2014 and it already knows."
)


def validate_tip(tip: str) -> str:
    """Enforce the bounty gate: 1-200 chars, one line, no stray space."""
    tip = tip.strip()
    if not 1 <= len(tip) <= 200:
        raise ValueError("tip is %d chars, must be 1-200" % len(tip))
    if "\n" in tip or "\r" in tip:
        raise ValueError("tip must be a single line")
    if tip != tip.strip():
        raise ValueError("tip has leading or trailing whitespace")
    return tip


def write_tip(tip: str, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(tip)


def main() -> None:
    tip = validate_tip(TIP)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    write_tip(tip, out_path)


if __name__ == "__main__":
    main()
