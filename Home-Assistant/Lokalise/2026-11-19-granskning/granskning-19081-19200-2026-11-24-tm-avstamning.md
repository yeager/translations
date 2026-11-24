# Home Assistant Core – historisk avstämning 19081–19200

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 41 direkta källtexter matchar HA Core-källan; 30 referensanvändningar med 17 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 49 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 19081 | 844252133 | `component::fumis::entity::sensor::alert::state::door_open` | Door open | Dörr öppen | Core-literal match |
| 19082 | 844252132 | `component::fumis::entity::sensor::alert::state::airflow_malfunction` | Airflow sensor malfunction | Fel på luftflödessensorn | Core-literal match |
| 19083 | 844252131 | `component::fumis::entity::sensor::alert::name` | Alert | Varning | Core-literal match |
| 19084 | 844240004 | `component::fumis::entity::number::power_level::name` | Power level | Effektnivå | Core-literal match |
| 19085 | 844240003 | `component::fumis::entity::number::fan_speed::name` | Fan speed | Fläkthastighet | Core-literal match |
| 19086 | 844152846 | `component::iaqualink::config::step::reconfigure::title` | Reconnect iAquaLink | Återanslut iAquaLink | Core-literal match |
| 19087 | 844152845 | `component::iaqualink::config::step::reconfigure::description` | Please enter the username and password for your iAquaLink account. | Ange användarnamn och lösenord för ditt iAquaLink-konto. | Shared reference target checked |
| 19088 | 844152844 | `component::iaqualink::config::step::reconfigure::data_description::username` | The email address used to sign in to your account using the iAquaLink app or website. | E-postadressen som används för att logga in på ditt konto med iAquaLink-appen eller webbplatsen. | Shared reference target checked |
| 19089 | 844152843 | `component::iaqualink::config::step::reconfigure::data_description::password` | The password associated with your account. | Lösenordet som är kopplat till ditt konto. | Shared reference target checked |
| 19090 | 844152842 | `component::iaqualink::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 19091 | 844152841 | `component::iaqualink::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 19092 | 844152840 | `component::iaqualink::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 19093 | 844152516 | `component::fritz::issues::deprecated_firmware_update_button::title` | 'Firmware update' button is deprecated | Knappen "Uppdatering av firmware" är föråldrad | Source-path follow-up open |
| 19094 | 844152515 | `component::fritz::issues::deprecated_firmware_update_button::description` | The 'Firmware update' button is deprecated and will be removed in Home Assistant Core {removal_version}. It has been superseded by an update entity. Please update your automations and dashboards to remove any usage of this button. | Knappen ”Firmware-uppdatering” är föråldrad och kommer att tas bort i Home Assistant Core {removal_version}. Den har ersatts av en uppdateringsentitet. Uppdatera dina automatiseringar och kontrollpaneler för att ta bort all användning av denna knapp. | Source-path follow-up open |
| 19095 | 844026042 | `component::unifi::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 19096 | 844021135 | `component::novy_cooker_hood::selector::code::options::9` | Code 9 | Kod 9 | Core-literal match |
| 19097 | 844021134 | `component::novy_cooker_hood::selector::code::options::8` | Code 8 | Kod 8 | Core-literal match |
| 19098 | 844021133 | `component::novy_cooker_hood::selector::code::options::7` | Code 7 | Kod 7 | Core-literal match |
| 19099 | 844021132 | `component::novy_cooker_hood::selector::code::options::6` | Code 6 | Kod 6 | Core-literal match |
| 19100 | 844021131 | `component::novy_cooker_hood::selector::code::options::5` | Code 5 | Kod 5 | Core-literal match |
| 19101 | 844021130 | `component::novy_cooker_hood::selector::code::options::4` | Code 4 | Kod 4 | Core-literal match |
| 19102 | 844021129 | `component::novy_cooker_hood::selector::code::options::3` | Code 3 | Kod 3 | Core-literal match |
| 19103 | 844021128 | `component::novy_cooker_hood::selector::code::options::2` | Code 2 | Kod 2 | Core-literal match |
| 19104 | 844021127 | `component::novy_cooker_hood::selector::code::options::10` | Code 10 | Kod 10 | Core-literal match |
| 19105 | 844021126 | `component::novy_cooker_hood::selector::code::options::1` | Code 1 | Kod 1 | Core-literal match |
| 19106 | 844021125 | `component::novy_cooker_hood::entity::light::light::name` | Light | Lampa | Shared reference target checked |
| 19107 | 844021124 | `component::novy_cooker_hood::config::step::user::description` | After you submit, Home Assistant will toggle the hood light on and off to verify the code works. | Efter att du bekräftat så kommer home assistant att tända och släcka fläktens lampa för att verifiera att koden fungerar. | Core-literal match |
| 19108 | 844021123 | `component::novy_cooker_hood::config::step::user::data_description::transmitter` | The radio frequency transmitter to use for sending commands. | Den radiofrekvenssändare som ska användas för att skicka kommandon. | Shared reference target checked |
| 19109 | 844021122 | `component::novy_cooker_hood::config::step::user::data_description::code` | The code your hood is paired with (1-10). Code 1 is the factory default. | Koden som din fläkt är parad med (1-10). Kod 1 är fabriksinställning. | Core-literal match |
| 19110 | 844021121 | `component::novy_cooker_hood::config::step::user::data::transmitter` | Radio frequency transmitter | Sändare för radiofrekvens | Shared reference target checked |
| 19111 | 844021120 | `component::novy_cooker_hood::config::step::user::data::code` | Code | Kod | Core-literal match |
| 19112 | 844021119 | `component::novy_cooker_hood::config::step::test_light::title` | Verify the code | Verifiera kod | Core-literal match |
| 19113 | 844021118 | `component::novy_cooker_hood::config::step::test_light::menu_options::retry` | Retry | Försök igen | Core-literal match |
| 19114 | 844021117 | `component::novy_cooker_hood::config::step::test_light::menu_options::finish` | Finish | Slutför | Core-literal match |
| 19115 | 844021116 | `component::novy_cooker_hood::config::step::test_light::description` | Toggled the hood light on and off using code {code}. Did you see it react? Press Finish to save, or Retry to pick a different code. | Tände och släckte huvens lampa med hjälp av kod {code}. Såg du att den reagerade? Tryck på "Slutför" för att spara eller "Försök igen" för att välja en annan kod. | Core-literal match |
| 19116 | 844021115 | `component::novy_cooker_hood::config::step::test_failed::title` | Test failed | Test misslyckades | Core-literal match |
| 19117 | 844021114 | `component::novy_cooker_hood::config::step::test_failed::menu_options::retry` | Retry | Försök igen | Core-literal match |
| 19118 | 844021113 | `component::novy_cooker_hood::config::step::test_failed::description` | Could not send the test command for code {code}. Check that your radio frequency transmitter is online, then press Retry. | Det gick inte att skicka testkommandot för kod {code}. Kontrollera att din radiosändare är ansluten och tryck sedan på ”Försök igen”. | Core-literal match |
| 19119 | 844021112 | `component::novy_cooker_hood::config::abort::no_transmitters` | No radio frequency transmitters are available. Please set up a device first. | Inga radiofrekvenssändare finns tillgängliga. Vänligen installera en enhet först. | Shared reference target checked |
| 19120 | 844021111 | `component::novy_cooker_hood::config::abort::no_compatible_transmitters` | No radio frequency transmitter supports {frequency} {modulation} transmissions. Please add a compatible transmitter first. | Ingen radiofrekvenssändare stöder {frequency} {modulation}-sändningar. Lägg först till en kompatibel sändare. | Shared reference target checked |
| 19121 | 844021110 | `component::novy_cooker_hood::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 19122 | 844007322 | `component::zinvolt::entity::select::battery_mode::state::self_use` | Self-use | Egenanvändning | Core-literal match |
| 19123 | 844007321 | `component::zinvolt::entity::select::battery_mode::state::idle` | Idle | Inaktiv | Source-path follow-up open |
| 19124 | 844007320 | `component::zinvolt::entity::select::battery_mode::state::fast_discharge` | Fast discharge | Snabb urladdning | Core-literal match |
| 19125 | 844007319 | `component::zinvolt::entity::select::battery_mode::state::fast_charge` | Fast charge | Snabb laddning | Core-literal match |
| 19126 | 844007318 | `component::zinvolt::entity::select::battery_mode::state::dynamic` | Dynamic | Dynamisk | Core-literal match |
| 19127 | 844007317 | `component::zinvolt::entity::select::battery_mode::state::charged` | Charged | Laddad | Source-path follow-up open |
| 19128 | 844007316 | `component::zinvolt::entity::select::battery_mode::name` | Mode | Läge | Core-literal match |
| 19129 | 844006887 | `component::window::conditions::is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19130 | 844006886 | `component::window::conditions::is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19131 | 844006885 | `component::window::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19132 | 844006884 | `component::gate::conditions::is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19133 | 844006883 | `component::gate::conditions::is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19134 | 844006882 | `component::gate::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19135 | 844006881 | `component::garage_door::conditions::is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19136 | 844006880 | `component::garage_door::conditions::is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19137 | 844006879 | `component::garage_door::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19138 | 844006878 | `component::door::conditions::is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19139 | 844006877 | `component::door::conditions::is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19140 | 844006876 | `component::door::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19141 | 844006875 | `component::cover::conditions::shutter_is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19142 | 844006874 | `component::cover::conditions::shutter_is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19143 | 844006873 | `component::cover::conditions::shade_is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19144 | 844006872 | `component::cover::conditions::shade_is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19145 | 844006871 | `component::cover::conditions::curtain_is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19146 | 844006870 | `component::cover::conditions::curtain_is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19147 | 844006869 | `component::cover::conditions::blind_is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19148 | 844006868 | `component::cover::conditions::blind_is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19149 | 844006867 | `component::cover::conditions::awning_is_open::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19150 | 844006866 | `component::cover::conditions::awning_is_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 19151 | 844006865 | `component::cover::common::condition_for_name` | For at least | I minst | Core-literal match |
| 19152 | 843972383 | `component::matter::entity::button::temporary_mute_request::name` | Temporary mute | Tillfällig ljudavstängning | Core-literal match |
| 19153 | 843969857 | `component::unifiprotect::exceptions::relay_not_available::message` | Relay is no longer available | Reläet är inte längre tillgängligt | Core-literal match |
| 19154 | 843969856 | `component::unifiprotect::entity::switch::relay_output::name` | Output {output_name} | Utgång {output_name} | Core-literal match |
| 19155 | 843931833 | `component::unifiprotect::exceptions::siren_not_available::message` | Siren is no longer available | Sirenen är inte längre tillgänglig | Core-literal match |
| 19156 | 843931832 | `component::unifiprotect::exceptions::siren_invalid_duration::message` | Invalid siren duration {duration}s. Valid values are: {valid} seconds | Ogiltig sirenvaraktighet: {duration} sekunder. Giltiga värden är: {valid} sekunder | Core-literal match |
| 19157 | 843809065 | `component::template::selector::number_device_class::options::wind_speed` | Wind speed | Vindhastighet | Source-path follow-up open |
| 19158 | 843809064 | `component::template::selector::number_device_class::options::wind_direction` | Wind direction | Vindriktning | Source-path follow-up open |
| 19159 | 843809063 | `component::template::selector::number_device_class::options::weight` | Weight | Vikt | Source-path follow-up open |
| 19160 | 843809062 | `component::template::selector::number_device_class::options::water` | Water | Vatten | Source-path follow-up open |
| 19161 | 843809061 | `component::template::selector::number_device_class::options::volume_storage` | Stored volume | Lagrad volym | Source-path follow-up open |
| 19162 | 843809060 | `component::template::selector::number_device_class::options::volume_flow_rate` | Volume flow rate | Flödeshastighet | Source-path follow-up open |
| 19163 | 843809059 | `component::template::selector::number_device_class::options::volume` | Volume | Volym | Source-path follow-up open |
| 19164 | 843809058 | `component::template::selector::number_device_class::options::voltage` | Voltage | Spänning | Source-path follow-up open |
| 19165 | 843809057 | `component::template::selector::number_device_class::options::volatile_organic_compounds` | Volatile organic compounds | Flyktiga organiska föreningar (VOC) | Source-path follow-up open |
| 19166 | 843809056 | `component::template::selector::number_device_class::options::temperature_delta` | Temperature delta | Temperatur delta | Source-path follow-up open |
| 19167 | 843809055 | `component::template::selector::number_device_class::options::temperature` | Temperature | Temperatur | Source-path follow-up open |
| 19168 | 843809054 | `component::template::selector::number_device_class::options::sulphur_dioxide` | Sulphur dioxide | Svaveldioxid | Source-path follow-up open |
| 19169 | 843809053 | `component::template::selector::number_device_class::options::speed` | Speed | Hastighet | Source-path follow-up open |
| 19170 | 843809052 | `component::template::selector::number_device_class::options::sound_pressure` | Sound pressure | Ljudtryck | Source-path follow-up open |
| 19171 | 843809051 | `component::template::selector::number_device_class::options::signal_strength` | Signal strength | Signalstyrka | Source-path follow-up open |
| 19172 | 843809050 | `component::template::selector::number_device_class::options::reactive_power` | Reactive power | Reaktiv effekt | Source-path follow-up open |
| 19173 | 843809049 | `component::template::selector::number_device_class::options::reactive_energy` | Reactive energy | Reaktiv energi | Source-path follow-up open |
| 19174 | 843809048 | `component::template::selector::number_device_class::options::pressure` | Pressure | Tryck | Source-path follow-up open |
| 19175 | 843809047 | `component::template::selector::number_device_class::options::precipitation_intensity` | Precipitation intensity | Nederbördsintensitet | Source-path follow-up open |
| 19176 | 843809046 | `component::template::selector::number_device_class::options::precipitation` | Precipitation | Nederbörd | Source-path follow-up open |
| 19177 | 843809045 | `component::template::selector::number_device_class::options::power_factor` | Power factor | Effektfaktor | Source-path follow-up open |
| 19178 | 843809044 | `component::template::selector::number_device_class::options::power` | Power | Effekt | Source-path follow-up open |
| 19179 | 843809043 | `component::template::selector::number_device_class::options::pm4` | PM4 | PM4 | Source-path follow-up open |
| 19180 | 843809042 | `component::template::selector::number_device_class::options::pm25` | PM2.5 | PM2,5 | Source-path follow-up open |
| 19181 | 843809041 | `component::template::selector::number_device_class::options::pm10` | PM10 | PM10 | Source-path follow-up open |
| 19182 | 843809040 | `component::template::selector::number_device_class::options::pm1` | PM1 | PM1 | Source-path follow-up open |
| 19183 | 843809039 | `component::template::selector::number_device_class::options::ph` | pH | pH | Source-path follow-up open |
| 19184 | 843809038 | `component::template::selector::number_device_class::options::ozone` | Ozone | Ozon | Source-path follow-up open |
| 19185 | 843809037 | `component::template::selector::number_device_class::options::nitrous_oxide` | Nitrous oxide | Lustgas | Source-path follow-up open |
| 19186 | 843809036 | `component::template::selector::number_device_class::options::nitrogen_monoxide` | Nitrogen monoxide | Kväveoxid | Source-path follow-up open |
| 19187 | 843809035 | `component::template::selector::number_device_class::options::nitrogen_dioxide` | Nitrogen dioxide | Kvävedioxid | Source-path follow-up open |
| 19188 | 843809034 | `component::template::selector::number_device_class::options::moisture` | Moisture | Fukt | Source-path follow-up open |
| 19189 | 843809033 | `component::template::selector::number_device_class::options::irradiance` | Irradiance | Instrålning | Source-path follow-up open |
| 19190 | 843809032 | `component::template::selector::number_device_class::options::illuminance` | Illuminance | Belysningsstyrka | Source-path follow-up open |
| 19191 | 843809031 | `component::template::selector::number_device_class::options::humidity` | Humidity | Luftfuktighet | Source-path follow-up open |
| 19192 | 843809030 | `component::template::selector::number_device_class::options::gas` | Gas | Gas | Source-path follow-up open |
| 19193 | 843809029 | `component::template::selector::number_device_class::options::frequency` | Frequency | Frekvens | Source-path follow-up open |
| 19194 | 843809028 | `component::template::selector::number_device_class::options::energy_storage` | Stored energy | Lagrad energi | Source-path follow-up open |
| 19195 | 843809027 | `component::template::selector::number_device_class::options::energy` | Energy | Energi | Source-path follow-up open |
| 19196 | 843809026 | `component::template::selector::number_device_class::options::distance` | Distance | Avstånd | Source-path follow-up open |
| 19197 | 843809025 | `component::template::selector::number_device_class::options::data_rate` | Data rate | Datahastighet | Source-path follow-up open |
| 19198 | 843809024 | `component::template::selector::number_device_class::options::current` | Current | Ström | Source-path follow-up open |
| 19199 | 843809023 | `component::template::selector::number_device_class::options::conductivity` | Conductivity | Ledningsförmåga | Source-path follow-up open |
| 19200 | 843809022 | `component::template::selector::number_device_class::options::carbon_monoxide` | Carbon monoxide | Kolmonoxid | Source-path follow-up open |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 844152840 | `component::iaqualink::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 844152516 | `component::fritz::issues::deprecated_firmware_update_button::title` | 'Firmware update' button is deprecated |
| 844152515 | `component::fritz::issues::deprecated_firmware_update_button::description` | The 'Firmware update' button is deprecated and will be removed in Home Assistant Core {removal_version}. It has been superseded by an update entity. Please update your automations and dashboards to remove any usage of this button. |
| 844007321 | `component::zinvolt::entity::select::battery_mode::state::idle` | Idle |
| 844007317 | `component::zinvolt::entity::select::battery_mode::state::charged` | Charged |
| 843809065 | `component::template::selector::number_device_class::options::wind_speed` | Wind speed |
| 843809064 | `component::template::selector::number_device_class::options::wind_direction` | Wind direction |
| 843809063 | `component::template::selector::number_device_class::options::weight` | Weight |
| 843809062 | `component::template::selector::number_device_class::options::water` | Water |
| 843809061 | `component::template::selector::number_device_class::options::volume_storage` | Stored volume |
| 843809060 | `component::template::selector::number_device_class::options::volume_flow_rate` | Volume flow rate |
| 843809059 | `component::template::selector::number_device_class::options::volume` | Volume |
| 843809058 | `component::template::selector::number_device_class::options::voltage` | Voltage |
| 843809057 | `component::template::selector::number_device_class::options::volatile_organic_compounds` | Volatile organic compounds |
| 843809056 | `component::template::selector::number_device_class::options::temperature_delta` | Temperature delta |
| 843809055 | `component::template::selector::number_device_class::options::temperature` | Temperature |
| 843809054 | `component::template::selector::number_device_class::options::sulphur_dioxide` | Sulphur dioxide |
| 843809053 | `component::template::selector::number_device_class::options::speed` | Speed |
| 843809052 | `component::template::selector::number_device_class::options::sound_pressure` | Sound pressure |
| 843809051 | `component::template::selector::number_device_class::options::signal_strength` | Signal strength |
| 843809050 | `component::template::selector::number_device_class::options::reactive_power` | Reactive power |
| 843809049 | `component::template::selector::number_device_class::options::reactive_energy` | Reactive energy |
| 843809048 | `component::template::selector::number_device_class::options::pressure` | Pressure |
| 843809047 | `component::template::selector::number_device_class::options::precipitation_intensity` | Precipitation intensity |
| 843809046 | `component::template::selector::number_device_class::options::precipitation` | Precipitation |
| 843809045 | `component::template::selector::number_device_class::options::power_factor` | Power factor |
| 843809044 | `component::template::selector::number_device_class::options::power` | Power |
| 843809043 | `component::template::selector::number_device_class::options::pm4` | PM4 |
| 843809042 | `component::template::selector::number_device_class::options::pm25` | PM2.5 |
| 843809041 | `component::template::selector::number_device_class::options::pm10` | PM10 |
| 843809040 | `component::template::selector::number_device_class::options::pm1` | PM1 |
| 843809039 | `component::template::selector::number_device_class::options::ph` | pH |
| 843809038 | `component::template::selector::number_device_class::options::ozone` | Ozone |
| 843809037 | `component::template::selector::number_device_class::options::nitrous_oxide` | Nitrous oxide |
| 843809036 | `component::template::selector::number_device_class::options::nitrogen_monoxide` | Nitrogen monoxide |
| 843809035 | `component::template::selector::number_device_class::options::nitrogen_dioxide` | Nitrogen dioxide |
| 843809034 | `component::template::selector::number_device_class::options::moisture` | Moisture |
| 843809033 | `component::template::selector::number_device_class::options::irradiance` | Irradiance |
| 843809032 | `component::template::selector::number_device_class::options::illuminance` | Illuminance |
| 843809031 | `component::template::selector::number_device_class::options::humidity` | Humidity |
| 843809030 | `component::template::selector::number_device_class::options::gas` | Gas |
| 843809029 | `component::template::selector::number_device_class::options::frequency` | Frequency |
| 843809028 | `component::template::selector::number_device_class::options::energy_storage` | Stored energy |
| 843809027 | `component::template::selector::number_device_class::options::energy` | Energy |
| 843809026 | `component::template::selector::number_device_class::options::distance` | Distance |
| 843809025 | `component::template::selector::number_device_class::options::data_rate` | Data rate |
| 843809024 | `component::template::selector::number_device_class::options::current` | Current |
| 843809023 | `component::template::selector::number_device_class::options::conductivity` | Conductivity |
| 843809022 | `component::template::selector::number_device_class::options::carbon_monoxide` | Carbon monoxide |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
