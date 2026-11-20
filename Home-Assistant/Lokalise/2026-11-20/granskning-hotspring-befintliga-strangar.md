# Home Assistant Core – HotSpring: befintliga svenska strängar

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge. Den breda komponentfrågan returnerar som mest 30 rader; den omfattade nio redan dokumenterade tomma sensorsrader och de 21 befintliga översättningarna nedan. Den publika Core-källan i commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12` saknar ännu HotSpring-källtexterna, så den engelska Lokalise-texten är det aktuella källunderlaget och eventuella ändringar ska återkontrolleras när koden publiceras.

## Tydligt ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::hotspring::exceptions::wrong_device::message` | Enheten på den angivna värden har MAC-adressen `{found}`, inte `{expected}`. | Enheten på den konfigurerade värden har MAC-adressen `{found}`, inte `{expected}`. | Källan säger *configured host*, inte *entered host*. Båda platshållarna bevaras. |

## Bedömda utan ändringsförslag

| Fullständig nyckel | Befintlig svenska | Bedömning |
| --- | --- | --- |
| `component::hotspring::exceptions::timeout::message` | Tidsgränsen överskreds vid kommunikation med Hot Spring-API:t. | Korrekt och idiomatisk. |
| `component::hotspring::exceptions::spa_not_connected::message` | Spabadet är inte anslutet till sin Hot Spring-hemnätverksadapter (HNA). | Godtagbar produktterm; återkontrollera mot publicerad komponentdokumentation. |
| `component::hotspring::entity::sensor::freshwater_iq_sensor_life::name` | Sensorlivslängd | Korrekt sensorbenämning. |
| `component::hotspring::entity::sensor::freshwater_iq_orp::name` | Oxidations-reduktionspotential | Korrekt fackterm. |
| `component::hotspring::entity::sensor::freshwater_iq_chlorine::name` | Klor | Korrekt. |
| `component::hotspring::entity::number::salt_output_level::name` | Saltproduktionsnivå | Korrekt. |
| `component::hotspring::entity::select::jet::state::off` | Av | Korrekt referensupplösning. |
| `component::hotspring::entity::select::jet::state::low` | Låg | Korrekt referensupplösning. |
| `component::hotspring::entity::select::jet::state::high` | Hög | Korrekt referensupplösning. |
| `component::hotspring::entity::select::jet::name` | Stråle `{jet}` | Rimlig svensk benämning; platshållaren bevarad. |
| `component::hotspring::entity::select::heating_mode::state::heat_with_boost` | Värme med boost | Behåll tills produkttermen *boost* kan verifieras i HotSpring-kontext. |
| `component::hotspring::entity::select::heating_mode::state::heat_saver` | Värmesparläge | Korrekt. |
| `component::hotspring::entity::select::heating_mode::state::chill` | Kylning | Korrekt. |
| `component::hotspring::entity::select::heating_mode::state::auto_with_boost` | Automatiskt med boost | Behåll tills produkttermen *boost* kan verifieras i HotSpring-kontext. |
| `component::hotspring::entity::select::heating_mode::state::auto_saver` | Automatisk sparfunktion | Korrekt. |
| `component::hotspring::entity::select::heating_mode::name` | Uppvärmningsläge | Korrekt. |
| `component::hotspring::config::error::sna_device` | Den angivna adressen hör till Spa-nätverksadaptern (SNA). Ange istället IP-adressen eller värdnamnet för din hemnätverksadapter (HNA). | Godtagbar; `istället` kan vid senare stilharmonisering vägas mot `i stället`, men saknar här tillräcklig anledning för ändring. |
| `component::hotspring::config::abort::sna_device` | Den upptäckta enheten är en Spa-nätverksadapter (SNA). Endast hemnätverksadaptern (HNA) kan konfigureras. | Korrekt. |
| `component::hotspring::entity::light::light_zone::name` | Ljuszon `{zone}` | Korrekt; platshållaren bevarad. |
| `component::hotspring::entity::binary_sensor::spa_connected::name` | Spa anslutet | Korrekt kort sensorstatus. |

## Kontrollgräns

Lokalise begränsade den breda komponentfrågan till 30 rader. Komponentens återstående nycklar måste därför sökas i smalare grupper innan HotSpring kan markeras som fullständigt granskat. Ingen Lokalise-skrivning är utförd.

`svlang skrivregler` fann inga fel i det föreslagna felmeddelandet och Hunspell accepterar de kontrollerade orden `konfigurerade` och `värden`.

## Konfigurationsflöde

Den smalare Lokalise-sökningen `component::hotspring::config` visade ytterligare 11 rader. Referensnycklarna och de redan granskade SNA/HNA-meddelandena behålls. Följande två har konkreta förslag:

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::hotspring::config::step::user::description` | Konfigurera din Hot Spring hemnätverksadapter (HNA) för att integrera med Home Assistant. | Konfigurera din Hot Spring-hemnätverksadapter (HNA) för att integrera den med Home Assistant. | Bindestreck gör produktnamnssammansättningen konsekvent; *den* ger verbet ett tydligt objekt. |
| `component::hotspring::config::step::user::data_description::host` | Värdnamn eller IP-adress för din Hot Spring hemnätverksadapter (HNA). | Värdnamn eller IP-adress för din Hot Spring-hemnätverksadapter (HNA). | Konsekvent produktnamnssammansättning. |

Övriga config-rader—inklusive `{name}`-platshållaren och referenserna till gemensamma config-flow-nycklar—är korrekta som de står. `svlang skrivregler` fann inga fel i den längre föreslagna beskrivningen och Hunspell accepterar `hemnätverksadapter`, `värdnamn` och `konfigurera`. HotSpring-källan ska ändå återkontrolleras när den finns i den publika Core-koden, före ett eventuellt sparbeslut.

## Entiteter

Lokalise-sökningar för varje entitetstyp täcker 2 binärsensorer, 1 lampa, 2 talvärden, 10 val och 19 sensorer. De nio tomma sensorsraderna är redan dokumenterade i den separata rapporten om nya strängar. De återstående befintliga svenska värdena bedöms som korrekta:

- `component::hotspring::entity::binary_sensor::heating::name` har `Värmer`. Home Assistant-minnet innehåller flera binärsensorer med samma källtext och just denna svenska processform; den behålls i stället för det mindre kontextspecifika substantivet `Uppvärmning`.
- `Måltemperatur`, `Saltvärde`, `Saltpatronens ålder`, `Timer för kontroll av salt efter 10 dagar`, `Aktuell temperatur` och `Styrenhetens version` är korrekta sensor- eller talvärdesetiketter.
- `Wi-Fi-dongelversion` och `FreshWater Salt System-version` bevarar produktnamn och svensk sammansättning. `Ljuszon {zone}` och `Stråle {jet}` bevarar respektive platshållare.
- Referensbaserade val (`Av`, `Låg`, `Hög`) och uppvärmningslägena behålls. De engelska produktlägena med `boost` är fortsatt markerade som produkttermsberoende, inte som automatiska ändringar.

Detta ger inga ytterligare ändringsförslag för befintliga HotSpring-entiteter. Hunspell accepterar `uppvärmning` och `värmer`; `svlang` bedömer `Uppvärmning` som ett naturligt enordsuttryck.
