# Home Assistant Core – historisk avstämning 15361–15480

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 69 direkta källtexter matchar HA Core-källan; 12 referensanvändningar med 10 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 39 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15361 | 887753447 | `component::data_grand_lyon::entity::sensor::available_spaces::unit_of_measurement` | spaces | platser | Shared reference target checked |
| 15362 | 887753446 | `component::data_grand_lyon::entity::sensor::available_spaces::name` | Available parking spaces | Tillgängliga parkeringsplatser | Core-literal match |
| 15363 | 887753445 | `component::data_grand_lyon::entity::sensor::accessible_spaces::unit_of_measurement` | spaces | platser | Core-literal match |
| 15364 | 887753444 | `component::data_grand_lyon::entity::sensor::accessible_spaces::name` | Accessible parking spaces | Handikappanpassade parkeringsplatser | Core-literal match |
| 15365 | 887753443 | `component::data_grand_lyon::config_subentries::park_and_ride::step::user::data_description::park_id` | Search by name, or enter a park & ride ID directly. | Sök efter namn eller ange ett infartsparkerings-ID direkt. | Core-literal match |
| 15366 | 887753442 | `component::data_grand_lyon::config_subentries::park_and_ride::step::user::data::park_id` | Park & ride | Infartsparkering | Core-literal match |
| 15367 | 887753441 | `component::data_grand_lyon::config_subentries::park_and_ride::initiate_flow::user` | Add park & ride | Lägg till infartsparkering | Core-literal match |
| 15368 | 887753440 | `component::data_grand_lyon::config_subentries::park_and_ride::entry_type` | Park & ride | Infartsparkering | Core-literal match |
| 15369 | 887753439 | `component::data_grand_lyon::config_subentries::park_and_ride::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 15370 | 887753438 | `component::data_grand_lyon::config_subentries::park_and_ride::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15371 | 887753437 | `component::data_grand_lyon::config_subentries::park_and_ride::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15372 | 887753436 | `component::data_grand_lyon::config_subentries::park_and_ride::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 15373 | 887689184 | `component::omie::services::get_prices_for_date::name` | Get prices for date | Hämta priser för datum | Core-literal match |
| 15374 | 887689183 | `component::omie::services::get_prices_for_date::fields::date::name` | Date | Datum | Core-literal match |
| 15375 | 887689182 | `component::omie::services::get_prices_for_date::fields::date::description` | The date to get the prices for. | De datum att hämta priser för. | Core-literal match |
| 15376 | 887689181 | `component::omie::services::get_prices_for_date::fields::countries::name` | Countries | Länder | Core-literal match |
| 15377 | 887689180 | `component::omie::services::get_prices_for_date::fields::countries::description` | The countries to get the prices for. | De länder att hämta priser för. | Core-literal match |
| 15378 | 887689179 | `component::omie::services::get_prices_for_date::description` | Retrieves the electricity spot prices (in €/kWh) for a specific date. Prices for the next day are published daily at around 13:30 CET. | Hämtar spotpriserna för el (i €/kWh) för ett specifikt datum. Priserna för nästa dag publiceras dagligen runt 13:30 CET. | Core-literal match |
| 15379 | 887689178 | `component::omie::selector::country::options::pt` | Portugal | Portugal | Core-literal match |
| 15380 | 887689177 | `component::omie::selector::country::options::es` | Spain | Spanien | Core-literal match |
| 15381 | 887689176 | `component::omie::exceptions::entry_not_loaded::message` | The OMIE integration is not loaded. | OMIE-integrationen är inte laddad. | Core-literal match |
| 15382 | 887689175 | `component::omie::exceptions::date_before_market_start::message` | No quarter-hourly prices exist for {date}. Prices are available from {start_date} onwards. | Det finns inga kvartspriser för {date}. Priser finns tillgängliga från och med {start_date}. | Core-literal match |
| 15383 | 887689174 | `component::omie::exceptions::data_not_available::message` | Prices for {date} have not been published yet. | Priser för {date} har ännu inte publicerats. | Core-literal match |
| 15384 | 887689173 | `component::omie::exceptions::cannot_connect::message` | Error connecting to the OMIE API. | Fel vid anslutning till OMIE API. | Core-literal match |
| 15385 | 887664733 | `component::tesla_fleet::exceptions::homelink_no_location::message` | Vehicle location is not available. Ensure the vehicle is awake and that the location scope has been granted. | Fordonspositionen är inte tillgänglig. Kontrollera att fordonet är aktivt och att behörighet för positionsdata har beviljats. | Core-literal match |
| 15386 | 887613955 | `component::holiday::selector::device_class::options::yazidi` | Yazidi | Yazidi | Source-path follow-up open |
| 15387 | 887613954 | `component::holiday::selector::device_class::options::vlach` | Vlach | Vlach | Source-path follow-up open |
| 15388 | 887613953 | `component::holiday::selector::device_class::options::turkish` | Turkish | Turkiska | Source-path follow-up open |
| 15389 | 887613952 | `component::holiday::selector::device_class::options::serbian` | Serbian | Serbiska | Source-path follow-up open |
| 15390 | 887613951 | `component::holiday::selector::device_class::options::sabian` | Sabian | Sabianska | Source-path follow-up open |
| 15391 | 887613950 | `component::holiday::selector::device_class::options::roma` | Roma | Roma | Source-path follow-up open |
| 15392 | 887613949 | `component::holiday::selector::device_class::options::public` | Public | Offentlig | Source-path follow-up open |
| 15393 | 887613948 | `component::holiday::selector::device_class::options::protestant` | Protestant | Protestantiska | Source-path follow-up open |
| 15394 | 887613947 | `component::holiday::selector::device_class::options::orthodox` | Orthodox | Ortodoxa | Source-path follow-up open |
| 15395 | 887613946 | `component::holiday::selector::device_class::options::de_facto` | De facto | De facto | Source-path follow-up open |
| 15396 | 887613945 | `component::holiday::selector::device_class::options::bosnian` | Bosnian | Bosniska | Source-path follow-up open |
| 15397 | 887613944 | `component::holiday::selector::device_class::options::armenian` | Armenian | Armeniska | Source-path follow-up open |
| 15398 | 887613943 | `component::holiday::selector::device_class::options::albanian` | Albanian | Albanska | Source-path follow-up open |
| 15399 | 887559620 | `component::victron_gx::entity::switch::vebus_pvinverter_disable::name` | Vebus PV inverter disable | Inaktivera Vebus PV-växelriktare | Core-literal match |
| 15400 | 887559619 | `component::victron_gx::entity::switch::vebus_hub4_target_power_is_max_feed_in::name` | Hub4 target power is max feed-in | Hub4 måleffekt är maximal inmatning | Core-literal match |
| 15401 | 887559618 | `component::victron_gx::entity::switch::vebus_hub4_fix_solar_offset_100mv::name` | Hub4 fix solar offset to 100mV | Hub4 fixar solförskjutning till 100mV | Core-literal match |
| 15402 | 887559617 | `component::victron_gx::entity::switch::vebus_hub4_do_not_feed_in_overvoltage::name` | Hub4 do not feed in on overvoltage | Hub4 matar inte in vid överspänning | Core-literal match |
| 15403 | 887559616 | `component::victron_gx::entity::switch::vebus_hub4_disable_charge::name` | Hub4 disable charge | Hub4 inaktivera laddning | Core-literal match |
| 15404 | 887559615 | `component::victron_gx::entity::switch::system_ess_always_peak_shave::name` | ESS always peak shave | ESS utjämna alltid toppbelastningar | Core-literal match |
| 15405 | 887559614 | `component::victron_gx::entity::sensor::solarcharger_total_pv_yield_system::name` | Total PV yield system | Total PV-avkastning för system | Shared reference target checked |
| 15406 | 887559613 | `component::victron_gx::entity::sensor::solarcharger_temperature::name` | Temperature | Temperatur | Shared reference target checked |
| 15407 | 887559612 | `component::victron_gx::entity::select::system_vrm_portal_mode::state::read_only` | Read-only | Läs endast | Core-literal match |
| 15408 | 887559611 | `component::victron_gx::entity::select::system_vrm_portal_mode::state::off` | Off | Av | Shared reference target checked |
| 15409 | 887559610 | `component::victron_gx::entity::select::system_vrm_portal_mode::state::full` | Full | Full | Shared reference target checked |
| 15410 | 887559609 | `component::victron_gx::entity::select::system_vrm_portal_mode::name` | VRM portal access level | Åtkomstnivå för VRM-portalen | Core-literal match |
| 15411 | 887559608 | `component::victron_gx::common::total_pv_yield_system` | Total PV yield system | Total PV-avkastning för system | Core-literal match |
| 15412 | 887469857 | `component::smlight::selector::ble_scanner_mode::options::passive` | Passive (lowest device battery use, some details may be missing) | Passiv (lägre batteriförbrukning på enheten, vissa detaljer kan saknas) | Core-literal match |
| 15413 | 887469856 | `component::smlight::selector::ble_scanner_mode::options::disabled` | Disabled | Inaktiverad | Shared reference target checked |
| 15414 | 887469855 | `component::smlight::selector::ble_scanner_mode::options::auto` | Auto (recommended, saves device battery) | Auto (rekommenderas, sparar enhetens batteri) | Core-literal match |
| 15415 | 887469854 | `component::smlight::selector::ble_scanner_mode::options::active` | Active (uses more device battery, fastest updates) | Aktiv (högre batteriförbrukning på enheten, uppdaterar snabbast) | Core-literal match |
| 15416 | 887469853 | `component::smlight::options::step::no_settings::description` | This SMLIGHT device ({model}) does not support settings. | Denna SMLIGHT-enhet ({model}) har inga inställningsmöjligheter. | Core-literal match |
| 15417 | 887469852 | `component::smlight::options::step::init::description` | Configure SLZB Bluetooth settings. Switching between Disabled and another mode will reboot the device to apply the new configuration. | Konfigurera Bluetooth-inställningarna för SLZB. Om du växlar mellan läget ”Inaktiverat” och ett annat läge kommer enheten att startas om för att den nya konfigurationen ska träda i kraft. | Core-literal match |
| 15418 | 887469851 | `component::smlight::options::step::init::data_description::ble_scanner_mode` | Auto is recommended for most setups. It saves battery on your Bluetooth devices while still catching new devices and updates quickly. | Auto rekommenderas för de flesta konfigurationer. Det sparar batteri på dina Bluetooth-enheter samtidigt som det snabbt fångar upp nya enheter och uppdateringar. | Core-literal match |
| 15419 | 887469850 | `component::smlight::options::step::init::data::ble_scanner_mode` | Bluetooth scanner mode | Skannerläge för Bluetooth | Core-literal match |
| 15420 | 887469849 | `component::smlight::options::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 15421 | 887469848 | `component::smlight::options::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15422 | 887229149 | `component::http::issues::yaml_still_present_after_migration::title` | HTTP YAML configuration is ignored after migration | HTTP YAML-konfigurationen ignoreras efter migrering | Core-literal match |
| 15423 | 887229148 | `component::http::issues::yaml_still_present_after_migration::description` | The HTTP configuration in `configuration.yaml` has already been migrated and is now being ignored. Please remove the `http:` block from your `configuration.yaml`. Manage the HTTP configuration from the UI under **Settings** > **System** > **Network**. | HTTP-konfigurationen i `configuration.yaml` har redan migrerats och ignoreras nu. Ta bort `http:`-blocket från din `configuration.yaml`. Hantera HTTP-konfigurationen från användargränssnittet under **Inställningar** > **System** > **Nätverk**. | Core-literal match |
| 15424 | 887229147 | `component::http::issues::deprecated_yaml_import_error::title` | Failed to import HTTP YAML configuration | Det gick inte att importera HTTP YAML-konfigurationen | Core-literal match |
| 15425 | 887229146 | `component::http::issues::deprecated_yaml_import_error::description` | Migrating the `http` configuration from `configuration.yaml` to the integration's storage failed. Please check the logs for details and configure the `http` integration from the UI under **Settings** > **System** > **Network**. | Migreringen av `http`-konfigurationen från `configuration.yaml` till integrationens lagring misslyckades. Kontrollera loggarna för mer information och konfigurera `http`-integrationen från användargränssnittet under **Inställningar** > **System** > **Nätverk**. | Core-literal match |
| 15426 | 887229145 | `component::http::issues::deprecated_yaml::title` | The HTTP YAML configuration is deprecated | HTTP YAML-konfigurationen är föråldrad | Core-literal match |
| 15427 | 887229144 | `component::http::issues::deprecated_yaml::description` | Your existing HTTP configuration from `configuration.yaml` has been imported. The `http` integration is now configured from the UI under **Settings** > **System** > **Network**.<br><br>Please remove the `http:` block from your `configuration.yaml` and restart Home Assistant. | Din befintliga HTTP-konfiguration från `configuration.yaml` har importerats. Integrationen `http` är nu konfigurerad från användargränssnittet under **Inställningar** > **System** > **Nätverk**.<br><br>Ta bort `http:`-blocket från din `configuration.yaml` och starta om Home Assistant. | Core-literal match |
| 15428 | 886732954 | `component::deconz::exceptions::no_master_gateway::message` | No master gateway available | Ingen master-gateway tillgänglig | Core-literal match |
| 15429 | 886732953 | `component::deconz::exceptions::gateway_not_found::message` | Could not find gateway {bridge_id} | Det gick inte att hitta gateway {bridge_id} | Core-literal match |
| 15430 | 886732952 | `component::deconz::exceptions::entity_not_found::message` | Could not find entity {entity_id} | Det gick inte att hitta entiteten {entity_id} | Core-literal match |
| 15431 | 886732951 | `component::deconz::exceptions::device_refresh_failed::message` | Failed to refresh devices | Det gick inte att uppdatera enheterna | Core-literal match |
| 15432 | 886732950 | `component::deconz::exceptions::configure_failed::message` | Failed to configure device | Det gick inte att konfigurera enheten | Core-literal match |
| 15433 | 886576900 | `component::saunum::exceptions::cannot_connect::message` | Error connecting to {host} | Fel vid anslutning till {host} | Core-literal match |
| 15434 | 886548771 | `component::roborock::entity::switch::dust_collection::name` | Dust collection | Dammuppsamling | Core-literal match |
| 15435 | 886548770 | `component::roborock::entity::switch::button_light::name` | Indicator light | Indikatorlampa | Core-literal match |
| 15436 | 886229083 | `component::modbus_connection::selector::parity::options::o` | Odd | Ojämna | Source-path follow-up open |
| 15437 | 886229082 | `component::modbus_connection::selector::parity::options::n` | None | Inga | Source-path follow-up open |
| 15438 | 886229081 | `component::modbus_connection::selector::parity::options::e` | Even | Jämna | Source-path follow-up open |
| 15439 | 886229080 | `component::modbus_connection::exceptions::connection_not_ready::message` | Modbus connection not ready | Modbus-anslutningen är inte klar | Source-path follow-up open |
| 15440 | 886229079 | `component::modbus_connection::config::step::user::menu_options::serial` | Serial (including serial proxies and networked connections) | Seriell (inklusive seriella proxyservrar och nätverksanslutningar) | Source-path follow-up open |
| 15441 | 886229078 | `component::modbus_connection::config::step::user::menu_options::modbus_tcp` | Modbus TCP | Modbus TCP | Source-path follow-up open |
| 15442 | 886229077 | `component::modbus_connection::config::step::user::description` | How is the Modbus network connected? | Hur är Modbus-nätverket anslutet? | Source-path follow-up open |
| 15443 | 886229076 | `component::modbus_connection::config::step::serial::title` | Serial connection | Seriell anslutning | Source-path follow-up open |
| 15444 | 886229075 | `component::modbus_connection::config::step::serial::data_description::stopbits` | The number of stop bits. | Antalet stopp-bits. | Source-path follow-up open |
| 15445 | 886229074 | `component::modbus_connection::config::step::serial::data_description::parity` | The serial parity. | Den seriella pariteten. | Source-path follow-up open |
| 15446 | 886229073 | `component::modbus_connection::config::step::serial::data_description::device` | The serial port the Modbus device is connected to, e.g. /dev/ttyUSB0. | Serieporten som Modbus-enheten är ansluten till, t.ex. /dev/ttyUSB0. | Source-path follow-up open |
| 15447 | 886229072 | `component::modbus_connection::config::step::serial::data_description::bytesize` | The number of data bits. | Antalet data-bits. | Source-path follow-up open |
| 15448 | 886229071 | `component::modbus_connection::config::step::serial::data_description::baudrate` | The serial baud rate the device communicates at. | Den seriella baudhastighet som enheten kommunicerar med. | Source-path follow-up open |
| 15449 | 886229070 | `component::modbus_connection::config::step::serial::data::stopbits` | Stop bits | Stopp-bits | Source-path follow-up open |
| 15450 | 886229069 | `component::modbus_connection::config::step::serial::data::parity` | Parity | Paritet | Source-path follow-up open |
| 15451 | 886229068 | `component::modbus_connection::config::step::serial::data::device` | Device | Enhet | Source-path follow-up open |
| 15452 | 886229067 | `component::modbus_connection::config::step::serial::data::bytesize` | Byte size | Byte-storlek | Source-path follow-up open |
| 15453 | 886229066 | `component::modbus_connection::config::step::serial::data::baudrate` | Baud rate | Baudfrekvens | Source-path follow-up open |
| 15454 | 886229065 | `component::modbus_connection::config::step::modbus_tcp::title` | Modbus TCP | Modbus TCP | Source-path follow-up open |
| 15455 | 886229064 | `component::modbus_connection::config::step::modbus_tcp::data_description::port` | The TCP port the Modbus gateway listens on (default 502). | Den TCP-port som Modbus-gatewayen lyssnar på (standard 502). | Source-path follow-up open |
| 15456 | 886229063 | `component::modbus_connection::config::step::modbus_tcp::data_description::host` | The hostname or IP address of the Modbus gateway or device. | Värdnamnet eller IP-adressen för Modbus-gatewayen eller enheten. | Source-path follow-up open |
| 15457 | 886229062 | `component::modbus_connection::config::step::modbus_tcp::data::port` | Port | Port | Source-path follow-up open |
| 15458 | 886229061 | `component::modbus_connection::config::step::modbus_tcp::data::host` | Host | Värd | Source-path follow-up open |
| 15459 | 886229060 | `component::modbus_connection::config::error::cannot_open_serial_port` | Failed to open the serial port | Det gick inte att öppna den seriella porten | Source-path follow-up open |
| 15460 | 886229059 | `component::modbus_connection::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Source-path follow-up open |
| 15461 | 886229058 | `component::modbus_connection::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Source-path follow-up open |
| 15462 | 886193531 | `component::knx::config_panel::selectors::knx-payload-selector::raw_payload` | Raw payload | Rå nyttolast | Core-literal match |
| 15463 | 886193530 | `component::knx::config_panel::selectors::knx-payload-selector::raw_length_description` | Length of the raw payload in bytes. For DPT 1, 2 and 3 use `0`. | Längden på den råa nyttolasten i byte. För DPT 1, 2 och 3, använd `0`. | Core-literal match |
| 15464 | 886193529 | `component::knx::config_panel::selectors::knx-payload-selector::raw_length` | Payload length | Längd på nyttolast | Core-literal match |
| 15465 | 886193528 | `component::knx::config_panel::selectors::knx-payload-selector::mode::typed` | Typed value | Inmatat värde | Core-literal match |
| 15466 | 886193527 | `component::knx::config_panel::selectors::knx-payload-selector::mode::raw` | Raw payload | Rå nyttolast | Core-literal match |
| 15467 | 886193526 | `component::knx::config_panel::selectors::knx-payload-selector::mode::label` | Payload format | Format för nyttolast | Core-literal match |
| 15468 | 886193525 | `component::knx::config_panel::selectors::knx-payload-selector::dpt_missing` | No DPT selected – Typed mode not available | Ingen DPT vald – Inmatat läge är inte tillgängligt | Core-literal match |
| 15469 | 886193524 | `component::knx::config_panel::entities::create::button::knx::ga_send::label` | Address | Adress | Core-literal match |
| 15470 | 886193523 | `component::knx::config_panel::entities::create::button::knx::ga_send::description` | Group address the value is sent to. | Den gruppadress som värdet ska skickas till. | Core-literal match |
| 15471 | 886193522 | `component::knx::config_panel::entities::create::button::knx::data::label` | Data | Data | Core-literal match |
| 15472 | 886193521 | `component::knx::config_panel::entities::create::button::knx::data::description` | The value sent when the button is pressed. The format of the value depends on the DPT of the configured address. | Det värde som skickas när knappen trycks in. Värdets format beror på DPT för den konfigurerade adressen. | Core-literal match |
| 15473 | 886193520 | `component::knx::config_panel::entities::create::button::description` | Entity for sending predefined values. | Den entitet som ska skicka fördefinierade värden. | Core-literal match |
| 15474 | 886190099 | `component::llama_cpp::exceptions::unsupported_file_type::message` | Only images and PDF are supported by the OpenAI API, {file_path} is not an image file or PDF. | Endast bild- och PDF-filer stöds av OpenAI:s API. {file_path} är inte en bildfil eller PDF. | Core-literal match |
| 15475 | 886190098 | `component::llama_cpp::exceptions::timeout::message` | Connection timed out: {message}. | Tidsgränsen för anslutningen har överskridits {message}. | Core-literal match |
| 15476 | 886190097 | `component::llama_cpp::exceptions::quota_exceeded::message` | Your account or API key has insufficient credits: {message}. | Ditt konto eller din API-nyckel har otillräckliga krediter: {message}. | Core-literal match |
| 15477 | 886190096 | `component::llama_cpp::exceptions::json_parse_error::message` | Unexpected tool argument response: {message}. | Oväntat svar på verktygsargument: {message}. | Core-literal match |
| 15478 | 886190095 | `component::llama_cpp::exceptions::invalid_auth::message` | Invalid authentication: {message}. | Ogiltig autentisering: {message}. | Core-literal match |
| 15479 | 886190094 | `component::llama_cpp::exceptions::file_not_found::message` | File does not exist: {file_path}. | Filen finns inte: {file_path}. | Core-literal match |
| 15480 | 886190093 | `component::llama_cpp::exceptions::cannot_connect::message` | Cannot connect to the server: {message}. | Det går inte att ansluta till servern: {message}. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 887613955 | `component::holiday::selector::device_class::options::yazidi` | Yazidi |
| 887613954 | `component::holiday::selector::device_class::options::vlach` | Vlach |
| 887613953 | `component::holiday::selector::device_class::options::turkish` | Turkish |
| 887613952 | `component::holiday::selector::device_class::options::serbian` | Serbian |
| 887613951 | `component::holiday::selector::device_class::options::sabian` | Sabian |
| 887613950 | `component::holiday::selector::device_class::options::roma` | Roma |
| 887613949 | `component::holiday::selector::device_class::options::public` | Public |
| 887613948 | `component::holiday::selector::device_class::options::protestant` | Protestant |
| 887613947 | `component::holiday::selector::device_class::options::orthodox` | Orthodox |
| 887613946 | `component::holiday::selector::device_class::options::de_facto` | De facto |
| 887613945 | `component::holiday::selector::device_class::options::bosnian` | Bosnian |
| 887613944 | `component::holiday::selector::device_class::options::armenian` | Armenian |
| 887613943 | `component::holiday::selector::device_class::options::albanian` | Albanian |
| 886229083 | `component::modbus_connection::selector::parity::options::o` | Odd |
| 886229082 | `component::modbus_connection::selector::parity::options::n` | None |
| 886229081 | `component::modbus_connection::selector::parity::options::e` | Even |
| 886229080 | `component::modbus_connection::exceptions::connection_not_ready::message` | Modbus connection not ready |
| 886229079 | `component::modbus_connection::config::step::user::menu_options::serial` | Serial (including serial proxies and networked connections) |
| 886229078 | `component::modbus_connection::config::step::user::menu_options::modbus_tcp` | Modbus TCP |
| 886229077 | `component::modbus_connection::config::step::user::description` | How is the Modbus network connected? |
| 886229076 | `component::modbus_connection::config::step::serial::title` | Serial connection |
| 886229075 | `component::modbus_connection::config::step::serial::data_description::stopbits` | The number of stop bits. |
| 886229074 | `component::modbus_connection::config::step::serial::data_description::parity` | The serial parity. |
| 886229073 | `component::modbus_connection::config::step::serial::data_description::device` | The serial port the Modbus device is connected to, e.g. /dev/ttyUSB0. |
| 886229072 | `component::modbus_connection::config::step::serial::data_description::bytesize` | The number of data bits. |
| 886229071 | `component::modbus_connection::config::step::serial::data_description::baudrate` | The serial baud rate the device communicates at. |
| 886229070 | `component::modbus_connection::config::step::serial::data::stopbits` | Stop bits |
| 886229069 | `component::modbus_connection::config::step::serial::data::parity` | Parity |
| 886229068 | `component::modbus_connection::config::step::serial::data::device` | Device |
| 886229067 | `component::modbus_connection::config::step::serial::data::bytesize` | Byte size |
| 886229066 | `component::modbus_connection::config::step::serial::data::baudrate` | Baud rate |
| 886229065 | `component::modbus_connection::config::step::modbus_tcp::title` | Modbus TCP |
| 886229064 | `component::modbus_connection::config::step::modbus_tcp::data_description::port` | The TCP port the Modbus gateway listens on (default 502). |
| 886229063 | `component::modbus_connection::config::step::modbus_tcp::data_description::host` | The hostname or IP address of the Modbus gateway or device. |
| 886229062 | `component::modbus_connection::config::step::modbus_tcp::data::port` | Port |
| 886229061 | `component::modbus_connection::config::step::modbus_tcp::data::host` | Host |
| 886229060 | `component::modbus_connection::config::error::cannot_open_serial_port` | Failed to open the serial port |
| 886229059 | `component::modbus_connection::config::error::cannot_connect` | Failed to connect |
| 886229058 | `component::modbus_connection::config::abort::already_configured` | Device is already configured |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
