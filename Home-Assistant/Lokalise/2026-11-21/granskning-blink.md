# Home Assistant Core – Blink

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/blink/strings.json`, tidigare radrapporter samt Lokalise API med direkt återläsning.

Status: samtliga aktuella bladsträngar och referensmål är radgranskade. Fem korrigeringar är sparade och återlästa.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `services::save_recent_clips::description` | `Sparar alla senaste videoklipp lokalt med filnamnet …` | `Sparar alla senaste videoklipp i en lokal katalog med filnamnsmönstret …` | Källan avser katalog och filnamnsmönster, inte ett enskilt filnamn. |
| `issues::service_deprecation::fix_flow::step::confirm::description` | `Blink Update-tjänsten …` utan kodmarkering | `Blinks uppdateringstjänst …` med bevarad kodmarkering | Korrekt svensk genitiv och Markdown-kodmarkering för tjänstnamnet. |
| `issues::service_deprecation::fix_flow::step::confirm::title` | `Blink uppdateringstjänst …` | `Blinks uppdateringstjänst …` | Korrekt sammansatt tjänstbenämning. |
| `issues::service_deprecation::title` | `Blink uppdateringstjänst …` | `Blinks uppdateringstjänst …` | Samma titel som fixflödet. |
| `entity::sensor::wifi_strength::name` | `Wi-Fi signalstyrka` | `Wi-Fi-signalstyrka` | Korrekt svensk sammansättning. |

Aktiva konfigurations-, autentiserings-, kamera-, undantags- och tjänstesträngar har kontrollerats. Platshållare, radbrytning, kodformatering och filnamnsmönstret `%Y%m%d_%H%M%S_[camera name].mp4` är bevarade. Äldre Lokalise-poster för borttagna Blink-tjänster hanteras inte som en del av den aktuella Core-källan. TMX-ledgern innehåller de fem nya, API-återlästa posterna och är validerad.
