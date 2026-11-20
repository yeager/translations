# Home Assistant Core – Lokalise-granskning, sida 599

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`ecobee`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::ecobee::services::create_vacation::fields::start_date::description` | `Datum då semestern börjar i formatet YYYY-MM-DD (valfritt, omedelbart om det inte anges tillsammans med "Start time").` | `Datum då semestern börjar i formatet YYYY-MM-DD (valfritt, omedelbart om det inte anges tillsammans med "Starttid").` | Fältnamnet är översatt i samma tjänst och ska inte lämnas på engelska i den svenska hjälpttexten. |
| `component::ecobee::services::create_vacation::fields::start_time::description` | `Tidpunkt då semesternläget börjar, i termostatens lokala tid. Anges i 24-timmarsformatet "HH:MM:SS".` | `Tidpunkt då semesterläget börjar, i termostatens lokala tid. Anges i 24-timmarsformatet "HH:MM:SS".` | Rättade det felaktiga sammansättningsordet. |

## Verifiering

Varje ändring skickades med Lokalise API och återlästes från respektive översättningsresurs. Platshållare och formatet `YYYY-MM-DD`/`HH:MM:SS` är oförändrade. Övriga 18 strängar på sidan är språkligt och terminologiskt korrekta eller är giltiga Lokalise-referenser.

Status: sparat och återläst i Lokalise.
