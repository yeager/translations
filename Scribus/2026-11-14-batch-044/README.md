# Scribus Swedish review, batch 044

Reviewed local TS entries 6451–6600 on 14 November 2026.

The batch contains 29 context-checked corrections in the short-words dialog
and PDF annotation/form controls. It replaces English UI remnants, corrects
the combination-box label, and clarifies pointer and validation events.

Validation completed before submission:

- `lrelease`: 8 127 finished translations and 24 untranslated source strings
- `git diff --cached --check`
- Gitleaks
- Hunspell-sv, run with lower CPU priority, with no findings
- svlang; its two warnings are expected false positives from concatenated short
  UI labels

Only the 29 changed strings were saved through the Transifex REST API. Exact
readback confirmed all 29 saved values. Review-state marking was not attempted.
