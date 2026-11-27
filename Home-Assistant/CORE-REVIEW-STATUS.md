# Home Assistant Core – granskningsstatus

Senast uppdaterad: 2026-11-27

Aktuell källrevision: `1d07105b760c73093145526a51758938e87cc658`
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`

## Senaste batch: 68 417–68 536

120 Lokalise-poster granskade: 54 direkta källmatchningar, 65 referenser till 48 mål och en äldre källfrånvarande Roborock-pluralnyckel. 12 aktuella strängar i intervallet och två delade mål utanför intervallet uppdaterades och API-lästes tillbaka. Alla referenser matchar; platshållare 119/119 för aktuella poster. `svlang` utan flaggor; Hunspell-tester 19/19 godkända. Ordlisteändringar för sirén, rumsprioritet och solcellsväxelriktare pushades utan release. TMX validerar med 36 123 poster (35 892 Lokalise-ID, 231 historiska).

Kvarstående importhinder: aktuell Core har Roborock-nycklar `state::one`/`state::two`, men de saknas i Lokalise. Försök att lägga till dem via API gav HTTP 403; se daterad rapport och tidigare fullständig missing-keys-rapport.

Nästa position: **68 537**. Cirka **9 000** positioner återstår; granskningen pågår.

Rapport: `2026-11-27-reviewed-core-68417-68536.md` med QA-, readback-, referens- och TMX-underlag.
