# Cataclysm-DDA, svenska: batch 46

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De hör till sortering och hantering av
skyddsutrustning.

Källkontexten kontrollerades i `src/armor_layers.cpp` och
`src/body_status_ui.cpp`. `Integrated armor` är den fasta, integrerade
rustningen och har fått en konsekvent svensk term. `Inventory letters` är de
enskilda bokstavstangenter som identifierar föremål i inventariet. API:t
normaliserar avslutande radbrytningar; målsträngen för hjälpraden arkiveras
därför i den återlästa, kanoniska formen utan avslutande radbrytning.

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
batch. Alla 10 av 10 stämde exakt, inklusive den servernormaliserade
hjälpraden utan avslutande radbrytning.

svlang markerade endast de bevarade färgtaggarna som ovanliga. Hunspell-SV
markerade endast samma taggar.
