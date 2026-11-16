# Weblate Documentation — svensk granskningsbatch 026

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Sju dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. Samtliga är bidragsgivarlistor med personnamn och användarnamn och behålls därför avsiktligt identiska med källtexten.

## Lokal granskning

Varje enhet innehåller enbart namn eller användarnamn. Oförändrad måltext är här korrekt och inte en oöversatt text eller ett QA-fel.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
