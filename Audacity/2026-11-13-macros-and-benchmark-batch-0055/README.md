# Audacity: makron och prestandatest

Tolv aktiva PO-poster har granskats rad för rad. Batchen förbättrar makroernas
val och tillämpning, använder tekniskt korrekt term för slumptalsfrö och
förtydligar prestandatestets intervall, diskblock och felutskrifter.

Källcommit: [`0014c32`](https://github.com/yeager/audacity/commit/0014c32).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, l10n-lint, svlang, diffkontroll och
Gitleaks passerade. Hunspell markerar endast tekniska formatmarkörer.
l10n-lint har inga fel och 29 befintliga varningar utanför batchen. En ogiltig
nordisk snabbtangent fångades och rättades före inskick. PR:n är öppen och
inväntar obligatorisk upstreamgranskning; den är inte mergad.
