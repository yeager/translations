# Cataclysm-DDA, svenska: batch 23

20 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller fordonsdelar, tankar, borttagning
och hopfällning i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod. Tankar fylls på
eller tankas, medan fordonsdelar monteras och demonteras. Formuleringarna
undviker genusberoende artiklar framför de dynamiska del- och fordonsnamnen.

Kontroller före API-inskick:

- 20 av 20 platsmarkörer, inklusive `<npcname>`, `%s`, `%1$d` och `%1$s`–`%2$s`,
  stämmer mellan källa och mål.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast platshållaren `npcname`.
- svlang markerar endast platshållaren och en falsk V2-varning för inledande
  `%1$s`; den faktiska svenska ordföljden är korrekt.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 20 översättningar via Transifex API.
Varje enskilt API-svar innehöll en målöversättning, och en ny oberoende
GET-återläsning jämförde sedan samtliga 20 sparade målvärden med denna batch:
20 av 20 stämde exakt.
