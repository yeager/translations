# Home Assistant Core – APCUPSd

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/apcupsd/strings.json` och Lokalise API med direkt återläsning.

Status: pågående radgranskning av 87 aktuella Lokalise-poster. Fyra korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `config::step::user::description` | `Ange värd och port för apcupsd NIS.` | Korrigerar den felaktiga satskonstruktionen. |
| `issues::apc_deprecated::title` | `Sensorn {entity_name} är föråldrad` | Korrekt ordföljd med dynamiskt sensornamn. |
| `issues::available_via_device_info::title` | `Sensorn {entity_name} är föråldrad` | Samma engelska rubrik, samma svenska formulering. |
| `issues::date_deprecated::title` | `Sensorn {entity_name} är föråldrad` | Samma engelska rubrik, samma svenska formulering. |

Platshållaren `{entity_name}` och referensen till apcupsd NIS är bevarade. Direkt API-återläsning bekräftade samtliga ändringar. TMX-ledgern är uppdaterad och validerad (1 686 poster). Resterande enhetsnamn och längre utfasningsmeddelanden fortsätter granskas separat.
