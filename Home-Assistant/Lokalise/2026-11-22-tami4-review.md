# Tami4: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga 18 strängar i komponenten `tami4`
har lästs från Lokalise. Platshållaren `{drink_name}` är bevarad.

## Rättningar sparade i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::tami4::config::error::invalid_phone` | Ogiltigt telefonnummer, använd följande format: +46xxxxxxxx | Ogiltigt telefonnummer, använd följande format: +972xxxxxxxx | Telefonnummerformatet är tekniskt källvärde och får inte lokaliseras. |
| `component::tami4::entity::sensor::filter_litters_passed::name` | Filter vatten passerat | Filtrerat vatten | Naturlig svensk sensorbenämning. |
| `component::tami4::entity::sensor::filter_upcoming_replacement::name` | Filter kommande utbyte | Kommande filterbyte | Korrekt svensk sammansättning och ordföljd. |
| `component::tami4::entity::sensor::uv_upcoming_replacement::name` | UV kommande utbyte | Kommande UV-byte | Korrekt svensk sammansättning och ordföljd. |

Alla fyra ändringar sparades via Lokalise API och lästes tillbaka ordagrant.
De finns i det validerade HA-minnet (`swedish-tm`, commit `21bb832`).

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::tami4::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::tami4::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::tami4::config::error::invalid_auth` | Ogiltig autentisering |
| `component::tami4::config::error::unknown` | Oväntat fel |
| `component::tami4::config::step::otp::data::otp` | SMS-kod |
| `component::tami4::config::step::otp::description` | Ange den kod du fått via SMS |
| `component::tami4::config::step::otp::title` | SMS-verifiering |
| `component::tami4::config::step::user::data::phone` | Telefonnummer |
| `component::tami4::config::step::user::description` | Ange ditt telefonnummer (samma som du använde för att registrera dig i Tami4-appen) |
| `component::tami4::config::step::user::title` | SMS-verifiering |
| `component::tami4::entity::button::boil_water::name` | Koka vatten |
| `component::tami4::entity::sensor::filter_installed::name` | Filter installerat |
| `component::tami4::entity::sensor::uv_installed::name` | UV installerat |
| `component::tami4::entity::button::prepare_drink::name` | Förbered {drink_name} |

## Verifiering

- Lokalise API: alla 18 svenska översättningar hämtades direkt vid denna
  granskning; de fyra rättningarna lästes tillbaka efter skrivning.
- `hunspell-sv`: inga stavningsavvikelser i de sparade svenska
  formuleringarna.
- `svlang` godkänner de nya sensoretiketterna; den korta telefonfeltexten
  markeras bara på grund av den avsiktliga telefonmallen.
- HA-TMX-validatorn: `valid: 3326 entries` efter uppdateringen.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
