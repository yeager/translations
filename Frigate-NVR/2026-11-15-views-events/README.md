# Frigate NVR, views-events — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/events.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-events`, svenska
- Omfattning: 26 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 26 av 68 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval och kontroller

**Rörelsesökning**, **rörelseförhandsvisning**, **tidslinje**, **bildruta** och
**nedtoning** används konsekvent med tidigare Frigate-batcher.

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 26`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 68 av 68
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
