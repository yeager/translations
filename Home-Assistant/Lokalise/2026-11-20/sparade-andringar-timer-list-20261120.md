# Home Assistant Core — Timer list: sparade ändringar

Datum: 2026-11-20  
Status: sparade och återlästa i Lokalise-gränssnittet

| Lokalise-ID | Fullständig nyckel | Engelska | Sparad svenska |
| --- | --- | --- | --- |
| 984043162 | `component::timer_list::triggers::timer_unpaused::name` | Timer resumed | Timer återupptagen |
| 984043161 | `component::timer_list::triggers::timer_unpaused::description` | Triggers when a timer is resumed on a timer list. | Utlöses när en timer återupptas i en timerlista. |
| 984043160 | `component::timer_list::triggers::timer_time_changed::name` | Timer time changed | Timerns tid ändrad |
| 984043159 | `component::timer_list::triggers::timer_time_changed::description` | Triggers when time is added to or subtracted from a timer on a timer list. | Utlöses när tid läggs till eller dras av från en timer i en timerlista. |
| 984043158 | `component::timer_list::triggers::timer_paused::name` | Timer paused | Timer pausad |
| 984043157 | `component::timer_list::triggers::timer_paused::description` | Triggers when a timer is paused on a timer list. | Utlöses när en timer pausas i en timerlista. |
| 984043156 | `component::timer_list::triggers::timer_finished::name` | Timer finished | Timer avslutad |
| 984043155 | `component::timer_list::triggers::timer_finished::description` | Triggers when a timer finishes on a timer list. | Utlöses när en timer avslutas i en timerlista. |
| 984043154 | `component::timer_list::triggers::timer_created::name` | Timer created | Timer skapad |
| 984043153 | `component::timer_list::triggers::timer_created::description` | Triggers when a timer is created on a timer list. | Utlöses när en timer skapas i en timerlista. |
| 984043152 | `component::timer_list::triggers::timer_cancelled::name` | Timer cancelled | Timer avbruten |
| 984043151 | `component::timer_list::triggers::timer_cancelled::description` | Triggers when a timer is cancelled on a timer list. | Utlöses när en timer avbryts i en timerlista. |
| 984043149 | `component::timer_list::services::unpause_timer::name` | Resume timer | Återuppta timer |
| 984043148 | `component::timer_list::services::unpause_timer::fields::timer_id::name` | Timer ID | Timer-ID |
| 984043147 | `component::timer_list::services::unpause_timer::fields::timer_id::description` | The id of the timer to resume. | ID:t för timern som ska återupptas. |
| 984043146 | `component::timer_list::services::unpause_timer::description` | Resumes a paused timer. | Återupptar en pausad timer. |
| 984043145 | `component::timer_list::services::subtract_time::name` | Subtract time | Dra av tid |
| 984043144 | `component::timer_list::services::subtract_time::fields::timer_id::name` | Timer ID | Timer-ID |
| 984043143 | `component::timer_list::services::subtract_time::fields::timer_id::description` | The id of the timer to subtract time from. | ID:t för timern som tiden ska dras av från. |
| 984043142 | `component::timer_list::services::subtract_time::fields::duration::name` | Duration | Varaktighet |
| 984043141 | `component::timer_list::services::subtract_time::fields::duration::description` | How much time to subtract from the timer. | Den tid som ska dras av från timern. |
| 984043140 | `component::timer_list::services::subtract_time::description` | Subtracts time from a timer. | Drar av tid från en timer. |
| 984043139 | `component::timer_list::services::remove_timer::name` | Remove timer | Ta bort timer |
| 984043138 | `component::timer_list::services::remove_timer::fields::timer_id::name` | Timer ID | Timer-ID |
| 984043137 | `component::timer_list::services::remove_timer::fields::timer_id::description` | The id of the timer to remove. | ID:t för timern som ska tas bort. |
| 984043136 | `component::timer_list::services::remove_timer::description` | Removes a timer from a timer list. | Tar bort en timer från en timerlista. |
| 984043135 | `component::timer_list::services::pause_timer::name` | Pause timer | Pausa timer |
| 984043134 | `component::timer_list::services::pause_timer::fields::timer_id::name` | Timer ID | Timer-ID |
| 984043133 | `component::timer_list::services::pause_timer::fields::timer_id::description` | The id of the timer to pause. | ID:t för timern som ska pausas. |
| 984043132 | `component::timer_list::services::pause_timer::description` | Pauses an active timer. | Pausar en aktiv timer. |
| 984043131 | `component::timer_list::services::get_timers::name` | Get timers | Hämta timers |
| 984043130 | `component::timer_list::services::get_timers::fields::status::name` | Status | Status |
| 984043129 | `component::timer_list::services::get_timers::fields::status::description` | Only return timers with the specified statuses. | Returnerar endast timers med angiven status. |
| 984043128 | `component::timer_list::services::get_timers::description` | Gets the timers on a timer list. | Hämtar timers i en timerlista. |
| 984043127 | `component::timer_list::services::finish_timer::name` | Finish timer | Avsluta timer |
| 984043126 | `component::timer_list::services::finish_timer::fields::timer_id::name` | Timer ID | Timer-ID |
| 984043125 | `component::timer_list::services::finish_timer::fields::timer_id::description` | The id of the timer to finish. | ID:t för timern som ska avslutas. |
| 984043124 | `component::timer_list::services::finish_timer::description` | Finishes a timer early, as if its remaining time had elapsed. | Avslutar en timer i förtid, som om dess återstående tid hade löpt ut. |
| 984043123 | `component::timer_list::services::create_timer::name` | Create timer | Skapa timer |
| 984043122 | `component::timer_list::services::create_timer::fields::name::name` | Name | Namn |
| 984043121 | `component::timer_list::services::create_timer::fields::name::description` | Optional name for the timer. | Valfritt namn för timern. |
| 984043120 | `component::timer_list::services::create_timer::fields::duration::name` | Duration | Varaktighet |
| 984043119 | `component::timer_list::services::create_timer::fields::duration::description` | How long the timer should run for. | Hur länge timern ska vara igång. |
| 984043118 | `component::timer_list::services::create_timer::description` | Creates a new timer on a timer list and starts it counting down. | Skapar en ny timer i en timerlista och startar nedräkningen. |
| 984043117 | `component::timer_list::services::cancel_timer::name` | Cancel timer | Avbryt timer |
| 984043116 | `component::timer_list::services::cancel_timer::fields::timer_id::name` | Timer ID | Timer-ID |
| 984043115 | `component::timer_list::services::cancel_timer::fields::timer_id::description` | The id of the timer to cancel. | ID:t för timern som ska avbrytas. |

Varje värde sparades från ett tidigare dokumenterat förslag och lästes tillbaka
direkt i Lokalise. Inga platshållare eller pluralformer förekommer.
