# Våteffekter: pölbildning, häfte 10

## Omfattning

Häftet omfattar 16 oarkiverade strängar för nederbördsanalys, scenväljare och
pölbildning.

## Språkval

- `Wetness Effects` är konsekvent **våteffekter**.
- `Scene Selector` är **Scenväljaren**, med versal eftersom det är namnet på
  en specifik funktion i programmet.
- `puddle wetness` och `puddle formation` är **pölväta** respektive
  **pölbildning**.
- Formatsträngarna behåller samtliga markörer. Procenttecknet får ett
  svenskt mellanrum efter interpolation och multiplikatorer skrivs med `×`.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 8,8 av 10;
V2-varningen för frågekonstruktionen `Hur plan en yta behöver vara …` är en
felträff. Hunspell markerar formatfragment och fackord som `pölbildning`,
`pölradie` och `pölväta`; de ska behållas.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
