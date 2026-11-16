# Weblate Documentation — svensk granskningsbatch 112

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- utvecklingsprofiler, ordlistor och rapportbehörighet
- språkbegränsningar och översättningsarbetsflöde
- incidenthantering och rapportering av produktsäkerhet
- CRA-begrepp, riskklassificering och rapporteringsfrister

Behörighetsnamn, UI-namn, kommandon, inställningsreferenser, rättsreferenser och reST-markering har bevarats exakt. Terminologin använder bland annat *rapportomfång*, *begränsad komponent*, *aktivt utnyttjande*, *incidentanteckning* och *slutrapport*.

## Lokal granskning

Varje enhet har granskats mot dess behörighets-, säkerhets- eller incidentkontext. Översättningarna skiljer tydligt mellan sårbarhet, aktivt illasinnat utnyttjande och allvarlig produktsäkerhetsincident utan att ändra den regulatoriska innebörden.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
