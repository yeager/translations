# FreeCAD: nittonde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
6679300–6691828, mot XLIFF-kontexten, den granskade FreeCAD-översättningen
och etablerad CAD- och robotterminologi. Inga ändringar eller röster skickades
till Crowdin.

## Bedömning

- Sjutton av 20 kandidater är godtagbara i sitt sammanhang.
- `avrundning`, `yta`, `referensplan`, `referenslinje`, `begränsningsruta`,
  `origo`, `punktmoln`, `normalvektor`, `sammansatt rörelsebana` och
  `VRML-fil` återges konsekvent.
- `Omvänd konstruktion` är en korrekt svensk benämning på *reverse
  engineering* i arbetsbänkens sammanhang. `Stickprov per nod` är en naturlig
  svensk formulering för Poisson-parametern.

## Rättelser att kontrollera i Crowdin

- 6679300 ska vara `Formelement för efterbearbetning`, inte `Efterbearbetande
  formelement`.
- 6679820 och 6679824 `Create Datum` ska vara `Skapa referensgeometri`, inte
  `Skapa referensobjekt`. De längre beskrivningarna får behålla
  `referensobjekt`, eftersom de uttryckligen omfattar både referensgeometri
  och lokalt koordinatsystem.

## Slutsats

De tre rättelserna ska först jämföras med Crowdins aktuellt valda måltexter.
Övriga 17 poster kräver inga nya Crowdin-förslag.
