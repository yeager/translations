# Home Assistant Core: Xiaomi BLE — pågående granskning

Aktuell genomgång omfattade konfiguration, automatiseringar och entitetssträngar i `component::xiaomi_ble`, jämförda mot export och backup. Två entydiga rättningar har sparats och API-återlästs:

- `config::step::get_encryption_key_4_5_choose_method::description`: `dem` → `den`, eftersom bindningsnyckel är singular.
- `entity::sensor::weight_non_stabilized::name`: `Vikt ej stabiliserad` → `Ostabiliserad vikt`.

TMX-manifest: `Home-Assistant/2026-11-21-xiaomi-ble-verified.json`; den kanoniska TMX-filen validerades till 2 450 poster.

Flera lås- och felhändelser med tvetydlig engelska lämnas för separat kontextgranskning; komponenten är alltså inte markerad som slutgranskad.
