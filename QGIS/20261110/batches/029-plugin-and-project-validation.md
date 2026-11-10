# Batch 029: plugin-kataloger och projektvalidering

Datum: 2026-11-10

Omfattning: fyra kontextbevarade korrigeringskandidater, poster 238 till 241.
De omfattar blockerade plugin-kataloger och valideringsmeddelanden för
lagrens kortnamn och projektets rotnamn.

Särskilt kontrollerat:

- Termen `centralkatalog` är etablerad i pluginhanterarens berörda dialoger
  och har därför behållits. Terminologilistan har kompletterats med beslutet.
- Att `inte kompatibel` uttrycker orsaken mer idiomatiskt än den tidigare
  felaktiga konstruktionen med `inkompabilitet`.
- Teckenregeln för namn: bokstav utan accent, alfanumeriska tecken, punkt,
  bindestreck och understreck.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `aca701d`](https://github.com/yeager/swedish-tm/commit/aca701d).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
