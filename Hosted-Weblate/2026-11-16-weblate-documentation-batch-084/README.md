# Weblate Documentation — svensk granskningsbatch 084

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De behandlar Git-återställning, API-klienter, GitHub-integrering, CI, åtkomstkontroll och säkerhetsfixar.

## Lokal granskning

reST-referenser, kod, URL:er, CVE/GHSA-ID:n, protokoll, miljövariabler, produktnamn och namnlistor har bevarats. Terminologi följer säkerhets- och integrationskontexten.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
