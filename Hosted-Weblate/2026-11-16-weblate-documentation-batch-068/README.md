# Weblate Documentation — svensk granskningsbatch 068

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De täcker inställningsarv för arbetsytor, projekt och kategorier, versionsnyheter samt språkspecifika instruktioner.

## Lokal granskning

reST-referenser, JSON, produktnamn, kod, namnlistor och synliga UI-namn har bevarats. Terminologi följer projektets kontext för arbetsytor och ärvda inställningar.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
