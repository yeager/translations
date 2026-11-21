# Sparade ändringar för ZhongHong

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::zhong_hong::exceptions::send_command_failed::message` | Failed to send {command} command to the ZhongHong gateway. | Det gick inte att skicka kommandot {command} till ZhongHong-gateway. | Det gick inte att skicka kommandot {command} till ZhongHong-gatewayen. |
| `component::zhong_hong::exceptions::no_devices_found::message` | The ZhongHong gateway at {host} did not report any air conditioners. | ZhongHong-gateway på {host} rapporterade inga luftkonditioneringsenheter. | ZhongHong-gatewayen på {host} rapporterade inga luftkonditioneringsenheter. |
| `component::zhong_hong::exceptions::cannot_connect::message` | Failed to connect to the ZhongHong gateway at {host}. | Det gick inte att ansluta till ZhongHong-gateway på {host}. | Det gick inte att ansluta till ZhongHong-gatewayen på {host}. |

Bestämd form har lagts till och platshållarna har bevarats.

## Konfiguration utan rapporterade enheter

Sparad och återläst i Lokalise 2026-11-19. Den separata avbrottsnyckeln hänvisar till denna text på både engelska och svenska.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::zhong_hong::config::error::no_devices_found` | Connected to the gateway, but it did not report any air conditioners. | Ansluten till gateway, men den rapporterade inga luftkonditioneringsapparater. | Ansluten till gatewayen, men den rapporterade inga luftkonditioneringsenheter. |

Bestämd form och ordval följer de relaterade feltexterna.

## Återverifiering 2026-11-21

Alla 20 strängar i `component::zhong_hong` kontrollerades mot den aktuella Lokalise-exporten. De tidigare sparade formuleringarna, platshållarna `{host}`, `{command}`, `{integration_title}` och `{domain}`, YAML- och filreferensen samt flerradsmeddelandena är korrekta. Inga ytterligare ändringar behövs.
