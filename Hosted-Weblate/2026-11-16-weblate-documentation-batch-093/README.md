# Weblate Documentation — svensk granskningsbatch 093

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- Git LFS och mått för översättningsförlopp
- översättningsspridning och Qt Linguist-filformat
- dokumenterad driftsättning samt nätverks- och VCS-säkerhet
- kontroller av AsciiDoc-märkning och högsta antal rader

Kodexempel, filändelser, platsmarkörer, protokoll, inställningsnamn och AsciiDoc-syntax har bevarats. Terminologin använder bland annat *översättningsspridning*, *lokaliseringsformat*, *förråd*, *adressbindning* och *genomsläpp*.

## Lokal granskning

Varje enhet har granskats i dokumentationskontexten. Svenska förklaringar har skilts från exakta tekniska strängar för att inte ändra format, konfiguration eller kontrolllogik.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
