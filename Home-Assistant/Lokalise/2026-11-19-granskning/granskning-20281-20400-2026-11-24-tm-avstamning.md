# Home Assistant Core – historisk avstämning 20281–20400

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 83 direkta källtexter matchar HA Core-källan; 31 referensanvändningar med 29 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 6 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20281 | 834008492 | `component::tuya::selector::set_feeder_meal_plan::fields::time::name` | Time | Tid | Core-literal match |
| 20282 | 834008491 | `component::tuya::selector::set_feeder_meal_plan::fields::time::description` | Time of the meal. | Tidpunkt för måltiden. | Core-literal match |
| 20283 | 834008490 | `component::tuya::selector::set_feeder_meal_plan::fields::portion::name` | Portion | Portion | Core-literal match |
| 20284 | 834008489 | `component::tuya::selector::set_feeder_meal_plan::fields::portion::description` | Amount in grams | Mängd i gram | Core-literal match |
| 20285 | 834008488 | `component::tuya::selector::set_feeder_meal_plan::fields::enabled::name` | Enabled | Aktiverad | Core-literal match |
| 20286 | 834008487 | `component::tuya::selector::set_feeder_meal_plan::fields::enabled::description` | Whether the meal plan is enabled. | Om måltidsplanen är aktiverad. | Core-literal match |
| 20287 | 834008486 | `component::tuya::selector::set_feeder_meal_plan::fields::days::name` | Days | Dagar | Core-literal match |
| 20288 | 834008485 | `component::tuya::selector::set_feeder_meal_plan::fields::days::description` | Days of the week for the meal plan. | Veckodagar för måltidsplanen. | Core-literal match |
| 20289 | 834008484 | `component::tuya::selector::days_of_week::options::wednesday` | Wednesday | Onsdag | Shared reference target checked |
| 20290 | 834008483 | `component::tuya::selector::days_of_week::options::tuesday` | Tuesday | Tisdag | Shared reference target checked |
| 20291 | 834008482 | `component::tuya::selector::days_of_week::options::thursday` | Thursday | Torsdag | Shared reference target checked |
| 20292 | 834008481 | `component::tuya::selector::days_of_week::options::sunday` | Sunday | Söndag | Shared reference target checked |
| 20293 | 834008480 | `component::tuya::selector::days_of_week::options::saturday` | Saturday | Lördag | Shared reference target checked |
| 20294 | 834008479 | `component::tuya::selector::days_of_week::options::monday` | Monday | Måndag | Shared reference target checked |
| 20295 | 834008478 | `component::tuya::selector::days_of_week::options::friday` | Friday | Fredag | Shared reference target checked |
| 20296 | 834008477 | `component::tuya::exceptions::invalid_meal_plan_data::message` | Unable to parse meal plan data. | Det gick inte att analysera måltidsplandata. | Core-literal match |
| 20297 | 834008476 | `component::tuya::exceptions::device_not_tuya_device::message` | Device with ID {device_id} is not a Tuya feeder. | Enhet med ID {device_id} är inte en Tuya-matare. | Core-literal match |
| 20298 | 834008475 | `component::tuya::exceptions::device_not_support_meal_plan_status::message` | Feeder with ID {device_id} does not support meal plan status. | Matare med ID {device_id} stöder inte måltidsplanstatus. | Core-literal match |
| 20299 | 834008474 | `component::tuya::exceptions::device_not_support_meal_plan_function::message` | Feeder with ID {device_id} does not support meal plan functionality. | Matare med ID {device_id} stöder inte måltidsplanfunktionen. | Core-literal match |
| 20300 | 834008473 | `component::tuya::exceptions::device_not_found::message` | Feeder with ID {device_id} could not be found. | Matare med ID {device_id} kunde inte hittas. | Core-literal match |
| 20301 | 834008208 | `component::evohome::services::set_dhw_override::name` | Set DHW override | Ställ in överstyrning av varmvatten | Core-literal match |
| 20302 | 834008207 | `component::evohome::services::set_dhw_override::fields::state::name` | State | Tillstånd | Core-literal match |
| 20303 | 834008206 | `component::evohome::services::set_dhw_override::fields::state::description` | The DHW state: True (on: heat the water up to the setpoint) or False (off). | Varmvattentillstånd: Sant (på: värm vattnet upp till börvärdet) eller Falskt (av). | Core-literal match |
| 20304 | 834008205 | `component::evohome::services::set_dhw_override::fields::duration::name` | Duration | Varaktighet | Core-literal match |
| 20305 | 834008204 | `component::evohome::services::set_dhw_override::fields::duration::description` | The DHW will revert to its schedule after this time. If 0 the change is until the next scheduled setpoint. | Varmvattnet återgår till sitt schema efter den här tiden. Om värdet är 0 gäller ändringen fram till nästa schemalagda börvärde. | Core-literal match |
| 20306 | 834008203 | `component::evohome::services::set_dhw_override::description` | Overrides a DHW's state, either indefinitely or for a specified duration, after which it will revert to following its schedule. | Åsidosätter en varmvattenberedares tillstånd, antingen på obestämd tid eller under en viss tid. Därefter återgår varmvattenberedaren till att följa sitt schema. | Core-literal match |
| 20307 | 833955522 | `component::telegram_bot::services::send_message_draft::sections::advanced::name` | Advanced | Avancerat | Source-path follow-up open |
| 20308 | 833955521 | `component::telegram_bot::services::send_message_draft::name` | Send message draft | Skicka utkast till meddelande | Core-literal match |
| 20309 | 833955520 | `component::telegram_bot::services::send_message_draft::fields::parse_mode::name` | Parse mode | Tolkningsläge | Shared reference target checked |
| 20310 | 833955519 | `component::telegram_bot::services::send_message_draft::fields::parse_mode::description` | Parser for the message text.<br>See [formatting options]({formatting_options_url}) for more details. | Tolkare för meddelandetexten.<br>Se [formateringsalternativ]({formatting_options_url}) för mer information. | Shared reference target checked |
| 20311 | 833955518 | `component::telegram_bot::services::send_message_draft::fields::message_thread_id::name` | Message thread ID | Meddelandetråds-ID | Shared reference target checked |
| 20312 | 833955517 | `component::telegram_bot::services::send_message_draft::fields::message_thread_id::description` | Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. | Unik identifierare för forumets målmeddelandetråd (ämne); Endast för forumets supergrupper. | Shared reference target checked |
| 20313 | 833955516 | `component::telegram_bot::services::send_message_draft::fields::message::name` | Message | Meddelande | Shared reference target checked |
| 20314 | 833955515 | `component::telegram_bot::services::send_message_draft::fields::message::description` | Available part of the message for temporary notification.<br>Can't parse entities? Format your message according to the [formatting options]({formatting_options_url}). | Den del av meddelandet som är tillgänglig för tillfällig avisering.<br>Går det inte att tolka entiteter? Formatera ditt meddelande enligt [formateringsalternativen]({formatting_options_url}). | Core-literal match |
| 20315 | 833955514 | `component::telegram_bot::services::send_message_draft::fields::entity_id::name` | Notify target | Aviseringsmål | Shared reference target checked |
| 20316 | 833955513 | `component::telegram_bot::services::send_message_draft::fields::entity_id::description` | Notification targets. | Aviseringsmål. | Shared reference target checked |
| 20317 | 833955512 | `component::telegram_bot::services::send_message_draft::fields::draft_id::name` | Draft ID | Utkast-ID | Core-literal match |
| 20318 | 833955511 | `component::telegram_bot::services::send_message_draft::fields::draft_id::description` | Unique identifier of the message draft. Changes of drafts with the same identifier are animated. | Unik identifierare för meddelandeutkastet. Ändringar av utkast med samma identifierare animeras. | Core-literal match |
| 20319 | 833955510 | `component::telegram_bot::services::send_message_draft::fields::config_entry_id::name` | Config entry ID | ID för konfigurationspost | Shared reference target checked |
| 20320 | 833955509 | `component::telegram_bot::services::send_message_draft::fields::config_entry_id::description` | The config entry representing the Telegram bot to send the message draft. | Konfigurationsposten som avser den Telegram-bot som ska skicka meddelandeutkastet. | Core-literal match |
| 20321 | 833955508 | `component::telegram_bot::services::send_message_draft::fields::chat_id::name` | Chat ID | Chatt-ID | Shared reference target checked |
| 20322 | 833955507 | `component::telegram_bot::services::send_message_draft::fields::chat_id::description` | One or more pre-authorized chat IDs to send the message draft to. | Ett eller flera förhandsgodkända chatt-ID:n som meddelandeutkastet ska skickas till. | Core-literal match |
| 20323 | 833955506 | `component::telegram_bot::services::send_message_draft::description` | Shows a partial message (draft) in Telegram while the full message is still being generated. | Visar ett ofullständigt meddelande (utkast) i Telegram medan hela meddelandet fortfarande genereras. | Core-literal match |
| 20324 | 833954697 | `component::pvoutput::exceptions::unknown_error::message` | An unknown error occurred while communicating with the PVOutput service. | Ett okänt fel uppstod vid kommunikationen med PVOutput-tjänsten. | Core-literal match |
| 20325 | 833954696 | `component::pvoutput::exceptions::no_data_available::message` | The PVOutput service has no data available for this system. | Tjänsten PVOutput har inga tillgängliga data för detta system. | Core-literal match |
| 20326 | 833954695 | `component::pvoutput::exceptions::communication_error::message` | An error occurred while communicating with the PVOutput service. | Ett fel uppstod vid kommunikationen med PVOutput-tjänsten. | Core-literal match |
| 20327 | 833947980 | `component::melcloud::entity::binary_sensor::water_pump_status::name` | Water pump {number} | Vattenpump {number} | Core-literal match |
| 20328 | 833947979 | `component::melcloud::entity::binary_sensor::valve_3way_status::name` | 3-way valve | 3-vägsventil | Core-literal match |
| 20329 | 833947978 | `component::melcloud::entity::binary_sensor::valve_2way_status::name` | 2-way valve | 2-vägsventil | Core-literal match |
| 20330 | 833947977 | `component::melcloud::entity::binary_sensor::immersion_heater_status::name` | Immersion heater | Elvärmare | Core-literal match |
| 20331 | 833947976 | `component::melcloud::entity::binary_sensor::booster_heater_status::name` | Booster heater {number} | Boostervärmare {number} | Core-literal match |
| 20332 | 833947975 | `component::melcloud::entity::binary_sensor::boiler_status::name` | Boiler | Panna | Core-literal match |
| 20333 | 833942023 | `component::duco::entity::sensor::ventilation_state::state::man3x3` | MAN3x3 | MAN3x3 | Core-literal match |
| 20334 | 833942022 | `component::duco::entity::sensor::ventilation_state::state::man3x2` | MAN3x2 | MAN3x2 | Core-literal match |
| 20335 | 833942021 | `component::duco::entity::sensor::ventilation_state::state::man3` | MAN3 | MAN3 | Core-literal match |
| 20336 | 833942020 | `component::duco::entity::sensor::ventilation_state::state::man2x3` | MAN2x3 | MAN2x3 | Core-literal match |
| 20337 | 833942019 | `component::duco::entity::sensor::ventilation_state::state::man2x2` | MAN2x2 | MAN2x2 | Core-literal match |
| 20338 | 833942018 | `component::duco::entity::sensor::ventilation_state::state::man2` | MAN2 | MAN2 | Core-literal match |
| 20339 | 833942017 | `component::duco::entity::sensor::ventilation_state::state::man1x3` | MAN1x3 | MAN1x3 | Core-literal match |
| 20340 | 833942016 | `component::duco::entity::sensor::ventilation_state::state::man1x2` | MAN1x2 | MAN1x2 | Core-literal match |
| 20341 | 833942015 | `component::duco::entity::sensor::ventilation_state::state::man1` | MAN1 | MAN1 | Core-literal match |
| 20342 | 833942014 | `component::duco::entity::sensor::ventilation_state::state::empt` | EMPT | EMPT | Core-literal match |
| 20343 | 833942013 | `component::duco::entity::sensor::ventilation_state::state::cnt3` | CNT3 | CNT3 | Core-literal match |
| 20344 | 833942012 | `component::duco::entity::sensor::ventilation_state::state::cnt2` | CNT2 | CNT2 | Core-literal match |
| 20345 | 833942011 | `component::duco::entity::sensor::ventilation_state::state::cnt1` | CNT1 | CNT1 | Core-literal match |
| 20346 | 833942010 | `component::duco::entity::sensor::ventilation_state::state::auto` | AUTO | AUTO | Core-literal match |
| 20347 | 833942009 | `component::duco::entity::sensor::ventilation_state::state::aut3` | AUT3 | AUT3 | Core-literal match |
| 20348 | 833942008 | `component::duco::entity::sensor::ventilation_state::state::aut2` | AUT2 | AUT2 | Core-literal match |
| 20349 | 833942007 | `component::duco::entity::sensor::ventilation_state::state::aut1` | AUT1 | AUT1 | Core-literal match |
| 20350 | 833942006 | `component::duco::entity::sensor::ventilation_state::name` | Ventilation state | Ventilationsläge | Core-literal match |
| 20351 | 833942005 | `component::duco::entity::sensor::iaq_rh::name` | Humidity air quality index | Luftfuktighetsindex | Core-literal match |
| 20352 | 833942004 | `component::duco::entity::sensor::iaq_co2::name` | CO2 air quality index | CO2 luftkvalitetsindex | Core-literal match |
| 20353 | 833933402 | `component::todo::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 20354 | 833933401 | `component::todo::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 20355 | 833933400 | `component::todo::conditions::incomplete::name` | Incomplete to-do items | Ofullständiga uppgifter | Core-literal match |
| 20356 | 833933399 | `component::todo::conditions::incomplete::fields::threshold::name` | Threshold type | Tröskelvärdestyp | Shared reference target checked |
| 20357 | 833933398 | `component::todo::conditions::incomplete::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 20358 | 833933397 | `component::todo::conditions::incomplete::description` | Tests the number of incomplete to-do items in one or more to-do lists. | Testar antalet ofullständiga att göra-uppgifter i en eller flera att göra-listor. | Core-literal match |
| 20359 | 833933396 | `component::todo::conditions::all_completed::name` | All to-do items completed | Alla uppgifter är slutförda | Core-literal match |
| 20360 | 833933395 | `component::todo::conditions::all_completed::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 20361 | 833933394 | `component::todo::conditions::all_completed::description` | Tests if all to-do items are completed in one or more to-do lists. | Testar om alla uppgifter är slutförda i en eller flera att-göra-listor. | Core-literal match |
| 20362 | 833933393 | `component::todo::common::condition_threshold_name` | Threshold type | Tröskelvärdestyp | Core-literal match |
| 20363 | 833933392 | `component::todo::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 20364 | 833897121 | `component::remote::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 20365 | 833897120 | `component::remote::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 20366 | 833897119 | `component::remote::conditions::is_on::name` | Remote is on | Fjärrkontroll är påslagen | Core-literal match |
| 20367 | 833897118 | `component::remote::conditions::is_on::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 20368 | 833897117 | `component::remote::conditions::is_on::description` | Tests if one or more remotes are on. | Testar om en eller flera fjärrkontroller är påslagna. | Core-literal match |
| 20369 | 833897116 | `component::remote::conditions::is_off::name` | Remote is off | Fjärrkontroll är avstängd | Core-literal match |
| 20370 | 833897115 | `component::remote::conditions::is_off::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 20371 | 833897114 | `component::remote::conditions::is_off::description` | Tests if one or more remotes are off. | Testar om en eller flera fjärrkontroller är avstängda. | Core-literal match |
| 20372 | 833897113 | `component::remote::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 20373 | 833637424 | `component::unifi_access::config::step::discovery_confirm::description` | A UniFi Access controller was discovered at {ip_address} ({name}). | En UniFi Access-kontroller har upptäckts på {ip_address} ({name}). | Core-literal match |
| 20374 | 833637423 | `component::unifi_access::config::step::discovery_confirm::data_description::verify_ssl` | Verify the SSL certificate of the controller. | Verifiera styrenhetens SSL-certifikat. | Shared reference target checked |
| 20375 | 833637422 | `component::unifi_access::config::step::discovery_confirm::data_description::api_token` | API token generated in the UniFi Access settings. | API-token som genererats i inställningarna för UniFi Access. | Shared reference target checked |
| 20376 | 833637421 | `component::unifi_access::config::step::discovery_confirm::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 20377 | 833637420 | `component::unifi_access::config::step::discovery_confirm::data::api_token` | API token | API-token | Shared reference target checked |
| 20378 | 833554818 | `component::template::options::step::binary_sensor::data::device_class` | Device class | Enhetsklass | Shared reference target checked |
| 20379 | 832986110 | `component::eurotronic_cometblue::entity::button::sync_time::name` | Sync time | Synka tiden | Core-literal match |
| 20380 | 832984211 | `component::rdw::exceptions::unknown_error::message` | An unknown error occurred while communicating with the RDW service. | Ett okänt fel uppstod vid kommunikationen med RDW-tjänsten. | Core-literal match |
| 20381 | 832984210 | `component::rdw::exceptions::communication_error::message` | An error occurred while communicating with the RDW service. | Ett fel uppstod vid kommunikationen med RDW-tjänsten. | Core-literal match |
| 20382 | 832984209 | `component::luftdaten::exceptions::unknown_error::message` | An unknown error occurred while communicating with the Sensor.Community service. | Ett okänt fel uppstod vid kommunikation med Sensor.Community-tjänsten. | Core-literal match |
| 20383 | 832984208 | `component::luftdaten::exceptions::no_data_received::message` | Did not receive sensor data from the Sensor.Community service. | Det gick inte att hämta sensordata från tjänsten Sensor.Community. | Core-literal match |
| 20384 | 832984207 | `component::luftdaten::exceptions::communication_error::message` | An error occurred while communicating with the Sensor.Community service. | Ett fel uppstod vid kommunikation med Sensor.Community-tjänsten. | Core-literal match |
| 20385 | 832940588 | `component::mastodon::services::post::fields::quote_approval_policy::name` | Who can quote | Vem kan citera | Core-literal match |
| 20386 | 832940587 | `component::mastodon::services::post::fields::quote_approval_policy::description` | Who can quote this post (default: account setting).<br>Ignored if visibility is private or direct. | Vem kan citera det här inlägget (standard: kontoinställning).<br>Ignoreras om synligheten är privat eller direkt. | Core-literal match |
| 20387 | 832940586 | `component::mastodon::selector::quote_approval_policy::options::public` | Public - Anyone can quote this post | Offentligt - Vem som helst kan citera det här inlägget | Core-literal match |
| 20388 | 832940585 | `component::mastodon::selector::quote_approval_policy::options::nobody` | Nobody - No one but you can quote this post | Ingen – Det är bara du som kan citera det här inlägget | Core-literal match |
| 20389 | 832940584 | `component::mastodon::selector::quote_approval_policy::options::followers` | Followers - Only accounts that follow you can quote this post | Följare – Endast konton som följer dig kan citera det här inlägget. | Core-literal match |
| 20390 | 832665517 | `component::elgato::config::step::reconfigure::data_description::host` | The hostname or IP address of your Elgato device. | Värdnamnet eller IP-adressen för din Elgato-enhet. | Shared reference target checked |
| 20391 | 832665516 | `component::elgato::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 20392 | 832665515 | `component::elgato::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 20393 | 832665514 | `component::elgato::config::abort::different_device` | The configured Elgato device is not the same as the one at this address. | Den konfigurerade Elgato-enheten är inte densamma som den på den här adressen. | Core-literal match |
| 20394 | 832433447 | `component::unifi_discovery::config::step::user::description` | UniFi Discovery is set up automatically. | UniFi Discovery konfigureras automatiskt. | Core-literal match |
| 20395 | 832433446 | `component::unifi_discovery::config::abort::discovery_started` | Discovery started | Upptäckten har startat | Core-literal match |
| 20396 | 832433445 | `component::unifi_discovery::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Shared reference target checked |
| 20397 | 832116330 | `component::tailwind::exceptions::unknown_error::message` | An unknown error occurred while communicating with the Tailwind device. | Ett okänt fel uppstod vid kommunikation med Tailwind-enheten. | Core-literal match |
| 20398 | 832086553 | `component::tailwind::config::step::reconfigure::description` | Reconfigure your Tailwind garage door opener.<br><br>This allows you to change the IP address and local control key of your Tailwind device. | Konfigurera om din Tailwind-garagedörröppnare.<br><br>På så sätt kan du ändra IP-adressen och den lokala kontrollnyckeln för din Tailwind-enhet. | Core-literal match |
| 20399 | 832086552 | `component::tailwind::config::step::reconfigure::data_description::token` | To find local control key token, browse to the [Tailwind web portal]({url}), log in with your Tailwind account, and select the [**Local Control Key**]({url}) tab. The 6-digit number shown is your local control key token. | För att hitta den lokala kontroll-token, surfa till [Tailwind webbportal]({url}), logga in med ditt Tailwind-konto och välj fliken [**Local Control Key**]({url}). Det 6-siffriga numret som visas är din lokala kontroll-token. | Shared reference target checked |
| 20400 | 832086551 | `component::tailwind::config::step::reconfigure::data_description::host` | The hostname or IP address of your Tailwind device. You can find the IP address by going into the Tailwind app and selecting your Tailwind device's cog icon. The IP address is shown in the **Device Info** section. | Värdnamnet eller IP-adressen för din Tailwind-enhet. Du kan hitta IP-adressen genom att gå in i Tailwind-appen och välja Tailwind-enhetens kugghjulsikon. IP-adressen visas i avsnittet **Enhetsinfo**. | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 833955522 | `component::telegram_bot::services::send_message_draft::sections::advanced::name` | Advanced |
| 833933402 | `component::todo::selector::condition_behavior::options::any` | Any |
| 833933401 | `component::todo::selector::condition_behavior::options::all` | All |
| 833897121 | `component::remote::selector::condition_behavior::options::any` | Any |
| 833897120 | `component::remote::selector::condition_behavior::options::all` | All |
| 832665515 | `component::elgato::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
