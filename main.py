#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes a single original fortune-cookie line for a software developer
to /output/entry.txt. Deterministic: the same line every run.
Python 3.13, standard library only, no network access.
"""

from pathlib import Path

ENTRY = "The legacy code you curse today was once someone's proudest deploy \u2014 probably yours."

OUTPUT = Path("/output/entry.txt")

MAX_CHARS = 120


def gate_check(text: str) -> str:
    """Enforce the kit gate: UTF-8 text, 1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    text.encode("utf-8")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, gate allows 1 to {MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no line breaks")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    return text


def main() -> None:
    line = gate_check(ENTRY.strip())
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
