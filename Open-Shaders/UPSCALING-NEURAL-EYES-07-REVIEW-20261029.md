# Open Shaders: neural rendering och ögonlägen, granskning 7

Det sjunde uppskalningshäftet innehåller 25 nycklar för dialogomfattning,
ögonlägen och materialval i Neural Rendering.

Ögonlägena har översatts konsekvent med `parallella ögon`, `separata ögon`
och `växla ögon`. `Follow Foveation` behålls som namnet på en befintlig
inställning. Prestandavärden i millisekunder och GPU-termer är bevarade.

Kontroller den 29 oktober 2026:

- JSON-syntax, 25 källnycklar och formatmarkörer är kontrollerade mot den
  lokala engelska katalogen.
- `l10n-lint` och `svlang skrivregler` godkänner filen utan anmärkning.
- Hunspell markerar endast den avsiktligt oförändrade inställningen `Follow
  Foveation`.
- Häftet kräver en ny Weblate-export före import till den låsta komponenten.
