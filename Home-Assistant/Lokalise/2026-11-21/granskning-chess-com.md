# Home Assistant Core – Chess.com

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`, `homeassistant/components/chess_com/strings.json`, tidigare förslag från 2026-11-19 och direkt återläsning via Lokalise API.

## Omfattning och verifiering

Alla 50 aktuella Chess.com-nycklar har jämförts med källan och lästs direkt från Lokalise. 32 språkpar ändrades (29 explicita API-skrivningar och 3 refererande enhetsnycklar som uppdaterades med den kanoniska enhetsreferensen) och lästes tillbaka. Platshållaren `{error}` samt produktnamnet `Chess.com` lämnades oförändrade.

## Sparade korrigeringar

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::chess_com::entity::sensor::chess_daily_rating::name` | Daglig schack-rating | Rating i dagsschack | Avser spelformen Daily Chess, inte frekvensen dagligen. |
| `component::chess_com::entity::sensor::chess_bullet_draw::name` | Totalt antal oavgjorda spel i bulletschack | Totalt antal oavgjorda bulletpartier | Schackspel uttrycks som partier. |
| `component::chess_com::entity::sensor::chess_bullet_lost::name` | Totalt antal förlorade spel i bulletschack | Totalt antal förlorade bulletpartier | Schackspel uttrycks som partier. |
| `component::chess_com::entity::sensor::chess_bullet_won::name` | Totalt antal vunna spel i bulletschack | Totalt antal vunna bulletpartier | Schackspel uttrycks som partier. |
| `component::chess_com::entity::sensor::chess_daily_draw::name` | Totalt antal oavgjorda spel i schack | Totalt antal oavgjorda dagsschackpartier | Återger spelformen Daily Chess. |
| `component::chess_com::entity::sensor::chess_daily_lost::name` | Totalt antal förlorade spel i schack | Totalt antal förlorade dagsschackpartier | Återger spelformen Daily Chess. |
| `component::chess_com::entity::sensor::chess_daily_won::name` | Totalt antal vunna spel i schack | Totalt antal vunna dagsschackpartier | Återger spelformen Daily Chess. |
| `component::chess_com::entity::sensor::chess_rapid_draw::name` | Totalt antal oavgjorda spel i snabbschack | Totalt antal oavgjorda snabbschackpartier | Schackspel uttrycks som partier. |
| `component::chess_com::entity::sensor::chess_rapid_lost::name` | Totalt antal förlorade spel i snabbschack | Totalt antal förlorade snabbschackpartier | Schackspel uttrycks som partier. |
| `component::chess_com::entity::sensor::chess_rapid_won::name` | Totalt antal vunna spel i snabbschack | Totalt antal vunna snabbschackpartier | Schackspel uttrycks som partier. |
| `component::chess_com::entity::sensor::chess960_daily_draw::name` | Totalt antal dragna Chess960-partier per dag | Totalt antal oavgjorda Chess960-partier i dagsschack | `drawn` är oavgjorda; Daily är spelform, inte tidsadverbial. |
| `component::chess_com::entity::sensor::chess960_daily_lost::name` | Totalt antal förlorade Chess960-partier per dag | Totalt antal förlorade Chess960-partier i dagsschack | Daily är spelform, inte tidsadverbial. |
| `component::chess_com::entity::sensor::chess960_daily_won::name` | Totalt antal vunna Chess960-partier per dag | Totalt antal vunna Chess960-partier i dagsschack | Daily är spelform, inte tidsadverbial. |
| `component::chess_com::entity::sensor::chess960_daily_rating::name` | Daglig Chess960-rating | Rating i dagsschack med Chess960 | Avser spelformen Daily Chess. |

Följande 18 enhetsnycklar hade **spel** och sparades som **partier**. De återlästes direkt efter API-skrivningen; de tre snabbschacknycklarna följer den kanoniska referensen och verifierades efter uppdateringen.

- `component::chess_com::entity::sensor::total_daily_draw::unit_of_measurement`
- `component::chess_com::entity::sensor::total_daily_lost::unit_of_measurement`
- `component::chess_com::entity::sensor::total_daily_won::unit_of_measurement`
- `component::chess_com::entity::sensor::chess960_daily_draw::unit_of_measurement`
- `component::chess_com::entity::sensor::chess960_daily_lost::unit_of_measurement`
- `component::chess_com::entity::sensor::chess960_daily_won::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_blitz_draw::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_blitz_lost::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_blitz_won::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_bullet_draw::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_bullet_lost::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_bullet_won::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_daily_draw::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_daily_lost::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_daily_won::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_rapid_draw::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_rapid_lost::unit_of_measurement`
- `component::chess_com::entity::sensor::chess_rapid_won::unit_of_measurement`

## Översättningsminne

De 32 direktverifierade språkparen finns i `swedish-tm`-manifestet `2026-11-21-chess-com-verified.json` och har lagts till i den kanoniska Home Assistant-TMX-filen. TMX-valideraren godkände efter uppdateringen 1 958 poster.
