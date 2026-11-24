# Home Assistant Core – historisk avstämning 13201–13320

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 84 direkta källtexter matchar HA Core-källan; 36 referensanvändningar med 9 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 0 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13201 | 911211549 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_west::label` | Brightness west | Ljusstyrka väster | Core-literal match |
| 13202 | 911211548 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_west::description` | Group address for reading the current brightness to the west. | Gruppadress för avläsning av aktuell ljusstyrka i väster. | Core-literal match |
| 13203 | 911211547 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_south::label` | Brightness south | Ljusstyrka söder | Core-literal match |
| 13204 | 911211546 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_south::description` | Group address for reading the current brightness to the south. | Gruppadress för avläsning av aktuell ljusstyrka i söder. | Core-literal match |
| 13205 | 911211545 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_north::label` | Brightness north | Ljusstyrka norr | Core-literal match |
| 13206 | 911211544 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_north::description` | Group address for reading the current brightness to the north. | Gruppadress för avläsning av aktuell ljusstyrka i norr. | Core-literal match |
| 13207 | 911211543 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_east::label` | Brightness east | Ljusstyrka öster | Core-literal match |
| 13208 | 911211542 | `component::knx::config_panel::entities::create::weather::knx::ga_brightness_east::description` | Group address for reading the current brightness to the east. | Gruppadress för avläsning av aktuell ljusstyrka i öster. | Core-literal match |
| 13209 | 911211541 | `component::knx::config_panel::entities::create::weather::knx::ga_air_pressure::label` | Air pressure | Lufttryck | Core-literal match |
| 13210 | 911211540 | `component::knx::config_panel::entities::create::weather::knx::ga_air_pressure::description` | Group address for reading the current air pressure. | Gruppadress för avläsning av aktuellt lufttryck. | Core-literal match |
| 13211 | 911211539 | `component::knx::config_panel::entities::create::weather::description` | The KNX weather platform is used as an interface to KNX weather stations. | KNX-väderplattformen används som gränssnitt till KNX-väderstationer. | Core-literal match |
| 13212 | 911198747 | `component::monzo::entity::event::transaction::name` | Transaction | Transaktion | Core-literal match |
| 13213 | 911029168 | `component::home_connect::entity::sensor::smart_filter_cleaning_reminder::state::present` | Present | Nuvarande | Shared reference target checked |
| 13214 | 911029167 | `component::home_connect::entity::sensor::smart_filter_cleaning_reminder::state::off` | Off | Av | Shared reference target checked |
| 13215 | 911029166 | `component::home_connect::entity::sensor::smart_filter_cleaning_reminder::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13216 | 911029165 | `component::home_connect::entity::sensor::smart_filter_cleaning_reminder::name` | Smart filter cleaning reminder | Smart påminnelse om filterrengöring | Core-literal match |
| 13217 | 911029164 | `component::home_connect::entity::sensor::salt_lack::state::present` | Present | Nuvarande | Shared reference target checked |
| 13218 | 911029163 | `component::home_connect::entity::sensor::salt_lack::state::off` | Off | Av | Shared reference target checked |
| 13219 | 911029162 | `component::home_connect::entity::sensor::salt_lack::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13220 | 911029161 | `component::home_connect::entity::sensor::salt_lack::name` | Salt lack | Saltbrist | Core-literal match |
| 13221 | 911029160 | `component::home_connect::entity::sensor::rinse_aid_lack::state::present` | Present | Nuvarande | Shared reference target checked |
| 13222 | 911029159 | `component::home_connect::entity::sensor::rinse_aid_lack::state::off` | Off | Av | Shared reference target checked |
| 13223 | 911029158 | `component::home_connect::entity::sensor::rinse_aid_lack::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13224 | 911029157 | `component::home_connect::entity::sensor::rinse_aid_lack::name` | Rinse aid lack | Brist på sköljmedel | Core-literal match |
| 13225 | 911029156 | `component::home_connect::entity::sensor::program_blocked_salt_lack::state::present` | Present | Nuvarande | Shared reference target checked |
| 13226 | 911029155 | `component::home_connect::entity::sensor::program_blocked_salt_lack::state::off` | Off | Av | Shared reference target checked |
| 13227 | 911029154 | `component::home_connect::entity::sensor::program_blocked_salt_lack::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13228 | 911029153 | `component::home_connect::entity::sensor::program_blocked_salt_lack::name` | Program blocked - salt lack | Program blockerat - saltbrist | Core-literal match |
| 13229 | 911029152 | `component::home_connect::entity::sensor::machine_care_reminder::state::present` | Present | Nuvarande | Shared reference target checked |
| 13230 | 911029151 | `component::home_connect::entity::sensor::machine_care_reminder::state::off` | Off | Av | Shared reference target checked |
| 13231 | 911029150 | `component::home_connect::entity::sensor::machine_care_reminder::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13232 | 911029149 | `component::home_connect::entity::sensor::machine_care_reminder::name` | Machine care reminder | Påminnelse om maskinvård | Core-literal match |
| 13233 | 911029148 | `component::home_connect::entity::sensor::machine_care_and_low_maintenance_filter_cleaning_reminder::state::present` | Present | Nuvarande | Shared reference target checked |
| 13234 | 911029147 | `component::home_connect::entity::sensor::machine_care_and_low_maintenance_filter_cleaning_reminder::state::off` | Off | Av | Shared reference target checked |
| 13235 | 911029146 | `component::home_connect::entity::sensor::machine_care_and_low_maintenance_filter_cleaning_reminder::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13236 | 911029145 | `component::home_connect::entity::sensor::machine_care_and_low_maintenance_filter_cleaning_reminder::name` | Machine care and low maintenance filter cleaning reminder | Maskinvård och påminnelse om filterrengöring med lågt underhållsbehov | Core-literal match |
| 13237 | 911029144 | `component::home_connect::entity::sensor::machine_care_and_filter_cleaning_reminder::state::present` | Present | Nuvarande | Shared reference target checked |
| 13238 | 911029143 | `component::home_connect::entity::sensor::machine_care_and_filter_cleaning_reminder::state::off` | Off | Av | Shared reference target checked |
| 13239 | 911029142 | `component::home_connect::entity::sensor::machine_care_and_filter_cleaning_reminder::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13240 | 911029141 | `component::home_connect::entity::sensor::machine_care_and_filter_cleaning_reminder::name` | Machine care and filter cleaning reminder | Påminnelse om maskinvård och filterrengöring | Core-literal match |
| 13241 | 911029140 | `component::home_connect::entity::sensor::favorite_short_press::state::present` | Present | Nuvarande | Shared reference target checked |
| 13242 | 911029139 | `component::home_connect::entity::sensor::favorite_short_press::state::off` | Off | Av | Shared reference target checked |
| 13243 | 911029138 | `component::home_connect::entity::sensor::favorite_short_press::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13244 | 911029137 | `component::home_connect::entity::sensor::favorite_short_press::name` | Favorite short press | Kort tryck på favoritknappen | Core-literal match |
| 13245 | 911029136 | `component::home_connect::entity::sensor::favorite_long_press::state::present` | Present | Nuvarande | Shared reference target checked |
| 13246 | 911029135 | `component::home_connect::entity::sensor::favorite_long_press::state::off` | Off | Av | Shared reference target checked |
| 13247 | 911029134 | `component::home_connect::entity::sensor::favorite_long_press::state::confirmed` | Confirmed | Bekräftad | Shared reference target checked |
| 13248 | 911029133 | `component::home_connect::entity::sensor::favorite_long_press::name` | Favorite long press | Långt tryck på favoritknappen | Core-literal match |
| 13249 | 910971599 | `component::gardena_bluetooth::entity::image::contour::name` | Contour {number} | Kontur {number} | Core-literal match |
| 13250 | 910971598 | `component::gardena_bluetooth::entity::image::active_contour::name` | Active contour | Aktiv kontur | Core-literal match |
| 13251 | 910962404 | `component::hotspring::exceptions::invalid_response::message` | Invalid response received from the Hot Spring API | Ett ogiltigt svar mottogs från Hot Spring-API:t. | Core-literal match |
| 13252 | 910962403 | `component::hotspring::exceptions::cannot_connect::message` | An error occurred while communicating with the Hot Spring API | Ett fel uppstod vid kommunikation med Hot Spring API. | Core-literal match |
| 13253 | 910962402 | `component::hotspring::entity::number::target_temperature::name` | Target temperature | Måltemperatur | Core-literal match |
| 13254 | 910962401 | `component::hotspring::config::step::user::description` | Set up your Hot Spring Home Network Adapter (HNA) to integrate with Home Assistant. | Konfigurera din Hot Spring-hemnätverksadapter (HNA) för att integrera den med Home Assistant. | Core-literal match |
| 13255 | 910962400 | `component::hotspring::config::step::user::data_description::host` | Hostname or IP address of your Hot Spring Home Network Adapter (HNA). | Värdnamn eller IP-adress för din Hot Spring-hemnätverksadapter (HNA). | Core-literal match |
| 13256 | 910962399 | `component::hotspring::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 13257 | 910962398 | `component::hotspring::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 13258 | 910962397 | `component::hotspring::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 13259 | 910962396 | `component::hotspring::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 13260 | 910950545 | `component::gatus::entity::sensor::last_event::state::unhealthy` | Unhealthy | Ohälsosam | Core-literal match |
| 13261 | 910950544 | `component::gatus::entity::sensor::last_event::state::start` | Started | Startade | Core-literal match |
| 13262 | 910950543 | `component::gatus::entity::sensor::last_event::state::resolved` | Resolved | Löst | Core-literal match |
| 13263 | 910950542 | `component::gatus::entity::sensor::last_event::state::healthy` | Healthy | Hälsosam | Core-literal match |
| 13264 | 910950541 | `component::gatus::entity::sensor::last_event::name` | Last event | Senaste händelsen | Core-literal match |
| 13265 | 910912881 | `component::izone::config::progress::discover` | Searching for iZone controllers on your network | Söker efter iZone-kontroller i ditt nätverk | Core-literal match |
| 13266 | 910912880 | `component::izone::config::abort::continue_setup` | Continue setting up the discovered iZone controller. | Fortsätt konfigurera den upptäckta iZone-kontrollern. | Core-literal match |
| 13267 | 910856658 | `component::imou::exceptions::switch_operation_failed::message` | Imou rejected the switch change | Imou avvisade ändringen av brytaren | Core-literal match |
| 13268 | 910856657 | `component::imou::exceptions::press_button_failed::message` | Imou rejected the button press | Imou avvisade knapptryckningen | Core-literal match |
| 13269 | 910856656 | `component::imou::exceptions::get_stream_failed::message` | Could not get the live stream URL from Imou | Det gick inte att hämta webbadressen till liveströmmen från Imou | Core-literal match |
| 13270 | 910856655 | `component::imou::exceptions::get_image_failed::message` | Could not get a snapshot from Imou | Kunde inte hämta en ögonblicksbild från Imou | Core-literal match |
| 13271 | 910423449 | `component::iometer::entity::sensor::power_three_phase::name` | Power on phase {phase_number} | Effekt på fas {phase_number} | Core-literal match |
| 13272 | 910362302 | `component::vizio::exceptions::cannot_determine_port::message` | Could not determine the SmartCast API port for {host}. If the device is reachable, reconfigure it using host:port. | Kunde inte fastställa SmartCast API-porten för {host}. Om enheten är nåbar, konfigurera om den med hjälp av host:port. | Core-literal match |
| 13273 | 910362301 | `component::vizio::config::error::cannot_determine_port` | Could not determine the SmartCast API port for this device. Check that the hostname or IP address is correct and the device is powered on, or enter the address as host:port if you know the port. | Kunde inte fastställa SmartCast API-porten för den här enheten. Kontrollera att värdnamnet eller IP-adressen är korrekt och att enheten är påslagen, eller ange adressen som host:port om du känner till porten. | Core-literal match |
| 13274 | 910339742 | `component::solax::config::step::select_model::data_description::model` | Auto-discovery matched multiple inverter models at this address. Select the model that matches your device. | Automatisk identifiering matchade flera växelriktarmodeller på den här adressen. Välj den modell som matchar din enhet. | Core-literal match |
| 13275 | 910339741 | `component::solax::config::step::select_model::data::model` | Inverter model | Växelriktarmodell | Core-literal match |
| 13276 | 910339090 | `component::scorpiontrack::entity::binary_sensor::ignition::name` | Ignition | Tändning | Core-literal match |
| 13277 | 910211312 | `component::imou::exceptions::select_option_failed::message` | Imou rejected the new option | Imou avvisade det nya alternativet | Core-literal match |
| 13278 | 910211311 | `component::imou::entity::select::night_vision_mode::state::smartlowlight` | Smart low light night vision | Smart nattseende i svagt ljus | Core-literal match |
| 13279 | 910211310 | `component::imou::entity::select::night_vision_mode::state::off` | Off | Av | Shared reference target checked |
| 13280 | 910211309 | `component::imou::entity::select::night_vision_mode::state::lowlight` | Low light night vision | Nattseende i svagt ljus | Core-literal match |
| 13281 | 910211308 | `component::imou::entity::select::night_vision_mode::state::intelligent` | Smart night vision | Smart nattseende | Core-literal match |
| 13282 | 910211307 | `component::imou::entity::select::night_vision_mode::state::infrared` | Infrared night vision | Infrarött nattseende | Core-literal match |
| 13283 | 910211306 | `component::imou::entity::select::night_vision_mode::state::fullcolor` | Bright color night vision | Nattseende i ljusa färger | Core-literal match |
| 13284 | 910211305 | `component::imou::entity::select::night_vision_mode::state::custom` | Custom mode | Anpassat läge | Core-literal match |
| 13285 | 910211304 | `component::imou::entity::select::night_vision_mode::name` | Night vision mode | Nattseendeläge | Core-literal match |
| 13286 | 910211303 | `component::imou::entity::select::device_volume::state::mute` | Mute | Tyst | Core-literal match |
| 13287 | 910211302 | `component::imou::entity::select::device_volume::state::medium` | Medium | Medel | Shared reference target checked |
| 13288 | 910211301 | `component::imou::entity::select::device_volume::state::low` | Low | Låg | Shared reference target checked |
| 13289 | 910211300 | `component::imou::entity::select::device_volume::state::high` | High | Hög | Shared reference target checked |
| 13290 | 910211299 | `component::imou::entity::select::device_volume::name` | Volume | Volym | Core-literal match |
| 13291 | 910179792 | `component::izone::entity::sensor::supply_temperature::name` | Supply temperature | Framledningstemperatur | Core-literal match |
| 13292 | 910179791 | `component::izone::entity::sensor::return_temperature::name` | Return temperature | Returtemperatur | Core-literal match |
| 13293 | 910179611 | `component::netatmo::entity::select::schedule::name` | Schedule | Schema | Core-literal match |
| 13294 | 909847954 | `component::liebherr::exceptions::invalid_temperature::message` | Temperature {temperature} is not supported. Allowed values: {allowed_values} | Temperaturen {temperature} stöds inte. Tillåtna värden: {allowed_values} | Core-literal match |
| 13295 | 909549470 | `component::mikrotik::entity::sensor::psu_voltage::name` | PSU {index} voltage | Spänning för nätaggregat {index} | Core-literal match |
| 13296 | 909549469 | `component::mikrotik::entity::sensor::psu_current::name` | PSU {index} current | Ström för nätaggregat {index} | Core-literal match |
| 13297 | 909549468 | `component::mikrotik::entity::sensor::poe_out_consumption::name` | PoE (out) consumption | PoE-förbrukning (ut) | Core-literal match |
| 13298 | 909549467 | `component::mikrotik::entity::sensor::cpu_temperature::name` | CPU temperature | CPU-temperatur | Core-literal match |
| 13299 | 909549466 | `component::mikrotik::entity::sensor::board_temperature::name` | Board temperature {index} | Korttemperatur {index} | Core-literal match |
| 13300 | 909245042 | `component::tesla_fleet::selector::region::options::na` | North America & Asia-Pacific | Nordamerika och Asien-Stillahavsområdet | Core-literal match |
| 13301 | 909245041 | `component::tesla_fleet::selector::region::options::eu` | Europe, Middle East & Africa | Europa, Mellanöstern och Afrika | Core-literal match |
| 13302 | 909245040 | `component::tesla_fleet::config::step::region::title` | Select region | Välj region | Core-literal match |
| 13303 | 909245039 | `component::tesla_fleet::config::step::region::data_description::region` | The region to register your application in. This defaults to the region detected from your Tesla account and only needs changing if your vehicles or energy sites are in a different region. | Den region där du ska registrera din applikation. Standardinställningen är den region som identifierats utifrån ditt Tesla-konto, och du behöver endast ändra detta om dina fordon eller energianläggningar finns i en annan region. | Core-literal match |
| 13304 | 909245038 | `component::tesla_fleet::config::step::region::data::region` | Region | Region | Core-literal match |
| 13305 | 909245037 | `component::tesla_fleet::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 13306 | 908982682 | `component::vizio::options::step::init::data_description::volume_step` | The number of volume levels the volume changes by with each volume up or volume down command. | Antalet volymsteg som volymen ändras med vid varje kommando för volym upp/ner. | Core-literal match |
| 13307 | 908982681 | `component::vizio::options::step::init::data_description::include_or_exclude` | Whether the selected apps should be included in or excluded from the source list. | Om de valda apparna ska inkluderas i eller exkluderas från källistan. | Core-literal match |
| 13308 | 908982680 | `component::vizio::options::step::init::data_description::apps_to_include_or_exclude` | The apps that should be included in or excluded from the source list. | De appar som ska inkluderas i eller exkluderas från källistan. | Core-literal match |
| 13309 | 908982679 | `component::vizio::config::step::user::data_description::name` | The name used for the device and its entities in Home Assistant. | Namnet som används för enheten och dess entiteter i Home Assistant. | Core-literal match |
| 13310 | 908982678 | `component::vizio::config::step::user::data_description::access_token` | The access token used to authenticate with your TV. Leave empty to start a pairing process that will provide one. | Den åtkomsttoken som används för att autentisera med din TV. Lämna tomt för att starta en parkopplingsprocess som kommer att generera en. | Core-literal match |
| 13311 | 908952449 | `component::gatus::entity::sensor::status_code::name` | Status code | Statuskod | Core-literal match |
| 13312 | 908749772 | `component::gatus::entity::sensor::response_time::name` | Response time | Svarstid | Core-literal match |
| 13313 | 908724497 | `component::home_connect::selector::programs::options::laundry_care_washer_program_wash_and_dry_90` | Wash and dry 90 min | Tvätta och torka 90 min | Core-literal match |
| 13314 | 908724496 | `component::home_connect::selector::programs::options::laundry_care_washer_program_wash_and_dry_60` | Wash and dry 60 min | Tvätta och torka 60 min | Core-literal match |
| 13315 | 908724495 | `component::home_connect::selector::programs::options::laundry_care_washer_program_super_153045_super_30` | Super 30 min | Super 30 min | Core-literal match |
| 13316 | 908724494 | `component::home_connect::selector::programs::options::laundry_care_washer_program_steaming_steaming` | Steaming | Ångbehandling | Core-literal match |
| 13317 | 908724493 | `component::home_connect::selector::programs::options::laundry_care_washer_program_sport_shoes` | Sport shoes | Sportskor | Core-literal match |
| 13318 | 908724492 | `component::home_connect::selector::programs::options::laundry_care_washer_program_my_time` | My time | Min tid | Core-literal match |
| 13319 | 908724491 | `component::home_connect::selector::programs::options::laundry_care_washer_dryer_program_wool` | Wool | Ull | Core-literal match |
| 13320 | 908724490 | `component::home_connect::selector::programs::options::laundry_care_washer_dryer_program_spin` | Spin | Centrifugering | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
