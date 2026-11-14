# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 78

- **Date:** 2026-11-14
- **Scope:** 51 complete UI strings for loading and generation status, building, selection, navigation, pumps, equipment, worker assignments, world creation, reports, and game options.
- **Terminology:** Added `History Seed` → `historikfrö` and `Cloud View` → `molnvy` to the component glossary.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, and bounded low-priority Hunspell passed. Hunspell only reported the documented component terms `historikfrö` and `molnvy`. `svlang check` produced two V2 heuristic false positives in imperative labels. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 51 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 51 submitted translations exactly (51/51).
- **Archive status:** This batch JSON, status record, and terminology update are ready for the `yeager/translations` archive commit.
