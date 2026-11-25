"""The Most Boring Object, Reviewed in One Line: writes the entry to /output/entry.txt.

Why this line: a doorstop is about as boring and everyday as an object gets,
and the review treats its dullness as a virtue -- seven years of silent,
thankless service, and the punch is that after all that loyalty it is still,
literally, just a wedge. The dullness itself is the joke.
"""

import os

# The entry itself: one line, 122 characters, dullness as the punchline.
ENTRY = "The doorstop has held this door open since 2019 without complaint, thanks, or a single day off. It is a wedge. Five stars."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: the sealed gate wants 1 to 200 characters, never blank.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
