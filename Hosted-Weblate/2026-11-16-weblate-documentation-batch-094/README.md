# Weblate Documentation — svensk granskningsbatch 094

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- rad- och formatkontroller samt nedladdningsformat
- SSH-nyckelsökning, HTTP-omdirigeringar och adressbindning
- juridiska dokument i Docker och arbetsytans filhantering
- användar- och komponent-API, bakgrundsarbete och arbetsytefunktioner

Synliga UI-namn, API-rutter, inställningsnycklar, kod, filnamn och reST-markering har bevarats. Terminologin använder bland annat *arbetsyta*, *översättningsminne*, *förråd*, *adressbindning* och *juridiska dokument*.

## Lokal granskning

Varje enhet har granskats mot dess UI-, API- eller driftsättningskontext. Säkerhets- och behörighetsinnebörd har bevarats, medan instruktionerna har skrivits idiomatiskt på svenska.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
