# Scribus Swedish review, batch 029

23 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: interface preferences, document-layout descriptions, printer dialogs,
and print-preview controls. The batch removes residual English terminology and
normalizes Swedish print-production terminology, including UCR and decorative
colours.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv and svlang manual triage for CMY/CMYK, UCR, HTML, and technical
  UI fragments

Upstream: saved through the Transifex REST API and read back successfully for
all 23 strings. This does not imply a Transifex review-state change.
