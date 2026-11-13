# Audacity: återställning och diagnostik

Tolv aktiva PO-poster har granskats rad för rad i återställning, makron och
teknisk diagnostik. Batchen förtydligar den permanenta raderingsvarningen,
förbättrar konfigurations- och felrapporteringstexter samt normaliserar
*sample* och beräkningsutdata.

Källcommit: [`0120196`](https://github.com/yeager/audacity/commit/0120196).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll
och Gitleaks passerade. Hunspell-sv träffar endast formatvariablerna `%ld` och
`%lld` samt den avsedda tekniska singularformen *sample*. `l10n-lint` har inga
fel och 28 befintliga varningar utanför batchen. PR:n är ett utkast tills den
radvisa genomgången är klar och är inte mergad.
