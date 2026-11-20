# Home Assistant Core – Private BLE Device

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/private_ble_device/strings.json`  
Lokalise: läsning av `component::private_ble_device`; inga skrivningar har gjorts.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::private_ble_device::config::step::user::description` | `Den IRK-nyckel (Identity Resolving Key) för den BLE-enhet som du vill spåra.` | `Vad är IRK-nyckeln (Identity Resolving Key) för BLE-enheten som du vill spåra?` | Källan är en fråga. Befintlig svenska är ett ofullständigt nominalt fragment; förslaget ger en fullständig och naturlig fråga. |
| `component::private_ble_device::config::error::irk_not_found` | `Den IRK som tillhandahålls matchar inte några BLE-enheter som Home Assistant kan se.` | `Den angivna IRK:n matchar inte någon BLE-enhet som Home Assistant kan se.` | Förslaget ersätter en onödigt passiv omskrivning med etablerad svensk böjning av förkortningen och gör mängdangivelsen idiomatisk. |

## Kontroll utan förslag

Övriga **sju aktuella** källsträngar är kontrollerade mot Core-källan.
`Beräknat sändningsintervall`, `Uppskattat avstånd`, `Ström`, den ogiltiga
IRK-texten, `{name}` och Bluetooth-proxytexten är korrekta i sin kontext.
`svlang` godkände den föreslagna frågan. Hunspell-träffarna gäller tekniska
förkortningar, engelska expansionsord och produktnamnet Home Assistant.

## TMX och Lokalise

Förslagen är lokala och ännu inte sparade i Lokalise. Home Assistant-TMX:en
ändras därför inte.
