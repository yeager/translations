# FreeCAD: tionde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
6664320–6677106, mot XLIFF-kontexten, Assembly-källkoden och den granskade
FreeCAD-terminologin. Inga ändringar eller röster skickades till Crowdin.

## Bedömning

- Sexton av 20 kandidater är godtagbara i sitt sammanhang.
- `Fästförskjutning`, `materialförteckning`, `sammanställning`, `cylindrisk
  led`, `kugghjuls-/remled` och `Gör stel` följer etablerad
  FreeCAD-terminologi.
- Platshållaren `{order}`, HTML-taggarna, radbrytningarna och de typografiska
  citattecknen är bevarade.
- Texten om materialförteckning förklarar på korrekt svenska att objektet kan
  exporteras utan att sparas i dokumentet.

## Rättelser att kontrollera i Crowdin

Fyra kandidater använder en avvikande översättning av `revolute joint` eller
`malformed joints`:

- 6689570 `Malformed joints:` ska vara `Felaktigt definierade leder:`, inte
  `Felaktigt utformade leder:`.
- 6677100 `Revolute Joint` ska vara `Rotationsled`, inte `Vridled`.
- 6677102 ska inledas `Skapar en rotationsled ...`, inte `Skapar en
  vridled ...`.
- 6690830 ska ange `rotationslederna`, inte `vridlederna`, i instruktionen
  om kugghjuls- eller remled.

## Slutsats

De fyra rättelserna ska först jämföras med Crowdins aktuellt valda måltexter.
Övriga 16 poster kräver inga nya Crowdin-förslag.
