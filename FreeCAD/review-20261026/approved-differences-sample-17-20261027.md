# FreeCAD: sjuttonde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
2594003–6677306, mot XLIFF-kontexten, Part- och PartDesign-källkoden samt den
granskade FreeCAD-terminologin. Inga ändringar eller röster skickades till
Crowdin.

## Bedömning

- Sjutton av 20 kandidater är godtagbara i sitt sammanhang.
- `Yta från kanter`, `Redigera förskjutning`, `sammansatt objekt`,
  `felaktig markering`, `fästning`, `referensplan`, `referenslinje`,
  `avgränsningsruta` och `självskärning` följer den etablerade terminologin.
- Platshållarna `%1`, `%2` och `{}` är bevarade i dialog- och feltexterna.

## Rättelser att kontrollera i Crowdin

- 2594004 `Planar` ska vara `Planär`, inte `Plan`, i
  `PartGui::TaskShapeBuilder`.
- 6685094 ska vara `Boolesk operation: yta som inte kan återställas`, inte
  `Boolesk operation: ytan kan inte återställas`.
- 6685450 `Datums` ska vara `Referensgeometri`, inte `Referensobjekt`, i
  kommandogruppen `CmdPartDatums`.

## Slutsats

De tre rättelserna ska först jämföras med Crowdins aktuellt valda måltexter.
Övriga 17 poster kräver inga nya Crowdin-förslag.
