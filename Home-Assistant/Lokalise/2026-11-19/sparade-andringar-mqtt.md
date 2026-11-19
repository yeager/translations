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
