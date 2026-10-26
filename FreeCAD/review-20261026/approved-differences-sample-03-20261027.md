# FreeCAD: tredje urvalet av godkända avvikelser

Den 27 oktober 2026 granskades nästa urval om 20 godkända avvikelser i den
arkiverade kandidatfilen. Granskningen omfattar sträng-id 6682544–6607651
och gjordes mot källtext, resursnamn och källkodssökväg i XLIFF-filen. Inga
ändringar eller röster skickades till Crowdin.

## Fynd

- Kandidaten för sträng-id `6606469` är felkopplad. Källan är `The export
  list contains no object with a valid bounding box`, men måltexten handlar
  i stället om en okänd SVG-exportstil. Den får inte röstas upp eller laddas
  upp igen. Den kontextuellt korrekta svenska texten är: `Exportlistan
  innehåller inget objekt med en giltig begränsningsruta.`
- `Fillet` har konsekvent översatts till `Avrundning` i båda Draft-kontexterna
  (6606963 och 6662036). Det stämmer med CAD-terminologin och tidigare
  granskning.
- Draft är arbetsbänkens namn och har behållits i `Draft: skapa`, `Draft:
  anteckningar`, `Draft: ändra` och `Draft: snäppning`. Det är att föredra
  framför att felaktigt översätta produktnamnet till exempelvis
  `Släppning`.
- `Trådens hörnpunkter`, `ytbindare`, `hänvisningslinje`, `referenslinje` och
  `begränsningsruta` är begripliga facktermer i sina respektive CAD-kontexter.
- Värdena `True`, `False`, `Axis`, `Center`, `Label Type` och liknande är
  egenskapsnamn eller visade värden i gränssnittet. De ska inte översättas
  inne i citattecken utan att motsvarande egenskapsnyckel i programmet också
  är lokaliserad.

## Slutsats

Nitton av tjugo granskade kandidater är språkligt eller terminologiskt
rimliga i sin givna kontext. Sträng 6606469 är ett verifierat fel och ska
rättas individuellt i Crowdin efter kontroll av den aktuellt valda
översättningen. Detta är ett läsande urval, inte en massändring.
