# Home Assistant Core – Redgtech

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/redgtech/strings.json`  
Status: samtliga 14 aktuella strängar granskade mot Lokalise och källtext.

Alla referenser och feltexter kontrollerades. Följande måltexter har
felaktiga mellanrum vid sammansättningar eller oidiomatisk API-ordföljd:

| Nyckel | Befintlig text | Föreslagen text |
| --- | --- | --- |
| `component::redgtech::config::step::user::description` | `Ange dina inloggningsuppgifter för att ansluta till {integration_name} API.` | `Ange dina inloggningsuppgifter för att ansluta till {integration_name}-API:et.` |
| `component::redgtech::config::step::user::data_description::password` | `Ange lösenordet för ditt {integration_name} -konto.` | `Ange lösenordet för ditt {integration_name}-konto.` |
| `component::redgtech::config::step::user::data_description::email` | `Ange e-postadressen som är kopplad till ditt {integration_name} -konto.` | `Ange e-postadressen som är kopplad till ditt {integration_name}-konto.` |
| `component::redgtech::exceptions::api_error::message` | `Fel vid kommunikation med API:et {integration_name}` | `Fel vid kommunikation med {integration_name}-API:et.` |
| `component::redgtech::exceptions::connection_error::message` | `Anslutningsfel med API:et {integration_name}` | `Anslutningsfel med {integration_name}-API:et.` |
| `component::redgtech::exceptions::switch_auth_error::message` | `Autentiseringen misslyckades vid styrning av {integration_name} -brytare` | `Autentiseringen misslyckades när {integration_name}-brytaren styrdes.` |

Raderna för e-postadress och lösenord var redan korrekta i den aktuella
API-katalogen. De fyra återstående korrigeringarna är sparade och återlästa
via Lokalise API 2026-11-21 och införda i den verifierade HA-TMX:en med
Lokalise-ID.
