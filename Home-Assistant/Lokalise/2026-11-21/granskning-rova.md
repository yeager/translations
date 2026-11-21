# Home Assistant Core – Rova

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/rova/strings.json`  
Status: samtliga 16 aktuella strängar granskade mot Lokalise och källtext.

| Nyckel | Befintlig text | Föreslagen text | Motivering |
| --- | --- | --- | --- |
| `component::rova::config::abort::not_collected_anymore` | `Rova hämtar inte längre på {zip_code}.\n\nTa bort integrationen.` | `Rova hämtar inte längre på {address}.\n\nTa bort integrationen.` | Återställer källans platshållare; nuvarande mål använder fel variabel. |
| `component::rova::config::error::cannot_connect` | `Det gick inte att ansluta till Rova API` | `Det gick inte att ansluta till Rova-API:et.` | Korrekt svensk sammansättning och bestämd form. |

Förslagen är ännu inte sparade i Lokalise och ska återläsas före TMX-synkning.
