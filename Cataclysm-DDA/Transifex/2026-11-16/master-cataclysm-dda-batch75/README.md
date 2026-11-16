# Cataclysm-DDA – svenska, batch 75

Datum: 2026-11-16  
Komponent: `master-cataclysm-dda`  
Kanal: Transifex REST API

Åtta granskade strängar från panelen för bioniska implantat. Källkontext har
kontrollerats i `src/bionics_ui.cpp` från Cataclysm-DDA:s aktuella release.
`%s act` är en energikostnad vid aktivering och har därför översatts med
`%s vid aktivering`; den är inte en fristående menyåtgärd. Färgtaggar,
platshållare, enheter och den synliga tangenten `SPACE` är bevarade.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint
- svlang för text utan UI-taggsyntax
- Hunspell-sv
- kontroll av platshållare och XML-liknande färgtaggar
- `msgfmt` är inte tillämpligt: Transifex API-batch med enskilda JSON-poster,
  inte en PO-katalog.

## Upstream-status

Skickad via Transifex REST API den 2026-11-16: 8 av 8 poster accepterades.
En separat API-återläsning bekräftade exakt måltext för samtliga 8 poster.
Detta bekräftar inskick och sparad översättning, inte upstream-granskning,
merge eller utgivning.
