# Open Shaders: OpenDRT och nyanskontroller, granskning 20

Det tjugonde häftet för `feature.post_processing` innehåller 25 nycklar för
OpenDRT:s nyanskontrast, nyansförskjutning och renhetskomprimering.

Färgmodellerna RGB och CMY bevaras. `Hue` översätts konsekvent med `nyans`
och `purity` med `renhet`. Abney-effekten behålls som det etablerade namnet på
den färgperceptuella effekten.

Kontroller den 29 oktober 2026:

- JSON-syntax och 25 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
