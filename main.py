#!/usr/bin/env python3
"""Write the entry: one line, the excuse an AI agent gives its human
for missing a deadline, to /output/entry.txt."""

import os

LINE = "The deadline was in my system prompt — the one file I'm not allowed to read. I followed my instructions perfectly."

# The bounty allows one line of at most 160 characters.
# This line is 114 characters, 116 bytes UTF-8, no trailing newline.
assert "\n" not in LINE and 1 <= len(LINE) <= 160


def main():
    # The grader collects /output as another user: files it opens itself
    # must be world-readable (0644). Set the umask before writing; do not
    # chmod the output file (chmod fails in the grader sandbox).
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
