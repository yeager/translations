# Home Assistant Core – historisk avstämning 13561–13680

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 70 direkta källtexter matchar HA Core-källan; 46 referensanvändningar med 45 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 4 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13561 | 908724249 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_clean_brewing_unit_manually` | Clean brewing unit manually | Rengör bryggenheten manuellt | Shared reference target checked |
| 13562 | 908724248 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_clean` | Clean | Rengör | Shared reference target checked |
| 13563 | 908724247 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_calc_n_clean` | Calc'N'Clean | Calc'N'Clean | Shared reference target checked |
| 13564 | 908724246 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_auto_descale` | Auto descale | Automatisk avkalkning | Shared reference target checked |
| 13565 | 908724245 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_auto_clean` | Auto clean | Automatisk rengöring | Shared reference target checked |
| 13566 | 908724244 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_appliance_on_rinsing` | Appliance on rinsing | Sköljning vid påslagning | Shared reference target checked |
| 13567 | 908724243 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_cleaning_modes_appliance_off_rinsing` | Appliance off rinsing | Sköljning vid avstängning | Shared reference target checked |
| 13568 | 908724242 | `component::home_connect::entity::select::active_program::state::consumer_products_coffee_maker_program_beverage_coffee_pot` | Coffee pot | Kaffekanna | Shared reference target checked |
| 13569 | 908101697 | `component::blebox::entity::button::second_output::name` | Second output | Andra utgången | Core-literal match |
| 13570 | 908012255 | `component::subaru::entity::binary_sensor::window_sunroof::name` | Sunroof | Soltak | Core-literal match |
| 13571 | 908012254 | `component::subaru::entity::binary_sensor::window_rear_right::name` | Window rear right | Fönster bak höger | Core-literal match |
| 13572 | 908012253 | `component::subaru::entity::binary_sensor::window_rear_left::name` | Window rear left | Fönster bak vänster | Core-literal match |
| 13573 | 908012252 | `component::subaru::entity::binary_sensor::window_front_right::name` | Window front right | Fönster fram höger | Core-literal match |
| 13574 | 908012251 | `component::subaru::entity::binary_sensor::window_front_left::name` | Window front left | Fönster fram vänster | Core-literal match |
| 13575 | 908012250 | `component::subaru::entity::binary_sensor::mil_wash::name` | Washer fluid warning | Varning för spolarvätska | Core-literal match |
| 13576 | 908012249 | `component::subaru::entity::binary_sensor::mil_vdc::name` | Vehicle dynamics control warning | Varning för stabilitetskontroll | Core-literal match |
| 13577 | 908012248 | `component::subaru::entity::binary_sensor::mil_tpms::name` | Tire pressure warning | Däcktrycksvarning | Core-literal match |
| 13578 | 908012247 | `component::subaru::entity::binary_sensor::mil_tel::name` | Telematics warning | Telematikvarning | Core-literal match |
| 13579 | 908012246 | `component::subaru::entity::binary_sensor::mil_srs::name` | Airbag warning | Krockkuddevarning | Core-literal match |
| 13580 | 908012245 | `component::subaru::entity::binary_sensor::mil_srh::name` | Steering responsive headlights warning | Varning för strålkastare som justeras efter styrningen | Core-literal match |
| 13581 | 908012244 | `component::subaru::entity::binary_sensor::mil_rab::name` | Reverse automatic braking warning | Varning för automatisk backbromsning | Core-literal match |
| 13582 | 908012243 | `component::subaru::entity::binary_sensor::mil_opl::name` | Oil pressure warning | Varning för oljetryck | Core-literal match |
| 13583 | 908012242 | `component::subaru::entity::binary_sensor::mil_iss::name` | Idle stop & start warning | Varning för start-stopp-systemet | Core-literal match |
| 13584 | 908012241 | `component::subaru::entity::binary_sensor::mil_ess::name` | EyeSight warning | Varning för EyeSight | Core-literal match |
| 13585 | 908012240 | `component::subaru::entity::binary_sensor::mil_epb::name` | Electric parking brake warning | Varning för elektrisk parkeringsbroms | Core-literal match |
| 13586 | 908012239 | `component::subaru::entity::binary_sensor::mil_epas::name` | Electric power steering warning | Varning för elektrisk servostyrning | Core-literal match |
| 13587 | 908012238 | `component::subaru::entity::binary_sensor::mil_eol::name` | Engine oil level warning | Varning för motoroljenivå | Core-literal match |
| 13588 | 908012237 | `component::subaru::entity::binary_sensor::mil_ebd::name` | Electronic brake force distribution warning | Varning för elektronisk bromskraftfördelning | Core-literal match |
| 13589 | 908012236 | `component::subaru::entity::binary_sensor::mil_cel::name` | Check engine | Kontrollera motorn | Core-literal match |
| 13590 | 908012235 | `component::subaru::entity::binary_sensor::mil_bsdrct::name` | Blind spot and rear cross traffic warning | Varning för död vinkel och korsande trafik bakifrån | Core-literal match |
| 13591 | 908012234 | `component::subaru::entity::binary_sensor::mil_awd::name` | AWD warning | AWD-varning | Core-literal match |
| 13592 | 908012233 | `component::subaru::entity::binary_sensor::mil_atf::name` | Transmission temperature warning | Varning för transmissionstemperatur | Core-literal match |
| 13593 | 908012232 | `component::subaru::entity::binary_sensor::mil_abs::name` | ABS warning | ABS-varning | Core-literal match |
| 13594 | 908012231 | `component::subaru::entity::binary_sensor::lock_status_rear_right::name` | Lock status rear right | Låsstatus bak höger | Core-literal match |
| 13595 | 908012230 | `component::subaru::entity::binary_sensor::lock_status_rear_left::name` | Lock status rear left | Låsstatus bak vänster | Core-literal match |
| 13596 | 908012229 | `component::subaru::entity::binary_sensor::lock_status_front_right::name` | Lock status front right | Låsstatus fram höger | Core-literal match |
| 13597 | 908012228 | `component::subaru::entity::binary_sensor::lock_status_front_left::name` | Lock status front left | Låsstatus fram vänster | Core-literal match |
| 13598 | 908012227 | `component::subaru::entity::binary_sensor::lock_status_boot::name` | Lock status tailgate | Låsstatus baklucka | Core-literal match |
| 13599 | 908012226 | `component::subaru::entity::binary_sensor::is_charging::name` | Charging | Laddning | Source-path follow-up open |
| 13600 | 908012225 | `component::subaru::entity::binary_sensor::health_istrouble::name` | Vehicle health | Fordonshälsa | Core-literal match |
| 13601 | 908012224 | `component::subaru::entity::binary_sensor::ev_is_plugged_in::name` | EV plug | Laddkontakt | Core-literal match |
| 13602 | 908012223 | `component::subaru::entity::binary_sensor::door_rear_right::name` | Door rear right | Dörr bak höger | Core-literal match |
| 13603 | 908012222 | `component::subaru::entity::binary_sensor::door_rear_left::name` | Door rear left | Dörr bak vänster | Core-literal match |
| 13604 | 908012221 | `component::subaru::entity::binary_sensor::door_front_right::name` | Door front right | Dörr fram höger | Core-literal match |
| 13605 | 908012220 | `component::subaru::entity::binary_sensor::door_front_left::name` | Door front left | Dörr fram vänster | Core-literal match |
| 13606 | 908012219 | `component::subaru::entity::binary_sensor::door_engine_hood::name` | Hood | Motorhuv | Core-literal match |
| 13607 | 908012218 | `component::subaru::entity::binary_sensor::door_boot::name` | Tailgate | Baklucka | Core-literal match |
| 13608 | 907439141 | `component::coolmaster::config::step::user::data_description::swing_support` | Expose a swing mode control. This adds one request per unit on every update, so polling is slower. | Exponera ett reglage för svängläge. Detta medför en extra begäran per enhet vid varje uppdatering, så pollningen går långsammare. | Core-literal match |
| 13609 | 907439140 | `component::coolmaster::config::step::user::data_description::off` | Allow the units to be turned off from Home Assistant. | Tillåt att enheterna stängs av från Home Assistant. | Core-literal match |
| 13610 | 907439139 | `component::coolmaster::config::step::user::data_description::heat_cool` | Enable if your units can switch between heating and cooling automatically. | Aktivera om dina enheter kan växla mellan uppvärmning och kylning automatiskt. | Core-literal match |
| 13611 | 907439138 | `component::coolmaster::config::step::user::data_description::heat` | Enable if your units can heat. | Aktivera om dina enheter kan värma. | Core-literal match |
| 13612 | 907439137 | `component::coolmaster::config::step::user::data_description::fan_only` | Enable if your units can run the fan without heating or cooling. | Aktivera om dina enheter kan köra fläkten utan uppvärmning eller kylning. | Core-literal match |
| 13613 | 907439136 | `component::coolmaster::config::step::user::data_description::dry` | Enable if your units have a dry (dehumidify) mode. | Aktivera om dina enheter har ett avfuktningsläge. | Core-literal match |
| 13614 | 907439135 | `component::coolmaster::config::step::user::data_description::cool` | Enable if your units can cool. | Aktivera om dina enheter kan kyla. | Core-literal match |
| 13615 | 907439134 | `component::coolmaster::config::step::reconfigure::sections::more_options::name` | More options | Fler alternativ | Shared reference target checked |
| 13616 | 907439133 | `component::coolmaster::config::step::reconfigure::sections::more_options::data_description::send_wakeup_prompt` | Send the coolmaster unit an empty command before issuing any actual command. This is required for serial models. | Skicka ett tomt kommando till CoolMaster-enheten innan du ger något egentligt kommando. Detta krävs för seriemodeller. | Shared reference target checked |
| 13617 | 907439132 | `component::coolmaster::config::step::reconfigure::sections::more_options::data::send_wakeup_prompt` | Send wakeup prompt | Skicka väckningsmeddelande | Shared reference target checked |
| 13618 | 907439131 | `component::coolmaster::config::step::reconfigure::description` | Update your CoolMasterNet connection details and supported modes. | Uppdatera dina CoolMasterNet-anslutningsuppgifter och vilka lägen som stöds. | Core-literal match |
| 13619 | 907439130 | `component::coolmaster::config::step::reconfigure::data_description::swing_support` | Expose a swing mode control. This adds one request per unit on every update, so polling is slower. | Exponera ett reglage för svängläge. Detta medför en extra begäran per enhet vid varje uppdatering, så pollningen går långsammare. | Shared reference target checked |
| 13620 | 907439129 | `component::coolmaster::config::step::reconfigure::data_description::off` | Allow the units to be turned off from Home Assistant. | Tillåt att enheterna stängs av från Home Assistant. | Shared reference target checked |
| 13621 | 907439128 | `component::coolmaster::config::step::reconfigure::data_description::host` | The hostname or IP address of your CoolMasterNet device. | Värdnamnet eller IP-adressen för din CoolMasterNet-enhet. | Shared reference target checked |
| 13622 | 907439127 | `component::coolmaster::config::step::reconfigure::data_description::heat_cool` | Enable if your units can switch between heating and cooling automatically. | Aktivera om dina enheter kan växla mellan uppvärmning och kylning automatiskt. | Shared reference target checked |
| 13623 | 907439126 | `component::coolmaster::config::step::reconfigure::data_description::heat` | Enable if your units can heat. | Aktivera om dina enheter kan värma. | Shared reference target checked |
| 13624 | 907439125 | `component::coolmaster::config::step::reconfigure::data_description::fan_only` | Enable if your units can run the fan without heating or cooling. | Aktivera om dina enheter kan köra fläkten utan uppvärmning eller kylning. | Shared reference target checked |
| 13625 | 907439124 | `component::coolmaster::config::step::reconfigure::data_description::dry` | Enable if your units have a dry (dehumidify) mode. | Aktivera om dina enheter har ett avfuktningsläge. | Shared reference target checked |
| 13626 | 907439123 | `component::coolmaster::config::step::reconfigure::data_description::cool` | Enable if your units can cool. | Aktivera om dina enheter kan kyla. | Shared reference target checked |
| 13627 | 907439122 | `component::coolmaster::config::step::reconfigure::data::swing_support` | Control swing mode | Styr svängläge | Shared reference target checked |
| 13628 | 907439121 | `component::coolmaster::config::step::reconfigure::data::off` | Can be turned off | Kan stängas av | Shared reference target checked |
| 13629 | 907439120 | `component::coolmaster::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 13630 | 907439119 | `component::coolmaster::config::step::reconfigure::data::heat_cool` | Support automatic heat/cool mode | Stöd för automatiskt värme-/kylläge | Shared reference target checked |
| 13631 | 907439118 | `component::coolmaster::config::step::reconfigure::data::heat` | Support heat mode | Stöd för värmeläge | Shared reference target checked |
| 13632 | 907439117 | `component::coolmaster::config::step::reconfigure::data::fan_only` | Support fan only mode | Stöd för enbart fläktläge | Shared reference target checked |
| 13633 | 907439116 | `component::coolmaster::config::step::reconfigure::data::dry` | Support dry mode | Stöd för avfuktningsläge | Shared reference target checked |
| 13634 | 907439115 | `component::coolmaster::config::step::reconfigure::data::cool` | Support cool mode | Stöd för kylläge | Shared reference target checked |
| 13635 | 907439114 | `component::coolmaster::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 13636 | 907250032 | `component::ouman_eh_800::config::step::reauth_confirm::description` | Re-enter the credentials for the Ouman EH-800 web interface. | Ange inloggningsuppgifterna för webbgränssnittet på Ouman EH-800 på nytt. | Core-literal match |
| 13637 | 907250031 | `component::ouman_eh_800::config::step::reauth_confirm::data_description::username` | Username for the Ouman EH-800 web interface | Användarnamn för Ouman EH-800:s webbgränssnitt | Shared reference target checked |
| 13638 | 907250030 | `component::ouman_eh_800::config::step::reauth_confirm::data_description::password` | Password for the Ouman EH-800 web interface | Lösenord för Ouman EH-800 webbgränssnitt | Shared reference target checked |
| 13639 | 907250029 | `component::ouman_eh_800::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 13640 | 907250028 | `component::ouman_eh_800::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 13641 | 907250027 | `component::ouman_eh_800::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 13642 | 907142829 | `component::teslemetry::entity::cover::tonneau::name` | Tonneau | Flakskydd | Core-literal match |
| 13643 | 907084012 | `component::schlage::config::step::user::data_description::username` | The email address of your Schlage account. | E-postadressen för ditt Schlage-konto. | Shared reference target checked |
| 13644 | 907084011 | `component::schlage::config::step::user::data_description::password` | The password of your Schlage account. | Lösenordet till ditt Schlage-konto. | Shared reference target checked |
| 13645 | 907084010 | `component::schlage::config::step::reauth_confirm::data_description::password` | The password of your Schlage account. | Lösenordet till ditt Schlage-konto. | Shared reference target checked |
| 13646 | 907084009 | `component::schlage::common::data_description_username` | The email address of your Schlage account. | E-postadressen för ditt Schlage-konto. | Core-literal match |
| 13647 | 907084008 | `component::schlage::common::data_description_password` | The password of your Schlage account. | Lösenordet till ditt Schlage-konto. | Core-literal match |
| 13648 | 906883170 | `component::vizio::exceptions::invalid_source::message` | Source "{source}" is not valid. Valid sources are listed in the source_list attribute. | Källan ”{source}” är ogiltig. Giltiga källor anges i attributet source_list. | Core-literal match |
| 13649 | 906883169 | `component::vizio::exceptions::invalid_sound_mode::message` | Sound mode "{sound_mode}" is not valid. Valid sound modes are listed in the sound_mode_list attribute. | Ljudläget ”{sound_mode}” är ogiltigt. Giltiga ljudlägen anges i attributet sound_mode_list. | Core-literal match |
| 13650 | 906664858 | `component::govee_ble::entity::sensor::temperature_probe::name` | Temperature probe {probe_id} | Temperaturgivare {probe_id} | Core-literal match |
| 13651 | 906664857 | `component::govee_ble::entity::sensor::temperature_alarm_probe::name` | Temperature alarm probe {probe_id} | Temperaturlarm för givare {probe_id} | Core-literal match |
| 13652 | 906664856 | `component::govee_ble::entity::sensor::low_temperature_alarm_probe::name` | Low temperature alarm probe {probe_id} | Larm för låg temperatur på givare {probe_id} | Core-literal match |
| 13653 | 906664855 | `component::govee_ble::entity::sensor::humidity_probe::name` | Humidity probe {probe_id} | Fuktighetsgivare {probe_id} | Core-literal match |
| 13654 | 906644727 | `component::reolink::entity::select::anti_flicker::state::other` | Other | Övrigt | Core-literal match |
| 13655 | 906644726 | `component::reolink::entity::select::anti_flicker::state::off` | Off | Av | Shared reference target checked |
| 13656 | 906644725 | `component::reolink::entity::select::anti_flicker::state::f60` | 60 Hz | 60 Hz | Core-literal match |
| 13657 | 906644724 | `component::reolink::entity::select::anti_flicker::state::f50` | 50 Hz | 50 Hz | Core-literal match |
| 13658 | 906644723 | `component::reolink::entity::select::anti_flicker::name` | Anti-flicker | Flimmerreducering | Core-literal match |
| 13659 | 906644722 | `component::reolink::entity::button::sync_time::name` | Synchronize time | Synkronisera tid | Core-literal match |
| 13660 | 906518079 | `component::hortimax::exceptions::no_devices::message` | The HortOS API reported no controllers for this API key | HortOS-API:et rapporterade inga styrenheter för den här API-nyckeln | Source-path follow-up open |
| 13661 | 906518078 | `component::hortimax::exceptions::invalid_auth::message` | The HortOS API rejected the API key | HortOS-API:et avvisade API-nyckeln | Core-literal match |
| 13662 | 906518077 | `component::hortimax::exceptions::cannot_connect::message` | Error talking to the HortOS API: {error} | Fel vid kommunikation med HortOS-API:et: {error} | Core-literal match |
| 13663 | 906518076 | `component::hortimax::config::step::user::title` | Connect to Ridder HortOS | Anslut till Ridder HortOS | Core-literal match |
| 13664 | 906518075 | `component::hortimax::config::step::user::description` | Enter the API key for the Ridder HortOS Automation API. You can request one from your Ridder account manager. | Ange API-nyckeln för Ridder HortOS Automation API. Du kan begära en från din Ridder-kontoansvariga. | Core-literal match |
| 13665 | 906518074 | `component::hortimax::config::step::user::data_description::api_key` | The API key that gives access to the controllers of your organization. | API-nyckel som ger åtkomst till styrenheterna i din organisation. | Core-literal match |
| 13666 | 906518073 | `component::hortimax::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 13667 | 906518072 | `component::hortimax::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 13668 | 906518071 | `component::hortimax::config::error::no_devices` | Authentication succeeded, but no controllers are available for this API key | Autentiseringen lyckades, men inga styrenheter är tillgängliga för denna API-nyckel | Core-literal match |
| 13669 | 906518070 | `component::hortimax::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 13670 | 906518069 | `component::hortimax::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 13671 | 906518068 | `component::hortimax::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 13672 | 906158216 | `component::alexa_devices::config::progress::login` | Logging in and scanning for Alexa devices. This can take several minutes if you have many devices linked to your Amazon account. | Loggar in och söker efter Alexa-enheter. Detta kan ta flera minuter om du har många enheter länkade till ditt Amazon-konto. | Core-literal match |
| 13673 | 906108246 | `component::bthome::entity::event::dimmer_numbered::state_attributes::event_type::state::rotate_right` | Rotate right | Rotera höger | Shared reference target checked |
| 13674 | 906108245 | `component::bthome::entity::event::dimmer_numbered::state_attributes::event_type::state::rotate_left` | Rotate left | Rotera vänster | Shared reference target checked |
| 13675 | 906108244 | `component::bthome::entity::event::dimmer_numbered::name` | Dimmer {number} | Dimmer {number} | Core-literal match |
| 13676 | 906108243 | `component::bthome::entity::event::dimmer::name` | Dimmer | Dimmer | Core-literal match |
| 13677 | 906108242 | `component::bthome::entity::event::command_numbered::state_attributes::event_type::state::toggle` | Toggle | Växla | Shared reference target checked |
| 13678 | 906108241 | `component::bthome::entity::event::command_numbered::state_attributes::event_type::state::step_up` | Step up | Steg upp | Shared reference target checked |
| 13679 | 906108240 | `component::bthome::entity::event::command_numbered::state_attributes::event_type::state::step_down` | Step down | Steg ner | Shared reference target checked |
| 13680 | 906108239 | `component::bthome::entity::event::command_numbered::state_attributes::event_type::state::on` | On | På | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 908012226 | `component::subaru::entity::binary_sensor::is_charging::name` | Charging |
| 907439114 | `component::coolmaster::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 907250027 | `component::ouman_eh_800::config::abort::reauth_successful` | Re-authentication was successful |
| 906518079 | `component::hortimax::exceptions::no_devices::message` | The HortOS API reported no controllers for this API key |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
