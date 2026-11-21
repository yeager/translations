# Home Assistant Core – sida 746: granskningsstatus

Datum: 2026-11-21  
Plattform: Lokalise API  
Omfattning: 100 aktiva nycklar, sida 746 av 752 (`limit=100`)

## Kontroll och resultat

De första 23 nycklarna avslutar LIFX-katalogen. Övriga nycklar hör till bland
annat Airzone, Bosch SHC, VeSync, System Bridge, Samsung ExLink, Amazon Polly,
Swiss Public Transport, Trimlight, Tuya och Daikin. Aktuell engelsk källa
kontrollerades för de nya Core-komponenterna. Platshållare i VeSync,
Samsung ExLink, Amazon Polly, System Bridge och Trimlight är bevarade exakt;
flera av deras engelska fält var inte exponerade i detta Lokalise-svar men
verifierades mot aktuell Core-källa.

| Fullständig nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
| --- | --- | --- | --- |
| `component::fritz::entity::sensor::link_download_rate::name` | `Nedladdningshastighet för länk` | `Länkens nedladdningshastighet` | Svensk genitiv ger den naturliga benämningen för *Download link rate*. |
| `component::fritz::entity::sensor::link_max_download_rate::name` | `Högsta nedladdningshastighet för länk` | `Länkens högsta nedladdningshastighet` | Samma konsekventa ordföljd för *Maximum download link rate*. |
| `component::fritz::entity::sensor::link_max_upload_rate::name` | `Högsta uppladdningshastighet för länk` | `Länkens högsta uppladdningshastighet` | Samma konsekventa ordföljd för *Maximum upload link rate*. |
| `component::fritz::entity::sensor::link_upload_rate::name` | `Uppladdningshastighet för länk` | `Länkens uppladdningshastighet` | Svensk genitiv ger den naturliga benämningen för *Upload link rate*. |

Alla fyra ändringar sparades via Lokalise API och varje returnerat värde
återlästes i PUT-svaret. Inga lint- eller stavningsanmärkningar återstår i
ändringarna; batchen saknar pluralformer och referensmål.
