# Weblate Documentation — svensk granskningsbatch 096

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- språkspecifika behörigheter, förslag och direktredigering
- servermått, uppgifter, tillägg och skyddade autentiseringsuppgifter
- kodvärdstjänster, webbkrokar och matchning av förråd
- filsystemlatens och driftsättningskontroller

Bidragsgivarnamn har medvetet bevarats oförändrade. UI-namn, behörighetsnamn, API-rutter, kommandon, inställningar och kod har bevarats exakt. Terminologin använder bland annat *språkavgränsade grupper*, *webbkrok*, *förråd*, *driftsättning* och *adressbindning*.

## Lokal granskning

Varje enhet har granskats mot sin behörighets-, integrations- eller driftsättningskontext. Skillnaden mellan automatisk accept, direktredigering och förslagsröstning har bevarats, liksom innebörden av konfigurations- och säkerhetsinstruktionerna.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
