# Begränsning av ljuskällor: budget, häfte 02

## Omfattning

Häftet omfattar 16 oarkiverade strängar för billboard-ljuskällor,
omritningsbudget och gallring av skuggkastare.

## Språkval

- `billboard` behålls som etablerad grafikterm och skrivs med bindestreck i
  sammansättningar.
- `shadow caster` är **skuggkastare**, och `cull` är **hoppa över** i den
  förklarande hjälpen.
- Kodnamnen `frametime`, `isinterior`, `frametarget`, `Intellightent` och
  tangentkombinationen `Ctrl+Click` bevaras som tekniska identifierare.
- Alla radbrytningar, formatmarkörer och den tomma raden i formelhjälpen
  bevaras.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. Den först skrivna formuleringen
`Förutsägbar, den oscillerar inte` förbättrades till `Förutsägbar och utan
svängningar`. `svlang` ger 0,4 av 10 eftersom katalogen består av tekniskt
täta flerradstexter med identifierare utanför frekvenslistan; V2-varningarna
gäller korrekta påståenden och uppmaningar. Hunspell-träffarna är format,
produktnamn, förkortningar eller granskade fackord.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
