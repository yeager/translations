# Home Assistant – SwitchBot: täcknings- och formatkontroll

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `switchbot`

## Underlag och metod

Den aktuella engelska källfilen `homeassistant/components/switchbot/strings.json` innehåller 212 textsträngar. Fullständiga Lokalise-nycklar byggdes från den aktuella källstrukturen och hämtades sedan från Lokalise API i fyra avgränsade batcher (60 + 60 + 60 + 32).

För varje sträng kontrollerades att svensk måltext finns samt att enkla formatplatshållare av formerna `{…}` och `%n$[sd]` överensstämmer med engelskan. Den samlade aktuella svenska måltexten kördes också genom `svlang check`, `hunspell-sv` och `l10n-lint` med engelskan som referens. Verktygsträffar bedömdes i sitt sammanhang; tekniska identifierare, produktnamn och sammansättningar är inte automatiska fel.

## Resultat

| Kontroll | Resultat |
| --- | ---: |
| Källsträngar | 212 |
| Hittade API-nycklar | 212 |
| Tomma svenska måltexter | 0 |
| Platshållaravvikelser | 0 |
| l10n-lint-fel | 0 |

## Insända ändringar

| Fullständig nyckel | Befintlig text | Sparad svensk text | Motivering |
| --- | --- | --- | --- |
| `component::switchbot::config::step::encrypted_choose_method::menu_options::encrypted_auth` | Switchbot-konto (rekommenderas) | SwitchBot-konto (rekommenderas) | Korrekt versalisering av produktnamnet SwitchBot. |
| `component::switchbot::config::step::encrypted_key::data::encryption_key` | Krypteringnyckel | Krypteringsnyckel | Korrekt svensk sammansättning; jämför etablerad FOSS-term. |

Båda ändringarna är sparade och lästa tillbaka från Lokalise API. `svlang` markerade bland annat produktnamn, tekniska fältnamn och långa sammanslagna etiketter; inga ytterligare automatiska träffar bedömdes som säkra ändringar utan en mer detaljerad radgranskning.

## Avgränsning

Detta är en kontroll av aktuell täckning, grundläggande formatintegritet och verktygssignaler, inte en deklaration om att samtliga 212 strängar redan är fullständigt språkligt radgranskade. En fortsatt radgranskning ska jämföra varje enskild svensk formulering med aktuell engelsk källa, tidigare rapporter och etablerad svensk FOSS-terminologi.
