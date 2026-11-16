# Weblate Documentation — svensk granskningsbatch 062

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De täcker dispositioner i hotmodellen, aviserings- och ändringsfilter samt GitLab-, Google Cloud Error Reporting- och OpenTelemetry-konfiguration.

## Lokal granskning

reST-referenser, inställningsnamn, filteruttryck, kod, URL:er och produktnamn har bevarats. Terminologi följer den projektspecifika listan och etablerad svensk fackterminologi.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
