# Retroaktiv avstämning av Home Assistant Core-TM

Datum: 2026-11-24

## Resultat

- En fullständig jämförelse av verifierade HA-Core-manifest i `swedish-tm/Home-Assistant` mot den kanoniska TMX-filen hittade 11 tidigare sparade och API-verifierade nycklar som saknades i minnet. Alla 11 återkontrollerades via Lokalise API och lades till i TMX.
- Datadog-nyckeln hade ett gammalt källvärde och ett blankstegsfel i `{domain} -konfigurationen`; därför kontrollerades den mot aktuell Core-källa och live-API, rättades i Lokalise och lästes tillbaka innan aktuell källtext och översättning lades in i TMX.
- Poster som redan fanns i TMX ändrades inte av denna avstämning.
- Kanonisk TMX validerades efter uppdateringen: 16 407 poster.

## Nycklar som saknades i TMX

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Slutlig svensk text | Status |
|---|---|---|---|---|
| `component::knx::config_panel::entities::create::datetime::description` | The KNX datetime platform is used as an interface to date and time objects. | KNX-plattformen för datum och tid används som gränssnitt till datum- och tidsobjekt. | KNX-plattformen för datum och tid används som gränssnitt till datum- och tidsobjekt. | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::knx::selector::sensor_device_class::options::current` | Current | Ström | Ström | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::route_b_smart_meter::entity::sensor::instantaneous_current_t_phase::name` | Instantaneous current T phase | Momentan ström i T-fasen | Momentan ström i T-fasen | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::route_b_smart_meter::entity::sensor::instantaneous_current_r_phase::name` | Instantaneous current R phase | Momentan ström i R-fasen | Momentan ström i R-fasen | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::portainer::config::step::reauth_confirm::data_description::api_token` | The new API access token for authenticating with Portainer | Den nya API-åtkomsttoken för autentisering mot Portainer | Den nya API-åtkomsttoken för autentisering mot Portainer | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::imap::services::fetch_part::name` | Fetch message part | Hämta meddelandedel | Hämta meddelandedel | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::imap::services::fetch_part::fields::part::description` | The message part index. | Meddelandedelens index. | Meddelandedelens index. | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::imap::exceptions::invalid_part_index::message` | Invalid part index. | Ogiltigt delindex. | Ogiltigt delindex. | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::portainer::config::step::user::data_description::url` | The URL, including the port, of your Portainer instance | URL:en, inklusive porten, för din Portainer-instans | URL:en, inklusive porten, för din Portainer-instans | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::portainer::config::step::user::data_description::api_token` | The API access token for authenticating with Portainer | API-åtkomsttoken för autentisering mot Portainer | API-åtkomsttoken för autentisering mot Portainer | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::portainer::config::step::user::data_description::verify_ssl` | Whether to verify SSL certificates. Disable only if you have a self-signed certificate | Om SSL-certifikat ska verifieras. Inaktivera endast om du har ett självsignerat certifikat. | Om SSL-certifikat ska verifieras. Inaktivera endast om du har ett självsignerat certifikat. | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |
| `component::datadog::issues::deprecated_yaml_import_connection_error::description` | There was an error connecting to the Datadog Agent when trying to import the YAML configuration.<br><br>Ensure the YAML configuration is correct and restart Home Assistant to try again or remove the {domain} configuration from your `configuration.yaml` file and continue to [set up the integration]({url}) manually. | Det gick inte att ansluta till Datadog Agent när YAML-konfigurationen importerades.<br><br>Kontrollera att YAML-konfigurationen är korrekt och starta om Home Assistant för att försöka igen. Ta annars bort konfigurationen för {domain} från filen `configuration.yaml` och fortsätt med att [konfigurera integreringen]({url}) manuellt. | Det gick inte att ansluta till Datadog Agent när YAML-konfigurationen importerades.<br><br>Kontrollera att YAML-konfigurationen är korrekt och starta om Home Assistant för att försöka igen. Ta annars bort konfigurationen för {domain} från filen `configuration.yaml` och fortsätt med att [konfigurera integreringen]({url}) manuellt. | `saved-and-read-back` — Källtext och befintlig översättning återkontrollerade live i Lokalise; saknades endast i TMX. |

## Källor och spårbarhet

- Source checkout: `home-assistant/core` commit `27d3675a294`.
- Lokalise-API: läsning av nyckel/källtext/måltext och återläsning av Datadog-rättningen.
- Maskinläsbart tillägg: `2026-11-24-retroactive-core-tmx-gap-reconciliation.json` i `yeager/swedish-tm`-checkouten.
- 24 tidigare källvägsuppföljningar i TMX är fortsatt öppna; de gäller äldre Lokalise-nycklar som saknas i senaste Core-källan.
