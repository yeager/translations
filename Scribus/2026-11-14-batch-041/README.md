# Scribus Swedish review, batch 041

Reviewed local TS entries 6001–6150 on 14 November 2026.

The batch contains 13 context-checked Swedish corrections in importer messages,
automatic recovery and the resource manager. In particular, resource retrieval
uses `Läs in`, and dictionary terminology is normalized to `ordlistor`.

Validation completed before submission:

- `lrelease`: 8 127 finished translations and 24 untranslated source strings
- `git diff --cached --check`
- Gitleaks
- Hunspell-sv, run with lower CPU priority
- svlang, with project names, API identifiers and short UI labels assessed as
  expected false positives

Only the 13 changed strings were saved through the Transifex REST API. Exact
readback confirmed all 13 saved values. Review-state marking was not attempted.
