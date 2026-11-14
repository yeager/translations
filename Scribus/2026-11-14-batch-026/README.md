# Scribus Swedish review, batch 026

34 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: keyboard shortcut terminology, operator settings, and PDF export
options. The batch replaces residual English UI words, preserves accelerator
semantics, and standardizes `återgivning` and print-production terminology.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv manual triage for the XML extension and a valid compound
- svlang manual triage for concatenated UI fragments

Upstream: saved through the Transifex REST API and read back successfully for
all 34 strings. This does not imply a Transifex review-state change.
