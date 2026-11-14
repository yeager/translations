# Scribus Swedish review, batch 030

32 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: print-preview settings and image, line, group, fill and shadow
properties. The batch normalizes Swedish graphics terms for clipping paths,
line joins, opacity, scaling, colour conversion and under-colour reduction.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv and svlang manual triage for graphics, colour-management and
  implementation terms

Upstream: saved through the Transifex REST API and read back successfully for
all 32 strings. This does not imply a Transifex review-state change.
