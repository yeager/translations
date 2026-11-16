# Cataclysm-DDA, svenska: batch 43

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De visar information om skyddets lager,
belastning och täckning.

Källkontexten kontrollerades i `src/armor_layers.cpp`. `Armor` återges här
som skydd, eftersom strängarna beskriver ett enskilt föremåls skyddsvärden.
`Coverage` är täckning och dess tre specialvärden är närstrid, distans och
vitala delar. Den första strängen är pluraliserad hos Transifex men har samma
svenska formulering i båda pluralformerna.

## Kontroller före API-inskick

- Platsmarkörer, formateringsbredd och XML-liknande taggar ska stämma mellan
  källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
Den pluraliserade strängen skickades med både formen `one` och `other`. En
ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna batch.
Alla 10 av 10 stämde exakt.

svlang markerade endast de bevarade färgtaggarna som ovanliga. Hunspell-SV
markerade endast samma taggar.
