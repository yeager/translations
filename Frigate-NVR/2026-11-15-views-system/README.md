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
