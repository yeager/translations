# ComfyUI svensk ombasning, manuell batch 11

Batchen omfattar 71 texter för arbetsytspanelens faktureringsstatus, automatisk
påfyllning och kreditöversikt.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 171 till 100. Inga platshållaravvikelser finns.

Commit-hooken rapporterar sex nya upstream-nycklar utan kodreferenser. De är
översatta och giltiga; varningen gäller endast källkodens användning.
