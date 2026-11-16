# Weblate Documentation — svensk granskningsbatch 031

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- riktlinjer för översättningsarbetsflöde, kontakt och leverans
- AsciiDoc-tabeller samt kommandoradsargument och miljövariabler
- översättningsstatusar och granskning av käll- och mallsträngar
- säkerhetsbegränsningar för projektwebbplatser
- RST-utdrag och genererade dokumentationsfiler

Personnamnet *Jane Done* är medvetet oförändrat.

## Lokal granskning

reST-roller, inställningsnamn, filnamn, URL:er och kodnamn har bevarats. Terminologi följer den projektspecifika listan, bland annat *källsträng*, *mallsträng*, *väntar på granskning*, *projektwebbplats* och *testförråd*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
