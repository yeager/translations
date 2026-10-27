# Våteffekter: parametrar, häfte 09

## Omfattning

Häftet omfattar 16 oarkiverade strängar för hårväta, intervall, regntyper,
radier och funktionssammanfattningen.

## Språkval

- `rain-wetness` är **regnväta** och `surface wetness` är **ytväta**.
  Termerna skiljer regnets direkta effekt från den allmänna yteffekten.
- `trails` är **rännilar** även här, konsekvent med tidigare våteffektshäften.
- `shore wetness effects` blir **våteffekter längs stränder**. Det avser
  effekten vid strandlinjen, inte allmän strandbelysning.
- `wetness intensity` uttrycks som **intensitet för väta**, vilket är naturlig
  svenska och tydligare än en konstruerad sammansättning.
- Formattal och enhet behålls i `{:.2f} meter` och `%.1f s`.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 10,0 av 10.
Hunspell markerar formatfragmenten `.1f` och `:.2f` samt de korrekta
fackorden `pölbildning`, `regnväta` och `ytväta`.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
