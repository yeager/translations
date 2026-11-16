# Weblate Documentation — svensk granskningsbatch 043

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- GitHub- och GitLab-autentisering samt pull- och sammanslagningsbegäranden
- tillåtelselistor för fjärrresurser och värdnamnsvalidering
- ALTCHA/Argon2id, körbara hjälpfiler och cachekataloger
- leverantörsspecifika instruktioner och aviseringar för kodvärdar

## Lokal granskning

Produktnamn, API-värdar, inställningsnamn, kodvärden, reST-roller och referensmål har bevarats. Terminologi följer den projektspecifika listan, bland annat *pullbegäran*, *sammanslagningsbegäran*, *förråd*, *webbkrok*, *grupp* och *API*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
