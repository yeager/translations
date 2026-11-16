# Home Assistant – svensk Lokalise-granskning

Senast uppdaterad: 2026-11-16

Den aktuella svenska Lokalise-kön är genomgången rad för rad där källtext
finns. Ändringarna är sparade via Lokalise API och varje ändring har lästs
tillbaka från API:t efter sparningen.

Slutkontrollen returnerar 33 poster i Lokalises filter för oöversatta
översättningar, men ingen av dem innehåller översättningsbar källtext:

- 24 aktiva nycklar har tom källtext eller en avsiktligt tom pluralstruktur.
- 9 översättningsposter saknar sin nyckel; respektive nyckel ger HTTP 404 i
  Lokalise API och kan bara städas av projektadministrationen.

Alltså återstår inga svenska strängar att översätta i den aktuella kön.
Detaljer och metod finns i
[slutgranskningen](Lokalise/2026-11-16/core-empty-source-audit/README.md).

## Kontroller

Varje ändringsbatch har arkiverats med källtext och svensk måltext. Där har
`l10n-lint`, Hunspell-sv, svlang, git-diffkontroll och Gitleaks körts.
`msgfmt` är inte tillämpligt på Lokalises JSON-poster.

## Upstreamstatus

Ändringarna är inskickade direkt till den etablerade Lokalise-komponenten via
API och verifierade genom efterföljande läsning. Det finns ingen separat
upstream-granskning eller mergekö för dessa API-sparningar.
