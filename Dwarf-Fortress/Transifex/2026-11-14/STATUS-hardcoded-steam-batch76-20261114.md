# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 76

- **Date:** 2026-11-14
- **Scope:** 53 standardised conversation actions for emotion, acknowledgement, and dismissal. The batch follows the established component patterns: `State feelings of …` → `Uttryck känslor av …`, `State minor feeling of …` → `Uttryck en svag känsla av …`, `Acknowledge lack of …` → `Tillstå brist på …`, and `Dismiss minor feeling of …` → `Avfärda en svag känsla av …`.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, and bounded low-priority Hunspell passed. `svlang check` only reported false positives because 53 independent action labels were supplied as one text block. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 53 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 53 submitted translations exactly (53/53).
- **Archive status:** This batch JSON and status record are ready for the `yeager/translations` archive commit.
