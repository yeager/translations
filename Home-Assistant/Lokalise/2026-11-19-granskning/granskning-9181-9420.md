# Home Assistant Core – granskning 9181–9420

Sortering: ”Last added” vid insamlingen. Den här rapporten är en tidigare granskning; aktuell kontroll och liveändringar redovisas i tillägget längst ned.

## 9181. `component::neopool::exceptions::device_time_write_failed::message`

**Engelska:** Failed to write the device time: {error}

**Befintlig svenska:** Det gick inte att skriva enhetens tid: {error}

**Bedömning:** Ingen ändring föreslås.

## 9182. `component::neopool::exceptions::device_time_read_failed::message`

**Engelska:** Failed to read the device time: {error}

**Befintlig svenska:** Det gick inte att läsa enhetens tid: {error}

**Bedömning:** Ingen ändring föreslås.

## 9183. `component::neopool::exceptions::device_not_found::message`

**Engelska:** No loaded NeoPool device found for device_id {device_id}

**Befintlig svenska:** Ingen inläst NeoPool-enhet hittades för device_id {device_id}

**Bedömning:** Ingen ändring föreslås.

## 9184. `component::duco::exceptions::failed_to_set_identify::message`

**Engelska:** Failed to set node identification.

**Befintlig svenska:** Det gick inte att ange nodidentifieringen.

**Bedömning:** Ingen ändring föreslås.

## 9185. `component::duco::entity::switch::identify::name`

**Engelska:** Identify

**Befintlig svenska:** Identifiera

**Bedömning:** Ingen ändring föreslås.

## 9186. `component::tuya::entity::sensor::water_total::name`

**Engelska:** Total water usage

**Befintlig svenska:** Total vattenförbrukning

**Bedömning:** Ingen ändring föreslås.

## 9187. `component::tuya::entity::sensor::water_once::name`

**Engelska:** Session water usage

**Befintlig svenska:** Vattenförbrukning för sessionen

**Bedömning:** Ingen ändring föreslås.

## 9188. `component::fronius::config::step::user::data_description::auto_revert_power_limit`

**Engelska:** The inverter drops the AC power limit and the battery charge and discharge limits an hour after it last received them, and returns to its own settings. Home Assistant sends active limits again every 15 minutes, so this only takes effect once it stops sending - because Home Assistant is down, or because the integration was removed. The battery minimum reserve and grid charging are not affected.

**Befintlig svenska:** Växelriktaren tar bort gränsen för växelströmseffekt och gränserna för batteriets laddning och urladdning en timme efter att den senast tog emot dem och återgår till sina egna inställningar. Home Assistant skickar aktiva gränser igen var femtonde minut, så detta sker först när Home Assistant slutar skicka dem, till exempel när Home Assistant är nere eller integrationen har tagits bort. Batteriets lägsta reservnivå och laddning från elnätet påverkas inte.

**Förslag:** Växelriktaren tar bort gränsen för växelströmseffekt och gränserna för batteriets laddning och urladdning en timme efter att den senast tog emot dem och återgår till sina egna inställningar. Home Assistant skickar aktiva gränser igen var femtonde minut, så detta sker först när Home Assistant slutar skicka dem, till exempel när Home Assistant är nere eller integreringen har tagits bort. Batteriets lägsta reservnivå och laddning från elnätet påverkas inte.

## 9189. `component::fronius::config::step::user::data::auto_revert_power_limit`

**Engelska:** Revert the power and battery limits if Home Assistant stops

**Befintlig svenska:** Återställ effekt- och batterigränserna om Home Assistant stannar

**Förslag:** Återställ effekt- och batterigränserna om Home Assistant stannar

## 9190. `component::fronius::config::step::reconfigure::data_description::auto_revert_power_limit`

**Engelska:** [%key:component::fronius::config::step::user::data_description::auto_revert_power_limit%]

**Befintlig svenska:** Växelriktaren tar bort AC-effektgränsen en timme efter att den senast tog emot den och återgår till sina egna inställningar. Home Assistant skickar gränsen igen var femtonde minut, så detta får bara effekt när systemet slutar skicka den eftersom Home Assistant är nere eller integrationen tagits bort. Batteriernas börvärden påverkas inte. Växelriktaren har ingen tidsgräns för dem.

**Kontextkontroll:** Den engelska texten hänvisar till en källnyckel med ett ändringsförslag ovan. Kontrollera att denna svenska text följer det uppdaterade referensmålet.

## 9191. `component::fronius::config::step::reconfigure::data::auto_revert_power_limit`

**Engelska:** [%key:component::fronius::config::step::user::data::auto_revert_power_limit%]

**Befintlig svenska:** Återställ gränsen för AC-effekt om Home Assistant stoppas

**Kontextkontroll:** Den engelska texten hänvisar till en källnyckel med ett ändringsförslag ovan. Kontrollera att denna svenska text följer det uppdaterade referensmålet.

## 9192. `component::bosch_shc::entity::switch::tamper_protection_enabled::name`

**Engelska:** Sabotage detection

**Befintlig svenska:** Manipuleringsdetektering

**Bedömning:** Ingen ändring föreslås.

## 9193. `component::geosphere_austria_warnings::entity::sensor::advance_warnings::unit_of_measurement`

**Engelska:** warnings

**Befintlig svenska:** varningar

**Bedömning:** Ingen ändring föreslås.

## 9194. `component::geosphere_austria_warnings::entity::sensor::advance_warnings::name`

**Engelska:** Advance warnings

**Befintlig svenska:** Förvarningar

**Bedömning:** Ingen ändring föreslås.

## 9195. `component::geosphere_austria_warnings::entity::sensor::advance_warning_level::state::yellow`

**Engelska:** Yellow

**Befintlig svenska:** Gul

**Bedömning:** Ingen ändring föreslås.

## 9196. `component::geosphere_austria_warnings::entity::sensor::advance_warning_level::state::red`

**Engelska:** Red

**Befintlig svenska:** Röd

**Bedömning:** Ingen ändring föreslås.

## 9197. `component::geosphere_austria_warnings::entity::sensor::advance_warning_level::state::orange`

**Engelska:** Orange

**Befintlig svenska:** Orange

**Bedömning:** Ingen ändring föreslås.

## 9198. `component::geosphere_austria_warnings::entity::sensor::advance_warning_level::state::none`

**Engelska:** No warning

**Befintlig svenska:** Ingen varning

**Bedömning:** Ingen ändring föreslås.

## 9199. `component::geosphere_austria_warnings::entity::sensor::advance_warning_level::name`

**Engelska:** Advance warning level

**Befintlig svenska:** Förvarningsnivå

**Bedömning:** Ingen ändring föreslås.

## 9200. `component::brother::entity::sensor::printer_status::state::warmup`

**Engelska:** Warming up

**Befintlig svenska:** Värmer upp

**Bedömning:** Ingen ändring föreslås.

## 9201. `component::brother::entity::sensor::printer_status::state::printing`

**Engelska:** Printing

**Befintlig svenska:** Skriver ut

**Bedömning:** Ingen ändring föreslås.

## 9202. `component::brother::entity::sensor::printer_status::state::other`

**Engelska:** Other

**Befintlig svenska:** Annat

**Bedömning:** Ingen ändring föreslås.

## 9203. `component::brother::entity::sensor::printer_status::state::idle`

**Engelska:** Idle

**Befintlig svenska:** Vänteläge

**Bedömning:** Ingen ändring föreslås.

## 9204. `component::brother::entity::sensor::printer_status::name`

**Engelska:** Printer status

**Befintlig svenska:** Skrivarstatus

**Bedömning:** Ingen ändring föreslås.

## 9205. `component::brother::entity::sensor::ink_capture_box_remaining_life::name`

**Engelska:** Ink capture box life

**Befintlig svenska:** Återstående livslängd för bläckuppsamlingsbox

**Bedömning:** Ingen ändring föreslås.

## 9206. `component::brother::entity::sensor::device_status::state::warning`

**Engelska:** Warning

**Befintlig svenska:** Varning

**Bedömning:** Ingen ändring föreslås.

## 9207. `component::brother::entity::sensor::device_status::state::testing`

**Engelska:** Testing

**Befintlig svenska:** Testas

**Bedömning:** Ingen ändring föreslås.

## 9208. `component::brother::entity::sensor::device_status::state::running`

**Engelska:** Running

**Befintlig svenska:** Körs

**Bedömning:** Ingen ändring föreslås.

## 9209. `component::brother::entity::sensor::device_status::state::down`

**Engelska:** Down

**Befintlig svenska:** Nere

**Bedömning:** Ingen ändring föreslås.

## 9210. `component::brother::entity::sensor::device_status::name`

**Engelska:** Health

**Befintlig svenska:** Hälsa

**Bedömning:** Ingen ändring föreslås.

## 9211. `component::nextdns::entity::switch::block_tunneling_endpoints::name`

**Engelska:** Block tunneling endpoints

**Befintlig svenska:** Blockera tunneländpunkter

**Bedömning:** Ingen ändring föreslås.

## 9212. `component::nextdns::entity::switch::block_residential_hosting::name`

**Engelska:** Block residential hosting

**Befintlig svenska:** Blockera webbhosting via bostadsanslutningar

**Bedömning:** Ingen ändring föreslås.

## 9213. `component::nextdns::entity::switch::block_free_hosting_domains::name`

**Engelska:** Block free hosting domains

**Befintlig svenska:** Blockera domäner för kostnadsfri webbhosting

**Bedömning:** Ingen ändring föreslås.

## 9214. `component::nextdns::entity::switch::block_decentralized_web_gateways::name`

**Engelska:** Block decentralized web gateways

**Befintlig svenska:** Blockera decentraliserade webbportaler

**Bedömning:** Ingen ändring föreslås.

## 9215. `component::nextdns::entity::switch::block_data_drop_services::name`

**Engelska:** Block data-drop services

**Befintlig svenska:** Blockera tjänster för dataöverföring

**Bedömning:** Ingen ändring föreslås.

## 9216. `component::bosch_shc::entity::switch::energy_saving_mode_enabled::name`

**Engelska:** Energy-saving mode

**Befintlig svenska:** Energisparläge

**Bedömning:** Ingen ändring föreslås.

## 9217. `component::silla_prism::entity::number::user_current::name`

**Engelska:** Maximum charging current

**Befintlig svenska:** Maximal laddningsström

**Bedömning:** Ingen ändring föreslås.

## 9218. `component::openai_conversation::config::step::reconfigure::description`

**Engelska:** Enter your updated OpenAI API key.

**Befintlig svenska:** Ange din uppdaterade OpenAI-API-nyckel.

**Förslag:** Ange din uppdaterade OpenAI-API-nyckel.

## 9219. `component::openai_conversation::config::step::reconfigure::data_description::api_key`

**Engelska:** [%key:component::openai_conversation::config::step::user::data_description::api_key%]

**Befintlig svenska:** Din OpenAI API-nyckel.

**Kontextkontroll:** Kontrollera referensmålet `component::openai_conversation::config::step::user::data_description::api_key`; det ingår ännu inte i det insamlade underlaget.

## 9220. `component::openai_conversation::config::step::reconfigure::data::api_key`

**Engelska:** [%key:common::config_flow::data::api_key%]

**Befintlig svenska:** API-nyckel

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::api_key`; det ingår ännu inte i det insamlade underlaget.

## 9221. `component::bosch_shc::entity::switch::humidity_warning_enabled::name`

**Engelska:** Humidity warning

**Befintlig svenska:** Fuktighetsvarning

**Bedömning:** Ingen ändring föreslås.

## 9222. `component::bosch_shc::entity::switch::nightly_promise_enabled::name`

**Engelska:** Heartbeat

**Befintlig svenska:** Hjärtslag

**Bedömning:** Ingen ändring föreslås.

## 9223. `component::tuya::config::step::reauth_confirm::title`

**Engelska:** [%key:common::config_flow::title::reauth%]

**Befintlig svenska:** Autentiseringen för {name} har upphört att gälla

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::title::reauth`; det ingår ännu inte i det insamlade underlaget.

## 9224. `component::tuya::config::step::reauth_confirm::description`

**Engelska:** Your Smart Life or Tuya Smart account needs to be reauthenticated.

Select **Submit** to get a QR code to scan with the app.

**Befintlig svenska:** Ditt Smart Life- eller Tuya Smart-konto måste autentiseras på nytt.

Välj **Skicka** för att få en QR-kod som kan skannas med appen.

**Bedömning:** Ingen ändring föreslås.

## 9225. `component::hotspring::entity::select::jet::state::off`

**Engelska:** [%key:common::state::off%]

**Befintlig svenska:** Av

**Kontextkontroll:** Kontrollera referensmålet `common::state::off`; det ingår ännu inte i det insamlade underlaget.

## 9226. `component::hotspring::entity::select::jet::state::low`

**Engelska:** [%key:common::state::low%]

**Befintlig svenska:** Låg

**Kontextkontroll:** Kontrollera referensmålet `common::state::low`; det ingår ännu inte i det insamlade underlaget.

## 9227. `component::hotspring::entity::select::jet::state::high`

**Engelska:** [%key:common::state::high%]

**Befintlig svenska:** Hög

**Kontextkontroll:** Kontrollera referensmålet `common::state::high`; det ingår ännu inte i det insamlade underlaget.

## 9228. `component::hotspring::entity::select::jet::name`

**Engelska:** Jet {jet}

**Befintlig svenska:** Stråle {jet}

**Bedömning:** Ingen ändring föreslås.

## 9229. `component::hotspring::entity::select::heating_mode::state::heat_with_boost`

**Engelska:** Heat with boost

**Befintlig svenska:** Värme med boost

**Bedömning:** Ingen ändring föreslås.

## 9230. `component::hotspring::entity::select::heating_mode::state::heat_saver`

**Engelska:** Heat saver

**Befintlig svenska:** Värmesparläge

**Bedömning:** Ingen ändring föreslås.

## 9231. `component::hotspring::entity::select::heating_mode::state::chill`

**Engelska:** Chill

**Befintlig svenska:** Kylning

**Bedömning:** Ingen ändring föreslås.

## 9232. `component::hotspring::entity::select::heating_mode::state::auto_with_boost`

**Engelska:** Auto with boost

**Befintlig svenska:** Automatiskt med boost

**Bedömning:** Ingen ändring föreslås.

## 9233. `component::hotspring::entity::select::heating_mode::state::auto_saver`

**Engelska:** Auto saver

**Befintlig svenska:** Automatisk sparfunktion

**Bedömning:** Ingen ändring föreslås.

## 9234. `component::hotspring::entity::select::heating_mode::name`

**Engelska:** Heating mode

**Befintlig svenska:** Uppvärmningsläge

**Bedömning:** Ingen ändring föreslås.

## 9235. `component::indi_allsky::entity::sensor::camera_sensor_temp::name`

**Engelska:** Camera sensor temperature

**Befintlig svenska:** Temperatur för kamerasensor

**Bedömning:** Ingen ändring föreslås.

## 9236. `component::bosch_shc::entity::switch::pet_immunity_enabled::name`

**Engelska:** Pet immunity

**Befintlig svenska:** Husdjursimmunitet

**Bedömning:** Ingen ändring föreslås.

## 9237. `component::lifx::exceptions::update_failed::message`

**Engelska:** Error fetching the state of the LIFX device: {error}

**Befintlig svenska:** Fel vid hämtning av LIFX-enhetens tillstånd: {error}

**Bedömning:** Ingen ändring föreslås.

## 9238. `component::lifx::exceptions::no_multizone_target::message`

**Engelska:** The targets of action lifx.{service} include no LIFX multizone light

**Befintlig svenska:** Målen för åtgärden lifx.{service} innehåller ingen LIFX-multizonlampa

**Bedömning:** Ingen ändring föreslås.

## 9239. `component::lifx::exceptions::no_matrix_target::message`

**Engelska:** The targets of action lifx.{service} include no LIFX matrix light

**Befintlig svenska:** Målen för åtgärden lifx.{service} innehåller ingen LIFX-matrislampa

**Bedömning:** Ingen ändring föreslås.

## 9240. `component::lifx::exceptions::no_lifx_target::message`

**Engelska:** The targets of action lifx.{service} include no LIFX light

**Befintlig svenska:** Målen för åtgärden lifx.{service} innehåller ingen LIFX-lampa

**Bedömning:** Ingen ändring föreslås.

## 9241. `component::lifx::exceptions::no_infrared::message`

**Engelska:** {entity_id} does not have infrared LEDs

**Befintlig svenska:** {entity_id} saknar infraröda lysdioder

**Bedömning:** Ingen ändring föreslås.

## 9242. `component::lifx::exceptions::no_hev::message`

**Engelska:** {entity_id} does not have HEV LEDs

**Befintlig svenska:** {entity_id} saknar HEV-lysdioder

**Bedömning:** Ingen ändring föreslås.

## 9243. `component::lifx::exceptions::invalid_serial::message`

**Engelska:** The LIFX device identified by {unique_id} cannot be migrated because that is not a LIFX serial number. Delete the entry and add the device again.

**Befintlig svenska:** LIFX-enheten med identifieraren {unique_id} kan inte migreras eftersom det inte är ett LIFX-serienummer. Ta bort posten och lägg till enheten igen.

**Bedömning:** Ingen ändring föreslås.

## 9244. `component::lifx::exceptions::invalid_color::message`

**Engelska:** The requested color is not valid: {error}

**Befintlig svenska:** Den begärda färgen är inte giltig: {error}

**Bedömning:** Ingen ändring föreslås.

## 9245. `component::lifx::exceptions::device_error::message`

**Engelska:** Error communicating with the LIFX device: {error}

**Befintlig svenska:** Fel vid kommunikation med LIFX-enheten: {error}

**Bedömning:** Ingen ändring föreslås.

## 9246. `component::lifx::exceptions::cannot_read_state::message`

**Engelska:** The current state of the LIFX device could not be read, so the requested change was not written to it

**Befintlig svenska:** Det gick inte att läsa det aktuella tillståndet för LIFX-enheten, så den begärda ändringen skrevs inte till den.

**Bedömning:** Ingen ändring föreslås.

## 9247. `component::lifx::exceptions::cannot_connect::message`

**Engelska:** Unable to connect to the LIFX device at {host}

**Befintlig svenska:** Det gick inte att ansluta till LIFX-enheten på {host}

**Bedömning:** Ingen ändring föreslås.

## 9248. `component::lifx::config::step::user::data_description::serial`

**Engelska:** The twelve-character serial number printed on your LIFX device. On its own, it is resolved by broadcasting to your network.

**Befintlig svenska:** Serienumret med tolv tecken som är tryckt på LIFX-enheten. Om endast serienumret anges hittas enheten genom en utsändning i nätverket.

**Förslag:** Serienumret med tolv tecken som är tryckt på LIFX-enheten. Om endast serienumret anges hittas enheten genom en utsändning i nätverket.

## 9249. `component::lifx::config::step::user::data::serial`

**Engelska:** Serial number

**Befintlig svenska:** Serienummer

**Bedömning:** Ingen ändring föreslås.

## 9250. `component::lifx::config::step::reconfigure::description`

**Engelska:** Update where Home Assistant reaches this LIFX device. The serial number is not changed, so this has to be the same device.

**Befintlig svenska:** Uppdatera var Home Assistant når LIFX-enheten. Serienumret ändras inte, så detta måste vara samma enhet.

**Bedömning:** Ingen ändring föreslås.

## 9251. `component::lifx::config::step::reconfigure::data_description::host`

**Engelska:** The new hostname or IP address of this LIFX device.

**Befintlig svenska:** Det nya värdnamnet eller den nya IP-adressen för LIFX-enheten.

**Bedömning:** Ingen ändring föreslås.

## 9252. `component::lifx::config::step::reconfigure::data::host`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** Värd

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::host`; det ingår ännu inte i det insamlade underlaget.

## 9253. `component::lifx::config::step::pick_device::data_description::device`

**Engelska:** The discovered LIFX device to add.

**Befintlig svenska:** Den upptäckta LIFX-enheten som ska läggas till.

**Bedömning:** Ingen ändring föreslås.

## 9254. `component::lifx::config::error::invalid_serial`

**Engelska:** This is not a valid LIFX serial number.

**Befintlig svenska:** Detta är inte ett giltigt LIFX-serienummer.

**Bedömning:** Ingen ändring föreslås.

## 9255. `component::lifx::config::abort::wrong_device`

**Engelska:** The device at this address is not the one this entry was set up for.

**Befintlig svenska:** Enheten på denna adress är inte den som posten konfigurerades för.

**Bedömning:** Ingen ändring föreslås.

## 9256. `component::lifx::config::abort::reconfigure_successful`

**Engelska:** [%key:common::config_flow::abort::reconfigure_successful%]

**Befintlig svenska:** Omkonfigureringen lyckades

**Bedömning:** Ingen ändring föreslås.

## 9257. `component::bosch_shc::entity::valve::valve::name`

**Engelska:** Valve

**Befintlig svenska:** Ventil

**Bedömning:** Ingen ändring föreslås.

## 9258. `component::bosch_shc::entity::sensor::valve_tappet_state::state::valve_too_tight`

**Engelska:** Valve too tight

**Befintlig svenska:** Ventilen är för trög

**Bedömning:** Ingen ändring föreslås.

## 9259. `component::bosch_shc::entity::sensor::valve_tappet_state::state::valve_adaption_successful`

**Engelska:** Adaptation successful

**Befintlig svenska:** Anpassning lyckades

**Bedömning:** Ingen ändring föreslås.

## 9260. `component::bosch_shc::entity::sensor::valve_tappet_state::state::valve_adaption_requested`

**Engelska:** Adaptation requested

**Befintlig svenska:** Anpassning begärd

**Bedömning:** Ingen ändring föreslås.

## 9261. `component::bosch_shc::entity::sensor::valve_tappet_state::state::valve_adaption_in_progress`

**Engelska:** Adaptation in progress

**Befintlig svenska:** Anpassning pågår

**Bedömning:** Ingen ändring föreslås.

## 9262. `component::bosch_shc::entity::sensor::valve_tappet_state::state::unknown`

**Engelska:** Unknown

**Befintlig svenska:** Okänd

**Bedömning:** Ingen ändring föreslås.

## 9263. `component::bosch_shc::entity::sensor::valve_tappet_state::state::start_position_requested`

**Engelska:** Start position requested

**Befintlig svenska:** Startposition begärd

**Bedömning:** Ingen ändring föreslås.

## 9264. `component::bosch_shc::entity::sensor::valve_tappet_state::state::run_to_start_position`

**Engelska:** Running to start position

**Befintlig svenska:** Kör till startposition

**Bedömning:** Ingen ändring föreslås.

## 9265. `component::bosch_shc::entity::sensor::valve_tappet_state::state::range_too_small`

**Engelska:** Range too small

**Befintlig svenska:** Intervallet är för litet

**Bedömning:** Ingen ändring föreslås.

## 9266. `component::bosch_shc::entity::sensor::valve_tappet_state::state::range_too_big`

**Engelska:** Range too big

**Befintlig svenska:** Intervallet är för stort

**Bedömning:** Ingen ändring föreslås.

## 9267. `component::bosch_shc::entity::sensor::valve_tappet_state::state::not_available`

**Engelska:** Not available

**Befintlig svenska:** Inte tillgänglig

**Bedömning:** Ingen ändring föreslås.

## 9268. `component::bosch_shc::entity::sensor::valve_tappet_state::state::no_valve_body_error`

**Engelska:** Error: no valve body detected

**Befintlig svenska:** Fel: inget ventilhus upptäcktes

**Bedömning:** Ingen ändring föreslås.

## 9269. `component::bosch_shc::entity::sensor::valve_tappet_state::state::no_motor_error`

**Engelska:** Error: no motor detected

**Befintlig svenska:** Fel: ingen motor upptäcktes

**Bedömning:** Ingen ändring föreslås.

## 9270. `component::bosch_shc::entity::sensor::valve_tappet_state::state::in_start_position`

**Engelska:** In start position

**Befintlig svenska:** I startposition

**Bedömning:** Ingen ändring föreslås.

## 9271. `component::bosch_shc::entity::sensor::valve_tappet_state::state::fix_motor_logic_successful`

**Engelska:** Motor logic fix successful

**Befintlig svenska:** Korrigering av motorlogik lyckades

**Bedömning:** Ingen ändring föreslås.

## 9272. `component::bosch_shc::entity::sensor::valve_tappet_state::state::fix_motor_logic_requested`

**Engelska:** Motor logic fix requested

**Befintlig svenska:** Korrigering av motorlogik begärd

**Bedömning:** Ingen ändring föreslås.

## 9273. `component::bosch_shc::entity::sensor::valve_tappet_state::state::fix_motor_logic_in_progress`

**Engelska:** Motor logic fix in progress

**Befintlig svenska:** Korrigering av motorlogik pågår

**Bedömning:** Ingen ändring föreslås.

## 9274. `component::bosch_shc::entity::sensor::valve_tappet_state::state::error`

**Engelska:** Error

**Befintlig svenska:** Fel

**Bedömning:** Ingen ändring föreslås.

## 9275. `component::bosch_shc::entity::sensor::valve_tappet_state::name`

**Engelska:** Valve motor status

**Befintlig svenska:** Ventilmotorstatus

**Bedömning:** Ingen ändring föreslås.

## 9276. `component::bosch_shc::entity::switch::bypass_infinite::name`

**Engelska:** Break function never expires

**Befintlig svenska:** Brytfunktionen upphör aldrig

**Bedömning:** Ingen ändring föreslås.

## 9277. `component::bosch_shc::entity::switch::bypass::name`

**Engelska:** Break function

**Befintlig svenska:** Brytfunktion

**Bedömning:** Ingen ändring föreslås.

## 9278. `component::bosch_shc::entity::sensor::open_windows_doors::name`

**Engelska:** Open doors and windows

**Befintlig svenska:** Öppna dörrar och fönster

**Bedömning:** Ingen ändring föreslås.

## 9279. `component::teslemetry::config_subentries::energy_site::error::key_expired`

**Engelska:** The approval window on your Powerwall closed before the key was approved. Submit to open a new window, flick the On/Off switch on your primary Powerwall off and back on to approve it, then submit again.

**Befintlig svenska:** Godkännandefönstret på din Powerwall stängdes innan nyckeln godkändes. Välj Skicka för att öppna ett nytt fönster, växla strömbrytaren på din primära Powerwall från Av till På för att godkänna nyckeln och välj sedan Skicka igen.

**Bedömning:** Ingen ändring föreslås.

## 9280. `component::switchbot::entity::cover::cover::state_attributes::speed::state::silent`

**Engelska:** Silent

**Befintlig svenska:** Tyst

**Bedömning:** Ingen ändring föreslås.

## 9281. `component::switchbot::entity::cover::cover::state_attributes::speed::state::normal`

**Engelska:** Normal

**Befintlig svenska:** Normal

**Bedömning:** Ingen ändring föreslås.

## 9282. `component::indi_allsky::entity::sensor::stars::name`

**Engelska:** Stars

**Befintlig svenska:** Stjärnor

**Bedömning:** Ingen ändring föreslås.

## 9283. `component::indi_allsky::entity::sensor::sqm::name`

**Engelska:** Sky quality

**Befintlig svenska:** Himmelskvalitet

**Bedömning:** Ingen ändring föreslås.

## 9284. `component::indi_allsky::entity::sensor::gain::name`

**Engelska:** Gain

**Befintlig svenska:** Förstärkning

**Bedömning:** Ingen ändring föreslås.

## 9285. `component::indi_allsky::entity::sensor::filename::name`

**Engelska:** Filename

**Befintlig svenska:** Filnamn

**Bedömning:** Ingen ändring föreslås.

## 9286. `component::indi_allsky::entity::sensor::exposure::name`

**Engelska:** Exposure time

**Befintlig svenska:** Exponeringstid

**Bedömning:** Ingen ändring föreslås.

## 9287. `component::indi_allsky::entity::sensor::binmode::name`

**Engelska:** Binning mode

**Befintlig svenska:** Bin-läge

**Bedömning:** Ingen ändring föreslås.

## 9288. `component::xbox::entity::image::titled_hero_art::name`

**Engelska:** Titled hero art

**Befintlig svenska:** Hjältebild med titel

**Bedömning:** Ingen ändring föreslås.

## 9289. `component::xbox::entity::image::super_hero_art::name`

**Engelska:** Superhero art

**Befintlig svenska:** Superhjältebild

**Bedömning:** Ingen ändring föreslås.

## 9290. `component::xbox::entity::image::poster::name`

**Engelska:** Poster

**Befintlig svenska:** Affisch

**Bedömning:** Ingen ändring föreslås.

## 9291. `component::xbox::entity::image::feature_promotional_square_art::name`

**Engelska:** Feature promotional square art

**Befintlig svenska:** Kvadratisk kampanjbild för funktion

**Bedömning:** Ingen ändring föreslås.

## 9292. `component::xbox::entity::image::branded_key_art::name`

**Engelska:** Branded key art

**Befintlig svenska:** Varumärkt nyckelbild

**Bedömning:** Ingen ändring föreslås.

## 9293. `component::xbox::entity::image::box_art::name`

**Engelska:** Box art

**Befintlig svenska:** Omslagsbild

**Bedömning:** Ingen ändring föreslås.

## 9294. `component::mystrom::exceptions::switch_action_failed::message`

**Engelska:** Failed to perform the action on the myStrom plug.

**Befintlig svenska:** Det gick inte att utföra åtgärden på myStrom-uttaget.

**Bedömning:** Ingen ändring föreslås.

## 9295. `component::knx::config_panel::dpt::options::4_002`

**Engelska:** Character (Latin-1)

**Befintlig svenska:** Tecken (Latin-1)

**Bedömning:** Ingen ändring föreslås.

## 9296. `component::knx::config_panel::dpt::options::4_001`

**Engelska:** Character (ASCII)

**Befintlig svenska:** Tecken (ASCII)

**Bedömning:** Ingen ändring föreslås.

## 9297. `component::knx::config_panel::dpt::options::3_008`

**Engelska:** Blinds control

**Befintlig svenska:** Persiennstyrning

**Bedömning:** Ingen ändring föreslås.

## 9298. `component::knx::config_panel::dpt::options::3_007`

**Engelska:** Dimming control

**Befintlig svenska:** Dimningsstyrning

**Bedömning:** Ingen ändring föreslås.

## 9299. `component::knx::config_panel::dpt::options::2_012`

**Engelska:** Invert control

**Befintlig svenska:** Inverteringsstyrning

**Bedömning:** Ingen ändring föreslås.

## 9300. `component::knx::config_panel::dpt::options::2_011`

**Engelska:** State control

**Befintlig svenska:** Tillståndsstyrning

**Bedömning:** Ingen ändring föreslås.

## 9301. `component::knx::config_panel::dpt::options::2_010`

**Engelska:** Start control

**Befintlig svenska:** Startstyrning

**Bedömning:** Ingen ändring föreslås.

## 9302. `component::knx::config_panel::dpt::options::2_009`

**Engelska:** Direction 2 control

**Befintlig svenska:** Riktningsstyrning 2

**Bedömning:** Ingen ändring föreslås.

## 9303. `component::knx::config_panel::dpt::options::2_008`

**Engelska:** Direction 1 control

**Befintlig svenska:** Riktningsstyrning 1

**Bedömning:** Ingen ändring föreslås.

## 9304. `component::knx::config_panel::dpt::options::2_007`

**Engelska:** Step control

**Befintlig svenska:** Stegstyrning

**Bedömning:** Ingen ändring föreslås.

## 9305. `component::knx::config_panel::dpt::options::2_006`

**Engelska:** Binary value control

**Befintlig svenska:** Styrning av binärt värde

**Bedömning:** Ingen ändring föreslås.

## 9306. `component::knx::config_panel::dpt::options::2_005`

**Engelska:** Alarm control

**Befintlig svenska:** Larmstyrning

**Bedömning:** Ingen ändring föreslås.

## 9307. `component::knx::config_panel::dpt::options::2_004`

**Engelska:** Ramp control

**Befintlig svenska:** Rampstyrning

**Bedömning:** Ingen ändring föreslås.

## 9308. `component::knx::config_panel::dpt::options::2_003`

**Engelska:** Enable control

**Befintlig svenska:** Aktiveringsstyrning

**Bedömning:** Ingen ändring föreslås.

## 9309. `component::knx::config_panel::dpt::options::2_002`

**Engelska:** Boolean control

**Befintlig svenska:** Boolesk styrning

**Bedömning:** Ingen ändring föreslås.

## 9310. `component::knx::config_panel::dpt::options::2_001`

**Engelska:** Switch control

**Befintlig svenska:** Brytarstyrning

**Bedömning:** Ingen ändring föreslås.

## 9311. `component::knx::config_panel::dpt::options::254_600`

**Engelska:** Relative RGB control

**Befintlig svenska:** Relativ RGB-styrning

**Bedömning:** Ingen ändring föreslås.

## 9312. `component::knx::config_panel::dpt::options::253_600`

**Engelska:** Relative xyY control

**Befintlig svenska:** Relativ xyY-styrning

**Bedömning:** Ingen ändring föreslås.

## 9313. `component::knx::config_panel::dpt::options::252_600`

**Engelska:** Relative RGBW control

**Befintlig svenska:** Relativ RGBW-styrning

**Bedömning:** Ingen ändring föreslås.

## 9314. `component::knx::config_panel::dpt::options::251_600`

**Engelska:** RGBW color

**Befintlig svenska:** RGBW-färg

**Bedömning:** Ingen ändring föreslås.

## 9315. `component::knx::config_panel::dpt::options::250_600`

**Engelska:** Brightness and color temperature control

**Befintlig svenska:** Styrning av ljusstyrka och färgtemperatur

**Bedömning:** Ingen ändring föreslås.

## 9316. `component::knx::config_panel::dpt::options::249_600`

**Engelska:** Brightness and color temperature transition

**Befintlig svenska:** Övergång för ljusstyrka och färgtemperatur

**Bedömning:** Ingen ändring föreslås.

## 9317. `component::knx::config_panel::dpt::options::243_600`

**Engelska:** xyY color transition

**Befintlig svenska:** Övergång för xyY-färg

**Bedömning:** Ingen ändring föreslås.

## 9318. `component::knx::config_panel::dpt::options::242_600`

**Engelska:** xyY color

**Befintlig svenska:** xyY-färg

**Bedömning:** Ingen ändring föreslås.

## 9319. `component::knx::config_panel::dpt::options::235_001`

**Engelska:** Tariff active energy

**Befintlig svenska:** Tariff för aktiv energi

**Bedömning:** Ingen ändring föreslås.

## 9320. `component::knx::config_panel::dpt::options::232_600`

**Engelska:** RGB color

**Befintlig svenska:** RGB-färg

**Bedömning:** Ingen ändring föreslås.

## 9321. `component::knx::config_panel::dpt::options::20_60102`

**Engelska:** HVAC status

**Befintlig svenska:** HVAC-status

**Bedömning:** Ingen ändring föreslås.

## 9322. `component::knx::config_panel::dpt::options::20_105`

**Engelska:** HVAC controller mode

**Befintlig svenska:** HVAC-styrenhetsläge

**Bedömning:** Ingen ändring föreslås.

## 9323. `component::knx::config_panel::dpt::options::20_102`

**Engelska:** HVAC mode

**Befintlig svenska:** HVAC-läge

**Bedömning:** Ingen ändring föreslås.

## 9324. `component::knx::config_panel::dpt::options::2`

**Engelska:** Generic 2-bit boolean control

**Befintlig svenska:** Generisk boolesk styrning med 2 bitar

**Bedömning:** Ingen ändring föreslås.

## 9325. `component::knx::config_panel::dpt::options::1_1201`

**Engelska:** Energy direction

**Befintlig svenska:** Energiriktning

**Bedömning:** Ingen ändring föreslås.

## 9326. `component::knx::config_panel::dpt::options::1_1200`

**Engelska:** Consumer / Producer

**Befintlig svenska:** Förbrukare/producent

**Bedömning:** Ingen ändring föreslås.

## 9327. `component::knx::config_panel::dpt::options::1_100`

**Engelska:** Heat / Cool

**Befintlig svenska:** Värme/kyla

**Bedömning:** Ingen ändring föreslås.

## 9328. `component::knx::config_panel::dpt::options::1_024`

**Engelska:** Day / Night

**Befintlig svenska:** Dag/natt

**Bedömning:** Ingen ändring föreslås.

## 9329. `component::knx::config_panel::dpt::options::1_023`

**Engelska:** Shutter / Blinds mode

**Befintlig svenska:** Läge för jalusi eller persienn

**Bedömning:** Ingen ändring föreslås.

## 9330. `component::knx::config_panel::dpt::options::1_022`

**Engelska:** Scene A/B

**Befintlig svenska:** Scen A/B

**Bedömning:** Ingen ändring föreslås.

## 9331. `component::knx::config_panel::dpt::options::1_021`

**Engelska:** Logical function

**Befintlig svenska:** Logisk funktion

**Bedömning:** Ingen ändring föreslås.

## 9332. `component::knx::config_panel::dpt::options::1_019`

**Engelska:** Window / Door

**Befintlig svenska:** Fönster/dörr

**Bedömning:** Ingen ändring föreslås.

## 9333. `component::knx::config_panel::dpt::options::1_018`

**Engelska:** Occupancy

**Befintlig svenska:** Beläggning

**Bedömning:** Ingen ändring föreslås.

## 9334. `component::knx::config_panel::dpt::options::1_017`

**Engelska:** Trigger

**Befintlig svenska:** Utlösare

**Bedömning:** Ingen ändring föreslås.

## 9335. `component::knx::config_panel::dpt::options::1_016`

**Engelska:** Acknowledge

**Befintlig svenska:** Bekräfta

**Bedömning:** Ingen ändring föreslås.

## 9336. `component::knx::config_panel::dpt::options::1_015`

**Engelska:** Reset

**Befintlig svenska:** Återställ

**Bedömning:** Ingen ändring föreslås.

## 9337. `component::knx::config_panel::dpt::options::1_014`

**Engelska:** Input source

**Befintlig svenska:** Ingångskälla

**Bedömning:** Ingen ändring föreslås.

## 9338. `component::knx::config_panel::dpt::options::1_013`

**Engelska:** Dimming send style

**Befintlig svenska:** Sändstil för dimning

**Bedömning:** Ingen ändring föreslås.

## 9339. `component::knx::config_panel::dpt::options::1_012`

**Engelska:** Invert

**Befintlig svenska:** Invertera

**Bedömning:** Ingen ändring föreslås.

## 9340. `component::knx::config_panel::dpt::options::1_011`

**Engelska:** State

**Befintlig svenska:** Tillstånd

**Bedömning:** Ingen ändring föreslås.

## 9341. `component::knx::config_panel::dpt::options::1_010`

**Engelska:** Start

**Befintlig svenska:** Start

**Bedömning:** Ingen ändring föreslås.

## 9342. `component::knx::config_panel::dpt::options::1_009`

**Engelska:** Open / Close

**Befintlig svenska:** Öppna/stäng

**Bedömning:** Ingen ändring föreslås.

## 9343. `component::knx::config_panel::dpt::options::1_008`

**Engelska:** Up / Down

**Befintlig svenska:** Upp/ned

**Bedömning:** Ingen ändring föreslås.

## 9344. `component::knx::config_panel::dpt::options::1_007`

**Engelska:** Step

**Befintlig svenska:** Steg

**Bedömning:** Ingen ändring föreslås.

## 9345. `component::knx::config_panel::dpt::options::1_006`

**Engelska:** Binary value

**Befintlig svenska:** Binärt värde

**Bedömning:** Ingen ändring föreslås.

## 9346. `component::knx::config_panel::dpt::options::1_005`

**Engelska:** Alarm

**Befintlig svenska:** Larm

**Bedömning:** Ingen ändring föreslås.

## 9347. `component::knx::config_panel::dpt::options::1_004`

**Engelska:** Ramp

**Befintlig svenska:** Ramp

**Bedömning:** Ingen ändring föreslås.

## 9348. `component::knx::config_panel::dpt::options::1_003`

**Engelska:** Enable

**Befintlig svenska:** Aktivera

**Bedömning:** Ingen ändring föreslås.

## 9349. `component::knx::config_panel::dpt::options::1_002`

**Engelska:** Boolean

**Befintlig svenska:** Boolesk

**Bedömning:** Ingen ändring föreslås.

## 9350. `component::knx::config_panel::dpt::options::1_001`

**Engelska:** Switch

**Befintlig svenska:** Brytare

**Bedömning:** Ingen ändring föreslås.

## 9351. `component::knx::config_panel::dpt::options::19_001`

**Engelska:** Date and time

**Befintlig svenska:** Datum och tid

**Bedömning:** Ingen ändring föreslås.

## 9352. `component::knx::config_panel::dpt::options::18_001`

**Engelska:** Scene control

**Befintlig svenska:** Scenstyrning

**Bedömning:** Ingen ändring föreslås.

## 9353. `component::knx::config_panel::dpt::options::11_001`

**Engelska:** Date

**Befintlig svenska:** Datum

**Bedömning:** Ingen ändring föreslås.

## 9354. `component::knx::config_panel::dpt::options::10_001`

**Engelska:** Time of day

**Befintlig svenska:** Tid på dagen

**Bedömning:** Ingen ändring föreslås.

## 9355. `component::knx::config_panel::dpt::options::1`

**Engelska:** Generic 1-bit

**Befintlig svenska:** Generisk 1-bit

**Bedömning:** Ingen ändring föreslås.

## 9356. `component::monarch_money::config::step::reauth_confirm::description`

**Engelska:** Your Monarch Money credentials have expired. Enter your email and password to reconnect your existing account. If required, you will also be prompted for your MFA code.

**Befintlig svenska:** Inloggningsuppgifterna för Monarch Money har upphört att gälla. Ange din e-postadress och ditt lösenord för att återansluta det befintliga kontot. Om det behövs uppmanas du även att ange din MFA-kod.

**Bedömning:** Ingen ändring föreslås.

## 9357. `component::monarch_money::config::step::reauth_confirm::data::password`

**Engelska:** [%key:common::config_flow::data::password%]

**Befintlig svenska:** Lösenord

**Bedömning:** Ingen ändring föreslås.

## 9358. `component::monarch_money::config::step::reauth_confirm::data::mfa_code`

**Engelska:** [%key:component::monarch_money::config::step::user::data::mfa_code%]

**Befintlig svenska:** Ange din MFA-kod

**Bedömning:** Ingen ändring föreslås.

## 9359. `component::monarch_money::config::step::reauth_confirm::data::email`

**Engelska:** [%key:common::config_flow::data::email%]

**Befintlig svenska:** E-post

**Bedömning:** Ingen ändring föreslås.

## 9360. `component::monarch_money::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Bedömning:** Ingen ändring föreslås.

## 9361. `component::monarch_money::config::abort::unique_id_mismatch`

**Engelska:** The authenticated Monarch Money account does not match the configured account.

**Befintlig svenska:** Det autentiserade Monarch Money-kontot stämmer inte överens med det konfigurerade kontot.

**Bedömning:** Ingen ändring föreslås.

## 9362. `component::monarch_money::config::abort::reauth_successful`

**Engelska:** [%key:common::config_flow::abort::reauth_successful%]

**Befintlig svenska:** Återautentisering lyckades

**Bedömning:** Ingen ändring föreslås.

## 9363. `component::theben_conexa::entity::sensor::energy_supplied::name`

**Engelska:** Energy supplied

**Befintlig svenska:** Levererad energi

**Bedömning:** Ingen ändring föreslås.

## 9364. `component::theben_conexa::entity::sensor::energy_consumed::name`

**Engelska:** Energy consumed

**Befintlig svenska:** Förbrukad energi

**Bedömning:** Ingen ändring föreslås.

## 9365. `component::theben_conexa::config::step::user::description`

**Engelska:** As a prerequisite you must be able to log in to your smartmeter gateway from a web browser via `https://[IP of your gateway]`.

**Befintlig svenska:** Du måste kunna logga in på smartmätargatewayen i en webbläsare via `https://[IP-adressen för din gateway]`.

**Bedömning:** Ingen ändring föreslås.

## 9366. `component::theben_conexa::config::step::user::data_description::username`

**Engelska:** The username provided by your power grid operator

**Befintlig svenska:** Användarnamnet från nätägaren

**Bedömning:** Ingen ändring föreslås.

## 9367. `component::theben_conexa::config::step::user::data_description::password`

**Engelska:** The password provided by your power grid operator

**Befintlig svenska:** Lösenordet från din elnätsoperatör.

**Bedömning:** Ingen ändring föreslås.

## 9368. `component::theben_conexa::config::step::user::data_description::host`

**Engelska:** The IP of your smartmeter gateway provided by your power grid operator

**Befintlig svenska:** IP-adressen till smartmätargatewayen från nätägaren

**Bedömning:** Ingen ändring föreslås.

## 9369. `component::theben_conexa::config::step::user::data::username`

**Engelska:** [%key:common::config_flow::data::username%]

**Befintlig svenska:** Användarnamn

**Bedömning:** Ingen ändring föreslås.

## 9370. `component::theben_conexa::config::step::user::data::password`

**Engelska:** [%key:common::config_flow::data::password%]

**Befintlig svenska:** Lösenord

**Bedömning:** Ingen ändring föreslås.

## 9371. `component::theben_conexa::config::step::user::data::host`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** Värd

**Bedömning:** Ingen ändring föreslås.

## 9372. `component::theben_conexa::config::error::unknown`

**Engelska:** [%key:common::config_flow::error::unknown%]

**Befintlig svenska:** Oväntat fel

**Bedömning:** Ingen ändring föreslås.

## 9373. `component::theben_conexa::config::error::invalid_auth`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** Ogiltig autentisering

**Bedömning:** Ingen ändring föreslås.

## 9374. `component::theben_conexa::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::cannot_connect`; det ingår ännu inte i det insamlade underlaget.

## 9375. `component::theben_conexa::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_device%]

**Befintlig svenska:** Enheten är redan konfigurerad

**Bedömning:** Ingen ändring föreslås.

## 9376. `component::threema::exceptions::send_error::message`

**Engelska:** Error sending message: {error}

**Befintlig svenska:** Fel vid skickande av meddelande: {error}

**Bedömning:** Ingen ändring föreslås.

## 9377. `component::threema::exceptions::invalid_auth::message`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** Ogiltig autentisering

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::invalid_auth`; det ingår ännu inte i det insamlade underlaget.

## 9378. `component::threema::exceptions::cannot_connect::message`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::cannot_connect`; det ingår ännu inte i det insamlade underlaget.

## 9379. `component::threema::config_subentries::recipient::step::user::title`

**Engelska:** Add recipient

**Befintlig svenska:** Lägg till mottagare

**Bedömning:** Ingen ändring föreslås.

## 9380. `component::threema::config_subentries::recipient::step::user::description`

**Engelska:** Enter the Threema ID of the person you want to send messages to.

**Befintlig svenska:** Ange Threema-ID:t för personen som du vill skicka meddelanden till.

**Bedömning:** Ingen ändring föreslås.

## 9381. `component::threema::config_subentries::recipient::step::user::data_description::recipient`

**Engelska:** The 8-character Threema ID of the recipient.

**Befintlig svenska:** Mottagarens Threema-ID med åtta tecken.

**Förslag:** Mottagarens Threema-ID med åtta tecken.

## 9382. `component::threema::config_subentries::recipient::step::user::data_description::name`

**Engelska:** Optional friendly name for this recipient (e.g. 'Dad').

**Befintlig svenska:** Valfritt visningsnamn för mottagaren, till exempel 'Pappa'.

**Bedömning:** Ingen ändring föreslås.

## 9383. `component::threema::config_subentries::recipient::step::user::data::recipient`

**Engelska:** Threema ID

**Befintlig svenska:** Threema-ID

**Bedömning:** Ingen ändring föreslås.

## 9384. `component::threema::config_subentries::recipient::step::user::data::name`

**Engelska:** Display name

**Befintlig svenska:** Visningsnamn

**Bedömning:** Ingen ändring föreslås.

## 9385. `component::threema::config_subentries::recipient::initiate_flow::user`

**Engelska:** Add recipient

**Befintlig svenska:** Lägg till mottagare

**Bedömning:** Ingen ändring föreslås.

## 9386. `component::threema::config_subentries::recipient::error::invalid_recipient_id`

**Engelska:** Threema ID must be exactly 8 alphanumeric characters.

**Befintlig svenska:** Threema-ID måste bestå av exakt åtta alfanumeriska tecken.

**Bedömning:** Ingen ändring föreslås.

## 9387. `component::threema::config_subentries::recipient::entry_type`

**Engelska:** Recipient

**Befintlig svenska:** Mottagare

**Bedömning:** Ingen ändring föreslås.

## 9388. `component::threema::config_subentries::recipient::abort::already_configured`

**Engelska:** This recipient is already configured.

**Befintlig svenska:** Mottagaren är redan konfigurerad.

**Bedömning:** Ingen ändring föreslås.

## 9389. `component::threema::config::step::user::title`

**Engelska:** Threema setup

**Befintlig svenska:** Konfigurera Threema

**Bedömning:** Ingen ändring föreslås.

## 9390. `component::threema::config::step::user::menu_options::setup_new`

**Engelska:** Generate new encryption keys

**Befintlig svenska:** Generera nya krypteringsnycklar

**Bedömning:** Ingen ändring föreslås.

## 9391. `component::threema::config::step::user::menu_options::credentials`

**Engelska:** Add existing Gateway ID

**Befintlig svenska:** Lägg till befintligt Gateway-ID

**Bedömning:** Ingen ändring föreslås.

## 9392. `component::threema::config::step::setup_new::title`

**Engelska:** Keys generated

**Befintlig svenska:** Nycklar genererade

**Bedömning:** Ingen ändring föreslås.

## 9393. `component::threema::config::step::setup_new::description`

**Engelska:** Your keys have been generated. Save them now before continuing!

Public key: `{public_key}`
Private key: `{private_key}`

When registering at gateway.threema.ch, paste the public key as shown above. Store the private key securely — it cannot be recovered.

**Befintlig svenska:** Nycklarna har genererats. Spara dem innan du fortsätter!

Offentlig nyckel: `{public_key}`
Privat nyckel: `{private_key}`

När du registrerar dig på gateway.threema.ch klistrar du in den offentliga nyckeln enligt ovan. Förvara den privata nyckeln säkert. Den går inte att återställa.

**Förslag:** Nycklarna har genererats. Spara dem innan du fortsätter!

Offentlig nyckel: `{public_key}`
Privat nyckel: `{private_key}`

När du registrerar dig på gateway.threema.ch klistrar du in den offentliga nyckeln enligt ovan. Förvara den privata nyckeln säkert. Den går inte att återställa.

## 9394. `component::threema::config::step::credentials::title`

**Engelska:** Gateway credentials

**Befintlig svenska:** Gateway-inloggningsuppgifter

**Bedömning:** Ingen ändring föreslås.

## 9395. `component::threema::config::step::credentials::description`

**Engelska:** Enter your Threema Gateway ID and secret obtained from gateway.threema.ch. Threema enables end-to-end mode for a Gateway ID manually after you register a public key, which can take a few days — so you may well be completing this step long after the keys were generated.

**Befintlig svenska:** Ange ditt Threema Gateway-ID och den hemlighet som du fick från gateway.threema.ch. Threema aktiverar E2E-läget för ett Gateway-ID manuellt efter att du registrerat en offentlig nyckel. Det kan ta några dagar, så det är möjligt att du gör detta långt efter att nycklarna genererades.

**Bedömning:** Ingen ändring föreslås.

## 9396. `component::threema::config::step::credentials::data_description::public_key`

**Engelska:** Never stored — only checked once against the private key above to catch copy-paste mistakes. Paste the public key you registered at gateway.threema.ch (a 'public:' prefix is accepted).

**Befintlig svenska:** Lagras aldrig. Kontrolleras endast en gång mot den privata nyckeln ovan för att fånga kopierings- och inklistringsmisstag. Klistra in den offentliga nyckeln som du registrerade på gateway.threema.ch (prefixet 'public:' accepteras).

**Bedömning:** Ingen ändring föreslås.

## 9397. `component::threema::config::step::credentials::data_description::private_key`

**Engelska:** Private key as hex string (64 characters). A 'private:' prefix, as used by Threema's key export tools, is accepted and stripped automatically. Leave empty for simple (non-E2E) mode.

**Befintlig svenska:** Privat nyckel som hexsträng (64 tecken). Prefixet 'private:', som används av Threemas verktyg för nyckelexport, accepteras och tas bort automatiskt. Lämna tomt för enkelt läge utan E2E.

**Bedömning:** Ingen ändring föreslås.

## 9398. `component::threema::config::step::credentials::data_description::gateway_id`

**Engelska:** ID of your Gateway, including '*', e.g.: *ABCD123

**Befintlig svenska:** ID:t för din Gateway, inklusive '*', till exempel: *ABCD123

**Bedömning:** Ingen ändring föreslås.

## 9399. `component::threema::config::step::credentials::data_description::api_secret`

**Engelska:** Secret you received from Threema

**Befintlig svenska:** Hemlighet som du fick från Threema

**Bedömning:** Ingen ändring föreslås.

## 9400. `component::threema::config::step::credentials::data::public_key`

**Engelska:** Public key to verify against (optional)

**Befintlig svenska:** Offentlig nyckel att kontrollera mot (valfritt)

**Bedömning:** Ingen ändring föreslås.

## 9401. `component::threema::config::step::credentials::data::private_key`

**Engelska:** Private key (optional, enables E2E encryption)

**Befintlig svenska:** Privat nyckel (valfritt, aktiverar E2E-kryptering)

**Bedömning:** Ingen ändring föreslås.

## 9402. `component::threema::config::step::credentials::data::gateway_id`

**Engelska:** Gateway ID

**Befintlig svenska:** Gateway-ID

**Bedömning:** Ingen ändring föreslås.

## 9403. `component::threema::config::step::credentials::data::api_secret`

**Engelska:** API secret

**Befintlig svenska:** API-hemlighet

**Bedömning:** Ingen ändring föreslås.

## 9404. `component::threema::config::error::unknown`

**Engelska:** [%key:common::config_flow::error::unknown%]

**Befintlig svenska:** Oväntat fel

**Bedömning:** Ingen ändring föreslås.

## 9405. `component::threema::config::error::public_key_requires_private_key`

**Engelska:** Enter the private key too to verify it against the public key.

**Befintlig svenska:** Ange även den privata nyckeln för att kontrollera den mot den offentliga nyckeln.

**Bedömning:** Ingen ändring föreslås.

## 9406. `component::threema::config::error::key_mismatch`

**Engelska:** The public key does not match the private key.

**Befintlig svenska:** Den offentliga nyckeln stämmer inte överens med den privata nyckeln.

**Bedömning:** Ingen ändring föreslås.

## 9407. `component::threema::config::error::invalid_key`

**Engelska:** Key must be a 64-character hex string (32 bytes).

**Befintlig svenska:** Nyckeln måste vara en hexsträng med 64 tecken (32 byte).

**Bedömning:** Ingen ändring föreslås.

## 9408. `component::threema::config::error::invalid_gateway_id`

**Engelska:** Gateway ID must start with * followed by 7 alphanumeric characters.

**Befintlig svenska:** Gateway-ID måste börja med * följt av sju alfanumeriska tecken.

**Bedömning:** Ingen ändring föreslås.

## 9409. `component::threema::config::error::invalid_auth`

**Engelska:** [%key:common::config_flow::error::invalid_auth%]

**Befintlig svenska:** Ogiltig autentisering

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::invalid_auth`; det ingår ännu inte i det insamlade underlaget.

## 9410. `component::threema::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** Det gick inte att ansluta

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::error::cannot_connect`; det ingår ännu inte i det insamlade underlaget.

## 9411. `component::threema::config::abort::key_generation_failed`

**Engelska:** Failed to generate encryption keys.

**Befintlig svenska:** Det gick inte att generera krypteringsnycklar.

**Bedömning:** Ingen ändring föreslås.

## 9412. `component::threema::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_service%]

**Befintlig svenska:** Tjänsten är redan konfigurerad

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::abort::already_configured_service`; det ingår ännu inte i det insamlade underlaget.

## 9413. `component::nexblue::entity::binary_sensor::is_lock::name`

**Engelska:** Cable lock state

**Befintlig svenska:** Status för kabellås

**Bedömning:** Ingen ändring föreslås.

## 9414. `component::nexblue::entity::binary_sensor::is_disable::name`

**Engelska:** Charging enabled

**Befintlig svenska:** Laddning aktiverad

**Bedömning:** Ingen ändring föreslås.

## 9415. `component::ifttt::exceptions::trigger_failed::message`

**Engelska:** Failed to trigger the IFTTT webhook.

**Befintlig svenska:** Det gick inte att utlösa IFTTT-webbkroken.

**Bedömning:** Ingen ändring föreslås.

## 9416. `component::lifx_cloud::exceptions::activate_failed::message`

**Engelska:** Failed to activate the LIFX Cloud scene: {error}

**Befintlig svenska:** Det gick inte att aktivera LIFX Cloud-scenen: {error}

**Bedömning:** Ingen ändring föreslås.

## 9417. `component::xbox::issues::deprecated_entity::title`

**Engelska:** The Xbox {name} entity is deprecated

**Befintlig svenska:** Xbox-entiteten {name} är föråldrad

**Bedömning:** Ingen ändring föreslås.

## 9418. `component::xbox::issues::deprecated_entity::fix_flow::step::confirm::description`

**Engelska:** The Xbox entity `{entity}` is no longer functional and will be removed in a future release.

Please update any automations and scripts that use this entity, then press **Submit** to remove it now and resolve this issue.

**Befintlig svenska:** Xbox-entiteten `{entity}` fungerar inte längre och tas bort i en kommande version.

Uppdatera de automatiseringar och skript som använder entiteten och tryck sedan på **Skicka** för att ta bort den nu och lösa problemet.

**Bedömning:** Ingen ändring föreslås.

## 9419. `component::environment_canada::services::get_precipitation_forecast::name`

**Engelska:** Get precipitation forecast

**Befintlig svenska:** Hämta nederbördsprognos

**Bedömning:** Ingen ändring föreslås.

## 9420. `component::environment_canada::services::get_precipitation_forecast::fields::precip_type::name`

**Engelska:** Precipitation type

**Befintlig svenska:** Nederbördstyp

**Bedömning:** Ingen ändring föreslås.


## Livegranskning 2026-11-24

Alla 240 poster återlästes från Lokalise och jämfördes med Core-källträdet vid commit `2fdaa177f3e94535b3b649fb1ffc2dbba52eb4ce`. Samtliga 240 nycklar och direktkällor matchade. Tjugotvå engelska nyckelreferenser återstår i aktuell källtext; ytterligare sex källor har nu direkttext efter källändringar. Totalt kontrollerades 28 referensanvändningar mot 20 unika mål; alla mål finns och konsumenternas svenska följer målen.

### Bedömning och uppföljning

- 23 av de aktuella svenska livevärdena skiljer sig från den äldre rapportögonblicksbilden. Ändringarna är redan sparade i Lokalise och befanns korrekta; rapportens befintlig-text har synkats med livevärdena utan nya API-skrivningar.
- Fronius måltext (9188–9191) är nu synkroniserad mellan konfigurering och omkonfigurering. Långtexten täcker AC-effekt, batteriladdning/urladdning, 15-minuters återutsändning, lägsta reserv och nätladdning.
- LIFX-serienumret (9248) säger nu korrekt tolv tecken och nätverksutsändning. OpenAI API-nyckeln, Threema-nyckelhantering, Monarch Money-återautentisering och Theben Conexa-inloggning följer sina fullständiga källtexter.
- Referensmålen lästes separat via API: 28/28 användningar matchar, inga saknade mål. Referenserna är korrekt återgivna i Lokalise; där översättningen är gemensam behålls referensen.
- Alla platshållare matchar på 240 poster; inga pluralposter. Ingen ny lokal översättningsändring behövdes efter live-readback. Svlang naturalness-poäng på utvalda meningar var 8,8–10/10; verktygsvarningar för V2, MFA och sammansatta egennamn bedömdes manuellt och godkändes i sammanhanget. Hunspell-flaggor på tekniska egennamn och `MFA-kod` är inte stavfel. Terminologistödet bekräftade API-nyckel, återautentisering och Home Assistant-termer.
- Nästa batch börjar vid 9421; Core-granskningen fortsätter.
