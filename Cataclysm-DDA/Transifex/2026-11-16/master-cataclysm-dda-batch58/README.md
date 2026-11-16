# Cataclysm-DDA, svenska: batch 58

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller kast, kroppslöshet, ett riddjur med
urladdade batterier och aktivering av våt utrustning.

Källkontexten kontrollerades i `src/avatar_action.cpp`. Det tillfälliga
tillståndet *incorporeal* översätts som ”kroppslös”. Platsmarkören för meken
är bevarad och källans riktiga utelämningstecken är kvar.

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

svlang rapporterade mycket naturlig svenska. Den enda V2-varningen gällde en
korrekt samordnad sats och är en falsk positiv. Hunspell-SV gav bara normal
analysutmatning och inga stavningsfel.
