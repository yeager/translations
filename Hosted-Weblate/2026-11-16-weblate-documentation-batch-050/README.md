# Weblate Documentation — svensk granskningsbatch 050

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

Tjugo dokumentationsenheter har granskats rad för rad och sparats i Hosted Weblate med dess REST API:

- översättningsminne, PO/POT-huvuden och maskinöversättning
- Gerrit, Git, Python-wheel-paket, Engage och RSS
- hotmodell, XSS-skydd, URL-hälsokontroll och webbkrokar
- pluralformler, OpenSSH/Borg och återställning av projektsäkerhetskopior

## Lokal granskning

reST-roller, kommandon, kodvärden, CVE- och GHSA-referenser, produktnamn och filformat har bevarats. Terminologi följer den projektspecifika listan, bland annat *översättningsminne*, *förråd*, *webbkrok*, *gren*, *säkerhetskopia* och *platshållare*.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

Ändringarna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
