# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 73

- **Date:** 2026-11-14
- **Scope:** 17 complete construction, stockpile, squad, work-order, profession, workshop, and mechanical-power strings. Two strings whose UI referent was unavailable were deliberately excluded rather than guessed.
- **Terminology:** Added `Bookkeeper` → `bokhållare` and `Quern` → `handkvarn`. Existing terms `stockpile` → `förråd`, `squad` → `trupp`, and `gear assembly` → `kugghjulsuppsättning` were applied.
- **Local validation:** JSON parsing, `git diff --check`, and Gitleaks passed. A bounded low-priority Hunspell run produced no unknown tokens. `svlang check` produced only V2 heuristic false positives caused by independent UI labels and imperatives. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 17 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 17 submitted translations exactly (17/17).
- **Archive status:** This batch JSON, this status record, and the terminology update are ready for the `yeager/translations` archive commit.
