# Weblate Documentation — svensk granskningsbatch 041

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- typade tilläggskonfigurationer och normaliserad JSON
- exportkontroll, ECCN, BIS och EAR
- LTEngine och ordlisteunderhåll
- offentliga profil-URL:er, Docker-uppladdningsgränser och pluralsträngar
- sammanslagningsbegäranden, filformatsflaggor och administratörsåtgärder

## Lokal granskning

Lagrum, myndighetsnamn, standardbeteckningar, kodidentifierare, filformat och UI-etiketter har bevarats där de är tekniska namn. Terminologi följer den projektspecifika listan, bland annat *ordlistepost*, *förråd*, *sammanslagningsbegäran*, *granskningslogg* och *översättningstjänst*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
