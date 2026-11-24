# Ekey Bionyx, Airzone och Blue Current: uppföljning

Kontrollerade nio poster från rapporten `granskning-32941-33060.md` mot aktuell Core-källa och live Lokalise API den 24 november 2026. Alla svenska måltexter var redan sparade; ingen ny textändring gjordes.

| Fullständig nyckel | Svensk text | Kontroll |
| --- | --- | --- |
| `component::ekeybionyx::config::step::webhooks::data_description::url` | `URL till Home Assistant-instansen som kan nås från fingeravtryckskontrollen` | Bekräftad mot aktuell källtext; Home Assistant-instansen ska kunna nås från kontrollern. |
| `component::blue_current::services::start_charge_session::fields::device_id::name` | `Enhets-ID` | Korrekt sammansättning för fältetikett. |
| `component::blue_current::services::start_charge_session::fields::charging_card_id::name` | `Laddkorts-ID` | Korrekt sammansättning för fältetikett. |
| `component::airzone::entity::select::q_adapt::name` | `Q-Adapt` | Produkt-/funktionsnamnet ska behållas; tidigare översättning `Q-Anpassa` är ersatt i Lokalise. |
| `component::ekeybionyx::config::step::webhooks::data::webhook1` | `Händelseentitet 1` | Aktuell källa bekräftar händelseentiteter som mappas till funktioner. |
| `component::ekeybionyx::config::step::webhooks::data::webhook2` | `Händelseentitet 2` | Samma funktion, fält 2. |
| `component::ekeybionyx::config::step::webhooks::data::webhook3` | `Händelseentitet 3` | Samma funktion, fält 3. |
| `component::ekeybionyx::config::step::webhooks::data::webhook4` | `Händelseentitet 4` | Samma funktion, fält 4. |
| `component::ekeybionyx::config::step::webhooks::data::webhook5` | `Händelseentitet 5` | Samma funktion, fält 5. |
