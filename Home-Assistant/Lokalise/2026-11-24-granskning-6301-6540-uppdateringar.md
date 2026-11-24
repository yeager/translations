# HA Core 6301–6540: livekontroll och referenskorrigeringar

Datum: 2026-11-24. Källa: Home Assistant Core commit `2fdaa177f3e94535b3b649fb1ffc2dbba52eb4ce`. De 240 rapportnycklarna finns fortfarande i Lokalise. Literal engelsk källtext är oförändrad sedan arkivrapporten, utom Roborocks pluralpost som undersöks nedan. 85 av de engelska rapportfälten är referensmarkörer som i Lokalise API returneras med upplöst källtext.

## Sparade korrigeringar

Alla rader i tabellen sparades i Lokalise med API och återlästes.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Skäl |
| --- | --- | --- | --- |
| `component::nature_remo::config::error::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Matchar gemensam felreferens utan extra slutpunkt. |
| `component::lg_infrared::config::step::reconfigure::data_description::infrared_receiver_entity_id` | Entiteten för infraröd mottagare som ska användas för att ta emot signaler. | Mottagarentiteten som ska användas för att ta emot infraröda signaler. | Idiomatisk, korrekt sammansättning för Home Assistant-entitet. |
| `component::lg_infrared::config::step::tv::data_description::infrared_receiver_entity_id` | Den infraröda mottagarenhet som ska användas för att ta emot signaler. | Mottagarentiteten som ska användas för att ta emot infraröda signaler. | Rättar den grammatiskt ofullständiga formen och synkar referensmål med konsument. |
| `component::lg_infrared::config::step::reconfigure::data_description::infrared_entity_id` | Entiteten för infraröd sändare som ska användas för att skicka kommandon. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Idiomatisk fältbeskrivning med korrekt entitetsbegrepp. |
| `common::config_flow::data_description::infrared_entity_id` | Den infraröda sändarenhet som ska användas för att skicka kommandon. | Sändarentiteten som ska användas för att skicka infraröda kommandon. | Rättar grammatiken och synkar gemensamt referensmål. |
| `component::lg_infrared::config::step::reconfigure::data_description::hvac_modes` | Välj de driftlägen som luftkonditioneringen stöder. Värme är inte tillgängligt på alla modeller. | Välj de driftlägen som luftkonditioneringen stöder. Värme är inte tillgängligt på alla modeller. | Konsumenten behölls; källreferensen ändrades till samma redan korrekta text. |
| `component::lg_infrared::config::step::ac::data_description::hvac_modes` | Välj de driftlägen som din AC-enhet stöder. Värme är inte tillgängligt på alla modeller. | Välj de driftlägen som luftkonditioneringen stöder. Värme är inte tillgängligt på alla modeller. | Synkar referensmålet med konsumenten och använder etablerad svensk term. |
| `component::lg_infrared::config::abort::no_infrared_emitters` | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Konsumenten behölls; referensmålet ändrades till den korrekta, naturliga formuleringen. |
| `common::config_flow::abort::no_infrared_emitters` | Inga infraröda sändar-entiteter hittades. Konfigurera först en infraröd enhet. | Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet. | Tar bort felaktig särskrivning/bindestreckskonstruktion och matchar konsumenten. |
| `component::renault::config::abort::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Matchar gemensam felreferens. |
| `component::volkszaehler::config::step::reconfigure::data_description::port` | Portnummer för Volkszaehler-servern. | Portnumret för Volkszaehler-servern. | Matchar användarflödets referenstext. |
| `component::volkszaehler::config::step::reconfigure::data_description::host` | IP-adress eller värdnamn för Volkszaehler-servern. | IP-adressen eller värdnamnet för Volkszaehler-servern. | Matchar användarflödets referenstext och svensk bestämd form. |
| `component::snoo::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensamt reautentiseringsmål; `{name}` bevarad. |
| `component::lichess::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensamt reautentiseringsmål; `{name}` bevarad. |
| `component::engie_be::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensamt reautentiseringsmål; `{name}` bevarad. |
| `component::airnow::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensamt reautentiseringsmål; `{name}` bevarad. |
| `component::elevenlabs::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensamt reautentiseringsmål; `{name}` bevarad. |
| `component::egauge::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensamt reautentiseringsmål; `{name}` bevarad. |
| `component::snoo::config::step::reauth_confirm::data_description::password` | Ditt Snoo-lösenord | Ditt lösenord till Snoo | Matchar användarflödets lösenordsreferens. |
| `component::aidot::config::step::reauth_confirm::data_description::password` | Lösenord för inloggning via AiDot-appen. | Lösenord för inloggning via AiDot-appen | Matchar referensmålets interpunktion. |
| `component::smartyplants::config::step::reauth_confirm::data_description::api_key` | Skapa den i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Skapa den i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Konsumenten behölls; referensmålet rättades från det onaturliga ”Skapa den här”. |
| `component::smartyplants::config::step::user::data_description::api_key` | Skapa den här i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Skapa den i SmartyPlants-appen under Inställningar. Den identifierar ditt konto för Home Assistant. | Tar bort överflödigt ”här” och ger samma återanvända beskrivning. |
| `component::lichess::config::step::reauth_confirm::data_description::api_token` | Spelarens Lichess-API-token. | Spelarens Lichess-API-token. | Konsumenten behölls; referensmålets tekniska sammansättning rättades. |
| `component::lichess::config::step::user::data_description::api_token` | Spelarens Lichess API-token. | Spelarens Lichess-API-token. | Svensk bindestreckssammansättning för produktnamn plus API-token. |
| `component::airnow::config::step::reauth_confirm::data_description::api_key` | Gå till {api_key_url} för att skapa en API-nyckel. | Gå till {api_key_url} för att skapa en API-nyckel. | Konsumenten behölls; referensmålet gjordes kortare och konsekvent. `{api_key_url}` bevarad. |
| `component::airnow::config::step::user::data_description::api_key` | För att generera en API-nyckel, gå till {api_key_url}. | Gå till {api_key_url} för att skapa en API-nyckel. | Matchar den länkledda instruktionen och konsumenten. `{api_key_url}` bevarad. |
| `component::elevenlabs::config::error::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Matchar gemensam felreferens. |
| `component::sensor::entity_component::monetary::name` | Saldo | Monetärt saldo | Gör den engelska källan ”Monetary balance” explicit och passar även selector-alternativet. |
| `component::integration::selector::device_class::options::monetary` | Monetärt värde | Monetärt saldo | Matchar den återanvända klassen och skiljer saldot från ett godtyckligt monetärt värde. |

## Tidigare ögonblicksbild som inte längre motsvarade livevärden

Sex översättningar som skilde sig från rapportens gamla ögonblicksbild kontrollerades mot aktuell källtext. De nuvarande livevärdena är korrekta; inga ytterligare API-skrivningar behövdes:

- `component::homeassistant::integration_category::blinds_curtains::name` → `Persienner och gardiner`; beskrivningsnyckeln har i stället den längre listan med persienner, gardiner, jalusier, markiser, garageportar och grindar. Rapportens två äldre svenska värden var omkastade.
- `component::enphase_envoy::entity::sensor::comm_level_sub_ghz::name` → `Kommunikationsnivå under 1 GHz`, vilket bevarar att `sub-GHz` betyder under 1 GHz.
- `component::volkszaehler::config::abort::reconfigure_successful` → `Omkonfigureringen lyckades`, i linje med gemensam referens.
- WebDAV och Vitesy `reauth_confirm::title` använder redan den gemensamma korrekta texten `Autentiseringen har upphört att gälla för {name}`.

## Roborock: tidigare saknad pluralform

Källan `homeassistant/components/roborock/strings.json` har tillstånden `one: "1x"` och `two: "2x"`. Lokalise hade bara en ifylld svensk pluralform; `other` var tom. Fyllde i båda svenska formerna i nyckeln `component::roborock::entity::select::cleaning_cycles::state` (key ID `954532785`): `one → 1×`, `other → 2×`. API-återläsning bekräftar båda.

Detta avslöjade ett fel i `home_assistant_export.py`: API-källans tomma `other` gjorde att exporten tappade källans riktiga `two`-form, och engelsk `other` kunde felaktigt dupliceras från `one`. Exportören läser nu pluralformerna från aktuell Core `strings.json` när de finns och behåller tidigare granskningsstatus endast om livekälla och måltext fortfarande är oförändrade. `update_lokalise_batch.py` kan nu skicka och återläsa pluralobjekt. Core-exporten genererades om och validerades: 75 556 nycklar, 75 558 segment och 42 652 unika språkpar.

## Referenskontroll

82 referenspar i den här batchens rapport har kontrollerats mot aktuell källstruktur och Lokalise. Efter ändringarna är **0 av 82** par oöverensstämmande. Referens-/reviewstatus för 143 nycklar synkades till snapshot, PO och TMX. Stavningskontroll med hunspell-sv gav inga flaggor för ändringarna; svlang signalerade korrekt att `{name}` är en placeholder när den kontrollerades utan klamrar.

Detta täcker endast posterna 6301–6540; fullständig Core-granskning pågår fortfarande.
