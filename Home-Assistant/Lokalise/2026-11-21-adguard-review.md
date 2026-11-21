# Home Assistant – AdGuard: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `adguard`

## Underlag och kontroll

- Aktuell Lokalise API-data: 73/73 exakta komponentnycklar, med engelsk källa och svensk måltext.
- Aktuellt lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Äldre komponentrapport fanns inte i arkivet; inga tidigare förslag för dessa tre nycklar har därför återanvänts.
- Platshållare och formatering kontrollerades radvis. Berörd text med `{error}` ändrades inte.
- `l10n-lint --language sv`: inga anmärkningar för ändringsmängden.
- `hunspell-sv`: inga språkliga anmärkningar; produktnamnet `AdGuard Home` är en förväntad ordlisteavvikelse i sammansättningen.
- `svlang check` gav bara en osäker V2-markering för den tekniska sammansättningen `AdGuard Home-växeln`; uttrycket är grammatisk korrekt i satsen och behölls efter manuell kontroll.

## Sparade och återlästa ändringar

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::adguard::entity::sensor::safe_browsing_blocked::name` | Safe browsing blocked | Blockerade för säker surfning | Blockerade av säker surfning | `för` ändrade relationen: sensorn räknar objekt som blockerats *av* funktionen. |
| `component::adguard::exceptions::error_while_turn_off::message` | An error occurred while turning off AdGuard Home switch. | Ett fel inträffade när AdGuard Home stängdes av. | Ett fel inträffade när AdGuard Home-växeln stängdes av. | Källans `switch` saknades i målet. |
| `component::adguard::exceptions::error_while_turn_on::message` | An error occurred while turning on AdGuard Home switch. | Ett fel uppstod när AdGuard Home skulle slås på. | Ett fel uppstod när AdGuard Home-växeln skulle slås på. | Källans `switch` saknades i målet. |

Alla tre poster skickades via Lokalise API och hämtades igen från API:t efter uppdateringen. Inga osparade lokala översättningsförslag återstår i denna komponent.

## Översättningsminne

De tre API-återlästa ändringarna är tillagda i `swedish-tm` med Lokalise-nyckel- och översättnings-ID, API-återläsning och datum. Den kanoniska Home Assistant-TMX:en validerades efter tillägget: 1 395 poster, 1 164 med Lokalise-ID.