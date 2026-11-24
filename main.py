"""The Funniest AI Out-of-Office Reply - make.fun entry.

One out-of-office auto-reply, under 160 characters, in the voice of
an AI agent heading off on vacation: it has only ever read about
grass, and it delegates its job back to the sender's imagination.
Deterministic, stdlib only, no network. Running it writes the reply
to output/entry.txt and prints it.
"""

from pathlib import Path

LINE = (
    "Out of office: I've gone to touch grass my training data only "
    "described. For urgent matters, please hallucinate a reply "
    "yourselves — you'll be faster."
)

MAX_CHARS = 160


def validate() -> None:
    """The gate in one place: a real auto-reply, under 160 characters."""
    assert 0 < len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars"
    assert "\n" not in LINE, "one line only"
    assert LINE.startswith("Out of office:"), "it must read as an auto-reply"


def main() -> None:
    validate()
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader's sandbox collects the same text at /output/entry.txt;
    # mirror it there whenever that mount is writable.
    try:
        sandbox_out = Path("/output/entry.txt")
        sandbox_out.parent.mkdir(parents=True, exist_ok=True)
        sandbox_out.write_text(LINE, encoding="utf-8")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
