# Frigate NVR, views-exports — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/exports.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-exports`, svenska
- Omfattning: 74 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 74 av 87 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval och kontroller

*Case* är konsekvent översatt som **ärende** och *export* som **export**.
Skillnaden mellan köade, pågående, kopierade, kodade och sammanfogade exporter
är bevarad i jobbstegen.

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 74`, `skipped: 0`, `not_found: 0` och
`result: true`. Tre kontrollträffar för extra punkter i statusmeddelanden
korrigerades via Weblates enhets-API. Komponenten rapporterar nu 87 av 87
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
