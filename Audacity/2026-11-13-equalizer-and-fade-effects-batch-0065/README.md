# Audacity: equalizer och toningseffekter

Fem aktiva PO-poster har granskats rad för rad. Batchen gör kurvfel,
in- och uttoning, utrymmesfel och polaritetsinvertering tydligare.

Källcommit: [`f8e3bbd`](https://github.com/yeager/audacity/commit/f8e3bbd).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv markerar endast sammansättningen
`ljudsamplarna`. `l10n-lint` har inga fel och 29 befintliga varningar utanför
batchen. PR:n är öppen och inväntar obligatorisk upstreamgranskning; den är
inte mergad.
