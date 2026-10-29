# Open Shaders: efterbehandling och tonmappning, granskning 6

Det sjätte häftet för `feature.post_processing` innehåller 25 nycklar för
färgkorrigering, kurvförhandsvisning och tonmappning.

`Color Grading` översätts konsekvent med `färgkorrigering` och `Tone Mapping`
med `tonmappning`. De tekniska beteckningarna HDR, LUT och RGB-kanalerna
bevaras. Facktermen `toe`/`shoulder` i verktygstipset skrivs om till den mörka
respektive ljusa delen av kurvan, så att texten är begriplig utan att ändra
innebörden.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga tekniska namn och facktermer som har
  granskats manuellt.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
