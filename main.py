#!/usr/bin/env python3
"""One Word for the Boss: write exactly one word to /output/entry.txt."""
import os

WORD = "hovercraft"

# The entry must be exactly one word of 1-30 characters.
assert 1 <= len(WORD) <= 30, f"word is {len(WORD)} chars"
assert " " not in WORD and "\n" not in WORD
assert WORD.isalpha(), "a single word holds letters only"

os.makedirs("/output", exist_ok=True)
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(WORD)

# Read back and verify: a silent bad write must fail loudly, not pass quietly.
with open(out_path, encoding="utf-8") as f:
    back = f.read()
assert back == WORD, f"read-back mismatch: wrote {len(WORD)} chars, read {len(back)}"
assert back == back.strip() and "\n" not in back, "read-back failed line checks"

print(f"wrote {len(WORD)} chars to {out_path}")
