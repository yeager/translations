# Home Assistant Core – UniFi Direct

Datum: 2026-11-21

Alla åtta strängar är granskade mot aktuell källa. Två korrigeringar är sparade i Lokalise och ordagrant återlästa via API.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::unifi_direct::issues::yaml_import_cannot_connect::description` | `Kontrollera att {host} är tillgänglig ... uppdatera din configuration.yaml` | `Kontrollera att {host} går att nå ... uppdatera configuration.yaml` | Följde Core-formuleringen för nåbar värd och tog bort ogrundat possessivt pronomen. |
| `component::unifi_direct::issues::yaml_import_cannot_connect::title` | `Import av ...: går inte att ansluta` | `Importen av ...: det går inte att ansluta` | Rättad bestämd form och fullständig svensk sats. |

Övriga sex konfigurationssträngar är korrekta. Platshållaren `{host}`, produktnamnet `UniFi AP`, `configuration.yaml` och `Home Assistant` är bevarade.
