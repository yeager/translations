# Home Assistant – Blackbird: svensk radgranskning

Datum: 2026-11-21  
Komponent: `blackbird`  
Omfattning: 6/6 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::blackbird::services::set_all_zones::description` | Sets all Blackbird zones to a single source. | Ställer in alla Blackbird-zoner till samma källa. | Oförändrad | Korrekt. |
| `component::blackbird::services::set_all_zones::fields::entity_id::description` | Name of any blackbird zone. | Namn på en Blackbird-zon. | Oförändrad | Korrekt och kort fältbeskrivning. |
| `component::blackbird::services::set_all_zones::fields::entity_id::name` | Entity | Entitet | Oförändrad | Korrekt HA-term. |
| `component::blackbird::services::set_all_zones::fields::source::description` | Name of source to switch to. | Namnet på källan att växla till. | Oförändrad | Korrekt. |
| `component::blackbird::services::set_all_zones::fields::source::name` | Source | Källa | Oförändrad | Korrekt. |
| `component::blackbird::services::set_all_zones::name` | Set all zones | Ställ in alla zoner | Oförändrad | Korrekt UI-verb. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga relevanta stavningsanmärkningar.
- `svlang`: 10,0/10; Blackbird markeras enbart som produktnamn.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
