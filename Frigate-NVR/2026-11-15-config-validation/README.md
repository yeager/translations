# Frigate NVR, config-validation — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/config/validation.json`
- Målkomponent: Hosted Weblate `frigate-nvr/config-validation`, svenska
- Omfattning: 25 tidigare tomma valideringssträngar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 25 av 26 nycklar; den återstående nyckeln var redan översatt och lämnades oförändrad.

## Språkval

Valideringsmeddelandena använder konsekvent **värde**, **objekt**,
**indataström**, **roll**, **schema** och **maskinvaruacceleration**. Den
redan översatta nyckeln `minimum` berörs inte av deltafilen.

## Kontroller

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 25`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 26 av 26
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
