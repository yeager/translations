# Weblate Documentation — svensk granskningsbatch 073

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De behandlar kod- och behållarskanning, externa säkerhetspolicyer, säkerhetsstyrning och status för formell utvärdering.

## Lokal granskning

reST-referenser, förkortningar, produktnamn, SARIF, SBOM, GitHub, FOSSA, Renovate, Dependabot och Trivy har bevarats. Terminologi följer säkerhetskontexten.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
