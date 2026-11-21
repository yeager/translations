# Home Assistant Core – BleBox

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/blebox/strings.json`, tidigare radrapporter samt Lokalise API med direkt återläsning.

Status: alla 99 aktuella Lokalise-poster som hör till komponentens bladsträngar och referensmål är radgranskade och återlästa. Fem korrigeringar är sparade och återlästa.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `entity::binary_sensor::input::name` | `Inmatning` | `Ingång` | En binärsensor anger en elektrisk/digital ingång, inte en inmatningshandling. |
| `entity::sensor::open_status::name` | `Öppen status` | `Öppningsstatus` | Sammansatt sensorbenämning för tillstånden öppen/stängd/låst. |
| `entity::sensor::co2_level::state::hazardous` | `Farligt` | `Farlig` | Tillståndet beskriver den feminina `koldioxidnivå` och ska kongruensböjas. |
| `entity::sensor::co2_level::state::medium` | `Medium` | `Måttlig` | Kvarlämnad engelsk UI-text ersatt med etablerad svensk nivåterm. |
| `entity::sensor::co2_level::state::unhealthy` | `Ohälsosamt` | `Ohälsosam` | Tillståndet beskriver `koldioxidnivå` och ska kongruensböjas. |

Övriga värden, inklusive enhetsmått och energiriktningar, är korrekta. Samtliga Markdown-markeringar, kodformaterade fält, radbrytningar och platshållare (`{address}`, `{name}`, `{host}`, `{index}`, `{error}`, `{sensor_name}`, `{device_name}`) har kontrollerats. Tidigare sparade nivå- och givaröversättningar har återlästs och är fortfarande korrekta. TMX-ledgern innehåller de fem korrigeringarna med Lokalise-spårbarhet och är validerad efter uppdateringen.
