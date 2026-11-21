# Home Assistant Core – Bosch Smart Home Controller

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bosch_shc/strings.json` och Lokalise API med direkt återläsning.

Status: samtliga 182 aktuella Lokalise-poster är radgranskade och återlästa. En korrigering är sparad och återläst.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `entity::switch::routing::name` | `Routing` | `Räckviddsutökning` | Källan är `Range extension`; etiketten avser radiosignalens räckvidd, inte nätverksroutning. |

Konfiguration, parkopplingsinstruktioner, ventilmotor, kamera, larm, belysning, värme, siren och samtliga väljare/reglage är kontrollerade. Markdown, radbrytningar och platshållarna `{name}`, `{model}`, `{host}` och `{hvac_mode}` är bevarade. TMX-ledgern innehåller korrigeringen och är validerad.
