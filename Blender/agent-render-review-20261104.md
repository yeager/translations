# Motgranskning: Blender Manual — material och förskjutning

Underlag: `agent-render-candidates-20261104.md`, råexporten
`exports/2026-11-04/blender-manual-manual-sv.po`, Blender UI-katalogen och
`TERMINOLOGY.md`. RST-destinationer och kodmarkering får inte ändras.

| Referens | Bedömning | Slutlig svensk form / motivering |
| --- | --- | --- |
| `components/displacement.rst:7` | Ändra | Korrigera även den synliga UI-etiketten *Material Output* till `Materialutdata`. Använd: `För att skapa förskjutning ansluter du en :doc:\`Förskjutning </render/shader_nodes/displacement/displacement>\`- eller :doc:\`Vektorförskjutning </render/shader_nodes/displacement/vector_displacement>\`-nod till förskjutningsingången i Materialutdata-noden. Procedurella, målade eller bakade texturer kan sedan anslutas till dessa noder.` Båda RST-målen är korrekta, och *Procedurell textur* är dokumenterad i manualens ordlista. |
| `components/displacement.rst:50` | Ändra | RST-rollen och målet är korrekta, men den synliga etiketten ska följa UI-katalogens *Adaptive Subdivision* → `Adaptiv underindelning`, inte den äldre manualvarianten *Adaptiv indelning*. Använd: `Det kräver att meshen är fint underindelad, vilket kan vara minneskrävande. :ref:\`Adaptiv underindelning <modifiers-generate-subsurf-adaptive-subdivision>\` är det bästa sättet att underindela meshen, så att exakt rätt mängd underindelning används utifrån objektets avstånd till kameran.` |
| `legacy_textures/types/index.rst:4` | Godkänn | `Äldre texturtyper` återger både *Legacy* och *Types* korrekt och följer svensk sammansättningspraxis. |

## Kontrollspår

- UI-exporten har *Displacement* → `Förskjutning`, *Vector Displacement* →
  `Vektorförskjutning`, *Material Output* → `Materialutdata` och *Adaptive
  Subdivision* → `Adaptiv underindelning`.
- Råexportens nuvarande översättningar har trasiga destinationer i två
  `:doc:`-roller respektive en felaktig `:doc:` i stället för `:ref:`.
- *Derivataförskjutning* lämnas utanför: den är fortfarande kontextuellt
  osäker och ska inte tas med i denna batch.

Slutsats: två poster kan föras in med de angivna följdrättelserna och en
utan ändring. Inga PO-filer eller råexporter har ändrats.
