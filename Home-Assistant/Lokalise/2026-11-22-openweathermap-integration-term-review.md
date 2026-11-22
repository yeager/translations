# OpenWeatherMap: terminologi i migreringsflöde

Den 22 november 2026 rättades en aktuell OpenWeatherMap-migreringsinstruktion
direkt i Lokalise. Den använde de inkonsekventa formerna `integreringar` och
`integreringen`; Home Assistants etablerade term är `integrationer` respektive
`integrationen`.

| Fullständig nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `component::openweathermap::issues::deprecated_v25::fix_flow::step::migrate::description` | `Du måste migrera alla dina OpenWeatherMap-integreringar … migrera integreringen till API V3.0.` | `Du måste migrera alla dina OpenWeatherMap-integrationer … migrera integrationen till API V3.0.` |

## Verifiering

- Lokalise API: ändringen sparades och lästes tillbaka ordagrant.
- Den fullständiga textens radbrytningar och fetstil för **Bekräfta** är
  oförändrade.
- Ändringen är inlagd i den validerade HA-TMX-filen: `valid: 3334 entries`
  (`swedish-tm`-commit `37bdd0a`).

Ingen platshållare eller teknisk referens berörs.
