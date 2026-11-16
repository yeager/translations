# Weblate Documentation — svensk granskningsbatch 078

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De behandlar HTML-kontroller, Git, komponentdiagnostik, Markdown, MDX, YAML, TBX och projektbackup.

## Lokal granskning

reST-referenser, kod, flaggor, filformat, protokoll, API-namn och produktnamn har bevarats. Terminologi följer projektets säkerhets- och filformatskontext.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
