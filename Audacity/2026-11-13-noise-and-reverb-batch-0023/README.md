# Audacity: brus och efterklang, batch 23

Datum: 2026-11-13

29 svenska PO-poster har granskats rad för rad i källkontext. Batchen omfattar
brusreducering, Paulstretch, Phaser, Reparera och efterklang.

Kontroller före arkivering och inskick:

- `msgfmt --check --statistics`: godkänd, 4 443 översatta meddelanden.
- `git diff --check`: godkänd.
- avgränsad Hunspell-sv: endast godtagna signalbehandlingstermer, produktnamn och kortkommandobokstäver.
- Gitleaks: godkänd, inga hemligheter hittades.

Patchen är pushad till Audacitys öppna upstream-PR #12759. PR:n inväntar
obligatorisk upstreamgranskning och är inte mergad.
