# SuiteCRM 8.10 – svensk översättningsgranskning

Granskad 24 september 2026 mot Crowdin-projektets `release.8.10` (branch-id 4906).

- 138 filer finns i grenen.
- 39 filer innehåller extraherade, översättningsbara fraser. Crowdin rapporterar 100 % översatta fraser för samtliga 39.
- 97 filer innehåller noll extraherade fraser och kräver ingen måltext.
- `include/SugarFields/Fields/Address/en_us.DetailView.tpl` och `en_us.EditView.tpl` har två felaktigt extraherade frasposter vardera. Källinnehållet är licenskommentarer, Smarty-uttryck, HTML och JavaScript; det ska behållas som kod och inte översättas som användargränssnitt.

## Terminologikontroll

Kontrollen omfattade 1 625 aktuella svenska måltexter från de 39 översättningsbara filerna.

| Kontroll | Resultat |
| --- | ---: |
| `Vänligen` | 0 |
| `drop-down` | 0 |
| `mål-lista` | 0 |
| `rullgardins…` | 31 |
| `mållista` | 13 |
| `avregistreringslista` | 1 |
| `undertryckningslista` | 1 |
| `fulltextsökning` | 2 |
| `Schemaläggare` | 31 |
| `Modulbyggaren` | 13 |
| `Modulläsaren` | 12 |

`l10n-lint` har körts på varje publicerad batch med en käll-/mål-katalog. Hunspell kördes mot hela den aktuella 8.10-måltexten; dess 414 okända ord är främst produktnamn, förkortningar, kodsymboler och egenamn och innebär inga funna stavfel i de nya batcharna. Gitleaks hittade inga hemligheter i auditunderlaget.
