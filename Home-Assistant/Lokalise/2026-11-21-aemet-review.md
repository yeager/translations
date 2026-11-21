# Home Assistant – AEMET: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `aemet`

Aktuellt källträd och Lokalise API jämfördes för 10/10 komponentnycklar. Ingen tidigare AEMET-rapport hittades.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::aemet::options::step::init::data::radar_updates` | Gather data from AEMET weather radar | Samla data från AEMET väderradar | Samla data från AEMET-väderradar | Samma svenska produktnamnssammansättning som i `AEMET-väderstationer`. |

Ändringen sparades via Lokalise API och lästes tillbaka.

Övriga strängar, inklusive `API-nyckel`, `väderradar`, `AEMET-ort` och platshållarna `{api_key_url}`, `{latitude}`, `{longitude}`, är korrekta. Inga lokala, osparade förslag återstår.