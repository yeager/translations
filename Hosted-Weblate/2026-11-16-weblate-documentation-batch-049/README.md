# Weblate Documentation — svensk granskningsbatch 049

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Nitton dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- säkra CDN-inställningar, HTTP-rubriker, MIME-typer och cachelivslängder
- RSS-flöden, bidragsstatistik och skärmbilds-API
- registrering, Gitea/Forgejo, Engage-sidan och MDX
- LLM-översättningssammanhang för automatiska förslag

## Avgränsad QA-spärr

En tjugonde enhet om offentlig CDN-publicering (Weblate-enhet `190801159`) sparades på svenska, men Hosted Weblate placerar den i status 11 och visar ingen kontrollorsak via API:t. Den räknas därför **inte** som klar och ingår inte i denna batch. Övriga 19 enheter är lästa tillbaka som översatta och väntande på granskning.

## Lokal granskning

HTTP-rubriker, MIME-typer, reST-roller, API-sökvägar, sökfilter, produktnamn och kodvärden har bevarats. Terminologi följer den projektspecifika listan, bland annat *webbkrok*, *förråd*, *granskningslogg*, *översättningsminne* och *platshållare*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De nitton färdiga ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
