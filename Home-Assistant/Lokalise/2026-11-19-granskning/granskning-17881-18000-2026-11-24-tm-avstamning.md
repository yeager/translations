# Home Assistant Core – historisk avstämning 17881–18000

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 96 direkta källtexter matchar HA Core-källan; 21 referensanvändningar med 17 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 3 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 17881 | 857235867 | `component::unifi_access::exceptions::update_failed_timeout::message` | Timeout communicating with the UniFi Access API. | Timeout för kommunikation med UniFi Access API. | Core-literal match |
| 17882 | 857235866 | `component::unifi_access::exceptions::update_failed_connection::message` | Error connecting to the UniFi Access API. | Fel vid anslutning till UniFi Access API. | Core-literal match |
| 17883 | 857235865 | `component::unifi_access::exceptions::update_failed_auth::message` | Authentication failed while updating data. | Autentiseringen misslyckades vid uppdatering av data. | Core-literal match |
| 17884 | 857235864 | `component::unifi_access::exceptions::update_failed_api::message` | Error communicating with the UniFi Access API. | Fel vid kommunikation med UniFi Access API. | Core-literal match |
| 17885 | 857235863 | `component::unifi_access::exceptions::cannot_connect::message` | Unable to connect to UniFi Access at {host}. | Det går inte att ansluta till UniFi Access på {host}. | Core-literal match |
| 17886 | 857235862 | `component::unifi_access::exceptions::auth_failed::message` | Authentication failed for UniFi Access at {host}. | Autentisering misslyckades för UniFi Access på {host}. | Core-literal match |
| 17887 | 857225166 | `component::indevolt::exceptions::update_failed::message` | Device update failed: {error} | Enhetsuppdatering misslyckades: {error} | Core-literal match |
| 17888 | 857225165 | `component::indevolt::exceptions::config_entry_not_ready::message` | Device config retrieval failed: {error} | Hämtning av enhetskonfiguration misslyckades: {error} | Core-literal match |
| 17889 | 857214682 | `component::arcam_fmj::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |
| 17890 | 857214681 | `component::arcam_fmj::config::error::invalid_host` | Invalid hostname or IP address | Ogiltigt värdnamn eller IP-adress | Shared reference target checked |
| 17891 | 857214680 | `component::arcam_fmj::config::error::connection_refused` | Host refused connection | Värden avvisade anslutningen | Core-literal match |
| 17892 | 857214679 | `component::arcam_fmj::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 17893 | 857205580 | `component::fritz::exceptions::error_upnp_disabled::message` | UPnP is disabled on the FRITZ!Box. Please enable UPnP to use this integration. | UPnP är inaktiverat på FRITZ!Box. Aktivera UPnP för att använda den här integrationen. | Core-literal match |
| 17894 | 857205579 | `component::fritz::exceptions::error_connecting::message` | Error connecting to the FRITZ!Box: {error} | Fel vid anslutning till FRITZ!Box: {error} | Core-literal match |
| 17895 | 857205500 | `component::indevolt::config::step::discovery_confirm::title` | Discovered Indevolt {model} | Upptäckte Indevolt {model} | Source-path follow-up open |
| 17896 | 857205499 | `component::indevolt::config::step::discovery_confirm::description` | Do you want to add {model} ({host}) to Home Assistant? | Vill du lägga till {model} ({host}) i Home Assistant? | Source-path follow-up open |
| 17897 | 857205460 | `component::backblaze_b2::exceptions::invalid_auth::message` | Authentication failed using the provided key ID and application key. | Autentiseringen misslyckades med det angivna nyckel-ID:t och programnyckeln. | Core-literal match |
| 17898 | 857204938 | `component::sma::exceptions::invalid_auth::message` | Invalid authentication for SMA device | Ogiltig autentisering för SMA-enheten | Core-literal match |
| 17899 | 857204937 | `component::sma::exceptions::cannot_connect::message` | Could not connect to SMA device | Kunde inte ansluta till SMA-enheten | Core-literal match |
| 17900 | 857204738 | `component::mqtt::exceptions::mqtt_not_enabled_cannot_subscribe::message` | Cannot subscribe to topic "{topic}" because MQTT is not enabled, make sure MQTT is set up correctly. | Det går inte att prenumerera på ämnet ”{topic}” eftersom MQTT inte är aktiverat. Kontrollera att MQTT är korrekt konfigurerat. | Core-literal match |
| 17901 | 857204737 | `component::mqtt::exceptions::invalid_platform_config_message::message` | Reloading YAML config for manually configured MQTT `{domain}` item failed. Message: {message} | Det gick inte att ladda om YAML-konfigurationen för det manuellt konfigurerade MQTT-objektet `{domain}`. Meddelande: {message} | Core-literal match |
| 17902 | 857198274 | `component::solarlog::exceptions::update_failed::message` | Error while updating data from the API. | Fel vid uppdatering av data från API:et. | Core-literal match |
| 17903 | 857152353 | `component::tankerkoenig::exceptions::connection_error::message` | Failed to connect to the Tankerkoenig API. Please check your network connection. | Det gick inte att ansluta till Tankerkoenig-API:t. Kontrollera din nätverksanslutning. | Core-literal match |
| 17904 | 857148153 | `component::isy994::config::step::user::data_description::verify_ssl` | Verify the controller's TLS certificate. Leave disabled for ISY-994/eisy/Polisy controllers using their default self-signed certificate. | Kontrollera styrenhetens TLS-certifikat. Lämna inställningen inaktiverad för ISY-994/eisy/Polisy-styrenheter som använder sitt standardsjälvsignerade certifikat. | Core-literal match |
| 17905 | 857148152 | `component::isy994::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 17906 | 857148151 | `component::isy994::config::error::ssl_error` | TLS handshake failed. The controller may require a newer TLS version, or SSL verification may be failing due to a self-signed certificate. | TLS-handskakningen misslyckades. Styrenheten kan kräva en nyare TLS-version, eller så kan SSL-verifieringen misslyckas på grund av ett självsignerat certifikat. | Core-literal match |
| 17907 | 857123522 | `component::lyric::exceptions::invalid_fan_mode::message` | The fan mode {fan_mode} is not supported by this device | Fläktläget {fan_mode} stöds inte av den här enheten | Source-path follow-up open |
| 17908 | 857123521 | `component::lyric::exceptions::failed_to_set_temperature::message` | Failed to set temperature | Misslyckades med att ställa in temperaturen | Core-literal match |
| 17909 | 857123520 | `component::lyric::exceptions::failed_to_set_preset_mode::message` | Failed to set preset mode | Misslyckades med att ställa in förinställt läge | Core-literal match |
| 17910 | 857123519 | `component::lyric::exceptions::failed_to_set_hvac_mode::message` | Failed to set HVAC mode | Misslyckades med att ställa in HVAC-läge | Core-literal match |
| 17911 | 857123518 | `component::lyric::exceptions::failed_to_set_hold_time::message` | Failed to set hold time | Misslyckades med att ställa in väntetid | Core-literal match |
| 17912 | 857123517 | `component::lyric::exceptions::failed_to_set_fan_mode::message` | Failed to set fan mode | Misslyckades med att ställa in fläktläge | Core-literal match |
| 17913 | 856977887 | `component::openevse::exceptions::unsupported_feature::message` | The charger does not support this feature. | Laddaren stöder inte den här funktionen. | Core-literal match |
| 17914 | 856977886 | `component::openevse::exceptions::invalid_value::message` | Value {value} is invalid for the charger. | Värdet {value} är ogiltigt för laddaren. | Core-literal match |
| 17915 | 856977885 | `component::openevse::exceptions::communication_error::message` | Failed to communicate with the charger | Misslyckades med att kommunicera med laddaren | Core-literal match |
| 17916 | 856977884 | `component::openevse::exceptions::authentication_error::message` | Authentication failed | Autentiseringen misslyckades | Core-literal match |
| 17917 | 856959891 | `component::nfandroidtv::exceptions::connection_failed::message` | Failed to connect to host: {host} | Det gick inte att ansluta till värden: {host} | Core-literal match |
| 17918 | 856779422 | `component::casper_glow::exceptions::device_not_found::message` | Could not find Casper Glow device with address {address}: {reason} | Kunde inte hitta Casper Glow-enheten med adress {address}: {reason} | Core-literal match |
| 17919 | 856769319 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::name` | Custom local AQI options | Anpassade lokala AQI-inställningar | Shared reference target checked |
| 17920 | 856769318 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::description` | Country and custom local AQI must match. You can find the available combinations here: {air_quality_coverage_url} | Land och anpassad lokal luftkvalitetsindex (AQI) måste stämma överens. Här hittar du de tillgängliga kombinationerna: {air_quality_coverage_url} | Shared reference target checked |
| 17921 | 856769317 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::data_description::enable_custom_laqi` | Select to enable a custom local air quality index | Markera för att aktivera ett anpassat lokalt luftkvalitetsindex | Shared reference target checked |
| 17922 | 856769316 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::data_description::custom_laqi` | The target air quality index | Målindexet för luftkvalitet | Shared reference target checked |
| 17923 | 856769315 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::data_description::country` | Country of the location | Landet där platsen är | Shared reference target checked |
| 17924 | 856769314 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::data::enable_custom_laqi` | Enable custom local AQI | Aktivera anpassad lokal AQI | Shared reference target checked |
| 17925 | 856769313 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::data::custom_laqi` | Custom local AQI | Anpassad lokal AQI | Shared reference target checked |
| 17926 | 856769312 | `component::google_air_quality::config_subentries::location::step::location::sections::custom_local_aqi_options::data::country` | Country | Land | Shared reference target checked |
| 17927 | 856769311 | `component::google_air_quality::config_subentries::location::error::missing_custom_laqi_options` | Please provide both country and custom local AQI when custom local AQI is enabled. | Ange både land och anpassad lokal AQI när anpassad lokal AQI är aktiverad. | Shared reference target checked |
| 17928 | 856769310 | `component::google_air_quality::config_subentries::location::error::mismatch_country_and_laqi` | This local AQI is not available for the selected country. Please select an available combination. | Denna lokala AQI är inte tillgängligt för det valda landet. Vänligen välj en tillgänglig kombination. | Shared reference target checked |
| 17929 | 856769309 | `component::google_air_quality::config_subentries::location::error::cannot_connect` | Unable to connect to the Google Air Quality API:<br><br>{error_message} | Det går inte att ansluta till Google Air Quality API:<br><br>{error_message} | Shared reference target checked |
| 17930 | 856769308 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::name` | Custom local AQI options | Anpassade lokala AQI-inställningar | Core-literal match |
| 17931 | 856769307 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::description` | Country and custom local AQI must match. You can find the available combinations here: {air_quality_coverage_url} | Land och anpassad lokal luftkvalitetsindex (AQI) måste stämma överens. Här hittar du de tillgängliga kombinationerna: {air_quality_coverage_url} | Core-literal match |
| 17932 | 856769306 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::data_description::enable_custom_laqi` | Select to enable a custom local air quality index | Markera för att aktivera ett anpassat lokalt luftkvalitetsindex | Core-literal match |
| 17933 | 856769305 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::data_description::custom_laqi` | The target air quality index | Målindexet för luftkvalitet | Core-literal match |
| 17934 | 856769304 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::data_description::country` | Country of the location | Landet där platsen är | Core-literal match |
| 17935 | 856769303 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::data::enable_custom_laqi` | Enable custom local AQI | Aktivera anpassad lokal AQI | Core-literal match |
| 17936 | 856769302 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::data::custom_laqi` | Custom local AQI | Anpassad lokal AQI | Core-literal match |
| 17937 | 856769301 | `component::google_air_quality::config::step::user::sections::custom_local_aqi_options::data::country` | Country | Land | Shared reference target checked |
| 17938 | 856769300 | `component::google_air_quality::config::error::missing_custom_laqi_options` | Please provide both country and custom local AQI when custom local AQI is enabled. | Ange både land och anpassad lokal AQI när anpassad lokal AQI är aktiverad. | Core-literal match |
| 17939 | 856769299 | `component::google_air_quality::config::error::mismatch_country_and_laqi` | This local AQI is not available for the selected country. Please select an available combination. | Denna lokala AQI är inte tillgängligt för det valda landet. Vänligen välj en tillgänglig kombination. | Core-literal match |
| 17940 | 856765787 | `component::mastodon::exceptions::update_failed::message` | Update failed. | Uppdatering misslyckades. | Core-literal match |
| 17941 | 856765786 | `component::mastodon::exceptions::failed_to_connect::message` | Failed to connect. | Det gick inte att ansluta. | Core-literal match |
| 17942 | 856554573 | `component::light::services::turn_on::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17943 | 856554572 | `component::light::services::turn_off::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17944 | 856554571 | `component::light::services::toggle::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17945 | 856554570 | `component::light::common::section_additional_fields_name` | Additional options | Ytterligare alternativ | Core-literal match |
| 17946 | 856551632 | `component::fan::services::increase_speed::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17947 | 856551631 | `component::fan::services::decrease_speed::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Shared reference target checked |
| 17948 | 856551630 | `component::fan::common::section_additional_fields_name` | Additional options | Ytterligare alternativ | Core-literal match |
| 17949 | 856551542 | `component::climate::services::set_temperature::sections::temperature_range::name` | Temperature range | Temperaturintervall | Core-literal match |
| 17950 | 856520381 | `component::kitchen_sink::services::test_service_1::sections::additional_fields::name` | Additional options | Ytterligare alternativ | Core-literal match |
| 17951 | 856520380 | `component::kitchen_sink::services::test_service_1::sections::additional_fields::description` | Some additional things | Några ytterligare saker | Core-literal match |
| 17952 | 856458251 | `component::zwave_js::services::set_user::name` | Set user | Ställ in användare | Core-literal match |
| 17953 | 856458250 | `component::zwave_js::services::set_user::fields::user_type::name` | User type | Användartyp | Core-literal match |
| 17954 | 856458249 | `component::zwave_js::services::set_user::fields::user_type::description` | The type of user (e.g. general, programming, remote_only). | Användartyp (t.ex. allmän, programmering, endast fjärråtkomst). | Core-literal match |
| 17955 | 856458248 | `component::zwave_js::services::set_user::fields::user_name::name` | User name | Användarnamn | Core-literal match |
| 17956 | 856458247 | `component::zwave_js::services::set_user::fields::user_name::description` | Display name for the user. | Användarens visningsnamn. | Core-literal match |
| 17957 | 856458246 | `component::zwave_js::services::set_user::fields::user_id::name` | User index | Användarindex | Core-literal match |
| 17958 | 856458245 | `component::zwave_js::services::set_user::fields::user_id::description` | User slot index. If not specified, the first available slot is used. | Index för användarplats. Om inget anges används den första tillgängliga platsen. | Core-literal match |
| 17959 | 856458244 | `component::zwave_js::services::set_user::fields::credential_rule::name` | Credential rule | Autentiseringsregel | Core-literal match |
| 17960 | 856458243 | `component::zwave_js::services::set_user::fields::credential_rule::description` | Credential rule for the user (single, dual, or triple). | Autentiseringsregel för användaren (enkel, dubbel eller trippel). | Core-literal match |
| 17961 | 856458242 | `component::zwave_js::services::set_user::fields::active::name` | Active | Aktiv | Core-literal match |
| 17962 | 856458241 | `component::zwave_js::services::set_user::fields::active::description` | Whether the user is active. | Anger om användaren är aktiv. | Core-literal match |
| 17963 | 856458240 | `component::zwave_js::services::set_user::description` | Creates or updates an access-control user on a lock entity. When no user_id is given, a new user is created. A credential (PIN code or password) can be written in the same call. Returns the allocated user_id, plus the credential_slot when a credential was written, for each targeted lock entity. | Skapar eller uppdaterar en användare för åtkomstkontroll på en låsenhet. Om inget user_id anges skapas en ny användare. En autentiseringsuppgift (PIN-kod eller lösenord) kan anges i samma anrop. Returnerar det tilldelade user_id, samt credential_slot om en autentiseringsuppgift angivits, för varje berörd låsenhet. | Core-literal match |
| 17964 | 856458239 | `component::zwave_js::services::set_credential::name` | Set credential | Ställ in autentiseringsuppgifter | Core-literal match |
| 17965 | 856458238 | `component::zwave_js::services::set_credential::fields::user_id::name` | User index | Användarindex | Core-literal match |
| 17966 | 856458237 | `component::zwave_js::services::set_credential::fields::user_id::description` | User slot index to assign the credential to. Must refer to an existing user. | Det användarplatsindex som autentiseringsuppgifterna ska tilldelas. Måste avse en befintlig användare. | Core-literal match |
| 17967 | 856458236 | `component::zwave_js::services::set_credential::fields::credential_type::name` | Credential type | Typ av autentisering | Core-literal match |
| 17968 | 856458235 | `component::zwave_js::services::set_credential::fields::credential_type::description` | The type of credential (pin_code or password). | Typ av autentiseringsuppgift (PIN-kod eller lösenord). | Core-literal match |
| 17969 | 856458234 | `component::zwave_js::services::set_credential::fields::credential_slot::name` | Credential slot | Plats för autentiseringsuppgift | Core-literal match |
| 17970 | 856458233 | `component::zwave_js::services::set_credential::fields::credential_slot::description` | Credential slot index. If not specified, the first available slot is used. | Index för autentiseringsuppgift. Om inget anges används den första tillgängliga platsen. | Core-literal match |
| 17971 | 856458232 | `component::zwave_js::services::set_credential::fields::credential_data::name` | Credential data | Autentiseringsuppgift | Core-literal match |
| 17972 | 856458231 | `component::zwave_js::services::set_credential::fields::credential_data::description` | The credential data (e.g. PIN digits or password string). | Autentiseringsuppgift (t.ex. PIN-siffror eller lösenordssträng). | Core-literal match |
| 17973 | 856458230 | `component::zwave_js::services::set_credential::description` | Adds or updates a credential (PIN code or password) for an existing user on a lock entity. Call `set_user` first to create a user if needed. | Lägger till eller uppdaterar en inloggningsuppgift (PIN-kod eller lösenord) för en befintlig användare på en låsenhet. Använd först `set_user` för att skapa en användare om det behövs. | Core-literal match |
| 17974 | 856458229 | `component::zwave_js::services::get_users::name` | Get users | Hämta användare | Core-literal match |
| 17975 | 856458228 | `component::zwave_js::services::get_users::description` | Lists all access-control users and their credential references on a lock. | Listar alla användare av åtkomstkontroll och deras autentiseringsuppgifter på ett lås. | Core-literal match |
| 17976 | 856458227 | `component::zwave_js::services::get_credential_capabilities::name` | Get credential capabilities | Hämta autentiseringsfunktioner | Core-literal match |
| 17977 | 856458226 | `component::zwave_js::services::get_credential_capabilities::description` | Queries the credential management capabilities of a lock. | Hämtar information om ett lås funktioner för hantering av autentiseringsuppgifter. | Core-literal match |
| 17978 | 856458225 | `component::zwave_js::services::delete_user::name` | Delete user | Ta bort användare | Core-literal match |
| 17979 | 856458224 | `component::zwave_js::services::delete_user::fields::user_id::name` | User index | Användarindex | Core-literal match |
| 17980 | 856458223 | `component::zwave_js::services::delete_user::fields::user_id::description` | User slot index to delete. | Index för den användarplats som ska raderas. | Core-literal match |
| 17981 | 856458222 | `component::zwave_js::services::delete_user::description` | Deletes a single access-control user from a lock. | Tar bort en enskild åtkomstkontrollanvändare från ett lås. | Core-literal match |
| 17982 | 856458221 | `component::zwave_js::services::delete_credential::name` | Delete credential | Radera inloggningsuppgift | Core-literal match |
| 17983 | 856458220 | `component::zwave_js::services::delete_credential::fields::user_id::name` | User index | Användarindex | Core-literal match |
| 17984 | 856458219 | `component::zwave_js::services::delete_credential::fields::user_id::description` | User slot index that owns the credential. | Användarplatsindex som äger autentiseringsuppgifterna. | Core-literal match |
| 17985 | 856458218 | `component::zwave_js::services::delete_credential::fields::credential_type::name` | Credential type | Typ av autentiseringsuppgifter | Core-literal match |
| 17986 | 856458217 | `component::zwave_js::services::delete_credential::fields::credential_type::description` | The type of credential to delete (pin_code or password). | Vilken typ av inloggningsuppgifter som ska raderas (PIN-kod eller lösenord). | Core-literal match |
| 17987 | 856458216 | `component::zwave_js::services::delete_credential::fields::credential_slot::name` | Credential slot | Plats för autentiseringsuppgift | Core-literal match |
| 17988 | 856458215 | `component::zwave_js::services::delete_credential::fields::credential_slot::description` | Credential slot index to delete. | Index för den autentiseringsplats som ska raderas. | Core-literal match |
| 17989 | 856458214 | `component::zwave_js::services::delete_credential::description` | Deletes a single credential from a lock. | Tar bort en enskild behörighet från ett lås. | Core-literal match |
| 17990 | 856458213 | `component::zwave_js::services::delete_all_users::name` | Delete all users | Ta bort alla användare | Core-literal match |
| 17991 | 856458212 | `component::zwave_js::services::delete_all_users::description` | Deletes all access-control users from a lock. | Tar bort alla användare med åtkomstbehörighet från ett lås. | Core-literal match |
| 17992 | 856458211 | `component::zwave_js::services::delete_all_credentials::name` | Delete all credentials | Ta bort alla inloggningsuppgifter | Core-literal match |
| 17993 | 856458210 | `component::zwave_js::services::delete_all_credentials::fields::user_id::name` | User index | Användarindex | Core-literal match |
| 17994 | 856458209 | `component::zwave_js::services::delete_all_credentials::fields::user_id::description` | User slot index to delete all credentials for. | Användarplatsindex att ta bort alla autentiseringsuppgifter för. | Core-literal match |
| 17995 | 856458208 | `component::zwave_js::services::delete_all_credentials::description` | Deletes all credentials for a user on a lock. | Tar bort alla autentiseringsuppgifter för en användare på ett lås. | Core-literal match |
| 17996 | 856458207 | `component::zwave_js::exceptions::user_rejected_unknown::message` | The device rejected the user update without giving a reason. | Enheten avvisade användaruppdateringen utan att ange någon anledning. | Core-literal match |
| 17997 | 856458206 | `component::zwave_js::exceptions::user_rejected_modify_empty::message` | Cannot modify user: the slot is empty. | Det går inte att ändra användare: platsen är tom. | Core-literal match |
| 17998 | 856458205 | `component::zwave_js::exceptions::user_rejected_add_occupied::message` | Cannot add user: the target slot is already in use. | Det går inte att lägga till användare: målplatsen används redan. | Core-literal match |
| 17999 | 856458204 | `component::zwave_js::exceptions::set_user_failed::message` | Failed to set user: {error} | Misslyckades med att ange användare: {error} | Core-literal match |
| 18000 | 856458203 | `component::zwave_js::exceptions::set_credential_failed::message` | Failed to set credential: {error} | Misslyckades med att ange inloggningsuppgifter: {error} | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 857205500 | `component::indevolt::config::step::discovery_confirm::title` | Discovered Indevolt {model} |
| 857205499 | `component::indevolt::config::step::discovery_confirm::description` | Do you want to add {model} ({host}) to Home Assistant? |
| 857123522 | `component::lyric::exceptions::invalid_fan_mode::message` | The fan mode {fan_mode} is not supported by this device |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
