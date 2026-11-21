# Home Assistant Core – REFOSS

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/refoss/strings.json`  
Status: samtliga sju aktuella strängar granskade; ett ändringsförslag väntar på sparning i Lokalise.

Konfigurationsreferensen är intakt och de direkta sensornamnen för ström,
effekt, effektfaktor, spänning och månadens energi är korrekta. Ett sakfel har
identifierats:

| Nyckel | Befintlig svensk text | Föreslagen svensk text | Motivering |
| --- | --- | --- | --- |
| `entity::sensor::this_month_energy_returned::name` | `{channel_name} återanvänd energi denna månad` | `{channel_name} återförd energi denna månad` | *Energy returned* avser energi som har återförts/exporterats till nätet, inte energi som används på nytt. |

Lokalise visar dessutom tre äldre abortnycklar (`no_devices_found`,
`single_instance_allowed` och `already_configured`) som saknas i aktuell
Core-källa; de är historiska. Förslaget är inte sparat och därför inte tillagt
i TMX-minnet.
