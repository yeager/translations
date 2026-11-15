# Frigate NVR, objects — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/objects.json`
- Målkomponent: Hosted Weblate `frigate-nvr/objects`, svenska
- Omfattning: 11 tidigare tomma objektnamn
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 11 av 129 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval och kontroller

Egennamnen **Canada Post** och **Royal Mail** är oförändrade. Övriga etiketter
är svenska vanliga namn på detekterade föremål och djur.

- `jq empty`: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 11`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten rapporterar 129 av 129 översatta strängar och 0
fuzzy. Kontrollerna för `Royal Mail` och `Skunk` är medvetna falska positiva:
egennamnet respektive det svenska djurnamnet är korrekt identiskt med
källtexten. Upstreamläge: inskickat och mottaget; separat projektgranskning
eller release är inte verifierad.
