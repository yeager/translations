# Weblate Documentation — svensk granskningsbatch 042

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- globala behörigheter, säkerhetskopior och OpenAPI-scheman
- komponentupptäckt, URL-validering och externa länkar
- Bootstrap-aviseringar, inbjudningar och tilläggskonfiguration
- Markdown, Forgejo, Gitea, ZIP-arkiv och uppladdningsgränser
- en bidragsgivarlista, en laghänvisning och ett filformatsvärde som avsiktligt behålls oförändrade

## Lokal granskning

UI-etiketter, reST-roller, malluttryck, inställningsnamn, CVE- och GHSA-referenser, API-termer och tekniska identifierare har bevarats. Terminologi följer den projektspecifika listan.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
