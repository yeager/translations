# Home Assistant Core – Anthropic

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/anthropic/strings.json`, tidigare delgranskningar och Lokalise API med direkt återläsning.

Status: samtliga aktuella bladsträngar och referensmål i komponenten är radgranskade. Tretton korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `config::step::user::description` | `Konfigurera Anthropic-integrationen genom att ange din API-nyckel från Anthropic. Instruktioner för att skaffa en API-nyckel finns i [dokumentationen]({instructions_url}).` | Idiomatisk svensk formulering; Markdown-länk och platshållare är bevarade. |
| `config::step::reauth_confirm::description` | `Återautentisering krävs. Ange din uppdaterade API-nyckel.` | Följer Home Assistants etablerade term för reauthentication. |
| `exceptions::api_authentication_error::message` | `Autentiseringsfel i Anthropics API: {message}. Återautentisering krävs.` | Korrekt possessivform och konsekvent term. |
| `exceptions::subentry_not_found::message` | `Underposten hittades inte.` | Ersätter den kvarlämnade engelska sammansättningen. |
| `exceptions::unexpected_stream_object::message` | `En ström av meddelanden förväntades.` | Tydlig och idiomatisk feltext. |
| `exceptions::response_stop_sequence::message` | `Claude slutade efter att ha stött på en stoppsekvens.` | Återger att Claude själv avbröt, inte att den stoppades externt. |
| `config_subentries::conversation::step::model::data::thinking_budget` | `Resonemangsbudget` | Ersätter felstavningen och gör begreppet begripligt. |
| `config_subentries::conversation::step::model::data::user_location` | `Inkludera hemposition` | *Home location* är en platsposition, inte nödvändigtvis en postadress. |
| `config_subentries::conversation::step::model::data_description::web_fetch` | `Verktyget för webbhämtning låter Claude hämta hela innehållet från angivna webbsidor och PDF-dokument för att utöka Claudes kontext med aktuellt webbinnehåll.` | Ersätter den oidiomatiska formuleringen “levande webbinnehåll”. |
| `issues::model_deprecated::fix_flow::step::init::description` | `Du uppdaterar {subentry_name} ({subentry_type}) i {entry_name}. Den aktuella modellen {model} är föråldrad. Välj en aktiv modell för att fortsätta.\n\nUtfasningsdatum: {deprecation_date}\nAvvecklingsdatum: {retirement_date}` | Återställer källans saknade platshållare och datumuppgifter. |
| `issues::model_deprecated::title` | `Modellen i {entry_name} är föråldrad` | Återställer den saknade platshållaren `{entry_name}`. |
| `selector::prompt_caching::options::automatic` | `Fullständig` | Svensk UI-text i stället för kvarlämnad engelska. |
| `config_subentries::conversation::step::init::data_description::llm_hass_api` | `**Enhetsstyrning** har endast åtkomst till de entiteter som du exponerar för röstassistenter. **Home Assistant** har åtkomst till allt och fungerar endast för administratörer, inte för röstassistentenheter.` | Återställer den kompletta aktuella källtexten och samma etablerade AI-åtkomstterminologi som andra komponenter använder. |

AI-uppgiftsunderposten har två egna aktuella strängar; båda är korrekta. Övriga nycklar där är referenser till de verifierade konversationsmålen. Äldre Lokalise-poster för borttagna steg ingår inte i aktuell Core-källa.

Den 22 november 2026 återställdes den kompletta `llm_hass_api`-beskrivningen
ovan via Lokalise API efter att den hade fallit tillbaka till den gamla, korta
etiketten `Tillåt LLM att styra Home Assistant.`. Ändringen lästes tillbaka
ordagrant, med bevarad Markdown, och fördes in i den validerade Core-TMX-filen
(3 322 poster, `swedish-tm`-commit `4b4d08f`).
