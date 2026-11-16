# Weblate Documentation — svensk granskningsbatch 034

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- återställning av väntande översättningar och felhantering
- PostgreSQL 18, Docker-volymer och `PGDATA`
- NGINX:s IPv6-lyssnare och juridiska dokumentmallar
- RST-utdrag, lösenordsåterställning och översättningsminnets API
- versionsexponering, Markdown-kontroller och URL-skydd för Docker

## Lokal granskning

Konfigurationsvärden, filsystemssökvägar, miljövariabler, reST-roller, URL:er och kodnamn har bevarats. Terminologi följer den projektspecifika listan, bland annat *förråd*, *projektwebbplats*, *webbkrok*, *översättningsminne* och *säkerhetskopia*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
