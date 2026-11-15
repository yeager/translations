# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 81

- **Date:** 2026-11-15
- **Scope:** 66 previously untranslated menu labels, status messages and gameplay settings in `hardcoded_steam`.
- **Review:** Reviewed against the project terminology and source context. Six clear Swedish improvements were made, including idiomatic labels for equipment and pets, sewer access, strand extraction, broker requests and masterwork architecture. Technical identifiers, punctuation and the trailing space in `Equipment/pet points: ` were preserved.
- **Local validation:** JSON parsing, whitespace/diff check and Gitleaks passed. Hunspell only reported `Redelåda`, `lärdas` and the established mining term `flusssten`. `svlang` parsed JSON identifiers as prose and flagged the ordinary game verb `attackera`; these are false positives. `l10n-lint` cannot parse this Transifex delta wrapper because its numeric `batch` field is metadata, not a catalogue entry. `msgfmt` does not apply to JSON deltas.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` with the bulk media-type profile accepted all 66 updates at 2026-11-15 03:03:16 UTC (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 66/66.
- **Status:** Submitted and verified upstream. The translations are not marked reviewed by Transifex.
