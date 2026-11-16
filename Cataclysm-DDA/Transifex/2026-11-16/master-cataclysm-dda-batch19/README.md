# Cataclysm-DDA, svenska: batch 19

25 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. Batchen omfattar träningsaktivitet, skörd och
robotstyrning i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod före översättning.
Särskilt granskades de variabla robotnamnen: formuleringarna har artikellös
svenska där namnets genus annars inte kan vara känt. `IFF` är ett tekniskt
protokollnamn och lämnas därför oförändrat. Den inledande lilla bokstaven i
`dig själv flämta och pusta!` bevarar källans avsiktliga fragmentform.

Kontroller före API-inskick:

- 25 av 25 platsmarkörer, inklusive `<npcname>` och `%s`, stämmer mellan källa
  och mål.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast `IFF`, `IFF-inställningarna`, `IFF-protokollen` och
  platshållaren `npcname`.
- svlang rapporterar IFF och platshållaren som ovanliga ord samt en falsk
  V2-varning för inledande `%s`; den faktiska satsen har korrekt ordföljd.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 25 översättningar via Transifex API.
Varje enskilt API-svar innehöll en målöversättning, och en ny oberoende
GET-återläsning jämförde sedan samtliga 25 sparade målvärden med denna batch:
25 av 25 stämde exakt.
