# Cataclysm-DDA, svenska: batch 61

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De omfattar resterande riktningstabbar samt
gränssnittstext för baslägret.

Källkontexten kontrollerades i `src/basecamp.cpp`. Svenska kompassförkortningar
används i visuella fliketiketter: SV, V och NV. Receptdetaljernas tre
platsmarkörer och samtliga radbrytningar bevaras exakt.

## Kontroller före API-inskick

- Platsmarkörer, radbrytningar, blanksteg och hakparenteser ska bevaras enligt
  respektive strängs UI-kontext.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio etiketter via Transifex API. En ny,
oberoende GET-återläsning jämförde sedan varje målsträng med denna batch. Alla
10 av 10 stämde exakt efter Transifex dokumenterade normalisering av en
avslutande radbrytning i den flerradiga receptsträngen.

svlangs enda V2-varning uppstod när den korta rubriken och en mening
analyserades tillsammans. Den är en falsk positiv.
