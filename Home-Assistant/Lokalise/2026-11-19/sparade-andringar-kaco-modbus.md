# Sparade ändringar för KACO Modbus

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med [tidigare granskningsrapport](granskning-10921-11040.md).

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::kaco_modbus::config::step::user::data_description::unit_id` | Leave at 1 unless the inverter is reached through an RS485-to-TCP gateway, which needs the address configured on that gateway. | Lämna som 1 om växelriktaren inte nås via en RS485-till-TCP-gateway, som behöver den adress som är konfigurerad på gatewayen. | Om växelriktaren nås via en RS485-till-TCP-gateway anger du adressen som är konfigurerad på gatewayen. Annars låter du värdet vara 1. |

Den äldre rapportens förslag ”Ange då” var tvetydigt efter den nekande satsen. Den sparade texten skiljer tydligt mellan de två fallen.

## Återställd referens

| Fullständig nyckel | Engelsk källa | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::kaco_modbus::config::step::reconfigure::data_description::unit_id` | `[%key:component::kaco_modbus::config::step::user::data_description::unit_id%]` | Behåll värdet 1 om inte växelriktaren nås via en RS485 till TCP-gateway. I så fall behöver adressen konfigureras på gatewayen. | `[%key:component::kaco_modbus::config::step::user::data_description::unit_id%]` |

Referensen återställdes så att omkonfigurering använder samma text som den granskade målnyckeln. Referenser förs inte in som separata textsegment i TMX.
