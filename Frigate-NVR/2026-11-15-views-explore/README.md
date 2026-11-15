# Frigate NVR, views-explore — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/explore.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-explore`, svenska
- Omfattning: 8 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 8 av 145 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval och kontroller

**Felsökningsuppspelning** följer `views-replay`; **spårat objekt** och
**poäng** används för Frigates detekteringsdata.

- `jq empty`: godkänd
- platshållaruppsättning bevarad: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 8`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 145 av 145
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
