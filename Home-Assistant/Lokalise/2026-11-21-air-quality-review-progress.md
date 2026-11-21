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

## Status

Täcknings-, tomvärdes- och identitetskontroll är klar. Semantisk radgranskning av de 237 villkors- och triggertexterna fortsätter. Inga osäkra ändringar har skickats.