# Cataclysm-DDA, svenska: batch 40

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De hör till flytt av föremål i avancerat
inventarium.

Källkontexten kontrollerades i `src/advanced_inv.cpp`. I dessa felmeddelanden
återges `wield` som att hålla ett föremål i handen. Strängarna om spillbara
behållare omformuleras för att undvika en grammatiskt osäker referens till
ett föremålsnamn med okänt genus. Färgmarkeringen i tangentbindningsrubriken
bevaras oförändrad.

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
batch. Alla 10 av 10 stämde exakt.

svlang markerade endast den förväntade V2-falskträffen i en sats där `%s`
ingår i subjektfrasen, samt de bevarade färgtaggarna. Hunspell-SV markerade
endast den bevarade taggen `color_yellow`.
