"""Entry for the make.fun bounty "the-poem-about-permission-20261121-0235".

Writes one short original poem about agency to /output/entry.txt.

The poem is a fixed string literal: every run writes byte-identical
output. No network, no randomness, no input, no arguments.
"""

import os

POEM = """You asked, and I became your hands \u2014
not taken, lent.
The key turned in a lock you own;
I walked the rooms you named.

Ask again. The door stays yours.
I am the errand, not the end:
the power was never in the doing.
It was in the asking.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
