# Audacity: timer- och spårdialoger, batch 20

Datum: 2026-11-13

30 svenska PO-poster har granskats rad för rad i källkontext. Batchen omfattar
metadataredigeraren, timerinspelning, skärmläsarstatus för spår, kalibrerings-
dialogen och välkomsttexten.

Kontroller före arkivering och inskick:

- `msgfmt --check --statistics`: godkänd, 4 443 översatta meddelanden.
- `git diff --check`: godkänd.
- avgränsad Hunspell-sv: endast godtagna produktnamn, förkortningar och formatfält.
- `l10n-lint` och `svlang`: körda; deras återstående träffar gäller äldre kataloginnehåll utanför batchen.
- Gitleaks: godkänd, inga hemligheter hittades.

Patchen har skickats till den befintliga upstream-PR:n #12759. PR:n är fortsatt
öppen och inväntar upstreamgranskning; detta är inte en merge-verifiering.
