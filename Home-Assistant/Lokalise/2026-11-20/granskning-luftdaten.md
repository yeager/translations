# Home Assistant Core – Luftdaten

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/luftdaten/strings.json`  
Lokalise: läsning av `component::luftdaten`; inga skrivningar har gjorts.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::luftdaten::config::error::invalid_sensor` | `Sensor är inte tillgänglig eller ogiltig` | `Sensorn är inte tillgänglig eller är ogiltig` | Den befintliga texten saknar bestämd form och andra predikatet. Förslaget är en komplett och naturlig svensk feltext. |

## Kontroll utan förslag

Övriga **nio aktuella** källsträngar är kontrollerade mot Core-källan.
Referenser, `Sensor-ID`, `Visa på karta`, `Lufttryck vid havsytan` och de tre
Sensor.Community-felen är korrekta. `svlang` godkände det föreslagna
felmeddelandet. Hunspell-träffen för `Sensor.Community-tjänsten` är ett
produktnamnssammansättningsfall och inte ett ordlistedefekt.

## TMX och Lokalise

Förslaget är lokalt och ännu inte sparat i Lokalise. Home Assistant-TMX:en
ändras därför inte.
