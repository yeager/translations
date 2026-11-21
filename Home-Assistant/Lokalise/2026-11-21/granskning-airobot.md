# Home Assistant Core – Airobot

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/airobot/strings.json`, Lokalise API med direkt återläsning.

Status: samtliga 44 aktuella bladnycklar är radgranskade. Tre korrigeringar är sparade och återlästa.

| Fullständig nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::airobot::config::step::dhcp_confirm::description` | Airobot-termostaten `{device_id}` upptäcktes på `{host}` … | Lägger till bestämd form och verb så att meddelandet blir en fullständig svensk sats. Lokalise-ID `761854009`. |
| `component::airobot::exceptions::authentication_failed::message` | Autentiseringen misslyckades. Autentisera igen. | Rätt bestämd form och tydlig meningsindelning. Lokalise-ID `765364226`. |
| `component::airobot::exceptions::connection_failed::message` | Det gick inte att kommunicera med enheten. | Fullständig svensk feltext med bestämd form. Lokalise-ID `765364227`. |

Övriga konfigurations-, återautentiserings-, sensor-, växel- och undantagstexter är korrekta. Platshållarna `{device_id}`, `{host}`, `{username}`, `{preset_mode}`, `{temperature}`, `{button}` och `{switch}` är bevarade.
