# Home Assistant Core – Rova

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/rova/strings.json`  
Status: samtliga 16 aktuella strängar granskade mot Lokalise och källtext.

| Nyckel | Befintlig text | Föreslagen text | Motivering |
| --- | --- | --- | --- |
| `component::rova::issues::no_rova_area::description` | `Rova hämtar inte längre på {zip_code}.\n\nTa bort integrationen.` | `Rova hämtar inte längre på {address}.\n\nTa bort integrationen.` | Återställer källans platshållare; nuvarande mål använder fel variabel. |
| `component::rova::config::abort::cannot_connect` | `Det gick inte att ansluta till Rova API` | `Det gick inte att ansluta till Rova-API:et.` | Korrekt svensk sammansättning och bestämd form. |

Båda korrigeringarna är sparade och återlästa i Lokalise 2026-11-21. TMX-uppdatering avvaktar en verifierbar Lokalise-översättningsidentifierare från API:t; värden från enbart webbläsargränssnittet förs inte in i det kanoniska minnet.
