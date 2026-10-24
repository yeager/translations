# ComfyUI svensk ombasning, manuell batch 5

Batchen omfattar 90 texter för distribution till Comfy API, val av distribution,
SSO på skrivbordet, dynamiska grupper, felkatalogen och allmänna gallerikontroller.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 562 till 472. Inga platshållaravvikelser finns.

Ändringarna är lokala tills den manuella ombasningen har översatt samtliga nya
upstream-nycklar och hela PR:n kan verifieras.
