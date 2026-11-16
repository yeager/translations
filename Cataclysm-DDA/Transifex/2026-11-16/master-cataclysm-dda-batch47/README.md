# Cataclysm-DDA, svenska: batch 47

Tio aktuella oöversatta hjälprader ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De visar hur rustningspanelen styrs.

Källkontexten kontrollerades i `src/armor_layers.cpp`. Alla tio rader är
hjälptext för kortkommandon. De svenska formuleringarna använder de synliga
panelernas namn och svenska ord som `bläddra`, `föremål`, `kroppsdel` och
`karaktärsfigur`. Färgtaggarna och samtliga platsmarkörer bevaras exakt.
API:t normaliserar avslutande radbrytningar, därför arkiveras målen utan
avslutande radbrytning.

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
avslutande radbrytning.

svlang markerade endast den förväntade V2-falskträffen eftersom hjälpraderna
är satsfragment som inleds med kortkommandon, samt de bevarade färgtaggarna.
Hunspell-SV markerade endast samma taggar.
