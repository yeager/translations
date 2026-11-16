# Weblate Documentation — svensk granskningsbatch 110

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- navigering, felrapportering, Celery och Borg-säkerhetskopiering
- offentlig projektdelning och autentiseringsappar
- utvecklingscontainer, Docker Compose och Git-arbetsträd
- testmiljöer, profiler, cacheminnen och livscykel för containrar

Miljövariabler, filvägar, kommandon, UI-namn, verktygsnamn och reST-markering har bevarats exakt. Terminologin använder bland annat *utvecklingscontainer*, *utcheckning*, *arbetsträd*, *programprofil*, *bootstrap* och *kombinerad arbetare*.

## Lokal granskning

Varje enhet har granskats mot sin utvecklar- eller driftkontext. Översättningarna bevarar isoleringen mellan utcheckningar, begränsningar för åtkomst till data och skillnaden mellan att stoppa en miljö och ta bort dess källfiler.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
