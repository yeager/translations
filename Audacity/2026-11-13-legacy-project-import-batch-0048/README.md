# Audacity: Äldre projektimport

Fjorton aktiva PO-poster har granskats rad för rad i importen av äldre AUP-
projekt. Projektattribut, MIDI-stöd, tidsspår, aliasfiler och samplar är nu
formulerade idiomatiskt och konsekvent.

Källcommit: [`6998f7d`](https://github.com/yeager/audacity/commit/6998f7d0f37d733b13ae00d6d3751ed20a226822).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. l10n-lint har
inga fel; 40 äldre varningar återstår utanför batchen. PR:n är öppen och
väntar på obligatorisk upstreamgranskning. Den är inte mergad.
