# Oberoende motgranskning – Blender Manual: armaturer, del 2

Datum: 2026-11-04  
Omfattning: kandidat 19–35 i `agent-manual-large-candidates-20261104.md`.  
Underlag: råexporten `exports/2026-11-04/blender-manual-manual-sv.po`,
`exports/2026-11-04/blender-ui-ui-sv.po` och `TERMINOLOGY.md`.

Ingen PO-fil har ändrats i denna granskning.

## Resultat

| Kandidat | Referens | Beslut | Kommentar |
| --- | --- | --- | --- |
| 19 | `duplicate_rename.rst:28` | Godkänn | Literalvärdena ``.L`` och ``.R`` är oförändrade och meningen är korrekt. |
| 20 | `duplicate_rename.rst:30` | Ändra | Skriv `Detta är användbart när du skapar speglade vänster- och högerbenkedjor.` Den föreslagna snedstreckskonstruktionen är svårläst. |
| 21 | `duplicate_rename.rst:33` | Godkänn | `ursprungliga bennamnen` anger rätt sökomfång. |
| 22 | `duplicate_rename.rst:35` | Godkänn | `Matchande text` och `duplicerade bennamn` är idiomatiska och innehållstrogna. |
| 23 | `duplicate_rename.rst:38` | Godkänn | Kort, begriplig fältbeskrivning utan ändrad innebörd. |
| 24 | `duplicate_rename.rst:40` | Godkänn | Villkor och följd när fältet lämnas tomt är korrekt uttryckta. |
| 25 | `transform.rst:21` | Ändra | *Parented* betyder att benet har en förälder, inte att det är överordnat. Använd: `Ben kan ha två typer av relationer: de kan ha en förälder och dessutom vara anslutna. Ben med en förälder beter sig i *redigeringsläge* som om de saknade relationer. De kan flyttas, roteras och skalas utan att deras underordnade ben påverkas. Anslutna ben måste däremot alltid ha förälderns spets ansluten till barnets rot. När du transformerar ett ben påverkar du därför dess anslutna föräldrar, barn och syskon.` |
| 26 | `transform.rst:32` | Ändra | UI-råexporten har `Transform` → `Transformering` i panelkontext och `Bone Roll` → `Benrullning`. Använd: `Slutligen kan du i panelen *Transformering* i sidofältet redigera positionerna och radien för båda lederna på det aktiva markerade benet, samt dess :ref:`benrullning <armature-bone-roll>`.` |
| 27 | `transform.rst:38` | Godkänn | UI-operatorn är exakt `Skala radie`. |
| 28 | `transform.rst:43` | Godkänn | Menyroll och den UI-belagda operatorn är korrekt bevarade. |
| 29 | `transform.rst:88` | Ändra | Bevara att det är benets kropp som väljs och det korrekta kortkommandot: `Du kan ändra storleken på volymen *Benhölje* genom att klicka på kroppen på det ben vars storlek du vill ändra, trycka på :kbd:`Shift-Ctrl-Alt-S` och sedan dra musen åt vänster eller höger. Volymen *Benhölje* ändras därefter i motsvarande grad.` |
| 30 | `transform.rst:91` | Godkänn | UI-termerna `Egenskaper`, `Ben`, `Deformera`, `Kuvert` och `Avstånd` samt RST-menysyntaxen stämmer. |
| 31 | `transform.rst:95` | Godkänn | `hörnpunkter` följer Blender-terminologin och satsens räckvidd är korrekt. |
| 32 | `transform.rst:120` | Godkänn | `objektläge` är UI-belagt; `Bone.004` och `B-Bone` är korrekt skyddade. |
| 33 | `transform.rst:126` | Godkänn | Exakt UI-belagd operatorform. |
| 34 | `transform.rst:131` | Godkänn | Menyvägen följer operatoröversättningen och behåller RST-rollen. |
| 35 | `symmetrize.rst:20` | Godkänn | Formella namnet `Action Constraints`, RST-målet och datatypen `Action` är bevarade; `nyckelbildrutor` och `målåtgärden` är rätt svenska termer. |

## Slutsats

13 av 17 kandidater kan användas oförändrade. Fyra behöver de fullständiga
ersättningar som anges ovan. Kontrollen fångar framför allt den semantiska
riktningen i benhierarkin och UI-belagda namn utan att ändra RST-mål,
kortkommandon eller programidentifierare.
