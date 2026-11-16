# Weblate Documentation — svensk granskningsbatch 091

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- utgåveanteckningar om statistik, Mercurial och förslag
- juridiska dokument och grafiska förhandsvisningar
- GitHub-appar, webbkrokar och nätverksskydd
- proxyer, certifikat, ASGI/WSGI och systemd

Inställningsnycklar, miljövariabler, HTTP-huvuden, sökvägar, programnamn och reST-markering har bevarats. Terminologi har normaliserats till bland annat *webbkrok*, *förråd*, *driftsättning*, *certifikatutfärdare* och *utgående trafik*.

## Lokal granskning

Varje enhet har granskats mot den administrativa och tekniska dokumentationskontexten. Översättningarna särskiljer exakta konfigurationsvärden från den förklarande svenska texten och behåller säkerhetsinnebörden för anslutnings- och nätverksinställningar.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
