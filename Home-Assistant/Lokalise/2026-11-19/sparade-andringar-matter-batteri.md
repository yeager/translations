# Matter: antal batterier

Sparad och återläst i Lokalise den 19 november 2026.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::matter::entity::sensor::battery_quantity::name` | Battery quantity | Tom | Antal batterier |

[Sensorimplementationen](https://github.com/home-assistant/core/blob/0cc8b3a588d2d72768c50fb2239d327c7d1bb586/homeassistant/components/matter/sensor.py) kopplar namnet till Matter-attributet `PowerSourceBatQuantity`. Strängen innehåller inga platshållare eller referenser.
