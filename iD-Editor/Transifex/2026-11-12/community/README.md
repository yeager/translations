# iD Editor, community, svenska

Datum: 2026-11-12
Projekt: iD Editor 2.42.3, publicerad 2026-10-20
Komponent: `community`
Upstream: https://app.transifex.com/openstreetmap/id-editor/translate/#sv/community/

## Resultat

19 saknade communityposter granskades mot iD:s communitydata och skickades i
en Transifex API-batch. API-kvittot omfattar samtliga 19 mål, och
efterkontrollen visar 0 oöversatta svenska poster i komponenten.

## Terminologi och undantag

* Organisations-, produkt- och platsnamn som Mapwyr Cymru, OpenStreetMap,
  Wikimedia Bay Area, Bluesky och WikiSalon är avsiktligt oförändrade.
* `mapper` är `kartläggare`; `mapping` är `kartläggning`.
* `Local Chapter` är `lokalavdelning` i beskrivningen av en OSM-gemenskap.
* l10n-lints träff för identiskt `Wikimedia Bay Area` är en korrekt
  namnbevaring, inte en oöversatt användartext.

## Kontroller

* l10n-lint och svlang: godkända.
* Platshållarna `{community}` och `{url}` är bevarade.
* Hunspell-sv träffade endast avsedda namn, bland annat OpenStreetMap,
  Mapwyr Cymru, Málaga, Bluesky och OSSJ.
* Kontroll av em dash, `git diff --check` och Gitleaks: godkända.
* `msgfmt`: inte tillämpligt, eftersom detta är en JSON-resurs.

## Status

Inskickad och mottagen i Transifex. Måltexterna är inte formellt granskade
i Transifex. Råexport, delta, API-kvitto och efterkontroll finns i denna
katalog.
