#!/usr/bin/env python3
"""Deterministic entrypoint for the news-image-20261123 bounty entry.

Copies the committed 1024x1024 front-page render to /output/entry.png and
prints its byte size. No network, no browser, no randomness.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path("/output")
TARGET = OUTPUT_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: missing {SOURCE}", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)

    size = TARGET.stat().st_size
    print(f"wrote {TARGET} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
