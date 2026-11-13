# Audacity: Import- och MIDI-diagnostik

Tio aktiva PO-poster har granskats rad för rad i källkontext. Batchen gör
filtypsdiagnostiken idiomatisk, förtydligar kommandofelet och använder
`samplar` konsekvent i tidsformatet.

Källcommit: [`8a19bdc`](https://github.com/yeager/audacity/commit/8a19bdc82f6bc3565eba2e1b153befc7ffcb6f6d).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och
Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint`
har inga fel; de 40 kvarvarande varningarna gäller andra delar av katalogen.
PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
