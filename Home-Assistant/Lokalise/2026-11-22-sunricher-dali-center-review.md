# Sunricher DALI Center: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga elva strängar i komponenten
`sunricher_dali_center` har lästs från Lokalise.

## Rättning sparad i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::sunricher_dali_center::config::step::user::description` | **Tre stegsprocess:** | **Trestegsprocess:** | Svensk sammansättning skrivs ihop. |

Hela instruktionen sparades via Lokalise API och lästes tillbaka ordagrant.
Antalet radbrytningar och Markdown-markörer verifierades som oförändrade. Den
finns i det validerade HA-minnet (`swedish-tm`, commit `0418aae`).

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text eller kontroll |
| --- | --- |
| `component::sunricher_dali_center::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::sunricher_dali_center::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::sunricher_dali_center::config::error::discovery_failed` | Det gick inte att upptäcka DALI-gateways i nätverket |
| `component::sunricher_dali_center::config::error::no_devices_found` | Inga DALI-gateways hittades i nätverket |
| `component::sunricher_dali_center::config::error::unknown` | Oväntat fel |
| `component::sunricher_dali_center::config::step::select_gateway::data::selected_gateway` | Gateway |
| `component::sunricher_dali_center::config::step::select_gateway::data_description::selected_gateway` | Varje alternativ visar gatewayens namn, serienummer och IP-adress. |
| `component::sunricher_dali_center::config::step::select_gateway::description` | Välj den gateway som ska konfigureras. |
| `component::sunricher_dali_center::config::step::select_gateway::title` | Välj DALI-gateway |
| `component::sunricher_dali_center::config::step::user::title` | Konfigurera DALI Center-gateway |

## Verifiering

- Lokalise API: alla elva svenska översättningar hämtades direkt vid denna
  granskning; rättningen lästes tillbaka efter skrivning.
- `svlang check`: 10,0/10 för `Trestegsprocess`.
- `hunspell-sv`: inga stavningsavvikelser för `Trestegsprocess`.
- Fetstil, numrerad lista och radbrytningar i den långa instruktionen är
  bevarade.
- HA-TMX-validatorn: `valid: 3321 entries` efter uppdateringen.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
