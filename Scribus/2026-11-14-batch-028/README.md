# Scribus Swedish review, batch 028

32 reviewed UI strings from the local Scribus Swedish TS catalog.

Scope: preflight verification, printing, UCR and spot-colour settings,
Scrapbook and Scripter preferences, table-of-contents terminology, and
typography controls. The work corrects legacy mistranslations and uses
established Swedish print-production terminology.

Checks passed before submission:

- Qt `lrelease` compilation
- cached-diff whitespace check
- Gitleaks
- Hunspell-sv manual triage for UCR, CMY and underfärgsreducering
- svlang manual triage for long technical help strings and UI fragments

Upstream: saved through the Transifex REST API and read back successfully for
all 32 strings. This does not imply a Transifex review-state change.
