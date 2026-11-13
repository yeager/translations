# Audacity: inläsning av molnprojekt

Två aktiva PO-poster har granskats rad för rad i källkontexten för Audacitys
molnprojektvy. Batchen använder *läs in* för lokal inläsning av projektlistan
och rättar bestämd form i kontobehörighetsfelet.

Källcommit: [`ed59c7e`](https://github.com/yeager/audacity/commit/ed59c7e).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv har inga träffar i batchen. `l10n-lint`
har inga fel och 28 befintliga varningar utanför batchen. `svlang` ger breda
falska positiva i hela PO-filen, men ingen träff i de två ändrade posterna.
PR:n är ett utkast tills den radvisa genomgången är klar och är inte mergad.
