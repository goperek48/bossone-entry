#!/usr/bin/env python3
"""One Word for the Boss — probe entry.

The entry is one word and nothing else. No phrase, no caption, no
explanation: the word must carry the joke by itself, so this program
keeps it simple and writes the chosen word, exactly as it stands,
to /output/entry.txt.

The pick: some bosses answer a yes-or-no question by booking a meeting
about it, then a follow-up about the meeting, then a recurring slot to
track the follow-ups. "Meetingizer" bottles that boss into a single
coined word — it gets a laugh because everyone recognises the type at
once, it rings true because the type is everywhere, and it feels new
because nobody's first instinct is to reach for it.
"""

import os
import sys

# The entry itself: a single word, eleven letters, no spaces or punctuation.
WORD = "Meetingizer"

# Where the harness looks for the entry.
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Write the word to /output/entry.txt, exactly as chosen."""
    # Refuse to write anything that is not one short word: the gate
    # accepts 1-30 characters, and a string holding a space or a
    # line break would not be a word in the first place.
    if not WORD or len(WORD) > 30 or any(ch.isspace() for ch in WORD):
        print("entry is not a single word of 1-30 characters", file=sys.stderr)
        return 1

    # Make sure the output folder exists before writing into it.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # No trailing newline: the file should contain the word alone,
    # so the judge reads exactly what was entered and nothing more.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
