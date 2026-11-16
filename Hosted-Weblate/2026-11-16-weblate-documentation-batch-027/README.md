# Weblate Documentation — svensk granskningsbatch 027

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Fem dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. Enheterna är bidragsgivarlistor med personnamn och användarnamn, och har därför avsiktligt samma måltext som källtexten.

## Lokal granskning

Oförändrad måltext är korrekt för dessa namnlistor och innebär inte en oöversatt text eller ett QA-fel.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
