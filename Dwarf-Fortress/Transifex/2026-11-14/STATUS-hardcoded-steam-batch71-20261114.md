# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 71

- **Date:** 2026-11-14
- **Scope:** 10 complete dialogue, configuration, warning, and navigation strings. Incomplete sentence fragments remain unmodified pending fuller UI context.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, bounded low-priority Hunspell, and `svlang check` completed. Hunspell and svlang reported only the intentional domain compounds `tributavtalet` and `tundraregioner`; svlang's two V2 findings are false positives in a normal declarative sentence and an imperative. `l10n-lint` was run but cannot parse the archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 10 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 10 submitted translations exactly (10/10).
- **Archive status:** This batch JSON and status record are ready for the `yeager/translations` archive commit.
