# Sparade ändringar för Forecast.Solar

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::forecast_solar::services::get_forecast::fields::start::description` | Earliest period start to return (inclusive). If omitted, the response begins at the start of the cached forecast. | Den tidigaste perioden som ingår i resultatet (inklusive). Om detta utelämnas börjar svaret vid början av den cachade prognosen. | Tidigaste starttid för perioder som ska ingå i resultatet, inklusive den angivna tiden. Om den utelämnas börjar svaret vid början av den cachelagrade prognosen. |
| `component::forecast_solar::services::get_forecast::fields::end::description` | Latest period start to return (exclusive). If omitted, the response includes the full cached forecast. | Den senaste periodens startdatum ska returneras (exklusivt). Om detta utelämnas innehåller svaret den fullständiga cachelagrade prognosen. | Övre gräns för periodernas starttid. Perioder som börjar vid eller efter denna tid ingår inte. Om den utelämnas innehåller svaret hela den cachelagrade prognosen. |
| `component::forecast_solar::services::get_forecast::fields::resolution::description` | Resolution of the returned series. 'Native' uses the upstream Forecast.Solar resolution (15-minute on paid accounts, hourly on the free tier). 'Hourly' aggregates to whole-hour buckets. | Upplösning för den returnerade serien. Alternativet ”Native” använder den uppströmsliggande upplösningen från Forecast.Solar (15 minuter för betalkonton, per timme för gratiskonton). Alternativet ”Hourly” aggregerar till hela timmar. | Upplösning för den returnerade serien. ”Native” använder upplösningen från Forecast.Solar: 15 minuter för betalkonton och en timme för gratiskonton. ”Hourly” sammanställer värdena per hel timme. |
| `component::forecast_solar::services::get_forecast::fields::config_entry::description` | The Forecast.Solar configuration entry to query. | Den Forecast.Solar-konfigurationspost som ska frågas. | Forecast.Solar-konfigurationen som prognosen ska hämtas för. |

Startgränsen inkluderar den angivna tiden och slutgränsen utesluter den. Upplösning och val av konfiguration förtydligas.
