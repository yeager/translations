# Home Assistant – Air Quality: pågående svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `air_quality`

## Aktuell täckning

- Lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Lokalise API: 237/237 exakta komponentnycklar hämtade med 20-nyckelsbatcher.
- Inga svenska mål är tomma.
- Ingen synlig källtext är identisk med svensk måltext i den automatiserade kontrollen.

Komponenten har långa nyckelnamn och kräver därför 20-nyckelsbatcher; större frågesträngar avvisas av Lokalise med HTTP 414. Detta är en API-begränsning i hämtningen, inte en översättningslucka.

## Sparade och återlästa rättningar

Sex N₂O-nycklar hade översatt `nitrous oxide` som `kväveoxid`. Korrekt svensk kemisk term är `dikväveoxid`; samtliga sex ändringar skickades via Lokalise API och lästes sedan tillbaka per översättnings-ID.

| Nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `conditions::is_n2o_value::description` | Testar kväveoxidnivån … | Testar dikväveoxidnivån … |
| `conditions::is_n2o_value::name` | Kväveoxidvärde | Dikväveoxidvärde |
| `triggers::n2o_changed::description` | … kväveoxidnivåer … | … dikväveoxidnivåer … |
| `triggers::n2o_changed::name` | Kväveoxidnivån förändrades | Dikväveoxidnivån förändrades |
| `triggers::n2o_crossed_threshold::description` | … kväveoxidnivåer … | … dikväveoxidnivåer … |
| `triggers::n2o_crossed_threshold::name` | Kväveoxidnivån har passerat … | Dikväveoxidnivån har passerat … |

## Verktygsvalidering

De tre representativa ändrade texterna validerades lokalt efter API-återläsningen: `l10n-lint --language sv --format text` rapporterade inga formatfel, `hunspell -d sv_SE` gav inga okända ord och `svlang check` gav 10,0/10 utan anmärkningar. Platshållare berörs inte av N₂O-ändringarna.


Den gemensamma nyckeln `common::trigger_behavior_description` var dessutom syntaktiskt oklar: `Det beteende som ska trigga för valda entiteter.` ersattes med `Det beteende hos de valda entiteterna som ska utlösa automatiseringen.` Den validerades med samma tre verktyg och återlästes från Lokalise som översättnings-ID `8016673893`.


I väljaren `selector::number_or_entity::choices::number` ändrades `Nummer` till `Tal`. Källans val står bredvid `Entity` och avser därför ett numeriskt värde, inte ett numrerings-ID. Ändringen validerades, sparades och återlästes som Lokalise-ID `8016674725`.


I den återanvända beteendeväljaren ändrades alternativet `Any` från `Något` till `Någon`, i linje med Home Assistants övriga motsvarande väljare och med villkorsläget (någon av de valda entiteterna). Validerad och API-återläst som Lokalise-ID `8016674789`.


## Sparad terminologigruppering: villkorsbeteende

Följande 20 nycklar ändrades från `Hur värdet ska stämma överens med de enheter som avses.` till `Hur värdet ska stämma överens för de valda entiteterna.` Den tidigare texten bröt mot projektets term `entitet` och var otydlig om vilka objekt som avses. Samma svenska text validerades med verktyg och varje sparning återlästes från Lokalise.

- `component::air_quality::common::condition_behavior_description`
- `component::air_quality::conditions::is_co2_value::fields::behavior::description`
- `component::air_quality::conditions::is_co_cleared::fields::behavior::description`
- `component::air_quality::conditions::is_co_detected::fields::behavior::description`
- `component::air_quality::conditions::is_co_value::fields::behavior::description`
- `component::air_quality::conditions::is_gas_cleared::fields::behavior::description`
- `component::air_quality::conditions::is_gas_detected::fields::behavior::description`
- `component::air_quality::conditions::is_n2o_value::fields::behavior::description`
- `component::air_quality::conditions::is_no2_value::fields::behavior::description`
- `component::air_quality::conditions::is_no_value::fields::behavior::description`
- `component::air_quality::conditions::is_ozone_value::fields::behavior::description`
- `component::air_quality::conditions::is_pm10_value::fields::behavior::description`
- `component::air_quality::conditions::is_pm1_value::fields::behavior::description`
- `component::air_quality::conditions::is_pm25_value::fields::behavior::description`
- `component::air_quality::conditions::is_pm4_value::fields::behavior::description`
- `component::air_quality::conditions::is_smoke_cleared::fields::behavior::description`
- `component::air_quality::conditions::is_smoke_detected::fields::behavior::description`
- `component::air_quality::conditions::is_so2_value::fields::behavior::description`
- `component::air_quality::conditions::is_voc_ratio_value::fields::behavior::description`
- `component::air_quality::conditions::is_voc_value::fields::behavior::description`

## Status

Täcknings-, tomvärdes- och identitetskontroll är klar. Semantisk radgranskning av de återstående villkors- och triggertexterna fortsätter.
