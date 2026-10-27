# DuckStation: lokal kontroll 2026-10-27

Utgångspunkt är `duckstation-qt_sv-reviewed-20261026.ts`, som enligt
`STATUS-20261026.md` motsvarar den dåvarande svenska upstreamkatalogen.
Den nya kandidaten `duckstation-qt_sv-lint-fixes-20261027.ts` är en lokal
granskningskopia och har inte skickats till upstream.

Följande säkra rättningar har gjorts:

- två platshållarfel i pluraltexter: `%n` respektive `%3$d` finns nu i båda
  pluralformerna;
- två dubbla mellanslag och två mellanslag före punkt har tagits bort;
- åtta tangentbordsgenvägar har flyttats från `å`, `ä` och `ö` till ASCII-bokstäver;
- XML-katalogens återstående l10n-lint-fel har därmed gått från 10 till 0.

17 varningar återstår. De är huvudsakligen stil- eller terminologifrågor,
exempelvis `patcha`, `Mappplatser` och kommatecken i längre meningar. De har
inte ändrats automatiskt. Varningen om dubbelord i texten om efterbehandling
är en felträff: ordet förekommer i en rubrik och därefter i en sammanhängande
brödtext, inte dubbelt i följd.

Kontroller: `xmllint`, `l10n-lint`, `svlang`, `hunspell-sv`, `gitleaks` och
`git diff --check`. `l10n-lint` rapporterar 0 fel och 17 varningar.

Kandidaten omfattar 5 656 meddelanden och får inte laddas upp som en enda
Weblate-batch. Vid inskickning ska endast de berörda meddelandena exporteras
som ett litet delunderlag och kontrolleras mot aktuell upstreamkatalog först.
