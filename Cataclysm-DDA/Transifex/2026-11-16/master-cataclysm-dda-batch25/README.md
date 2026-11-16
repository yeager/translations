# Cataclysm-DDA, svenska: batch 25

12 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller samtal, färdighetsträning,
besvärjelser, undervisning, batterier och rengöring i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod. `spell` översätts
som `besvärjelse`, och vatten uttrycks med neutrala `enheter` i den interna
resursräkning som används vid rengöring.

Kontroller före API-inskick:

- 12 av 12 platsmarkörer, inklusive `<npcname>`, `%s`, `%d` och `%1$i`,
  stämmer mellan källa och mål.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast platshållaren `npcname`.
- svlang rapporterar en falsk V2-varning från den inledande platshållaren i
  en annars korrekt svensk huvudsats.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 12 översättningar via Transifex API.
Varje enskilt API-svar innehöll en målöversättning, och en ny oberoende
GET-återläsning jämförde sedan samtliga 12 sparade målvärden med denna batch:
12 av 12 stämde exakt.
