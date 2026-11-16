# Weblate Documentation — svensk granskningsbatch 064

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De beskriver arbetsytors åtkomstkontroll och fakturering samt funktionsnyheter för aviseringar, skärmbilder, SBOM, inbjudningar och Gettext POT.

## Lokal granskning

reST-referenser, UUID, API-fält, produktnamn, filformat och synliga UI-namn har bevarats eller översatts i sitt gränssnittssammanhang.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
