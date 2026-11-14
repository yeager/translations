# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 75

- **Date:** 2026-11-14
- **Scope:** 36 complete UI, configuration, combat, conversation, world-generation, workshop, trap, and status strings. This is the first enlarged Transifex batch after the batch-size change.
- **Local validation:** JSON parsing, `git diff --check`, and Gitleaks passed. Bounded low-priority Hunspell reported only the intentional compounds `lerinsamling` and `makroinstruktioner`. `svlang check` generated false-positive V2 warnings because it assessed independent UI labels and imperative clauses as one prose passage. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 36 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 36 submitted translations exactly (36/36).
- **Archive status:** This batch JSON and status record are ready for the `yeager/translations` archive commit.
