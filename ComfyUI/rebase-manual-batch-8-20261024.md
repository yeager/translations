# ComfyUI svensk ombasning, manuell batch 8

Batchen omfattar 57 texter för arbetsyteåtkomst, OAuth, aviseringar, introduktion,
sidofält och widgetkontroller.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 333 till 276. Inga platshållaravvikelser finns.

Commit-hooken rapporterar åtta widgetnycklar som ännu saknar kodreferenser
uppströms. Översättningarna är giltiga; varningen gäller endast oanvända nya nycklar.
