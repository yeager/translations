# Cataclysm-DDA, svenska: batch 60

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De är förkortningar och flikrubriker för
baslägrets riktningar.

Källkontexten kontrollerades i `src/basecamp.cpp`. Strängarna är visuella
etiketter i riktningstabbarna, inte inmatade tangenter. Därför har de svenska
kompassförkortningarna använts: NO för nordost, O för öst och SO för sydost.
Omgivande blanksteg i flikrubrikerna är bevarade exakt.

## Kontroller före API-inskick

- Blanksteg, hakparenteser och kodliknande etiketter ska bevaras enligt
  respektive strängs UI-kontext.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio etiketter via Transifex API. En ny,
oberoende GET-återläsning jämförde sedan varje målsträng med denna batch. Alla
10 av 10 stämde exakt.
