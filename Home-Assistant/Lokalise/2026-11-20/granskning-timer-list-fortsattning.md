# Home Assistant Core – Timer list: fortsatt granskning av tomma strängar

Datum: 2026-11-20. Lokalise visade samtliga rader nedan som tomma på svenska. Källan har kontrollerats mot `homeassistant/components/timer_list/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`. Detta är förslag; Lokalise har inte ändrats.

| Fullständig nyckel | Engelsk källtext | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::timer_list::triggers::timer_time_changed::name` | Timer time changed | Timerns tid ändrad | Kort och entydig händelserubrik. |
| `component::timer_list::triggers::timer_time_changed::description` | Triggers when time is added to or subtracted from a timer on a timer list. | Utlöses när tid läggs till eller dras av från en timer i en timerlista. | Behåller triggerperspektivet och båda operationerna. |
| `component::timer_list::triggers::timer_paused::name` | Timer paused | Timer pausad | Konsekvent kort händelserubrik. |
| `component::timer_list::triggers::timer_paused::description` | Triggers when a timer is paused on a timer list. | Utlöses när en timer pausas i en timerlista. | Rak aktiv formulering. |
| `component::timer_list::triggers::timer_finished::name` | Timer finished | Timer avslutad | *Avslutad* omfattar att timern når sitt slut. |
| `component::timer_list::triggers::timer_finished::description` | Triggers when a timer finishes on a timer list. | Utlöses när en timer avslutas i en timerlista. | Samma term som rubriken. |
| `component::timer_list::triggers::timer_created::name` | Timer created | Timer skapad | Konsekvent kort händelserubrik. |
| `component::timer_list::triggers::timer_created::description` | Triggers when a timer is created on a timer list. | Utlöses när en timer skapas i en timerlista. | Samma term som rubriken. |
| `component::timer_list::triggers::timer_cancelled::name` | Timer cancelled | Timer avbruten | Svensk händelseform för en avbruten timer. |
| `component::timer_list::triggers::timer_cancelled::description` | Triggers when a timer is cancelled on a timer list. | Utlöses när en timer avbryts i en timerlista. | Samma term som rubriken. |
| `component::timer_list::title` | Timer list | Timerlista | Sammanhållen komponenttitel. |
| `component::timer_list::services::unpause_timer::name` | Resume timer | Återuppta timer | Imperativ åtgärdsform för tjänstnamn. |
| `component::timer_list::services::unpause_timer::fields::timer_id::name` | Timer ID | Timer-ID | Standardiserad etikett med bindestreck. |
| `component::timer_list::services::unpause_timer::fields::timer_id::description` | The id of the timer to resume. | ID:t för timern som ska återupptas. | Korrekt svensk böjning av ID. |
| `component::timer_list::services::unpause_timer::description` | Resumes a paused timer. | Återupptar en pausad timer. | Parallell med tjänstnamnet. |
| `component::timer_list::services::subtract_time::name` | Subtract time | Dra av tid | Kort, idiomatisk åtgärdstext. |

## Kontrollstöd och fortsatt arbete

- Lokalise visade nyckel-ID 984043145–984043160 för dessa rader, alla med tomt svenskt målvärde.
- De två första Timer list-raderna (`timer_unpaused`) finns i den tidigare rapporten om nya tomma strängar och dupliceras inte här.
- Inga platshållare eller pluraler förekommer i dessa 16 rader. *Timer-ID* följer Home Assistant-terminologins etablerade `…-ID`-form.
- Hunspell accepterar `återupptas` och `timer`, men markerar sammansättningen `timerlista`. Den är begriplig och komponentbunden, men saknar här en oberoende generell ordbokskälla och läggs därför inte in som en global ordbokspost. `svlang skrivregler` fann inga fel i triggerbeskrivningen. `svlang check` gav en möjlig V2-varning för fältbeskrivningen `ID:t för timern som ska återupptas.`; den är en heuristikträff på en nominal fras med relativsats, inte ett grammatiskt fel.
- Nästa synliga sträng efter denna avgränsning är `component::timer_list::services::subtract_time::fields::duration::name`; den är inte granskad i denna rapport.
