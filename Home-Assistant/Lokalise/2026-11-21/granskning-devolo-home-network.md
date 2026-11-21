# Home Assistant Core – devolo Home Network

Datum: 2026-11-21

Alla 37 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfigurationsflöden, entiteter, feltexter och platshållarna `{product}`, `{name}`, `{host_name}`, `{ip_address}`, `{title}` och `{error}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::user::description` | `Vill du starta installationen?` | `Vill du starta konfigurationen?` | `setup` avser konfigurationsflödet. |
| `entity::switch::switch_leds::name` | `Aktivera LED` | `Aktivera lysdioder` | Källan avser flera LED-lampor. |
| `entity::image::image_guest_wifi::name` | `Gäst-Wifi inloggningsuppgifter ...` | `Gäst-Wi-Fi-inloggningsuppgifter ...` | Korrekt stavning och sammansättning. |
| `entity::sensor::plc_rx_rate::name` | `PLC nedlänk PHY-hastighet` | `PLC-nedlänkens PHY-hastighet` | Korrekt teknisk sammansättning. |
| `entity::sensor::plc_tx_rate::name` | `PLC upplänk PHY-hastighet` | `PLC-uplänkens PHY-hastighet` | Korrekt teknisk sammansättning. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 062 poster.
