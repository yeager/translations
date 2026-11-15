# Frigate NVR, config-groups — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/config/groups.json`
- Målkomponent: Hosted Weblate `frigate-nvr/config-groups`, svenska
- Omfattning: 24 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 24 av 25 nycklar; den återstående nyckeln var redan översatt och lämnades oförändrad.

## Språkval och kontroller

Grupprubrikerna skiljer konsekvent mellan globala inställningar och
kamerainställningar. `FFmpeg` är oförändrat som produktnamn.

- `jq empty`: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 24`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 25 av 25
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
