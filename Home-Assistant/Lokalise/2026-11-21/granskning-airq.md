# Home Assistant Core – AirQ

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/airq/strings.json`, Lokalise API med direkt återläsning.

Status: samtliga 67 aktuella bladnycklar är radgranskade. Två korrigeringar är sparade och återlästa.

| Fullständig nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::airq::options::step::init::data::clip_negatives` | Begränsa negativa värden | Ersätter en otydlig direktöversättning av *clip*. Lokalise-ID `479693217`. |
| `component::airq::options::step::init::data_description::return_average` | air-Q gör det möjligt att läsa av både brusiga sensorvärden och de värden som har medelvärdesberäknats av enheten (standard). | Ersätter anglicismen “polla” och gör satsen idiomatisk. Lokalise-ID `479693220`. |

Kemiska ämnen, köldmedier, luftkvalitetsmått, decimaltecken, markdown i `{name}` och övriga konfigurationsposter är kontrollerade.
