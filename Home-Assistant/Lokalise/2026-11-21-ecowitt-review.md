# Home Assistant – Ecowitt: svensk radgranskning

Datum: 2026-11-21  
Komponent: `ecowitt`

Aktuell källtext och Lokalise-måltext kontrollerades för båda strängarna.

I den långa installationsinstruktionen sparades en avgränsad språkförbättring:

| Nyckel | Befintlig text | Sparad text | Kontroll |
| --- | --- | --- | --- |
| `component::ecowitt::config::create_entry::default` | För att slutföra integrationen måste du ange på Ecowitt-stationen att den ska skicka data … | För att slutföra integrationen måste du konfigurera Ecowitt-stationen så att den skickar data … | Platshållarna `{server}`, `{path}`, `{port}`, Markdown och liststruktur är bevarade. |

Den andra raden, **Är du säker på att du vill konfigurera Ecowitt?**, behölls. Ändringen är sparad via Lokalise API.