# Home Assistant Core – historisk avstämning 15241–15360

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 67 direkta källtexter matchar HA Core-källan; 32 referensanvändningar med 22 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 21 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15241 | 888596805 | `component::luci::issues::yaml_import_cannot_connect::description` | The YAML configuration for OpenWrt (luci) at `{host}` could not be imported because the connection failed.<br><br>Please check that `{host}` is reachable, update your `configuration.yaml` if needed, and restart Home Assistant. | YAML-konfigurationen för OpenWrt (luci) på `{host}` kunde inte importeras eftersom anslutningen misslyckades.<br><br>Kontrollera att `{host}` är nåbar, uppdatera din `configuration.yaml` om det behövs och starta om Home Assistant. | Core-literal match |
| 15242 | 888596804 | `component::luci::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 15243 | 888596803 | `component::luci::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 15244 | 888596802 | `component::luci::config::step::user::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 15245 | 888596801 | `component::luci::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 15246 | 888596800 | `component::luci::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 15247 | 888596799 | `component::luci::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 15248 | 888596798 | `component::luci::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 15249 | 888596797 | `component::luci::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15250 | 888596796 | `component::luci::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15251 | 888596795 | `component::luci::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 15252 | 888596794 | `component::luci::config::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15253 | 888596793 | `component::luci::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15254 | 888596792 | `component::luci::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 15255 | 888090343 | `component::google_health::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 15256 | 888090342 | `component::google_health::config::step::reauth_confirm::description` | The Google Health integration needs to re-authenticate your account | Google Health-integrationen kräver att du autentiserar ditt konto på nytt | Core-literal match |
| 15257 | 888090341 | `component::google_health::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 15258 | 888074877 | `component::stiebel_eltron::config::step::discovery_confirm::description` | Do you want to set up the STIEBEL ELTRON heat pump at {host}? | Vill du konfigurera STIEBEL ELTRON-värmepumpen på {host}? | Core-literal match |
| 15259 | 888074876 | `component::stiebel_eltron::config::flow_title` | STIEBEL ELTRON ({host}) | STIEBEL ELTRON ({host}) | Core-literal match |
| 15260 | 888032772 | `component::teslemetry::exceptions::update_failed_insufficient_credits::message` | Teslemetry account has insufficient command credits, pausing updates until credits are added | Det finns inte tillräckligt med kommandokrediter på Teslemetry-kontot, vilket innebär att uppdateringarna pausas tills fler krediter har lagts till | Core-literal match |
| 15261 | 887932596 | `component::roborock::entity::image::map::name` | Map | Karta | Core-literal match |
| 15262 | 887931066 | `component::stiebel_eltron::config::step::reconfigure::data_description::port` | The port of your Stiebel Eltron device. | Porten på din Stiebel Eltron-enhet. | Shared reference target checked |
| 15263 | 887931065 | `component::stiebel_eltron::config::step::reconfigure::data_description::host` | The hostname or IP address of your Stiebel Eltron device. | Värdnamnet eller IP-adressen för din Stiebel Eltron-enhet. | Shared reference target checked |
| 15264 | 887931064 | `component::stiebel_eltron::config::step::reconfigure::data::port` | Port | Port | Shared reference target checked |
| 15265 | 887931063 | `component::stiebel_eltron::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 15266 | 887931062 | `component::stiebel_eltron::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 15267 | 887909722 | `component::google_health::exceptions::oauth_error::message` | OAuth2 implementation temporarily unavailable. | OAuth2-implementeringen är för tillfället otillgänglig. | Source-path follow-up open |
| 15268 | 887909721 | `component::google_health::exceptions::missing_profile_scope::message` | Missing required Google Health profile read permission. | Det saknas nödvändiga läsbehörigheter för Google Health-profilen. | Core-literal match |
| 15269 | 887909720 | `component::google_health::exceptions::communication_error::message` | Error communicating with Google Health. | Fel vid kommunikation med Google Health. | Core-literal match |
| 15270 | 887909719 | `component::google_health::exceptions::auth_error::message` | Authentication or permission error talking to Google Health. | Autentiserings- eller behörighetsfel vid kommunikation med Google Health. | Core-literal match |
| 15271 | 887909718 | `component::google_health::entity::sensor::steps::unit_of_measurement` | steps | steg | Core-literal match |
| 15272 | 887909717 | `component::google_health::entity::sensor::steps::name` | Steps | Steg | Core-literal match |
| 15273 | 887909716 | `component::google_health::entity::sensor::resting_heart_rate::name` | Resting heart rate | Vilopuls | Core-literal match |
| 15274 | 887909715 | `component::google_health::config::step::pick_implementation::title` | Pick authentication method | Välj autentiseringsmetod | Shared reference target checked |
| 15275 | 887909714 | `component::google_health::config::create_entry::default` | Successfully authenticated | Autentisering lyckades | Shared reference target checked |
| 15276 | 887909713 | `component::google_health::config::abort::user_rejected_authorize` | Account linking rejected: {error} | Kontolänkning avvisades: {error} | Source-path follow-up open |
| 15277 | 887909712 | `component::google_health::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. | OAuth-auktoriseringsfel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 15278 | 887909711 | `component::google_health::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. | Tidsgränsen överskreds när OAuth-token hämtades. | Source-path follow-up open |
| 15279 | 887909710 | `component::google_health::config::abort::oauth_implementation_unavailable` | No OAuth2 implementations are currently available. | Inga OAuth2-implementeringar finns tillgängliga för närvarande. | Source-path follow-up open |
| 15280 | 887909709 | `component::google_health::config::abort::oauth_failed` | Error while obtaining access token. | Fel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 15281 | 887909708 | `component::google_health::config::abort::oauth_error` | Received invalid token data. | Ogiltiga tokendata mottogs. | Source-path follow-up open |
| 15282 | 887909707 | `component::google_health::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) | Ingen webbadress är tillgänglig. [Se hjälpavsnittet]({docs_url}) för information om det här felet. | Source-path follow-up open |
| 15283 | 887909706 | `component::google_health::config::abort::missing_profile_scope` | Missing required Google Health profile read permission. Please try again and select the right permission. | Saknar nödvändig läsbehörigheter för Google Hälsoprofilen. Försök igen och välj rätt behörighet. | Core-literal match |
| 15284 | 887909705 | `component::google_health::config::abort::missing_configuration` | The component is not configured. Please follow the documentation. | Komponenten har inte konfigurerats. Följ dokumentationen. | Shared reference target checked |
| 15285 | 887909704 | `component::google_health::config::abort::cannot_connect` | Failed to connect. | Det gick inte att ansluta. | Core-literal match |
| 15286 | 887909703 | `component::google_health::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. | Tidsgränsen överskreds vid generering av en auktoriserings-URL. | Source-path follow-up open |
| 15287 | 887909702 | `component::google_health::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 15288 | 887909701 | `component::google_health::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 15289 | 887909700 | `component::google_health::application_credentials::description` | Follow the [instructions]({more_info_url}) for [OAuth consent screen]({oauth_consent_url}) to give Home Assistant access to your Google Health data. You also need to create Application Credentials linked to your account:<br>1. Go to [Credentials]({oauth_creds_url}) and select **Create Credentials**.<br>1. From the drop-down list select **OAuth client ID**.<br>1. Select **Web application** for the Application Type. | Följ [instruktionerna]({more_info_url}) för [OAuth-samtyckesskärmen]({oauth_consent_url}) för att ge Home Assistant åtkomst till Google Health-data. Du måste också skapa autentiseringsuppgifter för appen, kopplade till kontot:<br>1. Gå till [Credentials]({oauth_creds_url}) och välj **Create Credentials**.<br>1. Välj **OAuth client ID** i listrutan.<br>1. Välj **Web application** som applikationstyp. | Core-literal match |
| 15290 | 887804204 | `component::neopool::issues::corrupted_gpio::title` | Corrupted GPIO register(s) detected | Korrupta GPIO-register upptäckta | Core-literal match |
| 15291 | 887804203 | `component::neopool::issues::corrupted_gpio::description` | The following GPIO register(s) on your pool controller contain invalid values:<br><br>{details}<br><br>This typically happens when the Modbus gateway framing mode does not match the integration's framer setting. The affected function(s) will not work correctly until the register(s) are restored to valid values.<br><br>See the integration documentation for repair instructions. | Följande GPIO-register på din poolkontroller innehåller ogiltiga värden:<br><br>{details}<br><br>Detta händer vanligtvis när Modbus-gatewayens framing-läge inte matchar integrationens framer-inställning. De berörda funktionerna kommer inte att fungera korrekt förrän registret har återställts till giltiga värden.<br><br>Se integrationsdokumentationen för reparationsinstruktioner. | Core-literal match |
| 15292 | 887804202 | `component::neopool::exceptions::modbus_communication_error::message` | An error occurred while communicating with the NeoPool controller: {error} | Ett fel uppstod vid kommunikationen med NeoPool-styrenheten: {error} | Core-literal match |
| 15293 | 887804201 | `component::neopool::entity::sensor::ph_status_alarm::state::tank_level` | Tank level alarm | Tanknivålarm | Core-literal match |
| 15294 | 887804200 | `component::neopool::entity::sensor::ph_status_alarm::state::pump_stopped` | Pump stopped (exceeded working time) | Pumpen stoppad (överskriden arbetstid) | Core-literal match |
| 15295 | 887804199 | `component::neopool::entity::sensor::ph_status_alarm::state::ph_under` | pH lower than the set point | pH-värdet är lägre än börvärdet | Core-literal match |
| 15296 | 887804198 | `component::neopool::entity::sensor::ph_status_alarm::state::ph_over` | pH higher than the set point | pH-värdet är högre än börvärdet | Core-literal match |
| 15297 | 887804197 | `component::neopool::entity::sensor::ph_status_alarm::state::ph_low` | pH too low | pH-värdet är för lågt | Core-literal match |
| 15298 | 887804196 | `component::neopool::entity::sensor::ph_status_alarm::state::ph_high` | pH too high | pH-värdet är för högt | Core-literal match |
| 15299 | 887804195 | `component::neopool::entity::sensor::ph_status_alarm::state::ok` | OK | OK | Core-literal match |
| 15300 | 887804194 | `component::neopool::entity::sensor::ph_status_alarm::name` | pH alarm | pH-larm | Core-literal match |
| 15301 | 887804193 | `component::neopool::entity::sensor::ph_pump_status::state::off` | Off | Av | Shared reference target checked |
| 15302 | 887804192 | `component::neopool::entity::sensor::ph_pump_status::state::idle` | Idle | Inaktiv | Shared reference target checked |
| 15303 | 887804191 | `component::neopool::entity::sensor::ph_pump_status::state::both` | Both pumps | Båda pumparna | Core-literal match |
| 15304 | 887804190 | `component::neopool::entity::sensor::ph_pump_status::state::base` | Base pump | Baspump | Core-literal match |
| 15305 | 887804189 | `component::neopool::entity::sensor::ph_pump_status::state::acid` | Acid pump | Syrapump | Core-literal match |
| 15306 | 887804188 | `component::neopool::entity::sensor::ph_pump_status::name` | pH pump status | pH-pumpstatus | Core-literal match |
| 15307 | 887804187 | `component::neopool::entity::sensor::measure_temperature::name` | Water temperature | Vattentemperatur | Core-literal match |
| 15308 | 887804186 | `component::neopool::entity::sensor::measure_rx::name` | Redox potential | Redoxpotential | Core-literal match |
| 15309 | 887804185 | `component::neopool::entity::sensor::measure_conductivity::name` | Conductivity level | Konduktivitetsnivå | Core-literal match |
| 15310 | 887804184 | `component::neopool::entity::sensor::measure_cl::name` | Salt level | Saltnivå | Core-literal match |
| 15311 | 887804183 | `component::neopool::entity::sensor::ion_polarity::state::pol2` | Polarity 2 | Polaritet 2 | Core-literal match |
| 15312 | 887804182 | `component::neopool::entity::sensor::ion_polarity::state::pol1` | Polarity 1 | Polaritet 1 | Core-literal match |
| 15313 | 887804181 | `component::neopool::entity::sensor::ion_polarity::state::off` | Off | Av | Shared reference target checked |
| 15314 | 887804180 | `component::neopool::entity::sensor::ion_polarity::state::dead_time` | Dead time | Dödtid | Core-literal match |
| 15315 | 887804179 | `component::neopool::entity::sensor::ion_polarity::name` | Ionizer polarity | Joniseringspolaritet | Core-literal match |
| 15316 | 887804178 | `component::neopool::entity::sensor::ion_current::name` | Ionization level | Joniseringsnivå | Core-literal match |
| 15317 | 887804177 | `component::neopool::entity::sensor::intelligent_tt_next_interval::name` | Intelligent mode next interval start | Nästa intervallstart i intelligent läge | Core-literal match |
| 15318 | 887804176 | `component::neopool::entity::sensor::intelligent_intervals::name` | Intelligent mode intervals | Intervall i intelligent läge | Core-literal match |
| 15319 | 887804175 | `component::neopool::entity::sensor::hidro_voltage::name` | Hydrolysis voltage | Hydrolysspänning | Core-literal match |
| 15320 | 887804174 | `component::neopool::entity::sensor::hidro_polarity::state::pol2` | Polarity 2 | Polaritet 2 | Core-literal match |
| 15321 | 887804173 | `component::neopool::entity::sensor::hidro_polarity::state::pol1` | Polarity 1 | Polaritet 1 | Core-literal match |
| 15322 | 887804172 | `component::neopool::entity::sensor::hidro_polarity::state::off` | Off | Av | Shared reference target checked |
| 15323 | 887804171 | `component::neopool::entity::sensor::hidro_polarity::state::no_flow` | No flow | Inget flöde | Core-literal match |
| 15324 | 887804170 | `component::neopool::entity::sensor::hidro_polarity::state::dead_time` | Dead time | Dödtid | Core-literal match |
| 15325 | 887804169 | `component::neopool::entity::sensor::hidro_polarity::name` | Hydrolysis polarity | Hydrolyspolaritet | Core-literal match |
| 15326 | 887804168 | `component::neopool::entity::sensor::hidro_current::name` | Hydrolysis intensity | Hydrolysintensitet | Core-literal match |
| 15327 | 887804167 | `component::neopool::entity::sensor::filtvalve_remaining::name` | Backwash time remaining | Återstående backspolningstid | Core-literal match |
| 15328 | 887804166 | `component::neopool::entity::sensor::filtration_speed::state::off` | Off | Av | Shared reference target checked |
| 15329 | 887804165 | `component::neopool::entity::sensor::filtration_speed::state::mid` | Medium | Medel | Core-literal match |
| 15330 | 887804164 | `component::neopool::entity::sensor::filtration_speed::state::low` | Low | Låg | Shared reference target checked |
| 15331 | 887804163 | `component::neopool::entity::sensor::filtration_speed::state::high` | High | Hög | Shared reference target checked |
| 15332 | 887804162 | `component::neopool::entity::sensor::filtration_speed::name` | Current filtration speed | Aktuell filtreringshastighet | Core-literal match |
| 15333 | 887804161 | `component::neopool::entity::sensor::filt_mode::state::smart` | Smart | Smart | Core-literal match |
| 15334 | 887804160 | `component::neopool::entity::sensor::filt_mode::state::manual` | Manual | Manuell | Shared reference target checked |
| 15335 | 887804159 | `component::neopool::entity::sensor::filt_mode::state::intelligent` | Intelligent | Intelligent | Core-literal match |
| 15336 | 887804158 | `component::neopool::entity::sensor::filt_mode::state::heating` | Heating | Uppvärmning | Core-literal match |
| 15337 | 887804157 | `component::neopool::entity::sensor::filt_mode::state::backwash` | Backwash | Backspolning | Core-literal match |
| 15338 | 887804156 | `component::neopool::entity::sensor::filt_mode::state::auto` | Automatic | Automatisk | Core-literal match |
| 15339 | 887804155 | `component::neopool::entity::sensor::filt_mode::name` | Filtration mode | Filtreringsläge | Core-literal match |
| 15340 | 887804154 | `component::neopool::entity::sensor::cell_runtime_total::name` | Cell runtime total | Cellens totala drifttid | Core-literal match |
| 15341 | 887804153 | `component::neopool::entity::sensor::cell_runtime_polb::name` | Cell runtime in polarity 2 | Cellens drifttid polaritet 2 | Core-literal match |
| 15342 | 887804152 | `component::neopool::entity::sensor::cell_runtime_pola::name` | Cell runtime in polarity 1 | Cellens drifttid polaritet 1 | Core-literal match |
| 15343 | 887804151 | `component::neopool::entity::sensor::cell_runtime_pol_changes::name` | Cell polarity changes | Cellpolaritetsförändringar | Core-literal match |
| 15344 | 887804150 | `component::neopool::entity::sensor::cell_runtime_part::name` | Cell runtime since reset | Cellens drifttid sedan återställningen | Core-literal match |
| 15345 | 887804149 | `component::neopool::config::step::user::title` | NeoPool Connection | NeoPool-anslutning | Core-literal match |
| 15346 | 887804148 | `component::neopool::config::step::user::description` | Choose how your NeoPool controller is reached. | Konfigurera anslutningen till din NeoPool-styrenhet. | Core-literal match |
| 15347 | 887804147 | `component::neopool::config::step::user::data_description::unit_id` | Modbus device address (1-247). Identifies the specific device on a shared bus. Most direct-connected devices use 1. Gateways may route requests to different addresses. | Modbus-enhetsadress (1–247). Identifierar den specifika enheten på en delad buss. De flesta direktanslutna enheter använder adress 1. Gateway-enheter kan dirigera förfrågningar till olika adresser. | Source-path follow-up open |
| 15348 | 887804146 | `component::neopool::config::step::user::data_description::port` | Standard Modbus TCP port (default: 502). Change only if your gateway uses a non-standard port. | Standardport för Modbus TCP (standard: 502). Ändra endast om din gateway använder en icke-standardport. | Source-path follow-up open |
| 15349 | 887804145 | `component::neopool::config::step::user::data_description::modbus_framer` | Wire protocol used by the gateway. Select TCP for MBAP framing (default for Ethernet-native gateways). Select RTU for RTU framing tunnelled through a TCP socket, used by passthrough serial-to-TCP bridges like ESPHome's stream_server. | Det nätverksprotokoll som används av gatewayen. Välj TCP för MBAP-framing (standardinställning för Ethernet-baserade gateways). Välj RTU för RTU-framing som tunnlas via en TCP-socket, vilket används av passthrough mellan seriell anslutning och TCP, såsom ESPHomes stream_server. | Source-path follow-up open |
| 15350 | 887804144 | `component::neopool::config::step::user::data_description::host` | Enter the IP address of the Modbus TCP gateway connected to your pool controller. | Ange IP-adressen för Modbus TCP-gatewayen som är ansluten till din poolregulator. | Source-path follow-up open |
| 15351 | 887804143 | `component::neopool::config::step::user::data::unit_id` | Unit ID | Enhets-ID | Source-path follow-up open |
| 15352 | 887804142 | `component::neopool::config::step::user::data::port` | Port | Port | Source-path follow-up open |
| 15353 | 887804141 | `component::neopool::config::step::user::data::modbus_framer` | Modbus framer | Modbus-framer | Source-path follow-up open |
| 15354 | 887804140 | `component::neopool::config::step::user::data::host` | Host | Värd | Source-path follow-up open |
| 15355 | 887804139 | `component::neopool::config::error::cannot_read_modbus` | Connected, but cannot read from the Modbus device. Check the unit ID and the connection settings. | Ansluten, men kan inte läsa från Modbus-enheten. Kontrollera enhets-ID och framer-inställningar. | Core-literal match |
| 15356 | 887804138 | `component::neopool::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15357 | 887804137 | `component::neopool::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 15358 | 887753450 | `component::data_grand_lyon::exceptions::update_failed_park_and_ride::message` | Error fetching park & ride availability from Data Grand Lyon. | Fel vid hämtning av tillgänglighet för infartsparkering från Data Grand Lyon. | Core-literal match |
| 15359 | 887753449 | `component::data_grand_lyon::entity::sensor::park_and_ride_capacity::unit_of_measurement` | spaces | platser | Shared reference target checked |
| 15360 | 887753448 | `component::data_grand_lyon::entity::sensor::park_and_ride_capacity::name` | Capacity | Kapacitet | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 888596795 | `component::luci::config::abort::reauth_successful` | Re-authentication was successful |
| 888090341 | `component::google_health::config::abort::reauth_successful` | Re-authentication was successful |
| 887931062 | `component::stiebel_eltron::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 887909722 | `component::google_health::exceptions::oauth_error::message` | OAuth2 implementation temporarily unavailable. |
| 887909713 | `component::google_health::config::abort::user_rejected_authorize` | Account linking rejected: {error} |
| 887909712 | `component::google_health::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. |
| 887909711 | `component::google_health::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. |
| 887909710 | `component::google_health::config::abort::oauth_implementation_unavailable` | No OAuth2 implementations are currently available. |
| 887909709 | `component::google_health::config::abort::oauth_failed` | Error while obtaining access token. |
| 887909708 | `component::google_health::config::abort::oauth_error` | Received invalid token data. |
| 887909707 | `component::google_health::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) |
| 887909703 | `component::google_health::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. |
| 887909702 | `component::google_health::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 887804147 | `component::neopool::config::step::user::data_description::unit_id` | Modbus device address (1-247). Identifies the specific device on a shared bus. Most direct-connected devices use 1. Gateways may route requests to different addresses. |
| 887804146 | `component::neopool::config::step::user::data_description::port` | Standard Modbus TCP port (default: 502). Change only if your gateway uses a non-standard port. |
| 887804145 | `component::neopool::config::step::user::data_description::modbus_framer` | Wire protocol used by the gateway. Select TCP for MBAP framing (default for Ethernet-native gateways). Select RTU for RTU framing tunnelled through a TCP socket, used by passthrough serial-to-TCP bridges like ESPHome's stream_server. |
| 887804144 | `component::neopool::config::step::user::data_description::host` | Enter the IP address of the Modbus TCP gateway connected to your pool controller. |
| 887804143 | `component::neopool::config::step::user::data::unit_id` | Unit ID |
| 887804142 | `component::neopool::config::step::user::data::port` | Port |
| 887804141 | `component::neopool::config::step::user::data::modbus_framer` | Modbus framer |
| 887804140 | `component::neopool::config::step::user::data::host` | Host |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
