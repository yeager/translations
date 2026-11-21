# Home Assistant Core – AquaCell

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aquacell/strings.json`, Lokalise API med direkt återläsning.

Status: samtliga 21 aktuella bladsträngar och referensmål är radgranskade. Sex korrigeringar är sparade och återlästa.

| Nyckelgrupp | Sparad text | Motivering |
|---|---|---|
| `config::step::user::description` | `Välj vattenavhärdarens varumärke och ange inloggningsuppgifterna för dess mobilapp.` | *Softener* avser vattenavhärdare, inte sköljmedel. |
| `salt_left_side_*` | `Salt på vänster sida (%)`; `Återstående tid för salt på vänster sida` | Korrekt svensk relation och enhet. |
| `salt_right_side_*` | `Salt på höger sida (%)`; `Återstående tid för salt på höger sida` | Korrekt svensk relation och enhet. |
| `last_update` | `Senaste uppdatering` | Sensorbenämning i nominalform. |

Platshållarna `{email}` och `{name}` är bevarade. Wi-Fi, autentisering och återautentisering är korrekta. Direkt API-återläsning bekräftade samtliga ändringar; TMX-ledgern är uppdaterad och validerad (1 719 poster).
