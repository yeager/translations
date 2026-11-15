# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 83

- **Date:** 2026-11-15
- **Scope:** 25 short UI labels for reading, facilities, history, construction, terrain, uniforms, material collection and character traits.
- **Terminology:** Preserved intentional trailing spaces in source fragments and used `Redelåda` for `Nest Box`, consistent with the earlier component batch.
- **Local validation:** JSON parsing, whitespace/diff check and Gitleaks passed. Hunspell only reported the correct compound `Redelåda`. `svlang` only found an English token while parsing the JSON wrapper. `l10n-lint` cannot parse the wrapper's numeric `batch` field as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` accepted all 25 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 25/25.
- **Status:** Submitted and verified upstream. The entries remain unreviewed in Transifex.
