# Home Assistant Core: knappar, IR, anslutningar och undantag

Sparat och separat återläst via Lokalises API 2026-11-19. Samtliga sparade fält var tomma när de kontrollerades och källtexterna stämde med [tidigare granskningsförslag](../2026-11-19-granskning/forslag-0001-0060.md). Variabler är bevarade. Redan översatta strängar i samma äldre rapport behölls efter kontroll och skrevs inte över.

## `component::irm_kmi::entity::sensor::uv_index::name`

**Engelska:** UV index

**Tidigare svenska:** (tom)

**Sparad svenska:** UV-index

## `component::button::selector::press_count::options::4`

**Engelska:** Quadruple press

**Tidigare svenska:** (tom)

**Sparad svenska:** Fyrdubbeltryck

## `component::button::selector::press_count::options::3`

**Engelska:** Triple press

**Tidigare svenska:** (tom)

**Sparad svenska:** Trippeltryck

## `component::button::selector::press_count::options::2`

**Engelska:** Double press

**Tidigare svenska:** (tom)

**Sparad svenska:** Dubbeltryck

## `component::button::selector::press_count::options::1`

**Engelska:** Single press

**Tidigare svenska:** (tom)

**Sparad svenska:** Enkeltryck

## `component::sony_infrared::config::step::user::title`

**Engelska:** Set up a Sony device

**Tidigare svenska:** (tom)

**Sparad svenska:** Konfigurera en Sony-enhet

## `component::sony_infrared::config::step::user::description`

**Engelska:** Select the type of Sony device and the infrared emitter that points at it.

**Tidigare svenska:** (tom)

**Sparad svenska:** Välj typen av Sony-enhet och den infraröda sändare som är riktad mot den.

## `component::sony_infrared::config::step::user::data_description::device_type`

**Engelska:** The type of Sony device to control.

**Tidigare svenska:** (tom)

**Sparad svenska:** Typen av Sony-enhet som ska styras.

## `component::sony_infrared::config::abort::already_configured`

**Engelska:** This Sony device is already set up with this infrared emitter.

**Tidigare svenska:** (tom)

**Sparad svenska:** Den här Sony-enheten är redan konfigurerad med den här infraröda sändaren.

## `component::button::conditions::is_being_held::name`

**Engelska:** Button is being held

**Tidigare svenska:** (tom)

**Sparad svenska:** Knappen hålls intryckt

## `component::button::conditions::is_being_held::description`

**Engelska:** Tests if one or more buttons are being held.

**Tidigare svenska:** (tom)

**Sparad svenska:** Kontrollerar om en eller flera knappar hålls intryckta.

## `component::button::common::condition_for_name`

**Engelska:** For at least

**Tidigare svenska:** (tom)

**Sparad svenska:** I minst

## `component::button::common::condition_behavior_name`

**Engelska:** Condition passes if

**Tidigare svenska:** (tom)

**Sparad svenska:** Villkoret är uppfyllt om

## `component::irm_kmi::exceptions::api_error::message`

**Engelska:** An error occurred while communicating with the API: {error}

**Tidigare svenska:** (tom)

**Sparad svenska:** Ett fel uppstod vid kommunikationen med API:et: {error}

## `component::shelly::entity::switch::input_lock_with_channel_name::name`

**Engelska:** {channel_name} input lock

**Tidigare svenska:** (tom)

**Sparad svenska:** Ingångslås för {channel_name}

## `component::shelly::entity::switch::input_lock::name`

**Engelska:** Input lock

**Tidigare svenska:** (tom)

**Sparad svenska:** Ingångslås

## `component::zwave_js::config::abort::serial_proxy_not_supported`

**Engelska:** Z-Wave JS can't use an ESPHome serial proxy. Use the ESPHome Z-Wave proxy instead.

**Tidigare svenska:** (tom)

**Sparad svenska:** Z-Wave JS kan inte använda en seriell proxy i ESPHome. Använd i stället ESPHomes Z-Wave-proxy.

## `component::engie_be::device::business_agreement::name`

**Engelska:** Business agreement {ban}

**Tidigare svenska:** (tom)

**Sparad svenska:** Företagsavtal {ban}

## `component::aurora_abb_powerone::exceptions::no_response::message`

**Engelska:** No response from the inverter, it may be dark

**Tidigare svenska:** (tom)

**Sparad svenska:** Inget svar från växelriktaren. Det kan vara mörkt.

## `component::sftp_storage::exceptions::sftp_session_failed::message`

**Engelska:** Cannot open an SFTP session on {host}

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att öppna en SFTP-session på {host}

## `component::sftp_storage::exceptions::list_failed::message`

**Engelska:** Failed to list backups

**Tidigare svenska:** (tom)

**Sparad svenska:** Det gick inte att lista säkerhetskopiorna

## `component::sftp_storage::exceptions::invalid_auth::message`

**Engelska:** Authentication failed for {username}@{host}. Check the password or private key

**Tidigare svenska:** (tom)

**Sparad svenska:** Autentisering misslyckades för {username}@{host}. Kontrollera lösenordet eller den privata nyckeln

## `component::sftp_storage::exceptions::delete_failed::message`

**Engelska:** Failed to delete backup {backup_id}

**Tidigare svenska:** (tom)

**Sparad svenska:** Det gick inte att ta bort säkerhetskopian {backup_id}

## `component::sftp_storage::exceptions::cannot_connect::message`

**Engelska:** Cannot connect to the SSH server {host}

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att ansluta till SSH-servern {host}

## `component::sftp_storage::exceptions::backup_location_unavailable::message`

**Engelska:** Cannot open the backup location {backup_location} on {host}. Make sure the directory exists and the user can access it

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att öppna platsen för säkerhetskopior {backup_location} på {host}. Kontrollera att katalogen finns och att användaren har åtkomst till den

## `component::lg_thinq::exceptions::device_not_connected::message`

**Engelska:** Device is not connected to the LG ThinQ cloud

**Tidigare svenska:** (tom)

**Sparad svenska:** Enheten är inte ansluten till LG ThinQ-molnet

## `component::evohome::exceptions::api_server_error::message`

**Engelska:** The vendor's API returned a server error; try again later

**Tidigare svenska:** (tom)

**Sparad svenska:** Leverantörens API returnerade ett serverfel. Försök igen senare

## `component::evohome::exceptions::api_request_rejected::message`

**Engelska:** The vendor's API rejected the request

**Tidigare svenska:** (tom)

**Sparad svenska:** Leverantörens API avvisade begäran

## `component::evohome::exceptions::api_request_failed::message`

**Engelska:** The request to the vendor's API failed

**Tidigare svenska:** (tom)

**Sparad svenska:** Begäran till leverantörens API misslyckades

## `component::evohome::exceptions::api_rate_limited::message`

**Engelska:** The vendor's API rate limit has been exceeded; try again later

**Tidigare svenska:** (tom)

**Sparad svenska:** Hastighetsgränsen för leverantörens API har överskridits. Försök igen senare

## `component::evohome::exceptions::api_connection_failed::message`

**Engelska:** Unable to connect to the vendor's API

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att ansluta till leverantörens API

## `component::nad_infrared::exceptions::invalid_source::message`

**Engelska:** Cannot select input source {invalid_source}. Valid sources: {valid_sources}.

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att välja ingångskällan {invalid_source}. Giltiga källor: {valid_sources}.

## `component::nad_infrared::exceptions::invalid_sound_mode::message`

**Engelska:** Cannot select sound mode {invalid_sound_mode}. Valid sound modes: {valid_sound_modes}.

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att välja ljudläget {invalid_sound_mode}. Giltiga ljudlägen: {valid_sound_modes}.

## `component::nad_infrared::exceptions::emitter_not_found::message`

**Engelska:** The infrared emitter used by this NAD device no longer exists. Remove this device and set it up again with another emitter.

**Tidigare svenska:** (tom)

**Sparad svenska:** Den infraröda sändaren som används av den här NAD-enheten finns inte längre. Ta bort enheten och konfigurera den igen med en annan sändare.

