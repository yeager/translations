# Scribus Swedish review, batch 024

24 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: document-section shortcuts, saving and autosave preferences, document
layout help text, and external-tool settings. The batch normalizes Swedish
wording and accelerators and uses **Återge** for rendering in visible UI text.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv manual triage for product names, technical format terms, and
  valid compounds
- svlang manual triage for UI fragments and technical help strings

Upstream: saved through the Transifex REST API and read back successfully for
all 24 strings. This does not imply a Transifex review-state change.
