# Audacity: konflikter för molnprojekt

Tio aktiva PO-poster har granskats rad för rad i molnprojektens dialoger.
Batchen använder idiomatisk bestämd form, *i stället*, *på audio.com* och
tydligare text när osparade ändringar ignoreras för en nyare molnversion.

Källcommit: [`7143ce5`](https://github.com/yeager/audacity/commit/7143ce5).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv markerar endast domännamnet *audio.com*.
`l10n-lint` har inga fel och 28 befintliga varningar utanför batchen. Tre
svlang-träffar är falska V2-varningar för korrekt imperativ och bisatsordföljd.
PR:n är ett utkast tills den radvisa genomgången är klar och är inte mergad.
