# Home Assistant Core – Radio Frequency

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/radio_frequency/strings.json`  
Status: samtliga nio aktuella strängar granskade; en korrigering är sparad och återläst.

Entitetsnamn, felmeddelanden, kodformaterade `{entity_id}`-platshållare och
värdeplatshållarna `{frequency}` och `{modulation}` är kontrollerade.

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
| --- | --- | --- | --- |
| `exceptions::no_transmitters::message` | `Inga radiosändare tillgängliga` | `Inga radiosändare är tillgängliga` | Predikatet behövs i den fullständiga svenska satsen. Sparad och återläst i Lokalise 2026-11-21. |

Lokalise visar även en äldre, ej aktuell `_`-nyckel; den ingår inte i Core-källans
nio aktuella strängar och har inte ändrats. Den sparade översättningen är
API-verifierad med Lokalise-ID `8332067637` och ingår i det kanoniska TMX-minnet.
