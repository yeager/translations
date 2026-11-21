# Home Assistant Core – Bluetti Modbus

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bluetti_modbus/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: samtliga 78 aktuella Lokalise-poster för komponentens bladsträngar och referensmål är radgranskade och återlästa. Ingen ny ändring behövs.

Konfigurationsflödet använder korrekta Modbus-termer, `Enhets-ID`, `Modbus-enhets-ID:t`, TCP-port och `BLUETTI-kraftstation`. Fel, återkonfigurering och Zeroconf behåller samtliga platshållare. Elnamnen är konsekventa: nät-, batteri-, växelriktar- och PV-värden samt laddning/urladdning och import/export har kontrollerats som grupper. De tidigare sparade formuleringarna för nätanslutet laddnings- och urladdningsläge är korrekta.

Tidigare detaljer och API-sparningar finns i `2026-11-19/sparade-andringar-bluetti-modbus-konfiguration.md`, `sparade-andringar-bluetti-foreca-evohome.md` och `sparade-andringar-prowl-bluetti-media.md`.
