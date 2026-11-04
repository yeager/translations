# Motgranskning – Blender Manual: armaturer

Datum: 2026-11-04  
Underlag: `agent-manual-large-candidates-20261104.md`, råexporten
`exports/2026-11-04/blender-manual-manual-sv.po`,
`exports/2026-11-04/blender-ui-ui-sv.po` och `TERMINOLOGY.md`.

Granskningen omfattar samtliga 35 kandidater. `Godkänn` betyder att den
föreslagna svenska texten kan användas oförändrad. `Ändra` anger en komplett,
ersättande `msgstr`. Ingen kandidat ska utelämnas.

| Nr | Referens | Beslut | Motgranskning |
| --- | --- | --- | --- |
| 1 | `bone_roll.rst:7` | Godkänn | `benrullning`, `viloposition` och RST-målet är korrekta. |
| 2 | `bone_roll.rst:21` | Godkänn | Naturlig och innehållstrogen beskrivning av omberäkning av rullning. |
| 3 | `bone_roll.rst:24` | Godkänn | Alla synliga axelvärden har återställts. |
| 4 | `bone_roll.rst:30` | Godkänn | Etikett och samtliga globala axelvärden är korrekta. |
| 5 | `bone_roll.rst:39` | Godkänn | `3D-markören` följer UI-termen och meningen bevarar Z-axelns riktning. |
| 6 | `bone_roll.rst:41` | Ändra | Använd imperativ som i källtexten: `msgstr "Ändra resultatet med 180°."` |
| 7 | `bone_roll.rst:57` | Godkänn | `Justera rullningen` återger *Tweak* utan att ändra innebörden. |
| 8 | `bone_roll.rst:62` | Godkänn | Exakt UI-belagd operator: `Rensa rullning`. |
| 9 | `bone_roll.rst:67` | Godkänn | Menysyntaxen är intakt och `Armatur` stämmer med operator-/menykontexten i UI-katalogen. |
| 10 | `bone_roll.rst:70` | Godkänn | Korrekt åtgärd och korrekt gradtecken. |
| 11 | `delete.rst:17` | Godkänn | Semikolon skiljer satserna tydligt; *leder* behåller den anatomiska innebörden. |
| 12 | `duplicate_rename.rst:5` | Godkänn | Exakt UI-belagd operator. |
| 13 | `duplicate_rename.rst:10` | Godkänn | Korrekt översatt menyväg med bevarad RST-roll. |
| 14 | `duplicate_rename.rst:12` | Godkänn | `bennamnen` och den automatiska namnändringen är idiomatiska. |
| 15 | `duplicate_rename.rst:14` | Ändra | Följ termen *parent* → *förälder* och använd en naturlig sammansättning: <code>msgstr "Den här operatorn fungerar på liknande sätt som :ref:`bpy.ops.armature.duplicate_move` och bevarar, när det är möjligt, föräldra- och anslutningsrelationer mellan duplicerade ben."</code> |
| 16 | `duplicate_rename.rst:17` | Godkänn | Markerings- och omplaceringsföljden är korrekt återgiven. |
| 17 | `duplicate_rename.rst:19` | Godkänn | `riggar` är en etablerad, begriplig Blender-term i denna förklarande text. |
| 18 | `duplicate_rename.rst:26` | Godkänn | Korrekt beskrivning av att vända riktningssuffix. |
| 19 | `duplicate_rename.rst:28` | Godkänn | Literalvärdena ``.L`` och ``.R`` är oförändrade. |
| 20 | `duplicate_rename.rst:30` | Ändra | Undvik den svårlästa formen `vänster-/högerbenkedjor`: `msgstr "Detta är användbart när du skapar speglade vänster- och högerbenkedjor."` |
| 21 | `duplicate_rename.rst:33` | Godkänn | Sökomfånget, de ursprungliga bennamnen, framgår korrekt. |
| 22 | `duplicate_rename.rst:35` | Godkänn | `Matchande text` och `duplicerade bennamn` är korrekta. |
| 23 | `duplicate_rename.rst:38` | Godkänn | Korrekt och kort etikettförklaring. |
| 24 | `duplicate_rename.rst:40` | Godkänn | Villkoret och följden vid tomt fält är tydliga. |
| 25 | `transform.rst:21` | Ändra | *Parented* betyder inte *överordnade*; de ben som har en förälder är underordnade. Använd: `msgstr "Ben kan ha två typer av relationer: de kan ha en förälder och dessutom vara anslutna. Ben med en förälder beter sig i *redigeringsläge* som om de saknade relationer. De kan flyttas, roteras och skalas utan att deras underordnade ben påverkas. Anslutna ben måste däremot alltid ha förälderns spets ansluten till barnets rot. När du transformerar ett ben påverkar du därför dess anslutna föräldrar, barn och syskon."` |
| 26 | `transform.rst:32` | Ändra | UI-katalogen belägger panelordet `Transformering`; `rullningsrotation` är inte belagd och blir onödigt tungt. Använd: <code>msgstr "Slutligen kan du i panelen *Transformering* i sidofältet redigera positionerna och radien för båda lederna på det aktiva markerade benet, samt dess :ref:`benrullning &lt;armature-bone-roll&gt;`."</code> |
| 27 | `transform.rst:38` | Godkänn | Exakt UI-belagd form: `Skala radie`. |
| 28 | `transform.rst:43` | Godkänn | Menyvägen återger den synliga operatören korrekt. |
| 29 | `transform.rst:88` | Ändra | Behåll att det är benets kropp som klickas på, men gör hänvisningen tydlig: <code>msgstr "Du kan ändra storleken på volymen *Benhölje* genom att klicka på kroppen på det ben vars storlek du vill ändra, trycka på :kbd:`Shift-Ctrl-Alt-S` och sedan dra musen åt vänster eller höger. Volymen *Benhölje* ändras därefter i motsvarande grad."</code> |
| 30 | `transform.rst:91` | Godkänn | UI-termerna `Egenskaper`, `Ben`, `Deformera`, `Kuvert` och `Avstånd` följer råexporten; RST-syntaxen är rättad. |
| 31 | `transform.rst:95` | Godkänn | `hörnpunkter` följer Blender-terminologin och räckvidden återges korrekt. |
| 32 | `transform.rst:120` | Godkänn | `objektläge` är UI-belagt; `Bone.004` och `B-Bone` lämnas korrekt oförändrade. |
| 33 | `transform.rst:126` | Godkänn | Exakt UI-belagd operator. |
| 34 | `transform.rst:131` | Godkänn | Menyvägen matchar den godkända operatoröversättningen. |
| 35 | `symmetrize.rst:20` | Godkänn | `Action Constraints` och RST-målet bevaras som formellt namn; `nyckelbildrutor` och `målåtgärden` följer terminologin. |

## Slutsats

29 kandidater godkänns, 6 ska justeras enligt de fullständiga ersättande
`msgstr`-raderna ovan och 0 ska utelämnas. De sex ändringarna är avgränsade
till stil, etablerad UI-terminologi eller den semantiska riktningen i
benhierarkin.
