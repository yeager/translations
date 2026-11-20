# Home Assistant Core – Medcom BLE

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/medcom_ble/strings.json`  
Lokalise: läsning av `component::medcom_ble`; inga skrivningar har gjorts.

## Osäkert ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::medcom_ble::entity::sensor::cpm::name` | `Antal per minut` | `Räkningar per minut` | CPM avser antal registrerade räkningar per tidsenhet. Förslaget är den mer specifika svenska mätbenämningen, men bör jämföras med produktens egen svenska dokumentation före eventuell sparning. |

Varken Home Assistant-minnet eller terminologiverktyget gav en direkt tidigare
träff för *Counts per minute*. Förslaget är därför uttryckligen osäkert och
inte underlag för en global termregel.

## Kontroll utan förslag

Övriga **åtta aktuella** källsträngar är kontrollerade mot Core-källan.
Bluetooth-referenserna, `{name}` och de gemensamma konfigurationsreferenserna
är intakta. `svlang` och Hunspell accepterar både befintlig och föreslagen
svensk term.

## Historisk Lokalise-rad

`component::medcom_ble::config::abort::already_in_progress` visas i Lokalise
men saknas i aktuell `strings.json`. Den behandlas som historisk.

## TMX och Lokalise

Förslaget är lokalt och ännu inte sparat i Lokalise. Home Assistant-TMX:en
ändras därför inte.
