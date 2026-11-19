# Sparade ändringar för Fronius

Sparade och återlästa i Lokalise 2026-11-19 efter kontroll mot tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::entity::switch::ac_power_limit_enabled::name` | AC power limiting | AC effektbegränsning | AC-effektbegränsning |
| `component::fronius::entity::number::ac_power_limit::name` | AC power limit | AC effektgräns | AC-effektgräns |

Bindestreck tydliggör sammansättningarna. Vid samma kontroll observerades separata Modbus-MPPT-strängar med platshållaravvikelser och olika källtexter; de kräver uppföljning mot aktuell källa och kontext.

## Modbus-likspänning

Sparad och återläst i Lokalise efter kontroll mot [aktuell källtext](https://github.com/home-assistant/core/blob/dev/homeassistant/components/fronius/strings.json).

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::entity::sensor::modbus_mppt_voltage_dc::name` | DC voltage (Modbus) | MPPT {mppt_no} Likspänning | Likspänning (Modbus) |

Den överflödiga platshållaren togs bort och Modbus återges. Separata fält för likström och likströmseffekt har samma platshållaravvikelse; försök att öppna effektfältet gav ett oväntat Lokalise-fel, så de återstår.

## Modbus-likström och likströmseffekt

Sparade och återlästa i Lokalise efter kontroll mot [aktuell källtext](https://github.com/home-assistant/core/blob/dev/homeassistant/components/fronius/strings.json).

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::entity::sensor::modbus_mppt_current_dc::name` | DC current (Modbus) | MPPT {mppt_no} Likström | Likström (Modbus) |
| `component::fronius::entity::sensor::modbus_mppt_power_dc::name` | DC power | MPPT {mppt_no} Likström | Likströmseffekt |

De överflödiga platshållarna togs bort och effekt skiljs från ström. De två fält som tidigare inte gick att öppna är nu sparade.

## Batteriladdning från elnätet

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::entity::switch::battery_grid_charging::name` | Battery grid charging | Batteri nätladdning | Batteriladdning från elnätet |

Sparad och återläst i Lokalise 2026-11-19. Sammansättningen och laddningens källa förtydligas.

## Urladdningseffekt

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::entity::number::battery_discharge_power_limit::name` | Battery discharge power limit | Batteriets urladdningsgräns | Gräns för batteriets urladdningseffekt |

Sparad och återläst i Lokalise 2026-11-19. Texten anger att gränsen avser effekt.

## Modbus-modell saknas

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::exceptions::modbus_model_unavailable::message` | The inverter no longer exposes the model this setting lives in | Växelriktaren exponerar inte längre modellen där den här inställningen finns | Växelriktaren tillhandahåller inte längre modellen där den här inställningen finns |

Sparad och återläst i Lokalise 2026-11-19. Tillhandahåller är tydligare i detta användarmeddelande.

## Modbus-port

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::fronius::config::step::user::data::modbus_port` | Modbus port | Modbus port | Modbus-port |

Sparad och återläst i Lokalise 2026-11-19. Den svenska och engelska referensen från `component::fronius::config::step::reconfigure::data::modbus_port` pekar båda på denna nyckel och behölls.
