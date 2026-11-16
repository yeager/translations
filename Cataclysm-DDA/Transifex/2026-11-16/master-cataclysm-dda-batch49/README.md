# Cataclysm-DDA, svenska: batch 49

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De hör till läsning, studier och träning.

Källkontexten kontrollerades i `src/avatar.cpp`. Här är `manual` en bok om
stridsteknik, så den svenska formuleringen använder `handboken` i stället för
den otydliga direktöversättningen manual. De två engelska formerna för att
läsa tillsammans får samma svenska verbform, eftersom `läser` fungerar för
både en person och flera personer.

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

svlangs varningar är förväntade falskträffar eftersom fristående menytexter
kontrollerades som en enda sammanhängande mening. Hunspell-SV rapporterade
inga stavningsfel; dess analysutmatning innehöll bara vanliga böjningsuppslag.
