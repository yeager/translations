# Home Assistant – aerosmart: pågående svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `aerosmart`

## Hämtning och täckning

- Aktuellt lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Lokalise API: 138/138 exakta komponentnycklar med aktuell engelsk källa och svensk måltext.
- Komponenten kräver API-batcher om högst 20 nycklar: dess långa nycklar överskrider URI-gränsen med den tidigare generella 50-nyckelsbatchen. Detta har verifierats och arbetssättet är anpassat.
- Ingen tidigare aerosmart-rapport hittades i `yeager/translations`.

## Genomgång hittills

De 138 svenska måltexterna har täcknings- och platshållarkontrollerats. Högprioriterade konfigurations- och felsträngar samt tekniska termer för Modbus, stationadresser, värmepump, ventilation, brine, givare, fläktar och drifttid jämfördes med engelska källan.

Hunspell-träffarna är etablerade domäntermer, produktnamnet `aerosmart`, Modbus-identifierare och platshållare. Ingen säker stavningsrättning följer av dem.

Integrationens egen manifestfil anger namnet `aerosmart` med gemener; den formen har därför bevarats även i svenska sammansättningar. Ingen säker ändring har identifierats ännu.

## Status

Den semantiska radgranskningen fortsätter. Denna rapport är en spårbar täckningsstatus, inte ett färdiggodkännande av komponenten.