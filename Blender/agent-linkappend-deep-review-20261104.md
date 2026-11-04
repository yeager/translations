# Motgranskning: Blender Manual — `link_append.rst`

Granskad mot råexporten `blender-manual-manual-sv.po` och Blender UI-katalogen
`blender-ui-ui-sv.po` (export 2026-11-04). RST-destinationer i `:doc:` och
`:ref:` får inte ändras.

| Nr | Referens | Bedömning | Resultat / exakt korrigering |
| --- | --- | --- | --- |
| 1 | `link_append.rst:28` | Godkänn | `:menuselection:\`Arkiv --> Länka...\``. UI-operatorn *Link...* är `Länka...`. |
| 2 | `link_append.rst:43` | Avslå | UI-katalogen har *Instance Collections* → `Instanssamlingar` och *Instance Object Data* → `Instansobjektdata`; dessa synliga UI-etiketter får inte lämnas på engelska. Använd: `Om du länkar en samling med *Instanssamlingar* aktiverat eller :doc:\`objektdata </scene_layout/object/introduction>\` med *Instansobjektdata* aktiverat, refereras samlingen respektive objektdata genom ett objekt som skapas i den aktuella blend-filen och som *kan* transformeras. (Det nya objektet skapas vid :ref:\`editors-3dview-3d_cursor\`.)` |
| 3 | `link_append.rst:73` | Godkänn | Kandidaten följer UI-termerna `Lägg till`, `Samlingsinstans` och bevarar RST-målen. |
| 4 | `link_append.rst:79` | Avslå | Kandidatens `biblioteksåsidosättningar` motsvarar inte den aktuella UI-rubrikens pluralform. Använd: `När den är inaktiverad läggs samlingarna till i befintligt skick så att du kan se deras innehåll i Outliner och skapa biblioteksåsidosättanden.` |
| 5 | `link_append.rst:126` | Godkänn | Samma bekräftade UI-terminologi som i post 3; `tillagd samling` återger *appended collection* korrekt. |
| 6 | `link_append.rst:135` | Godkänn | `tillagd` är rätt för *Append* och `3D-vyporten` stämmer med UI-katalogen. |
| 7 | `link_append.rst:140` | Godkänn | `tillagda datablock` rättar felaktiga `bifogade`. Länktexten *Protected* saknar här en belagd svensk UI-motsvarighet och lämnas därför oförändrad; RST-målet är intakt. |
| 8 | `link_append.rst:168` | Avslå | Tre faktiska UI-etiketter lämnades på engelska trots belagda former. Använd: `När Outliner är inställd på *Blender-fil* :ref:\`bpy.types.SpaceOutliner.display_mode\` visas alternativet *Flytta* när du högerklickar på ett bibliotek (en länkad blend-fil). Det låter dig ersätta biblioteket med en annan fil. Det kan användas för att antingen åtgärda ett trasigt länkat bibliotek, till exempel eftersom filen har flyttats eller bytt namn, eller för att växla till en variant av samma data i en annan fil.` |
| 9 | `link_append.rst:178` | Avslå | `flytta det saknade biblioteket` kan betyda att användaren flyttar filen, medan funktionen anger bibliotekets nya plats. Använd: `Om Blender inte kan hitta ett bibliotek när en blend-fil laddas skapas platshållardatablock som ersätter de länkade datablock som saknas. På så sätt går referenser till de saknade data inte förlorade, och genom att ange den nya platsen för det saknade biblioteket kan de förlorade data automatiskt återställas.` |
| 10 | `link_append.rst:190` | Godkänn | `Kontextmeny --> Datablock --> Flytta` stämmer med UI-katalogen och behåller hela `:menuselection:`-rollen. |
| 11 | `link_append.rst:192` | Avslå | Synlig UI-etikett ska följa UI-katalogen. Använd: `När du högerklickar på ett länkat ID visas alternativet *Flytta* i undermenyn *Datablock*. Det gör det möjligt att ersätta ett direktlänkat ID med ett annat från samma eller ett annat bibliotek. Det kan användas för att antingen åtgärda ett trasigt länkat datablock, till exempel eftersom ID:t har bytt namn, eller växla till en variant av samma data.` |
| 12 | `link_append.rst:217` | Godkänn | `Kontextmeny --> Datablock --> Gör lokalt` överensstämmer med aktuella UI-översättningar. |
| 13 | `link_append.rst:228` | Godkänn | `Outliners kontextmeny` är konsekvent med dokumentets menyvägar och korrekt svenska. |
| 14 | `link_append.rst:231` | Godkänn | `3D-vyporten` följer UI-katalogen och kandidatens formulering bevarar den tekniska betydelsen. |

## Kontrollspår

- UI-belägg: *Link...* → `Länka...`, *Collection Instance* →
  `Samlingsinstans`, *Relocate* → `Flytta`, *Make Local* → `Gör lokalt`,
  *Data-Block* → `Datablock`, *Blender File* → `Blender-fil`, *3D Viewport*
  → `3D-vyport`, *Instance Collections* → `Instanssamlingar` och *Instance
  Object Data* → `Instansobjektdata`.
- *Library Overrides* har flera konkurrerande översättningar i UI-katalogen.
  För den aktuella UI-rubriken används den belagda pluralformen
  `Biblioteksåsidosättanden`.
- Inga råexporter, deltafiler eller andra arbetsfiler har ändrats av denna
  motgranskning.
