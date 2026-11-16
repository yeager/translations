# Weblate Documentation — svensk granskningsbatch 098

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- validering och adressbindning för VCS-förråd
- generiska och autentiserade webbkrokar för kodvärdar
- Docker, nginx, betrodda proxyer och klientadresser
- VCS-parametrar samt diagnostik för matchning av förråd och gren

Headernamn, miljövariabler, inställningsnycklar, API-fält, URL:er, kommandon och reST-markering har bevarats exakt. Terminologin använder bland annat *omvänd proxy*, *adressbindning*, *webbkroksändpunkt*, *förråd*, *nyttolast* och *betrodd infrastruktur*.

## Lokal granskning

Varje enhet har granskats mot sin säkerhets- och driftsättningskontext. Översättningarna bevarar särskilt kraven på betrodda proxyer, begränsningarna i generiska webbkrokar och åtkomstinformationens räckvidd.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
