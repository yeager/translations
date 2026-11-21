# Home Assistant Core – Alexa Devices

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/alexa_devices/strings.json`, Lokalise API med direkt återläsning.

Status: pågående. Aktuella gemensamma inloggningssträngar, entiteter, undantag, kommandon och de 47 aktuella ljudalternativen granskas separat från 622 historiska katalogposter.

| Fullständig nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::alexa_devices::common::data_description_code` | Engångslösenordet för att logga in på ditt konto. För närvarande stöds endast koder från OTP-appar. | Ersätter det engelska `tokens` och den onödigt långa sammansättningen. Lokalise-ID `662508678`. |
| `component::alexa_devices::exceptions::invalid_sound_value::message` | Ogiltigt ljudvärde har angetts: `{sound}` | Rättar genus- och satsfel och bevarar platshållaren. Lokalise-ID `688367126`. |
| `component::alexa_devices::entity::notify::announce::name` | Meddela | Alexa-funktionen skickar ett meddelande; `Annonsera` har en missvisande betydelse på svenska. Lokalise-ID `662508699`. |
