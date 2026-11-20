# Home Assistant Core – Simplepush

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`,
`homeassistant/components/simplepush/strings.json`  
Lokalise: läsning av `component::simplepush`, med en verifierad skrivning
2026-11-20.

## Omfattning

Samtliga **9** aktuella Simplepush-nycklar har lästs i Lokalise och jämförts
mot Core-källan. De två gemensamma referenserna är intakta.

| Fullständig nyckel | Engelsk källtext | Befintlig svenska | Bedömning |
| --- | --- | --- | --- |
| `component::simplepush::config::abort::already_configured` | Gemensam referens | Samma gemensamma referens | Korrekt. |
| `component::simplepush::config::error::cannot_connect` | Gemensam referens | Samma gemensamma referens | Korrekt. |
| `component::simplepush::config::step::user::data::device_key` | The device key of your device | Enhetsnyckeln för din enhet | Korrekt; terminologin stöds. |
| `component::simplepush::config::step::user::data::event` | The event for the events. | Händelsen för händelserna. | Korrekt, men den engelska källan är avsiktligt/ursprungligen tautologisk. |
| `component::simplepush::config::step::user::data::name` | Gemensam referens | Samma gemensamma referens | Korrekt. |
| `component::simplepush::config::step::user::data::password` | The password of the encryption used by your device | Lösenordet för krypteringen som används av din enhet | Korrekt. |
| `component::simplepush::config::step::user::data::salt` | The salt used by your device. | Det salt som används av din enhet. | Korrekt. |
| `component::simplepush::exceptions::title_or_message_too_long::message` | The notification title or message is too long. | Aviseringens titel eller brödtext är för lång. | Godtagbar och korrekt; inget ändringsförslag. |
| `component::simplepush::exceptions::send_message_failed::message` | Failed to send the Simplepush notification. | Det gick inte att skicka  Simplepush-aviseringen . | Se förslag nedan. |

## Sparat förslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::simplepush::exceptions::send_message_failed::message` | `Det gick inte att skicka  Simplepush-aviseringen .` | `Det gick inte att skicka Simplepush-aviseringen.` | Sparad i Lokalise och återläst i redigeringsfältet; tar bort dubbla mellanrum och felaktigt blanksteg före punkt. Produktnamn och innebörd bevaras. |

## Verktygsunderlag

- `svlang` gav endast produktnamnet *Simplepush* som sällsynt ord och två
  kontextfria meningssignaler; de innebär inte ett språkfel i UI-strängarna.
- Hunspell markerar den sammansatta produkttermen `Simplepush-aviseringen`.
  Produktnamnet saknas i den globala egennamnslistan, men ingen ordboksändring
  görs utan en oberoende produktkälla enligt språkpolicyn.
- `swedish-foss-terminology` stöder `device key` → `enhetsnyckel`,
  `Encryption` → `kryptering`, `Message` → `meddelande` och
  `notification` → `avisering`.
- Ingen Simplepush-post finns i det verifierade Home Assistant-TMX-minnet.
  Värdet ska föras in först vid nästa verifierade TMX-synkning.
