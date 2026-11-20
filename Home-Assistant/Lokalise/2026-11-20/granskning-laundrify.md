# Home Assistant Core – Laundrify

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/laundrify/strings.json`  
Lokalise: de två angivna ändringarna sparades och lästes tillbaka 2026-11-20.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::laundrify::entity::binary_sensor::wash_cycle::name` | `Cykel` | `Tvättcykel` | Sparad och återläst i Lokalise. Nyckeln avser tvättmaskinens programcykel; `Tvättcykel` anger rätt kontext. |
| `component::laundrify::config::step::init::data::code` | `Auth-kod (xxx-xxx)` | `Autentiseringskod (xxx-xxx)` | Sparad och återläst i Lokalise. Svenska beskrivningen använder redan `autentiseringskod`; termbanken har belägg för *Authentication Code* → *Autentiseringskod*. |

## Kontroll utan förslag

Övriga **åtta aktuella** källsträngar har kontrollerats mot Core-källan.
Referenser, formatmönstret `xxx-xxx` och den svenska texten för återautentisering
är korrekta. `svlang` godkände den fria beskrivningen.

## Historisk Lokalise-rad

`component::laundrify::config::abort::single_instance_allowed` visas i
Lokalise men saknas i aktuell `strings.json`. Den behandlas som historisk.

## TMX och Lokalise

De två sparade och återlästa värdena är införda i den kanoniska Home
Assistant-TMX:en med fullständig nyckel, källproveniens och statusen
`saved-and-read-back`.
