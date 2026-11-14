# Scribus Swedish review, batch 022

32 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: Picture Browser insertion and filtering labels, Plugin Manager status
messages, and polygon controls. The batch uses Swedish UI terms, preserves
placeholders and mnemonics, and keeps product and project names unchanged.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv (only product names, URL terms, and the valid compound
  `taggnamn` remained)
- svlang manual triage (its aggregate warning was caused by a long technical
  support message plus product names and URLs)

Upstream: saved through the Transifex REST API and read back successfully for
all 32 strings. This does not imply a Transifex review-state change.
