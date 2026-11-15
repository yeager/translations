# Frigate NVR, config-cameras — svensk granskningsbatch 002

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/config/cameras.json`
- Målkomponent: Hosted Weblate `frigate-nvr/config-cameras`, svenska
- Omfattning: 50 tidigare tomma konfigurationssträngar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 50 av 522 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval och kontroller

**Underström**, **lagringstid**, **detekteringsscen**, **bildruta**,
**transkodning**, **bithastighet** och **tvåvägsljud** följer tidigare
Frigate-batcher. Tekniknamn, roller, värden, go2rtc och `fps` är oförändrade.

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 50`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten rapporterar 522 av 522 översatta strängar och 0
fuzzy. Den enda kontrollträffen, `ONVIF-port`, är den dokumenterade falska
positiva svenska sammansättningen från den tidigare kontrollfixbatchen.
Upstreamläge: inskickat och mottaget; separat projektgranskning eller release
är inte verifierad.
