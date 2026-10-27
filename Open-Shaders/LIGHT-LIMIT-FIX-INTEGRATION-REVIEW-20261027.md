# Begränsning av ljuskällor: integrationsgranskning 2026-10-27

## Omfattning

`feature.light_limit_fix` består av 326 aktuella källnycklar. Komponenten har
granskats i 21 separata häften om högst 16 strängar och därefter sammanfogats i
`open-shaders-light-limit-fix-sv-20261027.json`.

## Resultat

- Alla **326 av 326** källnycklar finns i den sammanslagna svenska filen.
- Den sammanslagna filen har inga extra nycklar och batchfilerna har inga
  dubblettnycklar.
- Samtliga formatmarkörer, bokstavliga procenttecken och radbrytningar stämmer
  exakt med den engelska källkatalogen.
- JSON-tolkning, `l10n-lint` och Gitleaks är godkända för hela komponenten.
- Hunspell och svlang har körts både per häfte och på den sammanslagna filen.
  Kvarvarande träffar är tekniska identifierare, filnamn, grafiktermer,
  förkortningar, formatsträngar eller URL:er. De svenska formuleringarna har
  lästs mot aktuell kontext; synlig svensk text har också kontrollerats för tre
  lika konsonanter i följd.

## Terminologi

Komponenten använder konsekvent bland annat **ljuskälla**, **punktljus**,
**strålkastarljus**, **skugga**, **skuggkarta**, **skuggplats**, **gallring**
och **omritning**. Terminologibanken och översättningsminnet har använts som
underlag, men varje term har prövats mot grafik- och spelkontexten.

## Upstreamstatus

Den kompletta komponentfilen och de små importvänliga häftena är arkiverade i
`yeager/translations`. Hosted Weblate-komponenten är fortfarande låst. Ingen
fil får importeras förrän komponenten är upplåst och dess nya export har
jämförts mot den här källversionen.
