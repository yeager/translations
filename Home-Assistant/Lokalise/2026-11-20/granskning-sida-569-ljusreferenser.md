# Home Assistant Core – Lokalisegranskning, sida 569

Granskad: 2026-11-20  
Källa: Lokalise API, Home Assistant Core, svenska (`sv`)  
Status: sparat och återläst i Lokalise

Tre `turn_off`-fält hade svenska referenser till `turn_on` i stället för den centrala `light.common`-nyckel som den engelska källan använder:

- `component::light::services::turn_off::fields::flash::name`
- `component::light::services::turn_off::fields::transition::description`
- `component::light::services::turn_off::fields::transition::name`

Samtliga referenser är nu synkroniserade och återlästa från keys-endpointen. Övriga 17 nycklar kontrollerades och lämnades oförändrade. Referenser förs inte in i TMX, eftersom de inte är fristående översättningssegment.
