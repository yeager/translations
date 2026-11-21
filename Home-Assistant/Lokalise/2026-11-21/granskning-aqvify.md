# Home Assistant Core – Aqvify

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aqvify/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: samtliga 23 aktuella bladsträngar och referensmål är radgranskade. Fem korrigeringar är sparade och återlästa.

| Nyckelgrupp | Sparad text | Motivering |
|---|---|---|
| `config::step::user::description` | `Gå till ditt [Aqvify-konto]({aqvify_url}), kopiera din API-nyckel och klistra in den nedan.` | Idiomatisk svensk uppmaning; Markdown-länk bevarad. |
| `config::step::reauth_confirm::description` | `Återautentisering krävs. Ange din uppdaterade API-nyckel.` | Följer Core-terminologin. |
| `exceptions::api_*` | `Ett fel uppstod vid kommunikation med Aqvifys API för {entry}`; `Tidsgränsen överskreds vid kommunikation med Aqvifys API för {entry}` | Korrekt possessivform och svensk tidsgränsterm; platshållaren bevarad. |
| `entity::sensor::level_from_sensor::name` | `Nivå från sensorn` | Korrekt bestämd form. |

Volym-, flödes-, grundvatten- och nivånamn samt övriga autentiseringssträngar är korrekta. TMX-ledgern är uppdaterad och validerad (1 725 poster).
