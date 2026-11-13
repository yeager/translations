# Audacity: vågspårens terminologi

Tolv aktiva PO-poster har granskats rad för rad i källkontext. Batchen
normaliserar *samplar*, *spektral markering*, *undervyer* och
*samplingsfrekvens* i vågspårens menyer, verktygstips och historik.

Källcommit: [`21a1a75`](https://github.com/yeager/audacity/commit/21a1a75).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv saknar de avsedda sammansättningarna
*undervy* och *undervyer*. `l10n-lint` har inga fel och 29 befintliga varningar
utanför batchen. PR:n är ett utkast tills den radvisa genomgången är klar och
är inte mergad.
