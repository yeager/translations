# Motgranskning: Blender Manual — extra kandidater för länkade bibliotek

Granskad mot råexporten `blender-manual-manual-sv.po` och Blender UI-katalogen
`blender-ui-ui-sv.po` (export 2026-11-04). RST-destinationer och
`:menuselection:`-format får inte ändras.

| Nr | Referens | Bedömning | Resultat / exakt korrigering |
| --- | --- | --- | --- |
| 1 | `link_append.rst:30` | Korrigera | *Link* är den synliga åtgärden och ska följa UI-formen: `*Länka* skapar en referens till data i en källfil så att ändringar som görs där återspeglas i den aktuella filen nästa gång den läses in på nytt. I :doc:\`filbläddraren </editors/file_browser>\` navigerar du till den externa källfilen av typen blend och väljer de datablock du vill återanvända.` |
| 2 | `link_append.rst:35` | Godkänn | `Blender-fil` är den exakta UI-formen för denna Outliner-vy; RST-målet bevaras. |
| 3 | `link_append.rst:48` | Korrigera | UI-katalogens aktuella etikett är `Biblioteksåsidosättanden`, inte `biblioteksåsidosättningar`. Använd: `Du kan också redigera eller animera länkade (och därmed normalt låsta) datablock till viss del med :doc:\`biblioteksåsidosättanden </files/linked_libraries/library_overrides>\`.` |
| 4 | `link_append.rst:53` | Godkänn | `Falsk användare`, `anpassad egenskap` och `textblock` är belagda och betydelsen för den länkade datan är korrekt. |
| 5 | `link_append.rst:82` | Godkänn | `3D-vyporten` överensstämmer med UI-katalogen; den svenska meningen beskriver korrekt en direkt länkad objektdata. |
| 6 | `link_append.rst:103` | Avslå | Kandidatens angivna `msgid` förekommer inte som egen post i råexporten. Den faktiska posten på rad 69 har en annan källtext och får inte importeras med fel källa. |
| 7 | `link_append.rst:155` | Godkänn | `Blender-fil` och `Ladda om` är belagda UI-former; åtgärdens funktion är korrekt återgiven. |
| 8 | `link_append.rst:212` | Godkänn | `Gör lokalt...` rättar den felaktiga genusformen och följer UI-operatorn *Make Local*. |
| 9 | `link_append.rst:235` | Godkänn | `göras lokala` återger här Blender-åtgärden *make local*, inte språklokalisering. |

## Kontrollspår

- UI-belägg: *File Browser* → `Filbläddrare`, *Blender File* →
  `Blender-fil`, *Reload* → `Ladda om`, *Make Local* → `Gör lokalt`,
  *Fake User* → `Falsk användare` och *Library Overrides* →
  `Biblioteksåsidosättanden` i den relevanta Outliner-kontexten.
- Kandidat 6 avvisas enbart på grund av att dess påstådda källpost inte är
  exakt; den ska inte komma med i en deltafil som den står.
- Inga råexporter, deltafiler eller andra arbetsfiler ändrades.
