# Matter: startorsak vid spänningsfall

Sparad och återläst i Lokalise den 19 november 2026.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::matter::entity::sensor::boot_reason::state::brown_out_reset` | Brownout reset | Återställning vid strömavbrott | Omstart vid spänningsfall |

Ett brownout innebär ett spänningsfall och behöver inte vara ett fullständigt strömavbrott. [Matter-sensorns kod](https://github.com/home-assistant/core/blob/0cc8b3a588d2d72768c50fb2239d327c7d1bb586/homeassistant/components/matter/sensor.py) visar att tillståndet är en startorsak och motsvarar `kBrownOutReset`. Ingen platshållare eller referens finns i texten.
