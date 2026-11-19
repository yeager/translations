# Sparade SmartThings-översättningar

Sparade och återlästa i Lokalise den 19 november 2026 efter användarens instruktion.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::smartthings::entity::select::spin_level::state::rinse_hold` | Rinse hold | Skölj väntande | Sköljstopp |
| `component::smartthings::entity::select::spin_level::state::delicate` | Delicate | Skonsamt | Skonsam centrifugering |

Båda valen hör till centrifugeringsnivån. Källtext och befintlig svenska kontrollerades före sparning mot tidigare granskningsunderlag.

## Tvättmaskinens smutsgrad

Sparade och återlästa i Lokalise den 19 november 2026. SmartThings-koden kopplar inställningen till tvättmaskinens smutsgrad.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::smartthings::entity::select::soil_level::state::heavy` | Heavy | Tung | Kraftig |
| `component::smartthings::entity::select::soil_level::state::extra_heavy` | Extra heavy | Extra tung | Extra kraftig |
| `component::smartthings::entity::select::soil_level::name` | Soil level | Jordnivå | Smutsgrad |

## Diskprogram

Sparade och återlästa i Lokalise 2026-11-19 efter kontroll mot diskprogrammets övriga alternativ.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::smartthings::entity::select::dishwasher_washing_course::state::rinse_only` | Rinse only | Skölj endast | Endast sköljning |
| `component::smartthings::entity::select::dishwasher_washing_course::state::rinse_dry` | Rinse dry | Skölj torrt | Sköljning och torkning |
| `component::smartthings::entity::select::dishwasher_washing_course::state::night_silence` | Night silence | Natt tyst | Tyst nattprogram |
| `component::smartthings::entity::select::dishwasher_washing_course::state::daily` | Daily | Daglig | Dagligt |

Programnamnen beskriver sköljning, torkning och tyst nattdrift; dagligt böjs efter program.

## Diskprogrammets fältnamn

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::smartthings::entity::select::dishwasher_washing_course::name` | Cycle | Cykel | Diskprogram |

Sparad och återläst i Lokalise 2026-11-19. Kontexten är val av diskmaskinens program.

## AirDresser: Keep Fresh

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::smartthings::entity::switch::keep_fresh_mode::name` | Keep fresh mode | Håll-färskt-läge | Keep Fresh-läge |
| `component::smartthings::entity::binary_sensor::keep_fresh_mode_active::name` | Keep fresh mode active | Håll-färskt-läge aktivt | Keep Fresh-läge aktivt |

Sparade och återlästa i Lokalise den 19 november 2026. [Samsungs svenska produktsida](https://www.samsung.com/se/washers-and-dryers/airdresser/df5000cm-dryer-dual-airwash-dual-jetsteam-ai-dry-silver-df18cb8700cre1/) använder funktionsnamnet Keep Fresh. [Samsungs beskrivning](https://www.samsung.com/au/support/home-appliances/airdresser-care-recipe/) anger att funktionen håller kläderna fräscha efter programmets slut. Detta ersätter det preliminära förslaget i `granskning-smartthings-angskap-2026-11-19.md`.
