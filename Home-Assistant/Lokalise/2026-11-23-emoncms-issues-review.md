# Home Assistant Core – EmonCMS, avvecklingsmeddelanden

Datum: 2026-11-23

Tre aktuella avvecklings- och migreringsmeddelanden radgranskades mot
källtexten, plats­hållarna och länkmålen. Samtliga ändringar är sparade och
återlästa via Lokalise API.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::emoncms::issues::missing_include_only_feed_id::description` | Konfigurering av `{domain}` med hjälp av YAML tas bort. … Du får manuellt lägga till … genom att använda integrationens `konfigurera`-knapp. | Konfiguration av `{domain}` med YAML tas bort. … Lägg manuellt till … med integrationens knapp `konfigurera`. | Naturlig imperativ stil och kortare, korrekt syntax. |
| `component::emoncms::issues::remove_value_template::description` | Konfigurering av `{domain}` med hjälp av YAML håller på att tas bort … Vänligen ta bort … | Konfiguration av `{domain}` med YAML tas bort … Ta bort … | Konsekvent terminologi, direkta instruktioner, korrekt preposition och slutpunkt. |
| `component::emoncms::issues::migrate_database::description` | Din [emoncms]({url}) skickar inte en unik identifierare. … Vänligen uppgradera … | Din [emoncms]({url}) innehåller ingen unik identifierare. … Uppgradera … | Identifieraren är data i instansen, inte något den skickar; mellanslag, länktext och imperativ har rättats. |

Platshållarna `{domain}`, `{parameter}`, `{url}` och `{doc_url}`, markdown-länkarna,
YAML samt filnamnet `configuration.yaml` är bevarade. svlang gav 10,0; dess enda
okända ord är produktnamnet `emoncms`. De tre liveåterlästa posterna har lagts
till i det validerade Home Assistant-TMX-minnet.
