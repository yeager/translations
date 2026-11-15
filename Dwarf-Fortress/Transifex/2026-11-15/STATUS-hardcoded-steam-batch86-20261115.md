# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 86

- **Date:** 2026-11-15
- **Scope:** 30 current UI labels for display modes, workshops, claims, history, equipment, locations, occupations and combat.
- **Terminology:** Used `Läderklädesverkstad`, `Benhuggare`, `Retorter` and `Smid` as idiomatic menu labels. Source whitespace in action fragments was preserved.
- **Local validation:** JSON parsing, whitespace/diff check and Gitleaks passed. Hunspell only reported the correct compound `Läderklädesverkstad`. The svlang V2 and `workshop` reports stem from JSON wrapper identifiers rather than the Swedish targets. `l10n-lint` cannot parse the wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` accepted all 30 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 30/30.
- **Status:** Submitted and verified upstream. The entries remain unreviewed in Transifex.
