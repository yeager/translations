# Home Assistant Core – historisk avstämning 20161–20280

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 34 direkta källtexter matchar HA Core-källan; 50 referensanvändningar med 21 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 36 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20161 | 834982908 | `component::alarm_control_panel::triggers::armed_night::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20162 | 834982907 | `component::alarm_control_panel::triggers::armed_home::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20163 | 834982906 | `component::alarm_control_panel::triggers::armed_away::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20164 | 834982905 | `component::alarm_control_panel::triggers::armed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20165 | 834982904 | `component::alarm_control_panel::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20166 | 834982903 | `component::air_quality::triggers::voc_ratio_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20167 | 834982902 | `component::air_quality::triggers::voc_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20168 | 834982901 | `component::air_quality::triggers::so2_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20169 | 834982900 | `component::air_quality::triggers::smoke_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20170 | 834982899 | `component::air_quality::triggers::smoke_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20171 | 834982898 | `component::air_quality::triggers::pm4_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20172 | 834982897 | `component::air_quality::triggers::pm25_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20173 | 834982896 | `component::air_quality::triggers::pm1_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20174 | 834982895 | `component::air_quality::triggers::pm10_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20175 | 834982894 | `component::air_quality::triggers::ozone_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20176 | 834982893 | `component::air_quality::triggers::no_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20177 | 834982892 | `component::air_quality::triggers::no2_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20178 | 834982891 | `component::air_quality::triggers::n2o_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20179 | 834982890 | `component::air_quality::triggers::gas_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20180 | 834982889 | `component::air_quality::triggers::gas_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20181 | 834982888 | `component::air_quality::triggers::co_detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20182 | 834982887 | `component::air_quality::triggers::co_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20183 | 834982886 | `component::air_quality::triggers::co_cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20184 | 834982885 | `component::air_quality::triggers::co2_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20185 | 834982884 | `component::air_quality::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20186 | 834955930 | `component::motion::triggers::detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20187 | 834955929 | `component::motion::triggers::cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20188 | 834955928 | `component::motion::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20189 | 834637048 | `component::media_player::triggers::turned_on::name` | Media player turned on | Mediaspelare slogs på | Core-literal match |
| 20190 | 834637047 | `component::media_player::triggers::turned_on::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 20191 | 834637046 | `component::media_player::triggers::turned_on::description` | Triggers when one or more media players turn on. | Utlöses när en eller flera mediespelare slås på. | Core-literal match |
| 20192 | 834637045 | `component::media_player::triggers::turned_off::name` | Media player turned off | Mediaspelare stängdes av | Core-literal match |
| 20193 | 834637044 | `component::media_player::triggers::turned_off::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 20194 | 834637043 | `component::media_player::triggers::turned_off::description` | Triggers when one or more media players turn off. | Utlöses när en eller flera mediespelare stängs av. | Core-literal match |
| 20195 | 834637042 | `component::media_player::triggers::started_playing::name` | Media player started playing | Mediaspelare började spela | Core-literal match |
| 20196 | 834637041 | `component::media_player::triggers::started_playing::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 20197 | 834637040 | `component::media_player::triggers::started_playing::description` | Triggers when one or more media players start playing. | Utlöses när en eller flera mediespelare börjar spela. | Core-literal match |
| 20198 | 834637039 | `component::media_player::triggers::paused_playing::name` | Media player paused playing | Mediaspelare pausade uppspelningen | Core-literal match |
| 20199 | 834637038 | `component::media_player::triggers::paused_playing::fields::behavior::name` | Trigger when | Utlös när | Shared reference target checked |
| 20200 | 834637037 | `component::media_player::triggers::paused_playing::description` | Triggers when one or more media players pause playing. | Utlöses när en eller flera mediespelare pausar uppspelningen. | Core-literal match |
| 20201 | 834199309 | `component::scrape::options::step::init::sections::auth::name` | Authentication settings | Autentiseringsinställningar | Shared reference target checked |
| 20202 | 834199308 | `component::scrape::options::step::init::sections::auth::description` | Provide authentication details to access the resource. | Ange autentiseringsuppgifter för att få åtkomst till resursen. | Shared reference target checked |
| 20203 | 834199307 | `component::scrape::options::step::init::sections::auth::data_description::authentication` | Type of the HTTP authentication. Either basic or digest. | Typ av HTTP-autentisering. Antingen basic eller digest. | Shared reference target checked |
| 20204 | 834199306 | `component::scrape::options::step::init::sections::auth::data::username` | Username | Användarnamn | Shared reference target checked |
| 20205 | 834199305 | `component::scrape::options::step::init::sections::auth::data::password` | Password | Lösenord | Shared reference target checked |
| 20206 | 834199304 | `component::scrape::options::step::init::sections::auth::data::authentication` | Select authentication method | Välj autentiseringsmetod | Shared reference target checked |
| 20207 | 834199303 | `component::scrape::options::step::init::sections::advanced::name` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 20208 | 834199302 | `component::scrape::options::step::init::sections::advanced::description` | Provide additional settings for the resource. | Ange ytterligare inställningar för resursen. | Source-path follow-up open |
| 20209 | 834199301 | `component::scrape::options::step::init::sections::advanced::data_description::verify_ssl` | Enables/disables verification of SSL/TLS certificate, for example if it is self-signed. | Aktiverar/inaktiverar verifiering av SSL/TLS-certifikat, t.ex. om det är självsignerat. | Source-path follow-up open |
| 20210 | 834199300 | `component::scrape::options::step::init::sections::advanced::data_description::timeout` | Timeout for connection to website. | Timeout för anslutning till webbplats. | Source-path follow-up open |
| 20211 | 834199299 | `component::scrape::options::step::init::sections::advanced::data_description::headers` | Headers to use for the web request. | Adressinformation att använda för webbförfrågan. | Source-path follow-up open |
| 20212 | 834199298 | `component::scrape::options::step::init::sections::advanced::data_description::encoding` | Character encoding to use. Defaults to UTF-8. | Teckenkodning att använda. Standard är UTF-8 | Source-path follow-up open |
| 20213 | 834199297 | `component::scrape::options::step::init::sections::advanced::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Source-path follow-up open |
| 20214 | 834199296 | `component::scrape::options::step::init::sections::advanced::data::timeout` | Timeout | Tidsgräns | Source-path follow-up open |
| 20215 | 834199295 | `component::scrape::options::step::init::sections::advanced::data::headers` | Headers | Adressinformation | Source-path follow-up open |
| 20216 | 834199294 | `component::scrape::options::step::init::sections::advanced::data::encoding` | Character encoding | Teckenkodning | Source-path follow-up open |
| 20217 | 834199293 | `component::scrape::options::step::init::data_description::resource` | The URL to the website that contains the value. | URL:en till webbplatsen som innehåller värdet. | Shared reference target checked |
| 20218 | 834199292 | `component::scrape::options::step::init::data_description::payload` | Payload to use when method is POST. | Nyttolast som ska användas när metoden är POST | Shared reference target checked |
| 20219 | 834199291 | `component::scrape::options::step::init::data::resource` | Resource | Resurs | Shared reference target checked |
| 20220 | 834199290 | `component::scrape::options::step::init::data::payload` | Payload | Nyttolast | Shared reference target checked |
| 20221 | 834199289 | `component::scrape::options::step::init::data::method` | Method | Metod | Shared reference target checked |
| 20222 | 834199288 | `component::scrape::options::error::resource_error` | Could not update REST data. Verify your configuration | Kunde inte uppdatera REST-data. Kontrollera konfigurationen. | Shared reference target checked |
| 20223 | 834199287 | `component::scrape::options::error::no_data` | REST data is empty. Verify your configuration | REST-data är tom. Verifiera din konfiguration. | Shared reference target checked |
| 20224 | 834199286 | `component::scrape::config_subentries::entity::step::user::sections::advanced::name` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 20225 | 834199285 | `component::scrape::config_subentries::entity::step::user::sections::advanced::description` | Provide additional settings for the sensor. | Ange ytterligare inställningar för sensorn. | Source-path follow-up open |
| 20226 | 834199284 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::value_template` | Defines a template to get the state of the sensor. | Definierar en mall för att hämta sensorns status. | Source-path follow-up open |
| 20227 | 834199283 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::unit_of_measurement` | Choose unit of measurement or create your own. | Välj måttenhet eller skapa din egen. | Source-path follow-up open |
| 20228 | 834199282 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::state_class` | The state_class of the sensor. | Sensorns state_class. | Source-path follow-up open |
| 20229 | 834199281 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::device_class` | The type/class of the sensor to set the icon in the frontend. | Typ/klass på den sensor vars ikon ska ställas in i gränssnittet | Source-path follow-up open |
| 20230 | 834199280 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::availability` | Defines a template to get the availability of the sensor. | Definierar en mall för att få information om sensorns tillgänglighet. | Source-path follow-up open |
| 20231 | 834199279 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::attribute` | Get value of an attribute on the selected tag. | Hämta värdet för ett attribut med den valda taggen. | Source-path follow-up open |
| 20232 | 834199278 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::value_template` | Value template | Värdemall | Source-path follow-up open |
| 20233 | 834199277 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::unit_of_measurement` | Unit of measurement | Måttenhet | Source-path follow-up open |
| 20234 | 834199276 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::state_class` | State class | Tillståndsklass | Source-path follow-up open |
| 20235 | 834199275 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::device_class` | Device class | Enhetsklass | Source-path follow-up open |
| 20236 | 834199274 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::availability` | Availability template | Tillgänglighetsmall | Source-path follow-up open |
| 20237 | 834199273 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::attribute` | Attribute | Attribut | Source-path follow-up open |
| 20238 | 834199272 | `component::scrape::config_subentries::entity::step::user::data_description::select` | Defines what tag to search for. Check Beautifulsoup CSS selectors for details. | Definierar vilken tagg att söka efter. Kolla Beautifulsoup CSS-selectors för mer detaljer. | Core-literal match |
| 20239 | 834199271 | `component::scrape::config_subentries::entity::step::user::data_description::index` | Defines which of the elements returned by the CSS selector to use. | Anger vilka av de element som returneras av CSS-selektorn som ska användas. | Core-literal match |
| 20240 | 834199270 | `component::scrape::config_subentries::entity::step::user::data::select` | Select | Välj | Core-literal match |
| 20241 | 834199269 | `component::scrape::config_subentries::entity::step::user::data::index` | Index | Index | Core-literal match |
| 20242 | 834199268 | `component::scrape::config_subentries::entity::initiate_flow::user` | Add sensor | Lägg till sensor | Core-literal match |
| 20243 | 834199267 | `component::scrape::config_subentries::entity::entry_type` | Sensor | Sensor | Core-literal match |
| 20244 | 834199266 | `component::scrape::config::step::user::sections::auth::name` | Authentication settings | Autentiseringsinställningar | Core-literal match |
| 20245 | 834199265 | `component::scrape::config::step::user::sections::auth::description` | Provide authentication details to access the resource. | Ange autentiseringsuppgifter för att få åtkomst till resursen. | Core-literal match |
| 20246 | 834199264 | `component::scrape::config::step::user::sections::auth::data_description::authentication` | Type of the HTTP authentication. Either basic or digest. | Typ av HTTP-autentisering. Antingen basic eller digest. | Core-literal match |
| 20247 | 834199263 | `component::scrape::config::step::user::sections::auth::data::username` | Username | Användarnamn | Shared reference target checked |
| 20248 | 834199262 | `component::scrape::config::step::user::sections::auth::data::password` | Password | Lösenord | Shared reference target checked |
| 20249 | 834199261 | `component::scrape::config::step::user::sections::auth::data::authentication` | Select authentication method | Välj autentiseringsmetod | Core-literal match |
| 20250 | 834199260 | `component::scrape::config::step::user::sections::advanced::name` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 20251 | 834199259 | `component::scrape::config::step::user::sections::advanced::description` | Provide additional settings for the resource. | Ange ytterligare inställningar för resursen. | Source-path follow-up open |
| 20252 | 834199258 | `component::scrape::config::step::user::sections::advanced::data_description::verify_ssl` | Enables/disables verification of SSL/TLS certificate, for example if it is self-signed. | Aktiverar/inaktiverar verifiering av SSL/TLS-certifikat, t.ex. om det är självsignerat. | Source-path follow-up open |
| 20253 | 834199257 | `component::scrape::config::step::user::sections::advanced::data_description::timeout` | Timeout for connection to website. | Timeout för anslutning till webbplats. | Source-path follow-up open |
| 20254 | 834199256 | `component::scrape::config::step::user::sections::advanced::data_description::headers` | Headers to use for the web request. | Adressinformation att använda för webbförfrågan. | Source-path follow-up open |
| 20255 | 834199255 | `component::scrape::config::step::user::sections::advanced::data_description::encoding` | Character encoding to use. Defaults to UTF-8. | Teckenkodning att använda. Standard är UTF-8 | Source-path follow-up open |
| 20256 | 834199254 | `component::scrape::config::step::user::sections::advanced::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Source-path follow-up open |
| 20257 | 834199253 | `component::scrape::config::step::user::sections::advanced::data::timeout` | Timeout | Tidsgräns | Source-path follow-up open |
| 20258 | 834199252 | `component::scrape::config::step::user::sections::advanced::data::headers` | Headers | Adressinformation | Source-path follow-up open |
| 20259 | 834199251 | `component::scrape::config::step::user::sections::advanced::data::encoding` | Character encoding | Teckenkodning | Source-path follow-up open |
| 20260 | 834199250 | `component::scrape::config::error::no_data` | REST data is empty. Verify your configuration | REST-data är tom. Verifiera din konfiguration. | Core-literal match |
| 20261 | 834136288 | `component::update::selector::condition_behavior::options::any` | Any | Något | Source-path follow-up open |
| 20262 | 834136287 | `component::update::selector::condition_behavior::options::all` | All | Alla | Source-path follow-up open |
| 20263 | 834136286 | `component::update::conditions::is_not_available::name` | Update is not available | Uppdatering är inte tillgänglig | Core-literal match |
| 20264 | 834136285 | `component::update::conditions::is_not_available::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 20265 | 834136284 | `component::update::conditions::is_not_available::description` | Tests if one or more updates are not available. | Testar om en eller flera uppdateringar inte är tillgängliga. | Core-literal match |
| 20266 | 834136283 | `component::update::conditions::is_available::name` | Update is available | Uppdatering är tillgänglig | Core-literal match |
| 20267 | 834136282 | `component::update::conditions::is_available::fields::behavior::name` | Condition passes if | Villkoret uppfylls om | Shared reference target checked |
| 20268 | 834136281 | `component::update::conditions::is_available::description` | Tests if one or more updates are available. | Testar om en eller flera uppdateringar finns tillgängliga. | Core-literal match |
| 20269 | 834136280 | `component::update::common::condition_behavior_name` | Condition passes if | Villkoret uppfylls om | Core-literal match |
| 20270 | 834044806 | `component::ruckus_unleashed::config::abort::invalid_host` | Invalid hostname or IP address | Ogiltigt värdnamn eller IP-adress | Shared reference target checked |
| 20271 | 834008502 | `component::tuya::services::set_feeder_meal_plan::name` | Set feeder meal plan data | Ställ in måltidsplandata för matare | Core-literal match |
| 20272 | 834008501 | `component::tuya::services::set_feeder_meal_plan::fields::meal_plan::name` | Meal plan | Måltidsplan | Core-literal match |
| 20273 | 834008500 | `component::tuya::services::set_feeder_meal_plan::fields::meal_plan::description` | The meal plan data to set. | De måltidsplandata som ska ställas in. | Core-literal match |
| 20274 | 834008499 | `component::tuya::services::set_feeder_meal_plan::fields::device_id::name` | Device | Enhet | Shared reference target checked |
| 20275 | 834008498 | `component::tuya::services::set_feeder_meal_plan::fields::device_id::description` | The Tuya feeder. | Tuya-mataren. | Shared reference target checked |
| 20276 | 834008497 | `component::tuya::services::set_feeder_meal_plan::description` | Sets a meal plan on a Tuya feeder. | Ställer in en måltidsplan på en Tuya-matare. | Core-literal match |
| 20277 | 834008496 | `component::tuya::services::get_feeder_meal_plan::name` | Get feeder meal plan data | Hämta data om matares måltidsplan | Core-literal match |
| 20278 | 834008495 | `component::tuya::services::get_feeder_meal_plan::fields::device_id::name` | Device | Enhet | Shared reference target checked |
| 20279 | 834008494 | `component::tuya::services::get_feeder_meal_plan::fields::device_id::description` | The Tuya feeder. | Tuya-mataren. | Core-literal match |
| 20280 | 834008493 | `component::tuya::services::get_feeder_meal_plan::description` | Retrieves a meal plan from a Tuya feeder. | Hämtar en måltidsplan från en Tuya-matare. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 834199303 | `component::scrape::options::step::init::sections::advanced::name` | Additional settings |
| 834199302 | `component::scrape::options::step::init::sections::advanced::description` | Provide additional settings for the resource. |
| 834199301 | `component::scrape::options::step::init::sections::advanced::data_description::verify_ssl` | Enables/disables verification of SSL/TLS certificate, for example if it is self-signed. |
| 834199300 | `component::scrape::options::step::init::sections::advanced::data_description::timeout` | Timeout for connection to website. |
| 834199299 | `component::scrape::options::step::init::sections::advanced::data_description::headers` | Headers to use for the web request. |
| 834199298 | `component::scrape::options::step::init::sections::advanced::data_description::encoding` | Character encoding to use. Defaults to UTF-8. |
| 834199297 | `component::scrape::options::step::init::sections::advanced::data::verify_ssl` | Verify SSL certificate |
| 834199296 | `component::scrape::options::step::init::sections::advanced::data::timeout` | Timeout |
| 834199295 | `component::scrape::options::step::init::sections::advanced::data::headers` | Headers |
| 834199294 | `component::scrape::options::step::init::sections::advanced::data::encoding` | Character encoding |
| 834199286 | `component::scrape::config_subentries::entity::step::user::sections::advanced::name` | Additional settings |
| 834199285 | `component::scrape::config_subentries::entity::step::user::sections::advanced::description` | Provide additional settings for the sensor. |
| 834199284 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::value_template` | Defines a template to get the state of the sensor. |
| 834199283 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::unit_of_measurement` | Choose unit of measurement or create your own. |
| 834199282 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::state_class` | The state_class of the sensor. |
| 834199281 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::device_class` | The type/class of the sensor to set the icon in the frontend. |
| 834199280 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::availability` | Defines a template to get the availability of the sensor. |
| 834199279 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data_description::attribute` | Get value of an attribute on the selected tag. |
| 834199278 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::value_template` | Value template |
| 834199277 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::unit_of_measurement` | Unit of measurement |
| 834199276 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::state_class` | State class |
| 834199275 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::device_class` | Device class |
| 834199274 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::availability` | Availability template |
| 834199273 | `component::scrape::config_subentries::entity::step::user::sections::advanced::data::attribute` | Attribute |
| 834199260 | `component::scrape::config::step::user::sections::advanced::name` | Additional settings |
| 834199259 | `component::scrape::config::step::user::sections::advanced::description` | Provide additional settings for the resource. |
| 834199258 | `component::scrape::config::step::user::sections::advanced::data_description::verify_ssl` | Enables/disables verification of SSL/TLS certificate, for example if it is self-signed. |
| 834199257 | `component::scrape::config::step::user::sections::advanced::data_description::timeout` | Timeout for connection to website. |
| 834199256 | `component::scrape::config::step::user::sections::advanced::data_description::headers` | Headers to use for the web request. |
| 834199255 | `component::scrape::config::step::user::sections::advanced::data_description::encoding` | Character encoding to use. Defaults to UTF-8. |
| 834199254 | `component::scrape::config::step::user::sections::advanced::data::verify_ssl` | Verify SSL certificate |
| 834199253 | `component::scrape::config::step::user::sections::advanced::data::timeout` | Timeout |
| 834199252 | `component::scrape::config::step::user::sections::advanced::data::headers` | Headers |
| 834199251 | `component::scrape::config::step::user::sections::advanced::data::encoding` | Character encoding |
| 834136288 | `component::update::selector::condition_behavior::options::any` | Any |
| 834136287 | `component::update::selector::condition_behavior::options::all` | All |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
