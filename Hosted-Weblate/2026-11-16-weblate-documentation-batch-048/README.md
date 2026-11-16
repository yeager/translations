# Weblate Documentation — svensk granskningsbatch 048

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- kodvärdsspecifika pull-, sammanslagnings- och granskningsbegäranden
- Docker-gränser vid import av projektsäkerhetskopior
- källdistributioner, Python-wheel-paket och exempelkonfigurationer
- Gettext-pluralformler och CDN-tillägg

## Lokal granskning

reST-roller, miljövariabler, filsystemssökvägar, operatorer, kodvärden och produktnamn har bevarats. Den initiala formuleringen *Python-hjul* ersattes med det etablerade tekniska uttrycket *Python-wheel-paket* innan API-läsningen och arkiveringen.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
