# Home Assistant Core – svensk granskning, sida 510

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Airthings BLE, Weather, Scrape, Assist Pipeline, VoIP och BAF. Osäkra varumärkes- och produktetiketter lämnades oförändrade.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::scrape::selector::device_class::options::volatile_organic_compounds_parts` | `[%key:component::sensor::entity_component::volatile_organic_compounds::name%]` | `Delar av flyktiga organiska föreningar (VOC)` | Det tidigare referensmålet saknade `_parts`. Korrekt referens skickades; Lokalise normaliserade den till den aktuella svenska måltexten vid återläsning. |
| `component::assist_pipeline::entity::select::vad_sensitivity::name` | `Slutdetektering av röstkommando` | `Detektering av avslutat tal` | Funktionen avser när talandet upphör, inte om ett röstkommando har slutförts. |
