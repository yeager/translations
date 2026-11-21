# Home Assistant Core – Cielo Home

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`, `homeassistant/components/cielo_home/strings.json`, tidigare granskningsanteckningar och direkt återläsning via Lokalise API.

Alla 42 aktuella Cielo Home-strängar har granskats mot aktuell källtext och lästs direkt från Lokalise. Tre säkra förbättringar sparades och återlästes. Länkformatet `[documentation]({url})` och platshållaren `{name}` kontrollerades och bevarades.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::cielo_home::config::step::user::description` | Logga in med API-nyckeln för Cielo Home. Följ [dokumentationen]({url}) om hur du hämtar API-nyckeln. | Logga in med API-nyckeln för ditt Cielo Home-konto. Följ [dokumentationen]({url}) om hur du hämtar API-nyckeln. | Återger att API-nyckeln hör till användarens konto. |
| `component::cielo_home::entity::climate::climate_device::state_attributes::swing_mode::state::swing` | Swing | Svängning | Oöversatt fläktspjällsläge. |
| `component::cielo_home::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen för {name} har upphört att gälla | Korrekt svensk betydelse för utgången autentisering. |

De tre språkparen är tillagda i den kanoniska Home Assistant-TMX-filen med Lokalise-ID och direkt återläsningsspårning. Valideraren godkände 1 962 poster efter uppdateringen.
