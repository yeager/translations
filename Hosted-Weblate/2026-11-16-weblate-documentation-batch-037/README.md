# Weblate Documentation — svensk granskningsbatch 037

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- villkorliga kontroller för Java MessageFormat och HTML
- länkade förrådskomponenter och interna URL:er
- rensning, granskning och nivåer i översättningsminnet
- Celery-arbetsköer, tilläggshantering och språkfiler
- Git, SSH, Borg-säkerhetskopior och värdnycklar

## Lokal granskning

Kvalitetskontroller, reST-roller, inställningsnamn, kommandon, kodvärden och UI-namn har bevarats. Terminologi följer den projektspecifika listan, bland annat *översättningsminne*, *förråd*, *incheckning*, *ombasering*, *värdnyckel* och *säkerhetskopia*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
