# Scribus Swedish review, batch 023

38 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: polygon controls, preference migration and error messages, colour
management, display preferences, and document item-attribute shortcuts.
Terminology was normalized for Swedish UI use; Qt and colour-management
technical identifiers were preserved where required.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv, with only product names, technical identifiers, HTML tags, and
  valid technical compounds remaining
- svlang manual triage, including long technical help texts

Upstream: saved through the Transifex REST API and read back successfully for
all 38 strings. This does not imply a Transifex review-state change.
