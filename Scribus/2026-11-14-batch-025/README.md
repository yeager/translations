# Scribus Swedish review, batch 025

30 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: guide and grid terminology, hyphenation and index settings, and object
tool labels. The batch replaces mixed English terminology and incorrect
interface labels with consistent Swedish UI terminology.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv manual triage (only the Scribus product name remained)
- svlang manual triage for UI fragments and one technical help message

Upstream: saved through the Transifex REST API and read back successfully for
all 30 strings. This does not imply a Transifex review-state change.
