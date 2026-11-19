# Sparade svenska översättningar: Besen, Rejseplanen, Teslemetry, Bitvis och Met Office

Datum: 2026-11-19

Alla poster nedan har sparats via Lokalise API och lästs tillbaka efter uppdateringen.

## Ändringar

### `component::besen::entity::sensor::charging_status::state::finish_charging`

- Engelska: Finish charging
- Tidigare svenska: Slutför laddningen
- Sparad svenska: Avslutar laddningen

### `component::besen::entity::sensor::charging_status::state::connect`

- Engelska: Connect
- Tidigare svenska: Anslut
- Sparad svenska: Ansluter

### `component::collection_image::config::error::invalid_selection`

- Engelska: Invalid media selected: {error}
- Tidigare svenska: Ogiltigt media valt: {error}
- Sparad svenska: Ogiltigt medium valt: {error}

### `component::rejseplanen::selector::departure_type::options::s_tog`

- Engelska: S-trains (Copenhagen suburban)
- Tidigare svenska: S-tåg (Köpenhamns förort)
- Sparad svenska: S-tåg (Köpenhamns pendeltåg)

### `component::rejseplanen::entity::sensor::delay::name`

- Engelska: Delayed by
- Tidigare svenska: Försenad av
- Sparad svenska: Försenad med

### `component::rejseplanen::config_subentries::stop::step::user::title`

- Engelska: Add Stop
- Tidigare svenska: Lägg till stopp
- Sparad svenska: Lägg till hållplats

### `component::rejseplanen::config_subentries::stop::step::user::description`

- Engelska: Set up stop subentry for Rejseplanen, see the [documentation]({documentation_url}) for information on obtaining the stop id.
- Tidigare svenska: Ställ in stoppunderpost för Rejseplanen, se [dokumentationen]({documentation_url}) för information om hur man får stopp-ID:t.
- Sparad svenska: Konfigurera en hållplatspost för Rejseplanen. Se [dokumentationen]({documentation_url}) för information om hur du får hållplatsens ID.

### `component::rejseplanen::config_subentries::stop::step::user::data_description::stop_id`

- Engelska: The Rejseplanen stop ID for the stop to monitor
- Tidigare svenska: Rejseplanens stopp-ID för den hållplats att övervaka
- Sparad svenska: Rejseplanens ID för hållplatsen som ska övervakas

### `component::rejseplanen::config_subentries::stop::step::user::data_description::name`

- Engelska: An optional name for this stop subentry
- Tidigare svenska: Ett valfritt namn för denna stoppunderpost
- Sparad svenska: Ett valfritt namn för hållplatsposten

### `component::rejseplanen::config_subentries::stop::step::user::data::stop_id`

- Engelska: Stop ID
- Tidigare svenska: Stopp-ID
- Sparad svenska: Hållplats-ID

### `component::rejseplanen::config_subentries::stop::initiate_flow::user`

- Engelska: Add stop
- Tidigare svenska: Lägg till stopp
- Sparad svenska: Lägg till hållplats

### `component::rejseplanen::config_subentries::stop::entry_type`

- Engelska: Stop
- Tidigare svenska: Stopp
- Sparad svenska: Hållplats

### `component::teslemetry::config_subentries::vehicle::step::user::data_description::vin`

- Engelska: The account vehicle to enable local Bluetooth control for.
- Tidigare svenska: Den enhet som ska användas för att möjliggöra lokal Bluetooth-styrning.
- Sparad svenska: Fordonet i kontot som lokal Bluetooth-styrning ska aktiveras för.

### `component::teslemetry::config_subentries::vehicle::step::scan::title`

- Engelska: Set up Bluetooth control
- Tidigare svenska: Konfigurera Bluetooth-kontroll
- Sparad svenska: Konfigurera Bluetooth-styrning

### `component::teslemetry::config_subentries::vehicle::step::scan::description`

- Engelska: Home Assistant will look for vehicle {vin} over Bluetooth. Make sure the vehicle is within Bluetooth range of a Home Assistant Bluetooth adapter and has fewer than three phone keys in range, then continue.
- Tidigare svenska: Hemassistenten kommer att leta efter fordonet {vin} via Bluetooth. Se till att fordonet är inom Bluetooth-räckvidden för en Home Assistant Bluetooth-adapter och har färre än tre telefonknappar inom räckhåll, fortsätt sedan.
- Sparad svenska: Home Assistant söker efter fordonet {vin} via Bluetooth. Se till att fordonet är inom räckhåll för en Bluetooth-adapter för Home Assistant och att färre än tre telefonnycklar finns inom räckhåll. Fortsätt sedan.

### `component::teslemetry::config_subentries::vehicle::step::instructions::title`

- Engelska: Add Home Assistant's key to the vehicle
- Tidigare svenska: Godkänn den virtuella nyckeln
- Sparad svenska: Lägg till Home Assistants nyckel i fordonet

### `component::teslemetry::config_subentries::vehicle::error::timeout`

- Engelska: Timed out waiting for the vehicle to add the key. Select Submit and tap a key card on the center console card reader.
- Tidigare svenska: Tidsgränsen för att bilen ska acceptera nyckeln har nåtts. Försök igen efter att nyckeln har godkänts på bilens pekskärm.
- Sparad svenska: Tidsgränsen överskreds medan fordonet väntades lägga till nyckeln. Välj Skicka och håll ett nyckelkort mot kortläsaren i mittkonsolen.

### `component::teslemetry::config_subentries::vehicle::error::device_not_found`

- Engelska: No matching Tesla vehicle was found nearby over Bluetooth. Make sure the vehicle is within range of a Bluetooth adapter or proxy, then try again.
- Tidigare svenska: Inget matchande Tesla-fordon hittades i närheten via Bluetooth. Se till att fordonet är aktivt och inom räckhåll, försök sedan igen.
- Sparad svenska: Inget matchande Tesla-fordon hittades i närheten via Bluetooth. Kontrollera att fordonet är inom räckhåll för en Bluetooth-adapter eller proxy och försök igen.

### `component::teslemetry::config_subentries::vehicle::entry_type`

- Engelska: Local vehicle
- Tidigare svenska: Bluetooth-fordon
- Sparad svenska: Lokalt fordon

### `component::teslemetry::config_subentries::vehicle::abort::no_vehicles`

- Engelska: Home Assistant cannot access any vehicles in your Teslemetry account. Check that the vehicle is in your account and that Teslemetry has access to it.
- Tidigare svenska: Alla berättigade fordon i ditt Teslemetry-konto har redan lagts till via Bluetooth.
- Sparad svenska: Home Assistant kan inte komma åt några fordon i ditt Teslemetry-konto. Kontrollera att fordonet finns i kontot och att Teslemetry har åtkomst till det.

### `component::lawn_mower::triggers::became_idle::description`

- Engelska: Triggers when one or more lawn mowers become idle.
- Tidigare svenska: Utlöses när en eller flera gräsklippare blir inaktiv.
- Sparad svenska: Utlöses när en eller flera gräsklippare blir inaktiva.

### `component::bitvis::entity::sensor::han_msg_buffer_overflow::name`

- Engelska: HAN buffer overflows
- Tidigare svenska: HAN-buffert överflöden
- Sparad svenska: HAN-buffertöverflöden

### `component::metoffice::config::step::user::data_description::longitude`

- Engelska: The longitude of a location for which to request a weather forecast.
- Tidigare svenska: Longitud för den plats att begära väderprognos för.
- Sparad svenska: Longituden för platsen som väderprognosen ska hämtas för.

### `component::metoffice::config::step::user::data_description::latitude`

- Engelska: The latitude of a location for which to request a weather forecast.
- Tidigare svenska: Latitud för den plats att begära väderprognos för.
- Sparad svenska: Latituden för platsen som väderprognosen ska hämtas för.

### `component::metoffice::config::step::user::data_description::api_key`

- Engelska: Met Office DataHub API key for the Site Specific Global Spot API.
- Tidigare svenska: Met Office DataHub API-nyckel för det platsspecifika Global Spot API:et.
- Sparad svenska: Met Office DataHub-API-nyckel för det platsspecifika Global Spot-API:t.
