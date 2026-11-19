# Home Assistant Core – granskning 1981–2220

Sortering: ”Last added” vid insamlingen. Inget har ändrats i Lokalise. Referenser vars mål inte finns i underlaget markeras för senare kontroll.

## 1981. `component::system_bridge::services::send_message::fields::title::name`

**Engelska:** Title

**Befintlig svenska:** Rubrik

**Bedömning:** Ingen ändring föreslås.

## 1982. `component::system_bridge::services::send_message::fields::title::description`

**Engelska:** Title of the notification.

**Befintlig svenska:** Rubriken för aviseringen.

**Bedömning:** Ingen ändring föreslås.

## 1983. `component::system_bridge::services::send_message::fields::sound::name`

**Engelska:** Sound

**Befintlig svenska:** Ljud

**Bedömning:** Ingen ändring föreslås.

## 1984. `component::system_bridge::services::send_message::fields::sound::description`

**Engelska:** Path to a sound file on the computer to play with the notification. Linux only.

**Befintlig svenska:** Sökväg till en ljudfil på datorn som spelas upp med aviseringen. Endast Linux.

**Bedömning:** Ingen ändring föreslås.

## 1985. `component::system_bridge::services::send_message::fields::path::name`

**Engelska:** [%key:common::config_flow::data::path%]

**Befintlig svenska:** Sökväg

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::path`; det ingår ännu inte i det insamlade underlaget.

## 1986. `component::system_bridge::services::send_message::fields::path::description`

**Engelska:** File or folder on the computer to open when the notification is clicked. Can't be used with URL.

**Befintlig svenska:** Fil eller mapp på datorn som öppnas när aviseringen klickas. Kan inte användas tillsammans med URL.

**Förslag:** Fil eller mapp på datorn som öppnas när du klickar på aviseringen. Kan inte användas tillsammans med URL.

## 1987. `component::system_bridge::services::send_message::fields::message::name`

**Engelska:** Message

**Befintlig svenska:** Meddelande

**Bedömning:** Ingen ändring föreslås.

## 1988. `component::system_bridge::services::send_message::fields::message::description`

**Engelska:** The message body of the notification.

**Befintlig svenska:** Själva meddelandet i aviseringen.

**Bedömning:** Ingen ändring föreslås.

## 1989. `component::system_bridge::services::send_message::fields::icon::name`

**Engelska:** Icon

**Befintlig svenska:** Ikon

**Bedömning:** Ingen ändring föreslås.

## 1990. `component::system_bridge::services::send_message::fields::icon::description`

**Engelska:** Icon to show with the notification: an image path on the computer, or on Linux an icon name from the icon theme. Standard icon names: {icon_naming_url}.

**Befintlig svenska:** Ikon som visas med aviseringen: en sökväg till en bild på datorn eller, i Linux, ett ikonnamn från ikontemat. Standardnamn på ikoner: {icon_naming_url}.

**Bedömning:** Ingen ändring föreslås.

## 1991. `component::system_bridge::services::send_message::fields::duration::name`

**Engelska:** Duration

**Befintlig svenska:** Varaktighet

**Bedömning:** Ingen ändring föreslås.

## 1992. `component::system_bridge::services::send_message::fields::duration::description`

**Engelska:** How long the notification shows for.

**Befintlig svenska:** Hur länge aviseringen visas.

**Bedömning:** Ingen ändring föreslås.

## 1993. `component::system_bridge::services::send_message::fields::buttons::name`

**Engelska:** Buttons

**Befintlig svenska:** Knappar

**Bedömning:** Ingen ändring föreslås.

## 1994. `component::system_bridge::services::send_message::fields::buttons::description`

**Engelska:** Up to 3 buttons to show on the notification. Pressing one reports its ID. Linux and Windows only.

**Befintlig svenska:** Upp till 3 knappar som visas i aviseringen. När en knapp trycks ned rapporteras dess ID. Endast Linux och Windows.

**Bedömning:** Ingen ändring föreslås.

## 1995. `component::system_bridge::services::send_message::description`

**Engelska:** Sends a notification to the computer, with options the standard notify action doesn't have. Only administrators can use it.

**Befintlig svenska:** Skickar en avisering till datorn med alternativ som den vanliga aviseringsåtgärden saknar. Endast administratörer kan använda den.

**Bedömning:** Ingen ändring föreslås.

## 1996. `component::system_bridge::selector::urgency::options::normal`

**Engelska:** Normal

**Befintlig svenska:** Normal

**Bedömning:** Ingen ändring föreslås.

## 1997. `component::system_bridge::selector::urgency::options::low`

**Engelska:** Low

**Befintlig svenska:** Låg

**Bedömning:** Ingen ändring föreslås.

## 1998. `component::system_bridge::selector::urgency::options::critical`

**Engelska:** Critical

**Befintlig svenska:** Kritisk

**Bedömning:** Ingen ändring föreslås.

## 1999. `component::system_bridge::selector::icon::options::dialog-warning`

**Engelska:** Warning

**Befintlig svenska:** Varning

**Bedömning:** Ingen ändring föreslås.

## 2000. `component::system_bridge::selector::icon::options::dialog-question`

**Engelska:** Question

**Befintlig svenska:** Fråga

**Bedömning:** Ingen ändring föreslås.

## 2001. `component::system_bridge::selector::icon::options::dialog-information`

**Engelska:** Information

**Befintlig svenska:** Information

**Bedömning:** Ingen ändring föreslås.

## 2002. `component::system_bridge::selector::icon::options::dialog-error`

**Engelska:** Error

**Befintlig svenska:** Fel

**Bedömning:** Ingen ändring föreslås.

## 2003. `component::system_bridge::selector::buttons::fields::label::name`

**Engelska:** Label

**Befintlig svenska:** Etikett

**Bedömning:** Ingen ändring föreslås.

## 2004. `component::system_bridge::selector::buttons::fields::label::description`

**Engelska:** Text shown on the button.

**Befintlig svenska:** Text som visas på knappen.

**Bedömning:** Ingen ändring föreslås.

## 2005. `component::system_bridge::selector::buttons::fields::id::name`

**Engelska:** ID

**Befintlig svenska:** ID

**Bedömning:** Ingen ändring föreslås.

## 2006. `component::system_bridge::selector::buttons::fields::id::description`

**Engelska:** Reported when the button is pressed. Can't be "default", which is reported when the notification itself is clicked.

**Befintlig svenska:** Rapporteras när knappen trycks ned. Får inte vara "default", som rapporteras när själva aviseringen klickas.

**Förslag:** Rapporteras när knappen trycks ned. Får inte vara ”default”, som rapporteras när du klickar på själva aviseringen.

## 2007. `component::system_bridge::issues::deprecated_notify_action::title`

**Engelska:** Detected use of deprecated action {action}

**Befintlig svenska:** Föråldrad åtgärd {action} används

**Bedömning:** Ingen ändring föreslås.

## 2008. `component::system_bridge::issues::deprecated_notify_action::description`

**Engelska:** The action `{action}` is deprecated and will be removed in a future release.

Update your automations and scripts to use the notify entity with the `{new_action_1}` or `{new_action_2}` action instead.

## Example automation using `{new_action_1}` action:

{example_yaml_1}

## Example automation using `{new_action_2}` action:

{example_yaml_2}

**Befintlig svenska:** Åtgärden `{action}` är föråldrad och tas bort i en framtida version.

Uppdatera dina automatiseringar och skript så att de använder aviseringsentiteten med åtgärden `{new_action_1}` eller `{new_action_2}` i stället.

## Exempel på automatisering som använder åtgärden `{new_action_1}`:

{example_yaml_1}

## Exempel på automatisering som använder åtgärden `{new_action_2}`:

{example_yaml_2}

**Bedömning:** Ingen ändring föreslås.

## 2009. `component::touchline::exceptions::error_set_temperature::message`

**Engelska:** An error occurred while setting the temperature.

**Befintlig svenska:** Ett fel inträffade när temperaturen angavs.

**Bedömning:** Ingen ändring föreslås.

## 2010. `component::touchline::exceptions::error_set_preset::message`

**Engelska:** An error occurred while setting the preset mode.

**Befintlig svenska:** Ett fel inträffade när förinställt läge angavs.

**Bedömning:** Ingen ändring föreslås.

## 2011. `component::google_health::entity::sensor::sleep_start_time::name`

**Engelska:** Sleep start time

**Befintlig svenska:** Sömnens starttid

**Bedömning:** Ingen ändring föreslås.

## 2012. `component::google_health::entity::sensor::sleep_rem::name`

**Engelska:** REM sleep

**Befintlig svenska:** REM-sömn

**Bedömning:** Ingen ändring föreslås.

## 2013. `component::google_health::entity::sensor::sleep_light::name`

**Engelska:** Light sleep

**Befintlig svenska:** Lätt sömn

**Bedömning:** Ingen ändring föreslås.

## 2014. `component::google_health::entity::sensor::sleep_end_time::name`

**Engelska:** Sleep end time

**Befintlig svenska:** Sömnens sluttid

**Bedömning:** Ingen ändring föreslås.

## 2015. `component::google_health::entity::sensor::sleep_deep::name`

**Engelska:** Deep sleep

**Befintlig svenska:** Djupsömn

**Bedömning:** Ingen ändring föreslås.

## 2016. `component::bosch_shc::entity::light::motion_light::name`

**Engelska:** Orientation light

**Befintlig svenska:** Orienteringsbelysning

**Bedömning:** Ingen ändring föreslås.

## 2017. `component::bosch_shc::entity::binary_sensor::ventilation_mode::name`

**Engelska:** Sustainable ventilation

**Befintlig svenska:** Energisnål ventilation

**Bedömning:** Ingen ändring föreslås.

## 2018. `component::bosch_shc::entity::binary_sensor::summer_mode::name`

**Engelska:** Heating break

**Befintlig svenska:** Värmeuppehåll

**Bedömning:** Ingen ändring föreslås.

## 2019. `component::bosch_shc::entity::binary_sensor::schedule_override_active::name`

**Engelska:** Schedule override active

**Befintlig svenska:** Åsidosättning av schema är aktiv

**Bedömning:** Ingen ändring föreslås.

## 2020. `component::bosch_shc::entity::binary_sensor::call_for_heat::name`

**Engelska:** Call for heat

**Befintlig svenska:** Värmebegäran

**Bedömning:** Ingen ändring föreslås.

## 2021. `component::ptdevices::exceptions::update_failed::message`

**Engelska:** Failed to update PTDevices data: {error}

**Befintlig svenska:** Det gick inte att uppdatera PTDevices-data: {error}

**Bedömning:** Ingen ändring föreslås.

## 2022. `component::vallox::entity::sensor::current_profile::state::home`

**Engelska:** [%key:common::state::home%]

**Befintlig svenska:** Hemma

**Kontextkontroll:** Kontrollera referensmålet `common::state::home`; det ingår ännu inte i det insamlade underlaget.

## 2023. `component::vallox::entity::sensor::current_profile::state::fireplace`

**Engelska:** [%key:component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::fireplace%]

**Befintlig svenska:** Eldstad/anpassat

**Bedömning:** Ingen ändring föreslås.

## 2024. `component::vallox::entity::sensor::current_profile::state::extra`

**Engelska:** [%key:component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::extra%]

**Befintlig svenska:** Extra

**Bedömning:** Ingen ändring föreslås.

## 2025. `component::vallox::entity::sensor::current_profile::state::boost`

**Engelska:** [%key:component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::boost%]

**Befintlig svenska:** Forcering

**Bedömning:** Ingen ändring föreslås.

## 2026. `component::vallox::entity::sensor::current_profile::state::away`

**Engelska:** [%key:common::state::not_home%]

**Befintlig svenska:** Bortaläge

**Kontextkontroll:** Kontrollera referensmålet `common::state::not_home`; det ingår ännu inte i det insamlade underlaget.

## 2027. `component::vallox::entity::sensor::current_profile::state::auto`

**Engelska:** [%key:common::state::auto%]

**Befintlig svenska:** Automatiskt

**Kontextkontroll:** Kontrollera referensmålet `common::state::auto`; det ingår ännu inte i det insamlade underlaget.

## 2028. `component::vallox::entity::sensor::cell_state::state::heat_recovery`

**Engelska:** Heat recovery

**Befintlig svenska:** Värmeåtervinning

**Bedömning:** Ingen ändring föreslås.

## 2029. `component::vallox::entity::sensor::cell_state::state::defrosting`

**Engelska:** Defrosting

**Befintlig svenska:** Avfrostning

**Bedömning:** Ingen ändring föreslås.

## 2030. `component::vallox::entity::sensor::cell_state::state::cool_recovery`

**Engelska:** Cool recovery

**Befintlig svenska:** Kylåtervinning

**Bedömning:** Ingen ändring föreslås.

## 2031. `component::vallox::entity::sensor::cell_state::state::bypass`

**Engelska:** Bypass

**Befintlig svenska:** Förbikoppling

**Bedömning:** Ingen ändring föreslås.

## 2032. `component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::home`

**Engelska:** [%key:common::state::home%]

**Befintlig svenska:** Hemma

**Kontextkontroll:** Kontrollera referensmålet `common::state::home`; det ingår ännu inte i det insamlade underlaget.

## 2033. `component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::fireplace`

**Engelska:** Fireplace / Custom

**Befintlig svenska:** Eldstad/anpassat

**Bedömning:** Ingen ändring föreslås.

## 2034. `component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::extra`

**Engelska:** Extra

**Befintlig svenska:** Extra

**Bedömning:** Ingen ändring föreslås.

## 2035. `component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::boost`

**Engelska:** Boost

**Befintlig svenska:** Forcering

**Bedömning:** Ingen ändring föreslås.

## 2036. `component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::away`

**Engelska:** [%key:common::state::not_home%]

**Befintlig svenska:** Bortaläge

**Kontextkontroll:** Kontrollera referensmålet `common::state::not_home`; det ingår ännu inte i det insamlade underlaget.

## 2037. `component::vallox::entity::fan::ventilation::state_attributes::preset_mode::state::auto`

**Engelska:** [%key:common::state::auto%]

**Befintlig svenska:** Automatiskt

**Kontextkontroll:** Kontrollera referensmålet `common::state::auto`; det ingår ännu inte i det insamlade underlaget.

## 2038. `component::lifx::services::effect_pulse::fields::xy_color::name`

**Engelska:** [%key:component::light::common::field_xy_color_name%]

**Befintlig svenska:** XY-färg

**Kontextkontroll:** Kontrollera referensmålet `component::light::common::field_xy_color_name`; det ingår ännu inte i det insamlade underlaget.

## 2039. `component::lifx::services::effect_pulse::fields::xy_color::description`

**Engelska:** The temporary color in XY-format. A list of two decimal numbers between 0 and 1.

**Befintlig svenska:** Den tillfälliga färgen i XY-format. En lista med två decimaltal mellan 0 och 1.

**Bedömning:** Ingen ändring föreslås.

## 2040. `component::lifx::services::effect_pulse::fields::hs_color::name`

**Engelska:** [%key:component::light::common::field_hs_color_name%]

**Befintlig svenska:** Nyans-/mättnadsfärg

**Kontextkontroll:** Kontrollera referensmålet `component::light::common::field_hs_color_name`; det ingår ännu inte i det insamlade underlaget.

## 2041. `component::lifx::services::effect_pulse::fields::hs_color::description`

**Engelska:** The temporary color in hue/sat format. A list of two numbers. Hue is 0-360 and Sat is 0-100.

**Befintlig svenska:** Den tillfälliga färgen i nyans-/mättnadsformat. En lista med två tal. Nyans är 0–360 och mättnad är 0–100.

**Bedömning:** Ingen ändring föreslås.

## 2042. `component::lifx::services::effect_pulse::fields::color_temp_kelvin::name`

**Engelska:** [%key:component::light::common::field_color_temp_kelvin_name%]

**Befintlig svenska:** Färgtemperatur

**Kontextkontroll:** Kontrollera referensmålet `component::light::common::field_color_temp_kelvin_name`; det ingår ännu inte i det insamlade underlaget.

## 2043. `component::lifx::services::effect_pulse::fields::color_temp_kelvin::description`

**Engelska:** The temporary color temperature in Kelvin.

**Befintlig svenska:** Den tillfälliga färgtemperaturen i kelvin.

**Bedömning:** Ingen ändring föreslås.

## 2044. `component::greencell::exceptions::execute_not_allowed::message`

**Engelska:** The device does not allow Home Assistant to execute commands. Enable it in the device settings.

**Befintlig svenska:** Enheten tillåter inte att Home Assistant kör kommandon. Aktivera det i enhetens inställningar.

**Bedömning:** Ingen ändring föreslås.

## 2045. `component::greencell::entity::switch::charging::name`

**Engelska:** [%key:common::state::charging%]

**Befintlig svenska:** Laddning

**Kontextkontroll:** Kontrollera referensmålet `common::state::charging`; det ingår ännu inte i det insamlade underlaget.

## 2046. `component::foreca::services::get_3_hour_forecast::name`

**Engelska:** Get 3-hour forecast

**Befintlig svenska:** Hämta 3-timmarsprognos

**Bedömning:** Ingen ändring föreslås.

## 2047. `component::foreca::services::get_3_hour_forecast::description`

**Engelska:** Retrieves the forecast in 3-hour steps for the next 14 days, in the weather entity's units, with the values weather.get_forecasts has no place for. Every call makes a request to the Foreca Weather API and counts toward the daily limit of your plan.

**Befintlig svenska:** Hämtar prognosen i 3-timmarssteg för de kommande 14 dagarna, i väderentitetens enheter, med de värden som weather.get_forecasts saknar plats för. Varje anrop gör en förfrågan till Foreca Weather API och räknas mot din plans dagliga gräns.

**Förslag:** Hämtar prognosen i 3-timmarssteg för de kommande 14 dagarna, i väderentitetens enheter, med de värden som weather.get_forecasts saknar plats för. Varje anrop gör en förfrågan till Foreca Weather API och räknas mot abonnemangets dagliga gräns.

## 2048. `component::foreca::exceptions::three_hour_forecast_error::message`

**Engelska:** Error fetching the 3-hour forecast.

**Befintlig svenska:** Fel vid hämtning av 3-timmarsprognosen.

**Bedömning:** Ingen ändring föreslås.

## 2049. `component::vicare::entity::sensor::water_flow::name`

**Engelska:** Water flow

**Befintlig svenska:** Vattenflöde

**Bedömning:** Ingen ändring föreslås.

## 2050. `component::vicare::entity::sensor::water_consumption_total::name`

**Engelska:** Water consumption

**Befintlig svenska:** Vattenförbrukning

**Bedömning:** Ingen ändring föreslås.

## 2051. `component::vicare::entity::sensor::water_consumption_today::name`

**Engelska:** Water consumption today

**Befintlig svenska:** Vattenförbrukning i dag

**Bedömning:** Ingen ändring föreslås.

## 2052. `component::vicare::entity::sensor::salt_supply::name`

**Engelska:** Salt supply

**Befintlig svenska:** Saltförråd

**Bedömning:** Ingen ändring föreslås.

## 2053. `component::synology_dsm::entity::update::package_update::name`

**Engelska:** {package_name} update

**Befintlig svenska:** {package_name}-uppdatering

**Bedömning:** Ingen ändring föreslås.

## 2054. `component::fressnapf_tracker::entity::sensor::last_seen::name`

**Engelska:** Last seen

**Befintlig svenska:** Senast sedd

**Bedömning:** Ingen ändring föreslås.

## 2055. `component::fressnapf_tracker::entity::binary_sensor::seen_recently::name`

**Engelska:** Seen recently

**Befintlig svenska:** Sedd nyligen

**Bedömning:** Ingen ändring föreslås.

## 2056. `component::izone::entity::binary_sensor::sensor_fault::name`

**Engelska:** Sensor fault

**Befintlig svenska:** Sensorfel

**Bedömning:** Ingen ändring föreslås.

## 2057. `component::izone::entity::binary_sensor::damper_fault::name`

**Engelska:** Damper fault

**Befintlig svenska:** Spjällfel

**Bedömning:** Ingen ändring föreslås.

## 2058. `component::watergate::entity::sensor::battery_voltage::name`

**Engelska:** Battery voltage

**Befintlig svenska:** Batterispänning

**Bedömning:** Ingen ändring föreslås.

## 2059. `component::watergate::entity::binary_sensor::external_power::name`

**Engelska:** External power

**Befintlig svenska:** Extern strömförsörjning

**Bedömning:** Ingen ändring föreslås.

## 2060. `component::hp_printer::config::step::user::sections::advanced_settings::name`

**Engelska:** Advanced settings

**Befintlig svenska:** Avancerade inställningar

**Bedömning:** Ingen ändring föreslås.

## 2061. `component::hp_printer::config::step::user::sections::advanced_settings::data_description::ssl`

**Engelska:** Connect to the printer's web interface over HTTPS.

**Befintlig svenska:** Anslut till skrivarens webbgränssnitt via HTTPS.

**Bedömning:** Ingen ändring föreslås.

## 2062. `component::hp_printer::config::step::user::sections::advanced_settings::data_description::port`

**Engelska:** The port of the printer's web interface. Leave empty to use 80, or 443 with SSL.

**Befintlig svenska:** Porten för skrivarens webbgränssnitt. Lämna tomt för att använda 80 eller 443 med SSL.

**Bedömning:** Ingen ändring föreslås.

## 2063. `component::hp_printer::config::step::user::sections::advanced_settings::data::ssl`

**Engelska:** [%key:common::config_flow::data::ssl%]

**Befintlig svenska:** [%key:common::config_flow::data::ssl%]

**Bedömning:** Ingen ändring föreslås.

## 2064. `component::hp_printer::config::step::user::sections::advanced_settings::data::port`

**Engelska:** [%key:common::config_flow::data::port%]

**Befintlig svenska:** [%key:common::config_flow::data::port%]

**Bedömning:** Ingen ändring föreslås.

## 2065. `component::synology_dsm::issues::deprecated_action::title`

**Engelska:** The `{action}` action is being removed

**Befintlig svenska:** Åtgärden `{action}` tas bort

**Bedömning:** Ingen ändring föreslås.

## 2066. `component::synology_dsm::issues::deprecated_action::description`

**Engelska:** The `{action}` action is deprecated and will be removed in Home Assistant 2027.6. Use the **Restart** or **Shut down** button entity of your NAS with the `button.press` action instead, and update any automations or scripts that use `{action}`.

**Befintlig svenska:** Åtgärden `{action}` är föråldrad och tas bort i Home Assistant 2027.6. Använd i stället knappentiteten **Starta om** eller **Stäng av** på NAS:en med åtgärden `button.press` och uppdatera de automationer eller skript som använder `{action}`.

**Bedömning:** Ingen ändring föreslås.

## 2067. `component::button::triggers::hold_ended::name`

**Engelska:** Button hold ended

**Befintlig svenska:** Knappnedtryckning avslutad

**Bedömning:** Ingen ändring föreslås.

## 2068. `component::button::triggers::hold_ended::description`

**Engelska:** Triggers when one or more buttons are released after being held.

**Befintlig svenska:** Utlöses när en eller flera knappar släpps efter att ha hållits nedtryckta.

**Bedömning:** Ingen ändring föreslås.

## 2069. `component::shelly::entity::fan::fan::state_attributes::preset_mode::state::manual`

**Engelska:** [%key:common::state::manual%]

**Befintlig svenska:** Manuellt

**Kontextkontroll:** Kontrollera referensmålet `common::state::manual`; det ingår ännu inte i det insamlade underlaget.

## 2070. `component::shelly::entity::fan::fan::state_attributes::preset_mode::state::auto`

**Engelska:** [%key:common::state::auto%]

**Befintlig svenska:** Automatiskt

**Kontextkontroll:** Kontrollera referensmålet `common::state::auto`; det ingår ännu inte i det insamlade underlaget.

## 2071. `component::vesync::entity::select::night_light_level::state::auto`

**Engelska:** [%key:common::state::auto%]

**Befintlig svenska:** Automatiskt

**Kontextkontroll:** Kontrollera referensmålet `common::state::auto`; det ingår ännu inte i det insamlade underlaget.

## 2072. `component::shelly::entity::switch::boost::name`

**Engelska:** Boost

**Befintlig svenska:** Forcering

**Bedömning:** Ingen ändring föreslås.

## 2073. `component::skoda::entity::binary_sensor::charging_cable::name`

**Engelska:** Charging cable

**Befintlig svenska:** Laddningskabel

**Bedömning:** Ingen ändring föreslås.

## 2074. `component::skoda::entity::binary_sensor::auxiliary_heating::name`

**Engelska:** Auxiliary heating

**Befintlig svenska:** Tillsatsvärmare

**Bedömning:** Ingen ändring föreslås.

## 2075. `component::skoda::entity::binary_sensor::air_conditioning::name`

**Engelska:** Air conditioning

**Befintlig svenska:** Luftkonditionering

**Bedömning:** Ingen ändring föreslås.

## 2076. `component::zwave_js::issues::deprecated_ping_action::title`

**Engelska:** The `{action}` action is being removed

**Befintlig svenska:** Åtgärden `{action}` tas bort

**Bedömning:** Ingen ändring föreslås.

## 2077. `component::zwave_js::issues::deprecated_ping_action::description`

**Engelska:** The `{action}` action is deprecated and will be removed in Home Assistant 2027.6. Use the **Ping** button entity of each Z-Wave device with the `button.press` action instead, and update any automations or scripts that use `{action}`.

**Befintlig svenska:** Åtgärden `{action}` är föråldrad och kommer att tas bort i Home Assistant 2027.6. Använd i stället knappentiteten **Ping** för varje Z-Wave-enhet med åtgärden `button.press`, och uppdatera automatiseringar eller skript som använder `{action}`.

**Bedömning:** Ingen ändring föreslås.

## 2078. `component::mijn_farmad_apotheek::config::step::reconfigure::title`

**Engelska:** Reconfigure Mijn Farmad Apotheek

**Befintlig svenska:** Konfigurera om Mijn Farmad Apotheek

**Bedömning:** Ingen ändring föreslås.

## 2079. `component::mijn_farmad_apotheek::config::step::reconfigure::description`

**Engelska:** Sign in with the current credentials of your Mijn Farmad Apotheek account.

**Befintlig svenska:** Logga in med de aktuella inloggningsuppgifterna för ditt Mijn Farmad Apotheek-konto.

**Bedömning:** Ingen ändring föreslås.

## 2080. `component::mijn_farmad_apotheek::config::step::reconfigure::data_description::password`

**Engelska:** [%key:component::mijn_farmad_apotheek::config::step::user::data_description::password%]

**Befintlig svenska:** Lösenordet till ditt Mijn Farmad Apotheek-konto.

**Kontextkontroll:** Kontrollera referensmålet `component::mijn_farmad_apotheek::config::step::user::data_description::password`; det ingår ännu inte i det insamlade underlaget.

## 2081. `component::mijn_farmad_apotheek::config::step::reconfigure::data_description::email`

**Engelska:** [%key:component::mijn_farmad_apotheek::config::step::user::data_description::email%]

**Befintlig svenska:** E-postadressen till ditt Mijn Farmad Apotheek-konto.

**Kontextkontroll:** Kontrollera referensmålet `component::mijn_farmad_apotheek::config::step::user::data_description::email`; det ingår ännu inte i det insamlade underlaget.

## 2082. `component::mijn_farmad_apotheek::config::step::reconfigure::data::password`

**Engelska:** [%key:common::config_flow::data::password%]

**Befintlig svenska:** Lösenord

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::password`; det ingår ännu inte i det insamlade underlaget.

## 2083. `component::mijn_farmad_apotheek::config::step::reconfigure::data::email`

**Engelska:** [%key:common::config_flow::data::email%]

**Befintlig svenska:** E-post

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::email`; det ingår ännu inte i det insamlade underlaget.

## 2084. `component::engie_be::config::step::reconfigure::description`

**Engelska:** [%key:component::engie_be::config::step::user::description%]

**Befintlig svenska:** Ange dina inloggningsuppgifter för ENGIE Belgium och metod för tvåfaktorsautentisering. **Ett särskilt ENGIE-konto krävs**: om du loggar in på samma konto från engie.be eller ENGIE Smart App verkar integrationens session återkallas och du måste autentisera dig igen. Skapa en separat användare via [ENGIE:s sida för användarhantering]({user_management_url}). Nya konton har 2FA aktiverat som standard.

**Kontextkontroll:** Kontrollera referensmålet `component::engie_be::config::step::user::description`; det ingår ännu inte i det insamlade underlaget.

## 2085. `component::engie_be::config::step::reconfigure::data_description::password`

**Engelska:** [%key:component::engie_be::config::step::user::data_description::password%]

**Befintlig svenska:** Lösenordet till ditt ENGIE Belgium-konto.

**Kontextkontroll:** Kontrollera referensmålet `component::engie_be::config::step::user::data_description::password`; det ingår ännu inte i det insamlade underlaget.

## 2086. `component::engie_be::config::step::reconfigure::data_description::mfa_method`

**Engelska:** [%key:component::engie_be::config::step::user::data_description::mfa_method%]

**Befintlig svenska:** Välj hur du vill ta emot din verifieringskod.

**Kontextkontroll:** Kontrollera referensmålet `component::engie_be::config::step::user::data_description::mfa_method`; det ingår ännu inte i det insamlade underlaget.

## 2087. `component::engie_be::config::step::reconfigure::data_description::email`

**Engelska:** [%key:component::engie_be::config::step::user::data_description::email%]

**Befintlig svenska:** E-postadressen till ditt ENGIE Belgium-konto.

**Kontextkontroll:** Kontrollera referensmålet `component::engie_be::config::step::user::data_description::email`; det ingår ännu inte i det insamlade underlaget.

## 2088. `component::engie_be::config::step::reconfigure::data::password`

**Engelska:** [%key:common::config_flow::data::password%]

**Befintlig svenska:** Lösenord

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::password`; det ingår ännu inte i det insamlade underlaget.

## 2089. `component::engie_be::config::step::reconfigure::data::mfa_method`

**Engelska:** [%key:component::engie_be::config::step::user::data::mfa_method%]

**Befintlig svenska:** Metod för tvåfaktorsautentisering

**Kontextkontroll:** Kontrollera referensmålet `component::engie_be::config::step::user::data::mfa_method`; det ingår ännu inte i det insamlade underlaget.

## 2090. `component::engie_be::config::step::reconfigure::data::email`

**Engelska:** [%key:common::config_flow::data::email%]

**Befintlig svenska:** E-post

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::email`; det ingår ännu inte i det insamlade underlaget.

## 2091. `component::sofar::entity::sensor::cell_voltage::name`

**Engelska:** Cell voltage {cell}

**Befintlig svenska:** Cellspänning {cell}

**Bedömning:** Ingen ändring föreslås.

## 2092. `component::sofar::entity::sensor::cell_temperature::name`

**Engelska:** Cell temperature {sensor}

**Befintlig svenska:** Celltemperatur {sensor}

**Bedömning:** Ingen ändring föreslås.

## 2093. `component::freebox::entity::sensor::ipv6::name`

**Engelska:** WAN IPv6 address

**Befintlig svenska:** WAN IPv6-adress

**Bedömning:** Ingen ändring föreslås.

## 2094. `component::freebox::entity::sensor::ipv4::name`

**Engelska:** WAN IPv4 address

**Befintlig svenska:** WAN IPv4-adress

**Bedömning:** Ingen ändring föreslås.

## 2095. `component::freebox::entity::sensor::connection_state::state::up`

**Engelska:** Up

**Befintlig svenska:** Uppe

**Bedömning:** Ingen ändring föreslås.

## 2096. `component::freebox::entity::sensor::connection_state::state::going_up`

**Engelska:** Going up

**Befintlig svenska:** Kopplas upp

**Bedömning:** Ingen ändring föreslås.

## 2097. `component::freebox::entity::sensor::connection_state::state::going_down`

**Engelska:** Going down

**Befintlig svenska:** Kopplas ner

**Bedömning:** Ingen ändring föreslås.

## 2098. `component::freebox::entity::sensor::connection_state::state::down`

**Engelska:** Down

**Befintlig svenska:** Nere

**Bedömning:** Ingen ändring föreslås.

## 2099. `component::freebox::entity::sensor::connection_state::name`

**Engelska:** Connection state

**Befintlig svenska:** Anslutningsstatus

**Bedömning:** Ingen ändring föreslås.

## 2100. `component::freebox::entity::sensor::bandwidth_up::name`

**Engelska:** Upload bandwidth

**Befintlig svenska:** Bandbredd för uppladdning

**Bedömning:** Ingen ändring föreslås.

## 2101. `component::freebox::entity::sensor::bandwidth_down::name`

**Engelska:** Download bandwidth

**Befintlig svenska:** Bandbredd för nedladdning

**Bedömning:** Ingen ändring föreslås.

## 2102. `component::abrp::entity::device_tracker::location::name`

**Engelska:** Location

**Befintlig svenska:** Plats

**Bedömning:** Ingen ändring föreslås.

## 2103. `component::zoneminder::services::set_run_state::fields::id::name`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** Värd

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::host`; det ingår ännu inte i det insamlade underlaget.

## 2104. `component::zoneminder::services::set_run_state::fields::id::description`

**Engelska:** The host of the ZoneMinder server, as configured.

**Befintlig svenska:** Värden för ZoneMinder-servern enligt konfigurationen.

**Bedömning:** Ingen ändring föreslås.

## 2105. `component::vitesy::config::step::reconfigure::description`

**Engelska:** Update the credentials of your Vitesy Hub account.

**Befintlig svenska:** Uppdatera inloggningsuppgifterna för ditt Vitesy Hub-konto.

**Bedömning:** Ingen ändring föreslås.

## 2106. `component::vitesy::config::step::reconfigure::data_description::password`

**Engelska:** [%key:component::vitesy::config::step::user::data_description::password%]

**Befintlig svenska:** Lösenordet till ditt Vitesy Hub-konto.

**Kontextkontroll:** Kontrollera referensmålet `component::vitesy::config::step::user::data_description::password`; det ingår ännu inte i det insamlade underlaget.

## 2107. `component::vitesy::config::step::reconfigure::data_description::email`

**Engelska:** [%key:component::vitesy::config::step::user::data_description::email%]

**Befintlig svenska:** E-postadressen till ditt Vitesy Hub-konto.

**Kontextkontroll:** Kontrollera referensmålet `component::vitesy::config::step::user::data_description::email`; det ingår ännu inte i det insamlade underlaget.

## 2108. `component::vitesy::config::step::reconfigure::data::password`

**Engelska:** [%key:common::config_flow::data::password%]

**Befintlig svenska:** Lösenord

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::password`; det ingår ännu inte i det insamlade underlaget.

## 2109. `component::vitesy::config::step::reconfigure::data::email`

**Engelska:** [%key:common::config_flow::data::email%]

**Befintlig svenska:** E-post

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::email`; det ingår ännu inte i det insamlade underlaget.

## 2110. `component::vitesy::config::abort::reconfigure_account_mismatch`

**Engelska:** The credentials belong to a different Vitesy Hub account than the one originally configured.

**Befintlig svenska:** Inloggningsuppgifterna tillhör ett annat Vitesy Hub-konto än det som ursprungligen konfigurerades.

**Bedömning:** Ingen ändring föreslås.

## 2111. `component::velbus::exceptions::no_modules::message`

**Engelska:** No Velbus modules found, please check your VLP file.

**Befintlig svenska:** Inga Velbus-moduler hittades. Kontrollera VLP-filen.

**Bedömning:** Ingen ändring föreslås.

## 2112. `component::velbus::entity::sensor::counter::name`

**Engelska:** {channel_name} counter

**Befintlig svenska:** {channel_name}-räknare

**Bedömning:** Ingen ändring föreslås.

## 2113. `component::velbus::entity::select::select_program::name`

**Engelska:** Program

**Befintlig svenska:** Program

**Bedömning:** Ingen ändring föreslås.

## 2114. `component::velbus::entity::light::button_light::name`

**Engelska:** LED {channel_name}

**Befintlig svenska:** LED {channel_name}

**Bedömning:** Ingen ändring föreslås.

## 2115. `component::button::triggers::held::name`

**Engelska:** Button held

**Befintlig svenska:** Knapp nedtryckt

**Förslag:** Knapp hålls nedtryckt

## 2116. `component::button::triggers::held::fields::interval::name`

**Engelska:** Interval

**Befintlig svenska:** Intervall

**Bedömning:** Ingen ändring föreslås.

## 2117. `component::button::triggers::held::fields::interval::description`

**Engelska:** How often to trigger again while the button stays held. Leave empty to trigger once per hold.

**Befintlig svenska:** Hur ofta den ska utlösas igen medan knappen hålls nedtryckt. Lämna tomt för att utlösa en gång per nedtryckning.

**Bedömning:** Ingen ändring föreslås.

## 2118. `component::button::triggers::held::description`

**Engelska:** Triggers when one or more buttons are held, optionally repeating at a set interval for as long as they stay held.

**Befintlig svenska:** Utlöses när en eller flera knappar hålls nedtryckta och kan upprepas med ett angivet intervall så länge de hålls nedtryckta.

**Bedömning:** Ingen ändring föreslås.

## 2119. `component::system_bridge::exceptions::notification_failed::message`

**Engelska:** Failed to send the notification: {error}

**Befintlig svenska:** Kunde inte skicka aviseringen: {error}

**Bedömning:** Ingen ändring föreslås.

## 2120. `component::foreca::services::get_forecasts_extra::name`

**Engelska:** Get extra forecast values

**Befintlig svenska:** Hämta extra prognosvärden

**Bedömning:** Ingen ändring föreslås.

## 2121. `component::foreca::services::get_forecasts_extra::fields::type::name`

**Engelska:** Forecast type

**Befintlig svenska:** Prognostyp

**Bedömning:** Ingen ändring föreslås.

## 2122. `component::foreca::services::get_forecasts_extra::fields::type::description`

**Engelska:** The forecast to return the values for.

**Befintlig svenska:** Prognosen som värdena ska returneras för.

**Bedömning:** Ingen ändring föreslås.

## 2123. `component::foreca::services::get_forecasts_extra::description`

**Engelska:** Retrieves the forecast values that weather.get_forecasts has no place for, such as precipitation type, snow, solar radiation, sunshine, sunrise and the ensemble range of the daily forecast. They come from the forecast already fetched, so the action makes no API requests.

**Befintlig svenska:** Hämtar de prognosvärden som weather.get_forecasts saknar plats för, till exempel nederbördstyp, snö, solstrålning, solsken, soluppgång och ensembleintervallet för dygnsprognosen. Värdena kommer från den prognos som redan har hämtats, så åtgärden gör inga API-anrop.

**Bedömning:** Ingen ändring föreslås.

## 2124. `component::foreca::selector::forecast_type::options::hourly`

**Engelska:** Hourly

**Befintlig svenska:** Varje timme

**Bedömning:** Ingen ändring föreslås.

## 2125. `component::foreca::selector::forecast_type::options::daily`

**Engelska:** Daily

**Befintlig svenska:** Dagligen

**Bedömning:** Ingen ändring föreslås.

## 2126. `component::sofar::services::set_battery_cutoffs::name`

**Engelska:** Set battery cut-offs

**Befintlig svenska:** Ange batteriets frånkopplingsgränser

**Bedömning:** Ingen ändring föreslås.

## 2127. `component::sofar::services::set_battery_cutoffs::fields::on_grid_discharge_cutoff_soc::name`

**Engelska:** On-grid discharge cut-off state of charge

**Befintlig svenska:** Urladdningens frånkopplingsgräns med elnät

**Bedömning:** Ingen ändring föreslås.

## 2128. `component::sofar::services::set_battery_cutoffs::fields::on_grid_discharge_cutoff_soc::description`

**Engelska:** The charge level at which the battery stops discharging while the grid is up. 10 to 100%.

**Befintlig svenska:** Laddningsnivån då batteriet slutar ladda ur medan elnätet är tillgängligt. 10 till 100 %.

**Bedömning:** Ingen ändring föreslås.

## 2129. `component::sofar::services::set_battery_cutoffs::fields::off_grid_recovery_soc::name`

**Engelska:** Off-grid discharge recovery state of charge

**Befintlig svenska:** Återhämtningsnivå för urladdning utan elnät

**Bedömning:** Ingen ändring föreslås.

## 2130. `component::sofar::services::set_battery_cutoffs::fields::off_grid_recovery_soc::description`

**Engelska:** The charge level the battery recharges to before it discharges off-grid again. 15 to 100%, at least 5% above the off-grid cut-off.

**Befintlig svenska:** Laddningsnivån som batteriet laddas till innan det laddar ur utan elnät igen. 15 till 100 %, minst 5 % över frånkopplingsgränsen utan elnät.

**Bedömning:** Ingen ändring föreslås.

## 2131. `component::sofar::services::set_battery_cutoffs::fields::off_grid_discharge_cutoff_soc::name`

**Engelska:** Off-grid discharge cut-off state of charge

**Befintlig svenska:** Urladdningens frånkopplingsgräns utan elnät

**Bedömning:** Ingen ändring föreslås.

## 2132. `component::sofar::services::set_battery_cutoffs::fields::off_grid_discharge_cutoff_soc::description`

**Engelska:** The charge level at which the battery stops discharging during a grid outage. 10 to 30%, at most the on-grid cut-off.

**Befintlig svenska:** Laddningsnivån då batteriet slutar ladda ur vid ett elnätsavbrott. 10 till 30 %, högst frånkopplingsgränsen med elnät.

**Bedömning:** Ingen ändring föreslås.

## 2133. `component::sofar::services::set_battery_cutoffs::fields::config_entry_id::name`

**Engelska:** Inverter

**Befintlig svenska:** Växelriktare

**Bedömning:** Ingen ändring föreslås.

## 2134. `component::sofar::services::set_battery_cutoffs::fields::config_entry_id::description`

**Engelska:** The Sofar inverter to send this to.

**Befintlig svenska:** Sofar-växelriktaren som detta ska skickas till.

**Bedömning:** Ingen ändring föreslås.

## 2135. `component::sofar::services::set_battery_cutoffs::fields::charge_cutoff_soc::name`

**Engelska:** Charge cut-off state of charge

**Befintlig svenska:** Laddningens frånkopplingsgräns

**Bedömning:** Ingen ändring föreslås.

## 2136. `component::sofar::services::set_battery_cutoffs::fields::charge_cutoff_soc::description`

**Engelska:** The charge level at which the battery stops charging. 60 to 100%. Left unchanged when omitted. Not every inverter supports it.

**Befintlig svenska:** Laddningsnivån då batteriet slutar ladda. 60 till 100 %. Lämnas oförändrad om den utelämnas. Stöds inte av alla växelriktare.

**Bedömning:** Ingen ändring föreslås.

## 2137. `component::sofar::services::set_battery_cutoffs::description`

**Engelska:** Sets the battery's cut-off levels, as shown on the SofarCloud app's battery parameters page. The inverter stores each change, so avoid calling this often. Only for inverters with battery storage.

**Befintlig svenska:** Anger batteriets frånkopplingsgränser enligt sidan med batteriparametrar i SofarCloud-appen. Växelriktaren sparar varje ändring, så använd inte detta ofta. Endast för växelriktare med batterilagring.

**Bedömning:** Ingen ändring föreslås.

## 2138. `component::sofar::exceptions::charge_cutoff_unsupported::message`

**Engelska:** {title} does not support setting the charge cut-off.

**Befintlig svenska:** {title} har inte stöd för att ange laddningens frånkopplingsgräns.

**Bedömning:** Ingen ändring föreslås.

## 2139. `component::sofar::entity::sensor::remaining_capacity::name`

**Engelska:** Remaining capacity

**Befintlig svenska:** Återstående kapacitet

**Bedömning:** Ingen ändring föreslås.

## 2140. `component::sofar::entity::sensor::mosfet_temperature::name`

**Engelska:** MOSFET temperature

**Befintlig svenska:** MOSFET-temperatur

**Bedömning:** Ingen ändring föreslås.

## 2141. `component::sofar::entity::sensor::internal_temperature::name`

**Engelska:** Internal temperature

**Befintlig svenska:** Intern temperatur

**Bedömning:** Ingen ändring föreslås.

## 2142. `component::sofar::entity::sensor::full_charge_capacity::name`

**Engelska:** Full charge capacity

**Befintlig svenska:** Kapacitet vid full laddning

**Bedömning:** Ingen ändring föreslås.

## 2143. `component::sofar::entity::sensor::cell_voltage_min::name`

**Engelska:** Lowest cell voltage

**Befintlig svenska:** Lägsta cellspänning

**Bedömning:** Ingen ändring föreslås.

## 2144. `component::sofar::entity::sensor::cell_voltage_max::name`

**Engelska:** Highest cell voltage

**Befintlig svenska:** Högsta cellspänning

**Bedömning:** Ingen ändring föreslås.

## 2145. `component::sofar::device::battery_pack::name`

**Engelska:** Battery pack {group}.{pack}

**Befintlig svenska:** Batteripaket {group}.{pack}

**Bedömning:** Ingen ändring föreslås.

## 2146. `component::foreca::entity::sensor::thunderstorm_probability::name`

**Engelska:** Thunderstorm probability

**Befintlig svenska:** Sannolikhet för åska

**Bedömning:** Ingen ändring föreslås.

## 2147. `component::foreca::entity::sensor::precipitation_probability::name`

**Engelska:** Precipitation probability

**Befintlig svenska:** Sannolikhet för nederbörd

**Bedömning:** Ingen ändring föreslås.

## 2148. `component::agent_dvr::config::step::hassio_confirm::title`

**Engelska:** Agent DVR via Home Assistant app

**Befintlig svenska:** Agent DVR via Home Assistant-appen

**Bedömning:** Ingen ändring föreslås.

## 2149. `component::agent_dvr::config::step::hassio_confirm::description`

**Engelska:** Do you want to configure Home Assistant to connect to the Agent DVR server provided by the app: {addon}?

**Befintlig svenska:** Vill du konfigurera Home Assistant så att den ansluter till Agent DVR-servern som tillhandahålls av appen {addon}?

**Bedömning:** Ingen ändring föreslås.

## 2150. `component::agent_dvr::config::abort::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::cannot_connect`; det ingår ännu inte i det insamlade underlaget.

## 2151. `component::zha::entity::sensor::hvac_action::state::preheating`

**Engelska:** [%key:component::climate::entity_component::_::state_attributes::hvac_action::state::preheating%]

**Befintlig svenska:** Förvärmning

**Kontextkontroll:** Kontrollera referensmålet `component::climate::entity_component::_::state_attributes::hvac_action::state::preheating`; det ingår ännu inte i det insamlade underlaget.

## 2152. `component::zha::entity::sensor::hvac_action::state::off`

**Engelska:** [%key:common::state::off%]

**Befintlig svenska:** Av

**Kontextkontroll:** Kontrollera referensmålet `common::state::off`; det ingår ännu inte i det insamlade underlaget.

## 2153. `component::zha::entity::sensor::hvac_action::state::idle`

**Engelska:** [%key:common::state::idle%]

**Befintlig svenska:** Viloläge

**Kontextkontroll:** Kontrollera referensmålet `common::state::idle`; det ingår ännu inte i det insamlade underlaget.

## 2154. `component::zha::entity::sensor::hvac_action::state::heating`

**Engelska:** [%key:component::climate::entity_component::_::state_attributes::hvac_action::state::heating%]

**Befintlig svenska:** Uppvärmning

**Kontextkontroll:** Kontrollera referensmålet `component::climate::entity_component::_::state_attributes::hvac_action::state::heating`; det ingår ännu inte i det insamlade underlaget.

## 2155. `component::zha::entity::sensor::hvac_action::state::fan`

**Engelska:** [%key:component::climate::entity_component::_::state_attributes::hvac_action::state::fan%]

**Befintlig svenska:** Fläkt

**Kontextkontroll:** Kontrollera referensmålet `component::climate::entity_component::_::state_attributes::hvac_action::state::fan`; det ingår ännu inte i det insamlade underlaget.

## 2156. `component::zha::entity::sensor::hvac_action::state::drying`

**Engelska:** [%key:component::climate::entity_component::_::state_attributes::hvac_action::state::drying%]

**Befintlig svenska:** Avfuktning

**Kontextkontroll:** Kontrollera referensmålet `component::climate::entity_component::_::state_attributes::hvac_action::state::drying`; det ingår ännu inte i det insamlade underlaget.

## 2157. `component::zha::entity::sensor::hvac_action::state::defrosting`

**Engelska:** [%key:component::climate::entity_component::_::state_attributes::hvac_action::state::defrosting%]

**Befintlig svenska:** Avfrostning

**Kontextkontroll:** Kontrollera referensmålet `component::climate::entity_component::_::state_attributes::hvac_action::state::defrosting`; det ingår ännu inte i det insamlade underlaget.

## 2158. `component::zha::entity::sensor::hvac_action::state::cooling`

**Engelska:** [%key:component::climate::entity_component::_::state_attributes::hvac_action::state::cooling%]

**Befintlig svenska:** Kylning

**Kontextkontroll:** Kontrollera referensmålet `component::climate::entity_component::_::state_attributes::hvac_action::state::cooling`; det ingår ännu inte i det insamlade underlaget.

## 2159. `component::synology_dsm::exceptions::entry_not_loaded::message`

**Engelska:** DSM with serial {serial} is not loaded.

**Befintlig svenska:** DSM med serienumret {serial} är inte inläst.

**Bedömning:** Ingen ändring föreslås.

## 2160. `component::synology_dsm::options::step::init::data_description::snap_profile_type`

**Engelska:** The quality of the snapshots taken from Surveillance Station cameras.

**Befintlig svenska:** Kvaliteten på ögonblicksbilderna från Surveillance Station-kameror.

**Bedömning:** Ingen ändring föreslås.

## 2161. `component::synology_dsm::config::step::user::data_description::verify_ssl`

**Engelska:** Verify the SSL certificate of the NAS. Disable this when the NAS uses a self-signed certificate.

**Befintlig svenska:** Verifiera NAS:ens SSL-certifikat. Inaktivera detta när NAS:en använder ett självsignerat certifikat.

**Bedömning:** Ingen ändring föreslås.

## 2162. `component::synology_dsm::config::step::user::data_description::username`

**Engelska:** The DSM user Home Assistant uses to connect. The user must be a member of the administrators group.

**Befintlig svenska:** DSM-användaren som Home Assistant använder för anslutning. Användaren måste tillhöra administratörsgruppen.

**Bedömning:** Ingen ändring föreslås.

## 2163. `component::synology_dsm::config::step::user::data_description::ssl`

**Engelska:** Connect to DSM over HTTPS.

**Befintlig svenska:** Anslut till DSM via HTTPS.

**Bedömning:** Ingen ändring föreslås.

## 2164. `component::synology_dsm::config::step::user::data_description::port`

**Engelska:** The port of the DSM web interface. Leave empty to use the default port (5000, or 5001 when using SSL).

**Befintlig svenska:** Porten för DSM:s webbgränssnitt. Lämna tomt för att använda standardporten (5000 eller 5001 med SSL).

**Bedömning:** Ingen ändring föreslås.

## 2165. `component::synology_dsm::config::step::user::data_description::password`

**Engelska:** The password of the DSM user.

**Befintlig svenska:** Lösenordet för DSM-användaren.

**Bedömning:** Ingen ändring föreslås.

## 2166. `component::synology_dsm::config::step::reconfigure::data_description::verify_ssl`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::verify_ssl%]

**Befintlig svenska:** Verifiera NAS:ens SSL-certifikat. Inaktivera detta när NAS:en använder ett självsignerat certifikat.

**Bedömning:** Ingen ändring föreslås.

## 2167. `component::synology_dsm::config::step::reconfigure::data_description::username`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::username%]

**Befintlig svenska:** DSM-användaren som Home Assistant använder för anslutning. Användaren måste tillhöra administratörsgruppen.

**Bedömning:** Ingen ändring föreslås.

## 2168. `component::synology_dsm::config::step::reconfigure::data_description::ssl`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::ssl%]

**Befintlig svenska:** Anslut till DSM via HTTPS.

**Bedömning:** Ingen ändring föreslås.

## 2169. `component::synology_dsm::config::step::reconfigure::data_description::port`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::port%]

**Befintlig svenska:** Porten för DSM:s webbgränssnitt. Lämna tomt för att använda standardporten (5000 eller 5001 med SSL).

**Bedömning:** Ingen ändring föreslås.

## 2170. `component::synology_dsm::config::step::reconfigure::data_description::password`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::password%]

**Befintlig svenska:** Lösenordet för DSM-användaren.

**Bedömning:** Ingen ändring föreslås.

## 2171. `component::synology_dsm::config::step::reauth_confirm::data_description::username`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::username%]

**Befintlig svenska:** DSM-användaren som Home Assistant använder för anslutning. Användaren måste tillhöra administratörsgruppen.

**Bedömning:** Ingen ändring föreslås.

## 2172. `component::synology_dsm::config::step::reauth_confirm::data_description::password`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::password%]

**Befintlig svenska:** Lösenordet för DSM-användaren.

**Bedömning:** Ingen ändring föreslås.

## 2173. `component::synology_dsm::config::step::link::data_description::verify_ssl`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::verify_ssl%]

**Befintlig svenska:** Verifiera NAS:ens SSL-certifikat. Inaktivera detta när NAS:en använder ett självsignerat certifikat.

**Bedömning:** Ingen ändring föreslås.

## 2174. `component::synology_dsm::config::step::link::data_description::username`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::username%]

**Befintlig svenska:** DSM-användaren som Home Assistant använder för anslutning. Användaren måste tillhöra administratörsgruppen.

**Bedömning:** Ingen ändring föreslås.

## 2175. `component::synology_dsm::config::step::link::data_description::ssl`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::ssl%]

**Befintlig svenska:** Anslut till DSM via HTTPS.

**Bedömning:** Ingen ändring föreslås.

## 2176. `component::synology_dsm::config::step::link::data_description::port`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::port%]

**Befintlig svenska:** Porten för DSM:s webbgränssnitt. Lämna tomt för att använda standardporten (5000 eller 5001 med SSL).

**Bedömning:** Ingen ändring föreslås.

## 2177. `component::synology_dsm::config::step::link::data_description::password`

**Engelska:** [%key:component::synology_dsm::config::step::user::data_description::password%]

**Befintlig svenska:** Lösenordet för DSM-användaren.

**Bedömning:** Ingen ändring föreslås.

## 2178. `component::synology_dsm::config::step::2sa::data_description::otp_code`

**Engelska:** The current code from your two-step authentication app.

**Befintlig svenska:** Den aktuella koden från appen för tvåstegsautentisering.

**Bedömning:** Ingen ändring föreslås.

## 2179. `component::hassio::entity::sensor::disk_life_time::name`

**Engelska:** Disk lifetime

**Befintlig svenska:** Disklivslängd

**Bedömning:** Ingen ändring föreslås.

## 2180. `component::music_assistant::services::play_media::fields::shuffle::name`

**Engelska:** Shuffle

**Befintlig svenska:** Blanda

**Bedömning:** Ingen ändring föreslås.

## 2181. `component::music_assistant::services::play_media::fields::shuffle::description`

**Engelska:** Whether to play the content in randomized order. Only applies when the content starts playing right away. If omitted, the queue's shuffle setting and the type of content decide.

**Befintlig svenska:** Om innehållet ska spelas i slumpmässig ordning. Gäller endast när innehållet börjar spelas direkt. Om det utelämnas avgör köns slumpinställning och innehållstypen.

**Bedömning:** Ingen ändring föreslås.

## 2182. `component::powerfox::exceptions::no_devices::message`

**Engelska:** No devices were found in the Powerfox account.

**Befintlig svenska:** Inga enheter hittades i Powerfox-kontot.

**Bedömning:** Ingen ändring föreslås.

## 2183. `component::powerfox::config::error::no_devices`

**Engelska:** No devices were found in this Powerfox account.

**Befintlig svenska:** Inga enheter hittades i det här Powerfox-kontot.

**Bedömning:** Ingen ändring föreslås.

## 2184. `component::ifttt::services::trigger::fields::target::name`

**Engelska:** Target

**Befintlig svenska:** Mål

**Bedömning:** Ingen ändring föreslås.

## 2185. `component::ifttt::services::trigger::fields::target::description`

**Engelska:** The names of the configured API keys to send the event to. Sends the event to all keys if this field is omitted.

**Befintlig svenska:** Namnen på de konfigurerade API-nycklar som händelsen ska skickas till. Händelsen skickas till alla nycklar om fältet utelämnas.

**Bedömning:** Ingen ändring föreslås.

## 2186. `component::chirpstack::config::error::tls_certificate_error`

**Engelska:** Unable to verify the server's TLS certificate. Check that it is trusted and matches the server address.

**Befintlig svenska:** Det går inte att verifiera serverns TLS-certifikat. Kontrollera att det är betrott och stämmer överens med serveradressen.

**Bedömning:** Ingen ändring föreslås.

## 2187. `component::chirpstack::config::error::http2_error`

**Engelska:** Unable to connect using HTTP/2. Check that the server and reverse proxy support gRPC.

**Befintlig svenska:** Det går inte att ansluta med HTTP/2. Kontrollera att servern och den omvända proxyn stöder gRPC.

**Bedömning:** Ingen ändring föreslås.

## 2188. `component::vicare::entity::sensor::heating_rod_runtime_level_two::name`

**Engelska:** Heating rod runtime level 2

**Befintlig svenska:** Drifttid för värmestav, nivå 2

**Bedömning:** Ingen ändring föreslås.

## 2189. `component::vicare::entity::sensor::heating_rod_runtime_level_one::name`

**Engelska:** Heating rod runtime level 1

**Befintlig svenska:** Drifttid för värmestav, nivå 1

**Bedömning:** Ingen ändring föreslås.

## 2190. `component::tuya::entity::switch::eco_mode::name`

**Engelska:** Eco mode

**Befintlig svenska:** Ekoläge

**Bedömning:** Ingen ändring föreslås.

## 2191. `component::accuweather::config::step::user::data_description::location`

**Engelska:** The location to get the weather data for. Defaults to the home location configured in Home Assistant.

**Befintlig svenska:** Platsen som väderdata ska hämtas för. Standardvärdet är hemplatsen som är konfigurerad i Home Assistant.

**Bedömning:** Ingen ändring föreslås.

## 2192. `component::system_bridge::exceptions::waiting_for_sleep::message`

**Engelska:** Waiting for {title} to sleep or shut down

**Befintlig svenska:** Väntar på att {title} ska försättas i vila eller stängas av

**Bedömning:** Ingen ändring föreslås.

## 2193. `component::system_bridge::exceptions::connection_lost::message`

**Engelska:** Connection lost while registering for {title}

**Befintlig svenska:** Anslutningen bröts när {title} registrerades

**Bedömning:** Ingen ändring föreslås.

## 2194. `component::shelly::entity::sensor::humidity_level_with_channel_name::state::very_high`

**Engelska:** [%key:common::state::very_high%]

**Befintlig svenska:** Mycket hög

**Kontextkontroll:** Kontrollera referensmålet `common::state::very_high`; det ingår ännu inte i det insamlade underlaget.

## 2195. `component::shelly::entity::sensor::humidity_level_with_channel_name::state::medium`

**Engelska:** [%key:common::state::medium%]

**Befintlig svenska:** Medel

**Kontextkontroll:** Kontrollera referensmålet `common::state::medium`; det ingår ännu inte i det insamlade underlaget.

## 2196. `component::shelly::entity::sensor::humidity_level_with_channel_name::state::low`

**Engelska:** [%key:common::state::low%]

**Befintlig svenska:** Låg

**Kontextkontroll:** Kontrollera referensmålet `common::state::low`; det ingår ännu inte i det insamlade underlaget.

## 2197. `component::shelly::entity::sensor::humidity_level_with_channel_name::state::high`

**Engelska:** [%key:common::state::high%]

**Befintlig svenska:** Hög

**Kontextkontroll:** Kontrollera referensmålet `common::state::high`; det ingår ännu inte i det insamlade underlaget.

## 2198. `component::shelly::entity::sensor::humidity_level_with_channel_name::name`

**Engelska:** {channel_name} humidity level

**Befintlig svenska:** {channel_name}: fuktnivå

**Förslag:** {channel_name}: luftfuktighetsnivå

## 2199. `component::shelly::entity::sensor::humidity_level::state::very_high`

**Engelska:** [%key:common::state::very_high%]

**Befintlig svenska:** Mycket hög

**Kontextkontroll:** Kontrollera referensmålet `common::state::very_high`; det ingår ännu inte i det insamlade underlaget.

## 2200. `component::shelly::entity::sensor::humidity_level::state::medium`

**Engelska:** [%key:common::state::medium%]

**Befintlig svenska:** Medel

**Kontextkontroll:** Kontrollera referensmålet `common::state::medium`; det ingår ännu inte i det insamlade underlaget.

## 2201. `component::shelly::entity::sensor::humidity_level::state::low`

**Engelska:** [%key:common::state::low%]

**Befintlig svenska:** Låg

**Kontextkontroll:** Kontrollera referensmålet `common::state::low`; det ingår ännu inte i det insamlade underlaget.

## 2202. `component::shelly::entity::sensor::humidity_level::state::high`

**Engelska:** [%key:common::state::high%]

**Befintlig svenska:** Hög

**Kontextkontroll:** Kontrollera referensmålet `common::state::high`; det ingår ännu inte i det insamlade underlaget.

## 2203. `component::shelly::entity::sensor::humidity_level::name`

**Engelska:** Humidity level

**Befintlig svenska:** Fuktnivå

**Förslag:** Luftfuktighetsnivå

## 2204. `component::e3dc::entity::sensor::sg_ready_status::state::switch_on_recommended`

**Engelska:** Switch-on recommended

**Befintlig svenska:** Aktivering rekommenderas

**Bedömning:** Ingen ändring föreslås.

## 2205. `component::e3dc::entity::sensor::sg_ready_status::state::normal`

**Engelska:** Normal operation

**Befintlig svenska:** Normal drift

**Bedömning:** Ingen ändring föreslås.

## 2206. `component::e3dc::entity::sensor::sg_ready_status::state::forced_on`

**Engelska:** Forced on

**Befintlig svenska:** Tvångsaktiverad

**Bedömning:** Ingen ändring föreslås.

## 2207. `component::e3dc::entity::sensor::sg_ready_status::state::blocked`

**Engelska:** Blocked

**Befintlig svenska:** Blockerad

**Bedömning:** Ingen ändring föreslås.

## 2208. `component::e3dc::entity::sensor::sg_ready_status::name`

**Engelska:** SG Ready status

**Befintlig svenska:** SG Ready-status

**Bedömning:** Ingen ändring föreslås.

## 2209. `component::e3dc::entity::sensor::reactive_power_failsafe_timeout::name`

**Engelska:** Reactive power failsafe timeout

**Befintlig svenska:** Tidsgräns för felsäker reaktiv effekt

**Bedömning:** Ingen ändring föreslås.

## 2210. `component::e3dc::entity::sensor::max_discharge_power::name`

**Engelska:** Maximum discharge power

**Befintlig svenska:** Maximal urladdningseffekt

**Bedömning:** Ingen ändring föreslås.

## 2211. `component::e3dc::entity::sensor::max_charge_power::name`

**Engelska:** Maximum charge power

**Befintlig svenska:** Maximal laddningseffekt

**Bedömning:** Ingen ändring föreslås.

## 2212. `component::e3dc::entity::sensor::inverter_mode::state::normal`

**Engelska:** Normal operation

**Befintlig svenska:** Normal drift

**Bedömning:** Ingen ändring föreslås.

## 2213. `component::e3dc::entity::sensor::inverter_mode::state::idle_off_grid_power_save`

**Engelska:** Idle, off-grid power save

**Befintlig svenska:** Viloläge, energisparläge utan elnät

**Bedömning:** Ingen ändring föreslås.

## 2214. `component::e3dc::entity::sensor::inverter_mode::name`

**Engelska:** Inverter mode

**Befintlig svenska:** Växelriktarläge

**Bedömning:** Ingen ändring föreslås.

## 2215. `component::e3dc::entity::sensor::full_charge_energy::name`

**Engelska:** Battery capacity

**Befintlig svenska:** Batterikapacitet

**Bedömning:** Ingen ändring föreslås.

## 2216. `component::e3dc::entity::sensor::active_power_failsafe_timeout::name`

**Engelska:** Active power failsafe timeout

**Befintlig svenska:** Tidsgräns för felsäker aktiv effekt

**Bedömning:** Ingen ändring föreslås.

## 2217. `component::shelly::entity::sensor::illuminance_level_with_channel_name::state::twilight`

**Engelska:** [%key:component::shelly::entity::sensor::illuminance_level::state::twilight%]

**Befintlig svenska:** Skymning

**Kontextkontroll:** Kontrollera referensmålet `component::shelly::entity::sensor::illuminance_level::state::twilight`; det ingår ännu inte i det insamlade underlaget.

## 2218. `component::shelly::entity::sensor::illuminance_level_with_channel_name::state::dark`

**Engelska:** [%key:component::shelly::entity::sensor::illuminance_level::state::dark%]

**Befintlig svenska:** Mörkt

**Kontextkontroll:** Kontrollera referensmålet `component::shelly::entity::sensor::illuminance_level::state::dark`; det ingår ännu inte i det insamlade underlaget.

## 2219. `component::shelly::entity::sensor::illuminance_level_with_channel_name::state::bright`

**Engelska:** [%key:component::shelly::entity::sensor::illuminance_level::state::bright%]

**Befintlig svenska:** Ljust

**Kontextkontroll:** Kontrollera referensmålet `component::shelly::entity::sensor::illuminance_level::state::bright`; det ingår ännu inte i det insamlade underlaget.

## 2220. `component::shelly::entity::sensor::illuminance_level_with_channel_name::name`

**Engelska:** {channel_name} illuminance level

**Befintlig svenska:** {channel_name}: belysningsnivå

**Bedömning:** Ingen ändring föreslås.
