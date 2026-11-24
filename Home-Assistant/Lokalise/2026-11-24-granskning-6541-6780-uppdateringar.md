# HA Core 6541–6780: livekontroll och referensuppföljning

Datum: 2026-11-24. Källa: Home Assistant Core commit `2fdaa177f3e94535b3b649fb1ffc2dbba52eb4ce`. Alla 240 rapportnycklar återfanns i Lokalise. Literal engelsk källtext stämmer med den tidigare granskningen, med undantag för referensvärden som Lokalise API löser upp, och ingen ny ofylld svensk pluralform hittades i batchen. 55 referenser från rapporten jämfördes mot livevärden. Efter rättningarna är **0 av 55** referenspar oöverensstämmande.

## Sparade ändringar

Alla föreslagna värden sparades i Lokalise med API och återlästes. `{name}` bevarades där den förekommer.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Skäl |
| --- | --- | --- | --- |
| `component::zinvolt::config::step::reconfigure::data_description::password` | Lösenordet för ditt Zinvolt-konto. | Lösenordet till ditt Zinvolt-konto. | Matchar det granskade användarflödets referensmål. |
| `component::spotify::issues::user_not_premium::title` | Spotify-integration kräver ett Spotify Premium-konto | Spotify-integreringen kräver ett Spotify Premium-konto. | Svensk bestämd form; matchar den feltext som återanvänder titeln. |
| `component::litellm::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::swisscom::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::saj::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::llama_cpp::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::flow_it::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::smappee::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::iotty::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::ondilo_ico::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::theben_conexa::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::hortimax::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::fish_audio::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::cielo_home::config::step::reauth_confirm::title` | Autentiseringen för {name} har upphört att gälla | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::touchline_sl::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::sunsynk::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::nexblue::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar gemensam reautentiseringstext. |
| `component::swisscom::config::step::reauth_confirm::data_description::password` | Administratörslösenordet som står tryckt på undersidan av boxen. | Administratörslösenordet som står tryckt på undersidan av boxen. | Konsumenttexten behölls; det återanvända målet rättades från ”lådan” så uttrycket blir begripligt i routerkontext. |
| `component::swisscom::config::step::user::data_description::password` | Administratörslösenordet som är tryckt på undersidan av lådan. | Administratörslösenordet som står tryckt på undersidan av boxen. | Bättre teknisk kontext för Swisscom-boxen och samma text som återautentiseringsflödet. |
| `component::flow_it::config::step::reauth_confirm::data_description::password` | Lösenordet finns på den fysiska enhetens LCD-skärm. Öppna menyn, välj ikonen ”inställningar” och sedan ikonen ”wifi”. | Lösenordet visas på enhetens LCD-skärm. Öppna menyn, välj ikonen ”Inställningar” och sedan Wi-Fi-ikonen. | Tar bort överflödighet och rättar skrivsättet för Wi-Fi och menyetiketten. |
| `component::flow_it::config::step::user::data_description::password` | Lösenordet visas på enhetens LCD-skärm. Du hittar det genom att navigera i menyn, klicka på ikonen ”Inställningar” och sedan på ”Wi-Fi-ikonen”. | Lösenordet visas på enhetens LCD-skärm. Öppna menyn, välj ikonen ”Inställningar” och sedan Wi-Fi-ikonen. | Kortare och direkt instruktion; samma formulering i båda flödena. |
| `component::theben_conexa::config::step::reauth_confirm::data_description::password` | Lösenordet från din elnätsoperatör. | Lösenordet från din elnätsoperatör. | Konsumenttexten behölls; användarflödets referensmål uppdaterades till en preciserad svensk term. |
| `component::theben_conexa::config::step::user::data_description::password` | Lösenordet från nätägaren | Lösenordet från din elnätsoperatör. | Preciserar ”power grid operator” och matchar återautentiseringsflödet. |
| `component::nyt_games::config::step::reconfigure::data_description::token` | Värdet för NYT Games-kakan NYT-S. | Värdet för NYT Games-cookien NYT-S. | Etablerad teknisk term och tydlig koppling till cookien NYT-S. |
| `component::nyt_games::config::step::user::data_description::token` | NYT Games NYT-S cookie-värde. | Värdet för NYT Games-cookien NYT-S. | Idiomatisk och tekniskt tydlig formulering; matchar omkonfigureringen. |
| `component::marantz_rs232::config::error::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Matchar gemensam felreferens utan extra slutpunkt. |
| `component::marantz_rs232::config::abort::already_configured` | Enheten är redan konfigurerad. | Enheten är redan konfigurerad | Matchar gemensam redan-konfigurerad-referens. |
| `component::hortimax::config::step::reauth_confirm::data_description::api_key` | API-nyckeln som ger åtkomst till organisationens styrenheter. | API-nyckel som ger åtkomst till styrenheterna i din organisation. | Matchar användarflödets tydligare beskrivning. |
| `component::hortimax::config::step::user::data_description::api_key` | API-nyckel som ger åtkomst till styrenheterna i din organisation. | API-nyckel som ger åtkomst till styrenheterna i din organisation. | Användarflödet behölls; den återautentiserade formuleringen synkades till det. |
| `component::myneomitis::config::step::reauth_confirm::data_description::password` | Lösenordet för ditt MyNeomitis-konto. | Lösenordet för ditt MyNeomitis-konto | Tar bort interpunktion som saknas i återanvänt mål. |
| `component::cielo_home::config::step::reauth_confirm::data_description::api_key` | API-nyckeln från ditt Cielo Home-konto. | API-nyckeln från ditt Cielo Home-konto | Matchar användarflödets text och interpunktion. |

`common::config_flow::error::cannot_connect`, `common::config_flow::abort::already_configured_device` och det gemensamma reautentiseringsmålet behölls där de redan var korrekta.

## Livevärden som ändrats sedan den gamla rapporten

Femton måltexter avvek från ögonblicksbilden. De kontrollerades mot aktuell källtext och sitt sammanhang; de är nu synkade i minnet:

- `component::assist_satellite::exceptions::tts_engine_not_found::message`: ”Text-till-tal-motorn {engine} hittades inte.” använder korrekt svensk sammansättning.
- `component::ai_task::exceptions::generate_image_not_supported::message`, `...::generate_data_not_supported::message`, `...::evaluate_not_supported::message`, `...::entity_not_found::message` och `...::attachments_not_supported::message`: ”AI-uppgiftsentiteten” är begriplig svenskare än det engelska produktuttrycket i äldre rapport.
- `component::sofar::config::step::reconfigure::menu_options::reconfigure_tcp` och `...::reconfigure_serial`: nuvarande `Modbus TCP` och `Seriell port (Modbus RTU)` matchar de upplösta referenserna.
- `component::epion::config::step::reauth_confirm::description`: `Epion-API-nyckel` följer svensk sammansättning.
- `component::ai_task::services::evaluate::fields::questions::description`: behåll `noul`, `choice` och `score` som källans bokstavliga schemaenum. Kontrollerat mot `evaluation.py`, där `noul` är det faktiskt accepterade literalvärdet; det är inte ett stavfel att översätta.
- `component::hortimax::config::step::reauth_confirm::description`: `HortOS-API:t` följer svensk sammansättning.
- `component::cielo_home::config::step::reauth_confirm::title`: uppdaterad till gemensam reautentiseringstext.
- `component::unifi::exceptions::unload_failed::message`, `component::broadlink::exceptions::unload_failed::message` och `component::hue::exceptions::unload_failed::message`: ”koppla från” återger `unload` i dessa integrationers avregistrerings-/frånkopplingskontext bättre än äldre ”avläsa”.

## Verifiering och minne

Samtliga 55 uppföljda referenspar jämfördes via Lokalise API efter rättningar; ingen avvikelse återstår. 240 rapportnycklar och deras externa referensmål synkades med käll-ID, mål-ID och granskningsstatus till Home Assistant Core-snapshoten. Inga nycklar i dessa 240 har en tom svensk form med ifylld engelsk motsvarighet.

PO och TMX genererades från samma JSONL-snapshot och validerades: 75 556 nycklar, 75 558 segment och 42 646 unika språkpar i Core-minnet. svlang gav naturlighetssignalen 10/10 för ändringsurvalet. hunspell-sv flaggade `Wi-Fi-ikonen` och produktnamnen `NYT`/`NYT-S`; dessa kontrollerades manuellt och behölls som korrekt fack-/produktstavning. Referenser, enumnamn och platshållare kontrollerades separat mot källkod. Fullständig Core-granskning pågår fortfarande.
