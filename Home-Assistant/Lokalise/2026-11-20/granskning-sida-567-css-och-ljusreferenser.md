# Home Assistant Core – Lokalisegranskning, sida 567

Granskad: 2026-11-20  
Källa: Lokalise API, Home Assistant Core, svenska (`sv`)  
Status: sparat och återläst i Lokalise

De nio svenska fälten nedan pekade på äldre `turn_on`-referenser trots att den engelska källan använder centrala `component::light::common`-referenser. De har synkroniserats till exakt motsvarande referensmål och återlästs från nyckel-API:t.

- `component::light::services::toggle::fields::brightness::description`
- `component::light::services::toggle::fields::brightness::name`
- `component::light::services::toggle::fields::brightness_pct::description`
- `component::light::services::toggle::fields::brightness_pct::name`
- `component::light::services::toggle::fields::color_name::description`
- `component::light::services::toggle::fields::color_name::name`
- `component::light::services::toggle::fields::color_temp::description`
- `component::light::services::toggle::fields::color_temp::name`
- `component::light::services::toggle::fields::effect::description`

Obs: translations-endpointen returnerar den upplösta svenska texten för en referens vid direkt återläsning, medan keys-endpointen auktoritativt bekräftar att referenssyntaxen är sparad. Färgbenämningarna och toggle-beskrivningen i övrigt kontrollerades utan ändring.
