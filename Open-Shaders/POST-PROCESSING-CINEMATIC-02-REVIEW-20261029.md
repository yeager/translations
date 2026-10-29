# Open Shaders: efterbehandling och filmisk kamera, granskning 2

Det andra häftet för `feature.post_processing` innehåller 25 nycklar för
bländare, ISO, exponering och optiska kameraregler.

Fototermerna följer svensk användning: `aperture` blir `bländare`,
`f-number` blir `bländartal`, `focal length` blir `brännvidd` och `filmback`
blir `filmplan`. `Cinematic Camera` och `Histogram Auto Exposure` behålls som
namn på funktioner i gränssnittet. ISO-värden och formatmarkörer är bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och fyra formatmarkörer är kontrollerade mot
  den lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga funktionsnamn och sammansatta
  fotografitermer.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
