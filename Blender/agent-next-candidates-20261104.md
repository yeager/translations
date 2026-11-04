# Blender Manual – nästa kandidatgranskning: Pose Mode-redigering

Datum: 2026-11-04  
Källa: `exports/2026-11-04/blender-manual-manual-sv.po` (råexport, endast
läsning) och `exports/2026-11-04/blender-ui-ui-sv.po`.  
Omfattning: 33 säkra kandidater i
`animation/armatures/posing/editing/`. Ingen PO-fil har ändrats.

## Avgränsning och terminologi

Kandidatens referenser förekommer inte i de tidigare manuella häftena
1–28 eller i den parallella armaturgranskningen. De kan därför bilda ett
eget häfte efter motgranskning.

UI-råexporten ger direkta belägg för följande namn:

- *Copy Pose* → `Kopiera pose`
- *Paste Pose* → `Klistra in pose`
- *Clear Transform* → `Rensa transformering`
- *Propagate* → `Sprid`
- *Inverse Kinematics* → `Invers kinematik`
- *Add IK to Bone* → `Lägg till IK på ben`
- *End Frame* → `Slutbildruta`
- *Viewport Display* → `Visning i visningsområde`

RST-roller, referensmål, kortkommandon, literalvärden och formella
API-namn ska bevaras exakt när en deltafil skapas.

## Kandidater

| Nr | Referens | Källtext | Råexportens svenska | Föreslagen svenska |
| --- | --- | --- | --- | --- |
| 1 | `apply.rst:32` | `Pose as Rest Pose` | `Pose som vilopose` | `Pose som viloposition` |
| 2 | `apply.rst:47` | `Pose Selected as Rest Pose` | `Pose vald som vilopose` | `Markera pose som viloposition` |
| 3 | `apply.rst:49` | `Similar to *Pose as Rest Pose*, but only applies the selected bones.` | `Samma som *Pose as Rest Pose* men gäller endast för markerade ben.` | `Liknar *Pose as Rest Pose*, men tillämpas bara på de markerade benen.` |
| 4 | `apply.rst:51` | `Unselected bones retain their original rest pose transforms.` | `Namnet på det spår som spårinformationen ska hämtas från.` | `Omarkerade ben behåller sina ursprungliga vilopositionstransformeringar.` |
| 5 | `apply.rst:57` | `Visual Transform to Pose` | `Visuell omvandling till pose` | `Visuell transformering till pose` |
| 6 | `apply.rst:59` | `Applies the evaluated visual transforms of bones after constraints are evaluated.` | *(tom)* | `Tillämpa de utvärderade visuella transformeringarna för benen efter att begränsningarna har utvärderats.` |
| 7 | `apply.rst:61` | `This converts the final constrained position, rotation, and scale into regular pose transforms, allowing constraints to be removed while preserving the current visual result.` | *(tom)* | `Detta omvandlar den slutliga begränsade positionen, rotationen och skalningen till vanliga posetransformeringar, så att begränsningar kan tas bort utan att det aktuella visuella resultatet ändras.` |
| 8 | `apply.rst:65` | `This is useful for baking constrained poses, preparing rigs for export, or simplifying complex constraint setups.` | *(tom)* | `Detta är användbart för att baka begränsade poser, förbereda riggar för export eller förenkla komplexa begränsningsuppsättningar.` |
| 9 | `apply.rst:72` | `Assign Custom Property Values as Default` | `Tilldela anpassade egenskapsvärden som standard` | `Ange värden för anpassade egenskaper som standardvärden` |
| 10 | `apply.rst:74` | `Stores the current values of custom properties as their default values.` | `Tilldela de aktuella värdena för anpassade egenskaper som deras standardvärden, för användning som en del av rest pose-status i NLA-spårmixning.` | `Lagrar de aktuella värdena för anpassade egenskaper som deras standardvärden.` |
| 11 | `apply.rst:76` | `These defaults are used as part of the armature's rest state for :doc:`NLA </editors/nla/index>` track blending and animation evaluation.` | *(tom)* | `Dessa standardvärden används som en del av armaturens viloläge för :doc:`NLA </editors/nla/index>`-spårblandning och utvärdering av animeringar.` |
| 12 | `apply.rst:79` | `This is useful when rigs rely on custom properties to control rig behavior, IK/FK switching, corrective shapes, or driver-based systems.` | *(tom)* | `Detta är användbart när riggar använder anpassade egenskaper för att styra riggbeteende, IK/FK-växling, korrigerande former eller drivarbaserade system.` |
| 13 | `clear.rst:4` | `Clear Transform` | `Tydlig omvandling` | `Rensa transformering` |
| 14 | `clear.rst:9` | `:menuselection:`Pose --> Clear Transform`` | `:menuselection:`Pose --> Clear Transform`` | `:menuselection:`Pose --> Rensa transformering`` |
| 15 | `clear.rst:11` | `Once you have transformed some bones, if you want to return to their rest position, just clear their transformations.` | `När du har transformerat några ben och vill återgå till deras viloposition är det bara att ta bort transformationen.` | `När du har transformerat några ben kan du återgå till deras viloposition genom att rensa deras transformeringar.` |
| 16 | `clear.rst:23` | `Location, Rotation, Scale :kbd:`Alt-G`, :kbd:`Alt-R`, :kbd:`Alt-S`` | `Placering, Rotation, Skala :kbd:`Alt-G`, :kbd:`Alt-R`, :kbd:`Alt-S`` | `Plats, rotation, skala :kbd:`Alt-G`, :kbd:`Alt-R`, :kbd:`Alt-S`` |
| 17 | `clear.rst:24` | `Clears individual transforms.` | `Rensar enskilda transformationer.` | `Rensar enskilda transformeringar.` |
| 18 | `clear.rst:33` | `Reset Unkeyed` | `Återställning okeyed` | `Återställ ej nyckelbildsatta` |
| 19 | `clear.rst:34` | `Clears the transforms to their keyframe state.` | `Återställer transformatorerna till deras keyframe-läge.` | `Återställer transformeringarna till deras nyckelbildrutetillstånd.` |
| 20 | `clear.rst:37` | `Operate on just the selected or all bones.` | `Operera bara det valda benet eller alla ben.` | `Använd på enbart de markerade benen eller på alla ben.` |
| 21 | `copy_paste.rst:4` | `Copy/Paste Pose` | `Kopiera/klistra in pose` | `Kopiera/klistra in pose` *(godkänn och ta bort fuzzy om den finns)* |
| 22 | `copy_paste.rst:6` | `Blender allows poses to be copied between armatures using a temporary pose buffer. Poses can be pasted normally or mirrored across the X axis.` | *(tom)* | `Blender låter dig kopiera poser mellan armaturer med hjälp av en tillfällig posebuffert. Poser kan klistras in normalt eller speglas över X-axeln.` |
| 23 | `copy_paste.rst:13` | `Copy Pose` | `Kopiera Pose` | `Kopiera pose` |
| 24 | `copy_paste.rst:18` | `:menuselection:`Pose --> Copy Pose`` | `:menuselection:`Pose --> Apply`` | `:menuselection:`Pose --> Kopiera pose`` |
| 25 | `copy_paste.rst:21` | `Copies the pose of the selected bones to the pose buffer. Only selected bones are included, allowing individual parts of a pose to be copied.` | *(tom)* | `Kopierar posen för de markerade benen till posebufferten. Bara markerade ben tas med, vilket gör att enskilda delar av en pose kan kopieras.` |
| 26 | `copy_paste.rst:28` | `Paste Pose` | `Paste Pose` | `Klistra in pose` |
| 27 | `copy_paste.rst:33` | `:menuselection:`Pose --> Paste Pose`` | `:menuselection:`Pose --> Propagera`` | `:menuselection:`Pose --> Klistra in pose`` |
| 28 | `copy_paste.rst:36` | `Applies the transforms stored in the pose buffer to bones in the active armature. Bones are matched by name, so only bones with corresponding names are affected.` | *(tom)* | `Tillämpa transformeringarna som lagrats i posebufferten på benen i den aktiva armaturen. Ben matchas efter namn, så endast ben med motsvarande namn påverkas.` |
| 29 | `copy_paste.rst:39` | `Flipped on X-Axis` | `Vänd axel` | `Speglad över X-axeln` |
| 30 | `copy_paste.rst:40` | `Mirrors the pasted pose across the X axis. This is useful for transferring poses between opposite sides of an armature, such as from the left arm to the right arm.` | *(tom)* | `Speglar den inklistrade posen över X-axeln. Detta är användbart för att överföra poser mellan motsatta sidor av en armatur, till exempel från vänster arm till höger arm.` |
| 31 | `copy_paste.rst:43` | `On Selected Only` | `Endast utvalda ben` | `Endast markerade` |
| 32 | `copy_paste.rst:44` | `Applies the stored pose only to selected bones. When disabled, all bones with matching names can be affected, regardless of selection.` | *(tom)* | `Tillämpa den lagrade posen endast på markerade ben. När alternativet är inaktiverat kan alla ben med matchande namn påverkas, oavsett markering.` |
| 33 | `copy_paste.rst:53` | `Paste Pose Flipped` | `Klistra in Pose Flippad` | `Klistra in speglad pose` |

## Föreslagen fortsättning

Skapa efter oberoende motgranskning två deltafiler med 17 respektive 16
poster.
Validera varje delta separat med `msgfmt --check`, l10n-lint, svlang,
Hunspell, terminologijämförelse, `git diff --check` och Gitleaks innan den
läggs till i en uppladdningsbatch.
