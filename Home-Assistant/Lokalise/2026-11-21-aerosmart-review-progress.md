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


## Sparade rättningar

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::aerosmart::entity::sensor::fine_dust_filter_operating_hours::name` | Finfiltrets drifttid | Finpartikelfiltrets drifttid | Samma källterm översätts redan som `finpartikelfilter` i komponentens binärsensorer. |
| `component::aerosmart::entity::sensor::fine_dust_filter_service_life::name` | Finfiltrets livslängd | Finpartikelfiltrets livslängd | Samma term- och sammansättningsrättning. |

Båda sparningarna validerades med `l10n-lint`, återlästes via Lokalise API och lades till i det verifierade TM-minnet. Hunspell saknar den produktiva sammansättningen `finpartikelfiltrets`; `svlang` bedömer den som ovanlig men naturlig. Det är en korrekt fackterm, inte en stavningsavvikelse.

## Status

Den semantiska radgranskningen fortsätter. Denna rapport är en spårbar täckningsstatus, inte ett färdiggodkännande av komponenten.

## Grovpartikelfilter – sparade och API-återlästa ändringar

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::aerosmart::entity::sensor::coarse_dust_filter_maximum_conveyed_volume::name` | Coarse dust filter maximum conveyed volume | Grovdammsfiltrets maximala luftvolym | Grovpartikelfiltrets maximala luftvolym | Konsekvent med den redan verifierade termen *finpartikelfilter*. |
| `component::aerosmart::entity::sensor::coarse_dust_filter_operating_hours::name` | Coarse dust filter operating hours | Grovdammsfiltrets drifttid | Grovpartikelfiltrets drifttid | Samma terminologi. |
| `component::aerosmart::entity::sensor::coarse_dust_filter_service_life::name` | Coarse dust filter service life | Grovdammsfiltrets livslängd | Grovpartikelfiltrets livslängd | Samma terminologi. |

Alla tre Lokalise-översättningar skickades med API och hämtades igen från sina respektive översättningsobjekt.
