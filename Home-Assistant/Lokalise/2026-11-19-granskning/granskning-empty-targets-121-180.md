# Home Assistant Core: tidigare tomma svenska mål 121–180

- Granskade och sparade: **60/60**. Källor kontrollerade mot Home Assistant Core `86a2eabe7e43f526db5821ef068087ce8404ae07`; aktuella Lokalise-källor och mål återlästes live.
- 11 unika levande referensmål kontrollerades; inga referensavvikelser efter sparning.
- Tre molnfeltexter korrigerades efter manuell teknisk genomgång och återlästes.
- `svlang skrivregler`: inga fel. Hunspell-flaggor för produktnamn, tekniska ord och platshållare bedömdes; alla 60 platshållaruppsättningar matchar exakt.
- Home Assistant-TMX: 17 307 poster, validerad. Manifest och live-referenser: `../Lokalise/2026-11-25-reviewed-empty-targets-121-180.json`, `../Lokalise/2026-11-25-reference-targets-empty-121-180-live.json`.

## Radgranskning

### `component::benq_projector_infrared::exceptions::cooling_down::message`
- Källa: The projector is cooling down and does not accept commands for another {seconds} seconds.
- Föreslagen och sparad svenska: Projektorn svalnar och tar inte emot kommandon på ytterligare {seconds} sekunder.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::exceptions::emitter_not_found::message`
- Källa: The infrared emitter used by this BenQ projector no longer exists. Remove this device and set it up again with another emitter.
- Föreslagen och sparad svenska: Den infraröda sändare som används av den här BenQ-projektorn finns inte längre. Ta bort enheten och konfigurera den igen med en annan sändare.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::exceptions::invalid_source::message`
- Källa: Cannot select input source {invalid_source}. Valid sources: {valid_sources}.
- Föreslagen och sparad svenska: Det går inte att välja ingångskällan {invalid_source}. Giltiga ingångskällor: {valid_sources}.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::exceptions::receiver_not_found::message`
- Källa: The infrared receiver used by this BenQ projector no longer exists. Remove this device and set it up again with another receiver.
- Föreslagen och sparad svenska: Den infraröda mottagare som används av den här BenQ-projektorn finns inte längre. Ta bort enheten och konfigurera den igen med en annan mottagare.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::exceptions::warming_up::message`
- Källa: The projector is warming up and does not accept commands for another {seconds} seconds.
- Föreslagen och sparad svenska: Projektorn värms upp och tar inte emot kommandon på ytterligare {seconds} sekunder.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::options::step::init::data::cool_down_time`
- Källa: Cool-down time
- Föreslagen och sparad svenska: Avsvalningstid
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::options::step::init::data::warm_up_time`
- Källa: Warm-up time
- Föreslagen och sparad svenska: Uppvärmningstid
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::options::step::init::data_description::cool_down_time`
- Källa: How long the projector ignores commands after it is turned off. Commands sent during this time are refused.
- Föreslagen och sparad svenska: Hur länge projektorn ignorerar kommandon efter att den har stängts av. Kommandon som skickas under den här tiden avvisas.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::benq_projector_infrared::options::step::init::data_description::warm_up_time`
- Källa: How long the projector ignores commands after it is turned on. Commands sent during this time are refused.
- Föreslagen och sparad svenska: Hur länge projektorn ignorerar kommandon efter att den har satts på. Kommandon som skickas under den här tiden avvisas.
- Motivering: BenQ projector state and configuration; warm-up/cool-down periods and input-source placeholders preserved.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::binary_sensor::siren_ac_dc_error::name`
- Källa: AC/DC error
- Föreslagen och sparad svenska: AC/DC-fel
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::binary_sensor::siren_battery_defect::name`
- Källa: Battery defect
- Föreslagen och sparad svenska: Batterifel
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::binary_sensor::siren_battery_temperature_abnormal::name`
- Källa: Battery temperature abnormal
- Föreslagen och sparad svenska: Avvikande batteritemperatur
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::binary_sensor::siren_primary_power_supply_outage::name`
- Källa: Primary power supply outage
- Föreslagen och sparad svenska: Avbrott i den primära strömförsörjningen
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::button::preview_max_brightness::name`
- Källa: Preview max brightness
- Föreslagen och sparad svenska: Förhandsgranska maximal ljusstyrka
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::button::preview_min_brightness::name`
- Källa: Preview min brightness
- Föreslagen och sparad svenska: Förhandsgranska minimal ljusstyrka
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::button::reset_energy_summation::name`
- Källa: Reset consumption value
- Föreslagen och sparad svenska: Återställ förbrukningsvärde
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::number::comfort_temperature::name`
- Källa: Comfort temperature
- Föreslagen och sparad svenska: Komforttemperatur
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::number::eco_temperature::name`
- Källa: Eco temperature
- Föreslagen och sparad svenska: Ekotemperatur
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::entity::update::controller_update::name`
- Källa: Software update
- Föreslagen och sparad svenska: Programvaruuppdatering
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::exceptions::update_install_failed::message`
- Källa: Failed to start the firmware update on {name}
- Föreslagen och sparad svenska: Det gick inte att starta uppdateringen av den fasta programvaran på {name}
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_shc::exceptions::update_not_ready::message`
- Källa: Firmware update for {name} cannot be activated right now (current state: {state}).
- Föreslagen och sparad svenska: Det går inte att aktivera uppdateringen av den fasta programvaran för {name} just nu (aktuellt läge: {state}).
- Motivering: Bosch SHC siren sensors, brightness controls, energy reset, temperatures and firmware updates.
- Status: sparad och återläst i Lokalise.

### `component::bosch_smart_camera::entity::light::camera_light::name`
- Källa: Camera light
- Föreslagen och sparad svenska: Kamerabelysning
- Motivering: Bosch smart-camera light control and Wi-Fi signal context.
- Status: sparad och återläst i Lokalise.

### `component::bosch_smart_camera::entity::sensor::wifi_signal_strength::name`
- Källa: Wi-Fi signal strength
- Föreslagen och sparad svenska: Wi-Fi-signalstyrka
- Motivering: Bosch smart-camera light control and Wi-Fi signal context.
- Status: sparad och återläst i Lokalise.

### `component::bosch_smart_camera::exceptions::light_failed::message`
- Källa: Unable to switch the camera light.
- Föreslagen och sparad svenska: Det gick inte att ändra kamerans belysning.
- Motivering: Bosch smart-camera light control and Wi-Fi signal context.
- Status: sparad och återläst i Lokalise.

### `component::cloud::issues::remote_client_certificate_error::description`
- Källa: Remote access through Home Assistant Link is off because the client certificate authority file ({ca_file}) could not be loaded. Fix the file or update the SSL peer certificate in the network settings, then restart Home Assistant.
- Föreslagen och sparad svenska: Fjärråtkomst via Home Assistant Link är avstängd eftersom certifikatutfärdarfilen för klientcertifikatet ({ca_file}) inte kunde läsas in. Åtgärda filen eller uppdatera motpartens SSL-certifikat i nätverksinställningarna och starta sedan om Home Assistant.
- Motivering: Home Assistant Link remote access and client certificate authority-file issue; filename placeholder preserved. Manual precision edit: distinguish certificate authority file, peer SSL certificate and required client certificate.
- Status: sparad och återläst i Lokalise.

### `component::cloud::issues::remote_client_certificate_error::title`
- Källa: Remote access client certificate authority could not be loaded
- Föreslagen och sparad svenska: Det gick inte att läsa in certifikatutfärdarfilen för klientcertifikatet för fjärråtkomst
- Motivering: Home Assistant Link remote access and client certificate authority-file issue; filename placeholder preserved. Manual precision edit: distinguish certificate authority file, peer SSL certificate and required client certificate.
- Status: sparad och återläst i Lokalise.

### `component::cloud::system_health::info::remote_client_certificate_required`
- Källa: Remote client certificate required
- Föreslagen och sparad svenska: Klientcertifikat för fjärråtkomst krävs
- Motivering: Home Assistant Link remote access and client certificate authority-file issue; filename placeholder preserved. Manual precision edit: distinguish certificate authority file, peer SSL certificate and required client certificate.
- Status: sparad och återläst i Lokalise.

### `component::control4::config::abort::wrong_account`
- Källa: The new credentials belong to a different Control4 controller
- Föreslagen och sparad svenska: De nya inloggningsuppgifterna tillhör en annan Control4-styrenhet
- Motivering: Control4 account reauthentication and controller identity context.
- Status: sparad och återläst i Lokalise.

### `component::control4::config::step::reauth_confirm::data::password`
- Källa: Password
- Föreslagen och sparad svenska: Lösenord
- Motivering: Control4 account reauthentication and controller identity context.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::control4::config::step::reauth_confirm::data_description::password`
- Källa: The password of your Control4 account.
- Föreslagen och sparad svenska: Lösenordet till ditt Control4-konto.
- Motivering: Control4 account reauthentication and controller identity context.
- Status: sparad och återläst i Lokalise.

### `component::control4::config::step::reauth_confirm::description`
- Källa: Enter the new password for the Control4 account {username}.
- Föreslagen och sparad svenska: Ange det nya lösenordet till Control4-kontot {username}.
- Motivering: Control4 account reauthentication and controller identity context.
- Status: sparad och återläst i Lokalise.

### `component::control4::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: Control4 account reauthentication and controller identity context.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::abort::already_configured`
- Källa: Device is already configured
- Föreslagen och sparad svenska: Enheten är redan konfigurerad
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::abort::no_infrared_emitters`
- Källa: No infrared emitter entities found. Please set up an infrared device first.
- Föreslagen och sparad svenska: Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet.
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::step::user::data::infrared_emitter_entity_id`
- Källa: Infrared emitter
- Föreslagen och sparad svenska: Infraröd sändare
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::step::user::data::infrared_receiver_entity_id`
- Källa: Infrared receiver
- Föreslagen och sparad svenska: Infraröd mottagare
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::step::user::data_description::infrared_emitter_entity_id`
- Källa: The infrared emitter entity to use for sending commands.
- Föreslagen och sparad svenska: Sändarentiteten som ska användas för att skicka infraröda kommandon.
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::step::user::data_description::infrared_receiver_entity_id`
- Källa: Optional — allows the integration to update state when the physical remote is used.
- Föreslagen och sparad svenska: Valfritt – gör att integrationen kan uppdatera status när den fysiska fjärrkontrollen används.
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::step::user::description`
- Källa: Select an infrared emitter for your Daikin AC.
- Föreslagen och sparad svenska: Välj en infraröd sändare till din Daikin-luftkonditionering.
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::config::step::user::title`
- Källa: Set up Daikin AC
- Föreslagen och sparad svenska: Konfigurera Daikin-luftkonditionering
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Status: sparad och återläst i Lokalise.

### `component::daikin_infrared::entity::climate::daikin_ac::state_attributes::fan_mode::state::silence`
- Källa: Silence
- Föreslagen och sparad svenska: Tyst
- Motivering: Daikin air-conditioning infrared setup; shared infrared terms follow live HA reference targets.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::abort::wrong_device`
- Källa: The credentials belong to a different Ecoforest device than the one this entry is set up for.
- Föreslagen och sparad svenska: Inloggningsuppgifterna tillhör en annan Ecoforest-enhet än den som den här konfigurationen har ställts in för.
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::reauth_confirm::data::password`
- Källa: Password
- Föreslagen och sparad svenska: Lösenord
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::reauth_confirm::data::username`
- Källa: Username
- Föreslagen och sparad svenska: Användarnamn
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::reauth_confirm::data_description::password`
- Källa: The password of your Ecoforest device.
- Föreslagen och sparad svenska: Lösenordet till din Ecoforest-enhet.
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::reauth_confirm::data_description::username`
- Källa: The username of your Ecoforest device.
- Föreslagen och sparad svenska: Användarnamnet till din Ecoforest-enhet.
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::reauth_confirm::description`
- Källa: Authentication on the Ecoforest device at {host} failed. Enter the credentials again.
- Föreslagen och sparad svenska: Autentiseringen på Ecoforest-enheten på {host} misslyckades. Ange inloggningsuppgifterna igen.
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::user::data_description::password`
- Källa: The password of your Ecoforest device.
- Föreslagen och sparad svenska: Lösenordet till din Ecoforest-enhet.
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Status: sparad och återläst i Lokalise.

### `component::ecoforest::config::step::user::data_description::username`
- Källa: The username of your Ecoforest device.
- Föreslagen och sparad svenska: Användarnamnet till din Ecoforest-enhet.
- Motivering: Ecoforest device credentials and reauthentication; referenced user-form descriptions are populated in this batch.
- Status: sparad och återläst i Lokalise.

### `component::elkm1::config::step::reauth_confirm::data::password`
- Källa: Password
- Föreslagen och sparad svenska: Lösenord
- Motivering: Elk-M1 alarm panel credentials and reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::elkm1::config::step::reauth_confirm::data::username`
- Källa: Username
- Föreslagen och sparad svenska: Användarnamn
- Motivering: Elk-M1 alarm panel credentials and reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::elkm1::config::step::reauth_confirm::data_description::password`
- Källa: The password of the Elk-M1 user.
- Föreslagen och sparad svenska: Lösenordet för Elk-M1-användaren.
- Motivering: Elk-M1 alarm panel credentials and reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::elkm1::config::step::reauth_confirm::data_description::username`
- Källa: The name of the Elk-M1 user.
- Föreslagen och sparad svenska: Namnet på Elk-M1-användaren.
- Motivering: Elk-M1 alarm panel credentials and reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::elkm1::config::step::reauth_confirm::description`
- Källa: The Elk-M1 panel rejected the credentials. Enter the current username and password.
- Föreslagen och sparad svenska: Elk-M1-centralapparaten avvisade inloggningsuppgifterna. Ange det aktuella användarnamnet och lösenordet.
- Motivering: Elk-M1 alarm panel credentials and reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::elkm1::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: Elk-M1 alarm panel credentials and reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::elvia::config::abort::wrong_account`
- Källa: The API token does not give access to the metering point of this entry.
- Föreslagen och sparad svenska: API-tokenen ger inte åtkomst till mätpunkten för den här konfigurationen.
- Motivering: Elvia meter-point access and API-token reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::elvia::config::step::reauth_confirm::data::api_token`
- Källa: API token
- Föreslagen och sparad svenska: API-token
- Motivering: Elvia meter-point access and API-token reauthentication.
- Källreferens verifierad mot levande Lokalise-mål; texten matchar referensmålet.
- Status: sparad och återläst i Lokalise.

### `component::elvia::config::step::reauth_confirm::data_description::api_token`
- Källa: The new meter value API token from Elvia.
- Föreslagen och sparad svenska: Den nya API-tokenen för mätvärden från Elvia.
- Motivering: Elvia meter-point access and API-token reauthentication.
- Status: sparad och återläst i Lokalise.

### `component::elvia::config::step::reauth_confirm::description`
- Källa: The Elvia API token is no longer valid. Enter a new one.
- Föreslagen och sparad svenska: Elvias API-token är inte längre giltig. Ange en ny.
- Motivering: Elvia meter-point access and API-token reauthentication.
- Status: sparad och återläst i Lokalise.

## Kvarvarande arbete

Core-granskningen fortsätter. Den fullständiga inventeringen uppdateras separat; inga strängar markeras som klara utanför den granskade omfattningen.
