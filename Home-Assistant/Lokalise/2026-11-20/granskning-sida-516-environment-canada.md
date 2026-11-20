# Home Assistant Core – svensk granskning, sida 516

Datum: 2026-11-20  
Status: sparat och återläst i Lokalise

Granskade nycklar omfattar Environment Canada. Befintliga referenser och etablerade vädertermer lämnades oförändrade.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::environment_canada::entity::sensor::icon_code::name` | `Ikon-kod` | `Ikonkod` | Svensk sammansättning skrivs ihop. |
| `component::environment_canada::entity::sensor::statements::name` | `Uttalanden` | `Meddelanden` | Vädermyndighetens statements är meddelanden, inte muntliga uttalanden. |
| `component::environment_canada::entity::sensor::tendency::name` | `Tendenser` | `Tendens` | Källtexten är singular och etiketten avser ett enskilt värde. |
| `component::environment_canada::entity::sensor::text_summary::name` | `Summering` | `Sammanfattning` | Etablerad svensk UI-term för `Summary`. |
| `component::environment_canada::entity::sensor::watches::name` | `Klockor` | `Bevakningar` | Meteorologiska `watches` är bevakningar, inte tidmätare. |
