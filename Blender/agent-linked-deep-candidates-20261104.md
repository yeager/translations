# Kandidater: Blender Manual — omsynkronisering, länkning och tillägg

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`  
Avgränsning: `files/linked_libraries/library_overrides.rst` och början av
`files/linked_libraries/link_append.rst`.  
Status: kandidatunderlag; råexport och befintliga deltafiler är orörda.

| Referens | Exakt `msgid` | Föreslagen `msgstr` | Motivering |
| --- | --- | --- | --- |
| `library_overrides.rst:385` | `Resync Enforce` | `Tvinga omsynkronisering` | Matchar den aktuella Blender-UI-katalogens operatoröversättning. |
| `library_overrides.rst:411` | `Remove the whole library override hierarchy, and replace all of these override data-blocks by their original linked data-blocks. This fully reverts the *Make* operation.` | `Ta bort hela biblioteksåsidosättningshierarkin och ersätt alla dessa åsidosättningsdatablock med deras ursprungliga länkade datablock. Detta återställer *Make*-åtgärden helt.` | Tar bort den felaktiga ägandekonstruktionen *bibliotekets åsidosättningshierarki* och gör *Make* till en sammanhängande UI-åtgärd. |
| `link_append.rst:3` | `Link & Append` | `Länka och lägg till` | *Append* är en importåtgärd; *bifoga* är här otydligt och skiljer sig från den aktuella menyöversättningen *Lägg till...*. |
| `link_append.rst:11` | `Instead of using the menu, you can also Link/Append blend-files by dragging and dropping them into the Blender window.` | `I stället för att använda menyn kan du också länka till eller lägga till blend-filer genom att dra och släppa dem i Blender-fönstret.` | Rättar den onaturliga och felböjda formen *länka/tillägga*. |
| `link_append.rst:72` | `Instance Collections` | `Instanssamlingar` | Är det vedertagna substantivet för samlingar som instansieras; den befintliga formen *Samlingar av instanser* ändrar relationen. |
| `link_append.rst:81` | `Instance Object Data` | `Instansobjektdata` | Följer Blender-sammansättningarna *objektdata* och *instanssamling*. |
| `link_append.rst:253` | `Scene-Level Settings` | `Inställningar på scennivå` | Svensk sammansättning utan den felaktiga bindningen i *scen-nivå*. |
| `link_append.rst:265` | `Referencing :ref:`compressed <files-blend-compress>` blend-files may need a lot of memory because they have to be loaded in their entirety, even if you only link/append a small part of them. Once the data-blocks are loaded, however, memory usage is the same.` | `Att referera till :ref:`komprimerade <files-blend-compress>` blend-filer kan kräva mycket minne eftersom de måste läsas in helt, även om du bara länkar till eller lägger till en liten del av dem. När datablocken väl har lästs in är minnesanvändningen dock densamma.` | Den nuvarande måltexten böjer inte *komprimerad* till plural och innehåller det felaktiga verbet *tillägger*. |

## Markup- och UI-risker

- Menysökvägarna med *Troubleshoot* måste jämföras med den faktiska
  svenska Blender-menyn innan de översätts. UI-katalogen styrker
  `Context Menu` → `Kontextmeny`, `Library Override` →
  `Biblioteksåsidosättning` och `Resync Enforce` →
  `Tvinga omsynkronisering`, men ger ingen entydig menyöversättning för
  *Troubleshoot* i denna export.
- Behåll `:menuselection:`, `:ref:`-målen, `*Make*`, `blend-fil` och
  `data-block`-motsvarigheten *datablock* i exakt rätt teknisk kontext.
- Förslagen är kandidater. Huvudagenten ska kontrollera den exakta
  råexportposten och besluta om deltafil innan något räknas som granskat.
