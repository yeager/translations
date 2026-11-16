# Home Assistant – svensk Lokalise-granskning

Senast uppdaterad: 2026-11-16

Den svenska Lokalise-kön har granskats rad för rad där källtext finns.
Ändringarna är sparade via Lokalise API och varje ändring har lästs tillbaka
från API:t efter sparningen.

Slutkontrollen returnerar 33 poster i Lokalises filter för oöversatta
översättningar, men ingen av dem innehåller översättningsbar källtext:

- 24 aktiva nycklar har tom källtext eller en avsiktligt tom pluralstruktur.
- 9 översättningsposter saknar sin nyckel; respektive nyckel ger HTTP 404 i
  Lokalise API och kan bara städas av projektadministrationen.

En senare API-kontroll med Lokalises språk-ID-filter visade 47 markerade
Core-poster och 11 markerade frontendposter. Frontendposterna hade verklig
källtext och är nu sparade samt återlästa. Coreposterna med verklig engelsk
källtext är också sparade och återlästa. De 33 återstående Coreposterna har
tom källtext eller tomma pluralstrukturer och ska inte översättas. Android,
iOS och frontend har 0 oöversatta svenska poster i den nya kontrollen.

Detaljer om den äldre slutgranskningen och den senare avvikelsen finns i
[slutgranskningen](Lokalise/2026-11-16/core-empty-source-audit/README.md)
och [API-kontrollen](Lokalise/2026-11-16/correct-language-filter-audit/README.md).

## Kontroller

Varje ändringsbatch har arkiverats med källtext och svensk måltext. Där har
`l10n-lint`, Hunspell-sv, svlang, git-diffkontroll och Gitleaks körts.
`msgfmt` är inte tillämpligt på Lokalises JSON-poster.

## Upstreamstatus

Ändringarna är inskickade direkt till den etablerade Lokalise-komponenten via
API och verifierade genom efterföljande läsning. Det finns ingen separat
upstream-granskning eller mergekö för dessa API-sparningar.
