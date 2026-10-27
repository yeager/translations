# FreeCAD: tjugoförsta urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
6680858–6696084, mot XLIFF-kontexten, den granskade FreeCAD-översättningen
och etablerad Sketcher- och Arch-terminologi. HTML-strukturen i
handledningssträngen kontrollerades utan att ändras. Inga ändringar eller röster
skickades till Crowdin.

## Bedömning

- Femton av 20 kandidater är godtagbara i sitt sammanhang.
- `femhörning`, `sjuhörning`, `avrundning`, `avfasning`, `knutar`,
  `felsökningsinformation`, `rörkoppling`, `normalen` och `icke-plana ytor`
  används korrekt.
- Platshållarna `%1`, `{self.obj.Label}` och `{face.normalAt(0, 0)}` samt
  HTML-markeringen är bevarade.

## Rättelser att kontrollera i Crowdin

- 6682034 ska vara `%1 ange förflyttningsvektor`, inte formuleringen med
  `translationsvektor`.
- 6682036 ska vara `%1 ange andra förflyttningsvektorn`, inte formuleringen
  med `translationsvektorn`.
- 177415 statusvärdet `Idle` ska vara `Inaktiv`, inte `Väntar`.
- 6662396 ska vara `Det går inte att skapa denna rörkoppling genom
  rotationssvep`, inte att den inte går att rotera.
- 6696084 ska ange framtid: `Areavärdena kommer att återställas till 0.`, inte
  presensformen `återställs`.

## Slutsats

De fem rättelserna ska först jämföras med Crowdins aktuellt valda måltexter.
Övriga 15 poster kräver inga nya Crowdin-förslag.
