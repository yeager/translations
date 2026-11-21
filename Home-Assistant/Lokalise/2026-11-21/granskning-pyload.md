# Home Assistant Core – pyLoad

Datum: 2026-11-21  
Status: klar radgranskning av samtliga 55 aktuella källsträngar mot Core `2fdaa177`. Två språkliga förslag är dokumenterade men ännu inte sparade i Lokalise.

## Osparat förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::pyload::config::step::user::data_description::api_key` | The API key to authenticate with pyLoad. To create a new API key, navigate to **Settings > Users > Actions > Manage API Keys** and select **Generate**. | Innehåller synliga `&gt;`-entiteter och `**Skapa**`. | API-nyckeln för att autentisera med pyLoad. För att skapa en ny API-nyckel går du till **Inställningar > Användare > Åtgärder > Hantera API-nycklar** och väljer **Generera**. | Rättar bokstavligt visade HTML-entiteter, följer källans navigeringskedja och återger “Generate” korrekt. Fetstil ska bevaras exakt vid Lokalise-sparning. Lokalise-ID `853560491`. |
| `component::pyload::entity::button::abort_downloads::name` | Abort all running downloads | Avbryta alla pågående nedladdningar | Avbryt alla pågående nedladdningar | Knappetiketter använder imperativ i svenskan. Lokalise-ID `496992181`. |

## Verifierat i första delen

- API-nyckel-, användarnamns-, lösenords-, URL- och SSL-referenser för användar-, reautentiserings-, hassio- och omkonfigureringsflöden är bevarade där de motsvarar aktuell källa.
- `{addon}` i hassio-beskrivningen och `{example_url}` i URL-beskrivningen är bevarade.
- Texterna för URL, SSL-validering samt föråldrade användarnamn- och lösenordsfält är språkligt korrekta.
- `Home Assistant` är oförändrat i pyLoad via Home Assistant-appen och hassio-beskrivningen.

Produktnamnsregel: när källtexten innehåller `Home Assistant` ska samma ordalydelse bevaras i den svenska översättningen.

## Verifierade konfigurationsfel

De tre aktuella konfigurationsfelen använder korrekt samma referenser som källan och kräver ingen ändring:

- `component::pyload::config::error::cannot_connect` (Lokalise-ID `496322871`): `[%key:common::config_flow::error::cannot_connect%]`.
- `component::pyload::config::error::invalid_auth` (ID `496322872`): `[%key:common::config_flow::error::invalid_auth%]`.
- `component::pyload::config::error::unknown` (ID `496322873`): `[%key:common::config_flow::error::unknown%]`.

## Abortposter och källomfattning

- `component::pyload::config::abort::already_configured` (Lokalise-ID `496322870`) är korrekt och följer exakt källreferensen `[%key:common::config_flow::abort::already_configured_device%]`.
- `reconfigure_successful` (ID `497619377`) och `reauth_successful` (ID `497454039`) finns ännu i Lokalise, men saknas i den aktuella Core-källan. De är därför historiska poster och inte förslag till ändring.
- Sökningen visade 75 pyLoad-poster i Lokalise. 55 motsvarar den aktuella källfilen; resterande 20 är historiska fält eller avvecklade flöden.

## Verifierade undantag

Samtliga fem aktuella undantag är kontrollerade utan ändringsförslag:

- `service_call_exception` (Lokalise-ID `498962219`): anslutningsfel vid kommando.
- `service_call_auth_exception` (ID `498962218`): autentiseringsfel vid kommando.
- `setup_request_exception` (ID `497675314`): anslutning och hämtning från pyLoad API.
- `setup_parse_exception` (ID `497675313`): tolkning av data från pyLoad API.
- `setup_authentication_exception` (ID `497675312`): misslyckad autentisering med inloggningsuppgifter.

Svenskan följer källans betydelse och använder produktnamnet `pyLoad` konsekvent.

## Verifierade entiteter

De övriga 11 aktuella entitetsnamnen är korrekta: återanslutning, köreglage, fyra återstående knappetiketter samt fem sensoretiketter för aktiva/totala/köade nedladdningar, ledigt utrymme och hastighet. Referenser saknas i denna del och inga platshållare påverkas.

Alla 55 aktuella pyLoad-strängar är nu granskade. De två förslagen ovan är inte sparade och finns inte i TMX-minnet. Verifierade befintliga poster kan föras in i Home Assistant-minnet med Lokalise-ID och källspårning i nästa TMX-synkning.
