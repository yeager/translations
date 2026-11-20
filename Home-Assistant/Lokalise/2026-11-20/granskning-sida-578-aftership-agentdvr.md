# Home Assistant Core – Lokalisegranskning, sida 578

Granskad: 2026-11-20  
Källa: Lokalise API, Home Assistant Core, svenska (`sv`)  
Status: sparat och återläst i Lokalise

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `component::aftership::services::add_tracking::fields::slug::description` | `Slug-ID för transportören för den nya spårningen` | `Transportörens slug för den nya spårningen.` | En slug är inte nödvändigtvis ett ID; svensk ordföljd och interpunktion. |
| `component::aftership::services::add_tracking::fields::slug::name` | `Slug-ID` | `Slug` | Bevarar den tekniska fälttermen korrekt. |
| `component::aftership::services::remove_tracking::fields::slug::description` | `Slug-ID för transportören för spårningen som ska tas bort` | `Transportörens slug för spårningen som ska tas bort.` | Samma korrigering i borttagningsflödet. |

Övriga 17 nycklar kontrollerades och lämnades oförändrade. Referensen till `add_tracking`-fältets slug är intakt.
