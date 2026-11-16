# Cataclysm-DDA, svenska: batch 48

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De omfattar hjälp för rustningspanelen,
uppdrag och läsning.

Källkontexten kontrollerades i `src/armor_layers.cpp` och `src/avatar.cpp`.
Den längre texten förklarar att belastningen först summeras per kroppsdel och
sedan ökas av plagg i samma lager eller fel lagerordning. Meningsgränser har
lagts till mellan källans hopsatta satser. Färgtaggar, citattecken och
platsmarkörer bevaras exakt. API:t normaliserar avslutande radbrytningar i
hjälpraderna, därför arkiveras målen utan dem.

## Kontroller före API-inskick

- Platsmarkörer och XML-liknande taggar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt i den servernormaliserade formen utan
avslutande radbrytning i hjälpraderna.

svlangs markeringar är förväntade falskträffar från kortkommandoraderna,
färgtaggarna och den sammansatta förklaringstexten. Hunspell-SV markerade
endast samma färgtaggar.
