# ComfyUI svensk nodeDefs, manuell batch 1

Batchen omfattar 23 texter för noden `BlockSparseAttention`, inklusive
beskrivning, indata, utdata och tekniska begränsningar.

Kontroller: JSON-parsning, platshållarjämförelse, svlang, l10n-lint 1.23.27,
Hunspell, `git diff --check` och avgränsad Gitleaks. Antalet saknade
`nodeDefs.json`-nycklar minskade från 1 321 till 1 298 utan
platshållaravvikelser.

Commit-hooken anger att nodens visningsnamn ännu saknar kodreferens uppströms.
Översättningen är giltig; varningen gäller endast användningen i koden.
