# HA Core: korrigerade återanvända referenstexter

Datum: 2026-11-24. Kontroll mot Home Assistant Core commit `2fdaa177f3e94535b3b649fb1ffc2dbba52eb4ce` och livevärden i Lokalise. Alla ändringar nedan sparades via API och återlästes. De ingår nu som `reviewed-saved` i Home Assistant-minnet.

## Sparade ändringar

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Skäl |
| --- | --- | --- | --- |
| `component::openai_conversation::config_subentries::conversation::abort::entry_not_loaded` | Det går inte att lägga till saker när konfigurationen är inaktiverad. | Det går inte att lägga till något när konfigurationen är inaktiverad. | Mer idiomatisk svensk återanvändbar feltext; de två rapporterade konsumenterna matchar nu referensmålet. |
| `component::haven_iaq::config::error::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Återanvänds som gemensam feltext; tog bort slutpunkten så konsumenten matchar exakt källreferensen. |
| `component::haven_iaq::config::abort::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Samma referensmål och samma interpunktion som den gemensamma feltexten. |
| `component::haven_iaq::config::abort::already_in_progress` | Konfiguration pågår redan. Slutför den befintliga konfigurationen innan du börjar om. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Samma text som den gemensamma referensen; bevarar villkoret att befintlig konfiguration måste slutföras först. |
| `component::electrasmart::config::step::reauth_confirm::title` | Autentiseringen har upphört för {name} | Autentiseringen har upphört att gälla för {name} | Matchar det återanvända reautentiseringsmålet och bevarar `{name}`. |
| `component::hr_energy_qube::entity::sensor::status_heatpump::state::anti_legionella` | Antilegionella | Anti-legionella | Matchar det namngivna binärsensormålet och svensk HA-terminologi för samma funktion. |
| `component::shelly::issues::ir_raw_receive_disabled::fix_flow::abort::issue_ignored` | Problemet ignorerades | Problemet ignorerat | Matchar det återanvända Shelly-meddelandet ordagrant. |
| `component::shelly::issues::ir_raw_receive_disabled::fix_flow::abort::cannot_connect` | Det gick inte att ansluta. | Det gick inte att ansluta | Matchar den gemensamma felreferensen, utan extra skiljetecken. |
| `component::opengarage::entity::light::light::name` | Belysning | Lampa | Källan använder Home Assistants gemensamma `light`-titel; måltermen är ”Lampa”. |

Hydrawise-konsumenten `component::hydrawise::config::step::reconfigure::data_description::api_key` (`958394137`) korrigerades också i den separata [Open-Meteo/Hydrawise-referensrapporten](2026-11-24-referenskontroll-openmeteo-hydrawise.md) till samma text som det explicita användarflödesmålet.

## Uppföljningskontroll

Återhämtade alla 28 referensuppföljningar som markerats i rapportserien 6061–6300. Jämförde aktuella engelska och svenska texter för varje konsument mot aktuellt referensmål i Lokalise. Efter ändringarna återstår **0 av 28** oöverensstämmande referenspar. Bland de verifierade målen finns gemensamma fältnamn, anslutnings- och konfigurationsfel, OpenAI:s återanvända avbrottstext, Anthropic-modellens reparationsflöde och Home Assistants `light`-titel.

Språkkontrollerna gav inga stavningsflaggor för de nya formuleringarna i hunspell-sv. svlang gav naturlighetssignalen 10/10 för den samlade batchen; en platshållare som analyserades fristående flaggades som ovanlig, så `{name}` har validerats separat som oförändrad från källan. Befintliga `Antilegionellafunktion`/`Anti-legionella`-poster i Home Assistant-minnet kontrollerades som terminologistöd.

De 32 berörda nycklarna synkades till Home Assistant Core-minnets snapshot, PO och TMX. Strukturer kontrollerade: 75 556 JSONL-poster, 75 556 PO-poster och välformad TMX XML. Granskningen av andra Core-nycklar och resterande batcher fortsätter; detta är inte ett färdigbesked för Core.
