# Home Assistant Core – Lokalisegranskning, sida 596

Granskad: 2026-11-20  
Källa: Lokalise API, Home Assistant Core, svenska (`sv`)  
Status: sparat och återläst i Lokalise

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `component::device_tracker::services::see::fields::gps::description` | `GPS-koordinater för var enheten befinner sig, angivna med latitud och longitud (till exempel: [51.513845, -0.100539]).` | Punktdecimaler måste behållas i JSON-/array-exemplet. |
| `component::device_tracker::services::see::name` | `Uppdatera enhetsspårare` | Tydligt svenskt tjänstnamn i linje med funktionen. |
| `component::button::services::press::name` | `Tryck på knapp` | Källans objekt saknades i den svenska åtgärdstexten. |

Övriga 17 nycklar kontrollerades och lämnades oförändrade. Kodformatering och konfigurationsvärden är intakta.
