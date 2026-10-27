# Våteffekter: klimatförinställningar, häfte 06

## Omfattning

Häftet omfattar 16 oarkiverade nycklar i `feature.wetness_effects`: de två
sista effekterna för nordiskt klimat samt samtliga etiketter och förklaringar
för klimatförinställningarna.

## Språkval

- `Climate Preset` blir **klimatförinställning**, vilket skiljer den valbara
  profilen från klimatets parametrar.
- `Legacy` är **ursprunglig**, eftersom profilen använder projektets äldre
  värden och inte en tidigare programversion i största allmänhet.
- `Custom` är **anpassad** och beskrivs som **användardefinierade
  inställningar**.
- Förinställningarnas namn är svenska beskrivningar. `monsun/extrem` och
  `nordiskt (standard)` bevarar profilernas avsedda skillnad.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 10,0 av 10;
frekvensnoteringarna gäller förväntade fackord. Hunspell markerar endast
`Standardväderövergångar`, en korrekt teknisk sammansättning.

Filen ska jämföras med en ny Weblate-export innan eventuell import efter att
komponenten har låsts upp.
