# Home Assistant Core – Alexa Devices

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/alexa_devices/strings.json`, Lokalise API med direkt återläsning.

Status: samtliga aktuella källsträngar är radgranskade. Sex korrigeringar är sparade och återlästa. Historiska poster har inte återinförts.

| Fullständig nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::alexa_devices::common::data_description_code` | Engångslösenordet för att logga in på ditt konto. För närvarande stöds endast koder från OTP-appar. | Ersätter det engelska `tokens` och den onödigt långa sammansättningen. Lokalise-ID `662508678`. |
| `component::alexa_devices::exceptions::invalid_sound_value::message` | Ogiltigt ljudvärde har angetts: `{sound}` | Rättar genus- och satsfel och bevarar platshållaren. Lokalise-ID `688367126`. |
| `component::alexa_devices::entity::notify::announce::name` | Meddela | Alexa-funktionen skickar ett meddelande; `Annonsera` har en missvisande betydelse på svenska. Lokalise-ID `662508699`. |
| `component::alexa_devices::selector::info_skill::options::fun_fact` | Berätta ett roligt faktum | Ersätter anglicismen `fun-fact`. Lokalise-ID `800693780`. |
| `component::alexa_devices::selector::sound::options::amzn_sfx_crowd_applause_01` | Applåder från publiken | Tar bort det ogrundade tillägget `2`. Lokalise-ID `704005496`. |
| `component::alexa_devices::exceptions::invalid_info_skill_value::message` | Ogiltigt informationskommando har angetts: `{info_skill}` | Ersätter felaktiga ordet `informationsfärdighet` och bevarar platshållaren. Lokalise-ID `800693773`. |
| `component::alexa_devices::services::send_info_skill::description` | Skickar ett info skill-kommando till en enhet | Konsekvent verbform. Lokalise-ID `800693791`. |

Inloggning, OTP, Drop In, entiteter, övriga undantag, 17 informationsalternativ, 42 aktuella ljudalternativ och samtliga tre tjänster är kontrollerade. Produkttermen `info skill` behålls där den är ett Alexa-kommandonamn.
