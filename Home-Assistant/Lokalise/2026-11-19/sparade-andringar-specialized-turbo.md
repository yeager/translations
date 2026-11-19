# Sparade ändringar för Specialized Turbo

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::specialized_turbo::entity::sensor::rider_power::name` | Rider power | Förarens kraft | Cyklistens effekt |
| `component::specialized_turbo::entity::sensor::odometer::name` | Odometer | Odometer | Vägmätare |
| `component::specialized_turbo::entity::sensor::battery_remaining_wh::name` | Battery remaining | Batteri återstår | Återstående batterienergi |

Cykelns sensorvärden får tydliga svenska namn; wattimmarsfältet avser återstående energi.

## Installation och parkoppling

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::specialized_turbo::config::step::bluetooth_confirm::title` | Discovered Specialized Turbo bike | Upptäckte Specialized Turbo-cykel | Upptäckt Specialized Turbo-cykel |
| `component::specialized_turbo::config::step::bluetooth_confirm::description` | A Specialized Turbo bike was found at {address} ({name}). Pairing prompts are handled by the active Bluetooth backend. | En Specialized Turbo-cykel hittades på {address} ({name}). Parningsmeddelanden hanteras av den aktiva Bluetooth-modulen. | En Specialized Turbo-cykel hittades på {address} ({name}). Parkopplingsförfrågningar hanteras av den aktiva Bluetooth-modulen. |
| `component::specialized_turbo::config::error::key_unavailable` | The Specialized encryption key could not be retrieved. | Det gick inte att hämta den specialiserade krypteringsnyckeln. | Det gick inte att hämta krypteringsnyckeln från Specialized. |

Sparade och återlästa i Lokalise 2026-11-19. Platshållarna `{address}` och `{name}` bevarades; Specialized är ett varumärke och parkoppling är Bluetooth-terminen.
