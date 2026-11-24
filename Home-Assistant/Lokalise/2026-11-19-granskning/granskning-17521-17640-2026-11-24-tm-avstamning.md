# Home Assistant Core – historisk avstämning 17521–17640

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 83 direkta källtexter matchar HA Core-källan; 28 referensanvändningar med 20 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 9 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17521 | 860556934 | `component::system_bridge::selector::key::options::numpad_3` | NumPad 3 | NumPad 3 | Core-literal match |
| 17522 | 860556933 | `component::system_bridge::selector::key::options::numpad_2` | NumPad 2 | NumPad 2 | Core-literal match |
| 17523 | 860556932 | `component::system_bridge::selector::key::options::numpad_1` | NumPad 1 | NumPad 1 | Core-literal match |
| 17524 | 860556931 | `component::system_bridge::selector::key::options::numpad_0` | NumPad 0 | NumPad 0 | Core-literal match |
| 17525 | 860556930 | `component::system_bridge::selector::key::options::lights_mon_up` | Display brightness up | Skärmljusstyrka upp | Core-literal match |
| 17526 | 860556929 | `component::system_bridge::selector::key::options::lights_mon_down` | Display brightness down | Skärmljusstyrka ner | Core-literal match |
| 17527 | 860556928 | `component::system_bridge::selector::key::options::lights_kbd_up` | Keyboard backlight brightness up | Tangentbordsbelysning upp | Core-literal match |
| 17528 | 860556927 | `component::system_bridge::selector::key::options::lights_kbd_toggle` | Toggle keyboard backlight | Växla Tangentbordsbelysning | Core-literal match |
| 17529 | 860556926 | `component::system_bridge::selector::key::options::lights_kbd_down` | Keyboard backlight brightness down | Tangentbordsbelysning ner | Core-literal match |
| 17530 | 860556925 | `component::system_bridge::selector::key::options::left` | Left | Vänster | Shared reference target checked |
| 17531 | 860556924 | `component::system_bridge::selector::key::options::insert` | Insert | Insert | Core-literal match |
| 17532 | 860556923 | `component::system_bridge::selector::key::options::home` | Home | Hem | Shared reference target checked |
| 17533 | 860556922 | `component::system_bridge::selector::key::options::f9` | F9 | F9 | Core-literal match |
| 17534 | 860556921 | `component::system_bridge::selector::key::options::f8` | F8 | F8 | Core-literal match |
| 17535 | 860556920 | `component::system_bridge::selector::key::options::f7` | F7 | F7 | Core-literal match |
| 17536 | 860556919 | `component::system_bridge::selector::key::options::f6` | F6 | F6 | Core-literal match |
| 17537 | 860556918 | `component::system_bridge::selector::key::options::f5` | F5 | F5 | Core-literal match |
| 17538 | 860556917 | `component::system_bridge::selector::key::options::f4` | F4 | F4 | Core-literal match |
| 17539 | 860556916 | `component::system_bridge::selector::key::options::f3` | F3 | F3 | Core-literal match |
| 17540 | 860556915 | `component::system_bridge::selector::key::options::f2` | F2 | F2 | Core-literal match |
| 17541 | 860556914 | `component::system_bridge::selector::key::options::f12` | F12 | F12 | Core-literal match |
| 17542 | 860556913 | `component::system_bridge::selector::key::options::f11` | F11 | F11 | Core-literal match |
| 17543 | 860556912 | `component::system_bridge::selector::key::options::f10` | F10 | F10 | Core-literal match |
| 17544 | 860556911 | `component::system_bridge::selector::key::options::f1` | F1 | F1 | Core-literal match |
| 17545 | 860556910 | `component::system_bridge::selector::key::options::escape` | Escape | Escape | Core-literal match |
| 17546 | 860556909 | `component::system_bridge::selector::key::options::enter` | Enter | Enter | Core-literal match |
| 17547 | 860556908 | `component::system_bridge::selector::key::options::end` | End | End | Core-literal match |
| 17548 | 860556907 | `component::system_bridge::selector::key::options::down` | Down | Ner | Shared reference target checked |
| 17549 | 860556906 | `component::system_bridge::selector::key::options::delete` | Delete | Ta bort | Core-literal match |
| 17550 | 860556905 | `component::system_bridge::selector::key::options::control` | Control | Kontroll | Core-literal match |
| 17551 | 860556904 | `component::system_bridge::selector::key::options::command` | Command | Kommando | Core-literal match |
| 17552 | 860556903 | `component::system_bridge::selector::key::options::backspace` | Backspace | Radera | Core-literal match |
| 17553 | 860556902 | `component::system_bridge::selector::key::options::audio_vol_up` | Volume up | Volym upp | Core-literal match |
| 17554 | 860556901 | `component::system_bridge::selector::key::options::audio_vol_down` | Volume down | Volym ner | Core-literal match |
| 17555 | 860556900 | `component::system_bridge::selector::key::options::audio_stop` | Stop media | Stoppa media | Core-literal match |
| 17556 | 860556899 | `component::system_bridge::selector::key::options::audio_rewind` | Rewind track | Spola tillbaka spår | Core-literal match |
| 17557 | 860556898 | `component::system_bridge::selector::key::options::audio_repeat` | Repeat track | Upprepa spår | Core-literal match |
| 17558 | 860556897 | `component::system_bridge::selector::key::options::audio_random` | Random track | Slumpvis spår | Core-literal match |
| 17559 | 860556896 | `component::system_bridge::selector::key::options::audio_prev` | Previous track | Föregående spår | Core-literal match |
| 17560 | 860556895 | `component::system_bridge::selector::key::options::audio_play` | Play media | Spela media | Core-literal match |
| 17561 | 860556894 | `component::system_bridge::selector::key::options::audio_pause` | Pause media | Pausa media | Core-literal match |
| 17562 | 860556893 | `component::system_bridge::selector::key::options::audio_next` | Next track | Nästa spår | Core-literal match |
| 17563 | 860556892 | `component::system_bridge::selector::key::options::audio_mute` | Mute | Mute | Core-literal match |
| 17564 | 860556891 | `component::system_bridge::selector::key::options::audio_forward` | Fast-Forward track | Snabbspola spår | Core-literal match |
| 17565 | 860556890 | `component::system_bridge::selector::key::options::alt` | Alt | Alt | Core-literal match |
| 17566 | 860556511 | `component::hassio::system_health::info::disk_life_time` | Disk lifetime | Diskens livslängd | Core-literal match |
| 17567 | 860556202 | `component::homematicip_cloud::entity::binary_sensor::raining::name` | Raining | Regnar | Core-literal match |
| 17568 | 860556201 | `component::homematicip_cloud::entity::binary_sensor::chamber_degraded::name` | Chamber degraded | Kammaren har försämrats | Core-literal match |
| 17569 | 860555078 | `component::homematicip_cloud::entity::event::button::state_attributes::event_type::state::short_release` | Short release | Kort uppsläpp | Core-literal match |
| 17570 | 860555077 | `component::homematicip_cloud::entity::event::button::state_attributes::event_type::state::long_release` | Long release | Långt uppsläpp | Core-literal match |
| 17571 | 860555076 | `component::homematicip_cloud::entity::event::button::state_attributes::event_type::state::long_press` | Long press | Lång nedtryckning | Core-literal match |
| 17572 | 860555075 | `component::homematicip_cloud::entity::event::button::name` | Button {channel} | Knapp {channel} | Core-literal match |
| 17573 | 860551590 | `component::local_file::exceptions::not_readable_path::message` | Path {file_path} is not readable | Sökvägen {file_path} går inte att läsa | Core-literal match |
| 17574 | 860541805 | `component::color_extractor::services::get_color::name` | Get predominant color | Hämta dominerande färg | Core-literal match |
| 17575 | 860541804 | `component::color_extractor::services::get_color::fields::color_extract_url::name` | URL | URL | Shared reference target checked |
| 17576 | 860541803 | `component::color_extractor::services::get_color::fields::color_extract_url::description` | The URL of the image we want to extract RGB values from. Must be allowed in allowlist_external_urls. | URL för bilden som RGB-värden ska extraheras från. Måste vara tillåten i allowlist_external_urls. | Core-literal match |
| 17577 | 860541802 | `component::color_extractor::services::get_color::fields::color_extract_path::name` | Path | Sökväg | Shared reference target checked |
| 17578 | 860541801 | `component::color_extractor::services::get_color::fields::color_extract_path::description` | The full system path to the image we want to extract RGB values from. Must be allowed in allowlist_external_dirs. | Den fullständiga systemsökvägen till bilden som RGB-värden ska extraheras från. Måste vara tillåten i allowlist_external_dirs. | Core-literal match |
| 17579 | 860541800 | `component::color_extractor::services::get_color::description` | Gets the predominant RGB color found in the image provided by URL or file path. | Hämtar den dominerande RGB-färgen som finns i bilden som anges via URL eller filsökväg. | Core-literal match |
| 17580 | 860541799 | `component::color_extractor::exceptions::invalid_image::message` | Bad image {image_reference} from {image_type} provided, are you sure it's an image? | Den angivna bilden {image_reference} från {image_type} är felaktig. Är du säker på att den är en bild? | Core-literal match |
| 17581 | 860524557 | `component::yoto::exceptions::update_error::message` | An error occurred while communicating with Yoto. | Fel vid kommunikation med Yoto. | Core-literal match |
| 17582 | 860524556 | `component::yoto::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry | OAuth2-implementation kan ej nås, försöker igen | Source-path follow-up open |
| 17583 | 860524555 | `component::yoto::exceptions::command_failed::message` | Could not send the command to the Yoto player. | Yoto-kommandot misslyckades. | Core-literal match |
| 17584 | 860524554 | `component::yoto::config::step::pick_implementation::title` | Pick authentication method | Välj autentiseringsmetod | Shared reference target checked |
| 17585 | 860524553 | `component::yoto::config::step::pick_implementation::data_description::implementation` | The credentials you want to use to authenticate. | Uppgifterna du vill använda för autentisering. | Shared reference target checked |
| 17586 | 860524552 | `component::yoto::config::step::pick_implementation::data::implementation` | Application credentials | Autentiseringsuppgifter för applikation | Shared reference target checked |
| 17587 | 860524551 | `component::yoto::config::step::oauth_discovery::description` | Home Assistant has found a Yoto player on your network. Press **Submit** to continue setting up Yoto. | Home Assistant har hittat en Yoto-spelare i ditt nätverk. Tryck på **Bekräfta** för att fortsätta med installationen av Yoto. | Core-literal match |
| 17588 | 860524550 | `component::yoto::config::create_entry::default` | Successfully authenticated | Autentisering lyckades | Shared reference target checked |
| 17589 | 860524549 | `component::yoto::config::abort::user_rejected_authorize` | Account linking rejected: {error} | Kontolänkning avvisades: {error} | Source-path follow-up open |
| 17590 | 860524548 | `component::yoto::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. | OAuth-auktoriseringsfel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 17591 | 860524547 | `component::yoto::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. | Tidsgränsen överskreds när OAuth-token hämtades. | Source-path follow-up open |
| 17592 | 860524546 | `component::yoto::config::abort::oauth_failed` | Error while obtaining access token. | Fel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 17593 | 860524545 | `component::yoto::config::abort::oauth_error` | Received invalid token data. | Ogiltiga tokendata mottogs. | Source-path follow-up open |
| 17594 | 860524544 | `component::yoto::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) | Ingen webbadress är tillgänglig. [Se hjälpavsnittet]({docs_url}) för information om det här felet. | Source-path follow-up open |
| 17595 | 860524543 | `component::yoto::config::abort::missing_credentials` | The integration requires application credentials. | Integrationen kräver applikationsuppgifter. | Source-path follow-up open |
| 17596 | 860524542 | `component::yoto::config::abort::missing_configuration` | The component is not configured. Please follow the documentation. | Komponenten har inte konfigurerats. Följ dokumentationen. | Shared reference target checked |
| 17597 | 860524541 | `component::yoto::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. | Tidsgränsen överskreds vid generering av en auktoriserings-URL. | Source-path follow-up open |
| 17598 | 860524540 | `component::yoto::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 17599 | 860517933 | `component::ghost::entity::sensor::gift_members::name` | Gift members | Gåvomedlemmar | Core-literal match |
| 17600 | 860445292 | `component::bthome::entity::sensor::settings_revision::name` | Settings revision | Inställningsrevision | Core-literal match |
| 17601 | 860445291 | `component::bthome::entity::sensor::light_level::name` | Light level | Ljusnivå | Core-literal match |
| 17602 | 860445290 | `component::bthome::entity::event::command::state_attributes::event_type::state::toggle` | Toggle | Växla | Core-literal match |
| 17603 | 860445289 | `component::bthome::entity::event::command::state_attributes::event_type::state::step_up` | Step up | Steg upp | Core-literal match |
| 17604 | 860445288 | `component::bthome::entity::event::command::state_attributes::event_type::state::step_down` | Step down | Steg ner | Core-literal match |
| 17605 | 860445287 | `component::bthome::entity::event::command::state_attributes::event_type::state::on` | On | På | Core-literal match |
| 17606 | 860445286 | `component::bthome::entity::event::command::state_attributes::event_type::state::off` | Off | Av | Core-literal match |
| 17607 | 860445285 | `component::bthome::device_automation::trigger_type::command` | Command "{subtype}" | Kommando "{subtype}" | Core-literal match |
| 17608 | 860445284 | `component::bthome::device_automation::trigger_subtype::toggle` | Toggle | Växla | Core-literal match |
| 17609 | 860445283 | `component::bthome::device_automation::trigger_subtype::step_up` | Step up | Steg upp | Core-literal match |
| 17610 | 860445282 | `component::bthome::device_automation::trigger_subtype::step_down` | Step down | Steg ner | Core-literal match |
| 17611 | 860445281 | `component::bthome::device_automation::trigger_subtype::on` | On | På | Core-literal match |
| 17612 | 860445280 | `component::bthome::device_automation::trigger_subtype::off` | Off | Av | Core-literal match |
| 17613 | 860442863 | `component::wake_on_lan::services::send_magic_packet::fields::secureon_password::name` | SecureOn password | SecureOn-lösenord | Shared reference target checked |
| 17614 | 860442862 | `component::wake_on_lan::services::send_magic_packet::fields::secureon_password::description` | The SecureOn password in 6 bytes hexadecimal format to append to the magic packet. | SecureOn-lösenordet i hexadecimalt format på 6 byte som ska läggas till i det magiska paketet. | Shared reference target checked |
| 17615 | 860442861 | `component::wake_on_lan::options::step::init::data_description::secureon_password` | The SecureOn password in 6 bytes hexadecimal format to append to the magic packet. | SecureOn-lösenordet i hexadecimalt format på 6 byte som ska läggas till i det magiska paketet. | Shared reference target checked |
| 17616 | 860442860 | `component::wake_on_lan::options::step::init::data::secureon_password` | SecureOn password | SecureOn-lösenord | Shared reference target checked |
| 17617 | 860442859 | `component::wake_on_lan::config::step::user::data_description::secureon_password` | The SecureOn password in 6 bytes hexadecimal format to append to the magic packet. | SecureOn-lösenordet i hexadecimalt format på 6 byte som ska läggas till i det magiska paketet. | Core-literal match |
| 17618 | 860442858 | `component::wake_on_lan::config::step::user::data::secureon_password` | SecureOn password | SecureOn-lösenord | Core-literal match |
| 17619 | 860356342 | `component::smartthings::entity::sensor::water_usage_month::name` | Water usage this month | Vattenförbrukningen denna månad | Core-literal match |
| 17620 | 860356341 | `component::smartthings::entity::sensor::water_usage_day::name` | Water usage today | Vattenförbrukningen idag | Core-literal match |
| 17621 | 860356340 | `component::smartthings::entity::sensor::water_usage_current::name` | Current water usage | Nuvarande vattenförbrukning | Core-literal match |
| 17622 | 860356339 | `component::ouman_eh_800::entity::climate::heating_circuit::state_attributes::preset_mode::state::temperature_drop` | Temperature drop | Temperaturfall | Shared reference target checked |
| 17623 | 860356338 | `component::ouman_eh_800::entity::climate::heating_circuit::state_attributes::preset_mode::state::big_temperature_drop` | Big temperature drop | Stort temperaturfall | Shared reference target checked |
| 17624 | 860356337 | `component::ouman_eh_800::entity::climate::heating_circuit::state_attributes::preset_mode::state::automatic` | Auto | Auto | Shared reference target checked |
| 17625 | 860335687 | `component::ouman_eh_800::entity::select::relay_pump_summer_stop_control::state::stop` | Stop | Stoppa | Shared reference target checked |
| 17626 | 860335686 | `component::ouman_eh_800::entity::select::relay_pump_summer_stop_control::state::run` | Run | Kör | Core-literal match |
| 17627 | 860335685 | `component::ouman_eh_800::entity::select::relay_pump_summer_stop_control::state::auto` | Auto | Auto | Shared reference target checked |
| 17628 | 860335684 | `component::ouman_eh_800::entity::select::relay_pump_summer_stop_control::name` | Pump summer stop | Pump summer stopp | Core-literal match |
| 17629 | 860335683 | `component::ouman_eh_800::entity::select::relay_control::state::on` | On | På | Shared reference target checked |
| 17630 | 860335682 | `component::ouman_eh_800::entity::select::relay_control::state::off` | Off | Av | Shared reference target checked |
| 17631 | 860335681 | `component::ouman_eh_800::entity::select::relay_control::state::auto` | Auto | Auto | Shared reference target checked |
| 17632 | 860335680 | `component::ouman_eh_800::entity::select::relay_control::name` | Relay control | Reläkontroll | Core-literal match |
| 17633 | 860335679 | `component::ouman_eh_800::entity::select::operation_mode::state::temperature_drop` | Temperature drop | Temperaturfall | Shared reference target checked |
| 17634 | 860335678 | `component::ouman_eh_800::entity::select::operation_mode::state::shutdown` | Standby | Viloläge | Shared reference target checked |
| 17635 | 860335677 | `component::ouman_eh_800::entity::select::operation_mode::state::normal_temperature` | Nominal temperature | Nominell temperatur | Core-literal match |
| 17636 | 860335676 | `component::ouman_eh_800::entity::select::operation_mode::state::manual_valve_control` | Manual valve control | Manuell ventilstyrning | Core-literal match |
| 17637 | 860335675 | `component::ouman_eh_800::entity::select::operation_mode::state::big_temperature_drop` | Big temperature drop | Stort temperaturfall | Shared reference target checked |
| 17638 | 860335674 | `component::ouman_eh_800::entity::select::operation_mode::state::automatic` | Auto | Auto | Shared reference target checked |
| 17639 | 860335673 | `component::ouman_eh_800::entity::select::operation_mode::name` | Operation mode | Driftläge | Core-literal match |
| 17640 | 860335672 | `component::ouman_eh_800::entity::select::home_away_mode::state::off` | Off | Av | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 860524556 | `component::yoto::exceptions::oauth2_implementation_unavailable::message` | OAuth2 implementation unavailable, will retry |
| 860524549 | `component::yoto::config::abort::user_rejected_authorize` | Account linking rejected: {error} |
| 860524548 | `component::yoto::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. |
| 860524547 | `component::yoto::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. |
| 860524546 | `component::yoto::config::abort::oauth_failed` | Error while obtaining access token. |
| 860524545 | `component::yoto::config::abort::oauth_error` | Received invalid token data. |
| 860524544 | `component::yoto::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) |
| 860524543 | `component::yoto::config::abort::missing_credentials` | The integration requires application credentials. |
| 860524541 | `component::yoto::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
