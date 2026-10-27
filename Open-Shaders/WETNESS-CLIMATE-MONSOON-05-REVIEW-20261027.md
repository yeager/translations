# Våteffekter: monsun och nordiskt klimat, häfte 05

## Omfattning

Häftet omfattar 16 tidigare oarkiverade nycklar i
`feature.wetness_effects`: återstående parametrar för monsunprofilen samt
inledande parametrar för den nordiska klimatprofilen. Den sammanlagda
lokala täckningen för komponenten är nu 80 av 201 nycklar.

## Språkval

- `wetness`, `puddle formation` och `transition` är **väta**,
  **pölbildning** och **övergång**.
- `grid` är **rutnät**, medan sannolikhet och intervall uttrycks med
  svensk decimalmarkering.
- Symbolen `×`, enheten `mm/h`, procenttecken och förkortningen `GPU` är
  tekniska data från gränssnittet. `GPU:n` följer svensk böjning av en
  förkortning.
- `Skyrims lätta regn motsvarar inte vätan` är medvetet en normal svensk
  huvudsats. V2-varningen från språkverktyget är därför en felträff.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. `svlang` gav 8,8 av 10 och
flaggar främst tekniska ord som `multiplikatorer`, `prestandapåverkan` och
`pölbildning`; de är korrekta i detta gränssnitt. Hunspell kvarstår med
`Skyrims`, `pölbildning` och `Standardpölbildning`. Det första är ett
egennamn och de andra är fackmässiga sammansättningar, så de ska inte
förvanskas för att passa ordlistan.

Filen är endast arkiverad. Import får ske först när Weblate-komponenten är
upplåst och en ny export har jämförts med varje källnyckel.
