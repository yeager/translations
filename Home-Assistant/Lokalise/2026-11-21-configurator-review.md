# Home Assistant – Configurator: svensk radgranskning

Datum: 2026-11-21  
Komponent: `configurator`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::configurator::title` | Configurator | Konfiguratorn | Oförändrad | Korrekt komponentnamn. |
| `component::configurator::entity_component::_::name` | Configurator | Konfiguratorn | Oförändrad | Refererar komponenttiteln; Lokalise visar den upplösta källtexten. |
| `component::configurator::entity_component::_::state::configure` | Configure | Konfigurera | Oförändrad | Korrekt verbform. |
| `component::configurator::entity_component::_::state::configured` | Configured | Konfigurerad | Oförändrad | Korrekt tillståndsform. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- `svlang`: 10,0/10; ”Konfiguratorn” är ett komponentnamn och ingen relevant språkvarning.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
