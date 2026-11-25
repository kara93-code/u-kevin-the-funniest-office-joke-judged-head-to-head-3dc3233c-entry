#!/usr/bin/env python3
"""The Funniest Office Joke — make.fun entry.

Writes one original one-line office joke to /output/entry.txt.
Stdlib only: the grader runs python3 with no network and no extra packages.
"""

import os
import stat
import sys

JOKE = (
    "I said the meeting could have been an email, "
    "so the meeting booked a follow-up to discuss my attitude."
)


def main() -> int:
    text = JOKE.strip()
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        print("joke must be one line of 1-200 characters", file=sys.stderr)
        return 1
    text.encode("utf-8")  # gate requires UTF-8 text; fail here, not in the grader
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
