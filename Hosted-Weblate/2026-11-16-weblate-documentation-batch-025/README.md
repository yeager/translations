# Weblate Documentation — svensk granskningsbatch 025

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Sex dokumentationsenheter har granskats rad för rad och översatts i Hosted Weblate med dess REST API:

- administration av projektgrupper och behörigheter via API:t
- tilläggslista och säkerhetsrådgivning
- enspråkig CSV och källkolumnen
- argumentinjektion i administrationskonsolen
- två bidragsgivarlistor

Bidragsgivarlistorna är avsiktligt identiska med källtexten eftersom de består av namn och användarnamn.

## Lokal granskning

Formatering och reST-roller har bevarats. Terminologi följer den projektspecifika ordlistan, bland annat *tillägg*, *projektadministratör*, *användarbehörighet* och *API:t*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
