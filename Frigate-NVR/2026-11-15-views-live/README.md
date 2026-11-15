# Frigate NVR, views-live — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/live.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-live`, svenska
- Omfattning: 36 tidigare tomma UI-strängar
- Status: inskickad och mottagen i Hosted Weblate. Importen accepterade 36 av 130 nycklar; övriga nycklar var redan översatta och lämnades oförändrade.

## Språkval och kontroller

**Live**, **tvåvägsljud**, **strömningsteknik**, **låg bandbredd** och
**felsökningsläge** används konsekvent. Protokoll, codec-namn, IP:port och
go2rtc-sökvägen är oförändrade.

- `jq empty`: godkänd
- platshållaruppsättning jämförd med engelskan: godkänd
- `l10n-lint`: godkänd
- `git diff --check`: godkänd
- `gitleaks detect --no-git --source … --redact`: godkänd, inga läckor

## Upstream-verifiering

Weblates API-import svarade `accepted: 36`, `skipped: 0`, `not_found: 0` och
`result: true`. Komponenten rapporterar 130 av 130 översatta strängar och 0
fuzzy. Kontrollträffarna för `Live - Frigate`, `WebRTC` och `JSMpeg` är
medvetna falska positiva eftersom produkt- och tekniknamnen ska vara
oförändrade. Upstreamläge: inskickat och mottaget; separat projektgranskning
eller release är inte verifierad.
