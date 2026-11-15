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

## Batch 003

Batchen för ögonblicksbilder, ljudtranskribering och klassificeringsmodeller
accepterades med 30 av 775 nycklar. Komponenten står därefter på 629 av 775
översatta strängar och 0 fuzzy. De tre kontrollträffarna är oförändrade,
dokumenterade tekniska undantag.

## Batch 004

Batchen omfattar anpassad klassificering, semantisk sökning och
ansiktsigenkänning. Hosted Weblate accepterade 37 strängar; två redan
översatta nycklar behövde därför inte ändras. Komponenten står därefter på
666 av 775 översatta strängar och 0 fuzzy. De tre kvarvarande
kontrollträffarna är dokumenterade tekniska undantag: `FFmpeg`, `ONVIF-port`
och produktnamnet/formatet för nätverksstatistik.

Kontroller: `jq empty`, `l10n-lint`, plats- och tekniktokenjämförelse mot
källfilen, `git diff --check` och Gitleaks.

## Batch 005

Batchen omfattar LPR (registreringsskyltigenkänning) och kameragrupper.
Hosted Weblate accepterade samtliga 33 strängar. Komponenten står därefter på
699 av 775 översatta strängar och 0 fuzzy. De tre kvarvarande kontrollträffarna
är de dokumenterade tekniska undantagen `FFmpeg`, `ONVIF-port` och
nätverksstatistikens produktnamn/format.

Kontroller: `jq empty`, `l10n-lint`, plats- och tekniktokenjämförelse mot
källfilen, `git diff --check` och Gitleaks.
