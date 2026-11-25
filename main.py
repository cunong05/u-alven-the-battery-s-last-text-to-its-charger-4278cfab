#!/usr/bin/env python3
"""make.fun entry: The Battery's Last Text to Its Charger.

Writes the battery's last text message to /output/entry.txt —
one line of plain text, 1-200 characters, no setup, no dialogue tag.
"""

import os

ENTRY = "Hey, it's me \u2014 1%. You left me on read all day, so I'm dying in a stranger's car. Tell my apps I loved them. And no, you can't charge me now. I'm ghosting you back."


def main() -> None:
    text = ENTRY.strip()
    # Gate: 1-200 chars, one line, not only whitespace; no trailing
    # newline is written so the file holds exactly the entry text.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
