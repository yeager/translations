# Weblate Documentation — svensk granskningsbatch 038

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- POT-uppdatering, OCR och komponentvalidering
- REST API, Docker och Keycloak
- autogenererad dokumentation, cacheminne och exporterade förråd
- säkerhetsåtgärder för symlänkar, SSRF, URL-omdirigeringar, webbkrokar och projektbackup

## Lokal granskning

reST-roller, miljövariabler, kodidentifierare, CVE- och GHSA-referenser samt produktnamn har bevarats. Terminologi följer den projektspecifika listan, bland annat *förråd*, *webbkrok*, *översättningsminne*, *grupp* och *säkerhetskopia*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
