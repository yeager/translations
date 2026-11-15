# Frigate NVR, views-classificationmodel — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/classificationModel.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-classificationmodel`, svenska
- Omfattning: 19 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 19 av 141 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Kontroller

- `jq empty`: godkänd
- platshållaruppsättning bevarad: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 19`, `skipped: 0`, `not_found: 0` och
`result: true`. En senare avläsning hittade ett kontrollfel för en extra punkt
i en meddelandetext; det korrigerades via Weblates enhets-API. Komponenten
rapporterar nu 141 av 141 översatta strängar, 0 fuzzy och 0 fallerande
kontroller. Upstreamläge: inskickat och mottaget; separat projektgranskning
eller release är inte verifierad.
