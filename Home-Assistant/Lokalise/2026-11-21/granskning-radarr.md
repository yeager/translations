# Home Assistant Core – Radarr

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/radarr/strings.json`  
Status: samtliga 29 aktuella strängar granskade; en korrigering är sparad och återläst.

Interna referenser, API- och URL-referenser, flerradig konfigurationshjälp,
Radarr-namnet, siffervärdet `0` och servicebeskrivningar är kontrollerade.
Lokalise visar dessutom tre historiska abortnycklar som inte längre ingår i
aktuell Core-källa; de är referenssträngar och har inte ändrats.

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
| --- | --- | --- | --- |
| `config::error::wrong_app` | `Felaktig applikation har nåtts. Försök igen` | `Felaktig applikation kontaktades. Försök igen.` | Naturlig svensk formulering för anslutning till fel applikation. Sparad och återläst i Lokalise 2026-11-21. |

Den sparade översättningen saknar här ett verifierat Lokalise-översättnings-ID
och läggs därför inte till i det kanoniska TMX-minnet förrän ett sådant ID kan
exporteras spårbart.
