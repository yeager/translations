# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 74

- **Date:** 2026-11-14
- **Scope:** 17 complete tutorial and UI strings covering unit filtering, conversations, world creation, meeting and dining zones, combat, animal handling, workshops, minecarts, and travel.
- **Local validation:** JSON parsing, `git diff --check`, and Gitleaks passed. Hunspell's only initial hit was the UI-name compound `hållmenyn`; it was rewritten as the visible menu name `menyn Håll`. `svlang check` thereafter reported only false-positive V2 warnings in grammatical UI labels and clauses. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 17 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 17 submitted translations exactly (17/17).
- **Archive status:** This batch JSON and status record are ready for the `yeager/translations` archive commit.
