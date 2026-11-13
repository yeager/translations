# Audacity: tidslinje, start och makron

Tretton aktiva PO-poster har granskats rad för rad. Batchen rättar
huvudmenyåtgärden ”Ny”, svenska sling- och rullningstermer samt naturligare
start-, återställnings- och makrotexter.

Källcommit: [`0f208ee`](https://github.com/yeager/audacity/commit/0f208ee).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, l10n-lint, svlang, diffkontroll och
Gitleaks passerade. l10n-lint har inga fel och 29 befintliga varningar utanför
batchen. En nordisk snabbtangent som l10n-lint avvisade i den första kontrollen
flyttades till `s` och är därmed åtgärdad. PR:n är öppen och inväntar
obligatorisk upstreamgranskning; den är inte mergad.
