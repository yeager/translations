# Frigate NVR, common — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/common.json`
- Målkomponent: Hosted Weblate `frigate-nvr/common`, svenska
- Omfattning: 13 tidigare tomma och 2 osäkra UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 15 av 266 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval

Kommandomenyn följer befintliga Frigate-namn: **Live**, **Granska** och
**Utforska**. Tidigare ofullständiga `Health and Metrics` och `Logs` har
granskats i sin systemmenykontext.

## Kontroller

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 15`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten rapporterar 266 av 266 översatta strängar och 0
fuzzy. En kontroll återstår på navigationsnamnet `Live`, som medvetet är
identiskt med källtexten enligt befintlig Frigate-terminologi. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
