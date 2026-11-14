# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 77

- **Date:** 2026-11-14
- **Scope:** 28 complete dialogue actions and response prompts for tribute, negotiation, ceasefire, information, family, accusation, trade, rescue, and local history. Incomplete template strings were deliberately excluded.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, and bounded low-priority Hunspell passed. `svlang check` produced only two V2 heuristic false positives caused by independent action labels. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 28 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 28 submitted translations exactly (28/28).
- **Archive status:** This batch JSON and status record are ready for the `yeager/translations` archive commit.
