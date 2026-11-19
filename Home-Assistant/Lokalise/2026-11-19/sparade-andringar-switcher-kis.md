# Sparade ändringar för Switcher KIS

Två tidigare tomma fält sparades och återlästes i Lokalise 2026-11-19.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::switcher_kis::entity::sensor::shutdown_time::name` | Shutdown time | Tom | Avstängningstid |
| `component::switcher_kis::entity::sensor::auto_off::name` | Auto-off | Tom | Automatisk avstängning |

”Automatisk avstängning” följer den befintliga svenska benämningen för integrationens äldre sensor `auto_shutdown`. Den nya avstängningstiden anger när enheten stängs av.

## Reparationsrubriker

Fyra tidigare tomma fält sparades och återlästes i Lokalise 2026-11-19.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::switcher_kis::issues::deprecated_remaining_time::title` | The Switcher remaining time sensor is deprecated | Tom | Switchers sensor för återstående tid är föråldrad |
| `component::switcher_kis::issues::deprecated_auto_shutdown::title` | The Switcher auto shutdown sensor is deprecated | Tom | Switchers sensor för automatisk avstängning är föråldrad |

Referenserna följer den engelska källan och målen ovan har kontrollerats.

| Fullständig nyckel | Tidigare svenska | Sparad referens |
|---|---|---|
| `component::switcher_kis::issues::deprecated_remaining_time_scripts::title` | Tom | `[%key:component::switcher_kis::issues::deprecated_remaining_time::title%]` |
| `component::switcher_kis::issues::deprecated_auto_shutdown_scripts::title` | Tom | `[%key:component::switcher_kis::issues::deprecated_auto_shutdown::title%]` |

De fyra tillhörande beskrivningarna med platshållare återstår.
