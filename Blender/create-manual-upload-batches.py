#!/usr/bin/env python3
"""Split the reviewed Blender Manual delta catalog into Weblate-safe PO files."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_GLOB = "blender-manual-sv-review-batch-20261104-*.po"
OUTPUT = ROOT / "upload-candidates" / "2026-11-04"
COMBINED = OUTPUT / "blender-manual-sv-reviewed-all.po"
LIMIT = 100


def main() -> None:
    sources = sorted(ROOT.glob(SOURCE_GLOB))
    if not sources:
        raise SystemExit("No reviewed Blender Manual delta files found.")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["msgcat", "--use-first", "--no-location", "-o", str(COMBINED), *map(str, sources)],
        check=True,
    )
    blocks = COMBINED.read_text(encoding="utf-8").split("\n\n")
    header, entries = blocks[0], [block for block in blocks[1:] if block.strip()]
    for index, start in enumerate(range(0, len(entries), LIMIT), start=1):
        candidate = OUTPUT / f"blender-manual-sv-reviewed-{index:02d}.po"
        content = "\n\n".join(entries[start : start + LIMIT]).rstrip("\n")
        candidate.write_text(f"{header}\n\n{content}\n", encoding="utf-8")
        subprocess.run(["msgfmt", "--check", "-o", "/dev/null", str(candidate)], check=True)

    print(f"{len(entries)} entries split into {(len(entries) + LIMIT - 1) // LIMIT} files.")


if __name__ == "__main__":
    main()
