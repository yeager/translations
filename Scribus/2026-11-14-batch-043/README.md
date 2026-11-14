# Scribus Swedish review, batch 043

Reviewed local TS entries 6301–6450 on 14 November 2026.

The batch contains 26 context-checked corrections in paragraph, table and
toolbar style controls. It aligns parent-style wording, tabulator terminology,
accelerators and Swedish UI phrasing.

Validation completed before submission:

- `lrelease`: 8 127 finished translations and 24 untranslated source strings
- `git diff --cached --check`
- Gitleaks
- Hunspell-sv, run with lower CPU priority
- svlang; its remaining findings are expected for short UI strings and
  established terms such as `styckestil` and `SVG`

Only the 26 changed strings were saved through the Transifex REST API. Exact
readback confirmed all 26 saved values. Review-state marking was not attempted.
