#!/usr/bin/env python3
"""Validate canonical Home Assistant TMX exports without flagging key references.

Lokalise key references (`[%key:…%]`) are source-side indirections. A Swedish
translation may deliberately contain expanded contextual text, so key references
must not be compared as runtime placeholders.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as etree
from pathlib import Path

RUNTIME_PLACEHOLDER = re.compile(
    r"\{[^{}]+\}|%\d*\$?[+#0\- ]*\d*(?:\.\d+)?[a-zA-Z]"
)
KEY_REFERENCE = re.compile(r"\[%(?:key|link):[^%]+%\]")


def text(tuv: etree.Element) -> str:
    segment = tuv.find("seg")
    return "" if segment is None else "".join(segment.itertext())


def validate(path: Path) -> list[str]:
    root = etree.parse(path).getroot()
    seen: set[str] = set()
    issues: list[str] = []
    for unit in root.findall(".//tu"):
        key = unit.get("tuid", "")
        translations = {
            tuv.get("{http://www.w3.org/XML/1998/namespace}lang"): text(tuv)
            for tuv in unit.findall("tuv")
        }
        if not key or key in seen:
            issues.append(f"{path}: duplicate or missing tuid: {key!r}")
        seen.add(key)
        if not translations.get("en") or translations.get("sv") is None:
            issues.append(f"{path}: incomplete language pair: {key}")
            continue
        source_text = KEY_REFERENCE.sub("", translations["en"])
        target_text = KEY_REFERENCE.sub("", translations["sv"])
        source = sorted(RUNTIME_PLACEHOLDER.findall(source_text))
        target = sorted(RUNTIME_PLACEHOLDER.findall(target_text))
        if source != target:
            issues.append(f"{path}: runtime-placeholder mismatch: {key}")
    print(f"{path.name}: {len(seen)} entries, {len(issues)} issue(s)")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", type=Path)
    arguments = parser.parse_args()
    issues = [issue for path in arguments.files for issue in validate(path)]
    print(*issues, sep="\n")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
