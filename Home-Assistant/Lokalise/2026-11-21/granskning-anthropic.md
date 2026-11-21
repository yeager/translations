# Home Assistant Core – Anthropic

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/anthropic/strings.json`, tidigare delgranskningar och Lokalise API med direkt återläsning.

Status: pågående fullständig radgranskning. Konfigurationsavsnittet och dess referensmål är kontrollerade; två korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `config::step::user::description` | `Konfigurera Anthropic-integrationen genom att ange din API-nyckel från Anthropic. Instruktioner för att skaffa en API-nyckel finns i [dokumentationen]({instructions_url}).` | Idiomatisk svensk formulering; Markdown-länk och platshållare är bevarade. |
| `config::step::reauth_confirm::description` | `Återautentisering krävs. Ange din uppdaterade API-nyckel.` | Följer Home Assistants etablerade term för reauthentication. |

Den återstående omfattningen består av konfigurationsunderposter, undantag, problem och väljare. Tidigare rapporterade förslag och referenskedjor ska kontrolleras mot denna källversion innan de sparas. TMX-ledgern är uppdaterad och validerad (1 688 poster).
