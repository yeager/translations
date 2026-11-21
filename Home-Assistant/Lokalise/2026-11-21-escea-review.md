# Home Assistant – Escea: svensk radgranskning

Datum: 2026-11-21  
Komponent: `escea`  
Omfattning: 1/1 aktuell källsträng

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Åtgärd |
| --- | --- | --- | --- | --- |
| `component::escea::config::step::confirm::description` | Do you want to set up an Escea fireplace? | Vill du sätta upp en Escea eldstad? | Vill du konfigurera en Escea-eldstad? | Sparad i Lokalise |

`konfigurera` följer etablerad svensk terminologi för installationsflöden. Bindestrecket gör produktnamnsbestämningen läsbar.

## Verifiering

- Aktuell källa och översättning hämtades via Lokalise API; ändringen lästes tillbaka efter sparning.
- `l10n-lint`: inga problem.
- `hunspell-sv` och `svlang` markerar `Escea` som okänt/sällsynt produktnamn; ingen stavningsändring behövs.
- Inga platshållare, pluralformer, referenser eller formateringsmarkörer förekommer.
