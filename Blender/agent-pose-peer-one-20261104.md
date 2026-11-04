# Oberoende motgranskning: Blender Manual — Pose Mode, del 1

Datum: 2026-11-04
Underlag: agent-next-candidates-20261104.md, råexporten för Blender Manual
och Blender-UI-katalogen.

Granskningen omfattar kandidat 1–11 i apply.rst. RST-målet för NLA ska
bevaras exakt. *Pose*, *rigg* och NLA används här i Blenders etablerade
fackkontext.

| Nr | Referens | Beslut | Motivering eller ersättande text |
| --- | --- | --- | --- |
| 1 | apply.rst:32 | Godkänn | Pose som viloposition använder UI-belagd viloposition. |
| 2 | apply.rst:47 | Ändra | Markera återger inte operationens apply. Använd ”Tillämpa pose som viloposition för markerade ben”. |
| 3 | apply.rst:49 | Ändra | Använd den översatta rubriken: ”Fungerar på samma sätt som *Pose som viloposition*, men tillämpas bara på de markerade benen.” |
| 4 | apply.rst:51 | Godkänn | vilopositionstransformeringar är tydligt och terminologiskt konsekvent. |
| 5 | apply.rst:57 | Godkänn | Visuell transformering till pose fungerar som avsnittsrubrik; UI:t använder den längre operatorformen när Apply ingår i källtexten. |
| 6 | apply.rst:59 | Ändra | Källtexten är påstående, inte uppmaning: ”Tillämpar de utvärderade visuella transformeringarna på benen efter att begränsningarna har utvärderats.” |
| 7 | apply.rst:61 | Ändra | Undvik begränsade positionen, som kan betyda begränsad i omfattning. Använd ”Detta omvandlar den slutliga positionen, rotationen och skalningen efter begränsningarna till vanliga posetransformeringar, så att begränsningarna kan tas bort utan att det aktuella visuella resultatet ändras.” |
| 8 | apply.rst:65 | Ändra | Begränsade poser blir tvetydigt. Använd ”Detta är användbart för att baka poser med begränsningar, förbereda riggar för export eller förenkla komplexa begränsningsuppsättningar.” |
| 9 | apply.rst:72 | Ändra | Följ den befintliga UI-strängen exakt: ”Tilldela anpassade egenskapsvärden som standard”. |
| 10 | apply.rst:74 | Godkänn | Förslaget är en tydlig och naturlig beskrivning av lagringen. |
| 11 | apply.rst:76 | Ändra | Skriv ”Dessa standardvärden används som en del av armaturens viloläge vid blandning av NLA-spår och utvärdering av animeringar.” RST-målet kring NLA ska bevaras. |

Slutsats: fyra kandidater kan användas oförändrade och sju behöver de
angivna ersättningarna. Inga PO-filer har ändrats.
