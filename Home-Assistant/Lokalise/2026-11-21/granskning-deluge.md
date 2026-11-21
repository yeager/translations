# Home Assistant Core – Deluge

Datum: 2026-11-21

Alla 25 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Konfigurationsinstruktionen, statusvärden och torrent-enheter kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `entity::sensor::protocol_traffic_download_speed::name` | `Protokoll trafik nedladdningshastighet` | `Nedladdningshastighet för protokolltrafik` | Korrekt svensk sammansättning och ordföljd. |
| `entity::sensor::protocol_traffic_upload_speed::name` | `Protokoll trafik uppladdningshastighet` | `Uppladdningshastighet för protokolltrafik` | Korrekt svensk sammansättning och ordföljd. |
| `entity::sensor::downloading_count::name` | `Nedladdnings räknare` | `Antal pågående nedladdningar` | Korrekt betydelse och idiomatisk etikett. |
| `entity::sensor::seeding_count::name` | `Antal seedare` | `Antal delningar` | Avser aktiva delningar, inte personer. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 047 poster.
