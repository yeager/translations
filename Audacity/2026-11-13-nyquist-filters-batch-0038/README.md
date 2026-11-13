# Audacity: Nyquist-filter och toning

15 PO-poster har granskats rad för rad i Nyquist-effekternas källkontext.
Arbetet rättar svenska sammansättningar, singular och plural, felaktig
ordföljd samt ljudtermer för hyllfilter, spektralredigering och övertoning.

Källcommit: [`dccce8d`](https://github.com/yeager/audacity/commit/dccce8d8c66f9fb19dfe0de15f95ee0e0de02c68).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt --check --statistics`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`,
diffkontroll och Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks
passerade. Hunspell-sv markerar bara det avsiktligt engelska licensnamnet och
den tekniska Lisp-markören `~a`. `l10n-lint` har inga fel; dess 40 kvarvarande
varningar är globala kontroller utanför den här patchen. `svlang` används som
triage och har kvar äldre tekniska false positives i hela PO-filen.

PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
