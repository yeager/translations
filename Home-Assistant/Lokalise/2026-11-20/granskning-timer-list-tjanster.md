# Home Assistant Core – Timer list: återstående granskade tjänststrängar

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge och visade samtliga nedanstående svenska målvärden som tomma. De engelska texterna matchar `homeassistant/components/timer_list/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`. Detta är förslag, inte Lokalise-ändringar.

| Fullständig nyckel | Engelsk källtext | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::timer_list::services::subtract_time::fields::timer_id::name` | Timer ID | Timer-ID | Samma etikett i alla Timer list-tjänster. |
| `component::timer_list::services::subtract_time::fields::timer_id::description` | The id of the timer to subtract time from. | ID:t för timern som tiden ska dras av från. | Bevarar vilken timer som ändras. |
| `component::timer_list::services::subtract_time::fields::duration::name` | Duration | Varaktighet | Etablerad svensk UI-term för en tidslängd. |
| `component::timer_list::services::subtract_time::fields::duration::description` | How much time to subtract from the timer. | Den tid som ska dras av från timern. | Naturlig svensk fältbeskrivning. |
| `component::timer_list::services::subtract_time::description` | Subtracts time from a timer. | Drar av tid från en timer. | Samma åtgärdsverb som tjänstnamnet. |
| `component::timer_list::services::remove_timer::name` | Remove timer | Ta bort timer | Kort imperativ för tjänstnamn. |
| `component::timer_list::services::remove_timer::fields::timer_id::name` | Timer ID | Timer-ID | Konsekvent fältetikett. |
| `component::timer_list::services::remove_timer::fields::timer_id::description` | The id of the timer to remove. | ID:t för timern som ska tas bort. | Korrekt svensk ID-böjning. |
| `component::timer_list::services::remove_timer::description` | Removes a timer from a timer list. | Tar bort en timer från en timerlista. | Samma term som tjänstnamnet. |
| `component::timer_list::services::pause_timer::name` | Pause timer | Pausa timer | Imperativ åtgärdsform. |
| `component::timer_list::services::pause_timer::fields::timer_id::name` | Timer ID | Timer-ID | Konsekvent fältetikett. |
| `component::timer_list::services::pause_timer::fields::timer_id::description` | The id of the timer to pause. | ID:t för timern som ska pausas. | Korrekt svensk ID-böjning. |
| `component::timer_list::services::pause_timer::description` | Pauses an active timer. | Pausar en aktiv timer. | Direkt verbform utan betydelseförskjutning. |

## Kontrollstöd och fortsättning

- Lokalise-nyckel-ID:n är 984043132–984043144; samtliga måltexter var tomma vid läsningen.
- Flera `Timer ID`-rader har samma föreslagna `Timer-ID`, men varje fullständig nyckel redovisas separat för spårbarhet.
- Inga platshållare eller pluraler förekommer. `svlang skrivregler` fann inga fel i en representativ fältbeskrivning och dess naturlighetsheuristik gav 10/10 för `Tar bort en timer från en timerlista.`; Hunspell markerar dock den kontextbundna sammansättningen `timerlista` (se föregående Timer list-rapport). Nästa tjänst att läsa i komponenten är `component::timer_list::services::get_timers`.
