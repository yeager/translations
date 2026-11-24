# Haven IAQ-referenser och Elk-M1-källstatus

## Verifierade befintliga referenser

| Nyckel | Referensmål | Svenskt mål | Resultat |
| --- | --- | --- | --- |
| `component::haven_iaq::config::abort::already_configured` | `common::config_flow::abort::already_configured_device` | `Enheten är redan konfigurerad` | Exakt match på engelska och svenska. |
| `component::haven_iaq::config::error::cannot_connect` | `common::config_flow::error::cannot_connect` | `Det gick inte att ansluta.` | Samma svenska formulering som gemensamt mål, med avslutande punkt. |
| `component::haven_iaq::config::abort::cannot_connect` | `common::config_flow::error::cannot_connect` | `Det gick inte att ansluta.` | Samma svenska formulering som gemensamt mål, med avslutande punkt. |
| `component::haven_iaq::config::abort::already_in_progress` | `common::config_flow::abort::already_in_progress` | `Konfiguration pågår redan. Slutför den befintliga konfigurationen innan du börjar om.` | Fullständig och betydelsemässigt korrekt återgivning. |

Engelska och svenska referensmål kontrollerades i aktuell Core `homeassistant/strings.json` och Lokalise API 2026-11-24. Ingen måltext ändrades; minnet markerar dessa rader `verified-existing`.

## Elk-M1: källa saknas i aktuell upstream

Nycklarna `component::elkm1::issues::deprecated_sensor_scripts::description` och `component::elkm1::issues::deprecated_sensor::description` finns kvar i Lokalise men saknas i den aktuella upstream-versionen av `homeassistant/components/elkm1/strings.json` (dev vid commit `263472e2`, 2026-11-24). De lämnades oförändrade och markeras som väntande källkontroll; deras befintliga översättningar har inte omklassats som granskade mot aktuell källa.
