# Home Assistant Core — granskning sida 484 (ElectraSmart, August, Workday, IMAP, KNX och Insteon)

Datum: 2026-11-20  
Status: sparat i Lokalise 2026-11-20

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::electrasmart::config::abort::already_configured` | `[%key:common::config_flow::abort::already_configured_device%]` | `[%key:common::config_flow::abort::already_configured_account%]` | Den svenska referensen pekar på ”enhet” medan engelskan pekar på ”konto”. Referensmålet måste vara identiskt mellan språken. |
| `component::electrasmart::config::error::invalid_phone_number` | `Antingen fel telefonnummer eller oregistrerad användare` | `Fel telefonnummer eller oregistrerad användare` | Kort feltext utan det inledande korrelatet ”antingen” är idiomatisk svenska. |
| `component::knx::options::step::communication_settings::data_description::telegram_log_size` | `Telegram att hålla i minnet för KNX panelgruppsmonitor. Högst: {telegram_log_size_max}` | `Antal telegram som ska behållas i minnet för gruppövervakningen i KNX-panelen. Högsta antal: {telegram_log_size_max}` | Gör betydelsen tydlig, undviker den ogenomskinliga sammansättningen ”panelgruppsmonitor” och bevarar platshållaren. |

Övriga 17 nycklar på sidan granskades utan dokumenterat ändringsförslag. August-referensen, Workdays landsalternativ, IMAP:s intervallnotation samt Insteons produkt- och åtgärdsnamn bevaras.