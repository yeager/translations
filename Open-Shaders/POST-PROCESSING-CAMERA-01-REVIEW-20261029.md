# Open Shaders: efterbehandling och kamera, granskning 1

Det första häftet för `feature.post_processing` innehåller 25 nycklar för
grundvärden, rameffekt och kameraeffekter.

`Post processing` översätts inom den här grafikkomponenten med
`efterbehandling`. `Fisheye` behålls som etablerad grafikterm, medan `FOV` är
`synfält`. Formatmarkören `%.3f` och betydelsebärande radbrytningar är
bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och formatmarkören är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast den avsiktliga facktermen `fisheye` och den
  sammansatta termen `brusmängd`.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
