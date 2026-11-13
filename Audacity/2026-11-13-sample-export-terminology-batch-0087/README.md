# Audacity: export av samplingsdata

Fjorton aktiva PO-poster har granskats rad för rad i källkontext. Batchen
normaliserar *samplingsfrekvens* och *samplar* i dataexporten samt förtydligar
filtyp, tidsindexering, brusband och en parameter i rytmspårseffekten.

Källcommit: [`9cde96c`](https://github.com/yeager/audacity/commit/9cde96c).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv saknar de avsedda termerna *brusbandets*,
*Pluck* och *samplenr* samt mallvariabeln `~a`. `l10n-lint` har inga fel och
28 befintliga varningar utanför batchen. PR:n är ett utkast tills den radvisa
genomgången är klar och är inte mergad.
