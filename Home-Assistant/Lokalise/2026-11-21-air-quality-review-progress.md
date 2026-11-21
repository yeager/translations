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


## Sparad terminologigruppering: triggerbeteende

20 nycklar med `The behavior of the targeted entities to trigger on.` använder nu `Det beteende hos de valda entiteterna som ska utlösa automatiseringen.` i stället för den oklara konstruktionen `Det beteende som ska trigga för valda entiteter.` Samtliga API-sparningar återlästes. Fullständiga nycklar:

- `component::air_quality::common::trigger_behavior_description`
- `component::air_quality::triggers::co2_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::co_cleared::fields::behavior::description`, `component::air_quality::triggers::co_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::co_detected::fields::behavior::description`
- `component::air_quality::triggers::gas_cleared::fields::behavior::description`, `component::air_quality::triggers::gas_detected::fields::behavior::description`, `component::air_quality::triggers::n2o_crossed_threshold::fields::behavior::description`
- `component::air_quality::triggers::no2_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::no_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::ozone_crossed_threshold::fields::behavior::description`
- `component::air_quality::triggers::pm10_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::pm1_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::pm25_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::pm4_crossed_threshold::fields::behavior::description`
- `component::air_quality::triggers::smoke_cleared::fields::behavior::description`, `component::air_quality::triggers::smoke_detected::fields::behavior::description`, `component::air_quality::triggers::so2_crossed_threshold::fields::behavior::description`
- `component::air_quality::triggers::voc_crossed_threshold::fields::behavior::description`, `component::air_quality::triggers::voc_ratio_crossed_threshold::fields::behavior::description`


## Sparad etikettgrupp: minsta varaktighet

42 Air Quality-fält med källtexten `For at least` ändrades från `I åtminstone` till `I minst`. Den gamla formuleringen var oidiomatisk; den nya är en korrekt svensk fältetikett för minsta varaktighet. `l10n-lint`, `hunspell-sv` och `svlang` godkände texten. API-sparningarna lästes tillbaka per översättnings-ID; en första batch avbröts efter 41 poster och den återstående radonnyckeln `component::air_quality::triggers::radon_crossed_threshold::fields::for::name` sparades och verifierades separat. Den spårbara 42-postersgruppen har lagts i det verifierade TM-minnet; den kanoniska TMX-valideringen passerade med 1 545 poster.


## Sparad statusgrupp: `cleared`

Källan och implementationen använder `cleared` när en binärsensor inte längre detekterar ämnet. Nio texter ändrades därför från `nollställd`/`nollställda` till `inte upptäckt` respektive `inte längre detekterar`. Berörda nycklar är `component::air_quality::triggers::{co,gas,smoke}_cleared::name`, `component::air_quality::conditions::is_{co,gas,smoke}_cleared::{name,description}`. `l10n-lint` och `hunspell-sv` passerade. `svlang` gav tre falskt positiva V2-varningar för de grammatiskt korrekta bisatserna efter `om`; de ändrades inte. Alla nio API-sparningar lästes tillbaka och har lagts till i det verifierade TM-minnet.


## Sparad genuskorrektion: rökdetektion

`component::air_quality::triggers::smoke_detected::name` och `component::air_quality::conditions::is_smoke_detected::name` ändrades från `Rök detekterat` till `Rök detekterad`. `Rök` är ett en-ord och kräver därför adjektivformen `detekterad`. Båda sparningarna validerades, återlästes och lades till i TM-minnet.


## Granskad utan ändring: PM- och VOC-gruppen

204 villkors- och triggerposter för PM1, PM2.5, PM4, PM10, VOC och VOC-kvot granskades mot aktuella `strings.json`. Beteckningar, måttenheter, tröskelvärdesterminologi och svenska sammansättningar är konsekventa. Inga säkra ändringar gjordes i denna grupp.


## Färsk export- och formatkontroll

Efter fullständig Core-export från Lokalise extraherades komponentens 570 aktuella poster. Kontroll: 0 tomma svenska mål, 0 identiska käll-/målpar och `msgfmt --check` passerade. Ett avgränsat `l10n-lint`-pass rapporterade 0 fel och 0 varningar. Två informationsnotiser avser enbart att svenska VOC-namn har tillägget `(VOC)`; de är avsiktliga och medför ingen format- eller platshållaravvikelse.


## Kompletterad N₂O-kontroll

Färsk API-export avslöjade två kvarvarande användningar av `kväveoxidnivån` i N₂O-triggerns gränshjälptexter. `component::air_quality::triggers::n2o_changed::fields::above::description` och `component::air_quality::triggers::n2o_changed::fields::below::description` använder nu `dikväveoxidnivån`. Båda är validerade, sparade, återlästa och införda i TM-minnet. `svlang` flaggade endast korrekta bisatser efter `när` som falskt positiva.


## Granskad gemensam terminologi och referensfråga

De 287 posterna för koldioxid, kolmonoxid, kväveoxider, ozon, svaveldioxid och radon har granskats mot aktuell källa. Efter N₂O-korrigeringarna behövs inga fler säkra ändringar. Gemensamma fält och väljare är också kontrollerade. `component::air_quality::selector::condition_behavior::options::any` har värdet `Något`, medan motsvarande nyckel varierar mellan `Något` och `Någon` i andra komponenter. Det saknas tillräcklig UI-kontext för att säkert välja en form; nyckeln är därför markerad för referenskontroll och lämnas oförändrad.

## Status

Den aktuella komponenten är radgranskad med full nyckeltäckning: 570/570 poster (204 PM/VOC, 287 kemi/radon, 38 gemensamma väljare och 41 binärsensor-/titelposter). Alla säkra rättningar är sparade och återlästa. En referensfråga återstår: `component::air_quality::selector::condition_behavior::options::any` (`Något`/`Någon`) kräver UI-kontext innan en eventuell ändring.
