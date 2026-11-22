# NMBS: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga 15 strängar i komponenten `nmbs`
har lästs från Lokalise. Mallvariablerna `{integration_title}`, `{station_name}`
och `{url}` samt YAML- och Markdown-syntaxen är bevarade.

## Rättning sparad i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::nmbs::config::step::user::data_description::exclude_vias` | Exkludera anslutningar med transfer | Exkludera anslutningar med byten | `Byten` är den etablerade svenska rese-termen. |

Ändringen sparades och lästes tillbaka via API. Den finns i det validerade
HA-minnet i `swedish-tm`.

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::nmbs::config::abort::already_configured` | Platsen är redan konfigurerad |
| `component::nmbs::config::abort::api_unavailable` | API:et är för närvarande inte tillgängligt. |
| `component::nmbs::config::abort::invalid_station` | Ogiltig station. |
| `component::nmbs::config::abort::same_station` | Avgångs- och ankomststation kan inte vara samma. |
| `component::nmbs::config::error::same_station` | Avgångs- och ankomststation kan inte vara samma. |
| `component::nmbs::config::step::user::data::exclude_vias` | Endast direktanslutningar |
| `component::nmbs::config::step::user::data::show_on_map` | Visa på kartan |
| `component::nmbs::config::step::user::data::station_from` | Avgångsstation |
| `component::nmbs::config::step::user::data::station_to` | Ankomststation |
| `component::nmbs::config::step::user::data_description::show_on_map` | Visa stationen på kartan |
| `component::nmbs::config::step::user::data_description::station_from` | Station där tåget avgår |
| `component::nmbs::config::step::user::data_description::station_to` | Station där tåget anländer |
| `component::nmbs::issues::deprecated_yaml_import_issue_station_not_found::description` | Konfigurering av {integration_title} med hjälp av YAML håller på att tas bort, men det uppstod ett problem när din YAML-konfiguration skulle importeras. |
| `component::nmbs::issues::deprecated_yaml_import_issue_station_not_found::title` | Importen av YAML-konfigurationen för {integration_title} misslyckades |

Den långa YAML-åtgärdsbeskrivningen har även kontrollerats med sitt andra
stycke, sina citattecken, `configuration.yaml` och länkmallen
`[konfigurera integrationen]({url})`; den är korrekt oförändrad.

## Verifiering

- Lokalise API: samtliga 15 svenska översättningar hämtades direkt vid denna
  granskning.
- `hunspell-sv`: inga stavningsavvikelser i provet av de språkberoende
  formuleringarna.
- `API:et` är korrekt böjning av den versalskrivna förkortningen och är därför
  inte normaliserad till en annan form.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
