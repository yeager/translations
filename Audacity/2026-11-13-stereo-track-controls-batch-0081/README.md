# Audacity: stereoåtgärder i vågspår

Nio aktiva PO-poster har granskats rad för rad i källkontext. Batchen
förtydligar åtgärder för att dela och sammanfoga stereospår, rättar
historiketiketter och använder *tillämpas* om realtidseffekter på vågformen.

Källcommit: [`352c33e`](https://github.com/yeager/audacity/commit/352c33e).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv saknar den avsedda sammansättningen
*vågfärg*. `l10n-lint` har inga fel och 29 befintliga varningar utanför batchen.
PR:n är ett utkast tills den radvisa genomgången är klar och är inte mergad.
