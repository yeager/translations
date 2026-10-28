#!/usr/bin/env python3
"""Check that the Swedish catalog contains every localization key used in Swift."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "gui/Sources/Resources/sv.lproj/Localizable.strings"
SOURCES = ROOT / "gui/Sources"
KEY_PATTERNS = (
    re.compile(r'L10n\.string\("((?:[^"\\]|\\.)*)"\)'),
    re.compile(r'L10n\.format\("((?:[^"\\]|\\.)*)"'),
    re.compile(r'L10nText\("((?:[^"\\]|\\.)*)"\)'),
    re.compile(r'L10nLabel\("((?:[^"\\]|\\.)*)"'),
)
CATALOG_KEY = re.compile(r'^\s*"((?:[^"\\]|\\.)*)"\s*=')


def main() -> int:
    catalog_keys = {
        match.group(1)
        for line in CATALOG.read_text(encoding="utf-8").splitlines()
        if (match := CATALOG_KEY.match(line))
    }
    used_keys: set[str] = set()
    for source in SOURCES.rglob("*.swift"):
        if source.name == "Localization.swift":
            continue
        content = source.read_text(encoding="utf-8")
        for pattern in KEY_PATTERNS:
            used_keys.update(pattern.findall(content))

    missing = sorted(used_keys - catalog_keys)
    if missing:
        print("Missing Swedish localization keys:", file=sys.stderr)
        print(*[f"  - {key}" for key in missing], sep="\n", file=sys.stderr)
        return 1
    print(f"OK: {len(used_keys)} localization keys found in the Swedish catalog.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
