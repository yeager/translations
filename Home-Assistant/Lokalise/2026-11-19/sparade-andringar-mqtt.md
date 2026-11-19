# MQTT: sparade ändringar i Lokalise

Den 19 november 2026 jämfördes engelsk och svensk text i Lokalise. Ändringarna sparades och återlästes. Källa: lokal rapport `granskning-38525-38554.md`.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::payload_stop` | The payload sent when a "stop" command is issued. Leave empty to disable the "stop" feature. | Nyttolasten som skickas när ett "stopp"kommando utfärdas. Lämna tomt för att inaktivera "stopp"funktionen. | Nyttolasten som skickas när ett stoppkommando utfärdas. Lämna tomt för att inaktivera stoppfunktionen. |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::payload_open` | The payload sent when an "open" command is issued. | Nyttolasten som skickas när ett "öppna"kommando utfärdas. | Nyttolasten som skickas när ett öppningskommando utfärdas. |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::payload_close` | The payload sent when a "close" command is issued. | Nyttolasten som skickas när ett "stäng"kommando utfärdas. | Nyttolasten som skickas när ett stängningskommando utfärdas. |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::state_stopped` | State "stopped" | Tillstånd "stoppad" | Tillstånd ”stoppat” |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::state_open` | State "open" | Tillstånd "öppen" | Tillstånd ”öppet” |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::state_closed` | State "closed" | Tillstånd "stängd" | Tillstånd ”stängt” |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::state_opening` | State "opening" | Tillstånd "öppnar" | Tillstånd ”öppnas” |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::state_closing` | State "closing" | Tillstånd "stänger" | Tillstånd ”stängs” |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::payload_stop` | Payload "stop" | Nyttolast "stopp" | Nyttolast för stopp |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::payload_open` | Payload "open" | Nyttolast "öppna" | Nyttolast för öppning |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::payload_close` | Payload "close" | Nyttolast "stäng" | Nyttolast för stängning |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data::payload_stop_tilt` | Payload "stop tilt" | Nyttolast "stopp lutning" | Nyttolast för att stoppa lutningen |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::payload_stop_tilt` | The payload sent when a "stop tilt" command is issued. | Nyttolasten som skickas när ett kommando "stoppa tilt" utfärdas. | Nyttolasten som skickas när ett kommando för att stoppa lutningen utfärdas. |
| `component::mqtt::config_subentries::device::error::cover_set_position_template_must_be_used_with_set_position_topic` | The set position template must be used with the set position topic | Mallen för 'set position' måste användas tillsammans med 'set position'-topic | Mallen för positionskommandon måste användas tillsammans med topic för positionskommandon |
| `component::mqtt::config_subentries::device::error::cover_get_position_template_must_be_used_with_get_position_topic` | The position value template must be used together with the position state topic | Mallen för positionsvärde måste användas tillsammans med 'position state'-topic | Mallen för positionsvärdet måste användas tillsammans med topic för positionstillstånd |
| `component::mqtt::config_subentries::device::error::cover_get_and_set_position_must_be_set_together` | The get position and set position topic options must be set together | Topic-alternativen 'get position' och 'set position' måste ställas in tillsammans | Topic för positionstillstånd och positionskommandon måste anges tillsammans |

Positionsfelen avviker från det äldre förslaget ”ämne”: Lokalises svenska MQTT-ordlista rekommenderar uttryckligen ”topic”.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::error::cover_value_template_must_be_used_with_state_topic` | The value template must be used with the state topic option | Värdemallen måste användas tillsammans med alternativet för tillståndsämne | Värdemallen måste användas tillsammans med alternativet för tillståndstopic |
| `component::mqtt::config_subentries::device::error::cover_tilt_status_template_must_be_used_with_tilt_status_topic` | The tilt value template must be used with the tilt status topic | Lutningsvärdemallen måste användas tillsammans med lutningsstatusämnet | Mallen för lutningsvärdet måste användas tillsammans med topic för lutningsstatus |
| `component::mqtt::config_subentries::device::error::cover_tilt_command_template_must_be_used_with_tilt_command_topic` | The tilt command template must be used with the tilt command topic | Lutningskommandomallen måste användas tillsammans med lutningskommandoämnet | Mallen för lutningskommandon måste användas tillsammans med topic för lutningskommandon |

De tre texterna anpassades efter Lokalises MQTT-ordlista för konsekvens med de närliggande feltexterna. Källtext och tidigare svenska kontrollerades i Lokalise och de sparade översättningarna återlästes.

## Positionsmallens variabler

Nyckel: `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data_description::set_position_template`.

Engelska: [Template]({command_templating_url}) to define the position to be sent to the set position topic. Within the template the following variables are available: `value` (the scaled target position), `entity_id`, `position` (the target position percentage), `position_open`, `position_closed`, `tilt_min` and `tilt_max`. [Learn more.]({url}#set_position_template)

Tidigare svenska: [Mall]({command_templating_url}) för att definiera den position som ska skickas till ämnet för inställd position. Inom mallen finns följande variabler tillgängliga: `värde` (den skalade målpositionen), `entitets_id`, `position` (målpositionens procentandel), `öppen_position`, `stängd_position`, `lutning_min` och `lutning_max`. [Läs mer.]({url}#set_position_template)

Sparad svenska: En [mall]({command_templating_url}) som anger positionen som ska skickas till topic för positionskommandon. Följande variabler finns i mallen: `value` (den skalade målpositionen), `entity_id`, `position` (målpositionen i procent), `position_open`, `position_closed`, `tilt_min` och `tilt_max`. [Läs mer.]({url}#set_position_template)

Källans variabelnamn återställdes och länkmål bevarades. Texten sparades och återlästes i Lokalise.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data::set_position_topic` | Set position topic | Ange positionsämne | Topic för positionskommandon |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data::set_position_template` | Set position template | Ställ in positionsmall | Mall för positionskommandon |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data::position_topic` | Position state topic | Ämne för positionstillstånd | Topic för positionstillstånd |

Källtext och tidigare svenska kontrollerades i Lokalise. Ändringarna sparades och återlästes med projektordlistans term ”topic”.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data_description::position_open` | Number which represents "open" position. | Nummer som representerar "öppen" position. | Talet som motsvarar positionen ”öppen”. |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data_description::position_closed` | Number which represents "closed" position. | Nummer som representerar en "stängd" position. | Talet som motsvarar positionen ”stängd”. |

Beskrivningarna jämfördes med källan, sparades och återlästes i Lokalise.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data::position_open` | Position "open" value | Positionens "öppna" värde | Positionsvärde för ”öppen” |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data::position_closed` | Position "closed" value | Positionens "stängda" värde | Positionsvärde för ”stängd” |

Fältnamnen jämfördes med källan och motsvarande hjälptexter; de sparades och återlästes i Lokalise.

## Mall för positionsvärde

Nyckel: `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data_description::position_template`.

Engelska: Defines a [template]({value_templating_url}) to extract the payload for the position topic. Within the template the following variables are also available: `entity_id`, `position_open`, `position_closed`, `tilt_min` and `tilt_max`. [Learn more.]({url}#position_template)

Tidigare svenska: Definierar en [mall]({value_templating_url}) för att extrahera nyttolasten för positionsämnet. Följande variabler finns också tillgängliga i mallen: `entity_id`, `position_open`, `position_closed`, `tilt_min` och `tilt_max`. [Läs mer.]({url}#position_template)

Sparad svenska: Definierar en [mall]({value_templating_url}) för att hämta nyttolasten från topic för positionstillstånd. Följande variabler finns också tillgängliga i mallen: `entity_id`, `position_open`, `position_closed`, `tilt_min` och `tilt_max`. [Läs mer.]({url}#position_template)

Källtext och tidigare översättning kontrollerades i Lokalise; texten sparades och återlästes med variabelnamn och länkmål bevarade.

## Topic för positionstillstånd

Nyckel: `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_position_settings::data_description::position_topic`.

Engelska: The MQTT topic subscribed to receive cover position state messages. [Learn more.]({url}#position_topic)

Tidigare svenska: Det MQTT-ämne som man prenumererar på för att ta emot meddelanden om enhetens position. [Läs mer.]({url}#position_topic)

Sparad svenska: Det MQTT-topic som Home Assistant prenumererar på för att ta emot meddelanden om skyddets position. [Läs mer.]({url}#position_topic)

Källan och tidigare översättning kontrollerades i Lokalise. Ändringen följer ordlistans termer ”topic” och ”skydd”; den sparades och återlästes med länkmålet bevarat.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::state_stopped` | The payload received at the state topic that represents the "stopped" state (for covers that do not report "open"/"closed" state). | Nyttolasten som mottagits vid det tillståndsämne som representerar tillståndet "stoppat" (för omslag som inte rapporterar tillståndet "öppet"/"stängt"). | Nyttolasten som tas emot på tillståndstopic och representerar tillståndet ”stoppat” (för skydd som inte rapporterar tillståndet ”öppet” eller ”stängt”). |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::state_opening` | The payload received at the state topic that represents the "opening" state. | Nyttolasten som tas emot vid tillståndsämnet som representerar "öppningstillståndet". | Nyttolasten som tas emot på tillståndstopic och representerar tillståndet ”öppnas”. |

Källtexter och tidigare översättningar kontrollerades i Lokalise; båda ändringarna sparades och återlästes. Termvalet följer ordlistan och tillståndens fältnamn.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::state_open` | The payload received at the state topic that represents the "open" state. | Nyttolasten som tas emot vid tillståndsämnet som representerar tillståndet "öppet". | Nyttolasten som tas emot på tillståndstopic och representerar tillståndet ”öppet”. |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::state_closing` | The payload received at the state topic that represents the "closing" state. | Nyttolasten som mottagits vid tillståndsämnet som representerar "stängningstillståndet". | Nyttolasten som tas emot på tillståndstopic och representerar tillståndet ”stängs”. |
| `component::mqtt::config_subentries::device::step::mqtt_platform_config::sections::cover_payload_settings::data_description::state_closed` | The payload received at the state topic that represents the "closed" state. | Nyttolasten som tas emot vid tillståndsämnet som representerar det "stängda" tillståndet. | Nyttolasten som tas emot på tillståndstopic och representerar tillståndet ”stängt”. |

Källor och tidigare texter jämfördes i Lokalise; alla tre sparades och återlästes.
