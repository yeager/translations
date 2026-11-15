# Frigate NVR, components-player — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/components/player.json`
- Målkomponent: Hosted Weblate `frigate-nvr/components-player`, svenska
- Omfattning: 15 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 15 av 37 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Kontroller

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 15`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten rapporterar 37 av 37 översatta strängar och 0
fuzzy. En kontroll återstår på `{{codec}} {{rate}} kHz`: den är en medveten
falsk positiv eftersom codec, frekvensen och enheten ska vara identiska med
källtexten. Upstreamläge: inskickat och mottaget; separat projektgranskning
eller release är inte verifierad.
