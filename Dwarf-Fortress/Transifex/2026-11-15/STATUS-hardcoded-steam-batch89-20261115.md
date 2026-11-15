# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 89

- **Date:** 2026-11-15
- **Scope:** 20 short labels for facilities, world generation, emotions, professions, navigation and combat outcomes.
- **Local validation:** JSON parsing, whitespace/diff check and Gitleaks passed. Hunspell reported the valid compounds `Ostmakare` and `Titanantal`. `msgfmt` does not apply to this JSON delta; `l10n-lint` cannot parse its numeric batch metadata.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` accepted all 20 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 20/20.
- **Status:** Submitted and verified upstream; entries remain unreviewed in Transifex.
