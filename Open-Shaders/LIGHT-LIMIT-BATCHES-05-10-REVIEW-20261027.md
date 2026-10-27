# Begränsning av ljuskällor: häfte 5–10, granskning 2026-10-27

## Omfattning

Häftena 5–10 omfattar 96 svenska strängar i `feature.light_limit_fix`:
konvertering, partikelljus, fladdrande skuggor, formelredigeraren,
ljusgrupper och visualisering. Varje sträng har lästs mot den aktuella engelska
katalogen rad för rad.

## Språk- och termbeslut

- *culling* är konsekvent **gallring**; när texten beskriver resultatet används
  **gallras bort**.
- *light* är **ljuskälla** eller **ljus** när sammanhanget redan avgränsar
  betydelsen.
- *point light* och *spot light* är **punktljus** respektive
  **strålkastarljus**, i enlighet med etablerade FOSS-termer.
- Tekniska identifierare och filnamn, till exempel `fShadowDistance:Display`,
  `SkyrimPrefs.ini`, `frustum` och `ConvertExcessToNormal`, är avsiktligt
  oförändrade.
- Formuleringar med otydlig ordföljd eller missvisande ordval har rättats,
  bland annat till **bildrutemål**, **dynamiskt omfång** och
  **gallrad av portaler**.

## Kontroller

Samtliga sex filer har kontrollerats med JSON-tolkning, `l10n-lint`, Gitleaks
och en jämförelse mot källan för formatmarkörer, bokstavliga procenttecken och
radbrytningar. Inga avvikelser hittades.

`svlang` och Hunspell kördes på samtliga filer. Deras återstående träffar har
granskats manuellt: de gäller främst spel- och grafiktermer, kodidentifierare,
filnamn, förkortningar och formatsträngar. De är inte stavningsfel eller
ofullständiga översättningar. Samtliga strängar har även kontrollerats mot
terminologibanken och översättningsminnet som förslag, aldrig som automatiskt
facit.

## Upstreamstatus

Filerna är arkiverade lokalt. Hosted Weblate-komponenten är låst, så ingen
import får göras innan den har låsts upp och katalogen har jämförts med en ny
export från Weblate.
