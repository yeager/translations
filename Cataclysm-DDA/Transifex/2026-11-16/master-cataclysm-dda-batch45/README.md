# Cataclysm-DDA, svenska: batch 45

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De beskriver egenskaper hos skydd och
gränssnittet för att sortera dem.

Källkontexten kontrollerades i `src/armor_layers.cpp`. `Sprite` är den
visade figuren och återges som `figur`, medan `water friendly` beskriver att
ett föremål tål vatten. Märkningen `H` i källan betyder att ett föremål är
hidden; den svenska markeringen är därför `D` för dold. Färgtaggar och alla
fyra platsmarkörer i hjälptexten bevaras exakt.

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

svlang markerade endast de bevarade färgtaggarna som ovanliga. Hunspell-SV
markerade endast samma taggar.
