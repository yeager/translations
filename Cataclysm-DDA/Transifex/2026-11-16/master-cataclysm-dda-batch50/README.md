# Cataclysm-DDA, svenska: batch 50

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De beskriver vad böcker kan lära ut.

Källkontexten kontrollerades i `src/avatar.cpp`. `Morale` är karaktärens
humörsvärde och återges därför som humör, inte den engelsknära falska vännen
`moral`. `Skill expertise` är en särskild, djup kunskap inom en färdighet och
återges som specialkunskap. Platsmarkörernas ordning är anpassad till naturlig
svensk satsföljd men bevaras exakt.

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

svlang markerade endast en förväntad V2-falskträff där platsmarkören `%s`
är ett predikativ. Hunspell-SV rapporterade inga stavningsfel; dess
analysutmatning innehöll bara vanliga böjningsuppslag.
