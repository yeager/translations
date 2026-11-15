# Frigate NVR, views-system — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/system.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-system`, svenska
- Omfattning: 38 tidigare tomma systemsträngar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 38 av 282 nycklar; övriga nycklar var redan översatta eller återstår för senare batcher.

## Språkval och kontroller

Batchen omfattar GPU/NPU, anslutningskvalitet, meddelandeloggar, delat minne
och bildrutor. Tekniknamn och platshållare är bevarade.

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 38`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten rapporterar 168 av 282 översatta strängar, 0
fuzzy och 0 fallerande kontroller. Upstreamläge för denna batch: inskickat och
mottaget; 114 systemsträngar återstår för senare granskning.

## Batch 002

Batchen för kamerors nyckelrutor samt systemhälsa accepterades med 34 av 282
nycklar. Efter importen rapporterar komponenten 202 av 282 översatta strängar,
0 fuzzy och 0 fallerande kontroller. Återstående systemsträngar: 80.

## Batch 003

Batchen för maskinvaru- och strömdiagnostik accepterades med 41 av 282 nycklar.
Komponenten står därefter på 243 av 282 översatta strängar. Den enda
kontrollträffen gäller den avsiktligt oförändrade teknikformatsträngen
`{{camera}} / {{expected}} fps`.

## Batch 004

Slutbatchen accepterades med 39 av 282 nycklar. Ett interpunktionsfel i en
diagnostiktext korrigerades via enhets-API:t. Komponenten är nu 282 av 282
översatt, med 0 fuzzy; den enda kontrollträffen är den medvetet oförändrade
formatsträngen `{{camera}} / {{expected}} fps`.
