# Home Assistant Core – Prana

Datum: 2026-11-21

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::prana::config::step::confirm::description` | Set up {name} at {host}? | Konfigurera {name} på {host}? | Verifierad i Lokalise (ID `792684389`); båda platshållarna är intakta. |
| `component::prana::config::step::confirm::title` | Confirm Prana device | Bekräfta Prana-enheten | Verifierad i Lokalise (ID `792684390`); korrekt sammansättning och betydelse. |
| `component::prana::config::abort::invalid_device` | The device is invalid | Enheten är ogiltig | Verifierad i Lokalise (ID `792684386`). |
| `component::prana::config::abort::invalid_device_or_unreachable` | The device is invalid or unreachable | Enheten är ogiltig eller kan inte nås | Verifierad i Lokalise (ID `792684387`). |
| `component::prana::config::error::invalid_device_or_unreachable` | The device is invalid or unreachable | Enheten är ogiltig eller kan inte nås | Verifierad i Lokalise (ID `792684388`). |
| `component::prana::config::step::user::data_description::host` | The IP address or hostname of your Prana device. | IP-adressen eller värdnamnet för din Prana-enhet. | Verifierad i Lokalise (ID `792684392`). |
| `component::prana::config::step::user::title` | Add Prana device by IP | Lägg till Prana-enhet via IP | Verifierad i Lokalise (ID `792684393`). |
| `component::prana::entity::fan::extract::name` | Extract fan | Utsugsfläkt | Verifierad i Lokalise (ID `815951324`). |
| `component::prana::entity::fan::extract::state_attributes::preset_mode::state::boost` | Boost | Boost | Verifierad i Lokalise (ID `815951325`); lägesnamnet behålls som produktnära term. |
| `component::prana::entity::fan::extract::state_attributes::preset_mode::state::night` | Night | Natt | Verifierad i Lokalise (ID `815951326`). |
| `component::prana::entity::fan::supply::name` | Supply fan | Tilluftsfläkt | Verifierad i Lokalise (ID `815951327`). |
| `component::prana::entity::sensor::inside_temperature::name` | Inside temperature | Innetemperatur | Verifierad i Lokalise (ID `816742316`). |
| `component::prana::entity::sensor::inside_temperature_2::name` | Inside temperature 2 | Innetemperatur 2 | Verifierad i Lokalise (ID `816742317`). |
| `component::prana::entity::sensor::outside_temperature::name` | Outside temperature | Utetemperatur | Verifierad i Lokalise (ID `816742318`). |
| `component::prana::entity::sensor::outside_temperature_2::name` | Outside temperature 2 | Utetemperatur 2 | Verifierad i Lokalise (ID `816742319`). |
| `component::prana::entity::switch::auto::name` | Auto | Auto | Verifierad i Lokalise (ID `792684394`); lägesnamn. |
| `component::prana::entity::switch::auto_plus::name` | Auto plus | Auto plus | Verifierad i Lokalise (ID `792684395`); lägesnamn. |
| `component::prana::entity::switch::bound::name` | Bound | Bunden | Verifierad i Lokalise (ID `792684396`). |
| `component::prana::entity::switch::heater::name` | Heater | Värmare | Verifierad i Lokalise (ID `792684397`). |
| `component::prana::entity::switch::winter::name` | Winter | Vinter | Verifierad i Lokalise (ID `792684398`). |
| `component::prana::entity::number::display_brightness::name` | Display brightness | Display ljusstyrka → **Displayens ljusstyrka** | Osparat förslag; nuvarande text blandar engelska och svenska. Lokalise-ID `817535752`. |

## Referenser

- `component::prana::config::step::user::data::host` refererar till `common::config_flow::data::host`.
- `component::prana::entity::fan::supply::state_attributes::preset_mode::state::{boost,night}` refererar till motsvarande redan granskade `extract`-nycklar.

Alla direkta Prana-strängar i aktuell `strings.json` är därmed granskade. Endast förslaget för displayens ljusstyrka är osparat och är därför inte tillagt i TMX-minnet.
