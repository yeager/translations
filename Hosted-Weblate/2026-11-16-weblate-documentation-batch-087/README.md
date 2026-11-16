# Weblate Documentation — svensk granskningsbatch 087

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De behandlar API-ändpunkter, rapporter, statiska tillgångar, OCR, Celery, PostgreSQL, REST-auktorisering och kodvärdskonton.

## Lokal granskning

reST-referenser, kod, API-namn, URL:er, produktnamn, UI-namn och tekniska begrepp har bevarats. Terminologi följer projektets administrations- och integrationskontext.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
