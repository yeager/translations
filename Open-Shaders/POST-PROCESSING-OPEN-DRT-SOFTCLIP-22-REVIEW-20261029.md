# Open Shaders: OpenDRT och mjuk klippning, granskning 22

Det tjugoandra häftet för `feature.post_processing` innehåller 25 nycklar för
OpenDRT:s mjuka renhetsklippning, nyansförskjutning och renderingsrymd.

Färgrymderna RGB och P3 bevaras. `Softclip` översätts beskrivande som `mjuk
klippning`, medan `purity` är `renhet` genomgående.

Kontroller den 29 oktober 2026:

- JSON-syntax och 25 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
