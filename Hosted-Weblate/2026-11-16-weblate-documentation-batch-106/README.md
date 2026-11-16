# Weblate Documentation — svensk granskningsbatch 106

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- WLC:s ursprungsavgränsade HTTP- och TLS-undantag
- schemalagda förrådsuppdateringar och API-hastighetsbegränsning
- uWSGI, Celery-prefork och minnesanvändning
- Docker-varningar, betrodda proxyer och konfigurationsrapporter

Miljövariabler, intervallsyntax, inställningsnycklar, kommandon, kod och reST-markering har bevarats exakt. Terminologin använder bland annat *ursprung*, *hastighetsbegränsning*, *arbetskopia*, *prefork*, *betrodd proxy* och *konfigurationsvarning*.

## Lokal granskning

Varje enhet har granskats mot sin säkerhets- eller driftsättningskontext. Översättningarna bevarar räknelogik, prioritetsordning för begränsningar och gränserna för osäker HTTP- och TLS-hantering.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
