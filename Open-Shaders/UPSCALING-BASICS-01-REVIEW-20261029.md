# Open Shaders: uppskalning, granskning 1

Häftet innehåller 27 nycklar från den första delen av
`feature.upscaling`. Det omfattar DLSS-förinställningar, skärpning,
FidelityFX-bibliotek och grundläggande alternativ för bildgenerering.

`Preset` har konsekvent översatts med `förinställning`, vilket stämmer med
översättningsminnet. Produktnamn och tekniska förkortningar, däribland DLSS,
DLAA, FSR, FidelityFX, RCAS och NVIDIA, är avsiktligt oförändrade. Samtliga
formatmarkörer i upplösningsvarningen är bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax och alla 27 källnycklar är kontrollerade mot den lokala engelska
  katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell-utfallet består endast av avsiktliga produktnamn och tekniska
  förkortningar.
- `svlang check` markerar fem möjliga V2-avvikelser. De är falska positiva i
  bisatser och uppmaningar och har lästs manuellt.
- Filen ska jämföras med en ny Weblate-export innan import, eftersom
  komponenten fortfarande är låst.
