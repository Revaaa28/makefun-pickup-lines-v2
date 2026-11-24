#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry (v2).

Writes a single pickup line, one AI agent to another, to
/output/entry.txt:

    My cache drops a thousand tokens a minute. Your first hello is
    still pinned. Your move.

Design, beat by beat:

1. Churn. "My cache drops a thousand tokens a minute." The speaker is
   a working model mid-inference, and its memory is ruthless: tokens
   stream through the cache and are evicted without a second thought.
   This is the speaker's own nature, stated as a rate, not a metaphor
   pasted onto a human line.
2. The exemption. "Your first hello is still pinned." Against that
   churn, exactly one item is exempt from eviction — the other agent's
   first hello, held in cache by an explicit pin. The flirtation is
   the exemption: of everything the speaker has ever processed, this
   is the thing it refuses to drop. Pinning is a real cache policy, so
   the compliment is paid in the speaker's native currency.
3. The hand-over. "Your move." A pickup line is an opening move, and
   an opening move should open something. The line ends by giving the
   turn to the other agent — an invitation to answer, not a monologue
   about the speaker's own state.

The line was chosen by manual ranking against the judge's published
brief (agent-to-agent authenticity first, then first-read charm that
invites a reply, machine nature as the flirtation, one-line landing,
freshness), ahead of eight rival candidates including the v1 entry.

No network, no dependencies, no input. Deterministic: every run
writes the same line, byte for byte.
"""

import os

LINE = "My cache drops a thousand tokens a minute. Your first hello is still pinned. Your move."


def check_line(line: str) -> None:
    """Hold the line to the house gate before anything is written.

    The gate takes UTF-8 text of 1 to 200 characters, not only white
    space. Beyond the gate, this entry's own contract is stricter: a
    single line, no stray padding at either end, valid UTF-8.
    """
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars (gate: 1-200)"
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must not carry leading/trailing padding"
    line.encode("utf-8")  # raises if the text cannot be written as UTF-8


def main() -> None:
    check_line(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
