# Införandeplan: Blender Manual — `link_append.rst`

Underlag: två oberoende granskningskedjor för
`agent-linkappend-deep-*` och `agent-linkappend-extra-*`.
Endast följande 22 poster har en verifierad källpost, bevarad RST-markering
och en slutlig svensk form. De kan föras in i ett nytt delta. Poster som
ursprungligen avslogs har bara tagits med när motgranskningen angav en exakt
ersättning.

| Referens | Slutlig `msgstr` |
| --- | --- |
| `link_append.rst:28` | `:menuselection:\`Arkiv --> Länka...\`` |
| `link_append.rst:30` | `*Länka* skapar en referens till data i en källfil så att ändringar som görs där återspeglas i den aktuella filen nästa gång den läses in på nytt. I :doc:\`filbläddraren </editors/file_browser>\` navigerar du till den externa källfilen av typen blend och väljer de datablock du vill återanvända.` |
| `link_append.rst:35` | `Länkade datablock visas med en kedjeikon i :doc:\`Outliner </editors/outliner/introduction>\`. De listas också i Outliners *Blender-fil* :ref:\`bpy.types.SpaceOutliner.display_mode\`, tillsammans med sökvägen till den blend-fil de kommer från.` |
| `link_append.rst:43` | `Om du länkar en samling med *Instanssamlingar* aktiverat eller :doc:\`objektdata </scene_layout/object/introduction>\` med *Instansobjektdata* aktiverat, refereras samlingen respektive objektdata genom ett objekt som skapas i den aktuella blend-filen och som *kan* transformeras. (Det nya objektet skapas vid :ref:\`editors-3dview-3d_cursor\`.)` |
| `link_append.rst:48` | `Du kan också redigera eller animera länkade (och därmed normalt låsta) datablock till viss del med :doc:\`biblioteksåsidosättanden </files/linked_libraries/library_overrides>\`.` |
| `link_append.rst:53` | `Eftersom länkade data inte är redigerbara kan de inte :ref:\`skyddas med alternativet Falsk användare <data-system-datablock-fake-user>\`. Att lägga till en :doc:\`anpassad egenskap </files/custom_properties>\` som pekar på ett annars oanvänt länkat datablock (t.ex. ett textblock) är ett bra sätt att behålla referensen vid sparning och omladdning.` |
| `link_append.rst:73` | `När den är aktiverad läggs varje länkad samling till i scenen som en :doc:\`samlingsinstans </scene_layout/object/properties/instancing/collection>\` (det vill säga ett enda objekt som representerar hela samlingen). Du kan lägga till fler sådana instanser via :menuselection:\`Lägg till --> Samlingsinstans\` eller ersätta en instans med samlingens innehåll med hjälp av :ref:\`bpy.ops.object.duplicates_make_real\`.` |
| `link_append.rst:79` | `När den är inaktiverad läggs samlingarna till i befintligt skick så att du kan se deras innehåll i Outliner och skapa biblioteksåsidosättanden.` |
| `link_append.rst:82` | `När funktionen är aktiverad skapas ett objekt för varje direkt länkad objektdata. I annat fall skapas inget objekt och objektdata syns inte i scenen förrän du själv skapar ett, till exempel genom att dra objektdata från Outliner till 3D-vyporten.` |
| `link_append.rst:126` | `När den är aktiverad läggs varje tillagd samling till i scenen som en :doc:\`samlingsinstans </scene_layout/object/properties/instancing/collection>\` (det vill säga ett enda objekt som representerar hela samlingen). Du kan lägga till fler sådana instanser via :menuselection:\`Lägg till --> Samlingsinstans\` eller ersätta en instans med samlingens innehåll med hjälp av :ref:\`bpy.ops.object.duplicates_make_real\`.` |
| `link_append.rst:135` | `När funktionen är aktiverad skapas ett objekt för varje direkt tillagd objektdata. I annat fall skapas inget objekt och objektdata syns inte i scenen förrän du själv skapar ett, till exempel genom att dra objektdata från Outliner till 3D-vyporten.` |
| `link_append.rst:140` | `Markerar de tillagda datablocken som :ref:\`Protected <data-system-datablock-fake-user>\`.` |
| `link_append.rst:155` | `När Outliner är inställd på *Blender-fil* :ref:\`bpy.types.SpaceOutliner.display_mode\` kan du högerklicka på en länkad blend-fil och välja *Ladda om* för att omedelbart uppdatera den aktuella blend-filen med den senaste versionen av de länkade datablocken, utan att behöva öppna filen igen.` |
| `link_append.rst:168` | `När Outliner är inställd på *Blender-fil* :ref:\`bpy.types.SpaceOutliner.display_mode\` visas alternativet *Flytta* när du högerklickar på ett bibliotek (en länkad blend-fil). Det låter dig ersätta biblioteket med en annan fil. Det kan användas för att antingen åtgärda ett trasigt länkat bibliotek, till exempel eftersom filen har flyttats eller bytt namn, eller för att växla till en variant av samma data i en annan fil.` |
| `link_append.rst:178` | `Om Blender inte kan hitta ett bibliotek när en blend-fil laddas skapas platshållardatablock som ersätter de länkade datablock som saknas. På så sätt går referenser till de saknade data inte förlorade, och genom att ange den nya platsen för det saknade biblioteket kan de förlorade data automatiskt återställas.` |
| `link_append.rst:190` | `:menuselection:\`Kontextmeny --> Datablock --> Flytta\`` |
| `link_append.rst:192` | `När du högerklickar på ett länkat ID visas alternativet *Flytta* i undermenyn *Datablock*. Det gör det möjligt att ersätta ett direktlänkat ID med ett annat från samma eller ett annat bibliotek. Det kan användas för att antingen åtgärda ett trasigt länkat datablock, till exempel eftersom ID:t har bytt namn, eller växla till en variant av samma data.` |
| `link_append.rst:212` | `:menuselection:\`Objekt --> Relationer --> Gör lokalt...\`` |
| `link_append.rst:217` | `:menuselection:\`Kontextmeny --> Datablock --> Gör lokalt\`` |
| `link_append.rst:228` | `Åtgärden i Outliners kontextmeny har inga alternativ och påverkar endast de valda datablocken.` |
| `link_append.rst:231` | `Åtgärden i 3D-vyporten påverkar endast de valda objekten, men kan även göra objektens beroenden lokala:` |
| `link_append.rst:235` | `Om endast själva objekten ska göras lokala eller även deras data och material.` |

## Utelämnat

- Den felaktigt angivna fristående källposten för `link_append.rst:103`.
- Kandidater med osäker eller konkurrerande UI-terminologi utöver de
  uttryckliga ersättningar som redan finns i tabellen.

Innan införande måste varje rad hämtas från råexporten med sin exakta `msgid`;
deltafilen ska därefter valideras med `msgfmt`, l10n-lint, svlang, Hunspell,
Gitleaks och `git diff --check`.
