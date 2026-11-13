# Audacity: inspelning och spektrogram

Två aktiva PO-poster har granskats rad för rad. Batchen använder
*ljudbortfall* konsekvent för inspelningsfel och fullständigt
*maximifrekvensen* i spektrogrammets validering.

Källcommit: [`fc66148`](https://github.com/yeager/audacity/commit/fc66148).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. `l10n-lint` har inga fel och 29 befintliga varningar
utanför batchen. PR:n är ett utkast tills den radvisa genomgången är klar och
är inte mergad.
