# ComfyUI svensk ombasning, manuell batch 9

Batchen omfattar 54 texter för fakturering, avslut av abonnemang,
betalningsåterställning och abonnemang som inte kan väljas.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 276 till 222. Inga platshållaravvikelser finns.

Commit-hooken rapporterar fem enkätalternativ som ännu saknar kodreferenser
uppströms. Översättningarna är giltiga; varningen gäller endast oanvända nya nycklar.
