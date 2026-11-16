# Weblate Documentation — svensk granskningsbatch 033

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De beskriver förrådsunderhåll i Weblate, bland annat:

- synkronisering med uppströms och överföring av incheckade översättningar
- sammanslagning, ombasering och bevarande av linjär historik
- låsning, återställning och rensning av lokala förråd
- återskrivning och import av översättnings- och förrådsfiler

## Lokal granskning

Git- och Weblate-terminologi följer den projektspecifika listan: *förråd*, *uppströms*, *incheckning*, *sammanslagning*, *ombasering*, *gren* och *översättningstjänst*. Referensen :ref:`component-new_base` har bevarats oförändrad.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
