# Home Assistant Core: Miele- och Immich-sensorer

Kontrollerat mot aktuell Lokalise-vy den 19 november 2026 och jämfört med Home Assistant-minnets ögonblicksbild från 24 oktober. Ingen ändring har gjorts i Lokalise. Nycklarna nedan återfanns inte i lokal rapportsökning eller GitHubs kodsökning; det bevisar inte att ingen annan tidigare granskning finns. Filtreringen bevisar inte att listan är ett sammanhängande intervall i den ofiltrerade ordningen.

| Fullständig nyckel | Engelska | Befintlig svenska | Bedömning |
|---|---|---|---|
| `component::miele::entity::sensor::water_forecast::name` | Water forecast | Vattenprognos | Behåll tills vidare. Sensorvärdet är procent; kontrollera produktens definition innan en mer precis benämning föreslås. |
| `component::miele::entity::sensor::energy_forecast::name` | Energy forecast | Energiprognos | Behåll tills vidare. Sensorvärdet är procent; kontrollera produktens definition innan en mer precis benämning föreslås. |
| `component::immich::entity::sensor::videos_count::unit_of_measurement` | videos | videor | Behåll. |
| `component::immich::entity::sensor::videos_count::name` | Videos count | Antal videor | Behåll. |
| `component::immich::entity::sensor::usage_by_videos::name` | Disk used by videos | Diskutrymme som används av videor | Behåll. |
| `component::immich::entity::sensor::usage_by_photos::name` | Disk used by photos | Diskutrymme som används av foton | Behåll. |
| `component::immich::entity::sensor::photos_count::unit_of_measurement` | photos | foton | Behåll. |
| `component::immich::entity::sensor::photos_count::name` | Photos count | Antal foton | Behåll. |
| `component::immich::entity::sensor::disk_use::name` | Disk used | Använt diskutrymme | Behåll. |
| `component::immich::entity::sensor::disk_usage::name` | Disk usage | Diskanvändning | Behåll. |
| `component::immich::entity::sensor::disk_size::name` | Disk size | Diskstorlek | Behåll. |
| `component::immich::entity::sensor::disk_available::name` | Disk available | Tillgängligt diskutrymme | Behåll. |

Källtext och måltext överensstämde med den historiska TMX-ögonblicksbilden för dessa nycklar. FOSS-termbanken stöder bland annat ”diskanvändning”, ”diskstorlek” och ”foto”; dess generella ”video → film” behöver inte användas här. Hunspell-sv gav inga stavningsträffar på de svenska texterna. Svlang flaggade passivkonstruktioner i två korta sensornamn; de är begripliga i sitt sammanhang och behålls. Inga platshållare, referenser eller pluralstrukturer förekom i de granskade strängarna.

Mieles [sensorimplementation](https://github.com/home-assistant/core/blob/dev/homeassistant/components/miele/sensor.py) anger procent för båda prognoserna; koden ensam fastställer inte exakt hur procentvärdena ska tolkas. Uppföljning: verifiera produktens definition och kontrollera nycklar mellan dessa filtrerade grupper i ofiltrerad ordning. Den historiska TMX:ens nästa identifierade nyckel efter sensorgruppen är `component::immich::config::step::user::data_description::verify_ssl` (650052346), men aktuell ordning måste kontrolleras.
