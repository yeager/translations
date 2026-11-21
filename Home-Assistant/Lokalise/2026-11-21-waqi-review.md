# Home Assistant Core – WAQI

Datum: 2026-11-21

Alla 48 WAQI-strängar har granskats mot aktuell källa. Två fel är rättade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `config::step::user::data_description::api_key` | `API-nyckel för World Air Quality Index` | Etablerad sammansättning med bindestreck och oförändrat tjänstenamn. |
| `selector::method::options::map` | `Välj närmaste mätstation från en punkt på kartan` | Fullständig och begriplig benämning på det objekt som väljs. |

Övriga strängar, inklusive föroreningsparametrar och platshållare, är korrekta.
