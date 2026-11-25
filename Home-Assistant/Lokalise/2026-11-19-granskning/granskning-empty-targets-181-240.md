# Home Assistant Core: tidigare tomma svenska mål 181–240

- Granskade och sparade: **60/60**. Källrevision `86a2eabe7e43f526db5821ef068087ce8404ae07`; aktuell engelsk källtext och svensk måltext verifierades via Lokalise API.
- 15 unika referensmål livekontrollerade; inga avvikelser. Platshållare matchar i samtliga rader.
- `svlang skrivregler`: inga fel. Hunspell-träffar för 15-minutersprognos, PM-former, produktnamn och platshållaren `name` bedömdes i sammanhanget.
- Foreca dokumenterar `icing` som is/underkylt regn; därför används **Underkylt regn** i nederbördstypen ([Foreca Point Forecast API](https://developer.foreca.com/docs/point-forecasts), [Foreca vädersymboler](https://developer.foreca.com/resources)).
- TMX: 17 367 poster, validerad. Se `../Lokalise/2026-11-25-reviewed-empty-targets-181-240.json` och referensunderlaget `../Lokalise/2026-11-25-reference-targets-empty-181-240-live.json`.

## Radgranskning

### `component::elvia::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: Elvia authentication and reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::elvia::exceptions::invalid_auth::message`
- Källa: Authentication with Elvia failed
- Föreslagen och sparad svenska: Autentiseringen med Elvia misslyckades.
- Motivering: Elvia authentication and reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::aqi_co::name`
- Källa: Carbon monoxide index
- Föreslagen och sparad svenska: Kolmonoxidindex
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::aqi_no2::name`
- Källa: Nitrogen dioxide index
- Föreslagen och sparad svenska: Kvävedioxidindex
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::aqi_o3::name`
- Källa: Ozone index
- Föreslagen och sparad svenska: Ozonindex
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::aqi_pm10::name`
- Källa: PM10 index
- Föreslagen och sparad svenska: PM10-index
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::aqi_pm25::name`
- Källa: PM2.5 index
- Föreslagen och sparad svenska: PM2,5-index
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::aqi_so2::name`
- Källa: Sulphur dioxide index
- Föreslagen och sparad svenska: Svaveldioxidindex
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::name`
- Källa: Dominant pollutant
- Föreslagen och sparad svenska: Dominerande luftförorening
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::state::carbon_monoxide`
- Källa: Carbon monoxide
- Föreslagen och sparad svenska: Kolmonoxid
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::state::nitrogen_dioxide`
- Källa: Nitrogen dioxide
- Föreslagen och sparad svenska: Kvävedioxid
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::state::ozone`
- Källa: Ozone
- Föreslagen och sparad svenska: Ozon
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::state::pm10`
- Källa: PM10
- Föreslagen och sparad svenska: PM10
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::state::pm25`
- Källa: PM2.5
- Föreslagen och sparad svenska: PM2,5
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::dominant_pollutant::state::sulphur_dioxide`
- Källa: Sulphur dioxide
- Föreslagen och sparad svenska: Svaveldioxid
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation::name`
- Källa: Observed hourly precipitation
- Föreslagen och sparad svenska: Uppmätt nederbörd per timme
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation_type::name`
- Källa: Observed precipitation type
- Föreslagen och sparad svenska: Uppmätt nederbördstyp
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation_type::state::hail`
- Källa: Hail
- Föreslagen och sparad svenska: Hagel
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation_type::state::icing`
- Källa: Icing
- Föreslagen och sparad svenska: Underkylt regn
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation_type::state::rain`
- Källa: Rain
- Föreslagen och sparad svenska: Regn
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation_type::state::sleet`
- Källa: Sleet
- Föreslagen och sparad svenska: Snöblandat regn
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::entity::sensor::observed_precipitation_type::state::snow`
- Källa: Snow
- Föreslagen och sparad svenska: Snö
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::exceptions::air_quality_forecast_error::message`
- Källa: Error fetching the air quality forecast.
- Föreslagen och sparad svenska: Det gick inte att hämta luftkvalitetsprognosen.
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::exceptions::air_quality_update_error::message`
- Källa: Error fetching the air quality.
- Föreslagen och sparad svenska: Det gick inte att hämta luftkvaliteten.
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::exceptions::fifteen_minute_forecast_error::message`
- Källa: Error fetching the 15-minute forecast.
- Föreslagen och sparad svenska: Det gick inte att hämta 15-minutersprognosen.
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::services::get_15_minute_forecast::description`
- Källa: Retrieves the forecast in 15-minute steps for the next three hours, in the weather entity's units. Every call makes a request to the Foreca Weather API and counts toward the daily limit of your plan.
- Föreslagen och sparad svenska: Hämtar prognosen i steg om 15 minuter för de kommande tre timmarna, i väderentitetens enheter. Varje anrop gör en förfrågan till Foreca Weather API och räknas in i planens dagliga gräns.
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::services::get_15_minute_forecast::name`
- Källa: Get 15-minute forecast
- Föreslagen och sparad svenska: Hämta 15-minutersprognos
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::services::get_air_quality_forecast::description`
- Källa: Retrieves the air quality index forecast, hourly for up to 85 hours or daily for 4 days. Every call makes a request to the Foreca Weather API and counts toward the daily limit of your plan.
- Föreslagen och sparad svenska: Hämtar prognosen för luftkvalitetsindex, per timme i upp till 85 timmar eller per dag i fyra dagar. Varje anrop gör en förfrågan till Foreca Weather API och räknas in i planens dagliga gräns.
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::services::get_air_quality_forecast::fields::type::description`
- Källa: The forecast to return.
- Föreslagen och sparad svenska: Prognosen som ska hämtas.
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::services::get_air_quality_forecast::fields::type::name`
- Källa: Forecast type
- Föreslagen och sparad svenska: Prognostyp
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::foreca::services::get_air_quality_forecast::name`
- Källa: Get air quality forecast
- Föreslagen och sparad svenska: Hämta luftkvalitetsprognos
- Motivering: Foreca air-quality or precipitation context; PM2,5 follows the live Home Assistant pollutant reference; “icing” is Foreca’s ice/freezing-rain category.
- Status: sparad och återläst i Lokalise.

### `component::fuelprices_dk::config_subentries::station::step::user::description`
- Källa: Try again to load the list of fuel companies.
- Föreslagen och sparad svenska: Försök igen att läsa in listan över bränsleföretag.
- Motivering: Fuelprices.dk station-list loading and API error context.
- Status: sparad och återläst i Lokalise.

### `component::fuelprices_dk::exceptions::cannot_connect::message`
- Källa: Failed to connect
- Föreslagen och sparad svenska: Det gick inte att ansluta
- Motivering: Fuelprices.dk station-list loading and API error context.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fuelprices_dk::exceptions::rate_limit_exceeded::message`
- Källa: Too many requests to the API. Please try again later.
- Föreslagen och sparad svenska: För många förfrågningar till API:et. Försök igen senare.
- Motivering: Fuelprices.dk station-list loading and API error context.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fuelprices_dk::exceptions::request_timeout::message`
- Källa: Timeout while establishing a connection
- Föreslagen och sparad svenska: Tidsgränsen överskreds när anslutningen upprättades.
- Motivering: Fuelprices.dk station-list loading and API error context.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fuelprices_dk::exceptions::server_error::message`
- Källa: Fuelprices.dk returned a server error.
- Föreslagen och sparad svenska: Fuelprices.dk returnerade ett serverfel.
- Motivering: Fuelprices.dk station-list loading and API error context.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::abort::already_configured`
- Källa: Device is already configured
- Föreslagen och sparad svenska: Enheten är redan konfigurerad
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::abort::no_infrared_emitters`
- Källa: No infrared emitter entities found. Please set up an infrared device first.
- Föreslagen och sparad svenska: Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::error::no_hvac_modes`
- Källa: Select at least one supported mode.
- Föreslagen och sparad svenska: Välj minst ett läge som stöds.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data::hvac_modes`
- Källa: Supported modes
- Föreslagen och sparad svenska: Lägen som stöds
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data::infrared_emitter_entity_id`
- Källa: Infrared emitter
- Föreslagen och sparad svenska: Infraröd sändare
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data::infrared_receiver_entity_id`
- Källa: Infrared receiver
- Föreslagen och sparad svenska: Infraröd mottagare
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data::protocol`
- Källa: Temperature steps
- Föreslagen och sparad svenska: Temperatursteg
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data_description::hvac_modes`
- Källa: Select the operating modes your AC unit supports. Heat is not available on all models.
- Föreslagen och sparad svenska: Välj de driftlägen som luftkonditioneringen stöder. Värme finns inte på alla modeller.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data_description::infrared_emitter_entity_id`
- Källa: The infrared emitter entity to use for sending commands.
- Föreslagen och sparad svenska: Sändarentiteten som ska användas för att skicka infraröda kommandon.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data_description::infrared_receiver_entity_id`
- Källa: Optional — allows the integration to update state when the physical remote is used.
- Föreslagen och sparad svenska: Valfritt – gör att integrationen kan uppdatera status när den fysiska fjärrkontrollen används.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::data_description::protocol`
- Källa: Half degrees are only carried by the extended message format. Select it if your remote's display shows half degrees in Celsius, such as 24.5.
- Föreslagen och sparad svenska: Halva grader överförs bara med det utökade meddelandeformatet. Välj det om fjärrkontrollens skärm visar halva grader i Celsius, till exempel 24,5.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::description`
- Källa: Select an infrared emitter and the modes your Fujitsu AC supports.
- Föreslagen och sparad svenska: Välj en infraröd sändare och de lägen som din Fujitsu-luftkonditionering stöder.
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::config::step::user::title`
- Källa: Set up Fujitsu AC
- Föreslagen och sparad svenska: Konfigurera Fujitsu-luftkonditionering
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::entity::climate::fujitsu_ac::state_attributes::fan_mode::state::quiet`
- Källa: Quiet
- Föreslagen och sparad svenska: Tyst
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::hvac_modes::options::cool`
- Källa: Cool
- Föreslagen och sparad svenska: Kyla
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::hvac_modes::options::dry`
- Källa: Dry
- Föreslagen och sparad svenska: Avfuktning
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::hvac_modes::options::fan_only`
- Källa: Fan only
- Föreslagen och sparad svenska: Endast fläkt
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::hvac_modes::options::heat`
- Källa: Heat
- Föreslagen och sparad svenska: Värme
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::hvac_modes::options::heat_cool`
- Källa: Heat/Cool
- Föreslagen och sparad svenska: Värme/kyla
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::protocol::options::extended`
- Källa: Half degrees
- Föreslagen och sparad svenska: Halva grader
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::fujitsu_infrared::selector::protocol::options::standard`
- Källa: Whole degrees
- Föreslagen och sparad svenska: Hela grader
- Motivering: Fujitsu air-conditioning modes and infrared setup; shared infrared terms match live references.
- Status: sparad och återläst i Lokalise.

### `component::google_health::entity::sensor::body_mass_index::name`
- Källa: Body mass index
- Föreslagen och sparad svenska: Kroppsmasseindex
- Motivering: Google Health measurement names.
- Status: sparad och återläst i Lokalise.

### `component::google_health::entity::sensor::heart_rate_variability::name`
- Källa: Heart rate variability
- Föreslagen och sparad svenska: Hjärtfrekvensvariabilitet
- Motivering: Google Health measurement names.
- Status: sparad och återläst i Lokalise.

### `component::google_health::entity::sensor::height::name`
- Källa: Height
- Föreslagen och sparad svenska: Längd
- Motivering: Google Health measurement names.
- Status: sparad och återläst i Lokalise.

## Kvarvarande arbete

Core-granskningen fortsätter; inga utanför denna batch markeras som klara.
