# Audacity: distorsion och effektgränssnitt

Fem aktiva PO-poster har granskats rad för rad. Batchen förtydligar DTMF-texten,
status för komprimering samt namn på effektgränssnittets inställningsmeny.

Källcommit: [`9e32203`](https://github.com/yeager/audacity/commit/9e32203).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv markerar endast den avsedda tekniska termen
`DTMF-toner`. `l10n-lint` har inga fel och 29 befintliga varningar utanför
batchen. PR:n är öppen och inväntar obligatorisk upstreamgranskning; den är
inte mergad.
