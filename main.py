"""One Emoji, One Dream Vacation — entry generator.

Writes the chosen single emoji to /output/entry.txt, deterministically,
with no network access.

Chosen emoji: U+1F334 PALM TREE (4 bytes UTF-8, 1 character).
Why this one — see candidates.md for the full tournament:
  * Won the internal pairwise tournament (QF 0.80 vs airplane departure,
    SF 0.75 vs canoe) with all four calls agreeing — the most
    order-robust pick of the eight candidates.
  * Plainly names a dream vacation at a glance (judge criterion 1+2):
    a tropical beach postcard, readable on any screen at any size.
  * One code point, 4 bytes: the smallest possible entry, winning the
    size tie-break against 7-byte picks such as the desert island.
  * Uncrowded: no palm-tree entry appears in the field's 711 submissions,
    unlike the desert island and Mount Fuji, which are copied dozens of
    times (byte-identical entries share one rate; the late receipt loses).
"""

import os

# The entry: exactly one emoji. Written as an escape so the source file
# is unambiguous and byte-exact regardless of editor encoding.
EMOJI = "\U0001F334"  # U+1F334 PALM TREE


def build_entry():
    """Return the entry text: exactly one emoji, nothing else."""
    return EMOJI


def write_entry(out_dir="/output"):
    """Write the entry to <out_dir>/entry.txt.

    Creates the output directory recursively. The file is left world
    readable (mode 0644): the grader collects outputs as a different
    user, so a 0600 file would fail with "<path> is not readable".
    """
    os.makedirs(out_dir, exist_ok=True)
    text = build_entry()
    # Gate self-check (house gate: UTF-8 text of 1 to 8 characters,
    # not only white space). Fail loudly here rather than ship an
    # entry the sealed scorer would refuse.
    assert 1 <= len(text) <= 8 and text.strip(), "entry fails the gate"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    write_entry()
