# Home Assistant Core – historisk avstämning 16201–16320

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 81 direkta källtexter matchar HA Core-källan; 27 referensanvändningar med 22 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 12 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16201 | 877183043 | `component::energieleser::config::flow_title` | {device_type} · {host} | {device_type} · {host} | Core-literal match |
| 16202 | 877183042 | `component::energieleser::config::error::unknown_device_type` | This isn't a supported energieleser product. Please check that the device is a stromleser, gasleser, wasserleser, or wärmeleser. | Denna produkt stöds inte som energimätare. Kontrollera att enheten är en elmätare, gasmätare, vattenmätare eller värmemätare. | Core-literal match |
| 16203 | 877183041 | `component::energieleser::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16204 | 877183040 | `component::energieleser::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16205 | 877183039 | `component::energieleser::config::abort::unknown_device_type` | This isn't a supported energieleser product. Please check that the device is a stromleser, gasleser, wasserleser, or wärmeleser. | Denna produkt stöds inte som energimätare. Kontrollera att enheten är en elmätare, gasmätare, vattenmätare eller värmemätare. | Core-literal match |
| 16206 | 877183038 | `component::energieleser::config::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16207 | 877183037 | `component::energieleser::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16208 | 877183036 | `component::energieleser::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16209 | 876961225 | `component::teslemetry::entity::sensor::credit_quota::name` | Teslemetry command quota used | Teslemetry-kommando kvot använt | Core-literal match |
| 16210 | 876884959 | `component::droplet::entity::binary_sensor::unusual_flow::state::on` | Live alert! | Live-varning! | Core-literal match |
| 16211 | 876884958 | `component::droplet::entity::binary_sensor::unusual_flow::state::off` | None | Ingen | Core-literal match |
| 16212 | 876884957 | `component::droplet::entity::binary_sensor::unusual_flow::name` | Unusual flow alert | Varning för ovanligt flöde | Core-literal match |
| 16213 | 876884956 | `component::droplet::entity::binary_sensor::high_flow::state::on` | Live alert! | Live-varning! | Core-literal match |
| 16214 | 876884955 | `component::droplet::entity::binary_sensor::high_flow::state::off` | None | Ingen | Core-literal match |
| 16215 | 876884954 | `component::droplet::entity::binary_sensor::high_flow::name` | High flow alert | Varning för högt flöde | Core-literal match |
| 16216 | 876884775 | `component::yoto::entity::select::night_mode_color::state::white` | White | Vit | Shared reference target checked |
| 16217 | 876884774 | `component::yoto::entity::select::night_mode_color::state::tambourine_red` | Tambourine red | Tamburinröd | Shared reference target checked |
| 16218 | 876884773 | `component::yoto::entity::select::night_mode_color::state::sky_blue` | Sky blue | Himmelsblå | Shared reference target checked |
| 16219 | 876884772 | `component::yoto::entity::select::night_mode_color::state::orange_peel` | Orange peel | Apelsinskal | Shared reference target checked |
| 16220 | 876884771 | `component::yoto::entity::select::night_mode_color::state::off` | Off | Av | Shared reference target checked |
| 16221 | 876884770 | `component::yoto::entity::select::night_mode_color::state::lilac` | Lilac | Lila | Shared reference target checked |
| 16222 | 876884769 | `component::yoto::entity::select::night_mode_color::state::bumblebee_yellow` | Bumblebee yellow | Bumblebee-gul | Shared reference target checked |
| 16223 | 876884768 | `component::yoto::entity::select::night_mode_color::state::apple_green` | Apple green | Äppelgrön | Shared reference target checked |
| 16224 | 876884767 | `component::yoto::entity::select::night_mode_color::name` | Night mode color | Nattläge färg | Core-literal match |
| 16225 | 876884766 | `component::yoto::entity::select::day_mode_color::state::white` | White | Vit | Core-literal match |
| 16226 | 876884765 | `component::yoto::entity::select::day_mode_color::state::tambourine_red` | Tambourine red | Tamburinröd | Core-literal match |
| 16227 | 876884764 | `component::yoto::entity::select::day_mode_color::state::sky_blue` | Sky blue | Himmelsblå | Core-literal match |
| 16228 | 876884763 | `component::yoto::entity::select::day_mode_color::state::orange_peel` | Orange peel | Apelsinskal | Core-literal match |
| 16229 | 876884762 | `component::yoto::entity::select::day_mode_color::state::off` | Off | Av | Shared reference target checked |
| 16230 | 876884761 | `component::yoto::entity::select::day_mode_color::state::lilac` | Lilac | Lila | Core-literal match |
| 16231 | 876884760 | `component::yoto::entity::select::day_mode_color::state::bumblebee_yellow` | Bumblebee yellow | Bumblebee-gul | Core-literal match |
| 16232 | 876884759 | `component::yoto::entity::select::day_mode_color::state::apple_green` | Apple green | Äppelgrön | Core-literal match |
| 16233 | 876884758 | `component::yoto::entity::select::day_mode_color::name` | Day mode color | Dagläge färg | Core-literal match |
| 16234 | 876884592 | `component::yoto::entity::number::night_mode_max_volume::name` | Night mode maximum volume | Nattläge högsta volym | Core-literal match |
| 16235 | 876884591 | `component::yoto::entity::number::night_mode_brightness::name` | Night mode brightness | Nattläge ljusstyrka | Core-literal match |
| 16236 | 876884590 | `component::yoto::entity::number::day_mode_max_volume::name` | Day mode maximum volume | Dagläge högsta volym | Core-literal match |
| 16237 | 876884589 | `component::yoto::entity::number::day_mode_brightness::name` | Day mode brightness | Dagläge ljusstyrka | Core-literal match |
| 16238 | 876884539 | `component::kiosker::entity::sensor::blackout_text::name` | Blackout text | Text för mörkläggningsläget | Core-literal match |
| 16239 | 876884538 | `component::kiosker::entity::sensor::blackout_sound::name` | Blackout sound | Ljud för mörkläggningsläget | Core-literal match |
| 16240 | 876884537 | `component::kiosker::entity::sensor::blackout_icon::name` | Blackout icon | Ikon för mörkläggningsläget | Core-literal match |
| 16241 | 876884536 | `component::kiosker::entity::sensor::blackout_foreground::name` | Blackout foreground color | Förgrundsfärg för mörkläggningsläget | Core-literal match |
| 16242 | 876884535 | `component::kiosker::entity::sensor::blackout_expire::name` | Blackout expiry | Mörkläggningslägets giltighetstid | Core-literal match |
| 16243 | 876884534 | `component::kiosker::entity::sensor::blackout_button_text::name` | Blackout button text | Knapptext i mörkläggningsläget | Core-literal match |
| 16244 | 876884533 | `component::kiosker::entity::sensor::blackout_button_foreground::name` | Blackout button foreground color | Förgrundsfärg för knappen i mörkläggningsläget | Core-literal match |
| 16245 | 876884532 | `component::kiosker::entity::sensor::blackout_button_background::name` | Blackout button background color | Bakgrundsfärg för knappen i mörkläggningsläget | Core-literal match |
| 16246 | 876884531 | `component::kiosker::entity::sensor::blackout_background::name` | Blackout background color | Bakgrundsfärg för mörkläggningsläget | Core-literal match |
| 16247 | 876884527 | `component::kiosker::entity::binary_sensor::blackout_dismissible::name` | Blackout dismissible | Mörkläggningsläge kan avfärdas | Core-literal match |
| 16248 | 876879689 | `component::switchbot::entity::switch::vertical_oscillation::name` | Vertical oscillation | Vertikal oscillation | Core-literal match |
| 16249 | 876879688 | `component::switchbot::entity::switch::horizontal_oscillation::name` | Horizontal oscillation | Horisontell oscillation | Core-literal match |
| 16250 | 876875189 | `component::overkiz::config::step::select_gateway::description` | Select the gateway you want to control with Home Assistant. | Välj den gateway som du vill styra med Home Assistant. | Core-literal match |
| 16251 | 876875188 | `component::overkiz::config::step::select_gateway::data_description::gateway_id` | Select the gateway you want to add. | Välj den gateway du vill lägga till. | Core-literal match |
| 16252 | 876875187 | `component::overkiz::config::step::select_gateway::data::gateway_id` | Gateway | Gateway | Core-literal match |
| 16253 | 876875186 | `component::overkiz::config::step::pick_implementation::title` | Pick authentication method | Välj autentiseringsmetod | Shared reference target checked |
| 16254 | 876875185 | `component::overkiz::config::abort::user_rejected_authorize` | Account linking rejected: {error} | Kontolänkning avvisades: {error} | Source-path follow-up open |
| 16255 | 876875184 | `component::overkiz::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. | OAuth-auktoriseringsfel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 16256 | 876875183 | `component::overkiz::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. | Tidsgränsen överskreds när OAuth-token hämtades. | Source-path follow-up open |
| 16257 | 876875182 | `component::overkiz::config::abort::oauth_implementation_unavailable` | No OAuth2 implementations are currently available. | Inga OAuth2-implementeringar finns tillgängliga för närvarande. | Source-path follow-up open |
| 16258 | 876875181 | `component::overkiz::config::abort::oauth_failed` | Error while obtaining access token. | Fel vid hämtning av åtkomsttoken. | Source-path follow-up open |
| 16259 | 876875180 | `component::overkiz::config::abort::oauth_error` | Received invalid token data. | Ogiltiga tokendata mottogs. | Source-path follow-up open |
| 16260 | 876875179 | `component::overkiz::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) | Ingen webbadress är tillgänglig. [Se hjälpavsnittet]({docs_url}) för information om det här felet. | Source-path follow-up open |
| 16261 | 876875178 | `component::overkiz::config::abort::no_gateways` | No gateways were found for your account. | Inga gateways hittades för ditt konto. | Core-literal match |
| 16262 | 876875177 | `component::overkiz::config::abort::missing_credentials` | The integration requires application credentials. | Integrationen kräver applikationsuppgifter. | Source-path follow-up open |
| 16263 | 876875176 | `component::overkiz::config::abort::missing_configuration` | The component is not configured. Please follow the documentation. | Komponenten har inte konfigurerats. Följ dokumentationen. | Shared reference target checked |
| 16264 | 876875175 | `component::overkiz::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16265 | 876875174 | `component::overkiz::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. | Tidsgränsen överskreds vid generering av en auktoriserings-URL. | Source-path follow-up open |
| 16266 | 876867991 | `component::powerwall::entity::sensor::max_discharge_power::name` | Max discharge power | Max urladdningseffekt | Core-literal match |
| 16267 | 876867990 | `component::powerwall::entity::sensor::max_charge_power::name` | Max charge power | Max laddningseffekt | Core-literal match |
| 16268 | 876851293 | `component::teslemetry::issues::streaming_toggle::title` | Enable data streaming for {vehicle} | Aktivera dataströmning för {vehicle} | Core-literal match |
| 16269 | 876851292 | `component::teslemetry::issues::streaming_toggle::fix_flow::step::confirm::title` | Enable data streaming for {vehicle} | Aktivera dataströmning för {vehicle} | Shared reference target checked |
| 16270 | 876851291 | `component::teslemetry::issues::streaming_toggle::fix_flow::step::confirm::description` | Home Assistant cannot receive streaming data from {vehicle} because the "Allow Third-Party App Data Streaming" toggle is disabled. This option is only available on older Model S and Model X vehicles with Intel-based computers.<br><br>1. In {vehicle}, open Controls > Safety.<br>2. Enable **Allow Third-Party App Data Streaming**.<br>3. Select **Submit** below to re-check. | Home Assistant kan inte ta emot strömmande data från {vehicle} eftersom alternativet ”Tillåt dataströmning från tredjepartsappar” är inaktiverat. Detta alternativ är endast tillgängligt på äldre Model S- och Model X-fordon med Intel-baserade datorer.<br><br>1. I {vehicle}, öppna Kontroller > Säkerhet.<br>2. Aktivera **Tillåt dataströmning från tredjepartsappar**.<br>3. Välj **Bekräfta** nedan för att kontrollera igen. | Core-literal match |
| 16271 | 876851290 | `component::teslemetry::issues::streaming_toggle::fix_flow::error::not_resolved` | Data streaming still appears to be disabled. Please enable "Allow Third-Party App Data Streaming" in the vehicle's Safety settings, then try again. | Dataströmning verkar fortfarande vara inaktiverad. Aktivera alternativet ”Tillåt dataströmning från tredjepartsappar” i fordonets säkerhetsinställningar och försök sedan igen. | Core-literal match |
| 16272 | 876851289 | `component::teslemetry::issues::key::title` | Pair the virtual key for {vehicle} | Koppla den virtuella nyckeln till {vehicle} | Core-literal match |
| 16273 | 876851288 | `component::teslemetry::issues::key::fix_flow::step::confirm::title` | Pair the virtual key for {vehicle} | Koppla den virtuella nyckeln till {vehicle} | Shared reference target checked |
| 16274 | 876851287 | `component::teslemetry::issues::key::fix_flow::step::confirm::description` | Home Assistant cannot receive data from or send commands to {vehicle} because the Teslemetry virtual key is not paired with the vehicle. Until it is paired, the vehicle's data will not update and commands such as locking, climate control and charging will not work.<br><br>1. Open {link}.<br>2. Follow the prompts to add the virtual key to {vehicle}.<br>3. Select **Submit** below to re-check. | Home Assistant kan inte skicka kommandon till {vehicle} eftersom den virtuella nyckeln för Teslemetry inte är kopplad till fordonet. Tills den är kopplad kommer kommandon som låsning, klimatkontroll och laddning inte att fungera.<br><br>1. Öppna {link}.<br>2. Följ anvisningarna för att lägga till den virtuella nyckeln till {vehicle}.<br>3. Välj **Bekräfta** nedan för att kontrollera igen. | Core-literal match |
| 16275 | 876851286 | `component::teslemetry::issues::key::fix_flow::error::not_resolved` | The virtual key still appears to be unpaired. Please complete the pairing at {link}, then try again. | Den virtuella nyckeln verkar fortfarande vara oparad. Slutför parkopplingen på {link}, försök sedan igen. | Core-literal match |
| 16276 | 876817626 | `component::hue_ble::exceptions::device_not_found::message` | The light {name} ({mac}) was not found: {reason} | Lampan {name} ({mac}) hittades inte: {reason} | Core-literal match |
| 16277 | 876762163 | `component::rpi_power::issues::under_voltage_detected::title` | Under-voltage detected | Underspänning detekterad | Core-literal match |
| 16278 | 876762162 | `component::rpi_power::issues::under_voltage_detected::fix_flow::step::confirm::title` | Under-voltage detected | Underspänning detekterad | Shared reference target checked |
| 16279 | 876762161 | `component::rpi_power::issues::under_voltage_detected::fix_flow::step::confirm::description` | Your device has reported a low-voltage condition. The Raspberry Pi monitors its power input and records an under-voltage event when the supply voltage drops below approximately 4.63V. This can lead to instability, unexpected reboots, poor performance, storage corruption, or unreliable operation of Home Assistant.<br><br>Common causes include:<br><br>- A power supply that cannot provide sufficient current.<br>- A low-quality or damaged USB power cable causing voltage drop.<br>- High-demand USB devices connected to the system.<br>- Loose power connections.<br><br>To resolve this issue:<br><br>- Switch to a higher quality power supply and cable.<br>- Disconnect unnecessary USB devices and check whether the warning stops.<br><br>After correcting the power issue, monitor the system to ensure no additional under-voltage events are reported. | Din enhet har rapporterat för låg spänning. Raspberry Pi övervakar sin strömtillförsel och registrerar en underspänningshändelse när matningsspänningen sjunker under cirka 4,63 V. Detta kan leda till instabilitet, oväntade omstarter, försämrad prestanda, skadade lagringsdata eller opålitlig drift av Home Assistant.<br><br>Vanliga orsaker är:<br><br>- En strömförsörjning som inte kan leverera tillräckligt med ström.<br>- En USB-strömkabel av låg kvalitet eller som är skadad, vilket orsakar spänningsfall.<br>- USB-enheter med hög strömförbrukning anslutna till systemet.<br>- Lösa/glappande anslutningar.<br><br>Så här åtgärdar du problemet:<br><br>- Byt till en strömförsörjning och kabel av högre kvalitet.<br>- Koppla bort onödiga USB-enheter och kontrollera om varningen upphör.<br><br>Efter att du har åtgärdat problemet bör du övervaka systemet för att säkerställa att inga ytterligare underspänningshändelser rapporteras. | Core-literal match |
| 16280 | 876761666 | `component::alexa_devices::entity::switch::communications::name` | Communications | Kommunikation | Core-literal match |
| 16281 | 876761665 | `component::alexa_devices::entity::switch::announcements::name` | Announcements | Meddelanden | Core-literal match |
| 16282 | 876746751 | `component::nws::exceptions::entity_unavailable::message` | The location entity {entity_id} is not available or does not have location coordinates. Setup will be retried. | Platsentiteten {entity_id} är inte tillgänglig eller saknar platskoordinater. Konfigurationen kommer att försöka igen. | Core-literal match |
| 16283 | 876746750 | `component::nws::exceptions::entity_not_found::message` | The location entity could not be found. Please remove this integration entry and set it up again. | Platsentiteten kunde inte hittas. Ta bort den här integrationsposten och konfigurera den på nytt. | Core-literal match |
| 16284 | 876746749 | `component::nws::exceptions::entity_disabled::message` | The location entity is disabled. Please enable it or remove this integration entry and set it up again. | Platsentiteten är inaktiverad. Aktivera den eller ta bort integrationsposten och konfigurera den på nytt. | Core-literal match |
| 16285 | 876746748 | `component::nws::config::step::user::menu_options::location` | Specific location | Specifik plats | Core-literal match |
| 16286 | 876746747 | `component::nws::config::step::user::menu_options::entity` | Follow a person or device | Följ en person eller enhet | Core-literal match |
| 16287 | 876746746 | `component::nws::config::step::location::title` | Set up a specific location | Ställ in en specifik plats | Core-literal match |
| 16288 | 876746745 | `component::nws::config::step::location::description` | If a METAR station code is not specified, the specified location will be used to find the closest station. For now, the API key can be anything. It is recommended to use a valid email address. | Om ingen METAR-stationskod anges används den angivna platsen för att hitta närmaste station. För närvarande kan API-nyckeln vara vad som helst. En giltig e-postadress rekommenderas. | Core-literal match |
| 16289 | 876746744 | `component::nws::config::step::location::data::station` | METAR station code | METAR-stationskod | Core-literal match |
| 16290 | 876746743 | `component::nws::config::step::location::data::longitude` | Longitude | Longitud | Source-path follow-up open |
| 16291 | 876746742 | `component::nws::config::step::location::data::latitude` | Latitude | Latitud | Source-path follow-up open |
| 16292 | 876746741 | `component::nws::config::step::location::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 16293 | 876746740 | `component::nws::config::step::entity::title` | Follow a person or device | Följ en person eller enhet | Core-literal match |
| 16294 | 876746739 | `component::nws::config::step::entity::description` | Track weather for a person, device, or zone. The weather station will update automatically as the entity moves. For now, the API key can be anything. It is recommended to use a valid email address. | Spåra väder för en person, enhet eller zon. Väderstationen uppdateras automatiskt när enheten rör sig. För närvarande kan API-nyckeln vara vad som helst. Det rekommenderas att använda en giltig e-postadress. | Core-literal match |
| 16295 | 876746738 | `component::nws::config::step::entity::data_description::location_entity` | Select a person, device tracker, or zone to dynamically track weather for its location. | Välj en person, enhetsspårare eller zon för att dynamiskt spåra vädret för dess plats. | Core-literal match |
| 16296 | 876746737 | `component::nws::config::step::entity::data::location_entity` | Location entity | Platsentitet | Core-literal match |
| 16297 | 876746736 | `component::nws::config::step::entity::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 16298 | 876746735 | `component::nws::config::error::entity_not_found` | The selected entity could not be found. Please choose a different entity. | Den valda entiteten kunde inte hittas. Välj en annan entitet. | Core-literal match |
| 16299 | 876746734 | `component::nws::config::error::entity_no_coordinates` | The selected entity does not have location coordinates. | Den valda entiteten har inga platskoordinater. | Core-literal match |
| 16300 | 876746733 | `component::nws::config::error::entity_disabled` | The selected entity is disabled. Please enable it first. | Den valda entiteten är inaktiverad. Aktivera den först. | Core-literal match |
| 16301 | 876743389 | `component::melcloud_home::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 16302 | 876743388 | `component::melcloud_home::config::step::reauth_confirm::description` | The credentials for your MELCloud Home account are no longer valid. Enter your current credentials to reauthenticate. | Inloggningsuppgifterna för ditt MELCloud Home-konto är inte längre giltiga. Ange dina nuvarande inloggningsuppgifter för att autentisera igen. | Core-literal match |
| 16303 | 876743387 | `component::melcloud_home::config::step::reauth_confirm::data_description::password` | Password for your MELCloud Home account. | Lösenord för ditt MELCloud Home-konto. | Shared reference target checked |
| 16304 | 876743386 | `component::melcloud_home::config::step::reauth_confirm::data_description::email` | Email address for your MELCloud Home account. | E-postadress för ditt MELCloud Home-konto. | Shared reference target checked |
| 16305 | 876743385 | `component::melcloud_home::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 16306 | 876743384 | `component::melcloud_home::config::step::reauth_confirm::data::email` | Email | E-post | Shared reference target checked |
| 16307 | 876743383 | `component::melcloud_home::config::abort::unique_id_mismatch` | The login details correspond to a different account. Please re-authenticate to the previously configured account. | Inloggningsuppgifterna hör till ett annat konto. Autentisera det tidigare konfigurerade kontot på nytt. | Core-literal match |
| 16308 | 876743382 | `component::melcloud_home::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16309 | 876592185 | `component::switchbot_cloud::services::upload_art_frame_image::name` | Upload AI Art Frame image | Ladda upp en bild till AI Art Frame | Core-literal match |
| 16310 | 876592184 | `component::switchbot_cloud::services::upload_art_frame_image::fields::image_url::name` | Image URL | Bild-URL | Core-literal match |
| 16311 | 876592183 | `component::switchbot_cloud::services::upload_art_frame_image::fields::image_url::description` | The URL of the image to upload. | URL-adressen till bilden som ska laddas upp. | Core-literal match |
| 16312 | 876592182 | `component::switchbot_cloud::services::upload_art_frame_image::fields::device_id::name` | Devices | Enheter | Core-literal match |
| 16313 | 876592181 | `component::switchbot_cloud::services::upload_art_frame_image::fields::device_id::description` | The target AI Art Frame device. | Målenheten för AI Art Frame. | Core-literal match |
| 16314 | 876592180 | `component::switchbot_cloud::services::upload_art_frame_image::description` | Upload web images to the device. | Ladda upp webbbilder till enheten. | Core-literal match |
| 16315 | 876549963 | `component::edifier_infrared::entity::button::pc::name` | PC | PC | Core-literal match |
| 16316 | 876549962 | `component::edifier_infrared::entity::button::optical::name` | Optical | Optisk | Core-literal match |
| 16317 | 876549961 | `component::edifier_infrared::entity::button::line_2::name` | Line 2 | Linjeingång 2 | Core-literal match |
| 16318 | 876549960 | `component::edifier_infrared::entity::button::line_1::name` | Line 1 | Linjeingång 1 | Core-literal match |
| 16319 | 876549959 | `component::edifier_infrared::entity::button::fx_on::name` | FX on | FX på | Core-literal match |
| 16320 | 876549958 | `component::edifier_infrared::entity::button::fx_off::name` | FX off | FX av | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 876875185 | `component::overkiz::config::abort::user_rejected_authorize` | Account linking rejected: {error} |
| 876875184 | `component::overkiz::config::abort::oauth_unauthorized` | OAuth authorization error while obtaining access token. |
| 876875183 | `component::overkiz::config::abort::oauth_timeout` | Timeout while resolving the OAuth token. |
| 876875182 | `component::overkiz::config::abort::oauth_implementation_unavailable` | No OAuth2 implementations are currently available. |
| 876875181 | `component::overkiz::config::abort::oauth_failed` | Error while obtaining access token. |
| 876875180 | `component::overkiz::config::abort::oauth_error` | Received invalid token data. |
| 876875179 | `component::overkiz::config::abort::no_url_available` | No URL available. For information about this error, [check the help section]({docs_url}) |
| 876875177 | `component::overkiz::config::abort::missing_credentials` | The integration requires application credentials. |
| 876875174 | `component::overkiz::config::abort::authorize_url_timeout` | Timeout while generating an authorization URL. |
| 876746743 | `component::nws::config::step::location::data::longitude` | Longitude |
| 876746742 | `component::nws::config::step::location::data::latitude` | Latitude |
| 876743382 | `component::melcloud_home::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
