# Weblate Documentation — svensk granskningsbatch 035

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- hotmodell, tvåfaktorsautentisering och återställning av översättningsfiler
- länkade förrådskomponenter, projektbackup och Git-exportör
- SSH, Git-grenar, felmaskering och Git LFS
- format, IPv6, interna URL:er och tilläggskrokar

## Lokal granskning

reST-roller, inställningsnamn, modulnamn, klassnamn, kommandon, kodnamn och API-värden har bevarats. Terminologi följer den projektspecifika listan, bland annat *förråd*, *gren*, *webbkrok*, *tillägg*, *källöversättning* och *uppströms*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
