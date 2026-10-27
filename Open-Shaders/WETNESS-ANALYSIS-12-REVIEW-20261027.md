# Våteffekter: analys och flikar, häfte 12

## Omfattning

Häftet omfattar 16 oarkiverade strängar för analys av regn och väta,
regndroppseffekter, strandväta och flikarna i gränssnittet.

## Språkval

- `rain & wetness analysis` är **analys av regn och väta**. Ordet *och*
  är tydligare än ett tekniskt snedstreck i rubriken.
- `Shore Wetness` och dess räckvidd blir **strandväta** och
  **strandräckvidd**.
- Radbrytningarna i hjälpen för regndroppar bevaras exakt.
- Alla `printf`-markörer, bokstavliga procenttecken och multiplikatorer
  bevaras med svensk typografi.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` ger 10,0 av 10.
Hunspell markerar formatfragment och sammansättningarna `miljöväta`,
`regnväta` och `strandväta`; de är avsedda tekniska termer.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
