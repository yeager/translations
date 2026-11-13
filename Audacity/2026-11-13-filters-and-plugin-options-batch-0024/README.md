# Audacity: filter och insticksmodulsalternativ, batch 24

Datum: 2026-11-13

30 svenska PO-poster har granskats rad för rad i källkontext. Batchen omfattar
klassiska filter, ton- och tidsutsträckningseffekter samt inställningar för VST,
VST3, Audio Unit, LADSPA, LV2 och Nyquist.

Kontroller före arkivering och inskick:

- `msgfmt --check --statistics`: godkänd, 4 443 översatta meddelanden.
- `git diff --check`: godkänd.
- avgränsad Hunspell-sv: endast formatnamn och godtagna facktermer.
- Gitleaks: godkänd, inga hemligheter hittades.

Patchen är pushad till Audacitys öppna upstream-PR #12759. PR:n inväntar
obligatorisk upstreamgranskning och är inte mergad.
