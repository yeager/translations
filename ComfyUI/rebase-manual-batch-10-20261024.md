# ComfyUI svensk ombasning, manuell batch 10

Batchen omfattar 51 texter för abonnemangsförhandsvisning, återaktivering,
rabatterbjudanden och årliga krediter.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 222 till 171. Inga platshållaravvikelser finns.
