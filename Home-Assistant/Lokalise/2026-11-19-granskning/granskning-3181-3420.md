# Home Assistant Core – granskning 3181–3420

Sortering: ”Last added” vid insamlingen. Inget har ändrats i Lokalise. Referenser vars mål inte finns i underlaget markeras för senare kontroll.

## 3181. `component::exicom_spin_ble::entity::sensor::state::state::out_of_service`

**Engelska:** Out of service

**Befintlig svenska:** Ur drift

**Bedömning:** Ingen ändring föreslås.

## 3182. `component::exicom_spin_ble::entity::sensor::state::state::idle`

**Engelska:** [%key:common::state::idle%]

**Befintlig svenska:** Viloläge

**Kontextkontroll:** Kontrollera referensmålet `common::state::idle`; det ingår ännu inte i det insamlade underlaget.

## 3183. `component::exicom_spin_ble::entity::sensor::state::state::finishing`

**Engelska:** Finishing

**Befintlig svenska:** Avslutar

**Bedömning:** Ingen ändring föreslås.

## 3184. `component::exicom_spin_ble::entity::sensor::state::state::fault`

**Engelska:** [%key:common::state::fault%]

**Befintlig svenska:** Fel

**Kontextkontroll:** Kontrollera referensmålet `common::state::fault`; det ingår ännu inte i det insamlade underlaget.

## 3185. `component::exicom_spin_ble::entity::sensor::state::state::evse_suspended`

**Engelska:** Paused by charger

**Befintlig svenska:** Pausad av laddaren

**Bedömning:** Ingen ändring föreslås.

## 3186. `component::exicom_spin_ble::entity::sensor::state::state::ev_suspended`

**Engelska:** Paused by vehicle

**Befintlig svenska:** Pausad av fordonet

**Bedömning:** Ingen ändring föreslås.

## 3187. `component::exicom_spin_ble::entity::sensor::state::state::charging`

**Engelska:** [%key:common::state::charging%]

**Befintlig svenska:** Laddar

**Kontextkontroll:** Kontrollera referensmålet `common::state::charging`; det ingår ännu inte i det insamlade underlaget.

## 3188. `component::exicom_spin_ble::entity::sensor::state::state::booting`

**Engelska:** Starting up

**Befintlig svenska:** Startar upp

**Bedömning:** Ingen ändring föreslås.

## 3189. `component::exicom_spin_ble::entity::sensor::state::state::available`

**Engelska:** Available

**Befintlig svenska:** Tillgänglig

**Bedömning:** Ingen ändring föreslås.

## 3190. `component::exicom_spin_ble::entity::sensor::state::name`

**Engelska:** State

**Befintlig svenska:** Status

**Bedömning:** Ingen ändring föreslås.

## 3191. `component::exicom_spin_ble::entity::sensor::session_energy::name`

**Engelska:** Session energy

**Befintlig svenska:** Sessionsenergi

**Bedömning:** Ingen ändring föreslås.

## 3192. `component::exicom_spin_ble::entity::sensor::lifetime_energy::name`

**Engelska:** Lifetime energy

**Befintlig svenska:** Total energi

**Bedömning:** Ingen ändring föreslås.

## 3193. `component::exicom_spin_ble::config::step::user::description`

**Engelska:** [%key:component::bluetooth::config::step::user::description%]

**Befintlig svenska:** Välj en enhet att konfigurera

**Kontextkontroll:** Kontrollera referensmålet `component::bluetooth::config::step::user::description`; det ingår ännu inte i det insamlade underlaget.

## 3194. `component::exicom_spin_ble::config::step::user::data_description::address`

**Engelska:** The chargers discovered over Bluetooth, listed by serial number.

**Befintlig svenska:** Laddarna som hittades via Bluetooth, listade efter serienummer.

**Bedömning:** Ingen ändring föreslås.

## 3195. `component::exicom_spin_ble::config::step::user::data::address`

**Engelska:** [%key:common::config_flow::data::device%]

**Befintlig svenska:** Enhet

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::device`; det ingår ännu inte i det insamlade underlaget.

## 3196. `component::exicom_spin_ble::config::step::bluetooth_confirm::description`

**Engelska:** [%key:component::bluetooth::config::step::bluetooth_confirm::description%]

**Befintlig svenska:** Vill du konfigurera {name}?

**Kontextkontroll:** Kontrollera referensmålet `component::bluetooth::config::step::bluetooth_confirm::description`; det ingår ännu inte i det insamlade underlaget.

## 3197. `component::exicom_spin_ble::config::flow_title`

**Engelska:** {name}

**Befintlig svenska:** {name}

**Bedömning:** Ingen ändring föreslås.

## 3198. `component::exicom_spin_ble::config::error::cannot_connect`

**Engelska:** Failed to connect. Check that the charger is powered on and in Bluetooth range, and that no phone app is connected to it, since it accepts one Bluetooth client at a time.

**Befintlig svenska:** Det gick inte att ansluta. Kontrollera att laddaren är påslagen och inom Bluetooth-räckvidd samt att ingen mobilapp är ansluten till den, eftersom den bara accepterar en Bluetooth-klient åt gången.

**Bedömning:** Ingen ändring föreslås.

## 3199. `component::exicom_spin_ble::config::abort::not_supported`

**Engelska:** This Bluetooth device is not a Spin EV charger.

**Befintlig svenska:** Den här Bluetooth-enheten är inte en Spin EV-laddare.

**Bedömning:** Ingen ändring föreslås.

## 3200. `component::exicom_spin_ble::config::abort::no_devices_found`

**Engelska:** No Spin EV charger was found over Bluetooth. Check that the charger is powered on, that no phone app is connected to it, and that Home Assistant has a Bluetooth adapter or an ESPHome Bluetooth proxy in range of the charger.

**Befintlig svenska:** Ingen Spin EV-laddare hittades via Bluetooth. Kontrollera att laddaren är påslagen, att ingen mobilapp är ansluten till den och att Home Assistant har en Bluetooth-adapter eller en ESPHome-Bluetooth-proxy inom laddarens räckvidd.

**Bedömning:** Ingen ändring föreslås.

## 3201. `component::exicom_spin_ble::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_device%]

**Befintlig svenska:** Enheten är redan konfigurerad

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::abort::already_configured_device`; det ingår ännu inte i det insamlade underlaget.

## 3202. `component::seafile::config_subentries::library::step::user::data_description::backup_path`

**Engelska:** The folder in the library to store backups in. It is created when the first backup is uploaded.

**Befintlig svenska:** Mappen i biblioteket där säkerhetskopior lagras. Den skapas när den första säkerhetskopian skickas upp.

**Bedömning:** Ingen ändring föreslås.

## 3203. `component::seafile::config_subentries::library::step::user::data_description::backup`

**Engelska:** Make this library available as a backup location in Home Assistant.

**Befintlig svenska:** Gör det här biblioteket tillgängligt som plats för säkerhetskopior i Home Assistant.

**Bedömning:** Ingen ändring föreslås.

## 3204. `component::seafile::config_subentries::library::step::user::data::backup_path`

**Engelska:** Backup folder

**Befintlig svenska:** Mapp för säkerhetskopior

**Bedömning:** Ingen ändring föreslås.

## 3205. `component::seafile::config_subentries::library::step::user::data::backup`

**Engelska:** Store backups

**Befintlig svenska:** Lagra säkerhetskopior

**Bedömning:** Ingen ändring föreslås.

## 3206. `component::seafile::config_subentries::library::step::reconfigure::data_description::backup_path`

**Engelska:** [%key:component::seafile::config_subentries::library::step::user::data_description::backup_path%]

**Befintlig svenska:** Mappen i biblioteket där säkerhetskopior lagras. Den skapas när den första säkerhetskopian skickas upp.

**Bedömning:** Ingen ändring föreslås.

## 3207. `component::seafile::config_subentries::library::step::reconfigure::data_description::backup`

**Engelska:** [%key:component::seafile::config_subentries::library::step::user::data_description::backup%]

**Befintlig svenska:** Gör det här biblioteket tillgängligt som plats för säkerhetskopior i Home Assistant.

**Bedömning:** Ingen ändring föreslås.

## 3208. `component::seafile::config_subentries::library::step::reconfigure::data::backup_path`

**Engelska:** [%key:component::seafile::config_subentries::library::step::user::data::backup_path%]

**Befintlig svenska:** Mapp för säkerhetskopior

**Bedömning:** Ingen ändring föreslås.

## 3209. `component::seafile::config_subentries::library::step::reconfigure::data::backup`

**Engelska:** [%key:component::seafile::config_subentries::library::step::user::data::backup%]

**Befintlig svenska:** Lagra säkerhetskopior

**Bedömning:** Ingen ändring föreslås.

## 3210. `component::seafile::config_subentries::library::initiate_flow::reconfigure`

**Engelska:** Reconfigure library

**Befintlig svenska:** Konfigurera om bibliotek

**Bedömning:** Ingen ändring föreslås.

## 3211. `component::tuya::entity::sensor::meter_status::state::working`

**Engelska:** Working

**Befintlig svenska:** Arbetar

**Bedömning:** Ingen ändring föreslås.

## 3212. `component::tuya::entity::sensor::meter_status::state::warning`

**Engelska:** Warning

**Befintlig svenska:** Varning

**Bedömning:** Ingen ändring föreslås.

## 3213. `component::tuya::entity::sensor::meter_status::state::monitor`

**Engelska:** Monitoring

**Befintlig svenska:** Övervakning

**Bedömning:** Ingen ändring föreslås.

## 3214. `component::tuya::entity::sensor::meter_status::state::idle`

**Engelska:** [%key:common::state::idle%]

**Befintlig svenska:** Viloläge

**Kontextkontroll:** Kontrollera referensmålet `common::state::idle`; det ingår ännu inte i det insamlade underlaget.

## 3215. `component::tuya::entity::sensor::meter_status::state::close`

**Engelska:** [%key:common::state::closed%]

**Befintlig svenska:** Stängd

**Kontextkontroll:** Kontrollera referensmålet `common::state::closed`; det ingår ännu inte i det insamlade underlaget.

## 3216. `component::tuya::entity::sensor::meter_status::name`

**Engelska:** Status

**Befintlig svenska:** Status

**Bedömning:** Ingen ändring föreslås.

## 3217. `component::tuya::entity::sensor::energy_today::name`

**Engelska:** Energy today

**Befintlig svenska:** Energi i dag

**Bedömning:** Ingen ändring föreslås.

## 3218. `component::tuya::entity::number::power_warning_threshold::name`

**Engelska:** Power warning threshold

**Befintlig svenska:** Varningströskel för effekt

**Bedömning:** Ingen ändring föreslås.

## 3219. `component::spotify::config::abort::unique_id_mismatch`

**Engelska:** The Spotify account authenticated with does not match the account of this entry.

**Befintlig svenska:** Spotify-kontot som autentiserades stämmer inte överens med kontot för den här posten.

**Bedömning:** Ingen ändring föreslås.

## 3220. `component::abrp::exceptions::oauth2_token_refresh_failed::message`

**Engelska:** Failed to refresh the OAuth2 access token.

**Befintlig svenska:** Det gick inte att förnya OAuth2-åtkomsttoken.

**Förslag:** Det gick inte att förnya OAuth2-åtkomsttokenen.

## 3221. `component::abrp::exceptions::abrp_update_failed::message`

**Engelska:** Failed to fetch vehicle data from A Better Routeplanner.

**Befintlig svenska:** Det gick inte att hämta fordonsdata från A Better Routeplanner.

**Bedömning:** Ingen ändring föreslås.

## 3222. `component::abrp::exceptions::abrp_session_invalid::message`

**Engelska:** A Better Routeplanner rejected the authentication session; please re-authenticate.

**Befintlig svenska:** A Better Routeplanner avvisade autentiseringssessionen. Autentisera igen.

**Bedömning:** Ingen ändring föreslås.

## 3223. `component::abrp::entity::sensor::soh::name`

**Engelska:** State of health

**Befintlig svenska:** Hälsostatus

**Bedömning:** Ingen ändring föreslås.

## 3224. `component::abrp::entity::sensor::soe::name`

**Engelska:** SoE

**Befintlig svenska:** SoE

**Bedömning:** Ingen ändring föreslås.

## 3225. `component::abrp::entity::sensor::soc::name`

**Engelska:** SoC

**Befintlig svenska:** SoC

**Bedömning:** Ingen ändring föreslås.

## 3226. `component::abrp::entity::sensor::range::name`

**Engelska:** Range

**Befintlig svenska:** Räckvidd

**Bedömning:** Ingen ändring föreslås.

## 3227. `component::abrp::entity::sensor::odometer::name`

**Engelska:** Odometer

**Befintlig svenska:** Vägmätare

**Bedömning:** Ingen ändring föreslås.

## 3228. `component::abrp::entity::sensor::charging_state::state::plugged_in`

**Engelska:** Plugged in

**Befintlig svenska:** Ansluten

**Bedömning:** Ingen ändring föreslås.

## 3229. `component::abrp::entity::sensor::charging_state::state::not_charging`

**Engelska:** Not charging

**Befintlig svenska:** Laddar inte

**Bedömning:** Ingen ändring föreslås.

## 3230. `component::abrp::entity::sensor::charging_state::state::charging_unknown`

**Engelska:** Charging

**Befintlig svenska:** Laddar

**Bedömning:** Ingen ändring föreslås.

## 3231. `component::abrp::entity::sensor::charging_state::state::charging_dc`

**Engelska:** Charging (DC)

**Befintlig svenska:** Laddar (DC)

**Bedömning:** Ingen ändring föreslås.

## 3232. `component::abrp::entity::sensor::charging_state::state::charging_ac`

**Engelska:** Charging (AC)

**Befintlig svenska:** Laddar (AC)

**Bedömning:** Ingen ändring föreslås.

## 3233. `component::abrp::entity::sensor::charging_state::name`

**Engelska:** Charging state

**Befintlig svenska:** Laddningsstatus

**Bedömning:** Ingen ändring föreslås.

## 3234. `component::abrp::entity::sensor::calibrated_ref_cons::name`

**Engelska:** Calibrated ref cons

**Befintlig svenska:** Kalibrerad referensförbrukning

**Bedömning:** Ingen ändring föreslås.

## 3235. `component::abrp::entity::sensor::battery_temperature::name`

**Engelska:** Battery temperature

**Befintlig svenska:** Batteritemperatur

**Bedömning:** Ingen ändring föreslås.

## 3236. `component::abrp::entity::sensor::battery_capacity::name`

**Engelska:** Battery capacity

**Befintlig svenska:** Batterikapacitet

**Bedömning:** Ingen ändring föreslås.

## 3237. `component::abrp::config::step::pick_implementation::title`

**Engelska:** [%key:common::config_flow::title::oauth2_pick_implementation%]

**Befintlig svenska:** Välj autentiseringsmetod

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::title::oauth2_pick_implementation`; det ingår ännu inte i det insamlade underlaget.

## 3238. `component::abrp::config::step::pick_implementation::data_description::implementation`

**Engelska:** [%key:common::config_flow::description::implementation%]

**Befintlig svenska:** Uppgifterna som ska användas för autentisering.

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::description::implementation`; det ingår ännu inte i det insamlade underlaget.

## 3239. `component::abrp::config::step::pick_implementation::data::implementation`

**Engelska:** [%key:common::config_flow::data::implementation%]

**Befintlig svenska:** Programuppgifter

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::implementation`; det ingår ännu inte i det insamlade underlaget.

## 3240. `component::abrp::config::create_entry::default`

**Engelska:** [%key:common::config_flow::create_entry::authenticated%]

**Befintlig svenska:** Autentiseringen lyckades

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::create_entry::authenticated`; det ingår ännu inte i det insamlade underlaget.

## 3241. `component::abrp::config::abort::no_vehicles`

**Engelska:** No vehicles were found on this A Better Routeplanner account.

**Befintlig svenska:** Inga fordon hittades på det här A Better Routeplanner-kontot.

**Bedömning:** Ingen ändring föreslås.

## 3242. `component::abrp::config::abort::missing_configuration`

**Engelska:** [%key:common::config_flow::abort::oauth2_missing_configuration%]

**Befintlig svenska:** Komponenten är inte konfigurerad. Följ dokumentationen.

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::abort::oauth2_missing_configuration`; det ingår ännu inte i det insamlade underlaget.

## 3243. `component::abrp::config::abort::cloud_not_enabled`

**Engelska:** Please make sure you run Home Assistant with `{default_config}` enabled in your configuration.yaml.

**Befintlig svenska:** Kontrollera att Home Assistant körs med `{default_config}` aktiverat i configuration.yaml.

**Bedömning:** Ingen ändring föreslås.

## 3244. `component::abrp::config::abort::cannot_connect`

**Engelska:** Failed to connect to A Better Routeplanner.

**Befintlig svenska:** Det gick inte att ansluta till A Better Routeplanner.

**Bedömning:** Ingen ändring föreslås.

## 3245. `component::abrp::config::abort::api_unauthorized`

**Engelska:** Could not verify your A Better Routeplanner account.

**Befintlig svenska:** Det gick inte att verifiera ditt A Better Routeplanner-konto.

**Bedömning:** Ingen ändring föreslås.

## 3246. `component::abrp::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_account%]

**Befintlig svenska:** Kontot är redan konfigurerat

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::abort::already_configured_account`; det ingår ännu inte i det insamlade underlaget.

## 3247. `component::withings::config::abort::unique_id_mismatch`

**Engelska:** Authenticated account does not match the account of this entry. Please log in with the correct account.

**Befintlig svenska:** Det inloggade kontot stämmer inte med kontot för den här konfigurationsposten. Logga in med rätt konto.

**Bedömning:** Ingen ändring föreslås.

## 3248. `component::flic_button::selector::push_twist_mode::options::selector`

**Engelska:** Selector mode

**Befintlig svenska:** Väljarläge

**Bedömning:** Ingen ändring föreslås.

## 3249. `component::flic_button::selector::push_twist_mode::options::default`

**Engelska:** Default

**Befintlig svenska:** Standard

**Bedömning:** Ingen ändring föreslås.

## 3250. `component::flic_button::selector::push_twist_mode::options::continuous`

**Engelska:** Continuous

**Befintlig svenska:** Kontinuerlig

**Bedömning:** Ingen ändring föreslås.

## 3251. `component::flic_button::options::step::init::title`

**Engelska:** Flic Twist options

**Befintlig svenska:** Alternativ för Flic Twist

**Bedömning:** Ingen ändring föreslås.

## 3252. `component::flic_button::options::step::init::data_description::push_twist_mode`

**Engelska:** Controls the behavior when holding the button and twisting. Default mode fires increment and decrement events that clamp at boundaries. Continuous mode is like default but wraps around instead of clamping. Selector mode fires rotation and selector changed events.

**Befintlig svenska:** Styr beteendet när knappen hålls ned och vrids. Standardläget utlöser öknings- och minskningshändelser som begränsas vid ändlägena. Kontinuerligt läge fungerar som standardläget men börjar om i stället för att begränsas. Väljarläget utlöser rotations- och väljarändringshändelser.

**Bedömning:** Ingen ändring föreslås.

## 3253. `component::flic_button::options::step::init::data::push_twist_mode`

**Engelska:** Push twist mode

**Befintlig svenska:** Tryckvridningsläge

**Bedömning:** Ingen ändring föreslås.

## 3254. `component::flic_button::exceptions::set_position_failed::message`

**Engelska:** Failed to send the position to {address}. Make sure it is in range and try again.

**Befintlig svenska:** Kunde inte skicka positionen till {address}. Kontrollera att den är inom räckvidd och försök igen.

**Bedömning:** Ingen ändring föreslås.

## 3255. `component::flic_button::exceptions::cannot_connect::message`

**Engelska:** Failed to connect to {address}. Make sure it is in range and try again.

**Befintlig svenska:** Kunde inte ansluta till {address}. Kontrollera att den är inom räckvidd och försök igen.

**Bedömning:** Ingen ändring föreslås.

## 3256. `component::flic_button::entity::number::twist_position::name`

**Engelska:** Twist position

**Befintlig svenska:** Vridposition

**Bedömning:** Ingen ändring föreslås.

## 3257. `component::flic_button::entity::number::slot::name`

**Engelska:** Slot {slot_number}

**Befintlig svenska:** Plats {slot_number}

**Bedömning:** Ingen ändring föreslås.

## 3258. `component::flic_button::entity::number::push_twist_position::name`

**Engelska:** Push-twist position

**Befintlig svenska:** Position för tryckvridning

**Bedömning:** Ingen ändring föreslås.

## 3259. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::up`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::up%]

**Befintlig svenska:** Släppt

**Bedömning:** Ingen ändring föreslås.

## 3260. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::twist_increment`

**Engelska:** Twist incremented

**Befintlig svenska:** Vridning ökade

**Förslag:** Vridningen ökade

## 3261. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::twist_decrement`

**Engelska:** Twist decremented

**Befintlig svenska:** Vridning minskade

**Förslag:** Vridningen minskade

## 3262. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::push_twist_increment`

**Engelska:** Push-twist incremented

**Befintlig svenska:** Tryckvridning ökade

**Förslag:** Tryckvridningen ökade

## 3263. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::push_twist_decrement`

**Engelska:** Push-twist decremented

**Befintlig svenska:** Tryckvridning minskade

**Förslag:** Tryckvridningen minskade

## 3264. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::hold`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::hold%]

**Befintlig svenska:** Håll ned

**Bedömning:** Ingen ändring föreslås.

## 3265. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::down`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::down%]

**Befintlig svenska:** Nedtryckt

**Bedömning:** Ingen ändring föreslås.

## 3266. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::double_click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::double_click%]

**Befintlig svenska:** Dubbeltryck

**Bedömning:** Ingen ändring föreslås.

## 3267. `component::flic_button::entity::event::button_twist_default::state_attributes::event_type::state::click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::click%]

**Befintlig svenska:** Enkeltryck

**Bedömning:** Ingen ändring föreslås.

## 3268. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::up`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::up%]

**Befintlig svenska:** Släppt

**Bedömning:** Ingen ändring föreslås.

## 3269. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::selector_changed`

**Engelska:** Selector changed

**Befintlig svenska:** Väljaren ändrades

**Bedömning:** Ingen ändring föreslås.

## 3270. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::rotate_counter_clockwise`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::rotate_counter_clockwise%]

**Befintlig svenska:** Vridits moturs

**Bedömning:** Ingen ändring föreslås.

## 3271. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::rotate_clockwise`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::rotate_clockwise%]

**Befintlig svenska:** Vridits medurs

**Bedömning:** Ingen ändring föreslås.

## 3272. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::hold`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::hold%]

**Befintlig svenska:** Håll ned

**Bedömning:** Ingen ändring föreslås.

## 3273. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::down`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::down%]

**Befintlig svenska:** Nedtryckt

**Bedömning:** Ingen ändring föreslås.

## 3274. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::double_click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::double_click%]

**Befintlig svenska:** Dubbeltryck

**Bedömning:** Ingen ändring föreslås.

## 3275. `component::flic_button::entity::event::button_twist::state_attributes::event_type::state::click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::click%]

**Befintlig svenska:** Enkeltryck

**Bedömning:** Ingen ändring föreslås.

## 3276. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::up`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::up%]

**Befintlig svenska:** Släppt

**Bedömning:** Ingen ändring föreslås.

## 3277. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::swipe_up`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_up%]

**Befintlig svenska:** Svep upp

**Bedömning:** Ingen ändring föreslås.

## 3278. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::swipe_right`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_right%]

**Befintlig svenska:** Svep åt höger

**Bedömning:** Ingen ändring föreslås.

## 3279. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::swipe_left`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_left%]

**Befintlig svenska:** Svep åt vänster

**Bedömning:** Ingen ändring föreslås.

## 3280. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::swipe_down`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_down%]

**Befintlig svenska:** Svep ned

**Bedömning:** Ingen ändring föreslås.

## 3281. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::rotate_counter_clockwise`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::rotate_counter_clockwise%]

**Befintlig svenska:** Vridits moturs

**Bedömning:** Ingen ändring föreslås.

## 3282. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::rotate_clockwise`

**Engelska:** [%key:component::flic_button::entity::event::button_big::state_attributes::event_type::state::rotate_clockwise%]

**Befintlig svenska:** Vridits medurs

**Bedömning:** Ingen ändring föreslås.

## 3283. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::hold`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::hold%]

**Befintlig svenska:** Håll ned

**Bedömning:** Ingen ändring föreslås.

## 3284. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::down`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::down%]

**Befintlig svenska:** Nedtryckt

**Bedömning:** Ingen ändring föreslås.

## 3285. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::double_click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::double_click%]

**Befintlig svenska:** Dubbeltryck

**Bedömning:** Ingen ändring föreslås.

## 3286. `component::flic_button::entity::event::button_small::state_attributes::event_type::state::click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::click%]

**Befintlig svenska:** Enkeltryck

**Bedömning:** Ingen ändring föreslås.

## 3287. `component::flic_button::entity::event::button_small::name`

**Engelska:** Small button

**Befintlig svenska:** Liten knapp

**Bedömning:** Ingen ändring föreslås.

## 3288. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::up`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::up%]

**Befintlig svenska:** Släppt

**Bedömning:** Ingen ändring föreslås.

## 3289. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_up`

**Engelska:** Swipe up

**Befintlig svenska:** Svep upp

**Bedömning:** Ingen ändring föreslås.

## 3290. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_right`

**Engelska:** Swipe right

**Befintlig svenska:** Svep åt höger

**Bedömning:** Ingen ändring föreslås.

## 3291. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_left`

**Engelska:** Swipe left

**Befintlig svenska:** Svep åt vänster

**Bedömning:** Ingen ändring föreslås.

## 3292. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::swipe_down`

**Engelska:** Swipe down

**Befintlig svenska:** Svep ned

**Bedömning:** Ingen ändring föreslås.

## 3293. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::rotate_counter_clockwise`

**Engelska:** Rotated counter-clockwise

**Befintlig svenska:** Vridits moturs

**Bedömning:** Ingen ändring föreslås.

## 3294. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::rotate_clockwise`

**Engelska:** Rotated clockwise

**Befintlig svenska:** Vridits medurs

**Bedömning:** Ingen ändring föreslås.

## 3295. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::hold`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::hold%]

**Befintlig svenska:** Håll ned

**Bedömning:** Ingen ändring föreslås.

## 3296. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::down`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::down%]

**Befintlig svenska:** Nedtryckt

**Bedömning:** Ingen ändring föreslås.

## 3297. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::double_click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::double_click%]

**Befintlig svenska:** Dubbeltryck

**Bedömning:** Ingen ändring föreslås.

## 3298. `component::flic_button::entity::event::button_big::state_attributes::event_type::state::click`

**Engelska:** [%key:component::flic_button::entity::event::button::state_attributes::event_type::state::click%]

**Befintlig svenska:** Enkeltryck

**Bedömning:** Ingen ändring föreslås.

## 3299. `component::flic_button::entity::event::button_big::name`

**Engelska:** Big button

**Befintlig svenska:** Stor knapp

**Bedömning:** Ingen ändring föreslås.

## 3300. `component::flic_button::entity::event::button::state_attributes::event_type::state::up`

**Engelska:** Up

**Befintlig svenska:** Släppt

**Bedömning:** Ingen ändring föreslås.

## 3301. `component::flic_button::entity::event::button::state_attributes::event_type::state::hold`

**Engelska:** Hold

**Befintlig svenska:** Håll ned

**Bedömning:** Ingen ändring föreslås.

## 3302. `component::flic_button::entity::event::button::state_attributes::event_type::state::down`

**Engelska:** Down

**Befintlig svenska:** Nedtryckt

**Bedömning:** Ingen ändring föreslås.

## 3303. `component::flic_button::entity::event::button::state_attributes::event_type::state::double_click`

**Engelska:** Double push

**Befintlig svenska:** Dubbeltryck

**Bedömning:** Ingen ändring föreslås.

## 3304. `component::flic_button::entity::event::button::state_attributes::event_type::state::click`

**Engelska:** Single push

**Befintlig svenska:** Enkeltryck

**Bedömning:** Ingen ändring föreslås.

## 3305. `component::flic_button::config::step::user::title`

**Engelska:** [%key:component::flic_button::config::step::pair::title%]

**Befintlig svenska:** Parkoppla Flic-enhet

**Bedömning:** Ingen ändring föreslås.

## 3306. `component::flic_button::config::step::pair::title`

**Engelska:** Pair with Flic device

**Befintlig svenska:** Parkoppla Flic-enhet

**Bedömning:** Ingen ändring föreslås.

## 3307. `component::flic_button::config::step::pair::description`

**Engelska:** Push and hold {name} for 6 seconds to put it in pairing mode (1.5 seconds if it is new or was factory reset). It stays in pairing mode for up to 30 seconds. Then submit this form to pair.

**Befintlig svenska:** Håll ned {name} i 6 sekunder för att försätta den i parkopplingsläge (1,5 sekunder om den är ny eller har återställts till fabriksinställningarna). Den är kvar i parkopplingsläget i upp till 30 sekunder. Skicka sedan formuläret för att parkoppla.

**Bedömning:** Ingen ändring föreslås.

## 3308. `component::flic_button::config::step::bluetooth_confirm::title`

**Engelska:** Discovered Flic device

**Befintlig svenska:** Flic-enhet hittades

**Bedömning:** Ingen ändring föreslås.

## 3309. `component::flic_button::config::step::bluetooth_confirm::description`

**Engelska:** Set up {name}?

**Befintlig svenska:** Konfigurera {name}?

**Bedömning:** Ingen ändring föreslås.

## 3310. `component::flic_button::config::progress::wait_for_discovery`

**Engelska:** Push and hold your Flic for 6 seconds to put it in pairing mode (1.5 seconds if it is new or was factory reset)…

**Befintlig svenska:** Håll ned din Flic i 6 sekunder för att försätta den i parkopplingsläge (1,5 sekunder om den är ny eller har återställts till fabriksinställningarna) …

**Bedömning:** Ingen ändring föreslås.

## 3311. `component::flic_button::config::error::unknown`

**Engelska:** An unexpected error occurred during pairing.

**Befintlig svenska:** Ett oväntat fel uppstod vid parkopplingen.

**Bedömning:** Ingen ändring föreslås.

## 3312. `component::flic_button::config::error::pairing_failed`

**Engelska:** Pairing failed. Make sure your Flic is in pairing mode and try again.

**Befintlig svenska:** Parkopplingen misslyckades. Kontrollera att din Flic är i parkopplingsläge och försök igen.

**Bedömning:** Ingen ändring föreslås.

## 3313. `component::flic_button::config::error::invalid_signature`

**Engelska:** Invalid device signature during pairing.

**Befintlig svenska:** Ogiltig enhetssignatur vid parkoppling.

**Bedömning:** Ingen ändring föreslås.

## 3314. `component::flic_button::config::error::cannot_connect`

**Engelska:** Failed to connect to the device. Make sure it is in range and try again.

**Befintlig svenska:** Kunde inte ansluta till enheten. Kontrollera att den är inom räckvidd och försök igen.

**Bedömning:** Ingen ändring föreslås.

## 3315. `component::flic_button::config::abort::no_devices_found`

**Engelska:** [%key:common::config_flow::abort::no_devices_found%]

**Befintlig svenska:** Inga enheter hittades i nätverket

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::abort::no_devices_found`; det ingår ännu inte i det insamlade underlaget.

## 3316. `component::flic_button::config::abort::already_configured`

**Engelska:** This Flic device is already configured.

**Befintlig svenska:** Den här Flic-enheten är redan konfigurerad.

**Bedömning:** Ingen ändring föreslås.

## 3317. `component::co2signal::config::step::reconfigure::data::location`

**Engelska:** [%key:common::config_flow::data::location%]

**Befintlig svenska:** Plats

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::location`; det ingår ännu inte i det insamlade underlaget.

## 3318. `component::adguard::exceptions::install_update_failed::message`

**Engelska:** Failed to install the AdGuard Home update

**Befintlig svenska:** Det gick inte att installera uppdateringen av AdGuard Home.

**Bedömning:** Ingen ändring föreslås.

## 3319. `component::lutron_caseta::exceptions::setup_timeout::message`

**Engelska:** Timed out on {step} for {host}

**Befintlig svenska:** Tidsgränsen överskreds vid {step} för {host}

**Bedömning:** Ingen ändring föreslås.

## 3320. `component::lutron_caseta::exceptions::cannot_connect::message`

**Engelska:** Connection failed to {host}

**Befintlig svenska:** Det gick inte att ansluta till {host}

**Bedömning:** Ingen ändring föreslås.

## 3321. `component::dwd_weather_warnings::exceptions::position_error::message`

**Engelska:** An error occurred while fetching the position of {entity_id}

**Befintlig svenska:** Ett fel inträffade när positionen för {entity_id} hämtades

**Bedömning:** Ingen ändring föreslås.

## 3322. `component::switchbot_cloud::exceptions::update_connection_error::message`

**Engelska:** An error occurred while retrieving data from SwitchBot Cloud

**Befintlig svenska:** Ett fel inträffade när data hämtades från SwitchBot Cloud

**Bedömning:** Ingen ändring föreslås.

## 3323. `component::switchbot_cloud::exceptions::no_valid_mac_address::message`

**Engelska:** No valid MAC address obtained.

**Befintlig svenska:** Ingen giltig MAC-adress hämtades.

**Bedömning:** Ingen ändring föreslås.

## 3324. `component::ecovacs::exceptions::setup_error::message`

**Engelska:** Error during setup

**Befintlig svenska:** Fel vid konfiguration

**Bedömning:** Ingen ändring föreslås.

## 3325. `component::ecovacs::exceptions::invalid_auth::message`

**Engelska:** Invalid credentials

**Befintlig svenska:** Ogiltiga inloggningsuppgifter

**Bedömning:** Ingen ändring föreslås.

## 3326. `component::ecovacs::exceptions::device_verification_required::message`

**Engelska:** Device verification required

**Befintlig svenska:** Enhetsverifiering krävs

**Bedömning:** Ingen ändring föreslås.

## 3327. `component::broadlink::exceptions::update_failed::message`

**Engelska:** Failed to update the device

**Befintlig svenska:** Det gick inte att uppdatera enheten

**Bedömning:** Ingen ändring föreslås.

## 3328. `component::waze_travel_time::exceptions::update_error::message`

**Engelska:** An error occurred while retrieving data from Waze

**Befintlig svenska:** Ett fel inträffade när data hämtades från Waze

**Bedömning:** Ingen ändring föreslås.

## 3329. `component::waze_travel_time::exceptions::unknown_origin_or_destination::message`

**Engelska:** Unable to determine origin or destination

**Befintlig svenska:** Det går inte att fastställa start- eller destinationsplats

**Bedömning:** Ingen ändring föreslås.

## 3330. `component::waze_travel_time::exceptions::connection_error::message`

**Engelska:** An error occurred while connecting to Waze

**Befintlig svenska:** Ett fel inträffade vid anslutning till Waze

**Bedömning:** Ingen ändring föreslås.

## 3331. `component::tasmota::exceptions::camera_image_timeout::message`

**Engelska:** Timeout getting camera image from {entity_id}

**Befintlig svenska:** Tidsgränsen överskreds när en kamerabild hämtades från {entity_id}

**Bedömning:** Ingen ändring föreslås.

## 3332. `component::tasmota::exceptions::camera_image_error::message`

**Engelska:** An error occurred while getting a new camera image from {entity_id}

**Befintlig svenska:** Ett fel inträffade när en ny kamerabild hämtades från {entity_id}

**Bedömning:** Ingen ändring föreslås.

## 3333. `component::ipp::exceptions::invalid_response::message`

**Engelska:** Invalid response received from the printer

**Befintlig svenska:** Ogiltigt svar mottogs från skrivaren.

**Bedömning:** Ingen ändring föreslås.

## 3334. `component::modbus::exceptions::device_in_use::message`

**Engelska:** Modbus device {endpoint} is already in use with different link settings: {existing_params} against {params}.

**Befintlig svenska:** Modbus-enheten {endpoint} används redan med andra länkinställningar: {existing_params} i stället för {params}.

**Bedömning:** Ingen ändring föreslås.

## 3335. `component::mcp_server::exceptions::snapshot_error::message`

**Engelska:** An error occurred while reading the Assist context snapshot

**Befintlig svenska:** Ett fel inträffade när ögonblicksbilden av Assist-kontexten lästes in

**Bedömning:** Ingen ändring föreslås.

## 3336. `component::harmony::exceptions::connection_timeout::message`

**Engelska:** {name}: Connection timed out to hub at {address}:8088

**Befintlig svenska:** {name}: Tidsgränsen för anslutning till hubben på {address}:8088 överskreds

**Bedömning:** Ingen ändring föreslås.

## 3337. `component::harmony::exceptions::connection_error::message`

**Engelska:** {name}: An error occurred while connecting to hub at {address}:8088

**Befintlig svenska:** {name}: Ett fel uppstod vid anslutning till hubben på {address}:8088

**Bedömning:** Ingen ändring föreslås.

## 3338. `component::harmony::exceptions::cannot_connect::message`

**Engelska:** {name}: Unable to connect to hub at {address}:8088

**Befintlig svenska:** {name}: Det gick inte att ansluta till hubben på {address}:8088

**Bedömning:** Ingen ändring föreslås.

## 3339. `component::wyoming::exceptions::update_error::message`

**Engelska:** Unable to get info from {host}:{port}

**Befintlig svenska:** Det gick inte att hämta information från {host}:{port}

**Bedömning:** Ingen ändring föreslås.

## 3340. `component::wyoming::exceptions::service_error::message`

**Engelska:** Error from Wyoming service: {error}

**Befintlig svenska:** Fel från Wyoming-tjänsten: {error}

**Bedömning:** Ingen ändring föreslås.

## 3341. `component::wyoming::exceptions::cannot_connect::message`

**Engelska:** Unable to connect to {host}:{port}

**Befintlig svenska:** Det går inte att ansluta till {host}:{port}

**Bedömning:** Ingen ändring föreslås.

## 3342. `component::wiz::exceptions::update_failed::message`

**Engelska:** Failed to update the WiZ device at {ip_address}

**Befintlig svenska:** Det gick inte att uppdatera WiZ-enheten på {ip_address}

**Bedömning:** Ingen ändring föreslås.

## 3343. `component::wiz::exceptions::unexpected_device::message`

**Engelska:** Found WiZ device {mac} at {ip_address}, expected {expected_mac}

**Befintlig svenska:** Hittade WiZ-enheten {mac} på {ip_address}, förväntade {expected_mac}

**Bedömning:** Ingen ändring föreslås.

## 3344. `component::wiz::exceptions::cannot_connect::message`

**Engelska:** Failed to connect to the WiZ device at {ip_address}

**Befintlig svenska:** Det gick inte att ansluta till WiZ-enheten på {ip_address}

**Bedömning:** Ingen ändring föreslås.

## 3345. `component::raspberry_pi::exceptions::firmware_info_error::message`

**Engelska:** An error occurred while fetching the Raspberry Pi firmware info

**Befintlig svenska:** Ett fel inträffade när firmwareinformationen för Raspberry Pi hämtades

**Förslag:** Ett fel inträffade när information om den inbyggda programvaran för Raspberry Pi hämtades

## 3346. `component::nws::exceptions::observation_update_error::message`

**Engelska:** An error occurred while updating the observation data

**Befintlig svenska:** Ett fel inträffade när observationsdata uppdaterades

**Bedömning:** Ingen ändring föreslås.

## 3347. `component::nws::exceptions::no_data::message`

**Engelska:** No data returned.

**Befintlig svenska:** Inga data returnerades.

**Bedömning:** Ingen ändring föreslås.

## 3348. `component::otbr::exceptions::cannot_connect::message`

**Engelska:** Unable to connect to the OTBR

**Befintlig svenska:** Det gick inte att ansluta till OTBR.

**Bedömning:** Ingen ändring föreslås.

## 3349. `component::otbr::exceptions::api_error::message`

**Engelska:** Failed to call OTBR API

**Befintlig svenska:** Det gick inte att anropa OTBR API.

**Bedömning:** Ingen ändring föreslås.

## 3350. `component::speedtestdotnet::exceptions::update_failed::message`

**Engelska:** An error occurred while running the speed test

**Befintlig svenska:** Ett fel inträffade när hastighetstestet kördes

**Bedömning:** Ingen ändring föreslås.

## 3351. `component::speedtestdotnet::exceptions::server_not_found::message`

**Engelska:** Selected server is not found

**Befintlig svenska:** Den valda servern hittades inte

**Bedömning:** Ingen ändring föreslås.

## 3352. `component::openweathermap::exceptions::update_error::message`

**Engelska:** An error occurred while retrieving data from OpenWeatherMap

**Befintlig svenska:** Ett fel inträffade när data hämtades från OpenWeatherMap

**Bedömning:** Ingen ändring föreslås.

## 3353. `component::upnp::exceptions::device_not_discovered::message`

**Engelska:** Device not discovered: {usn}

**Befintlig svenska:** Enheten hittades inte: {usn}

**Bedömning:** Ingen ändring föreslås.

## 3354. `component::upnp::exceptions::communication_error::message`

**Engelska:** Unable to communicate with IGD at: {device_url}

**Befintlig svenska:** Det går inte att kommunicera med IGD på {device_url}

**Bedömning:** Ingen ändring föreslås.

## 3355. `component::upnp::exceptions::cannot_connect::message`

**Engelska:** Error connecting to device at location: {location}

**Befintlig svenska:** Fel vid anslutning till enheten på platsen {location}

**Bedömning:** Ingen ändring föreslås.

## 3356. `component::wemo::exceptions::update_failed::message`

**Engelska:** WeMo update failed

**Befintlig svenska:** WeMo-uppdateringen misslyckades

**Bedömning:** Ingen ändring föreslås.

## 3357. `component::rest::exceptions::ssl_error::message`

**Engelska:** An SSL error occurred while connecting to {resource}

**Befintlig svenska:** Ett SSL-fel inträffade vid anslutning till {resource}

**Bedömning:** Ingen ändring föreslås.

## 3358. `component::rest::exceptions::resource_not_set::message`

**Engelska:** The resource is not set

**Befintlig svenska:** Resursen är inte angiven

**Bedömning:** Ingen ändring föreslås.

## 3359. `component::rest::exceptions::no_route::message`

**Engelska:** No route to resource/endpoint: {resource}

**Befintlig svenska:** Ingen väg till resursen eller ändpunkten: {resource}

**Bedömning:** Ingen ändring föreslås.

## 3360. `component::thread::exceptions::preferred_extended_address_required::message`

**Engelska:** Must set preferred extended address with preferred border agent ID

**Befintlig svenska:** Du måste ange önskad utökad adress tillsammans med ID för önskad gränsagent

**Bedömning:** Ingen ändring föreslås.

## 3361. `component::thread::exceptions::invalid_dataset::message`

**Engelska:** Invalid dataset

**Befintlig svenska:** Ogiltig datauppsättning

**Bedömning:** Ingen ändring föreslås.

## 3362. `component::co2signal::exceptions::update_error::message`

**Engelska:** An error occurred while retrieving data from Electricity Maps: {error}

**Befintlig svenska:** Ett fel inträffade när data hämtades från Electricity Maps: {error}

**Bedömning:** Ingen ändring föreslås.

## 3363. `component::portainer::config_subentries::environment::abort::unknown`

**Engelska:** [%key:common::config_flow::error::unknown%]

**Befintlig svenska:** Oväntat fel

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::unknown`; det ingår ännu inte i det insamlade underlaget.

## 3364. `component::zha::exceptions::not_zigbee_device::message`

**Engelska:** Device {ieee} is not a Zigbee device, so this action cannot be performed.

**Befintlig svenska:** Enheten {ieee} är inte en Zigbee-enhet, så åtgärden kan inte utföras.

**Bedömning:** Ingen ändring föreslås.

## 3365. `component::zha::entity::sensor::wiring_mode::name`

**Engelska:** Wiring mode

**Befintlig svenska:** Kopplingsläge

**Bedömning:** Ingen ändring föreslås.

## 3366. `component::zha::entity::sensor::water_warning::name`

**Engelska:** Water warning

**Befintlig svenska:** Vattenvarning

**Bedömning:** Ingen ändring föreslås.

## 3367. `component::zha::entity::sensor::setpoint_change_source_timestamp::name`

**Engelska:** Setpoint change source timestamp

**Befintlig svenska:** Tidsstämpel för källa till ändring av börvärde

**Bedömning:** Ingen ändring föreslås.

## 3368. `component::zha::entity::sensor::relay_address::name`

**Engelska:** Relay address

**Befintlig svenska:** Reläadress

**Bedömning:** Ingen ändring föreslås.

## 3369. `component::zha::entity::sensor::cooktop_temperature::name`

**Engelska:** Cooktop temperature

**Befintlig svenska:** Spishällstemperatur

**Bedömning:** Ingen ändring föreslås.

## 3370. `component::zha::entity::sensor::button_click_duration::name`

**Engelska:** Button click duration

**Befintlig svenska:** Varaktighet för knapptryckning

**Bedömning:** Ingen ändring föreslås.

## 3371. `component::zha::entity::sensor::button_click_count::name`

**Engelska:** Button click count

**Befintlig svenska:** Antal knapptryckningar

**Bedömning:** Ingen ändring föreslås.

## 3372. `component::zha::entity::sensor::alarm_status::name`

**Engelska:** Alarm status

**Befintlig svenska:** Larmstatus

**Bedömning:** Ingen ändring föreslås.

## 3373. `component::zha::entity::select::dimming_curve::name`

**Engelska:** Dimming curve

**Befintlig svenska:** Dämpningskurva

**Bedömning:** Ingen ändring föreslås.

## 3374. `component::zha::entity::select::control_mode::name`

**Engelska:** Control mode

**Befintlig svenska:** Styrningsläge

**Bedömning:** Ingen ändring föreslås.

## 3375. `component::zha::entity::number::stall_time::name`

**Engelska:** Stall time

**Befintlig svenska:** Stoppstid

**Bedömning:** Ingen ändring föreslås.

## 3376. `component::zha::entity::number::soil_warning_threshold::name`

**Engelska:** Soil warning threshold

**Befintlig svenska:** Varningströskel för markfuktighet

**Bedömning:** Ingen ändring föreslås.

## 3377. `component::zha::entity::number::soil_sampling_interval::name`

**Engelska:** Soil sampling interval

**Befintlig svenska:** Intervall för markprovtagning

**Kontextkontroll:** Kontrollera i enhetens dokumentation om mätintervallet avser jordfuktighet eller faktisk provtagning.

## 3378. `component::zha::entity::number::soil_moisture_calibration::name`

**Engelska:** Soil moisture calibration

**Befintlig svenska:** Kalibrering av markfuktighet

**Bedömning:** Ingen ändring föreslås.

## 3379. `component::zha::entity::number::pre_warning_time::name`

**Engelska:** Pre warning time

**Befintlig svenska:** Förvarningstid

**Bedömning:** Ingen ändring föreslås.

## 3380. `component::zha::entity::number::on_time_reload::name`

**Engelska:** On time reload

**Befintlig svenska:** Återställning av påslagen tid

**Bedömning:** Ingen ändring föreslås.

## 3381. `component::zha::entity::number::max_moisture::name`

**Engelska:** Max moisture

**Befintlig svenska:** Högsta fuktnivå

**Bedömning:** Ingen ändring föreslås.

## 3382. `component::zha::entity::number::illuminance_calibration::name`

**Engelska:** Illuminance calibration

**Befintlig svenska:** Kalibrering av belysningsstyrka

**Bedömning:** Ingen ändring föreslås.

## 3383. `component::zha::entity::event::rocker_top::name`

**Engelska:** Rocker {rocker} top

**Befintlig svenska:** Vippknapp {rocker}, övre

**Bedömning:** Ingen ändring föreslås.

## 3384. `component::zha::entity::event::rocker_bottom::name`

**Engelska:** Rocker {rocker} bottom

**Befintlig svenska:** Vippknapp {rocker}, nedre

**Bedömning:** Ingen ändring föreslås.

## 3385. `component::zha::entity::event::button_numbered::name`

**Engelska:** Button {number}

**Befintlig svenska:** Knapp {number}

**Bedömning:** Ingen ändring föreslås.

## 3386. `component::zha::entity::binary_sensor::cooktop_active::name`

**Engelska:** Cooktop active

**Befintlig svenska:** Spishäll aktiv

**Bedömning:** Ingen ändring föreslås.

## 3387. `component::zha::entity::binary_sensor::battery_alarm::name`

**Engelska:** Battery alarm

**Befintlig svenska:** Batterilarm

**Bedömning:** Ingen ändring föreslås.

## 3388. `component::zha::entity::binary_sensor::active_water_leak::name`

**Engelska:** Active water leak

**Befintlig svenska:** Aktivt vattenläckage

**Bedömning:** Ingen ändring föreslås.

## 3389. `component::portainer::config_subentries::environment::step::user::title`

**Engelska:** Add a Portainer environment

**Befintlig svenska:** Lägg till en Portainer-miljö

**Bedömning:** Ingen ändring föreslås.

## 3390. `component::portainer::config_subentries::environment::step::user::description`

**Engelska:** Select a Portainer environment to add as a device in Home Assistant.

**Befintlig svenska:** Välj en Portainer-miljö att lägga till som en enhet i Home Assistant.

**Bedömning:** Ingen ändring föreslås.

## 3391. `component::portainer::config_subentries::environment::step::user::data::endpoint_id`

**Engelska:** Environment

**Befintlig svenska:** Miljö

**Bedömning:** Ingen ändring föreslås.

## 3392. `component::portainer::config_subentries::environment::initiate_flow::user`

**Engelska:** Add environment

**Befintlig svenska:** Lägg till miljö

**Bedömning:** Ingen ändring föreslås.

## 3393. `component::portainer::config_subentries::environment::entry_type`

**Engelska:** Environment

**Befintlig svenska:** Miljö

**Bedömning:** Ingen ändring föreslås.

## 3394. `component::portainer::config_subentries::environment::abort::timeout_connect`

**Engelska:** [%key:common::config_flow::error::timeout_connect%]

**Befintlig svenska:** Tidsgränsen överskreds vid anslutning

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::timeout_connect`; det ingår ännu inte i det insamlade underlaget.

## 3395. `component::portainer::config_subentries::environment::abort::no_new_environments`

**Engelska:** All available environments on this Portainer server have already been added.

**Befintlig svenska:** Alla tillgängliga miljöer på den här Portainer-servern har redan lagts till.

**Bedömning:** Ingen ändring föreslås.

## 3396. `component::portainer::config_subentries::environment::abort::invalid_auth`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** Ogiltig autentisering

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::invalid_auth`; det ingår ännu inte i det insamlade underlaget.

## 3397. `component::portainer::config_subentries::environment::abort::config_entry_not_loaded`

**Engelska:** Cannot add an environment while the Portainer integration is not loaded.

**Befintlig svenska:** Det går inte att lägga till en miljö när Portainer-integrationen inte är inläst.

**Bedömning:** Ingen ändring föreslås.

## 3398. `component::portainer::config_subentries::environment::abort::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::cannot_connect`; det ingår ännu inte i det insamlade underlaget.

## 3399. `component::seafile::exceptions::timeout_connect::message`

**Engelska:** Timed out while connecting to the Seafile server.

**Befintlig svenska:** Tidsgränsen överskreds vid anslutning till Seafile-servern.

**Bedömning:** Ingen ändring föreslås.

## 3400. `component::seafile::exceptions::invalid_auth::message`

**Engelska:** The access token of the Seafile account is no longer valid.

**Befintlig svenska:** Åtkomsttoken för Seafile-kontot är inte längre giltig.

**Förslag:** Åtkomsttokenen för Seafile-kontot är inte längre giltig.

## 3401. `component::seafile::exceptions::cannot_connect::message`

**Engelska:** An error occurred while retrieving data from the Seafile server.

**Befintlig svenska:** Ett fel uppstod när data hämtades från Seafile-servern.

**Bedömning:** Ingen ändring föreslås.

## 3402. `component::seafile::entity::sensor::size::name`

**Engelska:** Size

**Befintlig svenska:** Storlek

**Bedömning:** Ingen ändring föreslås.

## 3403. `component::seafile::entity::sensor::last_modified::name`

**Engelska:** Last modified

**Befintlig svenska:** Senast ändrad

**Bedömning:** Ingen ändring föreslås.

## 3404. `component::seafile::entity::sensor::file_count::unit_of_measurement`

**Engelska:** files

**Befintlig svenska:** filer

**Bedömning:** Ingen ändring föreslås.

## 3405. `component::seafile::entity::sensor::file_count::name`

**Engelska:** Files

**Befintlig svenska:** Filer

**Bedömning:** Ingen ändring föreslås.

## 3406. `component::seafile::config_subentries::library::step::user::data_description::library_id`

**Engelska:** The library to add. Encrypted libraries are not supported.

**Befintlig svenska:** Biblioteket som ska läggas till. Krypterade bibliotek stöds inte.

**Bedömning:** Ingen ändring föreslås.

## 3407. `component::seafile::config_subentries::library::step::user::data::library_id`

**Engelska:** Library

**Befintlig svenska:** Bibliotek

**Bedömning:** Ingen ändring föreslås.

## 3408. `component::seafile::config_subentries::library::initiate_flow::user`

**Engelska:** Add library

**Befintlig svenska:** Lägg till bibliotek

**Bedömning:** Ingen ändring föreslås.

## 3409. `component::seafile::config_subentries::library::entry_type`

**Engelska:** Library

**Befintlig svenska:** Bibliotek

**Bedömning:** Ingen ändring föreslås.

## 3410. `component::seafile::config_subentries::library::abort::no_libraries`

**Engelska:** All libraries of this account have been added already, or they are encrypted.

**Befintlig svenska:** Alla bibliotek för det här kontot har redan lagts till eller är krypterade.

**Bedömning:** Ingen ändring föreslås.

## 3411. `component::seafile::config_subentries::library::abort::entry_not_loaded`

**Engelska:** The Seafile account is not loaded. Make sure it is set up and running before adding a library.

**Befintlig svenska:** Seafile-kontot har inte lästs in. Kontrollera att det är konfigurerat och körs innan du lägger till ett bibliotek.

**Bedömning:** Ingen ändring föreslås.

## 3412. `component::seafile::config_subentries::library::abort::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Kunde inte ansluta

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::cannot_connect`; det ingår ännu inte i det insamlade underlaget.

## 3413. `component::seafile::config::step::user::data_description::verify_ssl`

**Engelska:** Turn off for servers with a self-signed certificate.

**Befintlig svenska:** Stäng av för servrar med självsignerat certifikat.

**Bedömning:** Ingen ändring föreslås.

## 3414. `component::seafile::config::step::user::data_description::username`

**Engelska:** The email address or login ID of your Seafile account.

**Befintlig svenska:** E-postadressen eller inloggnings-ID:t för ditt Seafile-konto.

**Bedömning:** Ingen ändring föreslås.

## 3415. `component::seafile::config::step::user::data_description::url`

**Engelska:** The address you use to open Seafile in your browser.

**Befintlig svenska:** Adressen du använder för att öppna Seafile i webbläsaren.

**Bedömning:** Ingen ändring föreslås.

## 3416. `component::seafile::config::step::user::data_description::password`

**Engelska:** The password of your Seafile account. It is only used to create an access token and is not stored.

**Befintlig svenska:** Lösenordet för ditt Seafile-konto. Det används endast för att skapa en åtkomsttoken och sparas inte.

**Bedömning:** Ingen ändring föreslås.

## 3417. `component::seafile::config::step::user::data::verify_ssl`

**Engelska:** [%key:common::config_flow::data::verify_ssl%]

**Befintlig svenska:** Verifiera SSL-certifikat

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::verify_ssl`; det ingår ännu inte i det insamlade underlaget.

## 3418. `component::seafile::config::step::user::data::username`

**Engelska:** [%key:common::config_flow::data::username%]

**Befintlig svenska:** Användarnamn

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::username`; det ingår ännu inte i det insamlade underlaget.

## 3419. `component::seafile::config::step::user::data::url`

**Engelska:** [%key:common::config_flow::data::url%]

**Befintlig svenska:** URL

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::url`; det ingår ännu inte i det insamlade underlaget.

## 3420. `component::seafile::config::step::user::data::password`

**Engelska:** [%key:common::config_flow::data::password%]

**Befintlig svenska:** Lösenord

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::password`; det ingår ännu inte i det insamlade underlaget.
