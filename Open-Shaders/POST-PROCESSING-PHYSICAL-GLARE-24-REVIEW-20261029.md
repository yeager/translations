# Open Shaders: fysiskt bländljus, granskning 24

Det tjugofjärde häftet för `feature.post_processing` innehåller 25 nycklar för
fysiskt baserat bländljus, objektiv och öga.

Babinets princip, Fresnel, Fraunhofer, FFT och de matematiska uttrycken
bevaras. Foto- och ögattermer är översatta med bländare, pupill, ögonfransar
och tårfilm.

Kontroller den 29 oktober 2026:

- JSON-syntax och 25 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
