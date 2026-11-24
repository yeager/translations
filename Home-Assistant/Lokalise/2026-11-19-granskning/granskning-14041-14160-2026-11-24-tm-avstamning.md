# Home Assistant Core – historisk avstämning 14041–14160

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 97 direkta källtexter matchar HA Core-källan; 21 referensanvändningar med 21 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Två infrared-referenskonsumenter uppdaterades till exakt samma svenska mål som sina gemensamma referenser, sparades i Lokalise och verifierades med API-readback. Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 14041 | 900325943 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::80-85` | 80 - 85% | 80 - 85% | Core-literal match |
| 14042 | 900325942 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::75-80` | 75 - 80% | 75 - 80% | Core-literal match |
| 14043 | 900325941 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::70-75` | 70 - 75% | 70 - 75% | Core-literal match |
| 14044 | 900325940 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::65-70` | 65 - 70% | 65 - 70% | Core-literal match |
| 14045 | 900325939 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::60-65` | 60 - 65% | 60 - 65% | Core-literal match |
| 14046 | 900325938 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::55-60` | 55 - 60% | 55 - 60% | Core-literal match |
| 14047 | 900325937 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::50-55` | 50 - 55% | 50 - 55% | Core-literal match |
| 14048 | 900325936 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::5-10` | 5 - 10% | 5 - 10% | Core-literal match |
| 14049 | 900325935 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::45-50` | 45 - 50% | 45 - 50% | Core-literal match |
| 14050 | 900325934 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::40-45` | 40 - 45% | 40 - 45% | Core-literal match |
| 14051 | 900325933 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::35-40` | 35 - 40% | 35 - 40% | Core-literal match |
| 14052 | 900325932 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::30-35` | 30 - 35% | 30 - 35% | Core-literal match |
| 14053 | 900325931 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::25-30` | 25 - 30% | 25 - 30% | Core-literal match |
| 14054 | 900325930 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::20-25` | 20 - 25% | 20 - 25% | Core-literal match |
| 14055 | 900325929 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::15-20` | 15 - 20% | 15 - 20% | Core-literal match |
| 14056 | 900325928 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::10-15` | 10 - 15% | 10 - 15% | Core-literal match |
| 14057 | 900325927 | `component::enphase_envoy::entity::select::acb_sleep_soc::state::0-5` | 0 - 5% | 0 - 5% | Core-literal match |
| 14058 | 900325926 | `component::enphase_envoy::entity::select::acb_sleep_soc::name` | Battery sleep SOC target | SOC mål för batterivila | Core-literal match |
| 14059 | 900325925 | `component::enphase_envoy::entity::button::acb_wake::name` | Wake | Vakna | Core-literal match |
| 14060 | 900325924 | `component::enphase_envoy::entity::button::acb_sleep::name` | Sleep | Sova | Core-literal match |
| 14061 | 900325923 | `component::enphase_envoy::entity::binary_sensor::producing::name` | Producing | Producerar | Core-literal match |
| 14062 | 900325922 | `component::enphase_envoy::entity::binary_sensor::operating::name` | Operating | Drift | Core-literal match |
| 14063 | 900325883 | `component::environment_canada::selector::radar_colors::options::8` | 8 colours | 8 färger | Core-literal match |
| 14064 | 900325882 | `component::environment_canada::selector::radar_colors::options::14` | 14 colours | 14 färger | Core-literal match |
| 14065 | 900325881 | `component::environment_canada::options::step::init::data_description::radar_colors` | Number of colours in the rain/snow radar scale (has no effect on the precipitation type layer) | Antal färger på regn-/snöradarskalan (påverkar inte lagret för nederbördstyp) | Source-path follow-up open |
| 14066 | 900325880 | `component::environment_canada::options::step::init::data::radar_colors` | Colour scale | Färgskala | Source-path follow-up open |
| 14067 | 900295375 | `component::google_health::entity::sensor::last_sync_time::name` | Last sync time | Senaste synkroniseringstid | Core-literal match |
| 14068 | 900253834 | `component::melcloud::entity::select::operation_mode::state::room` | Room | Rum | Core-literal match |
| 14069 | 900253833 | `component::melcloud::entity::select::operation_mode::state::flow` | Flow | Flöde | Core-literal match |
| 14070 | 900253832 | `component::melcloud::entity::select::operation_mode::state::curve` | Curve | Kurva | Core-literal match |
| 14071 | 900253831 | `component::melcloud::entity::select::operation_mode::name` | Operation mode | Driftläge | Core-literal match |
| 14072 | 900241233 | `component::device_tracker::issues::deprecated_see_action::title` | Detected use of deprecated action device_tracker.see | Användning av föråldrad åtgärd device_tracker.see upptäcktes | Core-literal match |
| 14073 | 900241232 | `component::device_tracker::issues::deprecated_see_action::fix_flow::step::confirm::title` | Detected use of deprecated action device_tracker.see | Användning av föråldrad åtgärd device_tracker.see upptäcktes | Core-literal match |
| 14074 | 900241231 | `component::device_tracker::issues::deprecated_see_action::fix_flow::step::confirm::description` | The `device_tracker.see` action is deprecated and will be removed in Home Assistant Core 2027.5.<br><br>Use a [template device tracker]({docs_url}) instead, then remove any use of this action from your automations and scripts and select **Submit** to close this issue. | Åtgärden `device_tracker.see` är föråldrad och kommer att tas bort i Home Assistant Core 2027.5.<br><br>Använd en [mall för enhetsspårning]({docs_url}) istället, ta sedan bort all användning av den här åtgärden från dina automatiseringar och skript och välj sedan **Bekräfta** för att stänga det här meddelandet. | Core-literal match |
| 14075 | 900233418 | `component::shelly::entity::update::lora_firmware::name` | LoRa add-on firmware | LoRa add-on firmware | Core-literal match |
| 14076 | 899675264 | `component::eurotronic_cometblue::services::set_schedule::name` | Set schedule | Ställ in schema | Core-literal match |
| 14077 | 899675263 | `component::eurotronic_cometblue::services::set_schedule::fields::wednesday::name` | Wednesday | Onsdag | Shared reference target checked |
| 14078 | 899675262 | `component::eurotronic_cometblue::services::set_schedule::fields::wednesday::description` | Heating time periods for Wednesday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för onsdag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14079 | 899675261 | `component::eurotronic_cometblue::services::set_schedule::fields::tuesday::name` | Tuesday | Tisdag | Shared reference target checked |
| 14080 | 899675260 | `component::eurotronic_cometblue::services::set_schedule::fields::tuesday::description` | Heating time periods for Tuesday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för tisdag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14081 | 899675259 | `component::eurotronic_cometblue::services::set_schedule::fields::thursday::name` | Thursday | Torsdag | Shared reference target checked |
| 14082 | 899675258 | `component::eurotronic_cometblue::services::set_schedule::fields::thursday::description` | Heating time periods for Thursday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för torsdag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14083 | 899675257 | `component::eurotronic_cometblue::services::set_schedule::fields::sunday::name` | Sunday | Söndag | Shared reference target checked |
| 14084 | 899675256 | `component::eurotronic_cometblue::services::set_schedule::fields::sunday::description` | Heating time periods for Sunday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för söndag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14085 | 899675255 | `component::eurotronic_cometblue::services::set_schedule::fields::saturday::name` | Saturday | Lördag | Shared reference target checked |
| 14086 | 899675254 | `component::eurotronic_cometblue::services::set_schedule::fields::saturday::description` | Heating time periods for Saturday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för lördag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14087 | 899675253 | `component::eurotronic_cometblue::services::set_schedule::fields::monday::name` | Monday | Måndag | Shared reference target checked |
| 14088 | 899675252 | `component::eurotronic_cometblue::services::set_schedule::fields::monday::description` | Heating time periods for Monday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för måndag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14089 | 899675251 | `component::eurotronic_cometblue::services::set_schedule::fields::friday::name` | Friday | Fredag | Shared reference target checked |
| 14090 | 899675250 | `component::eurotronic_cometblue::services::set_schedule::fields::friday::description` | Heating time periods for Friday. Up to 4 heat times can be set. | Uppvärmningstidsperioder för fredag. Upp till 4 uppvärmningstider kan ställas in. | Core-literal match |
| 14091 | 899675249 | `component::eurotronic_cometblue::services::set_schedule::description` | Sets the configured heating time ranges of one or multiple devices. Days not included will be left unchanged. | Ställer in de konfigurerade uppvärmningstidsintervallen för en eller flera enheter. Dagar som inte inkluderas kommer att lämnas oförändrade. | Core-literal match |
| 14092 | 899675248 | `component::eurotronic_cometblue::services::set_holiday::name` | Set holiday/away mode | Ställ in semester/borta läge | Core-literal match |
| 14093 | 899675247 | `component::eurotronic_cometblue::services::set_holiday::fields::to::name` | To | Till | Core-literal match |
| 14094 | 899675246 | `component::eurotronic_cometblue::services::set_holiday::fields::to::description` | End of the away mode. | Slut på bortaläge. | Core-literal match |
| 14095 | 899675245 | `component::eurotronic_cometblue::services::set_holiday::fields::temperature::name` | Temperature | Temperatur | Core-literal match |
| 14096 | 899675244 | `component::eurotronic_cometblue::services::set_holiday::fields::temperature::description` | Temperature during away mode. | Temperatur under bortaläge. | Core-literal match |
| 14097 | 899675243 | `component::eurotronic_cometblue::services::set_holiday::fields::from::name` | From | Från | Core-literal match |
| 14098 | 899675242 | `component::eurotronic_cometblue::services::set_holiday::fields::from::description` | Start of the away mode. | Start av bortaläge. | Core-literal match |
| 14099 | 899675241 | `component::eurotronic_cometblue::services::set_holiday::description` | Sets holiday/away mode on one or multiple devices. | Ställer in semester/bortaläge på en eller flera enheter. | Core-literal match |
| 14100 | 899675240 | `component::eurotronic_cometblue::services::get_schedule::name` | Get schedule | Hämta schema | Core-literal match |
| 14101 | 899675239 | `component::eurotronic_cometblue::services::get_schedule::description` | Retrieves the configured heating time ranges of one or multiple devices. | Hämtar de konfigurerade uppvärmningstidsintervallen för en eller flera enheter. | Core-literal match |
| 14102 | 899675238 | `component::anglian_water::issues::consent_required::title` | Anglian Water terms and conditions updated | Anglian Waters villkor har uppdaterats | Core-literal match |
| 14103 | 899675237 | `component::anglian_water::issues::consent_required::description` | The terms and conditions for account {account_number} have been updated. Please visit and log in to your Anglian Water account to accept the new terms and conditions.<br><br>This issue will automatically resolve once the new conditions have been accepted and on the next refresh cycle. | Villkoren för kontot {account_number} har uppdaterats. Logga in på ditt Anglian Water-konto och godkänn de nya villkoren.<br><br>Det här problemet löses automatiskt när de nya villkoren har godkänts vid nästa uppdateringscykel. | Core-literal match |
| 14104 | 899675236 | `component::anglian_water::exceptions::consent_required::message` | The terms and conditions for your Anglian Water account have been updated. Please visit and log in to your Anglian Water account to accept the new terms and conditions. | Villkoren för ditt Anglian Water-konto har uppdaterats. Logga in på ditt Anglian Water-konto och godkänn de nya villkoren. | Core-literal match |
| 14105 | 899675235 | `component::anglian_water::config::error::consent_required` | You need to accept the terms and conditions for your Anglian Water account before using this integration. Log in to their website for further information. | Du måste godkänna villkoren för ditt Anglian Water-konto innan du använder den här integrationen. Logga in på Anglian Waters webbplats för mer information. | Core-literal match |
| 14106 | 899675228 | `component::dsmr::config::step::encryption_key::title` | Encryption key | Krypteringsnyckel | Core-literal match |
| 14107 | 899675227 | `component::dsmr::config::step::encryption_key::data_description::encryption_key` | The encryption key of your meter, provided by your grid operator (32 hexadecimal characters) | Krypteringsnyckeln för din mätare, tillhandahållen av din nätoperatör (32 hexadecimala tecken) | Core-literal match |
| 14108 | 899675226 | `component::dsmr::config::step::encryption_key::data::encryption_key` | Encryption key | Krypteringsnyckel | Core-literal match |
| 14109 | 899675225 | `component::dsmr::config::error::invalid_key` | Failed to decrypt the telegram, check the encryption key | Misslyckades med att dekryptera telegrammet, kontrollera krypteringsnyckeln | Core-literal match |
| 14110 | 899674967 | `component::sky_remote::exceptions::invalid_command::message` | Invalid command: {command} | Ogiltigt kommando: {command} | Core-literal match |
| 14111 | 899674914 | `component::directv::exceptions::send_command_failed::message` | Sending command {command} to device {device} failed. | Det gick inte att skicka kommandot {command} till enheten {device}. | Core-literal match |
| 14112 | 899674840 | `component::vesync::entity::fan::vesync::state_attributes::preset_mode::state::eco` | Eco | Eko | Core-literal match |
| 14113 | 899674833 | `component::smtp::services::send_message::name` | Send message | Skicka meddelande | Core-literal match |
| 14114 | 899674832 | `component::smtp::services::send_message::fields::title::name` | Title | Titel | Core-literal match |
| 14115 | 899674831 | `component::smtp::services::send_message::fields::title::description` | Subject for your email notification. | Ämne för din e-postavisering. | Core-literal match |
| 14116 | 899674830 | `component::smtp::services::send_message::fields::message::name` | Message | Meddelande | Core-literal match |
| 14117 | 899674829 | `component::smtp::services::send_message::fields::message::description` | The plain text message body of the email notification. | Meddelandets brödtext i oformaterad text i e-postmeddelandet. | Core-literal match |
| 14118 | 899674828 | `component::smtp::services::send_message::fields::html::name` | HTML message | HTML meddelande | Core-literal match |
| 14119 | 899674827 | `component::smtp::services::send_message::fields::html::description` | The HTML body of the email notification. Use HTML to create rich email content with formatting, images, links, tables, and custom styling. | HTML texten i e-postmeddelandet. Använd HTML för att skapa rikt e-postinnehåll med formatering, bilder, länkar, tabeller och anpassad stil. | Core-literal match |
| 14120 | 899674826 | `component::smtp::services::send_message::fields::attachments::name` | Attachments | Bilagor | Core-literal match |
| 14121 | 899674825 | `component::smtp::services::send_message::fields::attachments::description` | Attach images or other files from camera, image, TTS, or local media source. When selecting a camera entity, a snapshot of the current view will be captured and attached to the email. | Bifoga bilder eller andra filer från kamera, bild, TTS eller lokal mediekälla. När du väljer en kameraenhet tas en ögonblicksbild av den aktuella vyn och bifogas e-postmeddelandet. | Core-literal match |
| 14122 | 899674824 | `component::smtp::services::send_message::description` | Sends an email notification | Skickar ett e-postmeddelande | Core-literal match |
| 14123 | 899674823 | `component::smtp::selector::attachments::fields::media_source::name` | Media source | Mediekälla | Core-literal match |
| 14124 | 899674822 | `component::smtp::selector::attachments::fields::media_source::description` | Select a camera, image, TTS, or a local media source to attach. Camera sources are captured as an image snapshot when the email is sent. | Välj en kamera, bild, TTS eller en lokal mediekälla att bifoga. Kamerakällorna tas som en ögonblicksbild när e-postmeddelandet skickas. | Core-literal match |
| 14125 | 899674821 | `component::smtp::selector::attachments::fields::filename::name` | Filename | Filnamn | Core-literal match |
| 14126 | 899674820 | `component::smtp::selector::attachments::fields::filename::description` | Specify the filename for the attachment. This is required for camera, image, and TTS media sources, and optional for local media sources. | Ange filnamnet för den bifogade filen. Detta är obligatoriskt för kamera, bild och TTS mediekällor, och valfritt för lokala mediekällor. | Core-literal match |
| 14127 | 899674819 | `component::smtp::selector::attachments::fields::content_id::name` | Content-ID | Innehålls-ID | Core-literal match |
| 14128 | 899674818 | `component::smtp::selector::attachments::fields::content_id::description` | A unique identifier used to embed this image directly inside an HTML email body. | En unik identifierare som används för att bädda in den här bilden direkt i ett HTML e-postmeddelande. | Core-literal match |
| 14129 | 899674817 | `component::smtp::issues::deprecated_notify_action::title` | Detected use of deprecated action {action} | Användning av föråldrad åtgärd upptäcktes {action} | Core-literal match |
| 14130 | 899674816 | `component::smtp::issues::deprecated_notify_action::description` | The action `{action}` is deprecated and will be removed in a future release.<br><br>Please update your automations and scripts to use the notify entities with the `{new_action_1}` or `{new_action_2}` actions instead.<br><br>## Example automation using `{new_action_1}` action:<br><br>{example_yaml_1}<br><br>## Example automation using `{new_action_2}` action:<br><br>{example_yaml_2} | Handlingen `{action}` är föråldrad och kommer att tas bort i en framtida version.<br><br>Vänligen uppdatera dina automatiseringar och skript för att använda aviseringsenheterna med `{new_action_1}` eller `{new_action_2}`handlingar istället.<br><br>## Exempel på automatisering med hjälp av `{new_action_1}` handling:<br><br>{example_yaml_1}<br><br>## Exempel på automatisering med hjälp av `{new_action_2}` handling:<br><br>{example_yaml_2} | Core-literal match |
| 14131 | 899674815 | `component::smtp::exceptions::media_source_not_supported::message` | Media source {media_content_id} is not supported. | Mediekälla {media_content_id} stöds inte. | Core-literal match |
| 14132 | 899674814 | `component::smtp::exceptions::media_source_missing_filename::message` | Cannot attach {media_content_id}. This media source does not provide a filename, you must explicitly specify a filename. | Kan inte bifoga {media_content_id}. Denna mediekälla anger inget filnamn, du måste uttryckligen ange ett filnamn. | Core-literal match |
| 14133 | 899674753 | `component::tplink_omada::entity::sensor::poe_power::name` | Port {port_name} PoE power | Port {port_name}: PoE-effekt | Core-literal match |
| 14134 | 899674659 | `component::dyson_infrared::selector::device_type::options::fan` | Fan | Fläkt | Core-literal match |
| 14135 | 899674658 | `component::dyson_infrared::entity::fan::fan::name` | Dyson Fan | Dyson fläkt | Core-literal match |
| 14136 | 899674657 | `component::dyson_infrared::config::step::user::title` | Set up Infrared Remote | Konfigurera infraröd fjärrkontroll | Core-literal match |
| 14137 | 899674656 | `component::dyson_infrared::config::step::user::description` | Select the device type and the infrared emitter entity to use for controlling your device. | Välj enhetstyp och den infraröda sändarenhet som ska användas för att styra din enhet. | Core-literal match |
| 14138 | 899674655 | `component::dyson_infrared::config::step::user::data_description::infrared_emitter_entity_id` | The infrared emitter entity to use for sending commands. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Shared reference target checked |
| 14139 | 899674654 | `component::dyson_infrared::config::step::user::data_description::device_type` | The type of device to control. | Den typ av enhet som ska styras. | Core-literal match |
| 14140 | 899674653 | `component::dyson_infrared::config::step::user::data::infrared_emitter_entity_id` | Infrared emitter | Infraröd sändare | Shared reference target checked |
| 14141 | 899674652 | `component::dyson_infrared::config::step::user::data::device_type` | Device type | Enhetstyp | Core-literal match |
| 14142 | 899674651 | `component::dyson_infrared::config::abort::no_emitters` | No infrared emitter entities found. Please set up an infrared device first. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Shared reference target checked |
| 14143 | 899674650 | `component::dyson_infrared::config::abort::already_configured` | This device has already been configured with this infrared emitter. | Den här enheten har redan konfigurerats med den här sändaren. | Core-literal match |
| 14144 | 899674628 | `component::gardena_bluetooth::config::flow_title` | {name} ({identifier}) | {name} ({identifier}) | Core-literal match |
| 14145 | 899674529 | `component::mikrotik::entity::update::routerboard_update::name` | RouterBOARD | RouterBOARD | Core-literal match |
| 14146 | 899674528 | `component::mikrotik::entity::update::firmware_update::name` | RouterOS | RouterOS | Core-literal match |
| 14147 | 899674522 | `component::matter::entity::select::selected_chime::name` | Chime sound | Klockljud | Core-literal match |
| 14148 | 899674508 | `component::plugwise::entity::select::select_dhw_mode::state::eco` | Eco | Eco | Core-literal match |
| 14149 | 899674254 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::yellow` | Color: Yellow | Färg: Gul | Shared reference target checked |
| 14150 | 899674253 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::white` | Color: White | Färg: Vit | Shared reference target checked |
| 14151 | 899674252 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::turquoise` | Color: Turquoise | Färg: Turkos | Shared reference target checked |
| 14152 | 899674251 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::tomato` | Color: Tomato | Färg: Tomatröd | Shared reference target checked |
| 14153 | 899674250 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::timer` | Timer | Timer | Core-literal match |
| 14154 | 899674249 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::strobe` | Strobe | Strobe | Shared reference target checked |
| 14155 | 899674248 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::smooth` | Smooth | Smidig | Shared reference target checked |
| 14156 | 899674247 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::sky_blue` | Color: Sky blue | Färg: Himmelsblå | Shared reference target checked |
| 14157 | 899674246 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::red` | Color: Red | Färg: Röd | Shared reference target checked |
| 14158 | 899674245 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::rebecca_purple` | Color: Rebecca purple | Färg: Rebecca lila | Shared reference target checked |
| 14159 | 899674244 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::purple` | Color: Purple | Färg: Lila | Shared reference target checked |
| 14160 | 899674243 | `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::plum` | Color: Plum | Färg: Plommon | Shared reference target checked |

## Sparade referensrättningar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 899674655 | `component::dyson_infrared::config::step::user::data_description::infrared_emitter_entity_id` | Sändarentiteten som ska användas för att skicka infraröda kommandon. |
| 899674651 | `component::dyson_infrared::config::abort::no_emitters` | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 900325881 | `component::environment_canada::options::step::init::data_description::radar_colors` | Number of colours in the rain/snow radar scale (has no effect on the precipitation type layer) |
| 900325880 | `component::environment_canada::options::step::init::data::radar_colors` | Colour scale |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
