# Home Assistant Core: Immich-konfiguration

Kontrollerat i Lokalise den 19 november 2026. Inga ändringar har gjorts i Lokalise. Referenserna är identiska i engelska och svenska. Tabellen återger varje fullständig nyckel; `ref` betyder att båda språkfälten innehåller den angivna referensen. Filtrerade resultat bevisar inte ofiltrerad ordning.

| Fullständig nyckel | Engelska och befintlig svenska | Bedömning |
|---|---|---|
| `component::immich::config::step::user::data_description::verify_ssl` | ref `[%key:component::immich::common::data_desc_ssl_verify%]` | Behåll referensen; se mål nedan. |
| `component::immich::config::step::user::data_description::url` | ref `[%key:component::immich::common::data_desc_url%]` | Behåll referensen; se mål nedan. |
| `component::immich::config::step::user::data_description::api_key` | ref `[%key:component::immich::common::data_desc_api_key%]` | Behåll referensen; se mål nedan. |
| `component::immich::config::step::user::data::verify_ssl` | ref `[%key:common::config_flow::data::verify_ssl%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::step::user::data::url` | ref `[%key:common::config_flow::data::url%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::step::user::data::api_key` | ref `[%key:common::config_flow::data::api_key%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::step::reauth_confirm::description` | Update the API key for {name}. → Uppdatera API-nyckeln för {name}. | Behåll; platshållaren är bevarad. |
| `component::immich::config::step::reauth_confirm::data_description::api_key` | ref `[%key:component::immich::common::data_desc_api_key%]` | Behåll referensen; se mål nedan. |
| `component::immich::config::step::reauth_confirm::data::api_key` | ref `[%key:common::config_flow::data::api_key%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::error::unknown` | ref `[%key:common::config_flow::error::unknown%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::error::invalid_url` | The provided URL is invalid. → Den angivna URL:en är ogiltig. | Behåll. |
| `component::immich::config::error::invalid_auth` | ref `[%key:common::config_flow::error::invalid_auth%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::error::cannot_connect` | ref `[%key:common::config_flow::error::cannot_connect%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::abort::unique_id_mismatch` | The provided API key does not match the configured user. → Den angivna API-nyckeln matchar inte den konfigurerade användaren. | Behåll. |
| `component::immich::config::abort::reauth_successful` | ref `[%key:common::config_flow::abort::reauth_successful%]` | Behåll referensen; kontrollera gemensamt mål. |
| `component::immich::config::abort::already_configured` | This user is already configured for this Immich instance. → Den här användaren är redan konfigurerad för denna Immich-instans. | Behåll. |
| `component::immich::common::data_desc_url` | The full URL of your Immich instance. → Den fullständiga URL:en för din Immich-instans. | Behåll. |
| `component::immich::common::data_desc_api_key` | API key to connect to your Immich instance. → API-nyckel för att ansluta till din Immich-instans. | Behåll. |
| `component::immich::common::data_desc_ssl_verify` | Whether to verify the SSL certificate when SSL encryption is used to connect to your Immich instance. → Huruvida SSL-certifikatet ska verifieras när SSL-kryptering används för att ansluta till din Immich-instans. | Föreslå: Om SSL-certifikatet ska verifieras när SSL-kryptering används vid anslutning till din Immich-instans. Enklare ordval med samma innebörd. |

Historiska TMX-ögonblicksbilden återgav de tre `data_description`-texterna upplösta; aktuell Lokalise visar referenser till de gemensamma Immich-nycklarna. Referenser ska därför behållas, och ändringsförslaget gäller målnyckeln. Hunspell-sv markerade varumärkessammansättningen; svlang flaggade bisatsordföljd och passiv form i meningsfragmentet, vilket inte i sig motiverar ändring. FOSS-terminologin och översättningsminnet behöver kontrolleras specifikt för SSL-formuleringen. De sju gemensamma referensmålen ovan är ännu inte verifierade i denna kontroll.
