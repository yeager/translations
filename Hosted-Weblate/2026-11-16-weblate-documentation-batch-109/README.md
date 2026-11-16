# Weblate Documentation — svensk granskningsbatch 109

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- ordlistor, incidentrapportering och granskningsloggar
- Celery-, Docker- och minnesprestanda
- autentiseringsappar, Borg-säkerhetskopior och fontbegränsningar
- MDX, DeepL, REST API och automatisk översättning

API-rutter, UI-namn, produktnamn, konfigurationsreferenser, fältnamn och reST-markering har bevarats exakt. Terminologin använder bland annat *diagnostik*, *granskningslogg*, *driftsättningskontroll*, *engångskod*, *självstängande* och *begärandetext*.

## Lokal granskning

Varje enhet har granskats mot utgåve- och säkerhetskontexten. Översättningarna bevarar att offentlig delning är begränsad, att känsliga lösenfraser rensas ur felrapporter och att API-schemat beskriver faktiska fält.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
