# Weblate Documentation — svensk granskningsbatch 102

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- fakturering, översättningsflaggor och tvåfaktorsautentisering
- projektsäkerhetskopior, API-token och begränsade komponenter
- LLM-baserad maskinöversättning och REST API-förbättringar
- SPDX-licensdata samt Weblate Python-klientens API-objekt

Bidragsgivarnamn, API-anrop, fältnamn, klassnamn, kod, filnamn och reST-markering har bevarats exakt. Terminologin använder bland annat *granskningslogg*, *översättningsminne*, *tillåtelselista*, *tvåfaktorsautentisering* och *uppgifts-URL*.

## Lokal granskning

Varje enhet har granskats mot sin säkerhets-, API- eller utvecklarkontext. Översättningarna bevarar både exakta API-värden och säkerhetsreglerna för token, återställning och begränsade komponenter.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
