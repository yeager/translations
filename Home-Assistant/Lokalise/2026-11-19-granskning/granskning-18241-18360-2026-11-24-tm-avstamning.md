# Home Assistant Core – historisk avstämning 18241–18360

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 33 direkta källtexter matchar HA Core-källan; 42 referensanvändningar med 37 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 45 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 18241 | 853759308 | `component::arcam_fmj::exceptions::connection_failed::message` | Connection failed to the device. | Anslutningen till enheten misslyckades. | Core-literal match |
| 18242 | 853730301 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::yellow` | Yellow | Gul | Core-literal match |
| 18243 | 853730300 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::volume_up` | Volume up | Volym upp | Core-literal match |
| 18244 | 853730299 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::volume_down` | Volume down | Volym ner | Core-literal match |
| 18245 | 853730298 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::up` | Up | Upp | Shared reference target checked |
| 18246 | 853730297 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::unknown` | Unknown | Okänd | Core-literal match |
| 18247 | 853730296 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::text` | Text | Text | Core-literal match |
| 18248 | 853730295 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::subtitle` | Subtitle | Undertext | Core-literal match |
| 18249 | 853730294 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::stop` | Stop | Stopp | Core-literal match |
| 18250 | 853730293 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::settings` | Settings | Inställningar | Core-literal match |
| 18251 | 853730292 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::sap` | SAP | SAP | Core-literal match |
| 18252 | 853730291 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::right` | Right | Höger | Shared reference target checked |
| 18253 | 853730290 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::rewind` | Rewind | Spola tillbaka | Core-literal match |
| 18254 | 853730289 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::red` | Red | Röd | Core-literal match |
| 18255 | 853730288 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::power_on` | Power on | Av | Shared reference target checked |
| 18256 | 853730287 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::power_off` | Power off | På | Shared reference target checked |
| 18257 | 853730286 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::power` | Power | På/Av | Shared reference target checked |
| 18258 | 853730285 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::play` | Play | Spela | Core-literal match |
| 18259 | 853730284 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::pause` | Pause | Paus | Core-literal match |
| 18260 | 853730283 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::ok` | OK | OK | Shared reference target checked |
| 18261 | 853730282 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_9` | Number 9 | Nummer 9 | Shared reference target checked |
| 18262 | 853730281 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_8` | Number 8 | Nummer 8 | Shared reference target checked |
| 18263 | 853730280 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_7` | Number 7 | Nummer 7 | Shared reference target checked |
| 18264 | 853730279 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_6` | Number 6 | Nummer 6 | Shared reference target checked |
| 18265 | 853730278 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_5` | Number 5 | Nummer 5 | Shared reference target checked |
| 18266 | 853730277 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_4` | Number 4 | Nummer 4 | Shared reference target checked |
| 18267 | 853730276 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_3` | Number 3 | Nummer 3 | Shared reference target checked |
| 18268 | 853730275 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_2` | Number 2 | Nummer 2 | Shared reference target checked |
| 18269 | 853730274 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_1` | Number 1 | Nummer 1 | Shared reference target checked |
| 18270 | 853730273 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::num_0` | Number 0 | Nummer 0 | Shared reference target checked |
| 18271 | 853730272 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::mute` | Mute | Tysta | Core-literal match |
| 18272 | 853730271 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::menu` | Menu | Meny | Shared reference target checked |
| 18273 | 853730270 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::list` | List | Lista | Core-literal match |
| 18274 | 853730269 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::left` | Left | Vänster | Shared reference target checked |
| 18275 | 853730268 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::input` | Input | Ingång | Shared reference target checked |
| 18276 | 853730267 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::info` | Info | Info | Shared reference target checked |
| 18277 | 853730266 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::in_start` | In start | I början | Core-literal match |
| 18278 | 853730265 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::home` | Home | Hem | Shared reference target checked |
| 18279 | 853730264 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::hdmi_4` | HDMI 4 | HDMI 4 | Shared reference target checked |
| 18280 | 853730263 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::hdmi_3` | HDMI 3 | HDMI 3 | Shared reference target checked |
| 18281 | 853730262 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::hdmi_2` | HDMI 2 | HDMI 2 | Shared reference target checked |
| 18282 | 853730261 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::hdmi_1` | HDMI 1 | HDMI 1 | Shared reference target checked |
| 18283 | 853730260 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::guide` | Guide | Guide | Shared reference target checked |
| 18284 | 853730259 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::green` | Green | Grön | Core-literal match |
| 18285 | 853730258 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::fast_forward` | Fast forward | Spola fram | Core-literal match |
| 18286 | 853730257 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::ez_adjust` | EZ adjust | EZ-justering | Core-literal match |
| 18287 | 853730256 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::exit` | Exit | Avsluta | Shared reference target checked |
| 18288 | 853730255 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::down` | Down | Ner | Shared reference target checked |
| 18289 | 853730254 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::channel_up` | Channel up | Kanal upp | Core-literal match |
| 18290 | 853730253 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::channel_down` | Channel down | Kanal ner | Core-literal match |
| 18291 | 853730252 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::blue` | Blue | Blå | Core-literal match |
| 18292 | 853730251 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::back` | Back | Tillbaka | Shared reference target checked |
| 18293 | 853730250 | `component::lg_infrared::entity::event::received_command::state_attributes::event_type::state::aspect` | Aspect | Aspekt | Core-literal match |
| 18294 | 853730249 | `component::lg_infrared::entity::event::received_command::name` | Received command | Mottaget kommando | Core-literal match |
| 18295 | 853730248 | `component::lg_infrared::config::step::user::data_description::infrared_receiver_entity_id` | The infrared receiver entity to use for receiving signals. | Den infraröda mottagarenhet som ska användas för att ta emot signaler. | Source-path follow-up open |
| 18296 | 853730247 | `component::lg_infrared::config::step::user::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Source-path follow-up open |
| 18297 | 853730246 | `component::lg_infrared::config::error::missing_infrared_entity` | Select an infrared emitter or receiver. | Välj en infraröd sändare eller mottagare. | Shared reference target checked |
| 18298 | 853730245 | `component::lg_infrared::config::abort::no_infrared_entities` | No infrared entities found. Please set up an infrared device first. | Inga infraröda entiteter hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 18299 | 853721349 | `common::generic::tv` | TV | TV | Source-path follow-up open |
| 18300 | 853721348 | `common::generic::device_type` | Device type | Enhetstyp | Source-path follow-up open |
| 18301 | 853721347 | `common::entity::button::up::name` | Up | Upp | Source-path follow-up open |
| 18302 | 853721346 | `common::entity::button::right::name` | Right | Höger | Source-path follow-up open |
| 18303 | 853721345 | `common::entity::button::power_on::name` | Power on | Av | Source-path follow-up open |
| 18304 | 853721344 | `common::entity::button::power_off::name` | Power off | På | Source-path follow-up open |
| 18305 | 853721343 | `common::entity::button::power::name` | Power | På/Av | Source-path follow-up open |
| 18306 | 853721342 | `common::entity::button::ok::name` | OK | OK | Source-path follow-up open |
| 18307 | 853721341 | `common::entity::button::num_9::name` | Number 9 | Nummer 9 | Source-path follow-up open |
| 18308 | 853721340 | `common::entity::button::num_8::name` | Number 8 | Nummer 8 | Source-path follow-up open |
| 18309 | 853721339 | `common::entity::button::num_7::name` | Number 7 | Nummer 7 | Source-path follow-up open |
| 18310 | 853721338 | `common::entity::button::num_6::name` | Number 6 | Nummer 6 | Source-path follow-up open |
| 18311 | 853721337 | `common::entity::button::num_5::name` | Number 5 | Nummer 5 | Source-path follow-up open |
| 18312 | 853721336 | `common::entity::button::num_4::name` | Number 4 | Nummer 4 | Source-path follow-up open |
| 18313 | 853721335 | `common::entity::button::num_3::name` | Number 3 | Nummer 3 | Source-path follow-up open |
| 18314 | 853721334 | `common::entity::button::num_2::name` | Number 2 | Nummer 2 | Source-path follow-up open |
| 18315 | 853721333 | `common::entity::button::num_1::name` | Number 1 | Nummer 1 | Source-path follow-up open |
| 18316 | 853721332 | `common::entity::button::num_0::name` | Number 0 | Nummer 0 | Source-path follow-up open |
| 18317 | 853721331 | `common::entity::button::menu::name` | Menu | Meny | Source-path follow-up open |
| 18318 | 853721330 | `common::entity::button::left::name` | Left | Vänster | Source-path follow-up open |
| 18319 | 853721329 | `common::entity::button::input::name` | Input | Ingång | Source-path follow-up open |
| 18320 | 853721328 | `common::entity::button::info::name` | Info | Info | Source-path follow-up open |
| 18321 | 853721327 | `common::entity::button::home::name` | Home | Hem | Source-path follow-up open |
| 18322 | 853721326 | `common::entity::button::hdmi_4::name` | HDMI 4 | HDMI 4 | Source-path follow-up open |
| 18323 | 853721325 | `common::entity::button::hdmi_3::name` | HDMI 3 | HDMI 3 | Source-path follow-up open |
| 18324 | 853721324 | `common::entity::button::hdmi_2::name` | HDMI 2 | HDMI 2 | Source-path follow-up open |
| 18325 | 853721323 | `common::entity::button::hdmi_1::name` | HDMI 1 | HDMI 1 | Source-path follow-up open |
| 18326 | 853721322 | `common::entity::button::guide::name` | Guide | Guide | Source-path follow-up open |
| 18327 | 853721321 | `common::entity::button::exit::name` | Exit | Avsluta | Source-path follow-up open |
| 18328 | 853721320 | `common::entity::button::down::name` | Down | Ner | Source-path follow-up open |
| 18329 | 853721319 | `common::entity::button::back::name` | Back | Tillbaka | Source-path follow-up open |
| 18330 | 853721318 | `common::config_flow::data_description::radio_frequency_transmitter` | The radio frequency transmitter to use for sending commands. | Den radiofrekvenssändare som ska användas för att skicka kommandon. | Source-path follow-up open |
| 18331 | 853721317 | `common::config_flow::data_description::infrared_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Source-path follow-up open |
| 18332 | 853721316 | `common::config_flow::data::radio_frequency_transmitter` | Radio frequency transmitter | Sändare för radiofrekvens | Source-path follow-up open |
| 18333 | 853721315 | `common::config_flow::data::infrared_receiver_entity_id` | Infrared receiver | Infraröd mottagare | Source-path follow-up open |
| 18334 | 853721314 | `common::config_flow::data::infrared_entity_id` | Infrared emitter | Infraröd sändare | Source-path follow-up open |
| 18335 | 853721313 | `common::config_flow::abort::no_radio_frequency_transmitters` | No radio frequency transmitters are available. Please set up a device first. | Inga radiofrekvenssändare finns tillgängliga. Vänligen installera en enhet först. | Source-path follow-up open |
| 18336 | 853721312 | `common::config_flow::abort::no_infrared_entities` | No infrared entities found. Please set up an infrared device first. | Inga infraröda entiteter hittades. Konfigurera först en infraröd enhet. | Source-path follow-up open |
| 18337 | 853721311 | `common::config_flow::abort::no_infrared_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Source-path follow-up open |
| 18338 | 853721310 | `common::config_flow::abort::no_compatible_radio_frequency_transmitters` | No radio frequency transmitter supports {frequency} {modulation} transmissions. Please add a compatible transmitter first. | Ingen radiofrekvenssändare stöder {frequency} {modulation}-sändningar. Lägg först till en kompatibel sändare. | Source-path follow-up open |
| 18339 | 853562377 | `component::switchbot::entity::light::air_purifier_light::name` | Light | Lampa | Shared reference target checked |
| 18340 | 853562314 | `component::satel_integra::config_subentries::zone::step::user::data_description::enable_temperature_sensor` | Enable this if the zone also reports a temperature reading | Aktivera detta om zonen även rapporterar ett temperaturvärde | Core-literal match |
| 18341 | 853562313 | `component::satel_integra::config_subentries::zone::step::user::data::enable_temperature_sensor` | Enable temperature sensor | Aktivera temperatursensor | Core-literal match |
| 18342 | 853562312 | `component::satel_integra::config_subentries::zone::step::reconfigure::data_description::enable_temperature_sensor` | Enable this if the zone also reports a temperature reading | Aktivera detta om zonen även rapporterar ett temperaturvärde | Shared reference target checked |
| 18343 | 853562311 | `component::satel_integra::config_subentries::zone::step::reconfigure::data::enable_temperature_sensor` | Enable temperature sensor | Aktivera temperatursensor | Shared reference target checked |
| 18344 | 853562310 | `component::satel_integra::config_subentries::zone::error::zone_does_not_report_temperature` | This zone does not report temperature data. | Denna zon rapporterar inte temperaturdata. | Core-literal match |
| 18345 | 853562309 | `component::satel_integra::config_subentries::zone::abort::entry_not_loaded` | Cannot validate zone temperature support while the integration is disabled. | Det går inte att validera stöd för zontemperatur när integrationen är inaktiverad. | Core-literal match |
| 18346 | 853560491 | `component::pyload::config::step::user::data_description::api_key` | The API key to authenticate with pyLoad. To create a new API key, navigate to **Settings > Users > Actions > Manage API Keys** and select **Generate**. | API-nyckeln för att autentisera med pyLoad. För att skapa en ny API-nyckel går du till **Inställningar > Användare > Åtgärder > Hantera API-nycklar** och väljer **Generera**. | Core-literal match |
| 18347 | 853560490 | `component::pyload::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 18348 | 853560489 | `component::pyload::config::step::reconfigure::data_description::api_key` | The API key to authenticate with pyLoad. To create a new API key, navigate to **Settings > Users > Actions > Manage API Keys** and select **Generate**. | API-nyckeln för att autentisera med pyLoad. För att skapa en ny API-nyckel går du till **Inställningar > Användare > Åtgärder > Hantera API-nycklar** och väljer **Generera**. | Shared reference target checked |
| 18349 | 853560488 | `component::pyload::config::step::reconfigure::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 18350 | 853560487 | `component::pyload::config::step::reauth_confirm::data_description::api_key` | The API key to authenticate with pyLoad. To create a new API key, navigate to **Settings > Users > Actions > Manage API Keys** and select **Generate**. | API-nyckeln för att autentisera med pyLoad. För att skapa en ny API-nyckel går du till **Inställningar > Användare > Åtgärder > Hantera API-nycklar** och väljer **Generera**. | Shared reference target checked |
| 18351 | 853560486 | `component::pyload::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 18352 | 853560485 | `component::pyload::config::step::hassio_confirm::data_description::api_key` | The API key to authenticate with pyLoad. To create a new API key, navigate to **Settings > Users > Actions > Manage API Keys** and select **Generate**. | API-nyckeln för att autentisera med pyLoad. För att skapa en ny API-nyckel går du till **Inställningar > Användare > Åtgärder > Hantera API-nycklar** och väljer **Generera**. | Shared reference target checked |
| 18353 | 853560484 | `component::pyload::config::step::hassio_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 18354 | 853488085 | `component::guntamatic::entity::sensor::status::name` | Status | Status | Core-literal match |
| 18355 | 853488084 | `component::guntamatic::entity::sensor::room_2_temperature::name` | Room 2 temperature | Temperatur i rum 2 | Source-path follow-up open |
| 18356 | 853488083 | `component::guntamatic::entity::sensor::room_1_temperature::name` | Room 1 temperature | Temperatur i rum 1 | Source-path follow-up open |
| 18357 | 853488082 | `component::guntamatic::entity::sensor::room_0_temperature::name` | Room 0 temperature | Temperatur i rum 0 | Source-path follow-up open |
| 18358 | 853488081 | `component::guntamatic::entity::sensor::program::state::timer` | Timer | Timer | Core-literal match |
| 18359 | 853488080 | `component::guntamatic::entity::sensor::program::state::off` | Off | Av | Shared reference target checked |
| 18360 | 853488079 | `component::guntamatic::entity::sensor::program::state::hibernate_to` | Away mode | Bortaläge | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 853730248 | `component::lg_infrared::config::step::user::data_description::infrared_receiver_entity_id` | The infrared receiver entity to use for receiving signals. |
| 853730247 | `component::lg_infrared::config::step::user::data::infrared_receiver_entity_id` | Infrared receiver |
| 853721349 | `common::generic::tv` | TV |
| 853721348 | `common::generic::device_type` | Device type |
| 853721347 | `common::entity::button::up::name` | Up |
| 853721346 | `common::entity::button::right::name` | Right |
| 853721345 | `common::entity::button::power_on::name` | Power on |
| 853721344 | `common::entity::button::power_off::name` | Power off |
| 853721343 | `common::entity::button::power::name` | Power |
| 853721342 | `common::entity::button::ok::name` | OK |
| 853721341 | `common::entity::button::num_9::name` | Number 9 |
| 853721340 | `common::entity::button::num_8::name` | Number 8 |
| 853721339 | `common::entity::button::num_7::name` | Number 7 |
| 853721338 | `common::entity::button::num_6::name` | Number 6 |
| 853721337 | `common::entity::button::num_5::name` | Number 5 |
| 853721336 | `common::entity::button::num_4::name` | Number 4 |
| 853721335 | `common::entity::button::num_3::name` | Number 3 |
| 853721334 | `common::entity::button::num_2::name` | Number 2 |
| 853721333 | `common::entity::button::num_1::name` | Number 1 |
| 853721332 | `common::entity::button::num_0::name` | Number 0 |
| 853721331 | `common::entity::button::menu::name` | Menu |
| 853721330 | `common::entity::button::left::name` | Left |
| 853721329 | `common::entity::button::input::name` | Input |
| 853721328 | `common::entity::button::info::name` | Info |
| 853721327 | `common::entity::button::home::name` | Home |
| 853721326 | `common::entity::button::hdmi_4::name` | HDMI 4 |
| 853721325 | `common::entity::button::hdmi_3::name` | HDMI 3 |
| 853721324 | `common::entity::button::hdmi_2::name` | HDMI 2 |
| 853721323 | `common::entity::button::hdmi_1::name` | HDMI 1 |
| 853721322 | `common::entity::button::guide::name` | Guide |
| 853721321 | `common::entity::button::exit::name` | Exit |
| 853721320 | `common::entity::button::down::name` | Down |
| 853721319 | `common::entity::button::back::name` | Back |
| 853721318 | `common::config_flow::data_description::radio_frequency_transmitter` | The radio frequency transmitter to use for sending commands. |
| 853721317 | `common::config_flow::data_description::infrared_entity_id` | The infrared emitter entity to use for sending commands. |
| 853721316 | `common::config_flow::data::radio_frequency_transmitter` | Radio frequency transmitter |
| 853721315 | `common::config_flow::data::infrared_receiver_entity_id` | Infrared receiver |
| 853721314 | `common::config_flow::data::infrared_entity_id` | Infrared emitter |
| 853721313 | `common::config_flow::abort::no_radio_frequency_transmitters` | No radio frequency transmitters are available. Please set up a device first. |
| 853721312 | `common::config_flow::abort::no_infrared_entities` | No infrared entities found. Please set up an infrared device first. |
| 853721311 | `common::config_flow::abort::no_infrared_emitters` | No infrared emitter entities found. Please set up an infrared device first. |
| 853721310 | `common::config_flow::abort::no_compatible_radio_frequency_transmitters` | No radio frequency transmitter supports {frequency} {modulation} transmissions. Please add a compatible transmitter first. |
| 853488084 | `component::guntamatic::entity::sensor::room_2_temperature::name` | Room 2 temperature |
| 853488083 | `component::guntamatic::entity::sensor::room_1_temperature::name` | Room 1 temperature |
| 853488082 | `component::guntamatic::entity::sensor::room_0_temperature::name` | Room 0 temperature |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
