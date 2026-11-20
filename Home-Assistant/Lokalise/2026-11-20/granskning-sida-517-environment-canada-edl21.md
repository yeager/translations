# Home Assistant Core – svensk granskning, sida 517

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Environment Canada och EDL21. Källtexten i Home Assistant Core kontrollerades för EDL21:s tekniska mätarposter; övriga specialiserade elmätartermer lämnades oförändrade.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::edl21::entity::sensor::last_signed_positive_active_energy_total::name` | `Senast undertecknad positiv aktiv energi totalt` | `Senaste signerade totalvärde för positiv aktiv energi` | `Signed` i denna mätarkontext betyder signerad, inte undertecknad. Svensk ordföljd för totalvärdet har också rättats. |
| `component::edl21::entity::sensor::metering_point_id_1::name` | `Mätpunkt ID 1` | `Mätpunkts-ID 1` | Korrekt svensk sammansättning och ID-skrivning. |
