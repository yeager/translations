# Cataclysm-DDA, svenska: batch 44

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De visar skyddsvärden och egenskaper för
utrustning.

Källkontexten kontrollerades i `src/armor_layers.cpp`. `Environmental` är
föremålets motstånd mot miljöfaror och återges därför som miljöskydd.
`Breathability` är ett materialvärde och återges som andningsförmåga.
`Refitted` gäller passform, inte en obestämd ombyggnad, och får därför den
tydliga formuleringen `Passformen kan anpassas.`

## Kontroller före API-inskick

- Platsmarkörer och formateringsbredd ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang rapporterade inga språkvarningar. Hunspell-SV rapporterade inga
stavningsfel; dess analysutmatning innehöll bara vanliga böjningsuppslag.
