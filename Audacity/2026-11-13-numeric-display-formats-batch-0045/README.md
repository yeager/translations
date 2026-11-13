# Audacity: Numeriska visningsformat

Sexton aktiva PO-poster har granskats rad för rad i källkontext. Svenska
tids- och frekvensformat använder nu decimalmarkören för svensk lokal och
benämningen `samplar` genomgående. Formatsträngarnas styrtecken har ändrats
endast där källkommentaren uttryckligen anger lokalens decimaltecken.

Källcommit: [`4d8705d`](https://github.com/yeager/audacity/commit/4d8705df9bf98d2b2aaa37432f7f36559e940aba).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och
Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint`
har inga fel; de 40 kvarvarande varningarna gäller andra delar av katalogen.
PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
