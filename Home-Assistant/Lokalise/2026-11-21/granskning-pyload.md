# Home Assistant Core – pyLoad

Datum: 2026-11-21  
Status: pågående radgranskning mot aktuell Core-källa `2fdaa177`; konfigurationsdelens första 33 Lokalise-poster är kontrollerade.

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

Den fortsatta granskningen omfattar återstående aktuella entiteter, reglage, knappar och undantag. Förslaget ovan är inte sparat och finns inte i TMX-minnet.
