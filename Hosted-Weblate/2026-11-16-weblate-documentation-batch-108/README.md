# Weblate Documentation — svensk granskningsbatch 108

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- målspråk, ordlistespråk och instansstatistik
- API-token och hastighetsbegränsning per användare, IP och nät
- betrodda proxyer och undantag från hastighetsbegränsning
- Docker-utveckling, sökresultat, aviseringar och översättningsstatistik

Headernamn, HTTP-status, inställningsnycklar, kod, API-referenser och reST-markering har bevarats exakt. Terminologin använder bland annat *målspråk*, *ordlistespråk*, *hastighetsbegränsning*, *betrodd proxy*, *åsidosättning* och *sökresultat*.

## Lokal granskning

Varje enhet har granskats mot språkhanterings-, API- eller utvecklarkontexten. Översättningarna bevarar prioritetsordningen mellan användar- och IP-regler, liksom att undantag inte ger utökad åtkomst.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
