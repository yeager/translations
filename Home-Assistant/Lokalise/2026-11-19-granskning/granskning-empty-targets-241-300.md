# Home Assistant Core: tidigare tomma svenska mål 241–300

- Granskade och sparade: **60/60**. Aktuell Core-revision `86a2eabe7e43f526db5821ef068087ce8404ae07`; engelsk källtext och svensk måltext verifierades live i Lokalise.
- 8 unika referensmål kontrollerades; inga avvikelser. Pluraliserade och formaterade värden behåller samtliga platshållare.
- `svlang skrivregler`: inga fel. Hunspell-träffar för tekniska termer, länkar och egennamn bedömdes i sammanhanget. Luckan för den böjda formen `API-tokenen` rättades i hunspell-sv; båda ordböckerna och regressionstesterna verifierades (19 tester passerar).
- Google Maps använder HTTP Referer/webbplatsbegränsningar; källans HTTP-referrer återges som `HTTP-referer` ([Google Maps API security guidance](https://developers.google.com/maps/api-security-best-practices)).
- Supervisor-varningen bevarar inline-kod, radbrytning, markdown-länkar och länkplatshållare.
- Hue BLE-värden är effektetiketter. Deskriptiva namn har lokaliserats; `Opal` behålls eftersom det fungerar som namn och svensk term. Hue anger dessa som effekt-namn ([Philips Hue release notes](https://www.philips-hue.com/en-gb/support/release-notes/lamps)).
- Home Assistant-TMX: 17 427 poster, validerad. Manifest och levande referensunderlag: `../Lokalise/2026-11-25-reviewed-empty-targets-241-300.json` och `../Lokalise/2026-11-25-reference-targets-empty-241-300-live.json`.

## Radgranskning

### `component::google_health::entity::sensor::oxygen_saturation::name`
- Källa: Oxygen saturation
- Föreslagen och sparad svenska: Syremättnad
- Motivering: Google Health measurement label.
- Status: sparad och återläst i Lokalise.

### `component::google_health::entity::sensor::respiratory_rate::name`
- Källa: Respiratory rate
- Föreslagen och sparad svenska: Andningsfrekvens
- Motivering: Google Health measurement label.
- Status: sparad och återläst i Lokalise.

### `component::google_health::entity::sensor::vo2_max::name`
- Källa: VO2 max
- Föreslagen och sparad svenska: VO2 max
- Motivering: Google Health measurement label.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::error::invalid_referrer`
- Källa: The HTTP referrer is not allowed for this API key. Check the website application restrictions of the API key.
- Föreslagen och sparad svenska: HTTP-referern är inte tillåten för den här API-nyckeln. Kontrollera webbplatsbegränsningarna för API-nyckeln.
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::step::reconfigure::sections::api_key_options::data::referrer`
- Källa: HTTP referrer
- Föreslagen och sparad svenska: HTTP-referer
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::step::reconfigure::sections::api_key_options::data_description::referrer`
- Källa: Specify this only if the API key has a [website application restriction]({restricting_api_keys_url})
- Föreslagen och sparad svenska: Ange bara detta om API-nyckeln har en [webbplatsbegränsning]({restricting_api_keys_url})
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::step::reconfigure::sections::api_key_options::name`
- Källa: Optional API key options
- Föreslagen och sparad svenska: Valfria API-nyckelinställningar
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::step::user::sections::api_key_options::data::referrer`
- Källa: HTTP referrer
- Föreslagen och sparad svenska: HTTP-referer
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::step::user::sections::api_key_options::data_description::referrer`
- Källa: Specify this only if the API key has a [website application restriction]({restricting_api_keys_url})
- Föreslagen och sparad svenska: Ange bara detta om API-nyckeln har en [webbplatsbegränsning]({restricting_api_keys_url})
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::google_travel_time::config::step::user::sections::api_key_options::name`
- Källa: Optional API key options
- Föreslagen och sparad svenska: Valfria API-nyckelinställningar
- Motivering: Google Maps API-key website restrictions; HTTP-referer is the technical HTTP header term.
- Status: sparad och återläst i Lokalise.

### `component::hassio::issues::issue_core_deprecated_tcp_api_request::description`
- Källa: Something in Home Assistant is calling the Supervisor API with the `{supervisor_token}` token, for example a request to `{reference}`.

This usually comes from a [Command line]({command_line_url}) or [Shell command]({shell_command_url}) configuration, or from a custom integration. Select Learn more to find out how to find and update it.
- Föreslagen och sparad svenska: Något i Home Assistant anropar Supervisor API med tokenen `{supervisor_token}`, till exempel med en begäran till `{reference}`.

Det här kommer vanligtvis från en konfiguration för [Kommandorad]({command_line_url}) eller [Skalkommando]({shell_command_url}), eller från en anpassad integration. Välj Läs mer för att ta reda på hur du hittar och uppdaterar den.
- Motivering: Supervisor API migration notice. Inline code formatting, line break, Markdown links and link placeholders match source exactly; established Swedish labels Kommandorad and Skalkommando used.
- Status: sparad och återläst i Lokalise.

### `component::hassio::issues::issue_core_deprecated_tcp_api_request::title`
- Källa: Deprecated use of the Supervisor API token
- Föreslagen och sparad svenska: Föråldrad användning av Supervisor API-tokenen
- Motivering: Supervisor API migration warning; Markdown links, quotation marks and placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::hikvision::config::step::user::data::verify_ssl`
- Källa: Verify SSL certificate
- Föreslagen och sparad svenska: Verifiera SSL-certifikat
- Motivering: Hikvision SSL certificate setup and self-signed certificate behavior.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::hikvision::config::step::user::data_description::verify_ssl`
- Källa: Disable if your device uses a self-signed certificate, which is what Hikvision devices ship with. Only applies when SSL is used
- Föreslagen och sparad svenska: Inaktivera det här om enheten använder ett självsignerat certifikat, vilket medföljer Hikvision-enheter. Gäller endast när SSL används.
- Motivering: Hikvision SSL certificate setup and self-signed certificate behavior.
- Status: sparad och återläst i Lokalise.

### `component::hr_energy_qube::entity::sensor::working_hours_cooling::name`
- Källa: Working hours cooling
- Föreslagen och sparad svenska: Drifttimmar för kylning
- Motivering: Operating-hour counters for heating, cooling, hot water and heater units.
- Status: sparad och återläst i Lokalise.

### `component::hr_energy_qube::entity::sensor::working_hours_dhw::name`
- Källa: Working hours DHW
- Föreslagen och sparad svenska: Drifttimmar för tappvarmvatten
- Motivering: Operating-hour counters for heating, cooling, hot water and heater units.
- Status: sparad och återläst i Lokalise.

### `component::hr_energy_qube::entity::sensor::working_hours_heater::name`
- Källa: Working hours heater {number}
- Föreslagen och sparad svenska: Drifttimmar för värmare {number}
- Motivering: Operating-hour counters for heating, cooling, hot water and heater units.
- Status: sparad och återläst i Lokalise.

### `component::hr_energy_qube::entity::sensor::working_hours_heating::name`
- Källa: Working hours heating
- Föreslagen och sparad svenska: Drifttimmar för uppvärmning
- Motivering: Operating-hour counters for heating, cooling, hot water and heater units.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::candle`
- Källa: Candle
- Föreslagen och sparad svenska: Levande ljus
- Motivering: Philips Hue named light effect localized as a concise descriptive label.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::cosmos`
- Källa: Cosmos
- Föreslagen och sparad svenska: Kosmos
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::enchant`
- Källa: Enchant
- Föreslagen och sparad svenska: Förtrollning
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::fireplace`
- Källa: Fireplace
- Föreslagen och sparad svenska: Eldstad
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::glisten`
- Källa: Glisten
- Föreslagen och sparad svenska: Glimrande
- Motivering: Philips Hue named light effect localized as a concise descriptive label.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::opal`
- Källa: Opal
- Föreslagen och sparad svenska: Opal
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::prism`
- Källa: Prism
- Föreslagen och sparad svenska: Prisma
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sparkle`
- Källa: Sparkle
- Föreslagen och sparad svenska: Gnistrande
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sunbeam`
- Källa: Sunbeam
- Föreslagen och sparad svenska: Solstråle
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sunrise`
- Källa: Sunrise
- Föreslagen och sparad svenska: Soluppgång
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::sunset`
- Källa: Sunset
- Föreslagen och sparad svenska: Solnedgång
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::hue_ble::entity::light::hue_ble_light::state_attributes::effect::state::underwater`
- Källa: Underwater
- Föreslagen och sparad svenska: Under vatten
- Motivering: Philips Hue effect labels localized as descriptive effect names; branded names retain standard Swedish spellings where appropriate.
- Status: sparad och återläst i Lokalise.

### `component::huisbaasje::config::abort::wrong_account`
- Källa: The credentials belong to a different EnergyFlip account than the one configured.
- Föreslagen och sparad svenska: Inloggningsuppgifterna tillhör ett annat EnergyFlip-konto än det som har konfigurerats.
- Motivering: EnergyFlip account reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::huisbaasje::config::step::reauth_confirm::data::password`
- Källa: Password
- Föreslagen och sparad svenska: Lösenord
- Motivering: EnergyFlip account reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::huisbaasje::config::step::reauth_confirm::data_description::password`
- Källa: The current password of your EnergyFlip account.
- Föreslagen och sparad svenska: Det aktuella lösenordet till ditt EnergyFlip-konto.
- Motivering: EnergyFlip account reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::huisbaasje::config::step::reauth_confirm::description`
- Källa: The password for {username} is no longer valid. Enter the current password.
- Föreslagen och sparad svenska: Lösenordet för {username} är inte längre giltigt. Ange det aktuella lösenordet.
- Motivering: EnergyFlip account reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::huisbaasje::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: EnergyFlip account reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::intesis_modbus::device::air_conditioner::name`
- Källa: {gateway} air conditioner
- Föreslagen och sparad svenska: Luftkonditionering via {gateway}
- Motivering: Intesis Modbus air-conditioning gateway and response status.
- Status: sparad och återläst i Lokalise.

### `component::intesis_modbus::exceptions::gateway_unavailable::message`
- Källa: The gateway does not answer.
- Föreslagen och sparad svenska: Gatewayen svarar inte.
- Motivering: Intesis Modbus air-conditioning gateway and response status.
- Status: sparad och återläst i Lokalise.

### `component::knx::config_panel::entities::create::_::knx::knx_group_address::used_by`
- Källa: Used by
- Föreslagen och sparad svenska: Används av
- Motivering: KNX group-address usage and xknxproject compatibility errors.
- Status: sparad och återläst i Lokalise.

### `component::knx::exceptions::project_data_incompatible::message`
- Källa: The KNX project data is for xknxproject {version}, which is not compatible with the installed xknxproject {installed_version}.
- Föreslagen och sparad svenska: KNX-projektdata gäller xknxproject {version}, som inte är kompatibelt med den installerade versionen ({installed_version}).
- Motivering: KNX group-address usage and xknxproject compatibility errors.
- Status: sparad och återläst i Lokalise.

### `component::knx::exceptions::project_data_invalid::message`
- Källa: Invalid KNX project data: {error}
- Föreslagen och sparad svenska: Ogiltiga KNX-projektdata: {error}
- Motivering: KNX group-address usage and xknxproject compatibility errors.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::abort::auth_failed`
- Källa: Last.fm authorization failed. Start authorization again to request a new token.
- Föreslagen och sparad svenska: Auktoriseringen för Last.fm misslyckades. Starta auktoriseringen igen för att begära en ny token.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::abort::configuration_changed`
- Källa: The Last.fm configuration changed. Start again to use the current settings.
- Föreslagen och sparad svenska: Last.fm-konfigurationen har ändrats. Starta om för att använda de aktuella inställningarna.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::abort::wrong_account`
- Källa: The authorized Last.fm account ({authorized_user}) does not match the configured account ({configured_user}). Start authorization again and use the configured account.
- Föreslagen och sparad svenska: Det auktoriserade Last.fm-kontot ({authorized_user}) matchar inte det konfigurerade kontot ({configured_user}). Starta auktoriseringen igen och använd det konfigurerade kontot.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::error::api_secret_required`
- Källa: Enter the API secret that matches the API key to enable authenticated access.
- Föreslagen och sparad svenska: Ange API-hemligheten som hör till API-nyckeln för att aktivera autentiserad åtkomst.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::error::cannot_connect`
- Källa: Failed to connect
- Föreslagen och sparad svenska: Det gick inte att ansluta
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::auth_url::description`
- Källa: Select the link below to open Last.fm and authorize Home Assistant with your account, then return here and select Submit. Setup may continue automatically once the authorization is detected.
- Föreslagen och sparad svenska: Välj länken nedan för att öppna Last.fm och auktorisera Home Assistant för ditt konto. Gå sedan tillbaka hit och välj Skicka. Konfigurationen kan fortsätta automatiskt när auktoriseringen har upptäckts.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::auth_url::title`
- Källa: Authorize Home Assistant with Last.fm
- Föreslagen och sparad svenska: Auktorisera Home Assistant med Last.fm
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reauth_confirm::description`
- Källa: Your Last.fm account needs to be authorized again. Select Submit to start authorization.
- Föreslagen och sparad svenska: Ditt Last.fm-konto måste auktoriseras igen. Välj Skicka för att starta auktoriseringen.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reauth_confirm::title`
- Källa: Reconnect to Last.fm
- Föreslagen och sparad svenska: Återanslut till Last.fm
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data::api_key`
- Källa: API key
- Föreslagen och sparad svenska: API-nyckel
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data::api_secret`
- Källa: API secret
- Föreslagen och sparad svenska: API-hemlighet
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data::enable_authentication`
- Källa: Enable authenticated access
- Föreslagen och sparad svenska: Aktivera autentiserad åtkomst
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data::main_user`
- Källa: Last.fm username
- Föreslagen och sparad svenska: Last.fm-användarnamn
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data_description::api_secret`
- Källa: When authenticated access is enabled, leave blank to keep the existing secret. When changing the API key, enter its matching secret.
- Föreslagen och sparad svenska: När autentiserad åtkomst är aktiverad lämnar du fältet tomt för att behålla den befintliga hemligheten. Om du byter API-nyckel anger du den tillhörande hemligheten.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data_description::enable_authentication`
- Källa: Allows access to your own hidden listening information. Disabling this removes the saved authentication credentials; hidden listening information will no longer be accessible.
- Föreslagen och sparad svenska: Ger åtkomst till din egen dolda lyssningsinformation. Om du inaktiverar detta tas de sparade autentiseringsuppgifterna bort och du får inte längre åtkomst till den dolda lyssningsinformationen.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::data_description::main_user`
- Källa: Select the Last.fm account to authorize.
- Föreslagen och sparad svenska: Välj det Last.fm-konto som ska auktoriseras.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::reconfigure::description`
- Källa: Update the API credentials for this integration. Request an API account at {api_account_url}.
- Föreslagen och sparad svenska: Uppdatera API-inloggningsuppgifterna för den här integrationen. Begär ett API-konto på {api_account_url}.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::user::data::api_secret`
- Källa: API secret
- Föreslagen och sparad svenska: API-hemlighet
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::config::step::user::data_description::api_secret`
- Källa: Optional. Lets the integration read listening information hidden by the user's Last.fm privacy settings.
- Föreslagen och sparad svenska: Valfritt. Låter integrationen läsa lyssningsinformation som döljs av användarens sekretessinställningar på Last.fm.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Status: sparad och återläst i Lokalise.

### `component::lastfm::options::abort::configuration_changed`
- Källa: The Last.fm configuration changed. Start again to use the current settings.
- Föreslagen och sparad svenska: Last.fm-konfigurationen har ändrats. Starta om för att använda de aktuella inställningarna.
- Motivering: Last.fm authorization, API credentials and privacy-controlled listening information.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

## Kvarvarande arbete

Granskningen fortsätter. Kvarvarande tomma mål och saknade Core-nycklar inventeras separat; inga andra poster markeras som klara.
