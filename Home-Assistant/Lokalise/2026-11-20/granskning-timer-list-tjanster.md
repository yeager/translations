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
- Inga platshållare eller pluraler förekommer. `svlang skrivregler` fann inga fel i en representativ fältbeskrivning och dess naturlighetsheuristik gav 10/10 för `Tar bort en timer från en timerlista.`; Hunspell markerar dock den kontextbundna sammansättningen `timerlista` (se föregående Timer list-rapport).

## Get timers

| Fullständig nyckel | Engelsk källtext | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::timer_list::services::get_timers::name` | Get timers | Hämta timers | Imperativ tjänstform. |
| `component::timer_list::services::get_timers::fields::status::name` | Status | Status | Etablerad svensk UI-term. |
| `component::timer_list::services::get_timers::fields::status::description` | Only return timers with the specified statuses. | Returnerar endast timers med angiven status. | Följer befintligt Home Assistant-minne för motsvarande statusfilter. |
| `component::timer_list::services::get_timers::description` | Gets the timers on a timer list. | Hämtar timers i en timerlista. | Bevarar komponentkontexten utan onödig omskrivning. |

Lokalise-nyckel-ID:n 984043128–984043131 var tomma på svenska.

## Finish timer och Create timer

| Fullständig nyckel | Engelsk källtext | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::timer_list::services::finish_timer::name` | Finish timer | Avsluta timer | Imperativ tjänstform. |
| `component::timer_list::services::finish_timer::fields::timer_id::name` | Timer ID | Timer-ID | Konsekvent fältetikett. |
| `component::timer_list::services::finish_timer::fields::timer_id::description` | The id of the timer to finish. | ID:t för timern som ska avslutas. | Korrekt böjning och samma term som tjänsten. |
| `component::timer_list::services::finish_timer::description` | Finishes a timer early, as if its remaining time had elapsed. | Avslutar en timer i förtid, som om dess återstående tid hade löpt ut. | Bevarar förtidsavslutet och jämförelsen. |
| `component::timer_list::services::create_timer::name` | Create timer | Skapa timer | Imperativ tjänstform. |
| `component::timer_list::services::create_timer::fields::name::name` | Name | Namn | Etablerad fältetikett. |
| `component::timer_list::services::create_timer::fields::name::description` | Optional name for the timer. | Valfritt namn för timern. | Kort och idiomatisk fältbeskrivning. |
| `component::timer_list::services::create_timer::fields::duration::name` | Duration | Varaktighet | Samma fältterm som i `subtract_time`. |
| `component::timer_list::services::create_timer::fields::duration::description` | How long the timer should run for. | Hur länge timern ska vara igång. | Naturlig formulering för driftstid. |
| `component::timer_list::services::create_timer::description` | Creates a new timer on a timer list and starts it counting down. | Skapar en ny timer i en timerlista och startar nedräkningen. | Bevarar både skapandet och den omedelbara nedräkningen. |

Lokalise-nyckel-ID:n 984043118–984043127 var tomma på svenska. Nästa tjänst i granskningsordningen är `component::timer_list::services::cancel_timer`.

`svlang skrivregler` fann inga fel i den längre `finish_timer`-beskrivningen och gav 10/10 i naturlighetsheuristiken för `create_timer`-beskrivningen. Hunspell accepterar `nedräkningen`, `återstående` och `varaktighet`.

## Cancel timer, Add time och komponentens återstående rader

| Fullständig nyckel | Engelsk källtext | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::timer_list::services::cancel_timer::name` | Cancel timer | Avbryt timer | Imperativ tjänstform. |
| `component::timer_list::services::cancel_timer::fields::timer_id::name` | Timer ID | Timer-ID | Konsekvent fältetikett. |
| `component::timer_list::services::cancel_timer::fields::timer_id::description` | The id of the timer to cancel. | ID:t för timern som ska avbrytas. | Korrekt böjning och samma term som tjänsten. |
| `component::timer_list::services::cancel_timer::description` | Cancels a timer without finishing it. | Avbryter en timer utan att avsluta den. | Skiljer avbrott från normalt avslut. |
| `component::timer_list::services::add_time::name` | Add time | Lägg till tid | Imperativ tjänstform. |
| `component::timer_list::services::add_time::fields::timer_id::name` | Timer ID | Timer-ID | Konsekvent fältetikett. |
| `component::timer_list::services::add_time::fields::timer_id::description` | The id of the timer to add time to. | ID:t för timern vars tid ska utökas. | Naturlig svensk formulering av målobjektet. |
| `component::timer_list::services::add_time::fields::duration::name` | Duration | Varaktighet | Samma fältterm som i övriga tjänster. |
| `component::timer_list::services::add_time::fields::duration::description` | How much time to add to the timer. | Hur mycket tid som ska läggas till på timern. | Bevarar den angivna tidsmängden. |
| `component::timer_list::services::add_time::description` | Adds time to a timer. | Lägger till tid på en timer. | Samma verb som tjänstnamnet. |
| `component::timer_list::selector::status::options::paused` | Paused | Pausad | Statusform. |
| `component::timer_list::selector::status::options::finished` | Finished | Avslutad | Statusform, konsekvent med `finish_timer`. |
| `component::timer_list::selector::status::options::cancelled` | Cancelled | Avbruten | Statusform, konsekvent med `cancel_timer`. |
| `component::timer_list::selector::status::options::active` | Active | Aktiv | Etablerad statusetikett. |
| `component::timer_list::exceptions::timer_not_found::message` | Unable to find timer with id: `{timer_id}` | Det gick inte att hitta en timer med ID:t `{timer_id}` | Bevarar platshållaren och korrekt ID-böjning. |
| `component::timer_list::entity_component::_::name` | `[%key:component::timer_list::title%]` | `[%key:component::timer_list::title%]` | Referensen ska bevaras ordagrant; titelnyckeln ger den synliga svenskan. |

Lokalise-nyckel-ID:n 984043102–984043117 var tomma på svenska. Den aktuella komponentfrågan omfattade **61** `timer_list`-nycklar; samtliga har nu en dokumenterad bedömning i de tre Timer list-rapporterna. Inga pluraler förekommer. Den enda platshållaren, `{timer_id}`, är identisk i käll- och förslagstext.

`svlang skrivregler` fann inga fel i felmeddelandet med platshållare och naturlighetsheuristiken gav 10/10 för `Lägger till tid på en timer.`. Hunspell accepterar de kontrollerade böjningarna `utökas`, `avbrytas` och `avslutad`.
