# Sparad Bosch Alarm-översättning

Sparad och återläst i Lokalise den 19 november 2026 efter användarens instruktion.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::bosch_alarm::services::set_date_time::fields::datetime::description` | The date and time to set. The time zone of the Home Assistant instance is assumed. If omitted, the current date and time is used. | Datum och tid som ska ställas in. Tidszonen för Home Assistant-instansen antas. Om den utelämnas används aktuellt datum och aktuell tid. | Datum och tid som ska ställas in. Home Assistant-instansens tidszon används. Om inget datum och ingen tid anges används aktuellt datum och aktuell tid. |

Källa och mål jämfördes med granskningsunderlaget och aktuell Lokalise-text före sparning.

## Övervakningslarm

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::bosch_alarm::entity::sensor::alarms_gas::state::supervisory` | Supervisory | Övervakande | Övervakningslarm |

Sparad och återläst i Lokalise den 19 november 2026. Boschs [bruksanvisning](https://cdn.commerce.boschsecurity.com/public/documents/Operation_Manual_enUS_2511430027.pdf) skiljer supervisory alarm från trouble och vanligt larm; översättningen beskriver ett larmtillstånd snarare än att systemet övervakar. Brand- och inbrottssensorernas motsvarande tillstånd hänvisar till detta mål på båda språken; referenserna behölls och kontrollerades vid återläsning.
