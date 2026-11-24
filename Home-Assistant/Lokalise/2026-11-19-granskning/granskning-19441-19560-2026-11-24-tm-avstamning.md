# Home Assistant Core – historisk avstämning 19441–19560

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 47 direkta källtexter matchar HA Core-källan; 72 referensanvändningar med 30 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 1 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19441 | 837969251 | `component::nobo_hub::config::step::user::data_description::device` | Select the Nobø Ecohub discovered on your local network, or choose manual entry. | Välj den Nobø Ecohub som upptäckts i ditt lokala nätverk, eller välj manuell inmatning. | Core-literal match |
| 19442 | 837969250 | `component::nobo_hub::config::step::selected::data_description::serial_suffix` | The last 3 digits of the serial number printed on the back of your Nobø Ecohub. | De sista 3 siffrorna i serienumret som är tryckt på baksidan av din Nobø Ecohub. | Core-literal match |
| 19443 | 837969249 | `component::nobo_hub::config::step::manual::data_description::serial` | The full 12-digit serial number printed on the back of your Nobø Ecohub. | Det fullständiga 12-siffriga serienumret som är tryckt på baksidan av din Nobø Ecohub. | Core-literal match |
| 19444 | 837969248 | `component::nobo_hub::config::step::manual::data_description::ip_address` | The IP address of your Nobø Ecohub. | IP-adressen för din Nobø Ecohub. | Core-literal match |
| 19445 | 837791804 | `component::unifi::exceptions::remove_clients_request_failed::message` | Failed to remove clients from UniFi Network | Misslyckades med att ta bort klienter från UniFi-nätverket | Core-literal match |
| 19446 | 837791803 | `component::unifi::exceptions::reconnect_client_request_failed::message` | Failed to send reconnect request to UniFi Network | Misslyckades med att skicka begäran om återanslutning till UniFi-nätverket | Core-literal match |
| 19447 | 837791802 | `component::unifi::exceptions::reconnect_client_no_mac::message` | Unable to reconnect client: device does not have a network MAC address | Det går inte att återansluta klienten: enheten har ingen MAC-adress i nätverket | Core-literal match |
| 19448 | 837791801 | `component::unifi::exceptions::reconnect_client_device_not_found::message` | Unable to reconnect client: device not found | Det går inte att återansluta klienten: enheten hittades inte | Core-literal match |
| 19449 | 837791800 | `component::unifi::exceptions::action_request_failed::message` | Failed to send action request to UniFi Network | Det gick inte att skicka åtgärdsbegäran till UniFi Network | Core-literal match |
| 19450 | 837724292 | `component::sonos::exceptions::toggle_failed::message` | Could not toggle {entity_id}. | Det gick inte att växla {entity_id}. | Core-literal match |
| 19451 | 837724291 | `component::sonos::entity::switch::ungroup_on_autoplay::name` | Ungroup on autoplay | Avgruppera vid autouppspelning | Core-literal match |
| 19452 | 837724290 | `component::sonos::entity::switch::tv_autoplay::name` | TV autoplay | TV-autouppspelning | Core-literal match |
| 19453 | 837700447 | `component::kiosker::entity::binary_sensor::screensaver_state::name` | Screensaver | Skärmsläckare | Core-literal match |
| 19454 | 837700446 | `component::kiosker::entity::binary_sensor::blackout_state::name` | Blackout | Mörkläggningsläge | Core-literal match |
| 19455 | 837698641 | `component::doorbell::triggers::rang::name` | Doorbell rang | Dörrklocka ringde | Core-literal match |
| 19456 | 837698640 | `component::doorbell::triggers::rang::description` | Triggers when one or more doorbells ring. | Utlöses när en eller flera dörrklockor ringer. | Core-literal match |
| 19457 | 837698639 | `component::doorbell::title` | Doorbell | Dörrklocka | Core-literal match |
| 19458 | 837648293 | `component::water_heater::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19459 | 837648292 | `component::water_heater::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19460 | 837648291 | `component::vacuum::conditions::is_returning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19461 | 837648290 | `component::vacuum::conditions::is_paused::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19462 | 837648289 | `component::vacuum::conditions::is_encountering_an_error::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19463 | 837648288 | `component::vacuum::conditions::is_docked::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19464 | 837648287 | `component::vacuum::conditions::is_cleaning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19465 | 837648286 | `component::vacuum::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19466 | 837648285 | `component::update::conditions::is_not_available::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19467 | 837648284 | `component::update::conditions::is_available::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19468 | 837648283 | `component::update::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19469 | 837648282 | `component::todo::conditions::all_completed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19470 | 837648281 | `component::todo::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19471 | 837648280 | `component::timer::conditions::is_paused::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19472 | 837648279 | `component::timer::conditions::is_idle::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19473 | 837648278 | `component::timer::conditions::is_active::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19474 | 837648277 | `component::timer::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19475 | 837648276 | `component::switch::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19476 | 837648275 | `component::switch::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19477 | 837648274 | `component::switch::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19478 | 837648273 | `component::siren::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19479 | 837648272 | `component::siren::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19480 | 837648271 | `component::siren::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19481 | 837648270 | `component::schedule::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19482 | 837648269 | `component::schedule::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19483 | 837648268 | `component::schedule::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19484 | 837648267 | `component::remote::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19485 | 837648266 | `component::remote::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19486 | 837648265 | `component::remote::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19487 | 837648264 | `component::occupancy::conditions::is_not_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19488 | 837648263 | `component::occupancy::conditions::is_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19489 | 837648262 | `component::occupancy::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19490 | 837648261 | `component::moisture::conditions::is_not_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19491 | 837648260 | `component::moisture::conditions::is_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19492 | 837648259 | `component::moisture::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19493 | 837648258 | `component::media_player::conditions::is_playing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19494 | 837648257 | `component::media_player::conditions::is_paused::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19495 | 837648256 | `component::media_player::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19496 | 837648255 | `component::media_player::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19497 | 837648254 | `component::lock::conditions::is_unlocked::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19498 | 837648253 | `component::lock::conditions::is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19499 | 837648252 | `component::lock::conditions::is_locked::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19500 | 837648251 | `component::lock::conditions::is_jammed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19501 | 837648250 | `component::lock::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19502 | 837648249 | `component::light::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19503 | 837648248 | `component::light::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19504 | 837648247 | `component::light::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19505 | 837648246 | `component::lawn_mower::conditions::is_returning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19506 | 837648245 | `component::lawn_mower::conditions::is_paused::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19507 | 837648244 | `component::lawn_mower::conditions::is_mowing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19508 | 837648243 | `component::lawn_mower::conditions::is_encountering_an_error::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19509 | 837648242 | `component::lawn_mower::conditions::is_docked::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19510 | 837648241 | `component::lawn_mower::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19511 | 837648240 | `component::illuminance::conditions::is_not_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19512 | 837648239 | `component::illuminance::conditions::is_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19513 | 837648238 | `component::illuminance::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19514 | 837648237 | `component::humidifier::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19515 | 837648236 | `component::humidifier::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19516 | 837648235 | `component::humidifier::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19517 | 837648234 | `component::fan::conditions::is_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19518 | 837648233 | `component::fan::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19519 | 837648232 | `component::fan::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19520 | 837648231 | `component::climate::conditions::is_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19521 | 837648230 | `component::climate::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19522 | 837648229 | `component::calendar::conditions::is_event_active::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19523 | 837648228 | `component::calendar::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19524 | 837648227 | `component::battery::conditions::is_not_low::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19525 | 837648226 | `component::battery::conditions::is_not_charging::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19526 | 837648225 | `component::battery::conditions::is_low::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19527 | 837648224 | `component::battery::conditions::is_charging::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19528 | 837648223 | `component::battery::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19529 | 837648222 | `component::assist_satellite::conditions::is_responding::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19530 | 837648221 | `component::assist_satellite::conditions::is_processing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19531 | 837648220 | `component::assist_satellite::conditions::is_listening::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19532 | 837648219 | `component::assist_satellite::conditions::is_idle::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19533 | 837648218 | `component::assist_satellite::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19534 | 837648217 | `component::alarm_control_panel::conditions::is_triggered::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19535 | 837648216 | `component::alarm_control_panel::conditions::is_disarmed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19536 | 837648215 | `component::alarm_control_panel::conditions::is_armed_vacation::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19537 | 837648214 | `component::alarm_control_panel::conditions::is_armed_night::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19538 | 837648213 | `component::alarm_control_panel::conditions::is_armed_home::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19539 | 837648212 | `component::alarm_control_panel::conditions::is_armed_away::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19540 | 837648211 | `component::alarm_control_panel::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19541 | 837648210 | `component::air_quality::conditions::is_smoke_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19542 | 837648209 | `component::air_quality::conditions::is_smoke_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19543 | 837648208 | `component::air_quality::conditions::is_gas_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19544 | 837648207 | `component::air_quality::conditions::is_gas_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19545 | 837648206 | `component::air_quality::conditions::is_co_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19546 | 837648205 | `component::air_quality::conditions::is_co_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19547 | 837648204 | `component::air_quality::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19548 | 837382979 | `component::iaqualink::config::step::user::data_description::username` | The email address used to sign in to your account using the iAquaLink app or website. | E-postadressen som används för att logga in på ditt konto med iAquaLink-appen eller webbplatsen. | Core-literal match |
| 19549 | 837382978 | `component::iaqualink::config::step::user::data_description::password` | The password associated with your account. | Lösenordet som är kopplat till ditt konto. | Core-literal match |
| 19550 | 837382977 | `component::iaqualink::config::step::reauth_confirm::data_description::username` | The email address used to sign in to your account using the iAquaLink app or website. | E-postadressen som används för att logga in på ditt konto med iAquaLink-appen eller webbplatsen. | Shared reference target checked |
| 19551 | 837382976 | `component::iaqualink::config::step::reauth_confirm::data_description::password` | The password associated with your account. | Lösenordet som är kopplat till ditt konto. | Shared reference target checked |
| 19552 | 837323633 | `component::fumis::config::step::reauth_confirm::description` | The PIN code for your stove has changed. Please enter the new PIN code to re-authenticate. | PIN-koden för din spis har ändrats. Ange den nya PIN-koden för att autentisera dig på nytt. | Core-literal match |
| 19553 | 837323632 | `component::fumis::config::step::reauth_confirm::data_description::pin` | You can find the PIN code on the label of the Fumis WiRCU Wi-Fi module connected to your stove. | PIN-koden finns på etiketten på den Fumis WiRCU Wi-Fi-modul som är ansluten till din kamin. | Shared reference target checked |
| 19554 | 837323631 | `component::fumis::config::step::reauth_confirm::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 19555 | 837323630 | `component::fumis::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 19556 | 837199441 | `component::telegram_bot::exceptions::invalid_file_name::message` | Invalid file name: {file_name}. The file name must not contain `~`, `..`, `/` or `\`. | Ogiltigt filnamn: {file_name}. Filnamnet får inte innehålla `~`, `..`, `/` eller `\`. | Core-literal match |
| 19557 | 837199440 | `component::telegram_bot::exceptions::invalid_directory_path::message` | Invalid directory path: {directory_path}. The path must not contain `~` or `..`. | Ogiltig katalogväg: {directory_path}. Sökvägen får inte innehålla `~` eller `..`. | Core-literal match |
| 19558 | 837199439 | `component::duco::config::step::reconfigure::data_description::host` | IP address or hostname of your Duco ventilation box. | IP-adress eller värdnamn för din Duco-ventilationsbox. | Shared reference target checked |
| 19559 | 837199438 | `component::duco::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 19560 | 837199437 | `component::duco::config::abort::unique_id_mismatch` | The device you entered belongs to a different Duco box. | Enheten du angav tillhör en annan Duco-box. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 837323630 | `component::fumis::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
