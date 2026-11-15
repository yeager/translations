# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 84

- **Date:** 2026-11-15
- **Scope:** 35 current UI terms for construction, materials, professions, training, history, facilities, map zones and character status.
- **Terminology:** Uses plain Swedish UI verbs and established compounds, including `Läderverkstad`, `Djurträning`, `Underjordisk fästning` and `Mordkomplott`. Source whitespace on fragment labels was preserved.
- **Local validation:** JSON parsing, whitespace/diff check and Gitleaks passed. Hunspell found no unknown words. `svlang` found no Swedish-language concerns. `l10n-lint` cannot parse the wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` accepted all 35 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 35/35.
- **Status:** Submitted and verified upstream. The entries remain unreviewed in Transifex.
