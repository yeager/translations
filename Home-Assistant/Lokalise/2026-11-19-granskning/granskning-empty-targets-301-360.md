# Home Assistant Core: tidigare tomma svenska mål 301–360

- Granskade och sparade: **60/60**. Källor kontrollerade mot Core `86a2eabe7e43f526db5821ef068087ce8404ae07` och levande Lokalise; sparade svenska mål återlästa.
- 7 unika referensmål livekontrollerade; inga avvikelser. Alla platshållare matchar exakt.
- `svlang skrivregler`: inga fel. Hunspell-flaggor för egennamn, SSML, kodidentifierare och platshållare granskades manuellt.
- Delade titlar följer referensmålen. Microsoft-rösternas språk och regioner har översatts på svenska; `AUX` och tekniska Azure-/SSML-identifierare behålls.
- Home Assistant-TMX: 17 487 poster, validerad. Manifest och live-referenser: `../Lokalise/2026-11-25-reviewed-empty-targets-301-360.json`, `../Lokalise/2026-11-25-reference-targets-empty-301-360-live.json`.

## Radgranskning

### `component::lektrico::entity::switch::compatibility_mode::name`
**Källa:** Compatibility mode
**Svenska:** Kompatibilitetsläge
**Motivering:** Compatibility option in the LeKtrico integration.
**Status:** sparad och återläst i Lokalise.

### `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::aux_1`
**Källa:** Aux
**Svenska:** AUX
**Motivering:** Marantz receiver input and speaker-output controls; official input abbreviation AUX retained.
**Status:** sparad och återläst i Lokalise.

### `component::marantz_infrared::entity::media_player::receiver::state_attributes::source::state::aux_pm8006`
**Källa:** Aux
**Svenska:** AUX
**Motivering:** Marantz receiver input and speaker-output controls; official input abbreviation AUX retained.
**Status:** sparad och återläst i Lokalise.

### `component::marantz_infrared::entity::switch::power_amp_direct::name`
**Källa:** Power amp direct
**Svenska:** Direktläge för slutsteg
**Motivering:** Marantz receiver input and speaker-output controls; official input abbreviation AUX retained.
**Status:** sparad och återläst i Lokalise.

### `component::marantz_infrared::entity::switch::speaker_a::name`
**Källa:** Speaker A
**Svenska:** Högtalare A
**Motivering:** Marantz receiver input and speaker-output controls; official input abbreviation AUX retained.
**Status:** sparad och återläst i Lokalise.

### `component::marantz_infrared::entity::switch::speaker_b::name`
**Källa:** Speaker B
**Svenska:** Högtalare B
**Motivering:** Marantz receiver input and speaker-output controls; official input abbreviation AUX retained.
**Status:** sparad och återläst i Lokalise.

### `component::matter::entity::update::release_notes_messages::non_main_net_update_source`
**Källa:** Update provided by {update_source}. Installing this update is at your own risk and you may run into unexpected problems such as the need to re-add and factory reset your device.
**Svenska:** Uppdateringen tillhandahålls av {update_source}. Installera den på egen risk; oväntade problem kan uppstå, till exempel att du måste lägga till enheten igen och återställa den till fabriksinställningarna.
**Motivering:** Matter firmware-update source and duration warnings; update-source placeholder retained.
**Status:** sparad och återläst i Lokalise.

### `component::matter::entity::update::release_notes_messages::update_duration`
**Källa:** The update process can take a while, especially for battery powered devices. Please be patient and wait until the update process is fully completed. The device may restart during the update process and be unavailable for several minutes.
**Svenska:** Uppdateringsprocessen kan ta ett tag, särskilt för batteridrivna enheter. Vänta tills processen har slutförts helt. Enheten kan starta om under uppdateringen och vara otillgänglig i flera minuter.
**Motivering:** Matter firmware-update source and duration warnings; update-source placeholder retained.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::abort::already_configured`
**Källa:** Service is already configured
**Svenska:** Tjänsten är redan konfigurerad
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::error::cannot_connect`
**Källa:** Failed to connect
**Svenska:** Det gick inte att ansluta
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::error::invalid_api_key`
**Källa:** The API key was rejected. Check that the API key is valid and that the region matches your Azure Speech resource.
**Svenska:** API-nyckeln avvisades. Kontrollera att API-nyckeln är giltig och att regionen stämmer med din Azure Speech-resurs.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::error::unknown`
**Källa:** Unexpected error
**Svenska:** Oväntat fel
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data::api_key`
**Källa:** API key
**Svenska:** API-nyckel
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data::gender`
**Källa:** Gender
**Svenska:** Kön
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data::language`
**Källa:** Language
**Svenska:** Språk
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data::region`
**Källa:** Region
**Svenska:** Region
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data::type`
**Källa:** Voice
**Svenska:** Röst
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data_description::api_key`
**Källa:** A key of your Azure Speech resource.
**Svenska:** En nyckel till din Azure Speech-resurs.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data_description::gender`
**Källa:** The gender of the voice.
**Svenska:** Röstens kön.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data_description::language`
**Källa:** The default language of the speech.
**Svenska:** Standardspråket för talet.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data_description::region`
**Källa:** The location of your Azure Speech resource.
**Svenska:** Platsen där din Azure Speech-resurs finns.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::config::step::user::data_description::type`
**Källa:** The name of the voice without the language prefix, for example `JennyNeural`. The voice must be available for the selected language. You can find the available voices in the [Microsoft documentation]({voices_url}).
**Svenska:** Röstens namn utan språkprefix, till exempel `JennyNeural`. Rösten måste finnas tillgänglig för det valda språket. Du hittar tillgängliga röster i [Microsofts dokumentation]({voices_url}).
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::entity::tts::text_to_speech::name`
**Källa:** Text-to-speech
**Svenska:** Text-till-tal
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::exceptions::cannot_connect::message`
**Källa:** Could not connect to the Microsoft Text-to-Speech service.
**Svenska:** Det gick inte att ansluta till Microsofts text-till-tal-tjänst.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::exceptions::invalid_api_key::message`
**Källa:** The Microsoft Text-to-Speech service rejected the API key. Check that the API key is valid and that the region matches your Azure Speech resource.
**Svenska:** Microsofts text-till-tal-tjänst avvisade API-nyckeln. Kontrollera att API-nyckeln är giltig och att regionen stämmer med din Azure Speech-resurs.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::exceptions::synthesis_failed::message`
**Källa:** Microsoft Text-to-Speech failed to synthesize the speech.
**Svenska:** Microsofts text-till-tal-tjänst kunde inte syntetisera talet.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml::description`
**Källa:**

```text
Configuring {integration_title} using YAML is being removed.

Your existing YAML configuration has been imported into the UI automatically. The legacy `tts.{domain}_say` action (or the name you set with `service_name`) and the legacy `{domain}` text-to-speech engine keep working until you remove the YAML configuration. To fix this issue:

1. Update your automations and scripts to use the `tts.speak` action with the new text-to-speech entity.
2. Under **Settings** > **Voice assistants**, select the new text-to-speech entity in every assistant that uses the legacy `{domain}` engine.
3. Remove the `{domain}` platform from the `tts` section of your configuration.yaml file and restart Home Assistant.
```
**Svenska:**

```text
Konfiguration av {integration_title} via YAML tas bort.

Din befintliga YAML-konfiguration har importerats automatiskt till användargränssnittet. Den äldre åtgärden `tts.{domain}_say` (eller namnet du har angett i `service_name`) och den äldre text-till-tal-motorn `{domain}` fortsätter att fungera tills du tar bort YAML-konfigurationen. Så här åtgärdar du problemet:

1. Uppdatera dina automatiseringar och skript så att de använder åtgärden `tts.speak` med den nya text-till-tal-entiteten.
2. Gå till **Inställningar** > **Röstassistenter** och välj den nya text-till-tal-entiteten för varje assistent som använder den äldre motorn `{domain}`.
3. Ta bort plattformen `{domain}` från avsnittet `tts` i filen configuration.yaml och starta om Home Assistant.
```
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml::title`
**Källa:** The {integration_title} YAML configuration is being removed
**Svenska:** YAML-konfigurationen för {integration_title} tas bort
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml_import_issue_cannot_connect::description`
**Källa:**

```text
Configuring {integration_title} using YAML is being removed, but your YAML configuration could not be imported because Home Assistant could not connect to the Microsoft Text-to-Speech service.

Check the region in your YAML configuration and restart Home Assistant to try again, or remove the `{domain}` platform from the `tts` section of your configuration.yaml file and set up the integration in the UI.
```
**Svenska:**

```text
Konfiguration av {integration_title} via YAML tas bort, men YAML-konfigurationen kunde inte importeras eftersom Home Assistant inte kunde ansluta till Microsofts text-till-tal-tjänst.

Kontrollera regionen i YAML-konfigurationen och starta om Home Assistant för att försöka igen. Du kan också ta bort plattformen `{domain}` från avsnittet `tts` i filen configuration.yaml och konfigurera integrationen i användargränssnittet.
```
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml_import_issue_cannot_connect::title`
**Källa:** The {integration_title} YAML configuration import failed
**Svenska:** Det gick inte att importera YAML-konfigurationen för {integration_title}
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml_import_issue_invalid_api_key::description`
**Källa:**

```text
Configuring {integration_title} using YAML is being removed, but your YAML configuration could not be imported because the API key was rejected.

Check the API key and region in your YAML configuration and restart Home Assistant to try again, or remove the `{domain}` platform from the `tts` section of your configuration.yaml file and set up the integration in the UI.
```
**Svenska:**

```text
Konfiguration av {integration_title} via YAML tas bort, men YAML-konfigurationen kunde inte importeras eftersom API-nyckeln avvisades.

Kontrollera API-nyckeln och regionen i YAML-konfigurationen och starta om Home Assistant för att försöka igen. Du kan också ta bort plattformen `{domain}` från avsnittet `tts` i filen configuration.yaml och konfigurera integrationen i användargränssnittet.
```
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml_import_issue_invalid_api_key::title`
**Källa:** The {integration_title} YAML configuration import failed
**Svenska:** Det gick inte att importera YAML-konfigurationen för {integration_title}
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml_import_issue_unknown::description`
**Källa:**

```text
Configuring {integration_title} using YAML is being removed, but your YAML configuration could not be imported because of an unexpected error. Check the logs for details.

Remove the `{domain}` platform from the `tts` section of your configuration.yaml file and set up the integration in the UI.
```
**Svenska:**

```text
Konfiguration av {integration_title} via YAML tas bort, men YAML-konfigurationen kunde inte importeras på grund av ett oväntat fel. Kontrollera loggarna för mer information.

Ta bort plattformen `{domain}` från avsnittet `tts` i filen configuration.yaml och konfigurera integrationen i användargränssnittet.
```
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::issues::deprecated_yaml_import_issue_unknown::title`
**Källa:** The {integration_title} YAML configuration import failed
**Svenska:** Det gick inte att importera YAML-konfigurationen för {integration_title}
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Referens:** livekällan och svenska måltexten matchar.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data::contour`
**Källa:** Pitch contour
**Svenska:** Tonhöjdskontur
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data::pitch`
**Källa:** Pitch
**Svenska:** Tonhöjd
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data::rate`
**Källa:** Speaking rate
**Svenska:** Talhastighet
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data::volume`
**Källa:** Volume
**Svenska:** Volym
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data_description::contour`
**Källa:** Changes of the pitch over the course of the speech, in SSML `contour` format. Leave empty to not change the pitch contour.
**Svenska:** Ändringar i tonhöjden under talets gång, i SSML-formatet `contour`. Lämna fältet tomt om tonhöjdskonturen inte ska ändras.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data_description::pitch`
**Källa:** The pitch of the voice, for example `default`, `high` or `+10%`.
**Svenska:** Röstens tonhöjd, till exempel `default`, `high` eller `+10%`.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data_description::rate`
**Källa:** Speed up or slow down the speech.
**Svenska:** Snabba upp eller sakta ned talet.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::options::step::init::data_description::volume`
**Källa:** Raise or lower the volume of the speech.
**Svenska:** Höj eller sänk talvolymen.
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::gender::options::female`
**Källa:** Female
**Svenska:** Kvinna
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::gender::options::male`
**Källa:** Male
**Svenska:** Man
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::af-za`
**Källa:** Afrikaans (South Africa)
**Svenska:** Afrikaans (Sydafrika)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::am-et`
**Källa:** Amharic (Ethiopia)
**Svenska:** Amhariska (Etiopien)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-ae`
**Källa:** Arabic (United Arab Emirates)
**Svenska:** Arabiska (Förenade Arabemiraten)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-bh`
**Källa:** Arabic (Bahrain)
**Svenska:** Arabiska (Bahrain)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-dz`
**Källa:** Arabic (Algeria)
**Svenska:** Arabiska (Algeriet)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-eg`
**Källa:** Arabic (Egypt)
**Svenska:** Arabiska (Egypten)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-iq`
**Källa:** Arabic (Iraq)
**Svenska:** Arabiska (Irak)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-jo`
**Källa:** Arabic (Jordan)
**Svenska:** Arabiska (Jordanien)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-kw`
**Källa:** Arabic (Kuwait)
**Svenska:** Arabiska (Kuwait)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-lb`
**Källa:** Arabic (Lebanon)
**Svenska:** Arabiska (Libanon)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-ly`
**Källa:** Arabic (Libya)
**Svenska:** Arabiska (Libyen)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-ma`
**Källa:** Arabic (Morocco)
**Svenska:** Arabiska (Marocko)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-om`
**Källa:** Arabic (Oman)
**Svenska:** Arabiska (Oman)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-qa`
**Källa:** Arabic (Qatar)
**Svenska:** Arabiska (Qatar)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-sa`
**Källa:** Arabic (Saudi Arabia)
**Svenska:** Arabiska (Saudiarabien)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ar-sy`
**Källa:** Arabic (Syria)
**Svenska:** Arabiska (Syrien)
**Motivering:** Microsoft Azure Speech and text-to-speech setup, options and regional voice labels.
**Status:** sparad och återläst i Lokalise.

## Kvarvarande arbete

Core-granskningen fortsätter; övriga tomma mål och saknade Core-nycklar finns kvar i den uppdaterade fullinventeringen.
