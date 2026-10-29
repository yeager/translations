# Open Shaders: färgkontroller, granskning 7

Det sjunde häftet för `feature.post_processing` innehåller 25 nycklar för
färgkorrigeringens ton- och färgrymdskontroller.

`Hue` är `nyans`, medan `saturation` är `mättnad`. `Lift`, gamma och gain
behålls som den etablerade styrtrion, med `lift` översatt till `lyft` och gain
till `förstärkning`. De standardiserade beteckningarna HDR, ACEScg och OKLCH
bevaras.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga tekniska namn och facktermer som har
  granskats manuellt.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
