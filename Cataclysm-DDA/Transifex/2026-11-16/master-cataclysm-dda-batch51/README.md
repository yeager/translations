# Cataclysm-DDA, svenska: batch 51

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De är händelsemeddelanden om sömn, mutationer
och hunger.

Källkontexten kontrollerades i `src/avatar.cpp`. Det interna alarmet kommer
från en inbyggd väckarklocka. `Retched` översätts som `hulkar`, eftersom
magen redan är tom. Mutationsnamnen använder naturliga svenska sammansättningar
som kitin, insektslemmar, simhudsförsedda händer och spindelben.

## Kontroller före API-inskick

- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang markerade endast förväntade falskträffar i satsinledningen och de
avsiktliga mutationssammansättningarna. Hunspell-SV markerade samma
projektspecifika sammansättningar.
