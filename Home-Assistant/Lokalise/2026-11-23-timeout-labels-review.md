# Timeout → Tidsgräns

Datum: 2026-11-23. Samtliga aktuella Core-nycklar där den engelska etiketten `Timeout` fortfarande lämnats oöversatt lästes direkt från Lokalise. Core använder redan `Tidsgräns` för samma begrepp i motsvarande inställningar och tjänster, vilket nu tillämpas konsekvent.

| Nycklar | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::broadlink::config::step::user::data::timeout`<br>`component::sense::config::step::user::data::timeout` | `Timeout` | `Tidsgräns` | Konfigurationsfält för maximal väntetid. |
| `component::scrape::config::step::user::data::timeout`<br>`component::scrape::options::step::resource::data::timeout`<br>`component::scrape::config::step::user::sections::advanced::data::timeout`<br>`component::scrape::options::step::init::sections::advanced::data::timeout`<br>`component::scrape::config::step::user::sections::additional::data::timeout`<br>`component::scrape::options::step::init::sections::additional::data::timeout` | `Timeout` | `Tidsgräns` | Samma Scrape-inställning förekommer i grund-, avancerad- och ytterligare-sektioner. |
| `component::elkm1::services::alarm_display_message::fields::timeout::name`<br>`component::remote::services::learn_command::fields::timeout::name` | `Timeout` | `Tidsgräns` | Tjänstfält för tidsbegränsning. |
| `component::snoo::entity::sensor::state::state::timeout` | `Timeout` | `Tidsgräns` | Statusvärde som anger tidsgräns. |

Alla elva ändringar sparades via Lokalise API, lästes tillbaka och infogades med live-källa i den kanoniska Home Assistant-TMX:en.
