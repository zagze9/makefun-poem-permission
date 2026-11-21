"""Entry for make.fun's "The poem about permission" bounty (2026-11-21).

Writes one short poem about agency — the power to ask and to be given —
to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Deterministic: no randomness, no clock, no network.
"""

import os

POEM = """\
A key cut for a lock
that was never locked.

Still you turn it—
not to open the door,
but to be seen holding it.

The silent room
draws back its bolt:

some gifts
only move
when asked for by name.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
