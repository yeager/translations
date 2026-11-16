# Cataclysm-DDA, svenska: batch 21

25 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller klippning av djur, isärtagning,
lägerutrustning, spelmeddelanden och hårvård i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod. `field` används i
övervärldens terrängdata och översätts därför till `fält`. `crunch!` är ett
ljudeffektmeddelande från ett verktyg och fick den naturliga svenska
ljudåtergivningen `Krasch!`. I klippningsmeddelandena hålls `%1$s` utan
personböjning så att samma svenska fungerar för både spelarfigur och NPC.

Kontroller före API-inskick:

- 25 av 25 platsmarkörer, inklusive `<npcname>`, `%s` och `%1$s`–`%2$s`,
  stämmer mellan källa och mål.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast `mittrutan` och platshållaren `npcname`.
- svlang markerar dessa två ord som ovanliga och två falska V2-varningar; de
  beror på en fristående terrängterm respektive korrekta svenska huvudsatser.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 25 översättningar via Transifex API.
Varje enskilt API-svar innehöll en målöversättning, och en ny oberoende
GET-återläsning jämförde sedan samtliga 25 sparade målvärden med denna batch:
25 av 25 stämde exakt.
