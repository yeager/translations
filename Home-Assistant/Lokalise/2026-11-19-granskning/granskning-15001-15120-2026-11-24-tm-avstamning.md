# Home Assistant Core – historisk avstämning 15001–15120

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 76 direkta källtexter matchar HA Core-källan; 40 referensanvändningar med 25 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 4 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15001 | 890446214 | `component::enphase_envoy::config::step::user::data_description::use_manual_token` | If your Enphase Cloud account has multi-factor authentication enabled, check this option to add or update your token manually. | Om ditt Enphase Cloud-konto har aktiverat flerfaktorsautentisering markerar du det här alternativet för att lägga till eller uppdatera din token manuellt. | Core-literal match |
| 15002 | 890446213 | `component::enphase_envoy::config::step::user::data_description::token` | Go to the [Enphase login]({enphase_url}) to get a new token. Current token lifetime: {token_life} days. | Gå till [inloggningen för Enphase]({enphase_url}) för att hämta en ny token. Den aktuella tokenens giltighetstid är {token_life} dagar. | Core-literal match |
| 15003 | 890446212 | `component::enphase_envoy::config::step::user::data::use_manual_token` | Enter the Envoy access token manually | Ange Envoy-åtkomsttoken manuellt | Core-literal match |
| 15004 | 890446211 | `component::enphase_envoy::config::step::user::data::token` | Envoy access token | Envoy-åtkomsttoken | Core-literal match |
| 15005 | 890446210 | `component::enphase_envoy::config::step::reconfigure::data_description::use_manual_token` | If your Enphase Cloud account has multi-factor authentication enabled, check this option to add or update your token manually. | Om ditt Enphase Cloud-konto har aktiverat flerfaktorsautentisering markerar du det här alternativet för att lägga till eller uppdatera din token manuellt. | Shared reference target checked |
| 15006 | 890446209 | `component::enphase_envoy::config::step::reconfigure::data_description::token` | Go to the [Enphase login]({enphase_url}) to get a new token. Current token lifetime: {token_life} days. | Gå till [inloggningen för Enphase]({enphase_url}) för att hämta en ny token. Den aktuella tokenens giltighetstid är {token_life} dagar. | Shared reference target checked |
| 15007 | 890446208 | `component::enphase_envoy::config::step::reconfigure::data::use_manual_token` | Enter the Envoy access token manually | Ange Envoy-åtkomsttoken manuellt | Shared reference target checked |
| 15008 | 890446207 | `component::enphase_envoy::config::step::reconfigure::data::token` | Envoy access token | Envoy-åtkomsttoken | Shared reference target checked |
| 15009 | 890446206 | `component::enphase_envoy::config::step::reauth_confirm::data_description::use_manual_token` | If your Enphase Cloud account has multi-factor authentication enabled, check this option to add or update your token manually. | Om ditt Enphase Cloud-konto har aktiverat flerfaktorsautentisering markerar du det här alternativet för att lägga till eller uppdatera din token manuellt. | Shared reference target checked |
| 15010 | 890446205 | `component::enphase_envoy::config::step::reauth_confirm::data_description::token` | Go to the [Enphase login]({enphase_url}) to get a new token. Current token lifetime: {token_life} days. | Gå till [inloggningen för Enphase]({enphase_url}) för att hämta en ny token. Den aktuella tokenens giltighetstid är {token_life} dagar. | Shared reference target checked |
| 15011 | 890446204 | `component::enphase_envoy::config::step::reauth_confirm::data::use_manual_token` | Enter the Envoy access token manually | Ange Envoy-åtkomsttoken manuellt | Shared reference target checked |
| 15012 | 890446203 | `component::enphase_envoy::config::step::reauth_confirm::data::token` | Envoy access token | Envoy-åtkomsttoken | Shared reference target checked |
| 15013 | 890446000 | `component::lyngdorf::exceptions::setup_timeout::message` | Timeout connecting to {host} | Timeout vid anslutning till {host} | Core-literal match |
| 15014 | 890445999 | `component::lyngdorf::exceptions::setup_connection_error::message` | Failed to connect to {host} | Misslyckades med att ansluta till {host} | Core-literal match |
| 15015 | 890445998 | `component::lyngdorf::entity::media_player::main_zone::name` | Main zone | Huvudzon | Core-literal match |
| 15016 | 890445997 | `component::lyngdorf::device::zone_b::name` | {device_name} Zone B | {device_name} Zon B | Core-literal match |
| 15017 | 890445996 | `component::lyngdorf::config::step::user::title` | Lyngdorf device connection | Lyngdorf-enhetsanslutning | Core-literal match |
| 15018 | 890445995 | `component::lyngdorf::config::step::user::data_description::host` | Hostname or IP address of the Lyngdorf device | Värdnamn eller IP-adress för Lyngdorf-enheten | Core-literal match |
| 15019 | 890445994 | `component::lyngdorf::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 15020 | 890445993 | `component::lyngdorf::config::step::confirm::description` | Do you want to set up **{name}**? | Vill du konfigurera **{name}**? | Core-literal match |
| 15021 | 890445992 | `component::lyngdorf::config::flow_title` | {name} | {name} | Core-literal match |
| 15022 | 890445991 | `component::lyngdorf::config::error::unsupported_model` | This Lyngdorf model is not supported | Denna Lyngdorf-modell stöds inte | Core-literal match |
| 15023 | 890445990 | `component::lyngdorf::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 15024 | 890445989 | `component::lyngdorf::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 15025 | 890445988 | `component::lyngdorf::config::error::cannot_determine_id` | Could not determine device identity. Ensure the device is powered on and reachable. | Kunde inte fastställa enhetens identitet. Se till att enheten är påslagen och nåbar. | Core-literal match |
| 15026 | 890445987 | `component::lyngdorf::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15027 | 890445986 | `component::lyngdorf::config::abort::unsupported_model` | This Lyngdorf model is not supported | Denna Lyngdorf-modell stöds inte | Core-literal match |
| 15028 | 890445985 | `component::lyngdorf::config::abort::cannot_determine_id` | Could not determine device identity. Ensure the device is powered on and reachable. | Kunde inte fastställa enhetens identitet. Se till att enheten är påslagen och nåbar. | Shared reference target checked |
| 15029 | 890445984 | `component::lyngdorf::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15030 | 890445983 | `component::lyngdorf::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 15031 | 890445982 | `component::lyngdorf::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 15032 | 890445855 | `component::vicare::application_credentials::description` | The **client secret** is ignored, enter any value. Follow the [setup instructions]({more_info_url}) to obtain the Client ID. | **Klienthemligheten** ignoreras, ange valfritt värde. Följ [installationsanvisningarna]({more_info_url}) för att få fram klient-ID:t. | Core-literal match |
| 15033 | 890444804 | `component::fuelprices_dk::config_subentries::station::step::station_selection::description` | Select station to show prices for | Välj station för att visa priser för | Shared reference target checked |
| 15034 | 890444803 | `component::fuelprices_dk::config_subentries::station::step::station_selection::data_description::station` | The station you want to create sensors for | Den station som du vill skapa sensorer för | Shared reference target checked |
| 15035 | 890444802 | `component::fuelprices_dk::config_subentries::station::step::station_selection::data::station` | Select station | Välj station | Shared reference target checked |
| 15036 | 890444801 | `component::fuelprices_dk::config_subentries::station::step::company_selection::description` | Select company | Välj företag | Shared reference target checked |
| 15037 | 890444800 | `component::fuelprices_dk::config_subentries::station::step::company_selection::data_description::company` | The company you want to fetch prices from | Det företag som du vill hämta priser från | Shared reference target checked |
| 15038 | 890444799 | `component::fuelprices_dk::config_subentries::station::step::company_selection::data::company` | Select company | Välj företag | Shared reference target checked |
| 15039 | 890444798 | `component::fuelprices_dk::config_subentries::station::initiate_flow::user` | Add station | Lägg till station | Core-literal match |
| 15040 | 890444797 | `component::fuelprices_dk::config_subentries::station::error::rate_limit_exceeded` | Too many requests to the API. Please try again later. | För många förfrågningar till API:et. Försök igen senare. | Shared reference target checked |
| 15041 | 890444796 | `component::fuelprices_dk::config_subentries::station::error::invalid_api_key` | Invalid API key provided | Den angivna API-nyckeln är ogiltig | Shared reference target checked |
| 15042 | 890444795 | `component::fuelprices_dk::config_subentries::station::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15043 | 890444794 | `component::fuelprices_dk::config_subentries::station::entry_type` | Station | Station | Core-literal match |
| 15044 | 890444793 | `component::fuelprices_dk::config_subentries::station::abort::station_already_configured` | The selected station for this company is already configured | Den valda stationen för detta företag är redan konfigurerad | Shared reference target checked |
| 15045 | 890444792 | `component::fuelprices_dk::config_subentries::station::abort::rate_limit_exceeded` | Too many requests to the API. Please try again later. | För många förfrågningar till API:et. Försök igen senare. | Shared reference target checked |
| 15046 | 890444791 | `component::fuelprices_dk::config_subentries::station::abort::invalid_api_key` | Invalid API key provided | Den angivna API-nyckeln är ogiltig | Shared reference target checked |
| 15047 | 890444790 | `component::fuelprices_dk::config_subentries::station::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15048 | 890444789 | `component::fuelprices_dk::config::step::user::description` | Enter your Fuelprices.dk API key<br>If you do not have an API key, you can get one for free at {website_url} | Ange din API-nyckel för Fuelprices.dk<br>Om du inte har någon API-nyckel kan du skaffa en gratis på {website_url} | Core-literal match |
| 15049 | 890444788 | `component::fuelprices_dk::config::step::user::data_description::api_key` | Your personal API key | Din personliga API-nyckel | Core-literal match |
| 15050 | 890444787 | `component::fuelprices_dk::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 15051 | 890444786 | `component::fuelprices_dk::config::step::station_selection::description` | Select station to show prices for | Välj station för att visa priser för | Core-literal match |
| 15052 | 890444785 | `component::fuelprices_dk::config::step::station_selection::data_description::station` | The station you want to create sensors for | Den station som du vill skapa sensorer för | Core-literal match |
| 15053 | 890444784 | `component::fuelprices_dk::config::step::station_selection::data::station` | Select station | Välj station | Core-literal match |
| 15054 | 890444783 | `component::fuelprices_dk::config::step::reauth_confirm::description` | Your API key needs to be updated. | Din API-nyckel behöver uppdateras. | Core-literal match |
| 15055 | 890444782 | `component::fuelprices_dk::config::step::reauth_confirm::data_description::api_key` | Your personal API key | Din personliga API-nyckel | Core-literal match |
| 15056 | 890444781 | `component::fuelprices_dk::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 15057 | 890444780 | `component::fuelprices_dk::config::step::company_selection::description` | Select company | Välj företag | Core-literal match |
| 15058 | 890444779 | `component::fuelprices_dk::config::step::company_selection::data_description::company` | The company you want to fetch prices from | Det företag som du vill hämta priser från | Core-literal match |
| 15059 | 890444778 | `component::fuelprices_dk::config::step::company_selection::data::company` | Select company | Välj företag | Core-literal match |
| 15060 | 890444777 | `component::fuelprices_dk::config::error::rate_limit_exceeded` | Too many requests to the API. Please try again later. | För många förfrågningar till API:et. Försök igen senare. | Shared reference target checked |
| 15061 | 890444776 | `component::fuelprices_dk::config::error::invalid_api_key` | Invalid API key provided | Den angivna API-nyckeln är ogiltig | Shared reference target checked |
| 15062 | 890444775 | `component::fuelprices_dk::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15063 | 890444774 | `component::fuelprices_dk::config::abort::station_already_configured` | The selected station for this company is already configured | Den valda stationen för detta företag är redan konfigurerad | Core-literal match |
| 15064 | 890444773 | `component::fuelprices_dk::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Shared reference target checked |
| 15065 | 890444772 | `component::fuelprices_dk::config::abort::rate_limit_exceeded` | Too many requests to the API. Please try again later. | För många förfrågningar till API:et. Försök igen senare. | Core-literal match |
| 15066 | 890444771 | `component::fuelprices_dk::config::abort::invalid_api_key` | Invalid API key provided | Den angivna API-nyckeln är ogiltig | Core-literal match |
| 15067 | 890444770 | `component::fuelprices_dk::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 15068 | 890444769 | `component::fuelprices_dk::config::abort::already_configured` | This API key is already configured. | Denna API-nyckel är redan konfigurerad. | Core-literal match |
| 15069 | 890444768 | `component::bsblan::exceptions::not_a_water_heater_device::message` | The selected device ({device_name}) is not a water heater. Please select the water heater sub-device. | Den valda enheten ({device_name}) är inte en varmvattenberedare. Välj underenhet för varmvattenberedaren. | Core-literal match |
| 15070 | 890444641 | `component::izone::config::step::select_controller::description` | Multiple unconfigured iZone controllers were found:<br>{controllers}<br><br>Choose the controller you want to set up now. Any controller you do not select will remain available as a discovered device you can set up later under **Settings** > **Devices & services**. | Flera okonfigurerade iZone-styrenheter har hittats:<br>{controllers}<br><br>Välj den styrenhet du vill konfigurera nu. De styrenheter du inte väljer kommer att förbli tillgängliga som upptäckta enheter som du kan konfigurera senare under **Inställningar** > **Enheter och tjänster**. | Core-literal match |
| 15071 | 890444640 | `component::izone::config::step::select_controller::data::selected_controller_uid` | Controller | Styrenhet | Core-literal match |
| 15072 | 890444639 | `component::izone::config::flow_title` | {name} | {name} | Core-literal match |
| 15073 | 890444638 | `component::izone::config::abort::discovery_started` | iZone discovery has started. Your controllers will appear as discovered devices under Settings > Devices & services. | iZone-upptäckten har påbörjats. Dina styrenheter kommer att visas som upptäckta enheter under Inställningar > Enheter och tjänster. | Core-literal match |
| 15074 | 890444637 | `component::izone::config::abort::discovery_failed` | Failed to start iZone discovery. Make sure your network is properly configured. | Det gick inte att starta iZone-upptäckt. Kontrollera att nätverket är korrekt konfigurerat. | Core-literal match |
| 15075 | 890444636 | `component::izone::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 15076 | 890444635 | `component::izone::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 15077 | 890444321 | `component::scorpiontrack::exceptions::share_unavailable::message` | The shared location is unavailable. | Den delade platsen är inte tillgänglig. | Core-literal match |
| 15078 | 890444320 | `component::scorpiontrack::exceptions::invalid_token::message` | ScorpionTrack rejected the configured share token. | ScorpionTrack avvisade den konfigurerade delningstoken. | Core-literal match |
| 15079 | 890444319 | `component::scorpiontrack::exceptions::cannot_connect::message` | The ScorpionTrack share could not be reached right now. | ScorpionTrack-delningen kunde inte nås just nu. | Core-literal match |
| 15080 | 890444318 | `component::scorpiontrack::config::step::user::title` | Connect a ScorpionTrack share | Anslut en ScorpionTrack-delning | Core-literal match |
| 15081 | 890444317 | `component::scorpiontrack::config::step::user::description` | Paste a ScorpionTrack shared-location URL or the token from that URL. | Klistra in en ScorpionTrack-URL för delad plats eller token från den URL:en. | Core-literal match |
| 15082 | 890444316 | `component::scorpiontrack::config::step::user::data_description::share_token` | Paste the full ScorpionTrack shared-location URL or just the token itself. | Klistra in hela ScorpionTrack-URL:en för den delade platsen eller bara själva token. | Core-literal match |
| 15083 | 890444315 | `component::scorpiontrack::config::step::user::data::share_token` | Share URL or token | Dela URL eller token | Core-literal match |
| 15084 | 890444314 | `component::scorpiontrack::config::error::unknown` | An unexpected error occurred. | Ett oväntat fel uppstod. | Core-literal match |
| 15085 | 890444313 | `component::scorpiontrack::config::error::share_unavailable` | Your shared-location link is invalid, expired, has been revoked, or no longer returns data. | Din länk till den delade platsen är ogiltig, har gått ut, har återkallats eller returnerar inte längre data. | Core-literal match |
| 15086 | 890444312 | `component::scorpiontrack::config::error::invalid_token` | Your shared-location link is invalid or incomplete. | Din länk till den delade platsen är ogiltig eller ofullständig. | Core-literal match |
| 15087 | 890444311 | `component::scorpiontrack::config::error::cannot_connect` | The ScorpionTrack share could not be reached right now. | ScorpionTrack-delningen kunde inte nås just nu. | Core-literal match |
| 15088 | 890444310 | `component::scorpiontrack::config::abort::already_configured` | This shared location is already configured. | Den här delade platsen är redan konfigurerad. | Core-literal match |
| 15089 | 890444309 | `component::smtp::config_subentries::recipient::step::reconfigure::title` | Reconfigure recipient | Konfigurera om mottagaren | Core-literal match |
| 15090 | 890444308 | `component::smtp::config_subentries::recipient::step::reconfigure::description` | Update the recipient email address. | Uppdatera mottagarens e-postadress. | Core-literal match |
| 15091 | 890444307 | `component::smtp::config_subentries::recipient::step::reconfigure::data_description::recipient` | Email address of the recipient. | Mottagarens e-postadress. | Shared reference target checked |
| 15092 | 890444306 | `component::smtp::config_subentries::recipient::step::reconfigure::data::recipient` | Email | E-post | Shared reference target checked |
| 15093 | 890444305 | `component::smtp::config_subentries::recipient::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 15094 | 890444279 | `component::homekit::selector::climate_accessory_type::options::thermostat` | Thermostat | Termostat | Core-literal match |
| 15095 | 890444278 | `component::homekit::selector::climate_accessory_type::options::heater_cooler` | Heater Cooler | Värmare/kylare | Core-literal match |
| 15096 | 890444277 | `component::homekit::selector::climate_accessory_type::options::automatic` | Automatic | Automatisk | Core-literal match |
| 15097 | 890444276 | `component::homekit::options::step::climate::title` | Climate accessory configuration | Konfiguration av klimattillbehör | Core-literal match |
| 15098 | 890444275 | `component::homekit::options::step::climate::description` | Choose which accessory each climate entity uses in HomeKit. Heater Cooler puts the mode, temperature, and the supported fan speed and swing controls on one air conditioner style tile; Thermostat is the classic temperature dial with a separate fan. Automatic keeps the accessory the entity already uses and picks the best fit when it is bridged for the first time. Changing the accessory type keeps the room and name, but HomeKit scenes or automations that used the old controls may need to be recreated. | Välj vilket tillbehör varje klimatentitet använder i HomeKit. ”Värmare/kylare” visar läge, temperatur samt de stödda inställningarna för fläkthastighet och svängning på en bricka. ”Termostat” är den klassiska temperaturreglaget med en separat fläkt. ”Automatisk” behåller det tillbehör som entiteten redan använder och väljer det som passar bäst när den ansluts för första gången. Om du byter tillbehörstyp behålls rummet och namnet, men HomeKit-scener eller automatiseringar som använde de gamla kontrollerna kan behöva göras om på nytt. | Core-literal match |
| 15099 | 890380131 | `component::nina::services::get_details::name` | Get warning details | Hämta varningsinformation | Core-literal match |
| 15100 | 890380130 | `component::nina::services::get_details::description` | Retrieves the details of a warning. | Hämtar information om en varning. | Core-literal match |
| 15101 | 890307459 | `component::yardian::entity::button::stop_irrigation::name` | Stop irrigation | Stoppa bevattning | Core-literal match |
| 15102 | 890298261 | `component::vicare::entity::sensor::active_mode::state::standby` | Standby | Viloläge | Shared reference target checked |
| 15103 | 890298260 | `component::vicare::entity::sensor::active_mode::state::heating` | Heating | Värmer | Core-literal match |
| 15104 | 890298259 | `component::vicare::entity::sensor::active_mode::state::cooling` | Cooling | Kyler | Core-literal match |
| 15105 | 890298258 | `component::vicare::entity::sensor::active_mode::name` | Mode | Läge | Core-literal match |
| 15106 | 889758446 | `component::reolink::entity::select::floodlight_mode::state::scheduleplus` | Schedule plus | Schema plus | Core-literal match |
| 15107 | 889704103 | `component::kiosker::config::step::reauth_confirm::title` | Re-authenticate Kiosker | Återautentisera Kiosker | Core-literal match |
| 15108 | 889704102 | `component::kiosker::config::step::reauth_confirm::description` | Re-authenticate {name} with Home Assistant. Generate a new API token in the Kiosker app settings. | Återautentisera {name} med Home Assistant. Generera en ny API-token i Kiosker-appens inställningar. | Core-literal match |
| 15109 | 889704101 | `component::kiosker::config::step::reauth_confirm::data_description::api_token` | The API token for the Kiosker App. This can be generated in the app API settings. | API-token för Kiosker-appen. Denna kan genereras i appens API-inställningar. | Core-literal match |
| 15110 | 889704100 | `component::kiosker::config::step::reauth_confirm::data::api_token` | API token | API-token | Shared reference target checked |
| 15111 | 889704099 | `component::kiosker::config::abort::wrong_device` | The device does not match the configured device. | Enheten matchar inte den konfigurerade enheten. | Core-literal match |
| 15112 | 889704098 | `component::kiosker::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 15113 | 889703411 | `component::teslemetry::exceptions::auth_failed_login_required::message` | Login is no longer valid, please reauthenticate | Inloggningen är inte längre giltig. Vänligen logga in på nytt. | Core-literal match |
| 15114 | 889701865 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::swing_upper_middle` | Swing upper middle | Sving övre mitten | Core-literal match |
| 15115 | 889701864 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::swing_upper` | Swing upper | Sving övre | Core-literal match |
| 15116 | 889701863 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::swing_middle` | Swing middle | Sving mitten | Core-literal match |
| 15117 | 889701862 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::swing_lower_middle` | Swing lower middle | Sving nedre mitten | Core-literal match |
| 15118 | 889701861 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::swing_lower` | Swing lower | Sving nedre | Core-literal match |
| 15119 | 889701860 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::full_swing` | Full swing | Full sving | Core-literal match |
| 15120 | 889701859 | `component::gree::entity::climate::climate::state_attributes::swing_mode::state::fixed_upper_middle` | Fixed upper middle | Fast övre mitten | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 890445983 | `component::lyngdorf::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 890444636 | `component::izone::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 890444305 | `component::smtp::config_subentries::recipient::abort::reconfigure_successful` | Reconfiguration was successful |
| 889704098 | `component::kiosker::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
