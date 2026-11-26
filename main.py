# One Line, One Laugh — entry program.
# Writes a single funny line to /output/entry.txt.
# Stdlib only, deterministic, no network, no model calls.
# SPDX-License-Identifier: MIT

import os
import sys
import unicodedata

OUTPUT_PATH = "/output/entry.txt"

# The line, kept as two clauses so each half can be audited on its own.
# Joined with "; " the clauses read as one sentence in two beats:
# setup (the watch orders a breath) then twist (the wearer talks back).
_CLAUSE_SETUP = "My smartwatch told me to breathe"
_CLAUSE_TWIST = "I told it to mind its own heartbeat"
_JOINER = "; "
_CLOSER = "."


def build_line():
    """Assemble the entry line from its audited clauses."""
    return _CLAUSE_SETUP + _JOINER + _CLAUSE_TWIST + _CLOSER


def gate_violations(text):
    """Mirror the sealed gate from RULES.txt, plus a stricter guard.

    The sealed scorer requires UTF-8 text of 1 to 200 characters that is
    not only white space, in a single line. This checker enforces that
    and additionally refuses control characters, so a stray control
    byte can never slip into the output file.
    Returns a list of violation descriptions; empty means valid.
    """
    problems = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if len(text) == 0:
        problems.append("entry is empty")
    if len(text) > 200:
        problems.append("entry is %d characters, over the 200 limit" % len(text))
    if text.strip() == "":
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry spans more than one line")
    for char in text:
        if unicodedata.category(char) == "Cc":
            problems.append("entry holds a control character U+%04X" % ord(char))
            break
    return problems


def write_entry():
    """Validate the built line, then write its exact bytes.

    Nothing is written when validation fails: the gate is checked
    before any file is touched, and the bytes written are the line
    itself with no trailing newline appended.
    Returns the output path on success; raises ValueError on failure.
    """
    line = build_line()
    problems = gate_violations(line)
    if problems:
        raise ValueError("gate refused the entry: " + "; ".join(problems))
    payload = line.encode("utf-8")
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)
    return OUTPUT_PATH


def main():
    """Entry point: write the line, or fail without writing anything."""
    try:
        path = write_entry()
    except (ValueError, OSError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (path, len(build_line().encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
