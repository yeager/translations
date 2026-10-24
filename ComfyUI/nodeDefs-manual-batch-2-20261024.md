# ComfyUI svensk nodeDefs, manuell batch 2

Batchen omfattar 33 texter för Bria-noder som lägger till eller tar bort objekt,
förgrund och bakgrund.

Kontroller: JSON-parsning, platshållarjämförelse, svlang, l10n-lint 1.23.27,
Hunspell, `git diff --check` och avgränsad Gitleaks. Antalet saknade
`nodeDefs.json`-nycklar minskade från 1 298 till 1 265 utan
platshållaravvikelser.

Commit-hooken anger att fyra visningsnamn ännu saknar kodreferenser uppströms.
Översättningarna är giltiga; varningen gäller endast användningen i koden.
