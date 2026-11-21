# Home Assistant Core – DSMR

Datum: 2026-11-21

Alla 98 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. DSMR-konfiguration, krypteringsnycklar, tariff- och faselektricitet, vatten/gas samt belgiska mätarfält kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `entity::sensor::actual_threshold_electricity::name` | `Faktisk tröskelvärde el` | `Faktiskt tröskelvärde för el` | Rätt genus och svensk konstruktion. |

Ändringen PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 109 poster.
