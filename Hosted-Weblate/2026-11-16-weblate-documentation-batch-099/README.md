# Weblate Documentation — svensk granskningsbatch 099

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- diagnostik och svar för generiska webbkroksuppdateringar
- VCS-parametrar, xgettext, Celery och Git-undermoduler
- Docker-proxyer och GitLab/GitHub-funktioner
- säkerhetsmodell, matchning och exponering i webbkroksflödet

HTTP-statuskoder, API-fält, UI-namn, inställningsnycklar, kod, URL:er och reST-markering har bevarats exakt. Terminologin använder bland annat *webbkroksändpunkt*, *förråd*, *matchningsdiagnostik*, *autentiserad integrering* och *adressbindning*.

## Lokal granskning

Varje enhet har granskats mot sin integrations- och säkerhetskontext. Särskilt har skillnaden mellan teknisk diagnostik, åtkomstkontroll och faktisk åtkomst till förrådsinnehåll bevarats.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
