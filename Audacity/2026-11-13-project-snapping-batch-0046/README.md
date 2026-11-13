# Audacity: Projekt- och fästningsmeddelanden

Nio aktiva PO-poster har granskats rad för rad i källkontext. Batchen
förtydligar projektfilsfel, använder `torrsignal` i effektförhandsvisningen
och normaliserar `samplar` i fästningsalternativen.

Källcommit: [`f29a326`](https://github.com/yeager/audacity/commit/f29a32620d6f4f20799063fe2d2028fb8a77bf18).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv, `l10n-lint`, diffkontroll och Gitleaks
kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint` har inga
fel; de 40 kvarvarande varningarna gäller andra delar av katalogen.
PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
