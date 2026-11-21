# Home Assistant Core – aerosmart

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aerosmart/strings.json`, aktuell Lokalise-export.

Status: pågående radgranskning. Komponenten omfattar 138 aktuella bladnycklar.

## Kontrollerat hittills

- Konfigurationsflödena för Modbus RTU/TCP, serieport, gateway, stationsadresser och `{default_*}`-platshållare är korrekta.
- Den första genomgången av värmepumps-, ventilations- och givaretiketterna bekräftar etablerade termer såsom `brinetemperatur`, `frånluftsfläkt`, `tilluftsfläkt`, `drifttid`, `värmepump` och `köldmedium`.
- Tekniska förkortningar, kodmarkeringar och `{level}`, `{stage}`, `{percentage}`, `{field}` och `{error}` är bevarade där de förekommer.

Inga ändringar har ännu sparats för aerosmart. Återstående binärsensorer, sensorer, statusvärden och undantag granskas radvis i fortsatt pass.
