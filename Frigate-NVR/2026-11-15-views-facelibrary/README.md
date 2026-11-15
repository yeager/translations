# Frigate NVR, views-facelibrary — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/faceLibrary.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-facelibrary`, svenska
- Omfattning: 6 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 6 av 60 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Kontroller

- `jq empty`: godkänd
- platshållaruppsättning bevarad: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 6`, `skipped: 0`, `not_found: 0` och
`result: true`. Direkt efter importen rapporterade komponenten 60 av 60
översatta strängar, 0 fuzzy och 0 fallerande kontroller. Upstreamläge:
inskickat och mottaget; separat projektgranskning eller release är inte
verifierad.
