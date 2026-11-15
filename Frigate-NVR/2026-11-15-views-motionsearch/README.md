# Frigate NVR, views-motionsearch — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/motionSearch.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-motionsearch`, svenska
- Omfattning: 64 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 64 av 64 strängar.

## Språkval

**Rörelsesökning**, **intresseområde**, **rörelseförändring**, **värmekarta**
och **bildruta** används konsekvent. Pluralformerna följer den svenska
i18next-strukturen och platshållarna är oförändrade.

## Kontroller

- `jq empty`: godkänd
- nyckelstruktur jämförd med engelsk källfil: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 64`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 64 av 64
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
