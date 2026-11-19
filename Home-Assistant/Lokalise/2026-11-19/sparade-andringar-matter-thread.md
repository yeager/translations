# Matter: routningsroll i Thread

Sparad och återläst i Lokalise den 19 november 2026.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::matter::entity::sensor::thread_routing_role::name` | Thread routing role | Thread-routing roll | Routningsroll i Thread |

Svensk sammansättning och meningsbyggnad förtydligar sensorns roll i Thread-nätverket. Strängen innehåller inga platshållare eller referenser.


## Slutenhet med möjlighet att bli router

Sparad och återläst i Lokalise den 19 november 2026.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::matter::entity::sensor::thread_routing_role::state::reed` | Router eligible end device | Routerkompatibel slutenhet | Slutenhet som kan bli router |

En REED är en slutenhet som kan uppgraderas till router, inte bara en enhet som är kompatibel med en router. [OpenThreads dokumentation](https://openthread.io/reference/group/api-thread-router) beskriver villkoren för routerrollen, och [Home Assistants Matter-kod](https://github.com/home-assistant/core/blob/61ae71a7ba62d80ba5f43c2bfb60e8093507604d/homeassistant/components/matter/sensor.py) kopplar värdet till `kReed`. Inga platshållare eller referenser finns i översättningen.
