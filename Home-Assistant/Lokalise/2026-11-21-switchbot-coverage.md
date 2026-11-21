# Home Assistant – SwitchBot: täcknings- och formatkontroll

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `switchbot`

## Underlag och metod

Den aktuella engelska källfilen `homeassistant/components/switchbot/strings.json` innehåller 212 textsträngar. Fullständiga Lokalise-nycklar byggdes från den aktuella källstrukturen och hämtades sedan från Lokalise API i fyra avgränsade batcher (60 + 60 + 60 + 32).

För varje sträng kontrollerades att svensk måltext finns samt att enkla formatplatshållare av formerna `{…}` och `%n$[sd]` överensstämmer med engelskan.

## Resultat

| Kontroll | Resultat |
| --- | ---: |
| Källsträngar | 212 |
| Hittade API-nycklar | 212 |
| Tomma svenska måltexter | 0 |
| Platshållaravvikelser | 0 |

Inga ändringar behövde skickas in för denna täckningskontroll.

## Avgränsning

Detta är en kontroll av aktuell täckning och grundläggande formatintegritet, inte en deklaration om att samtliga 212 strängar redan är fullständigt språkligt radgranskade. En fortsatt radgranskning ska jämföra varje enskild svensk formulering med aktuell engelsk källa, tidigare rapporter och etablerad svensk FOSS-terminologi.
