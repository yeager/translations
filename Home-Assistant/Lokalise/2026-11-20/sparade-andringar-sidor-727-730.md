# Home Assistant Core – sparade ändringar, sidor 727–730

Datum: 2026-11-20. Källprojekt: Lokalise Home Assistant Core (sv). Varje nedanstående sparad text återlästes från Lokalise innan den fördes in i det kanoniska HA-TMX-minnet. TMX-posterna har Lokalise-översättnings-ID, fullständig nyckel, engelskt källsegment och statusen `saved-and-read-back`.

## Sida 727

| Fullständig nyckel | Före | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::homematicip_cloud::services::deactivate_eco_mode::name` | Inaktivera ekoläge | Inaktivera ekoläget | Bestämd form i åtgärdsrubrik. |
| `component::homematicip_cloud::services::deactivate_vacation::name` | Inaktivera semesterläge | Inaktivera semesterläget | Bestämd form i åtgärdsrubrik. |
| `component::homematicip_cloud::services::dump_hap_config::description` | Ladda ner konfigurationen av Homematics IP-accesspunkt(er). | Exporterar konfigurationen för Homematic IP-accesspunkterna. | Korrekt produktnamn/genitiv och åtgärdsinnebörd. |
| `component::homematicip_cloud::services::dump_hap_config::fields::config_output_path::description` | Standardvärde är config-katalogen för din Home Assistant-server. | Standardvärdet är Home Assistant-konfigurationskatalogen. | Svensk, konsekvent katalogterm. |
| `component::homematicip_cloud::services::dump_hap_config::name` | Ladda ner HAP-konfiguration | Exportera HAP-konfiguration | Samma innebörd som exportåtgärden. |
| `component::homematicip_cloud::services::reset_energy_counter::fields::entity_id::description` | Använd "all" … | Använd nyckelordet 'all' … | Kodvärdet markeras och förklaras som nyckelord. |
| `component::homematicip_cloud::services::set_active_climate_profile::description` | Ställer in index för aktiv klimatprofil. | Ställer in den aktiva klimatprofilens index. | Tydlig ägarkonstruktion. |

## Sida 728

| Fullständig nyckel | Före | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::homematicip_cloud::services::set_active_climate_profile::fields::climate_profile_index::name` | Index för klimatprofil | Klimatprofilsindex | Kompakt och etablerad sammansättning. |
| `component::html5::services::dismiss::fields::data::description` | Utökad information om avisering. | Utökad information om aviseringen. | Bestämd form. |
| `component::html5::services::dismiss::fields::target::description` | En array med mål. | En matris med mål. | Svensk teknisk term. |
| `component::huawei_lte::services::resume_integration::description` | Återupptar avbruten integration | Återupptar den pausade integrationen. | Konsekvent med suspend-/pause-åtgärden. |
| `component::huawei_lte::services::suspend_integration::fields::url::description` | … ska avbrytas. | … ska pausas. | Samma livscykelterm som källans suspend. |
| `component::huawei_lte::services::suspend_integration::name` | Avbryt integration | Pausa integration | Konsekvent åtgärdsnamn. |

## Sida 729

| Fullständig nyckel | Före | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::hue::services::activate_scene::fields::speed::description` | Hastighet för dynamisk palett för den här scenen. | Hastighet för den dynamiska paletten i den här scenen. | Naturligare svensk ordföljd. |
| `component::hue::services::hue_activate_scene::description` | … lagrats i hue-hubben. | Aktiverar en Hue-scen som lagrats i Hue-bryggan. | Produktnamn och svensk enhetsterm. |
| `component::hue::services::hue_activate_scene::fields::group_name::description` | Namn på grupp/rum från Hue-appen. | Namn på Hue-gruppen eller Hue-rummet i Hue-appen. | Tydligare omfattning och konsekvent varumärkesskrivning. |
| `component::hue::services::hue_activate_scene::fields::scene_name::description` | Namn på scen från hue-appen. | Namn på Hue-scenen i Hue-appen. | Produktnamn och bestämd form. |
| `component::conversation::services::process::fields::agent_id::description` | Konversationsagent för att behandla din förfrågan. | Den konversationsagent som ska behandla din förfrågan. | Fullständig svensk nominalfras. |

## Sida 730

| Fullständig nyckel | Före | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::date::services::set_value::description` | Anger värdet för ett datum. | Ställer in värdet för en datumentitet. | Åtgärden arbetar på en datumentitet. |
| `component::datetime::services::set_value::description` | Anger värdet för datum/tid. | Ställer in värdet för en datum-/tidentitet. | Konsekvent med datumåtgärden. |
| `component::datetime::services::set_value::fields::datetime::description` | Tidszonen … antas. | Tidszonen för Home Assistant-instansen används. | Tydligare funktionell betydelse. |
| `component::logbook::services::log::description` | Spårar en anpassad aktivitet. | Registrerar en anpassad aktivitet. | Loggboken registrerar händelser, den spårar inte kontinuerligt. |

## Verifiering

- Sidor 727–730: 22 nya TMX-poster vid synkning.
- Kanoniskt HA-TMX efter sida 730: 763 unika `tu`-poster och unika `tuid`-värden; XML-validering passerade.
- Referenssträngar och kodvärdet `'all'` bevarades exakt där de förekommer.
