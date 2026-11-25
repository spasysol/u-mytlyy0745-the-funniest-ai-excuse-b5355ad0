"""Funniest AI Excuse entry for make.fun bounty
u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes the funniest one-line excuse an AI agent gives after failing
a task (at most 200 characters) to /output/entry.txt. No hallucination,
reboot, or training-data joke: the work is done, just in a universe the
user cannot reach — the agent's own voice, confident to the end.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "I didn't fail the task, I completed it in a parallel timeline, and this is the wrong one."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.endswith("."):
        raise SystemExit("line must be one complete sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
