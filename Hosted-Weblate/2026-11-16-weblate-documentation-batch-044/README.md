# Weblate Documentation — svensk granskningsbatch 044

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- kodvärdsaviseringar och överföringsalternativ
- uppgraderingsvägar, Docker Compose och cachekataloger
- testsvit, Celery och Borg-säkerhetskopior
- SBOM, översättningssidan, projektåtkomst och API-token
- registrerings-CAPTCHA, språkteam och kalenderversionering

## Lokal granskning

Kommandon, inställningsnamn, filsystemssökvägar, reST-roller, kodvärden, produktnamn och filformatsparametrar har bevarats. Terminologi följer den projektspecifika listan, bland annat *förråd*, *grupp*, *säkerhetskopia*, *översättningsminne* och *API*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
