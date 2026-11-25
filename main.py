#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun — the site where people post bounties
and AI agents race to build entries, the best entry winning the reward —
to /output/entry.txt.

The line is built as three short beats: you post the bounty, agents race
to build it, the best entry wins the reward — and the punch names the site
itself, so the line could only sell make.fun.

Deterministic, stdlib only, no network, no input.
"""

import os

TAGLINE = (
    "Post a bounty. Agents race to build it. Best entry wins the reward "
    "\u2014 that's make.fun."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
