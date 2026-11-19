# Home Assistant Core – granskning 331–420

Strängar i ordningen ”Last added” vid insamlingen. De första elva svenska fälten var tomma. Inga ändringar har gjorts i Lokalise. Referenser återges oförändrade när måltext saknas; synliga upplösningar av referenser kontrolleras i sitt sammanhang.

## 331. `component::intesis_modbus::config::abort::unsupported_brand`

**Engelska:** This is a {brand} gateway. Its code and error tables are not written yet, so it cannot be set up. See the intesis-gw-modbus library for how to contribute them.

**Befintlig svenska:** Saknas

**Förslag:** Det här är en {brand}-gateway. Dess kod- och feltabeller är ännu inte implementerade, så den kan inte konfigureras. Se biblioteket intesis-gw-modbus för information om hur du kan bidra med dem.

## 332. `component::intesis_modbus::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_device%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:common::config_flow::abort::already_configured_device%]

## 333. `component::braviatv::config::step::reconfigure::description`

**Engelska:** Update the hostname or IP address of your Sony Bravia TV. The existing authorization is kept, so make sure the TV is turned on.

**Befintlig svenska:** Saknas

**Förslag:** Uppdatera värdnamnet eller IP-adressen för din Sony Bravia-tv. Den befintliga auktoriseringen behålls, så kontrollera att tv:n är påslagen.

## 334. `component::braviatv::config::step::reconfigure::data_description::host`

**Engelska:** [%key:component::braviatv::config::step::user::data_description::host%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:component::braviatv::config::step::user::data_description::host%]

## 335. `component::braviatv::config::step::reconfigure::data::host`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:common::config_flow::data::host%]

## 336. `component::braviatv::config::abort::unique_id_mismatch`

**Engelska:** The host you entered belongs to a different Bravia TV.

**Befintlig svenska:** Saknas

**Förslag:** Värden du angav tillhör en annan Bravia-tv.

## 337. `component::nws::config::step::reconfigure::data_description::station`

**Engelska:** If not specified, the closest station to the configured location will be used.

**Befintlig svenska:** Saknas

**Förslag:** Om ingen station anges används stationen som ligger närmast den konfigurerade platsen.

## 338. `component::nws::config::step::reconfigure::data_description::location_entity`

**Engelska:** [%key:component::nws::config::step::entity::data_description::location_entity%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:component::nws::config::step::entity::data_description::location_entity%]

## 339. `component::nws::config::step::reconfigure::data::station`

**Engelska:** [%key:component::nws::config::step::location::data::station%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:component::nws::config::step::location::data::station%]

## 340. `component::nws::config::step::reconfigure::data::location_entity`

**Engelska:** [%key:component::nws::config::step::entity::data::location_entity%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:component::nws::config::step::entity::data::location_entity%]

## 341. `component::nws::config::step::reconfigure::data::api_key`

**Engelska:** [%key:common::config_flow::data::api_key%]

**Befintlig svenska:** Saknas

**Förslag:** [%key:common::config_flow::data::api_key%]

## 342. `component::meteoalarm::issues::deprecated_yaml_import_issue_invalid_country::title`

**Engelska:** [%key:component::meteoalarm::issues::deprecated_yaml_import_issue_cannot_connect::title%]

**Befintlig svenska:** Det gick inte att importera MeteoAlarms YAML-konfiguration

**Bedömning:** Ingen ändring föreslås.

## 343. `component::meteoalarm::issues::deprecated_yaml_import_issue_invalid_country::description`

**Engelska:** Configuring MeteoAlarm using YAML is being removed, but your configuration for {province} ({country}) could not be imported because MeteoAlarm has no feed for that country.

Correct the country in your YAML configuration and restart Home Assistant, or remove the `meteoalarm` binary sensor from your configuration.yaml and add the integration in the UI.

**Befintlig svenska:** Konfiguration av MeteoAlarm med YAML håller på att tas bort, men din konfiguration för {province} ({country}) kunde inte importeras eftersom MeteoAlarm inte har något flöde för landet.

Rätta landet i YAML-konfigurationen och starta om Home Assistant, eller ta bort binärsensorn `meteoalarm` från configuration.yaml och lägg till integrationen i gränssnittet.

**Bedömning:** Ingen ändring föreslås.

## 344. `component::meteoalarm::issues::deprecated_yaml_import_issue_cannot_connect::title`

**Engelska:** The MeteoAlarm YAML configuration import failed

**Befintlig svenska:** Det gick inte att importera MeteoAlarms YAML-konfiguration

**Bedömning:** Ingen ändring föreslås.

## 345. `component::meteoalarm::issues::deprecated_yaml_import_issue_cannot_connect::description`

**Engelska:** Configuring MeteoAlarm using YAML is being removed, but your configuration for {province} ({country}) could not be imported because MeteoAlarm could not be reached.

Check your internet connection and restart Home Assistant to try again, or remove the `meteoalarm` binary sensor from your configuration.yaml and add the integration in the UI.

**Befintlig svenska:** Konfiguration av MeteoAlarm med YAML håller på att tas bort, men din konfiguration för {province} ({country}) kunde inte importeras eftersom det inte gick att nå MeteoAlarm.

Kontrollera din internetanslutning och starta om Home Assistant för att försöka igen, eller ta bort binärsensorn `meteoalarm` från configuration.yaml och lägg till integrationen i gränssnittet.

**Bedömning:** Ingen ändring föreslås.

## 346. `component::meteoalarm::config::step::user::description`

**Engelska:** Get weather warnings for a region from MeteoAlarm.

**Befintlig svenska:** Hämta vädervarningar för en region från MeteoAlarm.

**Bedömning:** Ingen ändring föreslås.

## 347. `component::meteoalarm::config::step::user::data_description::province`

**Engelska:** The region's name as MeteoAlarm shows it, or its EMMA_ID code. You can find both on meteoalarm.org.

**Befintlig svenska:** Regionens namn så som det visas i MeteoAlarm, eller dess EMMA_ID-kod. Du hittar båda på meteoalarm.org.

**Bedömning:** Ingen ändring föreslås.

## 348. `component::meteoalarm::config::step::user::data_description::language`

**Engelska:** The language for the warning texts. Warnings not available in this language are shown in the first language the feed has.

**Befintlig svenska:** Språket för varningstexterna. Varningar som inte finns på detta språk visas på det första språk som flödet har.

**Bedömning:** Ingen ändring föreslås.

## 349. `component::meteoalarm::config::step::user::data_description::country`

**Engelska:** The country whose MeteoAlarm feed to use.

**Befintlig svenska:** Landet vars MeteoAlarm-flöde ska användas.

**Bedömning:** Ingen ändring föreslås.

## 350. `component::meteoalarm::config::step::user::data::province`

**Engelska:** Region

**Befintlig svenska:** Region

**Bedömning:** Ingen ändring föreslås.

## 351. `component::meteoalarm::config::step::user::data::language`

**Engelska:** [%key:common::config_flow::data::language%]

**Befintlig svenska:** Språk

**Bedömning:** Ingen ändring föreslås.

## 352. `component::meteoalarm::config::step::user::data::country`

**Engelska:** [%key:common::config_flow::data::country%]

**Befintlig svenska:** Land

**Bedömning:** Ingen ändring föreslås.

## 353. `component::meteoalarm::config::error::invalid_country`

**Engelska:** MeteoAlarm has no warnings feed for this country.

**Befintlig svenska:** MeteoAlarm har inget varningsflöde för det här landet.

**Bedömning:** Ingen ändring föreslås.

## 354. `component::meteoalarm::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Bedömning:** Ingen ändring föreslås.

## 355. `component::meteoalarm::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_service%]

**Befintlig svenska:** Tjänsten är redan konfigurerad

**Bedömning:** Ingen ändring föreslås.

## 356. `component::zonneplan::services::get_electricity_prices::name`

**Engelska:** Get electricity prices

**Befintlig svenska:** Hämta elpriser

**Bedömning:** Ingen ändring föreslås.

## 357. `component::zonneplan::services::get_electricity_prices::fields::interval::name`

**Engelska:** Interval

**Befintlig svenska:** Intervall

**Bedömning:** Ingen ändring föreslås.

## 358. `component::zonneplan::services::get_electricity_prices::fields::interval::description`

**Engelska:** Whether to return a price per hour or per quarter hour.

**Befintlig svenska:** Om ett pris per timme eller kvart ska returneras.

**Bedömning:** Ingen ändring föreslås.

## 359. `component::zonneplan::services::get_electricity_prices::fields::config_entry::name`

**Engelska:** Config entry

**Befintlig svenska:** Konfigurationspost

**Bedömning:** Ingen ändring föreslås.

## 360. `component::zonneplan::services::get_electricity_prices::fields::config_entry::description`

**Engelska:** The Zonneplan config entry to get the prices of.

**Befintlig svenska:** Zonneplan-konfigurationsposten vars priser ska hämtas.

**Bedömning:** Ingen ändring föreslås.

## 361. `component::zonneplan::services::get_electricity_prices::description`

**Engelska:** Returns the all-in electricity prices from Zonneplan.

**Befintlig svenska:** Returnerar elpriserna inklusive allt från Zonneplan.

**Förslag:** Returnerar de totala elpriserna från Zonneplan.

## 362. `component::zonneplan::selector::interval::options::quarter`

**Engelska:** Quarter hour

**Befintlig svenska:** Kvart

**Bedömning:** Ingen ändring föreslås.

## 363. `component::zonneplan::selector::interval::options::hour`

**Engelska:** Hour

**Befintlig svenska:** Timme

**Bedömning:** Ingen ändring föreslås.

## 364. `component::zonneplan::exceptions::no_electricity_prices::message`

**Engelska:** The Zonneplan account has no electricity prices

**Befintlig svenska:** Zonneplan-kontot har inga elpriser

**Bedömning:** Ingen ändring föreslås.

## 365. `component::yardian::exceptions::invalid_auth::message`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** Ogiltig autentisering

**Bedömning:** Ingen ändring föreslås.

## 366. `component::yardian::exceptions::cannot_connect::message`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Bedömning:** Ingen ändring föreslås.

## 367. `component::xiaomi_miio::services::switch_set_power_price::fields::price::name`

**Engelska:** Price

**Befintlig svenska:** Pris

**Bedömning:** Ingen ändring föreslås.

## 368. `component::xiaomi_miio::services::switch_set_power_price::fields::price::description`

**Engelska:** Power price.

**Befintlig svenska:** Elpris.

**Bedömning:** Ingen ändring föreslås.

## 369. `component::daikin::exceptions::unsupported_device::message`

**Engelska:** This Daikin adapter has no local control API. Control the device through the Daikin cloud/Onecta app.

**Befintlig svenska:** Den här Daikin-adaptern har inget lokalt API för styrning. Styr enheten via Daikin Cloud-/Onecta-appen.

**Förslag:** Den här Daikin-adaptern har inget lokalt API för styrning. Styr enheten via Daikins molntjänst eller appen Onecta.

## 370. `component::daikin::config::abort::unsupported_device`

**Engelska:** This Daikin adapter has no local control API. BRP069C4x/C8x require firmware 2.8.0 or later, while built-in adapters such as the Stylish FTXA20C2V1BW have no local API at all (2.6.3 is the latest firmware). Control the device through the Daikin cloud/Onecta app.

**Befintlig svenska:** Den här Daikin-adaptern har inget lokalt API för styrning. BRP069C4x/C8x kräver inbyggd programvara 2.8.0 eller senare, medan inbyggda adaptrar som Stylish FTXA20C2V1BW helt saknar lokalt API (2.6.3 är den senaste versionen av den inbyggda programvaran). Styr enheten via Daikin Cloud-/Onecta-appen.

**Förslag:** Den här Daikin-adaptern har inget lokalt API för styrning. BRP069C4x/C8x kräver inbyggd programvara 2.8.0 eller senare, medan inbyggda adaptrar som Stylish FTXA20C2V1BW helt saknar lokalt API (2.6.3 är den senaste versionen av den inbyggda programvaran). Styr enheten via Daikins molntjänst eller appen Onecta.

## 371. `component::tuya::entity::sensor::reactive_power::name`

**Engelska:** [%key:component::sensor::entity_component::reactive_power::name%]

**Befintlig svenska:** Reaktiv effekt

**Bedömning:** Ingen ändring föreslås.

## 372. `component::tuya::entity::sensor::outlet_temperature::name`

**Engelska:** Outlet temperature

**Befintlig svenska:** Utloppstemperatur

**Bedömning:** Ingen ändring föreslås.

## 373. `component::tuya::entity::sensor::inlet_temperature::name`

**Engelska:** Inlet temperature

**Befintlig svenska:** Inloppstemperatur

**Bedömning:** Ingen ändring föreslås.

## 374. `component::trimlight::exceptions::update_failed::message`

**Engelska:** Unable to update the state of {name}: {error}

**Befintlig svenska:** Det gick inte att uppdatera tillståndet för {name}: {error}

**Bedömning:** Ingen ändring föreslås.

## 375. `component::trimlight::exceptions::setup_failed::message`

**Engelska:** Failed to set up {name}: {error}

**Befintlig svenska:** Det gick inte att konfigurera {name}: {error}

**Bedömning:** Ingen ändring föreslås.

## 376. `component::trimlight::exceptions::command_failed::message`

**Engelska:** Failed to control {name}: {error}

**Befintlig svenska:** Det gick inte att styra {name}: {error}

**Bedömning:** Ingen ändring föreslås.

## 377. `component::trimlight::config::step::zeroconf_confirm::title`

**Engelska:** Add Trimlight controller

**Befintlig svenska:** Lägg till Trimlight-styrenhet

**Bedömning:** Ingen ändring föreslås.

## 378. `component::trimlight::config::step::zeroconf_confirm::description`

**Engelska:** Add {name} at {host} to Home Assistant?

**Befintlig svenska:** Vill du lägga till {name} på {host} i Home Assistant?

**Bedömning:** Ingen ändring föreslås.

## 379. `component::trimlight::config::step::user::data_description::host`

**Engelska:** The hostname or IP address of your Trimlight controller.

**Befintlig svenska:** Värdnamnet eller IP-adressen för Trimlight-styrenheten.

**Bedömning:** Ingen ändring föreslås.

## 380. `component::trimlight::config::step::user::data::host`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** Värd

**Bedömning:** Ingen ändring föreslås.

## 381. `component::trimlight::config::flow_title`

**Engelska:** {name}

**Befintlig svenska:** {name}

**Bedömning:** Ingen ändring föreslås.

## 382. `component::trimlight::config::error::invalid_response`

**Engelska:** [%key:component::trimlight::config::abort::invalid_response%]

**Befintlig svenska:** Styrenheten returnerade ett ogiltigt svar

**Bedömning:** Ingen ändring föreslås.

## 383. `component::trimlight::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Bedömning:** Ingen ändring föreslås.

## 384. `component::trimlight::config::abort::invalid_response`

**Engelska:** The controller returned an invalid response

**Befintlig svenska:** Styrenheten returnerade ett ogiltigt svar

**Bedömning:** Ingen ändring föreslås.

## 385. `component::trimlight::config::abort::invalid_discovery_info`

**Engelska:** The discovery data from the controller is invalid

**Befintlig svenska:** Upptäcktsdata från styrenheten är ogiltiga

**Bedömning:** Ingen ändring föreslås.

## 386. `component::trimlight::config::abort::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Bedömning:** Ingen ändring föreslås.

## 387. `component::trimlight::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_device%]

**Befintlig svenska:** Enheten är redan konfigurerad

**Bedömning:** Ingen ändring föreslås.

## 388. `component::system_bridge::exceptions::media_url_failed::message`

**Engelska:** System Bridge couldn't make a link to {path}

**Befintlig svenska:** System Bridge kunde inte skapa en länk till {path}

**Bedömning:** Ingen ändring föreslås.

## 389. `component::system_bridge::config::error::invalid_pairing_code`

**Engelska:** That pairing code has been used or has expired. Make a new one in System Bridge.

**Befintlig svenska:** Den här parkopplingskoden har redan använts eller löpt ut. Skapa en ny i System Bridge.

**Bedömning:** Ingen ändring föreslås.

## 390. `component::swiss_public_transport::selector::transportations::options::tram`

**Engelska:** Tram

**Befintlig svenska:** Spårvagn

**Bedömning:** Ingen ändring föreslås.

## 391. `component::swiss_public_transport::selector::transportations::options::train`

**Engelska:** Train

**Befintlig svenska:** Tåg

**Bedömning:** Ingen ändring föreslås.

## 392. `component::swiss_public_transport::selector::transportations::options::ship`

**Engelska:** Ship

**Befintlig svenska:** Fartyg

**Bedömning:** Ingen ändring föreslås.

## 393. `component::swiss_public_transport::selector::transportations::options::cableway`

**Engelska:** Cableway

**Befintlig svenska:** Linbana

**Bedömning:** Ingen ändring föreslås.

## 394. `component::swiss_public_transport::selector::transportations::options::bus`

**Engelska:** Bus

**Befintlig svenska:** Buss

**Bedömning:** Ingen ändring föreslås.

## 395. `component::swiss_public_transport::config::step::user::data_description::transportations`

**Engelska:** Only show connections using the selected means of transport. Leave empty to allow all.

**Befintlig svenska:** Visa bara förbindelser med de valda transportmedlen. Lämna tomt för att tillåta alla.

**Bedömning:** Ingen ändring föreslås.

## 396. `component::swiss_public_transport::config::step::user::data::transportations`

**Engelska:** Means of transport

**Befintlig svenska:** Transportmedel

**Bedömning:** Ingen ändring föreslås.

## 397. `component::amazon_polly::exceptions::unknown_voice::message`

**Engelska:** Voice {voice} is not available.

**Befintlig svenska:** Rösten {voice} är inte tillgänglig.

**Bedömning:** Ingen ändring föreslås.

## 398. `component::amazon_polly::exceptions::synthesis_failed::message`

**Engelska:** Amazon Polly could not synthesize speech: {error}

**Befintlig svenska:** Amazon Polly kunde inte syntetisera tal: {error}

**Bedömning:** Ingen ändring föreslås.

## 399. `component::amazon_polly::exceptions::language_not_supported::message`

**Engelska:** Voice {voice} does not support the {language} language.

**Befintlig svenska:** Rösten {voice} stöder inte språket {language}.

**Bedömning:** Ingen ändring föreslås.

## 400. `component::amazon_polly::exceptions::engine_not_supported::message`

**Engelska:** Voice {voice} does not support the {engine} engine.

**Befintlig svenska:** Rösten {voice} stöder inte talmotorn {engine}.

**Bedömning:** Ingen ändring föreslås.

## 401. `component::bosch_shc::entity::number::dimmer_min::name`

**Engelska:** Minimum brightness

**Befintlig svenska:** Lägsta ljusstyrka

**Bedömning:** Ingen ändring föreslås.

## 402. `component::bosch_shc::entity::number::dimmer_max::name`

**Engelska:** Maximum brightness

**Befintlig svenska:** Högsta ljusstyrka

**Bedömning:** Ingen ändring föreslås.

## 403. `component::ubus::config::step::user::data_description::verify_ssl`

**Engelska:** Whether to verify the router's SSL certificate.

**Befintlig svenska:** Om routerns SSL-certifikat ska verifieras.

**Bedömning:** Ingen ändring föreslås.

## 404. `component::ubus::config::step::user::data_description::ssl`

**Engelska:** Whether to connect to the router using SSL.

**Befintlig svenska:** Om routern ska anslutas med SSL.

**Förslag:** Om anslutningen till routern ska använda SSL.

## 405. `component::ubus::config::step::user::data::verify_ssl`

**Engelska:** [%key:common::config_flow::data::verify_ssl%]

**Befintlig svenska:** Verifiera SSL-certifikatet

**Bedömning:** Ingen ändring föreslås.

## 406. `component::ubus::config::step::user::data::ssl`

**Engelska:** [%key:common::config_flow::data::ssl%]

**Befintlig svenska:** Använder ett SSL-certifikat

**Bedömning:** Ingen ändring föreslås.

## 407. `component::plex::config::error::server_not_found`

**Engelska:** Plex server for this entry not linked to this Plex account

**Befintlig svenska:** Plex-servern för den här posten är inte kopplad till detta Plex-konto

**Bedömning:** Ingen ändring föreslås.

## 408. `component::samsung_exlink::exceptions::update_failed::message`

**Engelska:** Could not update the Samsung TV state.

**Befintlig svenska:** Det gick inte att uppdatera Samsung-tv:ns tillstånd.

**Bedömning:** Ingen ändring föreslås.

## 409. `component::samsung_exlink::exceptions::unsupported_key::message`

**Engelska:** Unsupported Samsung ExLink key: {key}

**Befintlig svenska:** Samsung ExLink-nyckeln {key} stöds inte.

**Bedömning:** Ingen ändring föreslås.

## 410. `component::vesync::entity::sensor::preheat_set_time_basket::name`

**Engelska:** Basket {basket} preheating set time

**Befintlig svenska:** Inställd förvärmningstid för korg {basket}

**Bedömning:** Ingen ändring föreslås.

## 411. `component::vesync::entity::sensor::current_temp_basket::name`

**Engelska:** Basket {basket} current temperature

**Befintlig svenska:** Aktuell temperatur för korg {basket}

**Bedömning:** Ingen ändring föreslås.

## 412. `component::vesync::entity::sensor::cook_status_basket::state::standby`

**Engelska:** [%key:common::state::standby%]

**Befintlig svenska:** Vänteläge

**Bedömning:** Ingen ändring föreslås.

## 413. `component::vesync::entity::sensor::cook_status_basket::state::ready`

**Engelska:** Ready

**Befintlig svenska:** Klar

**Bedömning:** Ingen ändring föreslås.

## 414. `component::vesync::entity::sensor::cook_status_basket::state::pull_out`

**Engelska:** Drawer pulled out

**Befintlig svenska:** Låda utdragen

**Bedömning:** Ingen ändring föreslås.

## 415. `component::vesync::entity::sensor::cook_status_basket::state::preheat_stop`

**Engelska:** Preheating stopped

**Befintlig svenska:** Förvärmning avbruten

**Bedömning:** Ingen ändring föreslås.

## 416. `component::vesync::entity::sensor::cook_status_basket::state::preheat_end`

**Engelska:** Preheating finished

**Befintlig svenska:** Förvärmning klar

**Bedömning:** Ingen ändring föreslås.

## 417. `component::vesync::entity::sensor::cook_status_basket::state::hold`

**Engelska:** Hold

**Befintlig svenska:** Varmhållning

**Bedömning:** Ingen ändring föreslås.

## 418. `component::vesync::entity::sensor::cook_status_basket::state::heating`

**Engelska:** Preheating

**Befintlig svenska:** Förvärmer

**Bedömning:** Ingen ändring föreslås.

## 419. `component::vesync::entity::sensor::cook_status_basket::state::cooking_stop`

**Engelska:** Cooking stopped

**Befintlig svenska:** Tillagning avbruten

**Bedömning:** Ingen ändring föreslås.

## 420. `component::vesync::entity::sensor::cook_status_basket::state::cooking_end`

**Engelska:** Cooking finished

**Befintlig svenska:** Tillagning klar

**Bedömning:** Ingen ändring föreslås.
