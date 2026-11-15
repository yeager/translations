# Frigate NVR, config-global — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/config/global.json`
- Målkomponent: Hosted Weblate `frigate-nvr/config-global`, svenska
- Omfattning: 28 tidigare tomma globala konfigurationssträngar
- Status: inskickad och mottagen i Hosted Weblate.

## Språkval och verifiering

Batchen omfattar GenAI, ljud och Birdseye. API-/produktnamn, roller,
miljövariabler och RTSP bevaras där de är tekniska värden.

Weblates import svarade `accepted: 28`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten står därefter på 579 av 775 översatta strängar,
0 fuzzy och två dokumenterade falska positiva kontroller: `FFmpeg` och
`ONVIF-port`.

Kontroller: `jq empty`, `l10n-lint`, `git diff --check` och Gitleaks.

## Batch 002

Batchen för Birdseye-layout, FFmpeg, livevy, rörelse, objekt, inspelning och
granskningsinställningar accepterades med 20 av 775 nycklar. Komponenten står
därefter på 599 av 775 översatta strängar och 0 fuzzy. Kontrollträffarna för
`FFmpeg` och `ONVIF-port` är medvetna falska positiva tekniska namn och svensk
sammansättning.
