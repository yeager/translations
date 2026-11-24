# KNX: telegramegenskaper och sensor-klass

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::knx::selector::sensor_device_class::options::current` | `Nuvarande` | `Ström` | Källreferensen pekar på sensorklassen elektrisk ström. |
| `component::knx::config_panel::entities::create::sensor::knx::always_callback::label` | `Tvinga Uppdatering` | `Tvinga uppdatering` | Svensk versalisering i etikett. |
| `component::knx::selector::telegram_backend::options::postgres` | `PostgreSQL (Extern)` | `PostgreSQL (extern)` | Beskrivande parentes skrivs med gemen. |
| `component::knx::options::step::communication_settings::sections::telegram_store_section::data::telegram_db_backend` | `Backend för Telegram-lagring` | `Lagringsmetod för telegram` | Sektionen avser lagring av KNX-telegramhistorik; ersätter ett onödigt tekniskt låneord. |

Kontrollerade mot aktuell Core-källa och referenskontext, sparade/återlästa via Lokalise API 2026-11-24 och synkade till Home Assistant-minnets snapshot, PO och TMX.
