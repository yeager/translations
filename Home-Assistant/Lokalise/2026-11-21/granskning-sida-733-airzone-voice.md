# Home Assistant Core – sida 733: granskningsstatus

Datum: 2026-11-21  
Plattform: Lokalise API  
Omfattning: 100 aktiva nycklar, sida 733 av 752 (`limit=100`)

## Kontroller

- Färsk Lokalise-hämtning innehåller Airzone, iZone, HP Printer, La Marzocco, Midea, MQTT, RainMachine, Tuya och Voice Support.
- Samtliga 100 svenska mål är ifyllda.
- Platshållarkontroll gav 0 avvikelser; bland annat bevaras `{name}` i HP Printer-flödet.
- Hunspell-sv-träffarna är granskade som produktnamn, protokoll, YAML-/konfigurationsnycklar eller tekniska etiketter: `Eco-Adapt`, `Ethernet`, `iZone`, `MQTT`, `Wi-Fi`, `configuration.yaml`, `exclude`, `Voice-appen` och `Marzocco`.

## Bedömning

De svenska målen följer aktuell källa och Home Assistant-terminologi. Oöversatta identiska värden är medvetna: produktnamnet `Eco-Adapt`, beteckningen `A++`, etablerade tekniknamn (`Ethernet`, `USB`, `Wi-Fi`), en formatplatshållare `{name}`, nätverksordet `Port` och statusvärdet `Full` som har samma svenska form. Inga betydelse- eller formatfel som motiverar en Lokalise-ändring hittades.

## Resultat

Inga ändringar föreslogs eller sparades för sida 733. Batchen är radgranskad mot den färska API-batchen och dokumenterad för fortsatt spårning.
