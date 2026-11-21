# Home Assistant Core – QNAP

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/qnap/strings.json`  
Status: samtliga 43 aktuella källsträngar är radgranskade mot Lokalise.

## Sparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::qnap::entity::sensor::drive_smart_status::name` | Drive {monitor_device} status | Hårddisk {monitor_device} status | Status för hårddisk {monitor_device} | Variabelt disknamn gör den nuvarande ordföljden svårläst; förslaget är idiomatisk svenska och bevarar platshållaren. Lokalise-ID `437661476`. |
| `component::qnap::entity::sensor::drive_temp::name` | Drive {monitor_device} temperature | Hårddisk {monitor_device} temperatur | Temperatur för hårddisk {monitor_device} | Samma ordföljdskorrigering och platshållarbevarande. Lokalise-ID `437661477`. |

## Verifierade befintliga värden

- Konfigurationsavbrott, alla tre felreferenser, användar- och omkonfigureringsflödet är korrekta. Samtliga gemensamma referenser för värd, port, SSL, certifikatverifiering, användarnamn och lösenord följer källan exakt.
- Texterna för QNAP-enhet, QNAP NAS och värdnamn/IP-adress är språkligt riktiga. Produktnamnet `QNAP` bevaras.
- Samtliga övriga 18 aktuella sensoretiketter är korrekta, inklusive CPU, minne, nätverk, volym, status, systemtemperatur och drifttid. Platshållaren `{monitor_device}` är bevarad i samtliga relevanta etiketter.
- `uptime` använder en etablerad svensk referens till drifttid. Det är en giltig målreferens även om den engelska källan är direkttext.

Lokalise-sökningen innehåller dessutom den historiska QNAP-posten `component::qnap::config::abort::reconfigure_successful` (ID `822293473`), som saknas i aktuell källfil och därför lämnas orörd. Sökresultatet innehåller även QNAP QSW-poster på grund av namnöver­lappning; de avgränsades i separata sökningar och granskas i [QNAP QSW-rapporten](granskning-qnap-qsw.md). De två förslagen är sparade och API-återlästa 2026-11-21 med översättnings-ID `3487809135` och `3487809195` och ingår i verifierad TMX.
