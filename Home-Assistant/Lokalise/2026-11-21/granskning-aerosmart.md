# Home Assistant Core – aerosmart

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/aerosmart/strings.json`, aktuell Lokalise-export.

Status: samtliga 138 aktuella bladnycklar är radgranskade utan ändringsförslag.

## Kontrollerat hittills

- Konfigurationsflödena för Modbus RTU/TCP, serieport, gateway, stationsadresser och `{default_*}`-platshållare är korrekta.
- Den första genomgången av värmepumps-, ventilations- och givaretiketterna bekräftar etablerade termer såsom `brinetemperatur`, `frånluftsfläkt`, `tilluftsfläkt`, `drifttid`, `värmepump` och `köldmedium`.
- Tekniska förkortningar, kodmarkeringar och `{level}`, `{stage}`, `{percentage}`, `{field}` och `{error}` är bevarade där de förekommer.

## Slutförd kontroll

Alla återstående binärsensorer, sensorer, statusvärden och undantag har granskats. De svenska HVAC- och ventilationssammansättningarna är konsekventa, bland annat för `frånluft`, `tilluft`, `köldmedium`, `varmvattenberedare`, `elbolagsspärr`, `solavskärmning` och `drifttid`. Inga ändringar sparades för aerosmart.
