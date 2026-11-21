# Home Assistant Core – DROP Connect

Datum: 2026-11-21

Alla 29 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. MQTT-konfiguration, vatten- och kassettmätare, TDS, aviseringar och skyddsläge kontrollerades. `{device_type}` och `{device_name}` är intakta.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::abort::not_supported` | `Konfigurering för DROP ...` | `Konfiguration för DROP ...` | Korrekt substantivform. |
| `entity::sensor::cart1::name` | `Kassett 1 återstående livslängd` | `Återstående livslängd för kassett 1` | Idiomatisk svensk ordföljd. |
| `entity::sensor::cart2::name` | `Kassett 2 återstående livslängd` | `Återstående livslängd för kassett 2` | Idiomatisk svensk ordföljd. |
| `entity::sensor::cart3::name` | `Kassett 3 återstående livslängd` | `Återstående livslängd för kassett 3` | Idiomatisk svensk ordföljd. |
| `entity::sensor::inlet_tds::name` | `Inlopp TDS` | `Inlopps-TDS` | Korrekt teknisk sammansättning. |
| `entity::sensor::outlet_tds::name` | `Utlopp TDS` | `Utlopps-TDS` | Korrekt teknisk sammansättning. |
| `entity::sensor::peak_flow_rate::name` | `Högsta vattenflöde i dag` | `Högsta vattenflödeshastighet i dag` | Källan avser flödeshastighet. |
| `entity::binary_sensor::pending_notification::name` | `Avisering oläst` | `Oläst avisering` | Naturlig svensk ordföljd. |
| `entity::binary_sensor::salt::name` | `Salt låg` | `Låg saltnivå` | Korrekt svensk sats/etikett. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 104 poster.
