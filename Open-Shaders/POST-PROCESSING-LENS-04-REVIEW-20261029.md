# Open Shaders: efterbehandling och objektiv, granskning 4

Det fjärde häftet för `feature.post_processing` innehåller 25 nycklar för
objektiv, filmplan, sensorskalning och kamerastatus.

Fototermerna `lens`, `filmback`, `sensor`, `shutter angle` och `frame rate`
översätts med `objektiv`, `filmplan`, `sensor`, `slutarvinkel` och
`bildfrekvens`. Funktionsnamnen `Cinematic Camera`, `True Directional
Movement` och `Depth of Field` är bevarade. Alla tre formatmarkörerna för
sensor- och slutartidsvärden är bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och formatmarkörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast tekniska funktionsnamn, förkortningar och den
  etablerade grafiktermen `bloom`.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
