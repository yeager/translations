# Home Assistant Core: Recorder-statistik

Granskad i Lokalise 2026-11-19. Nedan återges synlig engelsk källtext och aktuell svensk översättning. Samtliga behålls; inga ändringar gjordes. Nycklarna hade inga synliga platshållare eller referenser. Detta är en avgränsad granskning, inte ett påstående om täckning för hela Recorder.

| Fullständig nyckel | Engelska | Svenska |
|---|---|---|
| `component::recorder::services::get_statistics::name` | Get Recorder statistics | Hämta statistik från Recorder |
| `component::recorder::services::get_statistics::fields::units::name` | Units | Enheter |
| `component::recorder::services::get_statistics::fields::units::description` | Optional unit conversion mapping. | Valfri mappning för enhetsomvandling. |
| `component::recorder::services::get_statistics::fields::types::name` | Types | Typer |
| `component::recorder::services::get_statistics::fields::types::description` | The types of statistics values to return. | Typerna av statistikvärden som ska returneras. |
| `component::recorder::services::get_statistics::fields::statistic_ids::name` | Statistic IDs | Statistik-ID:n |
| `component::recorder::services::get_statistics::fields::statistic_ids::description` | The entity IDs or statistic IDs to return statistics for. | De entitets-ID:n eller statistik-ID:n som statistik ska returneras för. |
| `component::recorder::services::get_statistics::fields::start_time::name` | Start time | Starttid |
| `component::recorder::services::get_statistics::fields::start_time::description` | The start time for the statistics query. | Starttiden för statistikförfrågan. |
| `component::recorder::services::get_statistics::fields::period::name` | Period | Period |
| `component::recorder::services::get_statistics::fields::period::description` | The time period to group statistics by. | Tidsperioden som statistik ska grupperas efter. |
| `component::recorder::services::get_statistics::fields::end_time::name` | End time | Sluttid |
| `component::recorder::services::get_statistics::fields::end_time::description` | The end time for the statistics query. If omitted, returns all statistics from start time onward. | Sluttiden för statistikförfrågan. Om den utelämnas returneras all statistik från starttiden och framåt. |
| `component::recorder::services::get_statistics::description` | Retrieves statistics data for entities within a specific time period. | Hämtar statistikdata för entiteter inom en viss tidsperiod. |
