# Frigate NVR, views-chat — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/chat.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-chat`, svenska
- Omfattning: 66 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 66 av 66 strängar.

## Språkval

Komponenten använder **chatt**, **händelse**, **observation**, **kamera** och
**semantisk sökning**. Frigates produktnamn och platshållarna `{{tools}}`,
`{{count}}`, `{{label}}`, `{{camera}}`, `{{eventId}}`, `{{tokens}}`,
`{{rate}}` och `{{tool}}` är oförändrade.

## Kontroller

- `jq empty`: godkänd
- nyckelstruktur jämförd med engelsk källfil: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 66`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 66 av 66
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; någon separat projektgranskning eller release är ännu
inte verifierad.
