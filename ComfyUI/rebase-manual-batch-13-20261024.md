# ComfyUI svensk ombasning, manuell batch 13

Batchen omfattar de sista 69 hittills saknade `main.json`-nycklarna för
arbetsytspanelens abonnemang, inbjudningar, medlemmar och fakturor.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Den direkta jämförelsen mellan
`en/main.json` och `sv/main.json` har nu inga saknade nycklar eller
platshållaravvikelser.

`pnpm locale:check` visar däremot nya engelska plural- och strukturändringar
som inte fångas av den direkta plattjämförelsen. De fortsätter i nästa manuella
batch, tillsammans med `nodeDefs.json`.
