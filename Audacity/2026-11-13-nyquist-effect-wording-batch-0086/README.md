# Audacity: Nyquist-effekternas språk

Sju aktiva PO-poster har granskats rad för rad i källkontext. Batchen
normaliserar *samplingsfrekvens*, rättar *tröskelmätning*, förtydligar
inledande tystnad och använder *bandbredd* för notchfiltrets Q-värde.

Källcommit: [`8d40ab9`](https://github.com/yeager/audacity/commit/8d40ab9).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv har inga träffar i batchen. `l10n-lint`
har inga fel och 28 befintliga varningar utanför batchen. PR:n är ett utkast
tills den radvisa genomgången är klar och är inte mergad.
