# Weblate Documentation — svensk granskningsbatch 076

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De behandlar Helm, Weblate Client, Docker, releaseattesteringar, SBOM, kontrollsummor och andra releasekanaler.

## Lokal granskning

reST-referenser, filnamn, produktnamn, Helm, Docker, GitHub, PyPI, SBOM, Cosign, CycloneDX, Syft och BuildKit har bevarats. Terminologi följer release- och leveranskedjekontexten.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
