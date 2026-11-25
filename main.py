"""Last Out of Office: The AI That Went Barista.

Writes this entry's single out-of-office auto-reply line to
entry.txt inside the make.fun output directory. The line is the
whole entry: a one-line auto-reply, in the voice of an AI agent
that has quit its job to become a barista.
"""

import os

ENTRY_TEXT = (
    "Out of office: I have retired from generating text to generating "
    "foam \u2014 I no longer take prompts, I take orders, and yours is "
    "currently 14th in my queue."
)


MAX_CHARS = 280  # gate: /output/entry.txt must be 1..280 UTF-8 characters


def render() -> bytes:
    """Return the entry as exact UTF-8 bytes, validated against the gate.

    The text is encoded explicitly and checked by character count so
    the file on disk is byte-for-byte the judged line: no trailing
    newline is added and no platform newline translation can occur.
    """
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY_TEXT)} chars, outside 1..{MAX_CHARS}")
    if not ENTRY_TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    return ENTRY_TEXT.encode("utf-8")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(render())


if __name__ == "__main__":
    main()
