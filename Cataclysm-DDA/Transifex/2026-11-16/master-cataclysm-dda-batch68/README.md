# Cataclysm-DDA, svenska: batch 68

Tolv aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller bioniska implantats status,
borttagning och installation.

Källkontexten är `src/bionics.cpp`. Måltexterna bevarar alla printf-markörer,
men utelämnar personnamn när bionikens namn redan identifierar det som avses.
`parent bionic` återges som det överordnade bioniska implantatet för att
beskriva beroendet tydligt.

## Kontroller före API-inskick

- Platsmarkörer och XML-liknande taggar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tolv översättningar via Transifex API.
En oberoende GET-återläsning jämförde därefter varje målsträng med batchens
underlag: 12 av 12 stämde exakt.

`l10n-lint` och svlang passerade utan avvikelser. Hunspell-SV markerar endast
`bioniska`, en etablerad böjning av projektets tekniska term `bionisk`.
