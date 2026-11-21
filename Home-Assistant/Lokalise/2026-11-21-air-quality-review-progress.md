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

## Status

Täcknings-, tomvärdes- och identitetskontroll är klar. Semantisk radgranskning av de återstående villkors- och triggertexterna fortsätter.