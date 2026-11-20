# Home Assistant Core – Lokalise-granskning, sida 603

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`elkm1`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::elkm1::services::sensor_zone_trigger::description` | `Utlösande zon.` | `Utlöser zonen.` | Beskrivningen ska vara ett verb, inte ett substantiv. |
| `component::elkm1::services::sensor_zone_trigger::name` | `Utlösande sensorzon` | `Utlös sensorzon` | Tjänstens namn ska ha åtgärdsform. |
| `component::elkm1::services::speak_phrase::description` | `Talar en fras. Se listan över fraser i Elk-M1 ASCII-protokollets dokumentation.` | `Läser upp en fras. Se listan över fraser i dokumentationen för Elk-M1:s ASCII-protokoll.` | Naturligare uttryck och korrekt genitiv. |
| `component::elkm1::services::speak_phrase::fields::number::description` | `Frasnummer att tala.` | `Frasnummer som ska läsas upp.` | Korrekt svenskt verbbruk. |
| `component::elkm1::services::speak_phrase::name` | `Tala fras` | `Läs upp fras` | Naturlig åtgärdsform. |
| `component::elkm1::services::speak_word::description` | `Talar ett ord. Se listan över ord i dokumentationen för Elk-M1 ASCII Protocol.` | `Läser upp ett ord. Se listan över ord i dokumentationen för Elk-M1:s ASCII-protokoll.` | Naturligare uttryck och översatt protokollterm. |
| `component::elkm1::services::speak_word::fields::number::description` | `Ordnummer att tala.` | `Ordnummer som ska läsas upp.` | Korrekt svenskt verbbruk. |

## Verifiering

Samtliga sju ändringar skickades med Lokalise API och återlästes. Referensen för `prefix` är korrekt; resterande 12 strängar behövde ingen ändring.

Status: sparat och återläst i Lokalise.
