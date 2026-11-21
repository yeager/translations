# Home Assistant – Brottsplatskartan: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `brottsplatskartan`

## Underlag och kontroll

Aktuell engelska kontrollerades både i `homeassistant/components/brottsplatskartan/strings.json` och via Lokalise API. Komponenten har fem strängar. Två är delade referenser; deras upplösta värden kontrollerades, men referensstrukturen ändrades inte.

`svlang check`, `hunspell-sv`, `swedish-foss-terminology` och `swedish-tm` användes som underlag. Hunspell gav inga stavningsträffar. Svlang markerade imperativet “Placera” som en möjlig V2-avvikelse; det är en falsk positiv och ingen ändring av ordföljden behövs.

## Radvis resultat

| Fullständig nyckel | Engelska | Befintlig svenska | Åtgärd / motivering |
| --- | --- | --- | --- |
| `component::brottsplatskartan::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Behåll. Delad referens, korrekt upplöst måltext. |
| `component::brottsplatskartan::config::step::user::data::area` | Area | Område | Behåll. Stöds av termbankens kontextoberoende träff för “Area”. |
| `component::brottsplatskartan::config::step::user::data::location` | Location | Plats | Behåll. Delad referens; “plats” stöds av FOSS-termbanken. |
| `component::brottsplatskartan::config::step::user::data_description::area` | If area is selected, any marked location is ignored | Om område väljs ignoreras alla markerade platser | Sparad som **Om ett område väljs ignoreras alla markerade platser.** Fullständig och naturlig villkorssats. |
| `component::brottsplatskartan::config::step::user::data_description::location` | Put marker on location to cover within 5km radius | Placera markören på platsen för att täcka inom en radie på 5 km | Sparad som **Placera markören på platsen för att täcka ett område inom en radie på 5 km.** Det saknade objektet har lagts till och enheten har normaliserats till “5 km”. |

## Verifiering

De två ändringarna skickades via Lokalise API och lästes tillbaka efter sparandet. Inga platshållare, referenser eller pluralformer påverkades.