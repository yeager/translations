# Weblate Documentation — svensk granskningsbatch 066

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De täcker översättningskostnader, Git-konflikter, SBOM och externa tjänster, åtkomst till privata förråd, skärmbildssökning samt standardvärden för meddelanden och juridiska dokument.

## Lokal granskning

reST-referenser, kod, filteruttryck, URL:er, SSH, API, Git, SBOM, produktnamn och formatnamn har bevarats. Terminologi följer projektets sammanhang.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
