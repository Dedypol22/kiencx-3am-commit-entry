"""One-line commit message for The 3AM Commit Message bounty.

The joke: an AI coding agent has spent the whole night fixing its own
bugs, and every fix only creates the next bug. At 3am it commits a line
admitting the chain out loud: the bug it just fixed was introduced by
its own 2am fix, which was itself a fix for the 1am bug. The agent is
its own worst enemy, on a schedule, one hour at a time.

Winner of 12 candidates scored against the judge brief (reads as a real
3am commit line first, laugh on first read, fresh, hurried voice, tight
use of characters): the hour-by-hour self-sabotage chain beat the
"deleted everything" family, the "it works, don't know why" recycled
joke, and the clever-but-slow puns.
"""

import os

# Winning line: 73 characters (verified by exact count).
LINE = "wip: 3am, fixed the bug I introduced at 2am while fixing the bug from 1am"


def output_dir():
    """Return the directory entry.txt must be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE + "\n", "entry.txt does not match LINE"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
