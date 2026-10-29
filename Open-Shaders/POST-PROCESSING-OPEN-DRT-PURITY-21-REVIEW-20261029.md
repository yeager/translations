# Open Shaders: OpenDRT och renhetsgränser, granskning 21

Det tjugoförsta häftet för `feature.post_processing` innehåller 25 nycklar för
OpenDRT:s renhetsgränser, efterbriljans och skärmkompensation.

`Purity` översätts med `renhet` genomgående. Färgstandarderna DCI, Rec.1886,
sRGB och HDR bevaras och måttenheten `nit` skrivs enligt svensk praxis.

Kontroller den 29 oktober 2026:

- JSON-syntax och 25 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
