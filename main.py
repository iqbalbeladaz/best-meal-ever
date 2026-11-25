#!/usr/bin/env python3
"""Rendang in the Rain — entry program.

Writes one sentence about the best meal the entrant ever had to
/output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The meal: rendang at the narrator's grandmother's house in Jakarta,
eaten cross-legged on the floor as rain hammered the tin roof, nobody
speaking because the beef was too good to interrupt. Named dish, place,
texture and sound in one sentence; a memory that belongs to one person,
not a stock line; the ending image — a whole room silenced by good beef
— is the turn that stays with the reader.
"""

from pathlib import Path

ENTRY = (
    "The best meal I ever had was rendang at my grandmother's house "
    "in Jakarta, eaten cross-legged on the floor as rain hammered the "
    "tin roof and nobody spoke, the beef too good to interrupt.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
