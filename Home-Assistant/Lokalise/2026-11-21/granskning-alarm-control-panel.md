# Home Assistant Core – Alarm Control Panel

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/alarm_control_panel/strings.json`, Lokalise API med direkt återläsning.

Status: pågående. Gemensamma tidsfält och alla sju aktuella tjänster är kontrollerade; tillstånd, automatiseringar, villkor och utlösare granskas fortsatt rad för rad.

| Fullständig nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::alarm_control_panel::common::trigger_for_name` | I minst | Rättar den ogrammatiska formuleringen `I åtminstone`. Lokalise-ID `834982904`. |
| `component::alarm_control_panel::common::condition_for_name` | I minst | Samma terminologi för villkor. Lokalise-ID `837648211`. |

Tjänsternas namn för borta-, hemma-, natt- och semesterläge har fått korrekt svensk ordföljd. Beskrivningarna för hemma-, natt- och semesterläge samt avlarmning använder nu konsekvent verbet `larma`. Lokalise-ID `349650536`, `349650540`, `349650541`, `349650544`, `349650545`, `349650548`, `349650549`, `349650552`, `349650553`.
