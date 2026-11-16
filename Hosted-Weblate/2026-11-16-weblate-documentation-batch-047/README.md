# Weblate Documentation — svensk granskningsbatch 047

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- webbvärdsregion, jurisdiktion, dataflöden och extern behandling
- transparens, registrerades rättigheter, lagringstid och personuppgiftsbiträden
- filformatsparametrar som avsiktligt behålls oförändrade
- konfiguration av GitHub- och GitLab-förrådsåtkomst

## Lokal granskning

Inställningsnamn, filformatsparametrar, reST-roller och produktnamn har bevarats. Terminologi följer den projektspecifika listan och svensk terminologi för integritet, bland annat *personuppgifter*, *granskningslogg*, *säkerhetskopia*, *förråd* och *spårbarhet*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
