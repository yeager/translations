# Open Shaders: neural rendering och körmiljö, granskning 9

Det nionde uppskalningshäftet innehåller 25 nycklar för områdesöverlägg,
återställning och validering av körmiljöversioner för Neural Rendering.

Filsökvägen `Data\Shaders\Upscaling\Streamline\` och DLL-namnet
`nvngx_dlssnr.dll` är bevarade exakt. `Build` används här som en installerbar
version och är därför översatt med `version`.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar, sökvägen och `%s`-markörerna är kontrollerade
  mot den lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga filnamn och tekniska komponentnamn.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
