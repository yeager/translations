# ESP Web Tools, svensk användargränssnittslokalisering 2026-11-15

## Omfattning

ESP Web Tools är en webbaserad installerare för ESP-enheter. Projektet saknade
lokaliseringsstöd för det inbyggda installationsflödet.

## Ändringar

- Lade till svensk lokalisering som väljs från dokumentets eller webbläsarens
  språk.
- Täcker installations-, anslutnings-, Wi-Fi-, flashnings-, logg- och
  felvyerna, inklusive dialogen som visas när ingen serieport har valts.
- Behåller originaltexten för andra språk.
- Lade till tester för svenska texter, platshållare och svensk felrubrik.

## Verifiering

- `script/build`
- `npm test` med 23 godkända tester
- `npm exec -- prettier --check src test`
- `git diff --check`
- Gitleaks utan träffar
- svlang utan skrivregelfel i den svenska katalogen

## Upstreamstatus

- Pull request: https://github.com/esphome/esp-web-tools/pull/774
- Status: öppen, inväntar upstream-granskning och merge.
