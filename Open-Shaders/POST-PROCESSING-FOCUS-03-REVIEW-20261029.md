# Open Shaders: efterbehandling och fokus, granskning 3

Det tredje häftet för `feature.post_processing` innehåller 25 nycklar för
fokus, synfält, bildfrekvens och ISO-gränser i den filmiska kameran.

Fototermerna är konsekventa med föregående häfte: `focus distance` blir
`fokusavstånd`, `focal length` blir `brännvidd`, `gate fit` blir
`sensoranpassning` och `angle of view` blir `bildvinkel`. Funktionsnamnet
`Cinematic Camera` och ISO lämnas oförändrade. De tre formatmarkörerna för
synfält och kamerastatus är bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och formatmarkörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast det bevarade funktionsnamnet och sammansatta
  fotografitermer som har granskats manuellt.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
