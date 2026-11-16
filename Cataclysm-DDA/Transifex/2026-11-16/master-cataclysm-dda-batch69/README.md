# Cataclysm-DDA, svenska: batch 69

Fjorton aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller borttagning och installation av
bioniska implantat, inklusive riskvarningar och konsekvenser för beroenden.

Källkontexten är `src/bionics.cpp`. Formuleringarna använder `bioniskt
implantat` konsekvent och bevarar samtliga printf-markörer. Namntaggar som
inte behöver visas i den svenska frasen har utelämnats, vilket är tillåtet i
den här resursens målformat.

## Kontroller före API-inskick

- Platsmarkörer och XML-liknande taggar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga fjorton översättningar via Transifex
API. En oberoende GET-återläsning jämförde därefter varje målsträng med
batchens underlag: 14 av 14 stämde exakt.

`l10n-lint` och svlang passerade utan avvikelser. Hunspell-SV markerar endast
`bioniska`, en etablerad böjning av projektets tekniska term `bionisk`.
