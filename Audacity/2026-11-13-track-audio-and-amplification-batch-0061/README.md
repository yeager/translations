# Audacity: spårljud och förstärkning

Fem aktiva PO-poster har granskats rad för rad. Batchen gör spårljudets
kommandoetikett tydligare, använder den vedertagna ljudtermen ”överstyrning”
och rättar enhetsskrivningen `dB`.

Källcommit: [`a36da1d`](https://github.com/yeager/audacity/commit/a36da1d).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv markerar endast UI-namnet `VZoom`.
`l10n-lint` har inga fel och 29 befintliga varningar utanför batchen. PR:n är
öppen och inväntar obligatorisk upstreamgranskning; den är inte mergad.
