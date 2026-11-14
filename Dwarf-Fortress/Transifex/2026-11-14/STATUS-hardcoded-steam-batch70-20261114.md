# Dwarf Fortress Steam, hardcoded_steam, Swedish, batch 70

- **Date:** 2026-11-14
- **Scope:** 14 complete UI and tutorial strings in `hardcoded_steam`; sentence fragments without sufficient context were deliberately excluded.
- **Terminology:** Updated the project glossary with `Megabeast` → `megabest`. Existing choices for `workshop`, `squad`, `item`, and combat terminology were retained.
- **Local validation:** JSON parsing, `git diff --check`, Gitleaks, and a bounded low-priority Hunspell run passed. Hunspell only reported the intentional game term `megabest`. `svlang check` reported that term as uncommon plus three V2 heuristic false positives in grammatical imperatives/subordinate clauses. `l10n-lint` was run but cannot parse this archive wrapper because it treats the numeric `batch` metadata field as a translation; the strings themselves were independently JSON-validated. `msgfmt` does not apply to this JSON delta.
- **Upstream submission:** Transifex JSON:API bulk PATCH accepted 14 updates (HTTP 200).
- **Upstream verification:** Direct API readback matched all 14 submitted translations exactly (14/14).
- **Live component status after submission:** 2,530 translated, 23,889 untranslated, 26,419 total, 915 reviewed. Translation and review are separate Transifex states.
- **Archive status:** This batch JSON, this status record, and the terminology update are ready for the `yeager/translations` archive commit.
