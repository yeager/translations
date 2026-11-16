# Weblate Documentation — svensk granskningsbatch 045

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- beroendeversioner, ALTCHA och säkerhetsfixar för Markdown och API
- kalenderversionering, utgåvor och uppgraderingspolicy
- licenser, typkontroll och uv/PyCharm-utvecklingsmiljö
- PO-huvuden, MDX och personuppgiftsbehandling

## Lokal granskning

reST-roller, kommandon, kodvärden, CVE- och GHSA-referenser, licensbeteckningar, filformat och produktnamn har bevarats. En grammatisk avvikelse i den första sparningen av PO-raden korrigerades och verifierades via API innan arkivering.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
