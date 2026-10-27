# FreeCAD: nionde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
6687712–6691166, mot XLIFF-kontexten, FreeCADs källkod och den granskade
FreeCAD-terminologin. Inga ändringar eller röster skickades till Crowdin.

## Bedömning

- Sexton av 20 kandidater är godtagbara i sitt sammanhang.
- `Gör stel` är den fastställda termen för `Turn rigid`; den beskriver låsta
  frihetsgrader och inte en solid geometri.
- `Avgränsningsruta`, `genomskinliga paneler`, `överläggspaneler`, `trädvy`,
  `sammanställning`, `led` och `vinkelgräns` är konsekventa med FreeCADs
  gränssnitt och monteringsarbetsbänk.
- HTML-taggarna och liststrukturen i Assembly-instruktionen är bevarade.

## Rättelser att kontrollera i Crowdin

Följande kandidater avviker från etablerad FreeCAD-terminologi och ska inte
återanvändas som de står:

- 6687712 `Activates the box selection tool`: `Aktiverar verktyget för
  rektangelmarkering`, inte `... för rutmarkering`.
- 6687714 `Bo&x Element Selection`: `Rektangelmarkering av &element`, inte
  `R&utmarkering av element`. Den svenska åtkomstnyckeln ska ligga på
  `element`.
- 6687716 `Activates box element selection`: `Aktiverar
  rektangelmarkering av element`, inte `Aktiverar rutmarkering av element`.
- 6650002 `RackPinion`: `Kuggstång och pinjong`, inte `Kugghjul och
  kuggstång`. Den senare texten tappar den tekniska termen `pinjong` och
  stämmer inte med Assembly-kommandot för en kuggstångs- och pinjongled.

## Slutsats

De fyra rättelserna ska först jämföras med Crowdins aktuellt valda måltexter.
Övriga 16 poster kräver inga nya Crowdin-förslag.
