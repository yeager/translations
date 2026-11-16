# Weblate Documentation — svensk granskningsbatch 103

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- hotmodell för Weblate Client och VCS-infrastruktur
- tillåtelselistor, GitHub App och behörighetsgränser
- återställning av förråd och hantering av Git-undermoduler
- granskningslogg, lagringstid och risker med alltför breda roller

Behörighetsnamn, inställningsnycklar, API- och VCS-identifierare, URL:er samt reST-markering har bevarats exakt. Terminologin använder bland annat *förtroendegräns*, *tillåtelselista*, *granskningsspår*, *lagringstid* och *begränsad komponent*.

## Lokal granskning

Varje enhet har granskats mot den aktuella hotmodellens säkerhetskontext. Översättningarna bevarar bedömningarnas räckvidd, förutsättningar och skillnaden mellan säkerhets-, integritets- och korrekthetspåverkan.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
