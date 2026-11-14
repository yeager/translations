# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 80

- **Date:** 2026-11-14
- **Scope:** 19 complete menu actions for selection, tombs, clothing display, workshop and stockpile links, digging, guildhalls, traffic, burrows, engraving, work details, gathering, display items, and blueprints.
- **Terminology:** Added `Dig Mode` → `grävläge`. The prior component choice `Burrow` → `håla` was retained.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, and bounded low-priority Hunspell passed. Hunspell only reported the documented compound `grävläge`. `svlang check` generated one V2 heuristic false positive from independent menu labels. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 19 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 19 submitted translations exactly (19/19).
- **Archive status:** This batch JSON, status record, and terminology update are ready for the `yeager/translations` archive commit.
