# Weblate Documentation — svensk granskningsbatch 053

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API. De beskriver hotmodellens:

- betrodda gränser och sådant som ligger utanför modellens ansvar
- säkerhetsfynd för webb, API, behörigheter, VCS, säkerhetskopior och bakgrundsuppgifter
- driftsättningsförutsättningar för databas, datalager, HTTPS och proxy

## Lokal granskning

reST-roller, inställningsnamn, kommandon, produktnamn och bevismarkörer har bevarats. Terminologi följer den projektspecifika listan och etablerad svensk säkerhetsterminologi.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
