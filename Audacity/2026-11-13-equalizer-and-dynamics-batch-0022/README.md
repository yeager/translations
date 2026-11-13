# Audacity: equalizer och dynamik, batch 22

Datum: 2026-11-13

24 svenska PO-poster har granskats rad för rad i källkontext. Batchen omfattar
equalizerkurvor, kompressorns nivåreglage, normalisering av ljudstyrka och
brusreducering.

Kontroller före arkivering och inskick:

- `msgfmt --check --statistics`: godkänd, 4 443 översatta meddelanden.
- `git diff --check`: godkänd.
- avgränsad Hunspell-sv: endast godtagna facktermer, förkortningar och formatfält.
- Gitleaks: godkänd, inga hemligheter hittades.

Patchen är pushad till den öppna upstream-PR:n #12759. Den inväntar fortfarande
obligatorisk upstreamgranskning och är inte mergad.
