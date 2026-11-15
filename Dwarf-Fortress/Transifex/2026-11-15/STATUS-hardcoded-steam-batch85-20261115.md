# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 85

- **Date:** 2026-11-15
- **Scope:** 20 concise UI terms for terrain, directions, construction, work details, trade, combat, grammar and world-map labels.
- **Terminology:** Preserved technical labels such as `X-dimension` and `Presensparticip`; used Swedish game UI terms including `Ugnsdrift`, `Metallmöbler` and `Spioneri`.
- **Local validation:** JSON parsing, whitespace/diff check, Gitleaks, Hunspell and svlang passed. `l10n-lint` cannot parse the wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk `PATCH` accepted all 20 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all submitted translations exactly, 20/20.
- **Status:** Submitted and verified upstream. The entries remain unreviewed in Transifex.
