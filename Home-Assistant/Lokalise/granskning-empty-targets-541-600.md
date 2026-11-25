# Home Assistant Core: tidigare tomma svenska mål 541–600

- Granskade och sparade: **60/60**. Aktuell källtext, fullständig nyckel och tomt svenskt mål kontrollerades live i Lokalise; alla svenska värden sparades med API och lästes tillbaka direkt. HA Core-revision: `86a2eabe7e43f526db5821ef068087ce8404ae07`.
- Batchen innehöll åtta referensalias över fem unika mål. Alla kontrollerades live; tre reautentiseringstitlar korrigerades för att matcha den gemensamma referenstexten. Teslemetry-aliasets referensmål var tomt och sparades i batch 601–641. Platshållare, markdown-bold, kod, YAML och styckeindelning bevarades.
- `svlang` från aktuell verktygskällkod: inga radfel; skrivregler: inga fel. Hunspell efter uppdaterad ordlista flaggar inga svenska ord eller projekttermer; ordlistans 19 tester passerar.
- Home Assistant-minnet återanvändes för `Hämta avbildning`, `Strömgräns`, `Senast rapporterad`, `Stäng avisering`, `Autentiseringen har upphört att gälla för {name}` och `Exit Code` → `utgångskod`. För mired-enheten kontrollerades svensk teknisk dokumentation: [Nikon beskriver mired som färgtemperaturenhet och anger värden i mired](https://chsv-origin-onlinemanual.nikonimglib.com/zf/sv/white_balance_36.html).
- Home Assistant-TMX uppdaterad och validerad: **17 727 poster**. Manifest: `2026-11-25-reviewed-empty-targets-541-600.json`; TM-underlag: `2026-11-25-reviewed-empty-targets-541-600-tm.json`.

## Radgranskning

### `component::myuplink::services::get_datapoints::name`
**Källa:** Get datapoints
**Svenska:** Hämta datapunkter
**Motivering:** Kort fält-/åtgärdsetikett; etablerad HA-TM-term återanvänd där den finns.
**Status:** sparad och återläst i Lokalise.

### `component::neopool::options::abort::entry_not_loaded`
**Källa:** The options can be changed once the device has been set up.
**Svenska:** Inställningarna kan ändras när enheten har konfigurerats.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::netatmo::entity::sensor::heating_power_request::name`
**Källa:** Heating power request
**Svenska:** Begärd värmeeffekt
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::current::name`
**Källa:** {output_name} current
**Svenska:** {output_name} – ström
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::energy::name`
**Källa:** {output_name} energy
**Svenska:** {output_name} – energi
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::load::name`
**Källa:** {output_name} load
**Svenska:** {output_name} – belastning
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::power_factor::name`
**Källa:** {output_name} power factor
**Svenska:** {output_name} – effektfaktor
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::reverse_energy::name`
**Källa:** {output_name} reverse energy
**Svenska:** {output_name} – omvänd energi
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::total_energy::name`
**Källa:** {output_name} total energy
**Svenska:** {output_name} – total energi
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::netio::entity::sensor::total_reverse_energy::name`
**Källa:** {output_name} total reverse energy
**Svenska:** {output_name} – total omvänd energi
**Motivering:** Sensorens elmätarvärde skiljs från effekt och energi i motsatt riktning; output-namnets platshållare står kvar.
**Status:** sparad och återläst i Lokalise.

### `component::nexblue::entity::number::dynamic_current_limit::name`
**Källa:** Current limit
**Svenska:** Strömgräns
**Motivering:** NexBlue-smartmätarvärde för hushållets elförbrukning i angiven tidsperiod; TM-termen `Strömgräns` återanvänd.
**Status:** sparad och återläst i Lokalise.

### `component::nexblue::entity::sensor::household_consumption_month::name`
**Källa:** Household consumption this month
**Svenska:** Hushållets elförbrukning den här månaden
**Motivering:** NexBlue-smartmätarvärde för hushållets elförbrukning i angiven tidsperiod; TM-termen `Strömgräns` återanvänd.
**Status:** sparad och återläst i Lokalise.

### `component::nexblue::entity::sensor::household_consumption_today::name`
**Källa:** Household consumption today
**Svenska:** Hushållets elförbrukning i dag
**Motivering:** NexBlue-smartmätarvärde för hushållets elförbrukning i angiven tidsperiod; TM-termen `Strömgräns` återanvänd.
**Status:** sparad och återläst i Lokalise.

### `component::nexblue::entity::sensor::household_consumption_year::name`
**Källa:** Household consumption this year
**Svenska:** Hushållets elförbrukning i år
**Motivering:** NexBlue-smartmätarvärde för hushållets elförbrukning i angiven tidsperiod; TM-termen `Strömgräns` återanvänd.
**Status:** sparad och återläst i Lokalise.

### `component::omnilogic::config::step::reauth_confirm::data::password`
**Källa:** Password
**Svenska:** Lösenord
**Motivering:** Kort fält-/åtgärdsetikett; etablerad HA-TM-term återanvänd där den finns.
**Status:** sparad och återläst i Lokalise.

### `component::omnilogic::config::step::reauth_confirm::data_description::password`
**Källa:** The new password of your Hayward OmniLogic account.
**Svenska:** Det nya lösenordet för ditt Hayward OmniLogic-konto.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::omnilogic::config::step::reauth_confirm::description`
**Källa:** The password for {username} is no longer valid. Enter the new password.
**Svenska:** Lösenordet för {username} är inte längre giltigt. Ange det nya lösenordet.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::omnilogic::config::step::reauth_confirm::title`
**Källa:** Authentication expired for {name}
**Svenska:** Autentiseringen för {name} har upphört att gälla
**Motivering:** Granskad HA-TM-formulering för utgången autentisering återanvänds; namnplatshållaren bevaras.
**Status:** sparad och återläst i Lokalise.

### `component::opendisplay::exceptions::device_not_configured::message`
**Källa:** The OpenDisplay device has no stored configuration. Configure it with the OpenDisplay website or CLI, then reload the integration.
**Svenska:** OpenDisplay-enheten saknar sparad konfiguration. Konfigurera den via OpenDisplay-webbplatsen eller kommandoraden och läs sedan in integrationen på nytt.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::opendisplay::exceptions::display_not_supported::message`
**Källa:** Images cannot be uploaded to this device: its configuration has no display, or a color scheme this integration does not support yet.
**Svenska:** Det går inte att ladda upp bilder till den här enheten: konfigurationen saknar en display eller använder ett färgschema som integrationen ännu inte stöder.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::poolsense::config::step::reauth_confirm::data::password`
**Källa:** Password
**Svenska:** Lösenord
**Motivering:** Kort fält-/åtgärdsetikett; etablerad HA-TM-term återanvänd där den finns.
**Status:** sparad och återläst i Lokalise.

### `component::poolsense::config::step::reauth_confirm::data_description::password`
**Källa:** The new password of your PoolSense account.
**Svenska:** Det nya lösenordet för ditt PoolSense-konto.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::poolsense::config::step::reauth_confirm::description`
**Källa:** Enter the new password for {email}.
**Svenska:** Ange det nya lösenordet för {email}.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::poolsense::config::step::reauth_confirm::title`
**Källa:** Authentication expired for {name}
**Svenska:** Autentiseringen för {name} har upphört att gälla
**Motivering:** Granskad HA-TM-formulering för utgången autentisering återanvänds; namnplatshållaren bevaras.
**Status:** sparad och återläst i Lokalise.

### `component::portainer::entity::button::pull_image::name`
**Källa:** Pull image
**Svenska:** Hämta avbildning
**Motivering:** Portainer använder den etablerade Docker-termen `avbildning`; privata register och containeråterskapande behålls.
**Status:** sparad och återläst i Lokalise.

### `component::portainer::entity::sensor::container_exit_code::name`
**Källa:** Last exit code
**Svenska:** Senaste utgångskod
**Motivering:** Portainer/Docker-term följer HA-minnets `Exit Code` → `utgångskod`.
**Status:** sparad och återläst i Lokalise.

### `component::portainer::exceptions::image_pull_failed::message`
**Källa:** Failed to pull image {image}. If the image is in a private registry, recreate the container instead.
**Svenska:** Det gick inte att hämta avbildningen {image}. Om avbildningen finns i ett privat avbildningsregister måste du återskapa containern i stället.
**Motivering:** Portainer använder den etablerade Docker-termen `avbildning`; privata register och containeråterskapande behålls.
**Status:** sparad och återläst i Lokalise.

### `component::portainer::exceptions::image_pull_timeout::message`
**Källa:** Pulling the image took too long.
**Svenska:** Det tog för lång tid att hämta avbildningen.
**Motivering:** Portainer använder den etablerade Docker-termen `avbildning`; privata register och containeråterskapande behålls.
**Status:** sparad och återläst i Lokalise.

### `component::schlage::exceptions::schlage_command_failed::message`
**Källa:** Failed to send the command to the lock.
**Svenska:** Det gick inte att skicka kommandot till låset.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::shelly::entity::update::release_notes_messages::multi_step_update`
**Källa:** This update reorganizes the device memory and can run in two steps. The device installs the update and restarts, and may come back still reporting the previous firmware version. About a minute and a half later, it downloads the update again and restarts once more on the new version. Do not restart, remove power from, or otherwise interrupt the device until it reports the new firmware version. If the device comes back on the previous version and the second step does not start within a few minutes, start the update again.
**Svenska:** Den här uppdateringen omorganiserar enhetens minne och kan installeras i två steg. Enheten installerar uppdateringen och startar om, men kan fortfarande rapportera den tidigare firmwareversionen. Efter ungefär en och en halv minut laddar den ned uppdateringen igen och startar om på nytt med den nya versionen. Starta inte om enheten, bryt inte strömmen och avbryt inte uppdateringen på något annat sätt innan enheten rapporterar den nya firmwareversionen. Om enheten fortfarande rapporterar den tidigare versionen och det andra steget inte startar inom några minuter startar du uppdateringen igen.
**Motivering:** Shelly-firmwareuppdatering i två steg; tidsförlopp, varning och uppdateringsvillkor återgivna utan att tappa någon instruktion.
**Status:** sparad och återläst i Lokalise.

### `component::skoda::entity::climate::air_conditioning::name`
**Källa:** Air conditioning
**Svenska:** Luftkonditionering
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::skoda::exceptions::invalid_hvac_mode::message`
**Källa:** HVAC mode {hvac_mode} is not supported. Supported modes are: {hvac_modes}.
**Svenska:** Klimatläget {hvac_mode} stöds inte. Lägen som stöds: {hvac_modes}.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::smartyplants::entity::binary_sensor::needs_attention::name`
**Källa:** Needs attention
**Svenska:** Kräver uppmärksamhet
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::smartyplants::entity::sensor::last_reported::name`
**Källa:** Last reported
**Svenska:** Senast rapporterad
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::sonos::exceptions::join_different_household::message`
**Källa:** Cannot join {entity_id} to {target_entity_id} because they belong to different Sonos households.
**Svenska:** Det går inte att lägga till {entity_id} i {target_entity_id}, eftersom de tillhör olika Sonos-hushåll.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::starlink::entity::sensor::signal_quality::name`
**Källa:** Signal quality
**Svenska:** Signalkvalitet
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::system_bridge::services::dismiss_message::description`
**Källa:** Closes a notification sent with the System Bridge send message action. Linux only.
**Svenska:** Stänger en avisering som skickats med åtgärden Skicka meddelande i System Bridge. Gäller endast Linux.
**Motivering:** Linux-åtgärd för att stänga en System Bridge-avisering; ID och åtgärdsreferenser bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::system_bridge::services::dismiss_message::fields::id::description`
**Källa:** The ID returned by the System Bridge send message action.
**Svenska:** ID:t som returnerades av åtgärden Skicka meddelande i System Bridge.
**Motivering:** Linux-åtgärd för att stänga en System Bridge-avisering; ID och åtgärdsreferenser bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::system_bridge::services::dismiss_message::fields::id::name`
**Källa:** ID
**Svenska:** ID
**Motivering:** Kort fält-/åtgärdsetikett; etablerad HA-TM-term återanvänd där den finns.
**Status:** sparad och återläst i Lokalise.

### `component::system_bridge::services::dismiss_message::name`
**Källa:** Dismiss message
**Svenska:** Stäng avisering
**Motivering:** Linux-åtgärd för att stänga en System Bridge-avisering; ID och åtgärdsreferenser bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::tellduslive::config::step::reauth_confirm::description`
**Källa:** Home Assistant can no longer access your Telldus Live account. Select **Submit** to authorize **Home Assistant** again.
**Svenska:** Home Assistant har inte längre åtkomst till ditt Telldus Live-konto. Välj **Skicka** för att auktorisera **Home Assistant** på nytt.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::tellduslive::config::step::reauth_confirm::title`
**Källa:** Authentication expired for {name}
**Svenska:** Autentiseringen för {name} har upphört att gälla
**Motivering:** Granskad HA-TM-formulering för utgången autentisering återanvänds; namnplatshållaren bevaras.
**Status:** sparad och återläst i Lokalise.

### `component::template::config::step::light::data::temperature_kelvin`
**Källa:** Color temperature
**Svenska:** Färgtemperatur
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::config::step::light::data_description::temperature_kelvin`
**Källa:** Defines a template to get the color temperature of the light in kelvin.
**Svenska:** Anger en mall som hämtar lampans färgtemperatur i kelvin.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_light_mireds_options::description`
**Källa:** The template light entity with `{identifier}` uses options in mireds. These options are deprecated and will be removed in a future version of Home Assistant.

Update your YAML configuration by replacing the following options and change their templates to render kelvin instead of mireds:

{options}

The lowest mireds value is the highest kelvin value, so `min_mireds` is replaced by `max_kelvin` and `max_mireds` by `min_kelvin`.

After updating the configuration, reload the template entities or restart Home Assistant to fix this issue.
**Svenska:** Mallentiteten för belysning med `{identifier}` använder alternativ med värden i mired. Alternativen är föråldrade och tas bort i en framtida version av Home Assistant.

Uppdatera YAML-konfigurationen genom att ersätta alternativen nedan och ändra mallarna så att de returnerar värden i kelvin i stället för mired:

{options}

Det lägsta mired-värdet motsvarar det högsta kelvin-värdet. Därför ersätts `min_mireds` med `max_kelvin` och `max_mireds` med `min_kelvin`.

Läs sedan in mallentiteterna på nytt eller starta om Home Assistant för att åtgärda problemet.
**Motivering:** Mired är färgtemperaturenheten som används i källan; tekniska YAML-nycklar, backtick-markering och platshållare har bevarats.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_light_mireds_options::title`
**Källa:** Template light entity uses deprecated options in mireds ({identifier})
**Svenska:** Mallentiteten för belysning använder föråldrade mired-alternativ ({identifier})
**Motivering:** Mired är färgtemperaturenheten som används i källan; tekniska YAML-nycklar, backtick-markering och platshållare har bevarats.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_light_mireds_options_blueprint::description`
**Källa:** The template light blueprint `{blueprint}` uses options in mireds. These options are deprecated and will be removed in a future version of Home Assistant.

Update the blueprint by replacing the following options and change their templates to render kelvin instead of mireds:

{options}

The lowest mireds value is the highest kelvin value, so `min_mireds` is replaced by `max_kelvin` and `max_mireds` by `min_kelvin`.

If the blueprint was imported, re-import it once its author has updated it instead. Then reload the template entities or restart Home Assistant to fix this issue.
**Svenska:** Blueprinten `{blueprint}` för mallbelysning använder alternativ med värden i mired. Alternativen är föråldrade och tas bort i en framtida version av Home Assistant.

Uppdatera blueprinten genom att ersätta alternativen nedan och ändra mallarna så att de returnerar värden i kelvin i stället för mired:

{options}

Det lägsta mired-värdet motsvarar det högsta kelvin-värdet. Därför ersätts `min_mireds` med `max_kelvin` och `max_mireds` med `min_kelvin`.

Om blueprinten har importerats läser du in den på nytt när upphovspersonen har uppdaterat den. Läs sedan in mallentiteterna på nytt eller starta om Home Assistant för att åtgärda problemet.
**Motivering:** Mired är färgtemperaturenheten som används i källan; tekniska YAML-nycklar, backtick-markering och platshållare har bevarats.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_light_mireds_options_blueprint::title`
**Källa:** Template light blueprint uses deprecated options in mireds ({blueprint})
**Svenska:** Blueprinten för mallbelysning använder föråldrade mired-alternativ ({blueprint})
**Motivering:** Mired är färgtemperaturenheten som används i källan; tekniska YAML-nycklar, backtick-markering och platshållare har bevarats.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_light_temperature::description`
**Källa:** The template light helper {name} defines its color temperature in mireds. This is deprecated and will stop working in Home Assistant Core {breaks_in_ha_version}.

To fix this issue, open the options of the template light helper and define the color temperature in kelvin, or remove the actions on set color temperature if the light should not support a color temperature.
**Svenska:** Mallhjälpen för belysning {name} anger färgtemperaturen i mired. Det är föråldrat och slutar fungera i Home Assistant Core {breaks_in_ha_version}.

Öppna inställningarna för mallhjälpen för belysning och ange färgtemperaturen i kelvin, eller ta bort åtgärderna för att ställa in färgtemperaturen om lampan inte ska ha stöd för färgtemperatur.
**Motivering:** Mired är färgtemperaturenheten som används i källan; tekniska YAML-nycklar, backtick-markering och platshållare har bevarats.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_light_temperature::title`
**Källa:** Template light helper {name} uses a color temperature in mireds
**Svenska:** Mallhjälpen för belysning {name} använder färgtemperatur i mired
**Motivering:** Mired är färgtemperaturenheten som används i källan; tekniska YAML-nycklar, backtick-markering och platshållare har bevarats.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_weather_template_options::description`
**Källa:** The template weather entity with `{identifier}` uses options ending in `_template`. These options are deprecated and will be removed in a future version of Home Assistant.

Update your YAML configuration by renaming the following options:

{options}

After updating the configuration, reload the template entities or restart Home Assistant to fix this issue.
**Svenska:** Vädermallen `{identifier}` använder alternativ som slutar på `_template`. Alternativen är föråldrade och tas bort i en framtida version av Home Assistant.

Uppdatera YAML-konfigurationen genom att byta namn på alternativen nedan:

{options}

Läs sedan in mallentiteterna på nytt eller starta om Home Assistant för att åtgärda problemet.
**Motivering:** Vädermallens föråldrade alternativ och blueprintflödet förklaras; `_template`, kodmarkering och platshållare är bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_weather_template_options::title`
**Källa:** Template weather entity uses deprecated options ({identifier})
**Svenska:** Blueprinten för vädermallen använder föråldrade alternativ ({identifier})
**Motivering:** Vädermallens föråldrade alternativ och blueprintflödet förklaras; `_template`, kodmarkering och platshållare är bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_weather_template_options_blueprint::description`
**Källa:** The template weather blueprint `{blueprint}` uses options ending in `_template`. These options are deprecated and will be removed in a future version of Home Assistant.

Update the blueprint by renaming the following options:

{options}

If the blueprint was imported, re-import it once its author has updated it instead. Then reload the template entities or restart Home Assistant to fix this issue.
**Svenska:** Blueprinten `{blueprint}` för vädermallen använder alternativ som slutar på `_template`. Alternativen är föråldrade och tas bort i en framtida version av Home Assistant.

Uppdatera blueprinten genom att byta namn på alternativen nedan:

{options}

Om blueprinten har importerats läser du in den på nytt när upphovspersonen har uppdaterat den. Läs sedan in mallentiteterna på nytt eller starta om Home Assistant för att åtgärda problemet.
**Motivering:** Vädermallens föråldrade alternativ och blueprintflödet förklaras; `_template`, kodmarkering och platshållare är bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::issues::deprecated_weather_template_options_blueprint::title`
**Källa:** Template weather blueprint uses deprecated options ({blueprint})
**Svenska:** Blueprinten för vädermallen använder föråldrade alternativ ({blueprint})
**Motivering:** Vädermallens föråldrade alternativ och blueprintflödet förklaras; `_template`, kodmarkering och platshållare är bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::options::step::light::data::temperature_kelvin`
**Källa:** Color temperature
**Svenska:** Färgtemperatur
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::template::options::step::light::data_description::temperature_kelvin`
**Källa:** Defines a template to get the color temperature of the light in kelvin.
**Svenska:** Anger en mall som hämtar lampans färgtemperatur i kelvin.
**Motivering:** Radgranskad mot aktuell Home Assistant Core-källa och integrationskontext; betydelse och variabler bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::teslemetry::exceptions::energy_site_not_paired::message`
**Källa:** Teslemetry is not paired with the Powerwall system for {site}, pair it in the Teslemetry console or set up local control
**Svenska:** Teslemetry är inte parkopplad med Powerwall-systemet för {site}. Parkoppla systemet i Teslemetry-konsolen eller konfigurera lokal styrning.
**Motivering:** Teslemetry-parkoppling med Powerwall och alternativet lokal styrning; webbplats-, namn- och versionsplatshållare bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::teslemetry::issues::energy_site_not_paired::fix_flow::error::not_resolved`
**Källa:** Teslemetry still appears to be unpaired. Please complete the pairing at {link}, then try again.
**Svenska:** Teslemetry verkar fortfarande inte vara parkopplad. Slutför parkopplingen på {link} och försök igen.
**Motivering:** Teslemetry-parkoppling med Powerwall och alternativet lokal styrning; webbplats-, namn- och versionsplatshållare bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::teslemetry::issues::energy_site_not_paired::fix_flow::step::confirm::description`
**Källa:** Home Assistant cannot send battery commands, such as dispatching battery power, to {site} because Teslemetry is not paired with its Powerwall system and local control is not set up. Teslemetry can only send these commands through the cloud once its key is verified on the Powerwall gateway.

1. Open {link}.
2. Follow the prompts to pair Teslemetry with the Powerwall system.
3. Select **Submit** below to re-check.

Alternatively, set up local control for {site}.
**Svenska:** Home Assistant kan inte skicka batterikommandon, till exempel för att styra batteriets effekt, till {site}. Teslemetry är inte parkopplad med Powerwall-systemet och lokal styrning har inte konfigurerats. Teslemetry kan skicka kommandona via molnet först när nyckeln har verifierats i Powerwall-gatewayen.

1. Öppna {link}.
2. Följ anvisningarna för att parkoppla Powerwall-systemet.
3. Välj **Skicka** nedan för att kontrollera igen.

Du kan också konfigurera lokal styrning för {site}.
**Motivering:** Teslemetry-parkoppling med Powerwall och alternativet lokal styrning; webbplats-, namn- och versionsplatshållare bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::teslemetry::issues::energy_site_not_paired::fix_flow::step::confirm::title`
**Källa:** Pair Teslemetry with the Powerwall system for {site}
**Svenska:** Parkoppla Teslemetry med Powerwall-systemet för {site}
**Motivering:** Teslemetry-parkoppling med Powerwall och alternativet lokal styrning; webbplats-, namn- och versionsplatshållare bevarade.
**Status:** sparad och återläst i Lokalise.

## Referenskontroll efter radgranskningen

- OmniLogic-, PoolSense- och TelldusLive-titlarna synkades med `common::config_flow::title::reauth`: `Autentiseringen har upphört att gälla för {name}`. De äldre formuleringarna ersattes i Lokalise och HA-minnet.
- OmniLogic- och PoolSense-lösenord samt Template-lampans två mål matchade redan sina referenser.
- Teslemetry-fixflödets rubrik matchade aliaset, men den gemensamma målnyckeln var tom. Den fylldes och återlästes i batch 601–641.
- Källrevisionsmanifest och färska API-svar: `../Lokalise/2026-11-25-reference-targets-empty-541-600-live.json`.
