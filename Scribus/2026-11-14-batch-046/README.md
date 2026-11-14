# Scribus Swedish review, batch 046

Reviewed local TS entries 6751–6900 on 14 November 2026.

The batch contains 28 context-checked corrections in startup messages,
document status and main-window commands. It removes English fragments,
normalizes terminology and fixes several malformed labels.

Validation completed before submission:

- `lrelease`: 8 127 finished translations and 24 untranslated source strings
- `git diff --cached --check`
- Gitleaks
- Hunspell-sv, run with lower CPU priority; findings are product names,
  file-format names and a runtime placeholder
- svlang; its remaining warnings are expected false positives from short UI
  labels, product names and runtime placeholders

Only the 28 changed strings were saved through the Transifex REST API. Exact
readback confirmed all 28 saved values. Review-state marking was not attempted.
