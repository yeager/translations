# Weblate Documentation — svensk granskningsbatch 092

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- Granian, WSGI och arbetsytans översättningsminne
- arbetsytestatistik, projektmått och granskningslogg
- visuella tillgänglighetsförbättringar och lösenordsautentisering
- Git-omdirigeringar, GitHub-webbkrokar och SSH-säkerhet

Synliga UI-namn, API-sökvägar, inställningsnycklar, protokoll och reST-markering har bevarats. Terminologi har normaliserats till bland annat *arbetsyta*, *översättningsminne*, *granskningslogg*, *webbkrok*, *förråd* och *adressbindning*.

## Lokal granskning

Varje enhet har granskats mot dess administrativa eller tekniska dokumentationskontext. Texterna skiljer mellan användaråtgärder, behörighetsstyrning och säkerhetsmekanismer utan att ändra exakta konfigurationsvärden.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
