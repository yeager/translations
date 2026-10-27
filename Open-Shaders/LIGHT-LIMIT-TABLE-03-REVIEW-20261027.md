# Begränsning av ljuskällor: tabell, häfte 03

## Omfattning

Häftet omfattar 16 oarkiverade strängar för felsökningsåterställning och
kolumnrubriker i ljuskällstabellen.

## Språkval

- `debug override` är **felsökningsåsidosättning**, enligt terminologin i
  tidigare Open Shaders-häften.
- `pins` blir **låsningar** eftersom de håller kvar en ljuskälla i ett valt
  läge.
- `spill` är **spill**, en etablerad kort etikett för data utanför tilldelad
  kapacitet.
- `Prio`, `Solo` och `Status` hålls korta för tabellens rubrikrad.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 8,8 av 10;
V2-varningen för återställningsuppmaningen är en felträff. Hunspell ger inga
träffar.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
