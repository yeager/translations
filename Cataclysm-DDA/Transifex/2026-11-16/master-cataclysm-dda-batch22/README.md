# Cataclysm-DDA, svenska: batch 22

25 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller snickeri, odling, batteriladdning,
reparation, fordonsmontering och redskapsljud i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod. `ladda` används
här endast för elektrisk batteriladdning. Verktygsljuden har svensk
ljudåtergivning: `KNAK!` för vedhuggning och `KLONK!` för hackarbete.

Kontroller före API-inskick:

- 25 av 25 platsmarkörer, inklusive `<npcname>`, `%s`, `%d` och `%1$s`–`%2$s`,
  stämmer mellan källa och mål. De två pluralsträngarna har både `one`- och
  `other`-former med svensk böjning.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast ljudordet `KLONK` och platshållaren `npcname`.
- svlang rapporterar samma specialord och fem falska V2-varningar i enkla
  svenska huvudsatser; faktisk ordföljd är korrekt.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 25 översättningar via Transifex API.
Den första API-skrivningen upptäckte korrekt att pluralsträngar kräver både
`one` och `other`; batchunderlaget kompletterades med de båda formerna innan
den slutliga inskickningen. Varje enskilt API-svar innehöll en målöversättning,
och en ny oberoende GET-återläsning jämförde sedan samtliga 25 värden,
inklusive pluralformerna: 25 av 25 stämde exakt.
