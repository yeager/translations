# Scribus Swedish review, batch 027

28 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: PDF export quality, security, colour profile, page-display, font, path,
plugin and preflight strings. The batch normalizes production-printing terms,
viewer terminology, and Swedish compound forms.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv manual triage for technical abbreviations and valid compounds
- svlang manual triage for PDF technical text and UI fragments

Upstream: saved through the Transifex REST API and read back successfully for
all 28 strings. This does not imply a Transifex review-state change.
