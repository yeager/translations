# Weblate Documentation — svensk granskningsbatch 030

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- sex bidragsgivarlistor, med avsiktligt oförändrad måltext
- utvecklingsverktygen `translate-toolkit`, `prek` och `pre-commit`
- manuell filkontroll och delprojekt
- paketerade JavaScript-bibliotek, testförråd och tredjepartsberoenden
- visuell testning, kontroll av projektwebbplatser och statistiketiketter

## Lokal granskning

reST-roller, filnamn, URL:er och kodnamn har bevarats. Terminologi följer den projektspecifika listan, bland annat *testförråd*, *beroenden*, *projektwebbplats* och *avisering*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
