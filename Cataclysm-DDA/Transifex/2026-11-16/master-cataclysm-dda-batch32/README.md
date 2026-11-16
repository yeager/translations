# Cataclysm-DDA, svenska: batch 32

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De fortsätter fordonsförvaringen och
hanteringen av föremål på marken.

Källkontexten kontrollerades i `src/activity_item_handling.cpp`. Samma svenska
fordonsuttryck används som i batch 31: `%3$s på %2$s`. Passiva satser används
där den dynamiska föremålsbenämningen kan vara antingen singular eller plural
och ha okänt grammatiskt genus.

## Kontroller före API-inskick

- Platsmarkörer och pluralformer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan måltexten, inklusive samtliga
pluralformer, med denna batch. Alla 10 av 10 stämde exakt.

svlang markerade falska V2-träffar i satser som börjar med den dynamiska
föremålsplatshållaren. Hunspell-SV markerade endast `<npcname>`.
