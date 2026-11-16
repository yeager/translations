# Weblate Documentation — svensk granskningsbatch 040

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- personligt, projekt- och instansomfattande översättningsminne
- import, export, rensning och behörighetsstyrning av minnesposter
- skärmbilder i användargränssnitt, förråd och REST API
- värdnamnsvalidering, SSH-värdnycklar, TMX och granskningsframsteg
- tilläggskonfiguration i JSON

## Lokal granskning

UI-etiketter, reST-roller, API-sökvägar, filformat, JSON- och klassidentifierare har bevarats. Terminologi följer den projektspecifika listan, bland annat *översättningsminne*, *förråd*, *källsträng*, *granskningslogg* och *webbkrok*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
