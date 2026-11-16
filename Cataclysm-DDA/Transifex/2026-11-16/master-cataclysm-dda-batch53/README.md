# Cataclysm-DDA, svenska: batch 53

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De omfattar status för kroppssmärta och sömn,
ett val av föremål samt varningar före dykning och vid förflyttning.

Källkontexten kontrollerades i `src/avatar.cpp` och `src/avatar_action.cpp`.
Den bioniska `soporific inducer` benämns konsekvent *sömnframkallare* och dess
resurs som *bionisk energi*. Rubrikerna för dykning beskriver listans föremål
och står därför i plural: ”Kommer att bli våta”.

## Kontroller före API-inskick

- Platsmarkörer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang gav en hög naturlighetspoäng. Den enda V2-varningen gällde en vanlig
samordnad sats och är en falsk positiv. Hunspell-SV saknar den etablerade,
projektspecifika termen ”bionisk”, men rapporterade inga andra stavningsfel.
