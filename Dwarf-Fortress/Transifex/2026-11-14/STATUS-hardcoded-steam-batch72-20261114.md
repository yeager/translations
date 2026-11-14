# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 72

- **Date:** 2026-11-14
- **Release check:** Bay 12's official release page lists Dwarf Fortress 53.17, released 2026-11-09. The project is active and well within the 48-month maintenance window.
- **Scope:** 20 complete UI, configuration, construction, work-order, navigation, and status strings. `NEW` in the ice-track label was preserved as a directional game code.
- **Terminology:** Added `Ice Upward Track` → `uppåtgående isspår` to the component terminology. `Stockpile` remains `förråd` and `Item` remains `föremål`.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, bounded low-priority Hunspell, and `svlang check` completed. Hunspell reported only the intentional game compound `isspår`; svlang reported it as uncommon plus three false-positive V2 findings across independent UI labels. `l10n-lint` was run but cannot parse this archive wrapper's numeric `batch` metadata as a catalogue entry. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 20 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 20 submitted translations exactly (20/20).
- **Live component status after submission:** 2,560 translated, 23,859 untranslated, 26,419 total, 915 reviewed. Translation and review are separate states.
- **Archive status:** This batch JSON, this status record, and the terminology update are ready for the `yeager/translations` archive commit.
