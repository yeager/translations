# ViCare: frånluft och avluft

Sparade och återlästa i Lokalise den 19 november 2026 efter uppföljning av [den tidigare granskningen](../2026-11-19-granskning/granskning-13801-13920.md).

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::vicare::entity::sensor::extract_temperature::name` | Extract temperature | Extraherad temperatur | Frånluftstemperatur |
| `component::vicare::entity::sensor::extract_humidity::name` | Extract humidity | Extraherad fuktighet | Frånluftens fuktighet |
| `component::vicare::entity::sensor::exhaust_temperature::name` | Exhaust temperature | Utströmningstemperatur | Avluftstemperatur |
| `component::vicare::entity::sensor::exhaust_humidity::name` | Exhaust humidity | Utströmningsfuktighet | Avluftens fuktighet |

[Viessmanns ventilationsbeskrivning](https://www.viessmann.co.uk/en/knowledge/technology-and-systems/housing-ventilation.html) skiljer extract air från exhaust air efter ventilationsaggregatet. [Core-koden](https://github.com/home-assistant/core/blob/0ed1ff906d0f04d21bf11c0b97ec813c928ff26b/homeassistant/components/vicare/sensor.py) kopplar nycklarna till separata extract- och exhaust-värden. Termerna frånluft och avluft återger denna skillnad. Inga platshållare eller referenser förekommer.
