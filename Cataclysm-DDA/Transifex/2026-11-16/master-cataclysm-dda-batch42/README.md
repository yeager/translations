# Cataclysm-DDA, svenska: batch 42

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De beskriver lager i klädsel och belastning
från utrustning.

Källkontexten kontrollerades i `src/armor_layers.cpp` och
`src/advanced_inv_area.cpp`. Sju strängar är avsiktligt satsfragment som
sammanfogas i felmeddelandet om belastning. Därför är de översatta för att
fungera i ramen `Att bära flera föremål %s på %s ökar belastningen där.`
Färgtaggarna och båda platsmarkörerna bevaras exakt.

## Kontroller före API-inskick

- Platsmarkörer och XML-liknande taggar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
De två `n_gettext`-strängarna skickades med både formen `one` och `other`;
de har samma svenska formulering eftersom meningen inte böjs efter antalet
kroppsdelar. En ny, oberoende GET-återläsning jämförde sedan varje målsträng
med denna batch. Alla 10 av 10 stämde exakt.

svlang markerade endast färgtaggarna och den förväntade falskträffen när
fragmenten kontrollerades som löpande text. Hunspell-SV markerade endast de
bevarade färgtaggarna.
