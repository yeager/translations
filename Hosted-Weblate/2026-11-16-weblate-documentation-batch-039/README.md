# Weblate Documentation — svensk granskningsbatch 039

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- tillägg, maskinöversättning och reStructuredText-kontroller
- komponentidentifiering och språkvarianter baserade på filnamn
- granskningslogg, WLC-konfiguration och Docker-uppladdningsgränser
- webbkrokars värdnamnsvalidering och översättningsminnets UI
- tre bidragsgivarlistor med avsiktligt oförändrad måltext

## Lokal granskning

reST-roller, malluttryck, filnamn, miljövariabler, kodvärden och UI-namn har bevarats. Terminologi följer den projektspecifika listan, bland annat *tillägg*, *granskningslogg*, *webbkrok*, *översättningsminne* och *förråd*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
