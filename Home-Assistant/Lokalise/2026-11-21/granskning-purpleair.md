# Home Assistant Core – PurpleAir

Datum: 2026-11-21  
Status: samtliga 43 aktuella bladnycklar är kontrollerade mot `origin/dev` och Lokalise.

## Sparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::purpleair::entity::sensor::uptime::name` | Uptime | `[%key:component::uptime::title%]` | **Drifttid** | Källan är vanlig text medan målet är en referens. Lokalise flaggar formatmismatch; samma referens är verifierad som `Drifttid` i `component::uptime::title`. Lokalise-ID `347200510`. |
| `component::purpleair::config::step::by_coordinates::description` | Search for a PurpleAir sensor within a certain distance of a location. | Sök efter en PurpleAir-sensor inom en viss distans från latitud/longitud. | **Sök efter en PurpleAir-sensor inom ett visst avstånd från en plats.** | Källan talar om en plats, inte specifikt latitud/longitud. Förslaget följer källans betydelse och normal svensk formulering. Lokalise-ID `250496896`. |
| `component::purpleair::options::step::remove_sensor::data_description::sensor_device_id` | The sensor to remove | Välj sensor att ta bort | **Sensorn som ska tas bort** | Fältbeskrivningen ska beskriva värdet, inte ge en annan uppmaning än källtexten. Lokalise-ID `253206597`. |

## Verifierade befintliga värden

- Konfigurations- och alternativflödenas gemensamma referenser är bevarade, inklusive API-nyckel, okänt fel, ogiltig API-nyckel och redan konfigurerad enhet.
- Referenser mellan konfigurations- och alternativflödet för plats, sökradie och sensorval är intakta.
- Sensoretiketterna för partikelantal, RSSI och VOC-luftkvalitetsindex är korrekta. Partikelstorlekar använder svensk decimalmarkering (`PM0,3`, `PM0,5`, `PM2,5`) där den förekommer.
- `Plats och sökradie`, `Platsen och radien inom vilken sensorer ska sökas.`, `Vilken av de närliggande sensorerna vill du följa?`, `Sensor att följa`, `Sökradie`, `Inga sensorer hittades nära koordinaterna inom sökradien.`, samt API-nyckel- och kartinställningssträngarna är korrekta i sin aktuella kontext.
- Historiska Lokalise-poster för separata latitud-, longitud- och avståndsfält, samt tidigare återautentiseringsposter, saknas i aktuell Core-källa. De är inte ändrade och ingår inte i aktuella 43 källnycklar.

Uptime är redan API-verifierat som `Drifttid`. De tre övriga förslagen är
sparade och API-återlästa 2026-11-21 med översättnings-ID `2007864997`,
`2025670469` och `2025671018` och ingår i verifierad TMX.
