# Home+ Control: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga 16 strängar i komponenten
`home_plus_control` har lästs från Lokalise. Mallreferenserna `{docs_url}` och
`{url}` samt Markdown-länkarna till hjälpavsnittet och Netatmo är bevarade.

## Rättningar sparade i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::home_plus_control::issues::move_to_netamo::title` | Nedstängning av Legrand Home+ Control | Avveckling av Legrand Home+ Control | `Avveckling` är den precisa svenska termen för *deprecation*. |
| `component::home_plus_control::issues::move_to_netatmo::title` | Nedstängning av Legrand Home+ Control | Avveckling av Legrand Home+ Control | Samma källtext och samma konsekventa term. |

Båda ändringarna lästes tillbaka via Lokalise efter sparning och finns i det
validerade HA-minnet i `swedish-tm`.

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text eller kontroll |
| --- | --- |
| `component::home_plus_control::config::abort::already_configured` | Kontot är redan konfigurerat |
| `component::home_plus_control::config::abort::already_in_progress` | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. |
| `component::home_plus_control::config::abort::authorize_url_timeout` | Tidsgränsen överskreds vid generering av en auktoriserings-URL. |
| `component::home_plus_control::config::abort::missing_configuration` | Komponenten har inte konfigurerats. Följ dokumentationen. |
| `component::home_plus_control::config::abort::no_url_available` | Ingen webbadress är tillgänglig. Markdown-länken med `{docs_url}` är korrekt. |
| `component::home_plus_control::config::abort::single_instance_allowed` | Redan konfigurerad. Endast en konfiguration kan göras. |
| `component::home_plus_control::config::create_entry::default` | Autentisering lyckades |
| `component::home_plus_control::config::step::pick_implementation::title` | Välj autentiseringsmetod |
| `component::home_plus_control::issues::move_to_netamo::description` | Netatmo-länken med `{url}`, produktnamnet och styckebrytningen är korrekta. |
| `component::home_plus_control::issues::move_to_netatmo::description` | Netatmo-länken med `{url}`, produktnamnet och styckebrytningen är korrekta. |
| `component::home_plus_control::config::abort::oauth_error` | Ogiltiga tokendata mottogs. |
| `component::home_plus_control::config::abort::oauth_failed` | Fel vid hämtning av åtkomsttoken. |
| `component::home_plus_control::config::abort::oauth_timeout` | Tidsgränsen överskreds när OAuth-token hämtades. |
| `component::home_plus_control::config::abort::oauth_unauthorized` | OAuth-auktoriseringsfel vid hämtning av åtkomsttoken. |

## Verifiering

- Lokalise API: alla 16 svenska översättningar hämtades direkt vid denna
  granskning.
- Produktnamnen `Home Assistant`, `Legrand Home+ Control` och `Netatmo` är
  oförändrade, enligt källtexten.
- De två långa avvecklingsmeddelandena förekommer med olika nycklar men har
  identisk käll- och måltext; båda har verifierats.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
