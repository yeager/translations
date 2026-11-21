# Home Assistant Core – YaleX BLE

Datum: 2026-11-21

Alla 27 YaleX BLE-strängar har granskats mot den äldre rapporten och aktuell källa. Tre motsvarande nyckeletiketter är korrigerade, sparade och API-återlästa.

| Omfattning | Tidigare form | Sparad form |
| --- | --- | --- |
| Konfiguration, återautentisering och nyckelplats | Varierande `Offlinenyckel` / `32-bytes hexadecimalsträng` | `Offline-nyckel (hexadecimal sträng på 32 byte)` |

Rättningen ger konsekvent sammansättning och korrekt måttform. Övriga Bluetooth-, lås- och platshållartexter är korrekta.
