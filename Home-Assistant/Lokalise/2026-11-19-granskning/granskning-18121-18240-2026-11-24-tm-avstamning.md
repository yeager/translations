# Home Assistant Core – historisk avstämning 18121–18240

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 94 direkta källtexter matchar HA Core-källan; 22 referensanvändningar med 19 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 4 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Tre infrared-integrationers konsumentnycklar uppdaterades till exakt samma svenska mål som sina gemensamma referenser, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18121 | 855448767 | `component::elkm1::issues::deprecated_sensor_scripts::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.<br><br>The sensor was used in the following automations or scripts:<br>{items}<br><br>Update the above automations or scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. | Sensorn {entity_name} (`{entity_id}`) är utfasad eftersom den har ersatts med `{replacement_entity_id}`. Sensorn användes i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera ovanstående automatiseringar eller skript så att de använder ersättningsenheten, inaktivera sedan den utfasade sensorn så att den tas bort efter nästa omstart. | Source-path follow-up open |
| 18122 | 855448766 | `component::elkm1::issues::deprecated_sensor::title` | Deprecated sensor detected | Föråldrad sensor upptäckt | Source-path follow-up open |
| 18123 | 855448765 | `component::elkm1::issues::deprecated_sensor::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.<br><br>Update your dashboards, templates, automations and scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. | Sensorn {entity_name} (`{entity_id}`) är utfasad eftersom den har ersatts med `{replacement_entity_id}`. Uppdatera dina instrumentpaneler, mallar, automatiseringar och skript så att de använder den ersättande enheten och inaktivera sedan den utfasade sensorn så att den tas bort efter nästa omstart. | Source-path follow-up open |
| 18124 | 855442024 | `component::data_grand_lyon::exceptions::update_failed_velov::message` | Error fetching Vélo'v stations from Data Grand Lyon. | Fel vid hämtning av Vélo'v-stationer från Data Grand Lyon. | Core-literal match |
| 18125 | 855442023 | `component::data_grand_lyon::exceptions::update_failed_tcl::message` | Error fetching TCL departures from Data Grand Lyon. | Fel vid hämtning av TCL-avgångar från Data Grand Lyon. | Core-literal match |
| 18126 | 855437691 | `component::matter::entity::siren::siren::name` | Siren | Siren | Shared reference target checked |
| 18127 | 855304836 | `component::aidot::config::step::user::data_description::username` | Account logged in through AiDot app | Kontot som är inloggat via AiDot-appen. | Core-literal match |
| 18128 | 855304835 | `component::aidot::config::step::user::data_description::password` | Password for logging in through AiDot app | Lösenord för inloggning via AiDot-appen | Core-literal match |
| 18129 | 855304834 | `component::aidot::config::step::user::data_description::country_code` | The country selected by AiDot app when logging in | Landet som AiDot-appen valde vid inloggning | Core-literal match |
| 18130 | 855304833 | `component::aidot::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 18131 | 855304832 | `component::aidot::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 18132 | 855304831 | `component::aidot::config::step::user::data::country_code` | Country | Land | Shared reference target checked |
| 18133 | 855304830 | `component::aidot::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 18134 | 855304829 | `component::aidot::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 18135 | 855304828 | `component::aidot::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 18136 | 855293129 | `component::sonos::exceptions::invalid_media_content_type::message` | Media content type {media_content_type} is not supported | Medieinnehållstyp {media_content_type} stöds inte | Core-literal match |
| 18137 | 855292945 | `component::easyenergy::services::get_gas_prices::fields::price_type::name` | Price type | Pristyp | Core-literal match |
| 18138 | 855292944 | `component::easyenergy::services::get_gas_prices::fields::price_type::description` | The type of prices to retrieve. | Vilken typ av priser som ska hämtas. | Core-literal match |
| 18139 | 855292943 | `component::easyenergy::services::get_energy_usage_prices::fields::price_type::name` | Price type | Pristyp | Shared reference target checked |
| 18140 | 855292942 | `component::easyenergy::services::get_energy_usage_prices::fields::price_type::description` | The type of prices to retrieve. | Vilken typ av priser som ska hämtas. | Shared reference target checked |
| 18141 | 855292941 | `component::easyenergy::services::get_energy_usage_prices::fields::granularity::name` | Granularity | Detaljnivå | Core-literal match |
| 18142 | 855292940 | `component::easyenergy::services::get_energy_usage_prices::fields::granularity::description` | The interval size for the electricity prices. | Intervallstorlek för elpriserna. | Core-literal match |
| 18143 | 855292939 | `component::easyenergy::services::get_energy_return_prices::fields::granularity::name` | Granularity | Detaljnivå | Shared reference target checked |
| 18144 | 855292938 | `component::easyenergy::services::get_energy_return_prices::fields::granularity::description` | The interval size for the electricity prices. | Intervallstorlek för elpriserna. | Shared reference target checked |
| 18145 | 855292937 | `component::easyenergy::selector::price_type_selector::options::market` | Market price | Marknadspris | Core-literal match |
| 18146 | 855292936 | `component::easyenergy::selector::price_type_selector::options::invoice` | All-in price | Totalpris | Core-literal match |
| 18147 | 855292935 | `component::easyenergy::selector::granularity_selector::options::quarter` | Quarter | Kvart | Core-literal match |
| 18148 | 855292934 | `component::easyenergy::selector::granularity_selector::options::hour` | Hour | Timme | Core-literal match |
| 18149 | 855255515 | `component::knx::exceptions::service_event_register_ga_not_found::message` | Could not find registered event for `{group_addresses}` to remove. | Det gick inte att hitta någon registrerad händelse för `{group_addresses}` att ta bort. | Core-literal match |
| 18150 | 855250597 | `component::template::exceptions::failed_to_reload_template_entities::message` | Error reloading template entities: {error} | Fel vid omladdning av mallenheter: {error} | Core-literal match |
| 18151 | 855246780 | `component::vlc_telnet::exceptions::connect_error::message` | Connection error: {error} | Anslutningsfel: {error} | Core-literal match |
| 18152 | 855246779 | `component::vlc_telnet::exceptions::command_error::message` | Command error: {error} | Kommandofel: {error} | Core-literal match |
| 18153 | 855228528 | `component::marantz_infrared::entity::button::speaker_ab::name` | Speaker A/B | Högtalare A/B | Core-literal match |
| 18154 | 855228527 | `component::marantz_infrared::entity::button::source_direct::name` | Source direct | Källa direkt | Core-literal match |
| 18155 | 855228526 | `component::marantz_infrared::entity::button::loudness::name` | Loudness | Ljudstyrka | Core-literal match |
| 18156 | 855208732 | `component::indevolt::entity::sensor::realtime_target_soc::name` | Real-time target SOC | SOC-mål i realtid | Core-literal match |
| 18157 | 855208731 | `component::indevolt::entity::sensor::realtime_power_limit::name` | Real-time power limit | Effektgräns i realtid | Core-literal match |
| 18158 | 855208730 | `component::indevolt::entity::sensor::realtime_command::state::standby` | Standby | Viloläge | Shared reference target checked |
| 18159 | 855208729 | `component::indevolt::entity::sensor::realtime_command::state::discharging` | Discharging | Laddar ur | Shared reference target checked |
| 18160 | 855208728 | `component::indevolt::entity::sensor::realtime_command::state::charging` | Charging | Laddar | Shared reference target checked |
| 18161 | 855208727 | `component::indevolt::entity::sensor::realtime_command::name` | Real-time mode | Realtidsläge | Core-literal match |
| 18162 | 855207643 | `component::cast::exceptions::app_not_supported::message` | App {app_name} is not supported | Appen {app_name} stöds inte | Core-literal match |
| 18163 | 855188666 | `component::lovelace::exceptions::failed_to_reload::message` | Failed to reload dashboard resources. Please check your configuration and try again. | Det gick inte att ladda om kontrollpanelens resurser. Kontrollera din konfiguration och försök igen. | Core-literal match |
| 18164 | 855186279 | `component::rest::exceptions::turn_on_failed::message` | Failed to turn on {resource} | Det gick inte att slå på {resource} | Core-literal match |
| 18165 | 855186278 | `component::rest::exceptions::turn_off_failed::message` | Failed to turn off {resource} | Det gick inte att stänga av {resource} | Core-literal match |
| 18166 | 855186277 | `component::rest::exceptions::error_communicating::message` | Error communicating with {resource} | Fel vid kommunikation med {resource} | Core-literal match |
| 18167 | 855176888 | `component::mqtt::exceptions::mqtt_max_subscription_id_reached::message` | MQTT Subscription ID limit reached. Cannot generate more IDs to subscribe. | Gränsen för MQTT-prenumerations-ID har nåtts. Det går inte att generera fler ID:n att prenumerera på. | Core-literal match |
| 18168 | 854698727 | `component::daikin::exceptions::error_communicating::message` | Error communicating with Daikin device: {error} | Fel vid kommunikation med Daikin-enhet: {error} | Core-literal match |
| 18169 | 854698709 | `component::verisure::exceptions::arm_state_failed::message` | Failed to change alarm state. Verify your code is correct and that your account is not temporarily locked. | Det gick inte att ändra larmstatus. Kontrollera att din kod är korrekt och att ditt konto inte är tillfälligt spärrat. | Core-literal match |
| 18170 | 854644327 | `component::kiosker::entity::button::screensaver_interact::name` | Dismiss screensaver | Avfärda skärmsläckare | Core-literal match |
| 18171 | 854644326 | `component::kiosker::entity::button::print::name` | Print page | Skriv ut | Core-literal match |
| 18172 | 854644325 | `component::kiosker::entity::button::ping::name` | Ping | Pinga | Core-literal match |
| 18173 | 854644324 | `component::kiosker::entity::button::navigate_refresh::name` | Refresh page | Ladda om sida | Core-literal match |
| 18174 | 854644323 | `component::kiosker::entity::button::navigate_home::name` | Go home | Hem | Core-literal match |
| 18175 | 854644322 | `component::kiosker::entity::button::navigate_forward::name` | Go forward | Framåt | Core-literal match |
| 18176 | 854644321 | `component::kiosker::entity::button::navigate_backward::name` | Go back | Tillbaka | Core-literal match |
| 18177 | 854644320 | `component::kiosker::entity::button::clear_cookies::name` | Clear cookies | Rensa cookies | Core-literal match |
| 18178 | 854644319 | `component::kiosker::entity::button::clear_cache::name` | Clear cache | Rensa cache | Core-literal match |
| 18179 | 854625049 | `component::nobo_hub::exceptions::set_week_profile_failed::message` | Failed to set week profile. | Misslyckades med att ställa in veckoprofil. | Core-literal match |
| 18180 | 854625048 | `component::nobo_hub::exceptions::set_temperature_failed::message` | Failed to set target temperature. | Misslyckades med att ställa in måltemperatur. | Core-literal match |
| 18181 | 854625047 | `component::nobo_hub::exceptions::set_preset_mode_failed::message` | Failed to set preset mode. | Misslyckades med att ställa in förinställt läge. | Core-literal match |
| 18182 | 854625046 | `component::nobo_hub::exceptions::set_hvac_mode_failed::message` | Failed to set HVAC mode. | Misslyckades med att ställa in HVAC-läge. | Core-literal match |
| 18183 | 854625045 | `component::nobo_hub::exceptions::set_global_override_failed::message` | Failed to set global override. | Misslyckades med att ange global åsidosättning. | Core-literal match |
| 18184 | 854609037 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::vcr` | VCR | VCR | Core-literal match |
| 18185 | 854609036 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::tv` | TV | TV | Core-literal match |
| 18186 | 854609035 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::tuner` | Tuner | Radio | Core-literal match |
| 18187 | 854609034 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::tape` | Tape | Tape | Core-literal match |
| 18188 | 854609033 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::satellite` | Satellite | Satellit | Core-literal match |
| 18189 | 854609032 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::recorder` | Recorder | Inspelare | Core-literal match |
| 18190 | 854609031 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::phono` | Phono | Phono | Core-literal match |
| 18191 | 854609030 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::optical` | Optical | Optisk | Core-literal match |
| 18192 | 854609029 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::network` | Network | Nätverk | Core-literal match |
| 18193 | 854609028 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::md` | MD | MD | Core-literal match |
| 18194 | 854609027 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::laserdisc` | LaserDisc | LaserDisc | Core-literal match |
| 18195 | 854609026 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::coax` | Coax | Coax | Core-literal match |
| 18196 | 854609025 | `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::cd` | CD | CD | Core-literal match |
| 18197 | 854609024 | `component::marantz_infrared::config::step::user::title` | Set up Marantz IR Remote | Konfigurera Marantz IR-fjärrkontroll | Core-literal match |
| 18198 | 854609023 | `component::marantz_infrared::config::step::user::description` | Select the Marantz model and the infrared emitter entity to use for controlling your Marantz device. | Välj Marantz-modellen och den infraröda sändaren som ska användas för att styra din Marantz-enhet. | Core-literal match |
| 18199 | 854609022 | `component::marantz_infrared::config::step::user::data_description::model` | The Marantz model to control. | Den Marantz-modell som ska styras. | Core-literal match |
| 18200 | 854609021 | `component::marantz_infrared::config::step::user::data_description::infrared_emitter_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 18201 | 854609020 | `component::marantz_infrared::config::step::user::data::model` | Model | Modell | Core-literal match |
| 18202 | 854609019 | `component::marantz_infrared::config::step::user::data::infrared_emitter_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 18203 | 854609018 | `component::marantz_infrared::config::abort::no_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 18204 | 854609017 | `component::marantz_infrared::config::abort::already_configured` | This Marantz device has already been configured with this infrared emitter. | Denna Marantz-enhet har redan konfigurerats med denna sändare. | Core-literal match |
| 18205 | 854599833 | `component::fritzbox::exceptions::login_failed::message` | Login failed, please check your username and password and try again. | Inloggningen misslyckades, kontrollera ditt användarnamn och lösenord och försök igen. | Core-literal match |
| 18206 | 854599832 | `component::fritzbox::exceptions::connect_error_reload::message` | A connection error occurred while updating the data from the FRITZ!Box. The integration is going to be reloaded to ensure a proper re-login. | Ett anslutningsfel uppstod när data från FRITZ!Box uppdaterades. Integrationen kommer att laddas om för att säkerställa en korrekt ominloggning. | Core-literal match |
| 18207 | 854599831 | `component::fritzbox::exceptions::connect_error::message` | A connection error occurred while setting up the integration. The setup will be retried. | Ett anslutningsfel uppstod när integrationen konfigurerades. Installationen kommer att försöka igen. | Core-literal match |
| 18208 | 854598611 | `component::adguard::exceptions::error_while_turn_on::message` | An error occurred while turning on AdGuard Home switch. | Ett fel uppstod när AdGuard Home-växeln skulle slås på. | Core-literal match |
| 18209 | 854598610 | `component::adguard::exceptions::error_while_turn_off::message` | An error occurred while turning off AdGuard Home switch. | Ett fel inträffade när AdGuard Home-växeln stängdes av. | Core-literal match |
| 18210 | 854594956 | `component::synology_dsm::exceptions::serial_not_found::message` | DSM with specified serial {serial} not found. | DSM med angivet serienummer {serial} hittades inte. | Core-literal match |
| 18211 | 854594955 | `component::synology_dsm::exceptions::missing_serial::message` | More than one DSM configured, must specify one of serials: {serials}. | Mer än en DSM är konfigurerad, ange ett av följande serienumren: {serials}. | Core-literal match |
| 18212 | 854594954 | `component::synology_dsm::exceptions::execution_error::message` | Execute {action} on DSM with serial {serial} not possible, because of {error}. | Det går inte att köra kommandot ” {action} ” på DSM med serienummer {serial} på grund av {error}. | Core-literal match |
| 18213 | 854579099 | `component::indevolt::entity::sensor::transformer_temperature::name` | Transformer temperature | Transformatortemperatur | Core-literal match |
| 18214 | 854579098 | `component::indevolt::entity::sensor::cycle_count::name` | Cycle count | Cykelantal | Source-path follow-up open |
| 18215 | 854441260 | `component::tractive::exceptions::failed_to_turn_on::message` | An error occurred while trying to turn on {entity} | Ett fel uppstod vid försök att slå på {entity} | Core-literal match |
| 18216 | 854441259 | `component::tractive::exceptions::failed_to_turn_off::message` | An error occurred while trying to turn off {entity} | Ett fel uppstod vid försök att stänga av {entity} | Core-literal match |
| 18217 | 854441210 | `component::samsungtv::exceptions::media_id_invalid::message` | Media ID must be a positive integer. | Medie-ID måste vara ett positivt heltal. | Core-literal match |
| 18218 | 854438470 | `component::samsung_infrared::selector::device_type::options::tv` | TV | TV | Core-literal match |
| 18219 | 854438469 | `component::samsung_infrared::config::step::user::title` | Set up infrared remote | Konfigurera den infraröda fjärrkontrollen | Core-literal match |
| 18220 | 854438468 | `component::samsung_infrared::config::step::user::description` | Select the device type and the infrared emitter entity to use for controlling your device. | Välj enhetstyp och den infraröda sändare som ska användas för att styra din enhet. | Core-literal match |
| 18221 | 854438467 | `component::samsung_infrared::config::step::user::data_description::infrared_emitter_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 18222 | 854438466 | `component::samsung_infrared::config::step::user::data_description::device_type` | The type of device to control. | Typ av enhet att styra. | Shared reference target checked |
| 18223 | 854438465 | `component::samsung_infrared::config::step::user::data::infrared_emitter_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 18224 | 854438464 | `component::samsung_infrared::config::step::user::data::device_type` | Device type | Enhetstyp | Shared reference target checked |
| 18225 | 854438463 | `component::samsung_infrared::config::abort::no_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 18226 | 854438462 | `component::samsung_infrared::config::abort::already_configured` | This device has already been configured with this infrared emitter. | Den här enheten har redan konfigurerats med den här sändaren. | Core-literal match |
| 18227 | 854422463 | `component::imgw_pib::entity::sensor::submerged_vegetation_cover::name` | Submerged vegetation cover | Nedsänkt vegetationstäcke | Core-literal match |
| 18228 | 854422462 | `component::imgw_pib::entity::sensor::floating_vegetation_cover::name` | Floating vegetation cover | Flytande vegetationstäcke | Core-literal match |
| 18229 | 854422461 | `component::imgw_pib::entity::sensor::emergent_vegetation_cover::name` | Emergent vegetation cover | Framväxande vegetationstäcke | Core-literal match |
| 18230 | 854172650 | `component::indevolt::entity::sensor::mos_temperature_discharge::name` | MOS temperature discharge | MOS-temperatur urladdning | Core-literal match |
| 18231 | 854172649 | `component::indevolt::entity::sensor::mos_temperature_charge::name` | MOS temperature charge | MOS-temperatur laddning | Core-literal match |
| 18232 | 854172648 | `component::indevolt::entity::sensor::battery_pack_5_mos_temperature::name` | Battery pack 5 MOS temperature | Batteripaket 5 MOS-temperatur | Core-literal match |
| 18233 | 854172647 | `component::indevolt::entity::sensor::battery_pack_4_mos_temperature::name` | Battery pack 4 MOS temperature | Batteripaket 4 MOS-temperatur | Core-literal match |
| 18234 | 854172646 | `component::indevolt::entity::sensor::battery_pack_3_mos_temperature::name` | Battery pack 3 MOS temperature | Batteripaket 3 MOS-temperatur | Core-literal match |
| 18235 | 854172645 | `component::indevolt::entity::sensor::battery_pack_2_mos_temperature::name` | Battery pack 2 MOS temperature | Batteripaket 2 MOS-temperatur | Core-literal match |
| 18236 | 854172644 | `component::indevolt::entity::sensor::battery_pack_1_mos_temperature::name` | Battery pack 1 MOS temperature | Batteripaket 1 MOS-temperatur | Core-literal match |
| 18237 | 853759312 | `component::unifi_access::exceptions::fetch_thumbnail_failed::message` | Failed to fetch door thumbnail. | Det gick inte att hämta dörrens miniatyrbild. | Core-literal match |
| 18238 | 853759311 | `component::arcam_fmj::exceptions::unsupported_source::message` | Unsupported source: {source}. | Källa stöds inte: {source}. | Core-literal match |
| 18239 | 853759310 | `component::arcam_fmj::exceptions::unsupported_sound_mode::message` | Unsupported sound mode: {sound_mode}. | Ljudläge stöds inte: {sound_mode}. | Core-literal match |
| 18240 | 853759309 | `component::arcam_fmj::exceptions::unsupported_media::message` | Unsupported media: {media}. | Media stöds inte: {media}. | Core-literal match |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 854609021 | `component::marantz_infrared::config::step::user::data_description::infrared_emitter_entity_id` | Sändarentiteten som ska användas för att skicka infraröda kommandon. |
| 854609018 | `component::marantz_infrared::config::abort::no_emitters` | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. |
| 854438463 | `component::samsung_infrared::config::abort::no_emitters` | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 855448767 | `component::elkm1::issues::deprecated_sensor_scripts::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.

The sensor was used in the following automations or scripts:
{items}

Update the above automations or scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. |
| 855448766 | `component::elkm1::issues::deprecated_sensor::title` | Deprecated sensor detected |
| 855448765 | `component::elkm1::issues::deprecated_sensor::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.

Update your dashboards, templates, automations and scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. |
| 854579098 | `component::indevolt::entity::sensor::cycle_count::name` | Cycle count |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
