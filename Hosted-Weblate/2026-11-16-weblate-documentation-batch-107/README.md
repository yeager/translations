# Weblate Documentation — svensk granskningsbatch 107

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- Celery-arbetarlägen, köer och minnesanvändning
- offentlig delning av projekt och statuswidgetar
- granskningsstyrda översättningar och incheckningspolicy
- språkvisa arbetsflöden, massredigering och sena incheckningar

Miljövariabler, UI-namn, policyreferenser, kommandon och reST-markering har bevarats exakt. Terminologin använder bland annat *prefork-arbetare*, *uppgiftskö*, *offentlig delning*, *begränsad komponent*, *granskning* och *incheckningspolicy*.

## Lokal granskning

Varje enhet har granskats mot sin drift- eller användargränssnittskontext. Översättningarna behåller särskilt skillnaden mellan sparade redigeringar, godkännande, filskrivning, incheckning och push.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
