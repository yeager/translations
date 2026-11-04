# Extra kandidater: Blender Manual — länkade bibliotek

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` och
`exports/2026-11-04/blender-ui-ui-sv.po`.

Avgränsning: ytterligare säkra poster i
`files/linked_libraries/link_append.rst`. Poster som redan finns i de
tidigare kandidatunderlagen eller i en befintlig granskningsbatch har
utelämnats. Detta är endast ett kandidatunderlag; råexporten och
deltafilerna är orörda.

| Referens | Exakt `msgid` | Föreslagen `msgstr` | Evidens |
| --- | --- | --- | --- |
| `link_append.rst:30` | `*Link* creates a reference to data in a source file such that changes made there will be reflected in the current file the next time it is reloaded. In the :doc:`File Browser </editors/file_browser>`, navigate to the external source blend-file and select the data-blocks you want to reuse.` | `*Link* skapar en referens till data i en källfil så att ändringar som görs där återspeglas i den aktuella filen nästa gång den läses in på nytt. I :doc:`filbläddraren </editors/file_browser>` navigerar du till den externa käll-blend-filen och väljer de datablock du vill återanvända.` | UI-katalogen har `File Browser` → `Filbläddrare`; RST-målet bevaras. |
| `link_append.rst:35` | `Linked data-blocks are indicated with a chain icon in the :doc:`Outliner </editors/outliner/introduction>`. They're also listed in the Outliner's *Blender File* :ref:`bpy.types.SpaceOutliner.display_mode`, along with the path of the blend-file they originate from.` | `Länkade datablock visas med en kedjeikon i :doc:`Outliner </editors/outliner/introduction>`. De listas också i Outliners *Blender-fil* :ref:`bpy.types.SpaceOutliner.display_mode`, tillsammans med sökvägen till den blend-fil de kommer från.` | `Blender File` har i UI-katalogen den synliga formen `Blender-fil`; RST bevaras. |
| `link_append.rst:48` | `You can also do some level of editing/animating on linked (and thus normally locked) data-blocks using :doc:`Library Overrides </files/linked_libraries/library_overrides>.`` | `Du kan också redigera eller animera länkade (och därmed normalt låsta) datablock till viss del med :doc:`biblioteksåsidosättningar </files/linked_libraries/library_overrides>.`` | UI-katalogen har `Library Overrides` → `Biblioteksåsidosättningar`; målet i `:doc:` är oförändrat. |
| `link_append.rst:53` | `Since it is not editable, linked data cannot be :ref:`protected with the Fake User option <data-system-datablock-fake-user>`. Adding a :doc:`custom property </files/custom_properties>` pointing to an otherwise unused linked data-block (e.g. a Text block) is a good way to keep it referenced across saves and reloads.` | `Eftersom länkade data inte är redigerbara kan de inte :ref:`skyddas med alternativet Falsk användare <data-system-datablock-fake-user>`. Att lägga till en :doc:`anpassad egenskap </files/custom_properties>` som pekar på ett annars oanvänt länkat datablock (t.ex. ett textblock) är ett bra sätt att behålla referensen vid sparning och omladdning.` | UI-katalogen belägger `Fake User` → `Falsk användare` och `custom property` → `anpassad egenskap`; RST-målen bevaras. |
| `link_append.rst:82` | `When enabled, an object will be created for each directly linked object data. Otherwise, no object will be created and the object data will not be visible in the scene until you create one yourself (e.g. by dragging the object data from the Outliner into the 3D Viewport).` | `När funktionen är aktiverad skapas ett objekt för varje direkt länkad objektdata. I annat fall skapas inget objekt och objektdata syns inte i scenen förrän du själv skapar ett, till exempel genom att dra objektdata från Outliner till 3D-vyporten.` | UI-katalogen har `3D Viewport` → `3D-vyport`; den tidigare kandidatomgången ändrade endast den parallella *Append*-posten. |
| `link_append.rst:103` | `In the :doc:`File Browser </editors/file_browser>`, navigate to the external source blend-file and select the data-blocks you want to reuse.` | `I :doc:`filbläddraren </editors/file_browser>` navigerar du till den externa käll-blend-filen och väljer de datablock du vill återanvända.` | Samma belagda UI-term som i post 1; RST-målet bevaras. |
| `link_append.rst:155` | `When the Outliner is in the *Blender File* :ref:`bpy.types.SpaceOutliner.display_mode`, you can right-click a linked blend-file and choose *Reload* to immediately update the current blend-file with the latest version of the linked data-blocks, without having to reopen the file.` | `När Outliner är inställd på *Blender-fil* :ref:`bpy.types.SpaceOutliner.display_mode` kan du högerklicka på en länkad blend-fil och välja *Ladda om* för att omedelbart uppdatera den aktuella blend-filen med den senaste versionen av de länkade datablocken, utan att behöva öppna filen igen.` | UI-katalogen belägger `Blender File` → `Blender-fil` och `Reload` → `Ladda om`; `:ref:`-målet är oförändrat. |
| `link_append.rst:212` | `:menuselection:`Object --> Relations --> Make Local...`` | `:menuselection:`Objekt --> Relationer --> Gör lokalt...`` | UI-katalogens operatör `Make Local` är `Gör lokalt`; den befintliga måltextens `Gör lokal` har fel genus. |
| `link_append.rst:235` | `Whether to localize only the objects themselves, or also their data and materials.` | `Om endast själva objekten ska göras lokala eller även deras data och material.` | I Blender betyder *localize* här *make local*, inte språklokalisering; formuleringen följer UI-operatorn `Gör lokalt`. |

## Avgränsning och risk

- De redan dokumenterade kandidaterna för rubriken, `Append`, samlingar,
  `Relocate`, `Data-block` och `Kontextmeny` upprepas inte här.
- RST-mål, menyformat och code-/produktnamn måste kontrolleras oförändrade
  när en deltafil skapas.
- `Text block` i post 4 är inte en synlig UI-etikett i denna mening utan ett
  exempel på ett datablock; `textblock` är föreslagen svensk fackterm och bör
  motgranskas före införande.
