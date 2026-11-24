# Home Assistant Core – historisk avstämning 16321–16440

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 80 direkta källtexter matchar HA Core-källan; 24 referensanvändningar med 16 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 16 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16321 | 876549957 | `component::edifier_infrared::entity::button::coax::name` | Coaxial | Coaxial | Core-literal match |
| 16322 | 876549956 | `component::edifier_infrared::entity::button::bluetooth::name` | Bluetooth | Bluetooth | Core-literal match |
| 16323 | 876549955 | `component::edifier_infrared::entity::button::aux::name` | AUX | AUX | Core-literal match |
| 16324 | 876293920 | `component::homeassistant::issues::deprecated_trigger_behavior::title` | Deprecated trigger behavior option in use | Föråldrat alternativ för utlösarbeteende används | Core-literal match |
| 16325 | 876293919 | `component::homeassistant::issues::deprecated_trigger_behavior::description` | An automation, script or template entity uses the trigger behavior option `{deprecated_behavior}`, which has been renamed to `{new_behavior}`. The old value still works for now, but support for it will be removed in a future release.<br><br>To fix this issue, open each affected automation or script in the editor and save it again; Home Assistant will automatically detect and update the deprecated option. Alternatively, edit your configuration files (for example `automations.yaml`) directly and change `behavior: {deprecated_behavior}` to `behavior: {new_behavior}` in the options of your triggers. Leave the `behavior` option of conditions unchanged, as conditions still use `any` and `all`. Restart Home Assistant afterwards. | En automatisering, ett skript eller en mall använder utlösarbeteendet `{deprecated_behavior}`, som har bytt namn till `{new_behavior}`. Det gamla värdet fungerar fortfarande för tillfället, men stödet för det kommer att tas bort i en framtida version.<br><br>För att åtgärda detta problem öppnar du varje berörd automatisering och/eller skript i redigeraren och sparar det på nytt. Home Assistant kommer automatiskt att upptäcka och uppdatera det utfasade alternativet. Alternativt kan du redigera dina konfigurationsfiler (till exempel `automations.yaml`) direkt och ändra `behavior: {deprecated_behavior}` till `behavior: {new_behavior}`. Starta sedan om Home Assistant. | Core-literal match |
| 16326 | 876293715 | `component::radio_frequency::entity_component::_::name` | Radio frequency transmitter | Sändare för radiofrekvens | Source-path follow-up open |
| 16327 | 876283841 | `component::duco::entity::select::ventilation_state::state::man3x3` | MAN3x3 | MAN3x3 | Core-literal match |
| 16328 | 876283840 | `component::duco::entity::select::ventilation_state::state::man3x2` | MAN3x2 | MAN3x2 | Core-literal match |
| 16329 | 876283839 | `component::duco::entity::select::ventilation_state::state::man3` | MAN3 | MAN3 | Core-literal match |
| 16330 | 876283838 | `component::duco::entity::select::ventilation_state::state::man2x3` | MAN2x3 | MAN2x3 | Core-literal match |
| 16331 | 876283837 | `component::duco::entity::select::ventilation_state::state::man2x2` | MAN2x2 | MAN2x2 | Core-literal match |
| 16332 | 876283836 | `component::duco::entity::select::ventilation_state::state::man2` | MAN2 | MAN2 | Core-literal match |
| 16333 | 876283835 | `component::duco::entity::select::ventilation_state::state::man1x3` | MAN1x3 | MAN1x3 | Core-literal match |
| 16334 | 876283834 | `component::duco::entity::select::ventilation_state::state::man1x2` | MAN1x2 | MAN1x2 | Core-literal match |
| 16335 | 876283833 | `component::duco::entity::select::ventilation_state::state::man1` | MAN1 | MAN1 | Core-literal match |
| 16336 | 876283832 | `component::duco::entity::select::ventilation_state::state::empt` | EMPT | EMPT | Core-literal match |
| 16337 | 876283831 | `component::duco::entity::select::ventilation_state::state::cnt3` | CNT3 | CNT3 | Core-literal match |
| 16338 | 876283830 | `component::duco::entity::select::ventilation_state::state::cnt2` | CNT2 | CNT2 | Core-literal match |
| 16339 | 876283829 | `component::duco::entity::select::ventilation_state::state::cnt1` | CNT1 | CNT1 | Core-literal match |
| 16340 | 876283828 | `component::duco::entity::select::ventilation_state::state::auto` | AUTO | AUTO | Core-literal match |
| 16341 | 876283827 | `component::duco::entity::select::ventilation_state::state::aut3` | AUT3 | AUT3 | Core-literal match |
| 16342 | 876283826 | `component::duco::entity::select::ventilation_state::state::aut2` | AUT2 | AUT2 | Core-literal match |
| 16343 | 876283825 | `component::duco::entity::select::ventilation_state::state::aut1` | AUT1 | AUT1 | Core-literal match |
| 16344 | 876283824 | `component::duco::entity::select::ventilation_state::name` | Ventilation state | Ventilationsläge | Core-literal match |
| 16345 | 876113712 | `component::raspberry_pi::exceptions::supervisor_not_ready::message` | Supervisor is not ready | Supervisor är inte redo | Core-literal match |
| 16346 | 876113711 | `component::raspberry_pi::entity::update::rpi_firmware::name` | Firmware | Firmware | Core-literal match |
| 16347 | 876113710 | `component::homeassistant_yellow::entity::update::rpi_firmware::name` | Firmware | Firmware | Core-literal match |
| 16348 | 876055431 | `component::rpi_power::exceptions::under_voltage_not_supported::message` | Under-voltage monitoring is not supported on this device. | Övervakning av underspänning stöds inte på den här enheten. | Core-literal match |
| 16349 | 876055430 | `component::rpi_power::entity::binary_sensor::rpi_power::name` | Power status | Strömstatus | Core-literal match |
| 16350 | 875775467 | `component::smtp::config::step::reauth_confirm::title` | Re-authenticate SMTP | Återautentisera SMTP | Core-literal match |
| 16351 | 875775466 | `component::smtp::config::step::reauth_confirm::data_description::username` | Username used to authenticate with the SMTP server. | Användarnamn som används för att autentisera sig hos SMTP-servern. | Shared reference target checked |
| 16352 | 875775465 | `component::smtp::config::step::reauth_confirm::data_description::password` | Password or app-specific password for the SMTP account. | Lösenord eller appspecifikt lösenord för SMTP-kontot. | Shared reference target checked |
| 16353 | 875775464 | `component::smtp::config::step::reauth_confirm::data::username` | Username | Användarnamn | Shared reference target checked |
| 16354 | 875775463 | `component::smtp::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 16355 | 875775462 | `component::smtp::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16356 | 875759482 | `component::wmspro::entity::number::rotation-raw::name` | Raw rotation | Rå rotation | Core-literal match |
| 16357 | 875759481 | `component::wmspro::entity::number::rotation-min::name` | Minimum rotation | Minsta rotation | Core-literal match |
| 16358 | 875759480 | `component::wmspro::entity::number::rotation-max::name` | Maximum rotation | Maximal rotation | Core-literal match |
| 16359 | 875759479 | `component::wmspro::entity::number::rotation::name` | Rotation | Rotation | Core-literal match |
| 16360 | 875759478 | `component::wmspro::entity::cover::valance::name` | Valance | Kappa | Core-literal match |
| 16361 | 875759477 | `component::wmspro::entity::button::rotation-reset::name` | Reset rotation | Återställ rotation | Core-literal match |
| 16362 | 875591796 | `component::rabbitair::entity::sensor::air_quality::state::medium` | Medium | Medel | Shared reference target checked |
| 16363 | 875591795 | `component::rabbitair::entity::sensor::air_quality::state::lowest` | Lowest | Lägsta | Core-literal match |
| 16364 | 875591794 | `component::rabbitair::entity::sensor::air_quality::state::low` | Low | Låg | Shared reference target checked |
| 16365 | 875591793 | `component::rabbitair::entity::sensor::air_quality::state::highest` | Highest | Högsta | Core-literal match |
| 16366 | 875591792 | `component::rabbitair::entity::sensor::air_quality::state::high` | High | Hög | Shared reference target checked |
| 16367 | 875591791 | `component::rabbitair::entity::sensor::air_quality::name` | Air quality | Luftkvalitet | Core-literal match |
| 16368 | 875368074 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::name` | Other text entity settings | Andra inställningar för textentiteter | Core-literal match |
| 16369 | 875368073 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data_description::pattern` | A valid regex pattern | Ett giltigt regex-mönster | Core-literal match |
| 16370 | 875368072 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data_description::mode` | Mode of the text input | Läge för textinmatning | Core-literal match |
| 16371 | 875368071 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data_description::min` | Minimum length of the text input | Minsta längd på den inmatade texten | Core-literal match |
| 16372 | 875368070 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data_description::max` | Maximum length of the text input | Maximal längd på den inmatade texten | Core-literal match |
| 16373 | 875368069 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data::pattern` | Pattern | Mönster | Core-literal match |
| 16374 | 875368068 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data::mode` | Mode | Läge | Core-literal match |
| 16375 | 875368067 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data::min` | Minimum length | Minsta längd | Core-literal match |
| 16376 | 875368066 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::text_other_settings::data::max` | Maximum length | Maximal längd | Core-literal match |
| 16377 | 875368065 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::siren_other_settings::name` | Other siren settings | Övriga sireninställningar | Core-literal match |
| 16378 | 875368064 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::siren_other_settings::data_description::command_off_template` | The [template]({command_templating_url}) for "off" state changes. By default the "[Command template]({url}#command_template)" will be used. [Learn more.]({url}#command_off_template) | [Mallen]({command_templating_url}) för när tillståndet "av" ändras. Som standard används "[Kommandomall]({url}#command_template)". [Läs mer.]({url}#command_off_template) | Core-literal match |
| 16379 | 875368063 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::siren_other_settings::data::command_off_template` | Command "off" template | Mall för kommandot "av" | Core-literal match |
| 16380 | 875368062 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::name` | Other settings | Övriga inställningar | Core-literal match |
| 16381 | 875368061 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::transition` | Enable the transition feature for this light | Aktivera funktionen för övergångstid för den här ljuskällan | Core-literal match |
| 16382 | 875368060 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::off_delay` | For sensors that only send "on" state updates (like PIRs), this variable sets a delay in seconds after which the sensor’s state will be updated back to "off". | För sensorer som endast skickar "på"-tillståndsändringar (t.ex. PIR-sensorer) ställer den här variabeln in en fördröjning i sekunder, varefter sensorns tillstånd automatiskt ändras tillbaka till "av". | Core-literal match |
| 16383 | 875368059 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::min_kelvin` | The minimum color temperature in Kelvin. | Den lägsta färgtemperaturen i Kelvin. | Core-literal match |
| 16384 | 875368058 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::max_kelvin` | The maximum color temperature in Kelvin. | Den högsta färgtemperaturen i Kelvin. | Core-literal match |
| 16385 | 875368057 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::flash_time_short` | The duration, in seconds, of a "short" flash. | Varaktigheten, i sekunder, för en "kort" blixt. | Core-literal match |
| 16386 | 875368056 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::flash_time_long` | The duration, in seconds, of a "long" flash. | Varaktigheten, i sekunder, för en "lång" blixt. | Core-literal match |
| 16387 | 875368055 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::flash` | Enable the flash feature for this light | Aktivera blixtfunktionen för den här ljuskällan | Core-literal match |
| 16388 | 875368054 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data_description::expire_after` | If set, it defines the number of seconds after the sensor’s state expires, if it’s not updated. After expiry, the sensor’s state becomes unavailable. If not set, the sensor's state never expires. [Learn more.]({url}#expire_after) | Om den är inställd definierar den antalet sekunder efter att sensorns tillstånd har löpt ut om det inte har uppdaterats. Efter utgången blir sensorns tillstånd otillgängligt. Om den inte anges upphör sensorns tillstånd aldrig att gälla. [Läs mer.]({url}#expire_after) | Core-literal match |
| 16389 | 875368053 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::transition` | Transition support | Stöd för övergångstid | Core-literal match |
| 16390 | 875368052 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::off_delay` | OFF delay | Avstängningsfördröjning | Core-literal match |
| 16391 | 875368051 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::min_kelvin` | Min Kelvin | Minsta kelvin | Core-literal match |
| 16392 | 875368050 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::max_kelvin` | Max Kelvin | Högsta kelvin | Core-literal match |
| 16393 | 875368049 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::flash_time_short` | Flash time short | Blixttid kort | Core-literal match |
| 16394 | 875368048 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::flash_time_long` | Flash time long | Blixttid lång | Core-literal match |
| 16395 | 875368047 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::flash` | Flash support | Stöd för blixtfunktion | Core-literal match |
| 16396 | 875368046 | `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::other_settings::data::expire_after` | Expire after | Upphör att gälla efter | Core-literal match |
| 16397 | 875368045 | `component::mqtt::config_subentries::device::step::entity_platform_config::sections::other_settings::name` | Other settings | Övriga inställningar | Core-literal match |
| 16398 | 875368044 | `component::mqtt::config_subentries::device::step::entity_platform_config::sections::other_settings::data_description::suggested_display_precision` | The number of decimals which should be used in the {platform} entity state after rounding. [Learn more.]({url}#suggested_display_precision) | Det antal decimaler som ska användas i {platform}-entitetens tillstånd efter avrundning. [Läs mer.]({url}#suggested_display_precision) | Core-literal match |
| 16399 | 875368043 | `component::mqtt::config_subentries::device::step::entity_platform_config::sections::other_settings::data::suggested_display_precision` | Suggested display precision | Föreslagen visningsprecision | Core-literal match |
| 16400 | 875368042 | `component::mqtt::config_subentries::device::step::device::sections::other_settings::name` | Other device settings | Övriga enhetsinställningar | Core-literal match |
| 16401 | 875368041 | `component::mqtt::config_subentries::device::step::device::sections::other_settings::data_description::sw_version` | The software version of the device. E.g. '2025.1.0'. | Enhetens programvaruversion. T.ex. '2025.1.0'. | Core-literal match |
| 16402 | 875368040 | `component::mqtt::config_subentries::device::step::device::sections::other_settings::data_description::hw_version` | The hardware version of the device. E.g. 'v1.0 rev a'. | Enhetens hårdvaruversion. T.ex. 'v1.0 rev a'. | Core-literal match |
| 16403 | 875368039 | `component::mqtt::config_subentries::device::step::device::sections::other_settings::data::sw_version` | Software version | Mjukvaruversion | Core-literal match |
| 16404 | 875368038 | `component::mqtt::config_subentries::device::step::device::sections::other_settings::data::hw_version` | Hardware version | Hårdvaruversion | Core-literal match |
| 16405 | 875007267 | `component::airos::config::step::reconfigure::sections::additional_settings::name` | Additional settings | Ytterligare inställningar | Shared reference target checked |
| 16406 | 875007266 | `component::airos::config::step::reconfigure::sections::additional_settings::data_description::verify_ssl` | Whether the certificate should be verified when using HTTPS. This should be off for self-signed certificates | Om certifikatet ska verifieras vid användning av HTTPS. Detta ska vara avstängt för självsignerade certifikat. | Shared reference target checked |
| 16407 | 875007265 | `component::airos::config::step::reconfigure::sections::additional_settings::data_description::ssl` | Whether the connection should be encrypted (required for most devices) | Om anslutningen ska vara krypterad (krävs för de flesta enheter) | Shared reference target checked |
| 16408 | 875007264 | `component::airos::config::step::reconfigure::sections::additional_settings::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 16409 | 875007263 | `component::airos::config::step::reconfigure::sections::additional_settings::data::ssl` | Use HTTPS | Använd HTTPS | Shared reference target checked |
| 16410 | 875007262 | `component::airos::config::step::manual::sections::additional_settings::name` | Additional settings | Ytterligare inställningar | Core-literal match |
| 16411 | 875007261 | `component::airos::config::step::manual::sections::additional_settings::data_description::verify_ssl` | Whether the certificate should be verified when using HTTPS. This should be off for self-signed certificates | Om certifikatet ska verifieras vid användning av HTTPS. Detta ska vara avstängt för självsignerade certifikat. | Core-literal match |
| 16412 | 875007260 | `component::airos::config::step::manual::sections::additional_settings::data_description::ssl` | Whether the connection should be encrypted (required for most devices) | Om anslutningen ska vara krypterad (krävs för de flesta enheter) | Core-literal match |
| 16413 | 875007259 | `component::airos::config::step::manual::sections::additional_settings::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 16414 | 875007258 | `component::airos::config::step::manual::sections::additional_settings::data::ssl` | Use HTTPS | Använd HTTPS | Core-literal match |
| 16415 | 875007257 | `component::airos::config::step::configure_device::sections::additional_settings::name` | Additional settings | Ytterligare inställningar | Shared reference target checked |
| 16416 | 875007256 | `component::airos::config::step::configure_device::sections::additional_settings::data_description::verify_ssl` | Whether the certificate should be verified when using HTTPS. This should be off for self-signed certificates | Om certifikatet ska verifieras vid användning av HTTPS. Detta ska vara avstängt för självsignerade certifikat. | Shared reference target checked |
| 16417 | 875007255 | `component::airos::config::step::configure_device::sections::additional_settings::data_description::ssl` | Whether the connection should be encrypted (required for most devices) | Om anslutningen ska vara krypterad (krävs för de flesta enheter) | Shared reference target checked |
| 16418 | 875007254 | `component::airos::config::step::configure_device::sections::additional_settings::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 16419 | 875007253 | `component::airos::config::step::configure_device::sections::additional_settings::data::ssl` | Use HTTPS | Använd HTTPS | Shared reference target checked |
| 16420 | 874664434 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::name` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 16421 | 874664433 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::description` | Provide additional settings for the sensor. | Ange ytterligare inställningar för sensorn. | Source-path follow-up open |
| 16422 | 874664432 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::value_template` | Defines a template to get the state of the sensor. | Definierar en mall för att hämta sensorns status. | Source-path follow-up open |
| 16423 | 874664431 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::unit_of_measurement` | Choose unit of measurement or create your own. | Välj måttenhet eller skapa din egen. | Source-path follow-up open |
| 16424 | 874664430 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::state_class` | The state_class of the sensor. | Sensorns state_class. | Source-path follow-up open |
| 16425 | 874664429 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::device_class` | The type/class of the sensor to set the icon in the frontend. | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet | Source-path follow-up open |
| 16426 | 874664428 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::availability` | Defines a template to get the availability of the sensor. | Definierar en mall för att få information om sensorns tillgänglighet. | Source-path follow-up open |
| 16427 | 874664427 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::attribute` | Get value of an attribute on the selected tag. | Hämta värdet för ett attribut med den valda taggen. | Source-path follow-up open |
| 16428 | 874664426 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::value_template` | Value template | Värdemall | Source-path follow-up open |
| 16429 | 874664425 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::unit_of_measurement` | Unit of measurement | Måttenhet | Source-path follow-up open |
| 16430 | 874664424 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::state_class` | State class | Tillståndsklass | Source-path follow-up open |
| 16431 | 874664423 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::device_class` | Device class | Enhetsklass | Source-path follow-up open |
| 16432 | 874664422 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::availability` | Availability template | Tillgänglighetsmall | Source-path follow-up open |
| 16433 | 874664421 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::attribute` | Attribute | Attribut | Source-path follow-up open |
| 16434 | 874664420 | `component::scrape::config_subentries::entity::step::reconfigure::data_description::select` | Defines what tag to search for. Check Beautifulsoup CSS selectors for details. | Definierar vilken tagg att söka efter. Kolla Beautifulsoup CSS-selectors för mer detaljer. | Shared reference target checked |
| 16435 | 874664419 | `component::scrape::config_subentries::entity::step::reconfigure::data_description::index` | Defines which of the elements returned by the CSS selector to use. | Anger vilka av de element som returneras av CSS-selektorn som ska användas. | Shared reference target checked |
| 16436 | 874664418 | `component::scrape::config_subentries::entity::step::reconfigure::data::select` | Select | Välj | Shared reference target checked |
| 16437 | 874664417 | `component::scrape::config_subentries::entity::step::reconfigure::data::index` | Index | Index | Shared reference target checked |
| 16438 | 874664233 | `component::otp::config::step::confirm::data::qr_code` | QR code | QR-kod | Core-literal match |
| 16439 | 874664232 | `component::ecobee::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 16440 | 874664231 | `component::ecobee::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 876293715 | `component::radio_frequency::entity_component::_::name` | Radio frequency transmitter |
| 875775462 | `component::smtp::config::abort::reauth_successful` | Re-authentication was successful |
| 874664434 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::name` | Additional settings |
| 874664433 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::description` | Provide additional settings for the sensor. |
| 874664432 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::value_template` | Defines a template to get the state of the sensor. |
| 874664431 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::unit_of_measurement` | Choose unit of measurement or create your own. |
| 874664430 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::state_class` | The state_class of the sensor. |
| 874664429 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::device_class` | The type/class of the sensor to set the icon in the frontend. |
| 874664428 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::availability` | Defines a template to get the availability of the sensor. |
| 874664427 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data_description::attribute` | Get value of an attribute on the selected tag. |
| 874664426 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::value_template` | Value template |
| 874664425 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::unit_of_measurement` | Unit of measurement |
| 874664424 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::state_class` | State class |
| 874664423 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::device_class` | Device class |
| 874664422 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::availability` | Availability template |
| 874664421 | `component::scrape::config_subentries::entity::step::reconfigure::sections::advanced::data::attribute` | Attribute |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
