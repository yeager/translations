# Audacity: kommandon och effekter, batch 21

Datum: 2026-11-13

80 svenska PO-poster har granskats rad för rad i källkontext. Batchen omfattar
kommandogränssnittet, Auto Duck, kompressorreglage, DTMF, kontrastanalys,
förvrängningsförinställningar och equalizer.

Kontroller före arkivering och inskick:

- `msgfmt --check --statistics`: godkänd, 4 443 översatta meddelanden.
- `git diff --check`: godkänd.
- avgränsad Hunspell-sv: endast godtagna produktnamn, förkortningar och formatfält.
- `l10n-lint` och `svlang`: körda; återstående träffar gäller äldre kataloginnehåll utanför batchen.
- Gitleaks: godkänd, inga hemligheter hittades.

Patchen är pushad till Audacitys öppna upstream-PR #12759. PR:n inväntar
fortfarande obligatorisk upstreamgranskning och är inte mergad.
