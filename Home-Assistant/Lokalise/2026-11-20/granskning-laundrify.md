# Home Assistant Core – Laundrify

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/laundrify/strings.json`  
Lokalise: läsning av `component::laundrify`; inga skrivningar har gjorts.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::laundrify::entity::binary_sensor::wash_cycle::name` | `Cykel` | `Tvättcykel` | Nyckeln avser tvättmaskinens programcykel. `Cykel` blir tvetydigt i svensk UI-text, medan `Tvättcykel` anger rätt kontext. |
| `component::laundrify::config::step::init::data::code` | `Auth-kod (xxx-xxx)` | `Autentiseringskod (xxx-xxx)` | Svenska beskrivningen använder redan `autentiseringskod`. Termbanken har dessutom belägg för *Authentication Code* → *Autentiseringskod*. |

## Kontroll utan förslag

Övriga **åtta aktuella** källsträngar har kontrollerats mot Core-källan.
Referenser, formatmönstret `xxx-xxx` och den svenska texten för återautentisering
är korrekta. `svlang` godkände den fria beskrivningen.

## Historisk Lokalise-rad

`component::laundrify::config::abort::single_instance_allowed` visas i
Lokalise men saknas i aktuell `strings.json`. Den behandlas som historisk.

## TMX och Lokalise

Förslagen är lokala och ännu inte sparade i Lokalise. Home Assistant-TMX:en
ändras därför inte; den ska endast innehålla Lokalise-verifierade sparade
värden.
