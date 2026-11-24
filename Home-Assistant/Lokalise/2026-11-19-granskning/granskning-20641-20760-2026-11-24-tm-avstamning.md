# Home Assistant Core – historisk avstämning 20641–20760

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 64 direkta källtexter matchar HA Core-källan; 41 referensanvändningar med 30 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 15 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20641 | 831103677 | `component::duco::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 20642 | 831100906 | `component::knx::config_panel::expose::title` | Expose | Exponera | Core-literal match |
| 20643 | 831100905 | `component::knx::config_panel::expose::description` | Expose Home Assistant entity states to the KNX bus | Exponera tillstånd för entiteter i Home Assistant på KNX-bussen | Core-literal match |
| 20644 | 831100904 | `component::knx::config_panel::expose::create::value_template::label` | Value template | Värdemall | Core-literal match |
| 20645 | 831100903 | `component::knx::config_panel::expose::create::value_template::description` | Optionally transform the entity state or attribute value before sending it to KNX using a template. The template receives the entity state or attribute value as `value` variable. | Du kan använda en mall för att omvandla entitetens tillstånd eller attributvärde innan det skickas till KNX. Mallen tar emot tillståndet eller attributvärdet som variabeln `value`. | Core-literal match |
| 20646 | 831100902 | `component::knx::config_panel::expose::create::title` | Add exposure | Lägg till exponering | Core-literal match |
| 20647 | 831100901 | `component::knx::config_panel::expose::create::show_raw_values` | Show raw values | Visa råvärden | Core-literal match |
| 20648 | 831100900 | `component::knx::config_panel::expose::create::section_advanced_options::title` | Additional settings | Ytterligare inställningar | Core-literal match |
| 20649 | 831100899 | `component::knx::config_panel::expose::create::respond_to_read::label` | Respond to read | Svara på läsning | Shared reference target checked |
| 20650 | 831100898 | `component::knx::config_panel::expose::create::respond_to_read::description` | Respond to GroupValueRead telegrams received to the configured send address. | Svara på GroupValueRead-telegram som mottagits till den konfigurerade sändningsadressen. | Shared reference target checked |
| 20651 | 831100897 | `component::knx::config_panel::expose::create::periodic_send::label` | Periodic send interval | Intervall för regelbunden sändning | Core-literal match |
| 20652 | 831100896 | `component::knx::config_panel::expose::create::periodic_send::description` | Time interval to automatically resend the current value to the KNX bus, even if it hasn’t changed. | Tidsintervall för automatisk återutsändning av det aktuella värdet till KNX-bussen, även om det inte har ändrats. | Core-literal match |
| 20653 | 831100895 | `component::knx::config_panel::expose::create::ga::label` | Group address | Gruppadress | Shared reference target checked |
| 20654 | 831100894 | `component::knx::config_panel::expose::create::entity::label` | Entity | Entitet | Core-literal match |
| 20655 | 831100893 | `component::knx::config_panel::expose::create::entity::description` | Home Assistant entity to expose state changes to the KNX bus. | Home Assistant-entitet för att exponera tillståndsändringar på KNX-bussen. | Core-literal match |
| 20656 | 831100892 | `component::knx::config_panel::expose::create::default::label` | Default value | Standardvärde | Core-literal match |
| 20657 | 831100891 | `component::knx::config_panel::expose::create::default::description` | The value to send if the entity state is `unavailable` or `unknown`, or if the attribute is not set. If `default` is omitted, nothing is sent in these cases, but the last known value remains available for read requests. | Det värde som ska skickas om entitetens status är `unavailable` eller `unknown`, eller om attributet inte är angivet. Om `default` utelämnas skickas inget i dessa fall, men det senast kända värdet förblir tillgängligt för läsförfrågningar. | Core-literal match |
| 20658 | 831100890 | `component::knx::config_panel::expose::create::cooldown::label` | Cooldown | Minsta sändningsintervall | Core-literal match |
| 20659 | 831100889 | `component::knx::config_panel::expose::create::cooldown::description` | Minimum time between consecutive sends. This can be used to prevent high traffic on the KNX bus when values change very frequently. Only the most recent value during the cooldown period is sent. | Minsta tid mellan på varandra följande sändningar. Detta kan förhindra hög trafik på KNX-bussen när värden ändras mycket ofta. Endast det senaste värdet under väntetiden skickas. | Core-literal match |
| 20660 | 831100888 | `component::knx::config_panel::expose::create::attribute::description` | Expose changes of a specific attribute of the entity instead of the state. Optional. If the attribute is not set, the entity state is exposed. | Exponera ändringar av ett visst attribut hos entiteten i stället för dess tillstånd. Valfritt. Om attributet inte anges exponeras entitetens tillstånd. | Core-literal match |
| 20661 | 831100887 | `component::knx::config_panel::expose::create::add_expose` | Add expose | Lägg till exponering | Core-literal match |
| 20662 | 831100871 | `component::russound_rio::entity::select::party_mode::state::on` | On | På | Shared reference target checked |
| 20663 | 831100870 | `component::russound_rio::entity::select::party_mode::state::off` | Off | Av | Shared reference target checked |
| 20664 | 831100869 | `component::russound_rio::entity::select::party_mode::state::master` | Leader | Ledare | Core-literal match |
| 20665 | 831100868 | `component::russound_rio::entity::select::party_mode::name` | Party mode | Partyläge | Core-literal match |
| 20666 | 831100864 | `component::opendisplay::entity::event::button::state_attributes::event_type::state::button_up` | Button up | Knapp upp | Core-literal match |
| 20667 | 831100863 | `component::opendisplay::entity::event::button::state_attributes::event_type::state::button_down` | Button down | Knapp ned | Core-literal match |
| 20668 | 831100862 | `component::opendisplay::entity::event::button::name` | Button {number} | Knapp {number} | Core-literal match |
| 20669 | 831096190 | `component::picnic::selector::two_fa_channel::options::sms` | Text message (SMS) | Textmeddelande (SMS) | Core-literal match |
| 20670 | 831096189 | `component::picnic::selector::two_fa_channel::options::email` | Email | E-post | Core-literal match |
| 20671 | 831096188 | `component::picnic::config::step::2fa_channel::title` | Two-factor authentication | Tvåfaktorsautentisering | Core-literal match |
| 20672 | 831096187 | `component::picnic::config::step::2fa_channel::description` | A second factor is required to complete the login. Select the channel through which you want to receive your second factor. | En andra faktor krävs för att slutföra inloggningen. Välj den kanal genom vilken du vill ta emot din andra faktor. | Core-literal match |
| 20673 | 831096186 | `component::picnic::config::step::2fa_channel::data::two_fa_channel` | Channel | Kanal | Core-literal match |
| 20674 | 831096185 | `component::picnic::config::step::2fa::title` | Two-factor authentication | Tvåfaktorsautentisering | Core-literal match |
| 20675 | 831096184 | `component::picnic::config::step::2fa::description` | A verification code has been sent to you via your selected channel. | En verifieringskod har skickats till dig via din valda kanal. | Core-literal match |
| 20676 | 831096183 | `component::picnic::config::step::2fa::data::two_fa_code` | Verification code | Verifieringskod | Core-literal match |
| 20677 | 831096182 | `component::picnic::config::error::invalid_2fa_code` | The verification code is incorrect or has expired. | Verifieringskoden är felaktig eller har gått ut. | Core-literal match |
| 20678 | 831092511 | `component::victron_gx::entity::select::vebus_inverter_mode::state::on` | On | På | Shared reference target checked |
| 20679 | 831092510 | `component::victron_gx::entity::select::vebus_inverter_mode::state::off` | Off | Av | Shared reference target checked |
| 20680 | 831092509 | `component::victron_gx::entity::select::vebus_inverter_mode::state::inverter_only` | Inverter only | Endast växelriktare | Shared reference target checked |
| 20681 | 831092508 | `component::victron_gx::entity::select::vebus_inverter_mode::state::charger_only` | Charger only | Endast laddare | Shared reference target checked |
| 20682 | 831092507 | `component::victron_gx::entity::select::system_settings_dess_mode::state::sell` | Sell | Sälj | Core-literal match |
| 20683 | 831092506 | `component::victron_gx::entity::select::system_settings_dess_mode::state::off` | Off | Av | Shared reference target checked |
| 20684 | 831092505 | `component::victron_gx::entity::select::system_settings_dess_mode::state::node_red` | Node-RED | Node-RED | Core-literal match |
| 20685 | 831092504 | `component::victron_gx::entity::select::system_settings_dess_mode::state::buy` | Buy | Köp | Core-literal match |
| 20686 | 831092503 | `component::victron_gx::entity::select::system_settings_dess_mode::state::auto_vrm` | Auto / VRM | Auto / VRM | Core-literal match |
| 20687 | 831092502 | `component::victron_gx::entity::select::system_settings_dess_mode::name` | DESS mode | DESS-läge | Core-literal match |
| 20688 | 831092501 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::weekends` | Weekends | Helger | Core-literal match |
| 20689 | 831092500 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::weekdays` | Weekdays | Veckodagar | Core-literal match |
| 20690 | 831092499 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::wednesday` | Wednesday | Onsdag | Shared reference target checked |
| 20691 | 831092498 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::tuesday` | Tuesday | Tisdag | Shared reference target checked |
| 20692 | 831092497 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::thursday` | Thursday | Torsdag | Shared reference target checked |
| 20693 | 831092496 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::sunday` | Sunday | Söndag | Shared reference target checked |
| 20694 | 831092495 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::saturday` | Saturday | Lördag | Shared reference target checked |
| 20695 | 831092494 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::monday` | Monday | Måndag | Shared reference target checked |
| 20696 | 831092493 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::friday` | Friday | Fredag | Shared reference target checked |
| 20697 | 831092492 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::every_day` | Every day | Varje dag | Core-literal match |
| 20698 | 831092491 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_weekend` | Disabled (Weekends) | Inaktiverad (helger) | Core-literal match |
| 20699 | 831092490 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_weekdays` | Disabled (Weekdays) | Inaktiverad (veckodagar) | Core-literal match |
| 20700 | 831092489 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_wednesday` | Disabled (Wednesday) | Inaktiverad (onsdag) | Core-literal match |
| 20701 | 831092488 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_tuesday` | Disabled (Tuesday) | Inaktiverad (tisdag) | Core-literal match |
| 20702 | 831092487 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_thursday` | Disabled (Thursday) | Inaktiverad (torsdag) | Core-literal match |
| 20703 | 831092486 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_sunday` | Disabled (Sunday) | Inaktiverad (söndag) | Core-literal match |
| 20704 | 831092485 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_saturday` | Disabled (Saturday) | Inaktiverad (lördag) | Core-literal match |
| 20705 | 831092484 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_monday` | Disabled (Monday) | Inaktiverad (måndag) | Core-literal match |
| 20706 | 831092483 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_friday` | Disabled (Friday) | Inaktiverad (fredag) | Core-literal match |
| 20707 | 831092482 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::state::disabled_every_day` | Disabled (Every day) | Inaktiverad (varje dag) | Core-literal match |
| 20708 | 831092481 | `component::victron_gx::entity::select::system_ess_schedule_charge_slot_days::name` | ESS BatteryLife schedule charge {slot} days | ESS BatteryLife schemalagd laddning {slot} dagar | Core-literal match |
| 20709 | 831092480 | `component::victron_gx::entity::select::system_ess_mode::state::phase_compensation_enabled` | Optimized mode or 'keep batteries charged' and phase compensation enabled | Optimerat läge eller ”håll batterierna laddade” och faskompensering aktiverad | Core-literal match |
| 20710 | 831092479 | `component::victron_gx::entity::select::system_ess_mode::state::phase_compensation_disabled` | Optimized mode or 'keep batteries charged' and phase compensation disabled | Optimerat läge eller ”håll batterierna laddade” och faskompensering inaktiverad | Core-literal match |
| 20711 | 831092478 | `component::victron_gx::entity::select::system_ess_mode::state::external_control` | External control | Extern styrning | Shared reference target checked |
| 20712 | 831092477 | `component::victron_gx::entity::select::system_ess_mode::name` | ESS mode (Hub4) | ESS-läge (Hub4) | Core-literal match |
| 20713 | 831092476 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::with_battery_life` | Optimized mode with BatteryLife | Optimerat läge med BatteryLife | Source-path follow-up open |
| 20714 | 831092475 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::sustain` | Multi/Quattro is in sustain | Multi/Quattro är i sustain-läge | Source-path follow-up open |
| 20715 | 831092474 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::soc_below_soc_limit_24_hours` | SoC has been below SoC limit for more than 24 hours. Charging battery with 5 amps | SoC har legat under SoC-gränsen i mer än 24 timmar. Batteriet laddas med 5 ampere. | Source-path follow-up open |
| 20716 | 831092473 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::soc_below_battery_life_dynamic_soc_limit` | SoC below BatteryLife dynamic SoC limit | SoC ligger under BatteryLife:s dynamiska SoC-gräns | Source-path follow-up open |
| 20717 | 831092472 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_exceeds_85` | Self-consumption, SoC exceeds 85% | Egenförbrukning, SoC överstiger 85 % | Source-path follow-up open |
| 20718 | 831092471 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_below_min` | Self-consumption, SoC is below minimum SoC | Egenförbrukning, SoC under minsta SoC | Source-path follow-up open |
| 20719 | 831092470 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_at_100` | Self-consumption, SoC at 100% | Egenförbrukning, SoC på 100 % | Source-path follow-up open |
| 20720 | 831092469 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_above_min` | Self-consumption, SoC at or above minimum SoC | Egenförbrukning, SoC på eller över minsta SoC | Source-path follow-up open |
| 20721 | 831092468 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption` | Self-consumption | Egenförbrukning | Source-path follow-up open |
| 20722 | 831092467 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::recharge_no_battery_life` | Recharge, SoC dropped 5% or more below minimum SoC (No BatteryLife) | Laddning, SoC sjönk 5 % eller mer under minsta SoC (utan BetteryLife) | Source-path follow-up open |
| 20723 | 831092466 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::recharge` | Recharge, SoC dropped 5% or more below minimum SoC | Laddning, SoC sjönk 5 % eller mer under minsta SoC | Source-path follow-up open |
| 20724 | 831092465 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::keep_batteries_charged` | Keep batteries charged | Håll batterierna laddade | Core-literal match |
| 20725 | 831092464 | `component::victron_gx::entity::select::system_ess_batterylife_state::name` | ESS mode | ESS-läge | Shared reference target checked |
| 20726 | 831092463 | `component::victron_gx::entity::select::inverter_mode::state::off` | Off | Av | Shared reference target checked |
| 20727 | 831092462 | `component::victron_gx::entity::select::inverter_mode::state::inverter` | Inverter | Växelriktare | Core-literal match |
| 20728 | 831092461 | `component::victron_gx::entity::select::inverter_mode::state::eco` | Eco | Eco | Core-literal match |
| 20729 | 831092460 | `component::victron_gx::entity::select::evcharger_mode::state::scheduled_charge` | Scheduled charge | Schemalagd debitering | Core-literal match |
| 20730 | 831092459 | `component::victron_gx::entity::select::evcharger_mode::state::manual` | Manual | Manuell | Shared reference target checked |
| 20731 | 831092458 | `component::victron_gx::entity::select::evcharger_mode::state::auto` | Auto | Auto | Shared reference target checked |
| 20732 | 831092457 | `component::victron_gx::entity::select::evcharger_mode::name` | Mode | Läge | Shared reference target checked |
| 20733 | 831092456 | `component::victron_gx::entity::select::acsystem_mode::state::passthrough` | Passthrough | Genomströmning | Shared reference target checked |
| 20734 | 831092455 | `component::victron_gx::entity::select::acsystem_mode::state::on` | On | På | Shared reference target checked |
| 20735 | 831092454 | `component::victron_gx::entity::select::acsystem_mode::state::off` | Off | Av | Shared reference target checked |
| 20736 | 831092453 | `component::victron_gx::entity::select::acsystem_mode::state::inverter_only` | Inverter only | Endast växelriktare | Shared reference target checked |
| 20737 | 831092452 | `component::victron_gx::entity::select::acsystem_mode::state::charger_only` | Charger only | Endast laddare | Shared reference target checked |
| 20738 | 831091245 | `component::music_assistant::entity::text::network_name::name` | Network name | Nätverksnamn | Core-literal match |
| 20739 | 831090873 | `component::huum::config::step::reconfigure::data_description::username` | The username (email) used in the Huum mobile app. | Användarnamnet (e-postadressen) som används i Huum-mobilappen. | Shared reference target checked |
| 20740 | 831090872 | `component::huum::config::step::reconfigure::data_description::password` | The password used in the Huum mobile app. | Lösenordet som används i Huum-mobilappen. | Shared reference target checked |
| 20741 | 831090871 | `component::huum::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 20742 | 831090870 | `component::huum::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 20743 | 831090869 | `component::huum::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 20744 | 831003720 | `component::lunatone::config::step::discovery_confirm::description` | Do you want to set up the Lunatone device at {url}? | Vill du konfigurera Lunatone-enheten på {url}? | Core-literal match |
| 20745 | 831003719 | `component::lunatone::config::error::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 20746 | 831003718 | `component::lunatone::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 20747 | 831003693 | `component::autoskope::config::step::reauth_confirm::description` | Please re-enter your password for your Autoskope account. | Ange lösenordet för ditt Autoskope-konto igen. | Core-literal match |
| 20748 | 831003692 | `component::autoskope::config::step::reauth_confirm::data_description::password` | The new password for your Autoskope account. | Det nya lösenordet för ditt Autoskope-konto. | Core-literal match |
| 20749 | 831003691 | `component::autoskope::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 20750 | 831003690 | `component::autoskope::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 20751 | 830157616 | `component::event::entity_component::doorbell::state_attributes::event_type::state::ring` | Ring | Signal | Core-literal match |
| 20752 | 829937045 | `component::smlight::entity::infrared::infrared_emitter::name` | IR emitter | IR-sändare | Source-path follow-up open |
| 20753 | 829933107 | `component::unifi_access::config::error::protect_api_key` | This API key is associated with UniFi Protect, not UniFi Access. Please generate a new API key from the UniFi Access application settings. | Denna API-nyckel är kopplad till UniFi Protect, inte UniFi Access. Generera en ny API-nyckel från UniFi Access-appens inställningar. | Core-literal match |
| 20754 | 829920985 | `component::victron_gx::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 20755 | 829920984 | `component::victron_gx::config::step::reauth_confirm::description` | Please re-authenticate with {host}. | Autentisera dig på nytt med {host}. | Core-literal match |
| 20756 | 829920983 | `component::victron_gx::config::step::reauth_confirm::data_description::username` | Username for the MQTT server, default is empty. Not needed by Victron devices. This is only needed if you route your MQTT messages through a non-Victron server and it does require a username. | Användarnamn för MQTT-servern, standardvärdet är tomt. Behövs inte för Victron-enheter. Detta behövs bara om du dirigerar dina MQTT-meddelanden via en server som inte är från Victron och som kräver ett användarnamn. | Shared reference target checked |
| 20757 | 829920982 | `component::victron_gx::config::step::reauth_confirm::data_description::ssl` | Indicates whether to use SSL to connect to the Victron device. Normally it is disabled. | Anger om SSL ska användas för att ansluta till Victron-enheten. Normalt är det inaktiverat. | Shared reference target checked |
| 20758 | 829920981 | `component::victron_gx::config::step::reauth_confirm::data_description::password` | Password for the Victron device, default is empty. This is not your VRM password. | Lösenord för Victron-enheten, standardinställningen är tom. Detta är inte ditt VRM-lösenord. | Shared reference target checked |
| 20759 | 829920980 | `component::victron_gx::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 20760 | 829920979 | `component::victron_gx::config::step::reauth_confirm::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 831092476 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::with_battery_life` | Optimized mode with BatteryLife |
| 831092475 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::sustain` | Multi/Quattro is in sustain |
| 831092474 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::soc_below_soc_limit_24_hours` | SoC has been below SoC limit for more than 24 hours. Charging battery with 5 amps |
| 831092473 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::soc_below_battery_life_dynamic_soc_limit` | SoC below BatteryLife dynamic SoC limit |
| 831092472 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_exceeds_85` | Self-consumption, SoC exceeds 85% |
| 831092471 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_below_min` | Self-consumption, SoC is below minimum SoC |
| 831092470 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_at_100` | Self-consumption, SoC at 100% |
| 831092469 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption_soc_above_min` | Self-consumption, SoC at or above minimum SoC |
| 831092468 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::self_consumption` | Self-consumption |
| 831092467 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::recharge_no_battery_life` | Recharge, SoC dropped 5% or more below minimum SoC (No BatteryLife) |
| 831092466 | `component::victron_gx::entity::select::system_ess_batterylife_state::state::recharge` | Recharge, SoC dropped 5% or more below minimum SoC |
| 831090869 | `component::huum::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 831003718 | `component::lunatone::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 831003690 | `component::autoskope::config::abort::reauth_successful` | Re-authentication was successful |
| 829937045 | `component::smlight::entity::infrared::infrared_emitter::name` | IR emitter |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
