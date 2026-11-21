# Home Assistant Core – Remote Calendar

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/remote_calendar/strings.json`  
Status: samtliga 24 aktuella strängar granskade mot Lokalise och källtext.

Referenser och platshållare är korrekta. Följande tydliga fel eller
innehållsavvikelser återstår i Lokalise:

| Nyckel | Befintlig text | Föreslagen text |
| --- | --- | --- |
| `component::remote_calendar::config::step::auth::data_description::username` | `Användarnamnet för HTTP  Basic-autentisering .` | `Användarnamnet för HTTP Basic-autentisering.` |
| `component::remote_calendar::config::step::auth::data_description::password` | `Lösenordet för HTTP  Basic-autentisering .` | `Lösenordet för HTTP Basic-autentisering.` |
| `component::remote_calendar::config::step::user::description` | `Välj ett namn för kalendern som ska importeras` | `Ange uppgifterna för fjärrkalendern.` |
| `component::remote_calendar::config::step::user::data::url` | `URL för kalender` | `Kalender-URL` |
| `component::remote_calendar::exceptions::unable_to_parse::message` | `Kalenderflödet från fjärrservern innehåller ogiltiga uppgifter. Se felloggen för mer information.` | `Kalenderflödet från fjärrkällan innehåller ogiltiga uppgifter. Se felloggen för mer information.` |

De två HTTP Basic-texterna och feltexten under `config` var redan korrekta i
den aktuella API-katalogen. De tre återstående korrigeringarna är sparade och
återlästa via Lokalise API 2026-11-21 och ingår i verifierad HA-TMX med
översättnings-ID `5430849129`, `5430849318` och `5430849444`.
