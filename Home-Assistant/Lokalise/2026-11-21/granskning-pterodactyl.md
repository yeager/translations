# Home Assistant Core – Pterodactyl

Datum: 2026-11-21  
Status: pågående radgranskning mot aktuell `origin/dev`.

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::pterodactyl::entity::sensor::uptime::name` | Uptime | `[%key:component::uptime::title%]` → **Drifttid** | Osparat förslag (Lokalise-ID `627549837`); aktuell källa är vanlig text medan målet är en referens och Lokalise flaggar formatmismatch. `component::uptime::title` är verifierad i Lokalise som `Drifttid` (ID `157847620`). |
| `component::pterodactyl::config::step::reauth_confirm::description` | Please update your account API key. | Uppdatera API-nyckeln för ditt konto. | Verifierad i Lokalise (ID `630639968`). |
| `component::pterodactyl::config::step::user::data_description::api_key` | The account API key for accessing your Pterodactyl server. | Kontons API-nyckel för åtkomst till din Pterodactyl-server. | Verifierad i Lokalise (ID `624879581`). |
| `component::pterodactyl::config::step::user::data_description::url` | The URL of your Pterodactyl server, including the protocol (http:// or https://) and optionally the port number. | URL:en till din Pterodactyl-server, inklusive protokollet (http:// eller https://) och eventuellt portnumret. | Verifierad i Lokalise (ID `624879582`). |
| `component::pterodactyl::entity::binary_sensor::{status,suspended}::name` | Status; Suspended | Status; Pausad | Verifierade i Lokalise (ID `624879583`, `935693244`). |
| `component::pterodactyl::entity::button::{force_stop_server,restart_server,start_server,stop_server}::name` | Force stop server; Restart server; Start server; Stop server | Forcera stopp av server; Starta om server; Starta server; Stoppa server | Verifierade i Lokalise (ID `628027670`–`628027673`). |
| `component::pterodactyl::entity::sensor::{cpu_limit,cpu_utilization,disk_limit,disk_usage,memory_limit,memory_usage,network_inbound,network_outbound}::name` | CPU limit; CPU utilization; Disk limit; Disk usage; Memory limit; Memory usage; Network inbound; Network outbound | CPU-gräns; CPU-användning; Diskgräns; Diskanvändning; Minnesgräns; Minnesanvändning; Nätverk inkommande; Nätverk utgående | Verifierade i Lokalise (ID `627549829`–`627549836`). |

Konfigurationsreferenserna är kontrollerade och bevarade. Återstående radkontroll dokumenteras löpande.
