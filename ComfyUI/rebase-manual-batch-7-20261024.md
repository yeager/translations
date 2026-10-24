# ComfyUI svensk ombasning, manuell batch 7

Batchen omfattar 71 texter för agentens instruktionspaket och mallarbetsflöden.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 404 till 333. Inga platshållaravvikelser finns.

Ändringarna är lokala tills den manuella ombasningen har översatt samtliga nya
upstream-nycklar och hela PR:n kan verifieras.
