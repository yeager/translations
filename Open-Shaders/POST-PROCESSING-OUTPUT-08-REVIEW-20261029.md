# Open Shaders: färgkorrigeringens utdata, granskning 8

Det åttonde häftet för `feature.post_processing` innehåller 25 nycklar för
färgkorrigeringens utdata, dynamikomfång och skuggkontroller.

`Output` är `utdata`, medan `display` är `skärm`. SDR, HDR, sRGB, BT2020 och
LUT bevaras som tekniska standardbeteckningar. Enheten `nit` skrivs utan
engelsk pluralböjning. `SAT` översätts till den korta etiketten `MÄT` för att
stämma med den svenska termen `mättnad`.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och printf-markörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast avsiktliga tekniska namn och facktermer som har
  granskats manuellt.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
