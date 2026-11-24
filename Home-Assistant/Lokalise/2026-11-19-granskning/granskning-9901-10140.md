# Home Assistant Core – livegranskning 9901–10140

Varje nyckel granskades rad för rad. Tidigare rapport `ha-core/granskning-9901-10140.md` användes för granskningshistorik och dupliceringskontroll; aktuell svensk och engelsk text hämtades och lästes tillbaka via Lokalise API den 2026-11-24.

## Resultat

- 240/240 poster granskade individuellt; tomma engelska eller svenska värden: 0.
- 171 källvärden matchar direkt en sträng i pinad Core-källa. 62 referensanvändningar täcker referensbaserade strängar: 37 unika mål, saknade mål 0, konsument/mål-mismatch 0/62 efter korrigering.
- Sju poster saknar direkt literal/sökväg i den pinade Core-katalogen; de listas separat för källägaruppföljning. Lokalises engelska källtext granskades utan att räknas som verifiering mot Core-kod.
- Platshållare matchar 240/240; pluralposter 0.
- 90 värden skiljer sig från den äldre rapportbilden (59 upplösta referensmarkörer och 31 direkta textändringar). Samtliga 25 äldre förslag är redan live; inga skrevs om.
- Sju strängvärden korrigerades i den här livegranskningen, sparades i Lokalise och lästes tillbaka via API.

## Korrigeringar sparade i denna genomgång

| Fullständig Lokalise-nyckel | Föregående live-text | Sparad text | Motivering |
|---|---|---|---
| `component::lawn_mower::triggers::became_idle::name` | Gräsklippare blev inaktiv | Gräsklipparen blir inaktiv | Entity-/händelsenamn uttrycks naturligt som övergång till inaktivt läge. |
| `component::zwave_js::conditions::value::fields::endpoint::description` | Värdets ändpunkt. | Värdets slutpunkt. | Samma Z-Wave-term används som i de relaterade endpoint-etiketterna. |
| `component::zwave_js::conditions::value::fields::behavior::description` | Om någon eller alla valda noder måste matcha. | Om villkoret ska gälla för en eller alla valda noder. | Gemensam formulering; undviker att antyda att noderna ska matcha varandra. |
| `component::zwave_js::conditions::node_status::fields::behavior::description` | Anger om någon eller alla valda noder måste matcha. | Om villkoret ska gälla för en eller alla valda noder. | Samma källreferens och text som övriga Z-Wave-villkor. |
| `component::zwave_js::conditions::config_parameter::fields::endpoint::description` | Värdets ändpunkt. | Värdets slutpunkt. | Samma Z-Wave-term används som i de relaterade endpoint-etiketterna. |
| `component::zwave_js::common::condition_endpoint_description` | Värdets ändpunkt. | Värdets slutpunkt. | Etablerar konsekvent svensk term för Z-Wave endpoint. |
| `component::zwave_js::common::condition_behavior_description` | Om någon eller alla målnoder måste stämma överens. | Om villkoret ska gälla för en eller alla valda noder. | Gemensamt källmål för Z-Wave-villkorskonsumenterna. |

## Radvis liveinventering

| Ordning | Fullständig nyckel | English source (Lokalise) | Aktuell svenska (Lokalise) | Kontroll |
|---:|---|---|---|
| 9901 | `component::besen::entity::sensor::charging_status::state::finished` | Finished | Färdig | Granskad; livevärde godkänt |
| 9902 | `component::besen::entity::sensor::charging_status::state::finish_charging` | Finish charging | Avslutar laddningen | Granskad; tidigare förslag redan live |
| 9903 | `component::besen::entity::sensor::charging_status::state::fault` | Fault | Fel | Granskad; referensmål upplöst och verifierat |
| 9904 | `component::besen::entity::sensor::charging_status::state::connect` | Connect | Ansluter | Granskad; tidigare förslag redan live |
| 9905 | `component::besen::entity::sensor::charging_status::state::canceled` | Canceled | Avbruten | Granskad; livevärde godkänt |
| 9906 | `component::besen::entity::sensor::charging_status::name` | Charging status | Laddningsstatus | Granskad; livevärde godkänt |
| 9907 | `component::besen::entity::sensor::charging_message::state::waiting_for_swipe` | Waiting for a card swipe | Väntar på att kortet ska dras | Granskad; livevärde godkänt |
| 9908 | `component::besen::entity::sensor::charging_message::state::waiting_for_ev` | Charging started, waiting for the EV | Laddningen har startat, väntar på elbilen | Granskad; livevärde godkänt |
| 9909 | `component::besen::entity::sensor::charging_message::state::waiting_for_button` | Waiting for the button to activate | Väntar på att knappen ska aktiveras | Granskad; livevärde godkänt |
| 9910 | `component::besen::entity::sensor::charging_message::state::see_error_state` | See error state | Se felstatus | Granskad; livevärde godkänt |
| 9911 | `component::besen::entity::sensor::charging_message::state::plug_not_connected` | The plug is not connected. Connect it before starting charging. | Kontakten är inte ansluten. Anslut den innan laddningen påbörjas. | Granskad; livevärde godkänt |
| 9912 | `component::besen::entity::sensor::charging_message::state::ev_connected_press_start` | EV is connected, press start | Elbilen är ansluten, tryck på start | Granskad; livevärde godkänt |
| 9913 | `component::besen::entity::sensor::charging_message::state::charging_reservation` | Charging reservation | Laddningsreservation | Granskad; livevärde godkänt |
| 9914 | `component::besen::entity::sensor::charging_message::state::charging_completed` | Charging completed | Laddning klar | Granskad; livevärde godkänt |
| 9915 | `component::besen::entity::sensor::charging_message::state::charging` | Charging | Laddar | Granskad; referensmål upplöst och verifierat |
| 9916 | `component::besen::entity::sensor::charging_message::name` | Charging message | Laddningsmeddelande | Granskad; livevärde godkänt |
| 9917 | `component::collection_image::config::error::invalid_selection` | Invalid media selected: {error} | Ogiltigt medium valt: {error} | Granskad; tidigare förslag redan live |
| 9918 | `component::fyta::entity::sensor::last_update::name` | Last update | Senast uppdaterad | Granskad; livevärde godkänt |
| 9919 | `component::librenms::config::step::reconfigure::data_description::verify_ssl` | Whether to verify the SSL certificate when SSL encryption is used to connect to your LibreNMS instance. | Om SSL-certifikatet ska verifieras när SSL-kryptering används för att ansluta till din LibreNMS-instans. | Granskad; referensmål upplöst och verifierat |
| 9920 | `component::librenms::config::step::reconfigure::data_description::url` | The full URL of your LibreNMS instance. | Den fullständiga URL:en till din LibreNMS-instans. | Granskad; referensmål upplöst och verifierat |
| 9921 | `component::librenms::config::step::reconfigure::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Granskad; referensmål upplöst och verifierat |
| 9922 | `component::librenms::config::step::reconfigure::data::url` | URL | URL | Granskad; referensmål upplöst och verifierat |
| 9923 | `component::librenms::config::step::reauth_confirm::description` | Update the API key for {name}. | Uppdatera API-nyckeln för {name}. | Granskad; livevärde godkänt |
| 9924 | `component::librenms::config::step::reauth_confirm::data_description::api_key` | API key to connect to your LibreNMS instance. | API-nyckel för att ansluta till din LibreNMS-instans. | Granskad; referensmål upplöst och verifierat |
| 9925 | `component::librenms::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Granskad; referensmål upplöst och verifierat |
| 9926 | `component::librenms::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Granskad; referensmål upplöst och verifierat |
| 9927 | `component::librenms::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Granskad; referensmål upplöst och verifierat |
| 9928 | `component::librenms::entity::sensor::rrdtool_version::name` | RRDTool version | RRDTool-version | Granskad; livevärde godkänt |
| 9929 | `component::librenms::entity::sensor::python_version::name` | Python version | Python-version | Granskad; livevärde godkänt |
| 9930 | `component::librenms::entity::sensor::php_version::name` | PHP version | PHP-version | Granskad; livevärde godkänt |
| 9931 | `component::librenms::entity::sensor::netsnmp_version::name` | NetSNMP version | NetSNMP-version | Granskad; livevärde godkänt |
| 9932 | `component::librenms::entity::sensor::device_count::name` | Total device count | Totalt antal enheter | Granskad; livevärde godkänt |
| 9933 | `component::librenms::entity::sensor::database_version::name` | Database version | Databasversion | Granskad; livevärde godkänt |
| 9934 | `component::unifi::config::abort::unknown_site_id` | Previously configured UniFi Network site can no longer be found | Tidigare konfigurerad UniFi-nätverksplats kan inte längre hittas | Granskad; livevärde godkänt |
| 9935 | `component::smartthings::entity::media_player::media_player::state_attributes::sound_mode::state::surround` | Surround | Surround | Granskad; livevärde godkänt |
| 9936 | `component::smartthings::entity::media_player::media_player::state_attributes::sound_mode::state::standard` | Standard | Standard | Granskad; livevärde godkänt |
| 9937 | `component::smartthings::entity::media_player::media_player::state_attributes::sound_mode::state::game` | Game | Spel | Granskad; livevärde godkänt |
| 9938 | `component::smartthings::entity::media_player::media_player::state_attributes::sound_mode::state::adaptive_sound` | Adaptive sound | Adaptivt ljud | Granskad; livevärde godkänt |
| 9939 | `component::rejseplanen::selector::departure_type::options::tog` | Long distance trains (EC, IR, ICE, SJ, etc.) | Långdistanståg (EC, IR, ICE, SJ, etc.) | Granskad; livevärde godkänt |
| 9940 | `component::rejseplanen::selector::departure_type::options::s_tog` | S-trains (Copenhagen suburban) | S-tåg (Köpenhamns pendeltåg) | Granskad; tidigare förslag redan live |
| 9941 | `component::rejseplanen::selector::departure_type::options::re` | Regional trains (Re, RA, RX) | Regionala tåg (Re, RA, RX) | Granskad; livevärde godkänt |
| 9942 | `component::rejseplanen::selector::departure_type::options::night_bus` | Night & special buses | Natt- och specialbussar | Granskad; livevärde godkänt |
| 9943 | `component::rejseplanen::selector::departure_type::options::metro` | Metro | Metro | Granskad; livevärde godkänt |
| 9944 | `component::rejseplanen::selector::departure_type::options::letbane` | Light rail | Spårväg | Granskad; livevärde godkänt |
| 9945 | `component::rejseplanen::selector::departure_type::options::icl` | InterCity Lyn trains (ICL, ICL-X, ICL+) | InterCity Lyn-tåg (ICL, ICL-X, ICL+) | Granskad; livevärde godkänt |
| 9946 | `component::rejseplanen::selector::departure_type::options::ic` | InterCity trains (IC, IB) | InterCity-tåg (IC, IB) | Granskad; livevärde godkänt |
| 9947 | `component::rejseplanen::selector::departure_type::options::flight` | Flight | Flyg | Granskad; livevärde godkänt |
| 9948 | `component::rejseplanen::selector::departure_type::options::flexible_bus` | Flexible transport | Flexibel transport | Granskad; livevärde godkänt |
| 9949 | `component::rejseplanen::selector::departure_type::options::ferry` | Ferry | Färja | Granskad; livevärde godkänt |
| 9950 | `component::rejseplanen::selector::departure_type::options::express_bus` | Express buses | Expressbussar | Granskad; livevärde godkänt |
| 9951 | `component::rejseplanen::selector::departure_type::options::bus` | City buses | Stadsbussar | Granskad; livevärde godkänt |
| 9952 | `component::rejseplanen::issues::yaml_deprecated::title` | YAML configuration detected | YAML-konfiguration upptäckt | Granskad; livevärde godkänt |
| 9953 | `component::rejseplanen::issues::yaml_deprecated::description` | You have configured Rejseplanen in configuration.yaml. This method is deprecated and will be ignored. Please use the UI to configure the integration. To solve this issue, remove the platform configuration from the configuration.yaml. | Du har konfigurerat Rejseplanen i filen configuration.yaml. Denna metod är föråldrad och kommer att ignoreras. Använd istället användargränssnittet för att konfigurera integrationen. För att lösa problemet ska du ta bort plattformskonfigurationen från filen configuration.yaml. | Granskad; livevärde godkänt |
| 9954 | `component::rejseplanen::entity::sensor::track::name` | Departing from track | Avgår från spår | Granskad; livevärde godkänt |
| 9955 | `component::rejseplanen::entity::sensor::no_departures::name` | Number of departures | Antal avgångar | Granskad; livevärde godkänt |
| 9956 | `component::rejseplanen::entity::sensor::line::name` | Line | Linje | Granskad; livevärde godkänt |
| 9957 | `component::rejseplanen::entity::sensor::is_delayed::name` | Delayed | Försenad | Granskad; livevärde godkänt |
| 9958 | `component::rejseplanen::entity::sensor::direction::name` | Towards | Mot | Granskad; livevärde godkänt |
| 9959 | `component::rejseplanen::entity::sensor::departure_time::name` | Departing in | Avgång om | Granskad; livevärde godkänt |
| 9960 | `component::rejseplanen::entity::sensor::delay::name` | Delayed by | Försenad med | Granskad; tidigare förslag redan live |
| 9961 | `component::rejseplanen::config_subentries::stop::step::user::title` | Add Stop | Lägg till hållplats | Granskad; tidigare förslag redan live |
| 9962 | `component::rejseplanen::config_subentries::stop::step::user::description` | Set up stop subentry for Rejseplanen, see the [documentation]({documentation_url}) for information on obtaining the stop id. | Konfigurera en hållplatspost för Rejseplanen. Se [dokumentationen]({documentation_url}) för information om hur du får hållplatsens ID. | Granskad; tidigare förslag redan live |
| 9963 | `component::rejseplanen::config_subentries::stop::step::user::data_description::stop_id` | The Rejseplanen stop ID for the stop to monitor | Rejseplanens ID för hållplatsen som ska övervakas | Granskad; tidigare förslag redan live |
| 9964 | `component::rejseplanen::config_subentries::stop::step::user::data_description::name` | An optional name for this stop subentry | Ett valfritt namn för hållplatsposten | Granskad; tidigare förslag redan live |
| 9965 | `component::rejseplanen::config_subentries::stop::step::user::data_description::direction` | Optional destination filter for departures | Valfritt destinationsfilter för avgångar | Granskad; livevärde godkänt |
| 9966 | `component::rejseplanen::config_subentries::stop::step::user::data_description::departure_type` | Select which types of departures to include | Välj vilka typer av avgångar som ska inkluderas | Granskad; livevärde godkänt |
| 9967 | `component::rejseplanen::config_subentries::stop::step::user::data::stop_id` | Stop ID | Hållplats-ID | Granskad; tidigare förslag redan live |
| 9968 | `component::rejseplanen::config_subentries::stop::step::user::data::name` | Name | Namn | Granskad; livevärde godkänt |
| 9969 | `component::rejseplanen::config_subentries::stop::step::user::data::direction` | Direction | Riktning | Granskad; livevärde godkänt |
| 9970 | `component::rejseplanen::config_subentries::stop::step::user::data::departure_type` | Departure type | Avgångstyp | Granskad; livevärde godkänt |
| 9971 | `component::rejseplanen::config_subentries::stop::initiate_flow::user` | Add stop | Lägg till hållplats | Granskad; tidigare förslag redan live |
| 9972 | `component::rejseplanen::config_subentries::stop::entry_type` | Stop | Hållplats | Granskad; tidigare förslag redan live |
| 9973 | `component::rejseplanen::config::step::user::description` | Set up Rejseplanen data service. | Konfigurera datatjänsten Rejseplanen. | Granskad; livevärde godkänt |
| 9974 | `component::rejseplanen::config::step::user::data_description::api_key` | API key provided by Rejseplanen.dk | API-nyckel tillhandahållen av Rejseplanen.dk | Granskad; livevärde godkänt |
| 9975 | `component::rejseplanen::config::step::user::data::api_key` | API key | API-nyckel | Granskad; referensmål upplöst och verifierat |
| 9976 | `component::rejseplanen::config::error::invalid_auth` | Invalid authentication key | Ogiltig autentiseringsnyckel | Granskad; livevärde godkänt |
| 9977 | `component::rejseplanen::config::error::cannot_connect` | Cannot connect to the Rejseplanen service | Det går inte att ansluta till tjänsten Rejseplanen | Granskad; livevärde godkänt |
| 9978 | `component::rejseplanen::config::abort::single_instance_allowed` | Already configured. Only a single configuration is possible. | Redan konfigurerad. Endast en konfiguration kan göras. | Granskad; referensmål upplöst och verifierat |
| 9979 | `component::rejseplanen::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Granskad; referensmål upplöst och verifierat |
| 9980 | `component::teslemetry::config_subentries::vehicle::step::user::title` | Add local vehicle | Lägg till lokalt fordon | Granskad; livevärde godkänt |
| 9981 | `component::teslemetry::config_subentries::vehicle::step::user::description` | Select which of your eligible vehicles to configure the local Bluetooth connection. | Välj vilket av dina berättigade fordon som du vill konfigurera den lokala Bluetooth-anslutningen för. | Granskad; livevärde godkänt |
| 9982 | `component::teslemetry::config_subentries::vehicle::step::user::data_description::vin` | The account vehicle to enable local Bluetooth control for. | Fordonet i kontot som lokal Bluetooth-styrning ska aktiveras för. | Granskad; tidigare förslag redan live |
| 9983 | `component::teslemetry::config_subentries::vehicle::step::user::data::vin` | Vehicle | Fordon | Granskad; livevärde godkänt |
| 9984 | `component::teslemetry::config_subentries::vehicle::step::scan::title` | Set up Bluetooth control | Konfigurera Bluetooth-styrning | Granskad; tidigare förslag redan live |
| 9985 | `component::teslemetry::config_subentries::vehicle::step::scan::description` | Home Assistant will look for vehicle {vin} over Bluetooth. Make sure the vehicle is within Bluetooth range of a Home Assistant Bluetooth adapter and has fewer than three phone keys in range, then continue. | Home Assistant söker efter fordonet {vin} via Bluetooth. Se till att fordonet är inom räckhåll för en Bluetooth-adapter för Home Assistant och att färre än tre telefonnycklar finns inom räckhåll. Fortsätt sedan. | Granskad; tidigare förslag redan live |
| 9986 | `component::teslemetry::config_subentries::vehicle::step::instructions::title` | Add Home Assistant's key to the vehicle | Lägg till Home Assistants nyckel i fordonet | Granskad; tidigare förslag redan live |
| 9987 | `component::teslemetry::config_subentries::vehicle::step::instructions::description` | Vehicle {vin} does not have Home Assistant's Bluetooth key on its key list. This is expected the first time, and happens again if the key was removed from the vehicle. To add it, select **Submit**, then tap a key card on the center console card reader within about 30 seconds. The vehicle's touchscreen shows a prompt while it waits for the card. | Fordonet {vin} har inte Bluetooth-nyckeln för Home Assistant i sin nyckellista. Det är väntat första gången och om nyckeln har tagits bort från fordonet. För att lägga till den väljer du **Skicka** och håller sedan ett nyckelkort mot kortläsaren i mittkonsolen inom ungefär 30 sekunder. Fordonets pekskärm visar en uppmaning medan den väntar på kortet. | Granskad; livevärde godkänt |
| 9988 | `component::teslemetry::config_subentries::vehicle::progress::pair` | Tap a key card on the center console card reader now. The vehicle stops waiting after about 30 seconds. | Håll ett nyckelkort mot kortläsaren i mittkonsolen nu. Fordonet slutar vänta efter ungefär 30 sekunder. | Granskad; livevärde godkänt |
| 9989 | `component::teslemetry::config_subentries::vehicle::initiate_flow::user` | Add local vehicle | Lägg till lokalt fordon | Granskad; livevärde godkänt |
| 9990 | `component::teslemetry::config_subentries::vehicle::error::timeout` | Timed out waiting for the vehicle to add the key. Select Submit and tap a key card on the center console card reader. | Tidsgränsen överskreds medan fordonet väntades lägga till nyckeln. Välj Skicka och håll ett nyckelkort mot kortläsaren i mittkonsolen. | Granskad; tidigare förslag redan live |
| 9991 | `component::teslemetry::config_subentries::vehicle::error::pair_failed` | The vehicle rejected the key. Make sure it is not in valet mode and does not already have the maximum number of keys, then try again. | Fordonet avvisade nyckeln. Kontrollera att det inte är i betjäningsläge och inte redan har det maximala antalet nycklar, försök sedan igen. | Granskad; livevärde godkänt |
| 9992 | `component::teslemetry::config_subentries::vehicle::error::device_not_found` | No matching Tesla vehicle was found nearby over Bluetooth. Make sure the vehicle is within range of a Bluetooth adapter or proxy, then try again. | Inget matchande Tesla-fordon hittades i närheten via Bluetooth. Kontrollera att fordonet är inom räckhåll för en Bluetooth-adapter eller proxy och försök igen. | Granskad; tidigare förslag redan live |
| 9993 | `component::teslemetry::config_subentries::vehicle::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Granskad; referensmål upplöst och verifierat |
| 9994 | `component::teslemetry::config_subentries::vehicle::entry_type` | Local vehicle | Lokalt fordon | Granskad; tidigare förslag redan live |
| 9995 | `component::teslemetry::config_subentries::vehicle::abort::no_vehicles` | Home Assistant cannot access any vehicles in your Teslemetry account. Check that the vehicle is in your account and that Teslemetry has access to it. | Home Assistant kan inte komma åt några fordon i ditt Teslemetry-konto. Kontrollera att fordonet finns i kontot och att Teslemetry har åtkomst till det. | Granskad; tidigare förslag redan live |
| 9996 | `component::teslemetry::config_subentries::vehicle::abort::entry_not_loaded` | The Teslemetry configuration entry is not loaded. Please ensure it is set up correctly before adding a vehicle. | Konfigurationsposten för Teslemetry har inte laddats. Se till att den är korrekt konfigurerad innan du lägger till ett fordon. | Granskad; livevärde godkänt |
| 9997 | `component::teslemetry::config_subentries::vehicle::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Granskad; referensmål upplöst och verifierat |
| 9998 | `component::teslemetry::config_subentries::energy_site::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Granskad; referensmål upplöst och verifierat |
| 9999 | `component::flexit::entity::sensor::outdoor_air_temperature::name` | Outdoor air temperature | Utomhustemperatur | Granskad; livevärde godkänt |
| 10000 | `component::flexit::entity::sensor::heat_exchanger_regulation::name` | Heat exchanger regulation | Reglering av värmeväxlare | Granskad; livevärde godkänt |
| 10001 | `component::flexit::entity::sensor::electric_heater_regulation::name` | Electric heater regulation | Reglering av elektrisk värmare | Granskad; livevärde godkänt |
| 10002 | `component::flexit::entity::sensor::cooling_regulation::name` | Cooling regulation | Reglering av kylning | Granskad; livevärde godkänt |
| 10003 | `component::flexit::entity::sensor::air_filter_operating_time::name` | Air filter operating time | Drifttid för luftfilter | Granskad; livevärde godkänt |
| 10004 | `component::lawn_mower::triggers::became_idle::name` | Lawn mower became idle | Gräsklipparen blir inaktiv | Korrigerad; API-readback verifierad |
| 10005 | `component::lawn_mower::triggers::became_idle::fields::for::name` | For at least | I minst | Granskad; referensmål upplöst och verifierat |
| 10006 | `component::lawn_mower::triggers::became_idle::fields::behavior::name` | Trigger when | Utlös när | Granskad; referensmål upplöst och verifierat |
| 10007 | `component::lawn_mower::triggers::became_idle::description` | Triggers when one or more lawn mowers become idle. | Utlöses när en eller flera gräsklippare blir inaktiva. | Granskad; tidigare förslag redan live |
| 10008 | `component::lawn_mower::services::stop::name` | Stop lawn mower | Stoppa gräsklippare | Granskad; livevärde godkänt |
| 10009 | `component::lawn_mower::services::stop::description` | Stops a lawn mower's current task. | Avbryter en gräsklippares pågående uppgift. | Granskad; livevärde godkänt |
| 10010 | `component::lawn_mower::entity_component::_::state::idle` | Idle | Inaktiv | Granskad; referensmål upplöst och verifierat |
| 10011 | `component::lawn_mower::conditions::is_idle::name` | Lawn mower is idle | Gräsklippare är inaktiv | Granskad; livevärde godkänt |
| 10012 | `component::lawn_mower::conditions::is_idle::fields::for::name` | For at least | I minst | Granskad; referensmål upplöst och verifierat |
| 10013 | `component::lawn_mower::conditions::is_idle::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Granskad; referensmål upplöst och verifierat |
| 10014 | `component::lawn_mower::conditions::is_idle::description` | Tests if one or more lawn mowers are idle. | Testar om en eller flera gräsklippare är inaktiva. | Granskad; livevärde godkänt |
| 10015 | `component::libre_hardware_monitor::exceptions::deprecated_version::message` | Your version of Libre Hardware Monitor is no longer supported. Please update to version 0.9.5 or later. | Din version av Libre Hardware Monitor stöds inte längre. Uppdatera till version 0.9.5 eller senare. | Granskad; referensmål upplöst och verifierat |
| 10016 | `component::libre_hardware_monitor::config::error::deprecated_version` | Your version of Libre Hardware Monitor is no longer supported. Please update to version 0.9.5 or later. | Din version av Libre Hardware Monitor stöds inte längre. Uppdatera till version 0.9.5 eller senare. | Granskad; referensmål upplöst och verifierat |
| 10017 | `component::libre_hardware_monitor::common::deprecated_version` | Your version of Libre Hardware Monitor is no longer supported. Please update to version 0.9.5 or later. | Din version av Libre Hardware Monitor stöds inte längre. Uppdatera till version 0.9.5 eller senare. | Granskad; livevärde godkänt |
| 10018 | `component::miele::entity::sensor::program_id::state::long_black` | Long black | Lång svart | Granskad; livevärde godkänt |
| 10019 | `component::miele::entity::sensor::program_id::state::chai_latte` | Chai latte | Chai latte | Granskad; livevärde godkänt |
| 10020 | `component::miele::entity::sensor::program_id::state::caffe_americano` | Caffè Americano | Caffè Americano | Granskad; livevärde godkänt |
| 10021 | `component::silla_prism::entity::select::charging_mode::state::solar` | Solar | Solel | Granskad; livevärde godkänt |
| 10022 | `component::silla_prism::entity::select::charging_mode::state::pause` | Paused | Pausad | Granskad; referensmål upplöst och verifierat |
| 10023 | `component::silla_prism::entity::select::charging_mode::state::normal` | Normal | Normal | Granskad; referensmål upplöst och verifierat |
| 10024 | `component::silla_prism::entity::select::charging_mode::name` | Charging mode | Laddningsläge | Granskad; livevärde godkänt |
| 10025 | `component::modbus::exceptions::not_loaded::message` | Modbus is not loaded, so this action cannot be performed. | Modbus är inte laddat, så den här åtgärden kan inte utföras. | Granskad; livevärde godkänt |
| 10026 | `component::hikvision::entity::event::motion::state_attributes::event_type::state::vehicle` | Vehicle | Fordon | Granskad; referensmål upplöst och verifierat |
| 10027 | `component::hikvision::entity::event::motion::state_attributes::event_type::state::triggered` | Triggered | Utlöst | Granskad; referensmål upplöst och verifierat |
| 10028 | `component::hikvision::entity::event::motion::state_attributes::event_type::state::pet` | Pet | Sällskapsdjur | Granskad; referensmål upplöst och verifierat |
| 10029 | `component::hikvision::entity::event::motion::state_attributes::event_type::state::human` | Human | Människa | Granskad; referensmål upplöst och verifierat |
| 10030 | `component::hikvision::entity::event::motion::name` | Motion | Rörelse | Granskad; referensmål upplöst och verifierat |
| 10031 | `component::hikvision::entity::event::line_crossing::state_attributes::event_type::state::vehicle` | Vehicle | Fordon | Granskad; referensmål upplöst och verifierat |
| 10032 | `component::hikvision::entity::event::line_crossing::state_attributes::event_type::state::triggered` | Triggered | Utlöst | Granskad; referensmål upplöst och verifierat |
| 10033 | `component::hikvision::entity::event::line_crossing::state_attributes::event_type::state::pet` | Pet | Sällskapsdjur | Granskad; referensmål upplöst och verifierat |
| 10034 | `component::hikvision::entity::event::line_crossing::state_attributes::event_type::state::human` | Human | Människa | Granskad; referensmål upplöst och verifierat |
| 10035 | `component::hikvision::entity::event::line_crossing::name` | Line crossing | Linjepassering | Granskad; referensmål upplöst och verifierat |
| 10036 | `component::hikvision::entity::event::field_detection::state_attributes::event_type::state::vehicle` | Vehicle | Fordon | Granskad; livevärde godkänt |
| 10037 | `component::hikvision::entity::event::field_detection::state_attributes::event_type::state::triggered` | Triggered | Utlöst | Granskad; livevärde godkänt |
| 10038 | `component::hikvision::entity::event::field_detection::state_attributes::event_type::state::pet` | Pet | Sällskapsdjur | Granskad; livevärde godkänt |
| 10039 | `component::hikvision::entity::event::field_detection::state_attributes::event_type::state::human` | Human | Människa | Granskad; livevärde godkänt |
| 10040 | `component::hikvision::entity::event::field_detection::name` | Field detection | Fältdetektering | Granskad; referensmål upplöst och verifierat |
| 10041 | `component::midea::entity::water_heater::water_heater_heating::name` | Heating water heater | Varmvattenberedare | Granskad; livevärde godkänt |
| 10042 | `component::midea::entity::water_heater::water_heater_bathing::name` | Bathing water heater | Badvattenberedare | Granskad; livevärde godkänt |
| 10043 | `component::airly::config::error::unknown` | Unexpected error | Oväntat fel | Granskad; referensmål upplöst och verifierat |
| 10044 | `component::airly::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Granskad; referensmål upplöst och verifierat |
| 10045 | `component::melcloud_home::entity::sensor::outdoor_temperature::name` | Outdoor temperature | Utomhustemperatur | Granskad; livevärde godkänt |
| 10046 | `component::wolflink::config::step::user::data_description::username` | The username for your Wolf SmartSet account. | Användarnamnet för ditt Wolf SmartSet-konto. | Granskad; livevärde godkänt |
| 10047 | `component::wolflink::config::step::user::data_description::password` | The password for your Wolf SmartSet account. | Lösenordet för ditt Wolf SmartSet-konto. | Granskad; livevärde godkänt |
| 10048 | `component::bitvis::entity::sensor::wifi_rssi::name` | Wi-Fi signal strength | Wi-Fi-signalstyrka | Granskad; livevärde godkänt |
| 10049 | `component::bitvis::entity::sensor::power_reactive_phase_import::name` | Reactive power import {phase} | Reaktiv effektimport {phase} | Granskad; livevärde godkänt |
| 10050 | `component::bitvis::entity::sensor::power_reactive_phase_export::name` | Reactive power export {phase} | Reaktiv effektexport {phase} | Granskad; livevärde godkänt |
| 10051 | `component::bitvis::entity::sensor::power_reactive_import::name` | Reactive power import | Reaktiv effektimport | Granskad; livevärde godkänt |
| 10052 | `component::bitvis::entity::sensor::power_reactive_export::name` | Reactive power export | Reaktiv effektexport | Granskad; livevärde godkänt |
| 10053 | `component::bitvis::entity::sensor::power_active_phase_import::name` | Active power import {phase} | Aktiv effektimport {phase} | Granskad; livevärde godkänt |
| 10054 | `component::bitvis::entity::sensor::power_active_phase_export::name` | Active power export {phase} | Aktiv effektexport {phase} | Granskad; livevärde godkänt |
| 10055 | `component::bitvis::entity::sensor::power_active_import::name` | Active power import | Aktiv effektimport | Granskad; livevärde godkänt |
| 10056 | `component::bitvis::entity::sensor::power_active_export::name` | Active power export | Aktiv effektexport | Granskad; livevärde godkänt |
| 10057 | `component::bitvis::entity::sensor::phase_voltage::name` | Voltage {phase} | Spänning {phase} | Granskad; livevärde godkänt |
| 10058 | `component::bitvis::entity::sensor::phase_current::name` | Current {phase} | Ström {phase} | Granskad; livevärde godkänt |
| 10059 | `component::bitvis::entity::sensor::han_msg_successfully_parsed::name` | HAN messages successfully parsed | HAN-meddelanden har analyserats korrekt | Granskad; livevärde godkänt |
| 10060 | `component::bitvis::entity::sensor::han_msg_buffer_overflow::name` | HAN buffer overflows | HAN-buffertöverflöden | Granskad; tidigare förslag redan live |
| 10061 | `component::bitvis::entity::sensor::energy_reactive_import::name` | Reactive energy import | Reaktiv energiimport | Granskad; livevärde godkänt |
| 10062 | `component::bitvis::entity::sensor::energy_reactive_export::name` | Reactive energy export | Reaktiv energiexport | Granskad; livevärde godkänt |
| 10063 | `component::bitvis::entity::sensor::energy_active_import::name` | Active energy import | Aktiv energiimport | Granskad; livevärde godkänt |
| 10064 | `component::bitvis::entity::sensor::energy_active_export::name` | Active energy export | Aktiv energiexport | Granskad; livevärde godkänt |
| 10065 | `component::bitvis::config::step::zeroconf_confirm::title` | Discovered Bitvis Power Hub | Upptäckt Bitvis Power Hub | Granskad; livevärde godkänt |
| 10066 | `component::bitvis::config::step::zeroconf_confirm::description` | Do you want to add the discovered Bitvis Power Hub ({name}) at {host} to Home Assistant? | Vill du lägga till den upptäckta Bitvis Power Hub ({name}) på {host} i Home Assistant? | Granskad; livevärde godkänt |
| 10067 | `component::bitvis::config::step::user::title` | Set up Bitvis Power Hub | Konfigurera Bitvis Power Hub | Granskad; livevärde godkänt |
| 10068 | `component::bitvis::config::step::user::description` | Enter the hostname or IP address of your Bitvis Power Hub. Setup waits for a UDP packet from the device. | Ange värdnamnet eller IP-adressen för din Bitvis Power Hub. Installationsprogrammet väntar på ett UDP-paket från enheten. | Granskad; livevärde godkänt |
| 10069 | `component::bitvis::config::step::user::data_description::host` | Hostname or IP address of your Bitvis Power Hub device. | Värdnamn eller IP-adress för din Bitvis Power Hub-enhet. | Granskad; livevärde godkänt |
| 10070 | `component::bitvis::config::step::user::data::host` | Host | Värd | Granskad; referensmål upplöst och verifierat |
| 10071 | `component::bitvis::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Granskad; referensmål upplöst och verifierat |
| 10072 | `component::bitvis::config::error::invalid_mac` | The device did not provide a valid MAC address. Update the Power Hub to the latest firmware and try again. | Enheten angav inte en giltig MAC-adress. Uppdatera Power Hub till den senaste firmwareversionen och försök igen. | Granskad; livevärde godkänt |
| 10073 | `component::bitvis::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Granskad; referensmål upplöst och verifierat |
| 10074 | `component::bitvis::config::abort::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Granskad; referensmål upplöst och verifierat |
| 10075 | `component::bitvis::config::abort::invalid_mac` | The device did not provide a valid MAC address. Update the Power Hub to the latest firmware and try again. | Enheten angav inte en giltig MAC-adress. Uppdatera Power Hub till den senaste firmwareversionen och försök igen. | Granskad; livevärde godkänt |
| 10076 | `component::bitvis::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Granskad; referensmål upplöst och verifierat |
| 10077 | `component::bitvis::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Granskad; referensmål upplöst och verifierat |
| 10078 | `component::bitvis::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Granskad; referensmål upplöst och verifierat |
| 10079 | `component::besen::entity::number::charging_current::name` | Charging current | Laddningsström | Granskad; livevärde godkänt |
| 10080 | `component::ukraine_alarm::entity::binary_sensor::air_yellow::name` | Air (yellow) | Luft (gul) | Granskad; livevärde godkänt |
| 10081 | `component::ukraine_alarm::entity::binary_sensor::air_red::name` | Air (red) | Luft (röd) | Granskad; livevärde godkänt |
| 10082 | `component::zwave_js::selector::node_status::options::dead` | Dead | Död | Granskad; livevärde godkänt |
| 10083 | `component::zwave_js::selector::node_status::options::awake` | Awake | Vaken | Granskad; livevärde godkänt |
| 10084 | `component::zwave_js::selector::node_status::options::asleep` | Asleep | Sover | Granskad; livevärde godkänt |
| 10085 | `component::zwave_js::selector::node_status::options::alive` | Alive | Lever | Granskad; livevärde godkänt |
| 10086 | `component::zwave_js::conditions::value::name` | Z-Wave JS value | Z-Wave JS-värde | Granskad; livevärde godkänt |
| 10087 | `component::zwave_js::conditions::value::fields::value::name` | Value | Värde | Granskad; referensmål upplöst och verifierat |
| 10088 | `component::zwave_js::conditions::value::fields::value::description` | The value to compare with, either the raw value or its state label. | Det värde som ska jämföras med, antingen det råa värdet eller dess tillståndsetikett. | Granskad; referensmål upplöst och verifierat |
| 10089 | `component::zwave_js::conditions::value::fields::property_key::name` | Property key | Egenskapsnyckel | Granskad; livevärde godkänt |
| 10090 | `component::zwave_js::conditions::value::fields::property_key::description` | Property key of the value. | Egenskapsnyckel för värdet. | Granskad; livevärde godkänt |
| 10091 | `component::zwave_js::conditions::value::fields::property::name` | Property | Egenskap | Granskad; livevärde godkänt |
| 10092 | `component::zwave_js::conditions::value::fields::property::description` | Property of the value. | Värdets egenskap. | Granskad; livevärde godkänt |
| 10093 | `component::zwave_js::conditions::value::fields::endpoint::name` | Endpoint | Slutpunkt | Granskad; referensmål upplöst och verifierat |
| 10094 | `component::zwave_js::conditions::value::fields::endpoint::description` | Endpoint of the value. | Värdets slutpunkt. | Korrigerad; API-readback verifierad |
| 10095 | `component::zwave_js::conditions::value::fields::device_id::name` | Devices | Enheter | Granskad; referensmål upplöst och verifierat |
| 10096 | `component::zwave_js::conditions::value::fields::device_id::description` | The Z-Wave JS devices whose nodes to test. | De Z-Wave JS-enheter vars noder ska testas. | Granskad; referensmål upplöst och verifierat |
| 10097 | `component::zwave_js::conditions::value::fields::command_class::name` | Command class | Kommandoklass | Granskad; livevärde godkänt |
| 10098 | `component::zwave_js::conditions::value::fields::command_class::description` | Command class of the value. | Kommandoklass för värdet. | Granskad; livevärde godkänt |
| 10099 | `component::zwave_js::conditions::value::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Granskad; livevärde godkänt |
| 10100 | `component::zwave_js::conditions::value::fields::behavior::description` | Whether any or every targeted node must match. | Om villkoret ska gälla för en eller alla valda noder. | Korrigerad; API-readback verifierad |
| 10101 | `component::zwave_js::conditions::value::description` | Tests if a Z-Wave value on one or more nodes equals the given value. | Kontrollerar om ett Z-Wave-värde på en eller flera noder är lika med det angivna värdet. | Granskad; livevärde godkänt |
| 10102 | `component::zwave_js::conditions::node_status::name` | Z-Wave JS node status | Nodstatus för Z-Wave JS | Granskad; livevärde godkänt |
| 10103 | `component::zwave_js::conditions::node_status::fields::status::name` | Status | Status | Granskad; livevärde godkänt |
| 10104 | `component::zwave_js::conditions::node_status::fields::status::description` | The node status to test for. | Nodstatusen som ska testas. | Granskad; livevärde godkänt |
| 10105 | `component::zwave_js::conditions::node_status::fields::device_id::name` | Devices | Enheter | Granskad; livevärde godkänt |
| 10106 | `component::zwave_js::conditions::node_status::fields::device_id::description` | The Z-Wave JS devices whose nodes to test. | De Z-Wave JS-enheter vars noder ska testas. | Granskad; livevärde godkänt |
| 10107 | `component::zwave_js::conditions::node_status::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Granskad; livevärde godkänt |
| 10108 | `component::zwave_js::conditions::node_status::fields::behavior::description` | Whether any or every targeted node must match. | Om villkoret ska gälla för en eller alla valda noder. | Korrigerad; API-readback verifierad |
| 10109 | `component::zwave_js::conditions::node_status::description` | Tests if one or more Z-Wave JS nodes have the given status. | Testar om en eller flera Z-Wave JS-noder har angiven status. | Granskad; livevärde godkänt |
| 10110 | `component::zwave_js::conditions::config_parameter::name` | Z-Wave JS configuration parameter | Konfigurationsparameter för Z-Wave JS | Granskad; livevärde godkänt |
| 10111 | `component::zwave_js::conditions::config_parameter::fields::value::name` | Value | Värde | Granskad; livevärde godkänt |
| 10112 | `component::zwave_js::conditions::config_parameter::fields::value::description` | The value to compare with, either the raw value or its state label. | Det värde som ska jämföras med, antingen det råa värdet eller dess tillståndsetikett. | Granskad; referensmål upplöst och verifierat |
| 10113 | `component::zwave_js::conditions::config_parameter::fields::parameter::name` | Parameter | Parameter | Granskad; livevärde godkänt |
| 10114 | `component::zwave_js::conditions::config_parameter::fields::parameter::description` | Number of the configuration parameter. | Nummer på konfigurationsparametern. | Granskad; livevärde godkänt |
| 10115 | `component::zwave_js::conditions::config_parameter::fields::endpoint::name` | Endpoint | Slutpunkt | Granskad; referensmål upplöst och verifierat |
| 10116 | `component::zwave_js::conditions::config_parameter::fields::endpoint::description` | Endpoint of the value. | Värdets slutpunkt. | Korrigerad; API-readback verifierad |
| 10117 | `component::zwave_js::conditions::config_parameter::fields::device_id::name` | Devices | Enheter | Granskad; referensmål upplöst och verifierat |
| 10118 | `component::zwave_js::conditions::config_parameter::fields::device_id::description` | The Z-Wave JS devices whose nodes to test. | De Z-Wave JS-enheter vars noder ska testas. | Granskad; referensmål upplöst och verifierat |
| 10119 | `component::zwave_js::conditions::config_parameter::fields::bitmask::name` | Bitmask | Bitmask | Granskad; livevärde godkänt |
| 10120 | `component::zwave_js::conditions::config_parameter::fields::bitmask::description` | Bitmask of a partial parameter, as a number or hexadecimal string, if the parameter is split into parts. | Bitmask för en delparameter, i form av ett tal eller en hexadecimal sträng, om parametern är uppdelad i delar. | Granskad; livevärde godkänt |
| 10121 | `component::zwave_js::conditions::config_parameter::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Granskad; referensmål upplöst och verifierat |
| 10122 | `component::zwave_js::conditions::config_parameter::fields::behavior::description` | Whether any or every targeted node must match. | Om villkoret ska gälla för en eller alla valda noder. | Granskad; referensmål upplöst och verifierat |
| 10123 | `component::zwave_js::conditions::config_parameter::description` | Tests if a configuration parameter on one or more Z-Wave JS nodes has the given value. | Kontrollerar om en konfigurationsparameter på en eller flera Z-Wave JS-noder har det angivna värdet. | Granskad; livevärde godkänt |
| 10124 | `component::zwave_js::common::condition_value_name` | Value | Värde | Granskad; livevärde godkänt |
| 10125 | `component::zwave_js::common::condition_value_description` | The value to compare with, either the raw value or its state label. | Det värde som ska jämföras med, antingen det råa värdet eller dess tillståndsetikett. | Granskad; livevärde godkänt |
| 10126 | `component::zwave_js::common::condition_endpoint_name` | Endpoint | Slutpunkt | Granskad; livevärde godkänt |
| 10127 | `component::zwave_js::common::condition_endpoint_description` | Endpoint of the value. | Värdets slutpunkt. | Korrigerad; API-readback verifierad |
| 10128 | `component::zwave_js::common::condition_device_id_name` | Devices | Enheter | Granskad; livevärde godkänt |
| 10129 | `component::zwave_js::common::condition_device_id_description` | The Z-Wave JS devices whose nodes to test. | De Z-Wave JS-enheter vars noder ska testas. | Granskad; livevärde godkänt |
| 10130 | `component::zwave_js::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Granskad; livevärde godkänt |
| 10131 | `component::zwave_js::common::condition_behavior_description` | Whether any or every targeted node must match. | Om villkoret ska gälla för en eller alla valda noder. | Korrigerad; API-readback verifierad |
| 10132 | `component::metoffice::config::step::user::data_description::longitude` | The longitude of a location for which to request a weather forecast. | Longituden för platsen som väderprognosen ska hämtas för. | Granskad; tidigare förslag redan live |
| 10133 | `component::metoffice::config::step::user::data_description::latitude` | The latitude of a location for which to request a weather forecast. | Latituden för platsen som väderprognosen ska hämtas för. | Granskad; tidigare förslag redan live |
| 10134 | `component::metoffice::config::step::user::data_description::api_key` | Met Office DataHub API key for the Site Specific Global Spot API. | Met Office DataHub-API-nyckel för det platsspecifika Global Spot-API:t. | Granskad; tidigare förslag redan live |
| 10135 | `component::metoffice::config::step::reauth_confirm::data_description::api_key` | Met Office DataHub API key for the Site Specific Global Spot API. | Met Office DataHub-API-nyckel för det platsspecifika Global Spot-API:t. | Granskad; referensmål upplöst och verifierat |
| 10136 | `component::midea::entity::switch::pump::name` | Pump | Pump | Granskad; livevärde godkänt |
| 10137 | `component::tplink_omada::services::set_client_name::name` | Set client name | Ställ in klientnamn | Granskad; livevärde godkänt |
| 10138 | `component::tplink_omada::services::set_client_name::fields::name::name` | Name | Namn | Granskad; livevärde godkänt |
| 10139 | `component::tplink_omada::services::set_client_name::fields::name::description` | New name for the client. | Nytt namn på klienten. | Granskad; livevärde godkänt |
| 10140 | `component::tplink_omada::services::set_client_name::fields::device_id::name` | Device | Enhet | Granskad; livevärde godkänt |

## Källuppföljning

| Ordning | Fullständig nyckel | English source |
|---:|---|---|
| 9905 | `component::besen::entity::sensor::charging_status::state::canceled` | Canceled |
| 9926 | `component::librenms::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 9927 | `component::librenms::config::abort::reauth_successful` | Re-authentication was successful |
| 9978 | `component::rejseplanen::config::abort::single_instance_allowed` | Already configured. Only a single configuration is possible. |
| 10030 | `component::hikvision::entity::event::motion::name` | Motion |
| 10132 | `component::metoffice::config::step::user::data_description::longitude` | The longitude of a location for which to request a weather forecast. |
| 10133 | `component::metoffice::config::step::user::data_description::latitude` | The latitude of a location for which to request a weather forecast. |

## Proveniens och validering

- HA Core-checkout: `sources/home-assistant-core-current`, commit `2fdaa177f3e94535b3b649fb1ffc2dbba52eb4ce`.
- Lokalise-projekt `130246255a974bd3b5e8a1.51616605`; 240 måltranslationer återlästa efter eventuella skrivningar.
- Manifest `2026-11-24-reviewed-core-9901-10140.json`: `verified-existing` markerar redan sparade värden som granskats på nytt; `saved-and-read-back` markerar sju nyss sparade korrigeringar.
- svlang kördes per sträng; Hunspell-sv användes med manuell bedömning av produktnamn, protokoll, egennamn och låneord. Swedish FOSS-terminologi och Home Assistant-TM kontrollerades som stöd, inte facit. Varningarna för passiv form/långa meningar avslogs när formuleringarna var idiomatiska UI-texter; ett onaturligt triggernamn förbättrades.
- HA-TM snapshot, PO, genererad TMX och kanonisk gransknings-TMX uppdateras med dessa livevärden och proveniens.
