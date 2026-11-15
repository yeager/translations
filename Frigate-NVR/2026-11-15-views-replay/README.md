# Frigate NVR, views-replay — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/replay.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-replay`, svenska
- Omfattning: 46 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 46 av 46 strängar.

## Språkval

**Felsökningsuppspelning** används konsekvent för *Debug Replay* och
**uppspelningskamera** för *replay camera*. Terminologin skiljer mellan
inspelning, uppspelning, objekt, detektering och spårning.

## Kontroller

- `jq empty`: godkänd
- nyckelstruktur jämförd med engelsk källfil: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 46`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 46 av 46
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
