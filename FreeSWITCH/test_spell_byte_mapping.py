#!/usr/bin/env python3
"""Model mod_say_sv's current byte-wise say_spell lookup for known encodings."""
import json
import locale
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).with_name("spell-byte-mapping-audit.json")
OUT = Path(__file__).with_name("spell-byte-mapping-runtime-model.json")


def c_bytewise_ids(data: bytes) -> list[int]:
    """Model int a = tolower((int)*p), using unsigned input bytes.

    The C implementation's signed-char conversion is undefined for negative
    high-bit values, so report this model as deterministic path arithmetic only.
    """
    return [byte + 32 if 65 <= byte <= 90 else byte for byte in data]


def main() -> None:
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    examples = []
    for char in ("ä", "å", "ö"):
        utf8 = char.encode("utf-8")
        cp437 = char.encode("cp437")
        utf8_ids = c_bytewise_ids(utf8)
        cp437_ids = c_bytewise_ids(cp437)
        examples.append({
            "character": char,
            "utf8_bytes_hex": utf8.hex(" ").upper(),
            "utf8_modeled_lookup_ids": utf8_ids,
            "utf8_modeled_paths": [f"ascii/{value}.wav" for value in utf8_ids],
            "cp437_byte_hex": cp437.hex(" ").upper(),
            "cp437_modeled_lookup_ids": cp437_ids,
            "cp437_modeled_paths": [f"ascii/{value}.wav" for value in cp437_ids],
            "expected_legacy_resource": f"ascii/{ord(char.encode('cp437'))}.wav",
        })

    output = {
        "status": "MODEL_ONLY_CALLER_ENCODING_UNVERIFIED",
        "source_commit": audit["source_commit"],
        "model": "Unsigned byte values; ASCII lowercase conversion only, matching the defined C tolower result when char is unsigned.",
        "limitation": "This does not run FreeSWITCH, observe the actual caller encoding, or model undefined behavior from signed high-bit char passed to tolower.",
        "c_locale": locale.setlocale(locale.LC_CTYPE, None),
        "examples": examples,
    }
    OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
