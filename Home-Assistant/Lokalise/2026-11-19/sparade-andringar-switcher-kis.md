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

## Reparation av återstående tid

Nyckel: `component::switcher_kis::issues::deprecated_remaining_time::description`. Tidigare svenska: tom. Sparad och återläst i Lokalise 2026-11-19.

Engelska:

```text
The `{entity_id}` ({entity_name}) sensor is deprecated and has been replaced by the **Shutdown time** sensor, which reports when the device will turn off.

Update any dashboards, templates, automations or scripts to use the new sensor, then disable `{entity_id}` to have it removed.
```

Svenska:

```text
Sensorn `{entity_id}` ({entity_name}) är föråldrad och har ersatts av sensorn **Avstängningstid**, som visar när enheten stängs av.

Uppdatera eventuella instrumentpaneler, mallar, automationer och skript så att de använder den nya sensorn. Inaktivera sedan `{entity_id}` för att ta bort den.
```

Variabler, kodmarkeringar, fetstil och styckesindelning kontrollerades. De tre andra reparationsbeskrivningarna återstår.

## Återstående tid i automationer och skript

Nyckel: `component::switcher_kis::issues::deprecated_remaining_time_scripts::description`. Tidigare svenska: tom. Sparad och återläst i Lokalise 2026-11-19.

Engelska:

```text
The `{entity_id}` ({entity_name}) sensor is deprecated and has been replaced by the **Shutdown time** sensor, which reports when the device will turn off.

It is still used in the following automations or scripts:
{items}

Update them to use the new sensor, then disable `{entity_id}` to have it removed.
```

Svenska:

```text
Sensorn `{entity_id}` ({entity_name}) är föråldrad och har ersatts av sensorn **Avstängningstid**, som visar när enheten stängs av.

Den används fortfarande i följande automationer eller skript:
{items}

Uppdatera dem så att de använder den nya sensorn. Inaktivera sedan `{entity_id}` för att ta bort den.
```

Variabler, kodmarkeringar, fetstil och styckesindelning kontrollerades. De två beskrivningarna för automatisk avstängning återstår.
