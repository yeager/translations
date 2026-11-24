# Home Assistant Core – historisk avstämning 14161–14280

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 77 direkta källtexter matchar HA Core-källan; 38 referensanvändningar med 30 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 5 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Två infrared-referenskonsumenter uppdaterades till exakt samma svenska mål som sin gemensamma referens, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 14161 | 899674242 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::orange_red` | Color: Orange red | Färg: Orangeröd | Shared reference target checked |
| 14162 | 899674241 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::orange` | Color: Orange | Färg: Orange | Shared reference target checked |
| 14163 | 899674240 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::on` | Power on | Av | Shared reference target checked |
| 14164 | 899674239 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::off` | Power off | På | Shared reference target checked |
| 14165 | 899674238 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_8` | Mode 8 | Läge 8 | Shared reference target checked |
| 14166 | 899674237 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_7` | Mode 7 | Läge 7 | Shared reference target checked |
| 14167 | 899674236 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_6` | Mode 6 | Läge 6 | Shared reference target checked |
| 14168 | 899674235 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_5` | Mode 5 | Läge 5 | Shared reference target checked |
| 14169 | 899674234 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_4` | Mode 4 | Läge 4 | Shared reference target checked |
| 14170 | 899674233 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_3` | Mode 3 | Läge 3 | Shared reference target checked |
| 14171 | 899674232 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_2` | Mode 2 | Läge 2 | Shared reference target checked |
| 14172 | 899674231 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::mode_1` | Mode 1 | Läge 1 | Shared reference target checked |
| 14173 | 899674230 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::light_green` | Color: Light green | Färg: Ljusgrön | Shared reference target checked |
| 14174 | 899674229 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::green` | Color: Green | Färg: Grön | Shared reference target checked |
| 14175 | 899674228 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::flash` | Flash | Blinka | Shared reference target checked |
| 14176 | 899674227 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::fade` | Fade | Tona | Shared reference target checked |
| 14177 | 899674226 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::dark_cyan` | Color: Dark cyan | Färg: Mörk cyan | Shared reference target checked |
| 14178 | 899674225 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::cyan` | Color: Cyan | Färg: Cyan | Shared reference target checked |
| 14179 | 899674224 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::brightness_up` | Brightness up | Ljusstyrka upp | Core-literal match |
| 14180 | 899674223 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::brightness_down` | Brightness down | Ljusstyrka ner | Core-literal match |
| 14181 | 899674222 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::blue` | Color: Blue | Färg: Blå | Shared reference target checked |
| 14182 | 899674221 | `component::led_infrared::entity::event::received_command::name` | Received command | Mottaget kommando | Core-literal match |
| 14183 | 899674220 | `component::led_infrared::config::step::user::data_description::infrared_receiver_entity_id` | The infrared receiver entity to use for receiving signals. | Mottagarentiteten som ska användas för att ta emot infraröda signaler. | Shared reference target checked |
| 14184 | 899674219 | `component::led_infrared::config::step::user::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Shared reference target checked |
| 14185 | 899674218 | `component::led_infrared::config::step::reconfigure::data_description::infrared_receiver_entity_id` | The infrared receiver entity to use for receiving signals. | Mottagarentiteten som ska användas för att ta emot infraröda signaler. | Shared reference target checked |
| 14186 | 899674217 | `component::led_infrared::config::step::reconfigure::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Shared reference target checked |
| 14187 | 899660095 | `component::geosphere_austria_warnings::exceptions::municipality_not_found::message` | No Austrian municipality was found for the configured location | Ingen österrikisk kommun hittades för den konfigurerade platsen | Core-literal match |
| 14188 | 899660094 | `component::geosphere_austria_warnings::exceptions::connection_error::message` | Error communicating with the GeoSphere Austria Warn API: {error} | Fel vid kommunikation med GeoSphere Austria Warn API: {error} | Core-literal match |
| 14189 | 899660093 | `component::geosphere_austria_warnings::exceptions::api_error::message` | The GeoSphere Austria Warn API returned an unexpected response: {error} | GeoSphere Austria Warn API returnerade ett oväntat svar: {error} | Core-literal match |
| 14190 | 899660092 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::yellow` | Yellow | Gul | Source-path follow-up open |
| 14191 | 899660091 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::red` | Red | Röd | Source-path follow-up open |
| 14192 | 899660090 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::orange` | Orange | Orange | Source-path follow-up open |
| 14193 | 899660089 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::none` | No warning | Ingen varning | Source-path follow-up open |
| 14194 | 899660088 | `component::geosphere_austria_warnings::entity::sensor::warning_level::name` | Warning level | Varningsnivå | Source-path follow-up open |
| 14195 | 899660087 | `component::geosphere_austria_warnings::entity::sensor::active_warnings::unit_of_measurement` | warnings | varningar | Core-literal match |
| 14196 | 899660086 | `component::geosphere_austria_warnings::entity::sensor::active_warnings::name` | Active warnings | Aktiva varningar | Core-literal match |
| 14197 | 899660085 | `component::geosphere_austria_warnings::config::step::user::description` | Select the location to monitor for official GeoSphere Austria weather warnings. | Välj den ort som du vill följa för officiella vädervarningar från GeoSphere Austria. | Core-literal match |
| 14198 | 899660084 | `component::geosphere_austria_warnings::config::step::user::data_description::location` | Warnings are provided for the Austrian municipality at this location. | Varningar utfärdas för den österrikiska kommunen på den här platsen. | Core-literal match |
| 14199 | 899660083 | `component::geosphere_austria_warnings::config::step::user::data::location` | Location | Plats | Shared reference target checked |
| 14200 | 899660082 | `component::geosphere_austria_warnings::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 14201 | 899660081 | `component::geosphere_austria_warnings::config::error::municipality_not_found` | No Austrian municipality was found at the selected location. | Ingen österrikisk kommun hittades på den valda platsen. | Core-literal match |
| 14202 | 899660080 | `component::geosphere_austria_warnings::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 14203 | 899660079 | `component::geosphere_austria_warnings::config::abort::already_configured` | Location is already configured | Platsen är redan konfigurerad | Shared reference target checked |
| 14204 | 899660001 | `component::knx::config_panel::entities::create::notify::knx::ga_send::label` | Address | Adress | Core-literal match |
| 14205 | 899660000 | `component::knx::config_panel::entities::create::notify::knx::ga_send::description` | The group address messages are sent to. | Den gruppadress som meddelandena skickas till. | Core-literal match |
| 14206 | 899659999 | `component::knx::config_panel::entities::create::notify::description` | The KNX notify platform allows you to send text messages to the KNX bus. | Plattformen KNX-notify låter dig skicka textmeddelanden till KNX-bussen. | Core-literal match |
| 14207 | 899659991 | `component::steam_online::entity::image::vertical_capsule::name` | Vertical capsule | Vertikal kapsyl | Core-literal match |
| 14208 | 899659990 | `component::steam_online::entity::image::small_capsule::name` | Small capsule | Liten kapsyl | Core-literal match |
| 14209 | 899659989 | `component::steam_online::entity::image::page_background::name` | Page background | Sidbakgrund | Core-literal match |
| 14210 | 899659988 | `component::steam_online::entity::image::main_capsule::name` | Main capsule | Huvudkapsyl | Core-literal match |
| 14211 | 899659987 | `component::steam_online::entity::image::library_logo::name` | Library logo | Bibliotek logo | Core-literal match |
| 14212 | 899659986 | `component::steam_online::entity::image::library_hero::name` | Library hero capsule | Bibliotekshjälte-kapsyl | Core-literal match |
| 14213 | 899659985 | `component::steam_online::entity::image::library_capsule::name` | Library capsule | Bibliotekskapsyl | Core-literal match |
| 14214 | 899659984 | `component::steam_online::entity::image::header_capsule::name` | Header capsule | Header-kapsyl | Core-literal match |
| 14215 | 899659983 | `component::steam_online::entity::image::avatar::name` | Avatar | Profilbild | Core-literal match |
| 14216 | 899659982 | `component::steam_online::entity::image::app_icon::name` | App icon | Appikon | Core-literal match |
| 14217 | 899659972 | `component::google_health::entity::sensor::hydration::name` | Water intake | Vattenintag | Core-literal match |
| 14218 | 899659971 | `component::google_health::entity::sensor::calories_consumed::name` | Calories consumed | Konsumerade kalorier | Core-literal match |
| 14219 | 899500081 | `component::indevolt::entity::sensor::main_cycles::unit_of_measurement` | cycles | cykler | Shared reference target checked |
| 14220 | 899500080 | `component::indevolt::entity::sensor::equivalent_full_cycles::unit_of_measurement` | cycles | cykler | Core-literal match |
| 14221 | 899500079 | `component::indevolt::entity::sensor::battery_pack_5_cycles::unit_of_measurement` | cycles | cykler | Shared reference target checked |
| 14222 | 899500078 | `component::indevolt::entity::sensor::battery_pack_4_cycles::unit_of_measurement` | cycles | cykler | Shared reference target checked |
| 14223 | 899500077 | `component::indevolt::entity::sensor::battery_pack_3_cycles::unit_of_measurement` | cycles | cykler | Shared reference target checked |
| 14224 | 899500076 | `component::indevolt::entity::sensor::battery_pack_2_cycles::unit_of_measurement` | cycles | cykler | Shared reference target checked |
| 14225 | 899500075 | `component::indevolt::entity::sensor::battery_pack_1_cycles::unit_of_measurement` | cycles | cykler | Shared reference target checked |
| 14226 | 899500067 | `component::open_router::selector::web_search_modes::options::tool_perplexity` | Perplexity | Perplex | Core-literal match |
| 14227 | 899500066 | `component::open_router::selector::web_search_modes::options::tool_parallel` | Parallel | Parallell | Core-literal match |
| 14228 | 899500065 | `component::open_router::selector::web_search_modes::options::tool_native` | Model native | Inbyggd modell | Core-literal match |
| 14229 | 899500064 | `component::open_router::selector::web_search_modes::options::tool_firecrawl` | Firecrawl | Firecrawl | Core-literal match |
| 14230 | 899500063 | `component::open_router::selector::web_search_modes::options::tool_exa` | Exa | Exa | Core-literal match |
| 14231 | 899500062 | `component::open_router::selector::web_search_modes::options::tool` | Auto | Auto | Shared reference target checked |
| 14232 | 899500061 | `component::open_router::selector::web_search_modes::options::plugin` | Plugin (deprecated) | Plugin (föråldrad) | Core-literal match |
| 14233 | 899500060 | `component::open_router::selector::web_search_modes::options::off` | Off | Av | Shared reference target checked |
| 14234 | 899500055 | `component::oralb::entity::sensor::toothbrush_state::state::post_brushing_statistics` | Post-brushing statistics | Statistik efter tandborstning | Core-literal match |
| 14235 | 899500054 | `component::oralb::entity::sensor::mode::state::smart_adapt` | Smart adapt | Smart anpassning | Core-literal match |
| 14236 | 899476291 | `component::gardena_bluetooth::entity::sensor::activation_reason::state::setup` | Setup | Konfiguration | Core-literal match |
| 14237 | 899476290 | `component::gardena_bluetooth::entity::sensor::activation_reason::state::schedule` | Schedule | Schema | Core-literal match |
| 14238 | 899476289 | `component::gardena_bluetooth::entity::sensor::activation_reason::state::none` | Inactive | Inaktiv | Core-literal match |
| 14239 | 899476288 | `component::gardena_bluetooth::entity::sensor::activation_reason::state::manual` | Manual | Manuell | Core-literal match |
| 14240 | 899476287 | `component::gardena_bluetooth::entity::sensor::activation_reason::state::external` | External | Extern | Core-literal match |
| 14241 | 899358449 | `component::shelly::exceptions::circuit_breaker_remote_disabled::message` | Circuit breaker for {entity} of {device} is tripped and cannot be turned on remotely | Säkring för {entity} på {device} har löst ut och går inte att slå på från distans | Core-literal match |
| 14242 | 899358448 | `component::shelly::entity::binary_sensor::safety_switch_with_channel_name::name` | {channel_name} safety switch | {channel_name} säkerhetsbrytare | Core-literal match |
| 14243 | 899358447 | `component::shelly::entity::binary_sensor::safety_switch::name` | Safety switch | Säkerhetsbrytare | Core-literal match |
| 14244 | 899358446 | `component::shelly::entity::binary_sensor::output_with_channel_name::name` | {channel_name} output | {channel_name} utgång | Core-literal match |
| 14245 | 899358445 | `component::shelly::entity::binary_sensor::output::name` | Output | Utgång | Core-literal match |
| 14246 | 898997079 | `component::unifi::options::step::init::sections::more_options::data_description::ignore_local_mac` | Don't create entities for Wi-Fi clients whose MAC is locally administered (e.g. private/randomized Wi-Fi addresses). Wired clients are unaffected. Clients in "Create entities from network clients" are still included. | Skapa inte entiteter för Wi-Fi-klienter vars MAC-adress administreras lokalt (t.ex. privata/slumpmässiga Wi-Fi-adresser). Trådbundna klienter påverkas inte. Klienter i "Skapa entiteter från nätverksklienter" ingår fortfarande. | Core-literal match |
| 14247 | 898997078 | `component::unifi::options::step::init::sections::more_options::data::ignore_local_mac` | Ignore Wi-Fi clients with private (e.g. randomized) MAC addresses | Ignorera Wi-Fi-klienter med privata (t.ex. randomiserade) MAC-adresser | Core-literal match |
| 14248 | 898758048 | `component::midea::selector::login_mode::options::preset` | Preset cloud credentials | Förinställda inloggningsuppgifter för moln | Core-literal match |
| 14249 | 898758047 | `component::midea::selector::login_mode::options::account` | Your account credentials | Dina inloggningsuppgifter | Core-literal match |
| 14250 | 898758046 | `component::midea::exceptions::unsupported_hvac_mode::message` | HVAC mode {hvac_mode} is not supported by this device. | HVAC-läge {hvac_mode} stöds inte av den här enheten. | Core-literal match |
| 14251 | 898758045 | `component::midea::entity::climate::climate_zone2::name` | Zone 2 thermostat | Zon 2 termostat | Core-literal match |
| 14252 | 898758044 | `component::midea::entity::climate::climate_zone1::name` | Zone 1 thermostat | Zon 1 termostat | Core-literal match |
| 14253 | 898758043 | `component::midea::config::step::user::title` | Set up Midea | Konfigurera Midea | Core-literal match |
| 14254 | 898758042 | `component::midea::config::step::user::menu_options::search` | Search automatically | Sök automatiskt | Core-literal match |
| 14255 | 898758041 | `component::midea::config::step::user::menu_options::manually` | Configure manually | Konfigurera manuellt | Core-literal match |
| 14256 | 898758040 | `component::midea::config::step::user::menu_options::list` | List all appliances only | Lista endast alla apparater | Core-literal match |
| 14257 | 898758039 | `component::midea::config::step::search::title` | Search devices | Sök enheter | Core-literal match |
| 14258 | 898758038 | `component::midea::config::step::search::data_description::ip_address` | Enter 'auto' to scan your network, or enter a specific IP address | Ange "auto" för att skanna ditt nätverk, eller ange en specifik IP-adress | Core-literal match |
| 14259 | 898758037 | `component::midea::config::step::search::data::ip_address` | IP address | IP-adress | Shared reference target checked |
| 14260 | 898758036 | `component::midea::config::step::manually::title` | Configure manually | Konfigurera manuellt | Core-literal match |
| 14261 | 898758035 | `component::midea::config::step::manually::data_description::type` | The type of your Midea appliance | Typen av din Midea-apparat | Core-literal match |
| 14262 | 898758034 | `component::midea::config::step::manually::data_description::token` | The token of your Midea appliance (hexadecimal string) | Token för din Midea-apparat (hexadecimal sträng) | Core-literal match |
| 14263 | 898758033 | `component::midea::config::step::manually::data_description::subtype` | The subtype of your Midea appliance | Subtypen för din Midea-apparat | Core-literal match |
| 14264 | 898758032 | `component::midea::config::step::manually::data_description::protocol` | The protocol used by your Midea appliance | Protokollet som används av din Midea-apparat | Core-literal match |
| 14265 | 898758031 | `component::midea::config::step::manually::data_description::port` | The local port used by your Midea appliance | Den lokala porten som används av din Midea-apparat | Core-literal match |
| 14266 | 898758030 | `component::midea::config::step::manually::data_description::model` | The model of your Midea appliance | Modellen på din Midea-apparat | Core-literal match |
| 14267 | 898758029 | `component::midea::config::step::manually::data_description::key` | The key of your Midea appliance (hexadecimal string) | Nyckeln till din Midea-apparat (hexadecimal sträng) | Core-literal match |
| 14268 | 898758028 | `component::midea::config::step::manually::data_description::ip_address` | The local IP address of your Midea appliance | Den lokala IP-adressen för din Midea-apparat | Core-literal match |
| 14269 | 898758027 | `component::midea::config::step::manually::data_description::device_id` | The device ID of your Midea appliance | Enhets-ID:t för din Midea-apparat | Core-literal match |
| 14270 | 898758026 | `component::midea::config::step::manually::data::type` | Type | Typ | Core-literal match |
| 14271 | 898758025 | `component::midea::config::step::manually::data::token` | Token | Token | Core-literal match |
| 14272 | 898758024 | `component::midea::config::step::manually::data::subtype` | Subtype | Subtyp | Core-literal match |
| 14273 | 898758023 | `component::midea::config::step::manually::data::protocol` | Protocol | Protokoll | Core-literal match |
| 14274 | 898758022 | `component::midea::config::step::manually::data::port` | Port | Port | Shared reference target checked |
| 14275 | 898758021 | `component::midea::config::step::manually::data::model` | Model | Modell | Core-literal match |
| 14276 | 898758020 | `component::midea::config::step::manually::data::key` | Key | Nyckel | Core-literal match |
| 14277 | 898758019 | `component::midea::config::step::manually::data::ip_address` | IP address | IP-adress | Shared reference target checked |
| 14278 | 898758018 | `component::midea::config::step::manually::data::device_id` | Device ID | Enhets-ID | Core-literal match |
| 14279 | 898758017 | `component::midea::config::step::login_credentials::title` | Cloud login | Molninloggning | Core-literal match |
| 14280 | 898758016 | `component::midea::config::step::login_credentials::data_description::server` | The Midea cloud server for your region | Mideas molnserver för din region | Core-literal match |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 899674220 | `component::led_infrared::config::step::user::data_description::infrared_receiver_entity_id` | Mottagarentiteten som ska användas för att ta emot infraröda signaler. |
| 899674218 | `component::led_infrared::config::step::reconfigure::data_description::infrared_receiver_entity_id` | Mottagarentiteten som ska användas för att ta emot infraröda signaler. |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 899660092 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::yellow` | Yellow |
| 899660091 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::red` | Red |
| 899660090 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::orange` | Orange |
| 899660089 | `component::geosphere_austria_warnings::entity::sensor::warning_level::state::none` | No warning |
| 899660088 | `component::geosphere_austria_warnings::entity::sensor::warning_level::name` | Warning level |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
