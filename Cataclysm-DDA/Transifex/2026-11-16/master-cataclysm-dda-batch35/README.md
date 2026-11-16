# Cataclysm-DDA, svenska: batch 35

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De beskriver varför automatiska aktiviteter
inte kan genomföras.

Källkontexten kontrollerades i `src/activity_item_handling.cpp`. Åtgärden
`task` följer projektets etablerade term `uppgift`, medan `activity` blir
`aktivitet`. Alla jämförbara felmeddelanden använder samma svenska satsform.

## Kontroller före API-inskick

- Platsmarkörer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang och Hunspell-SV rapporterade inga avvikelser.
