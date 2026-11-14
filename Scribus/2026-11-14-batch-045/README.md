# Scribus Swedish review, batch 045

Reviewed local TS entries 6601–6750 on 14 November 2026.

The batch contains 25 context-checked corrections in PDF annotation controls,
viewer toolbar names, navigation actions and plugin categories.

Validation completed before submission:

- `lrelease`: 8 127 finished translations and 24 untranslated source strings
- `git diff --cached --check`
- Gitleaks
- Hunspell-sv, run with lower CPU priority; `Courier` and `Helvetica` are
  intentional PDF font names
- svlang; its remaining warnings are expected false positives from concatenated
  short UI labels and font names

Only the 25 changed strings were saved through the Transifex REST API. Exact
readback confirmed all 25 saved values. Review-state marking was not attempted.
