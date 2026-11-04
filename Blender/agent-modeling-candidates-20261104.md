# Kandidater: Blender Manual — meshavfasning

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`, avsnittet
`modeling/meshes/editing/edge/bevel.rst`. Underlaget är jämfört med
`blender-ui-ui-sv.po` och `TERMINOLOGY.md`. Ingen kandidat förekommer i
tidigare Blender-batchar.

| Referens | Exakt `msgid` | Föreslagen `msgstr` | Belägg och skäl |
| --- | --- | --- | --- |
| `bevel.rst:10,14` | `:menuselection:\`Vertex --> Bevel Vertices\`, :menuselection:\`Edge --> Bevel Edges\`` | `:menuselection:\`Hörnpunkt --> Fasa hörnpunkter\`, :menuselection:\`Kant --> Fasa kanter\`` | UI: *Bevel Vertices* → `Fasa hörnpunkter`, *Bevel Edges* → `Fasa kanter`; *vertex* är hörnpunkt i meshkontext. |
| `bevel.rst:11,15` | `:kbd:\`Shift-Ctrl-B\` (Bevel Vertices), :kbd:\`Ctrl-B\` (Bevel Edges)` | `:kbd:\`Shift-Ctrl-B\` (Fasa hörnpunkter), :kbd:\`Ctrl-B\` (Fasa kanter)` | Matchar samma bekräftade operatornamn. |
| `bevel.rst:18,22` | `Cubes without and with bevel.` | `Kuber utan respektive med fasning.` | Korrekt svensk bildtext; UI använder `Avfasning` för *Bevel*. |
| `bevel.rst:22,26` | `The :doc:\`/modeling/modifiers/generate/bevel\` does this non-destructively.` | `:doc:\`Avfasningsmodifieraren </modeling/modifiers/generate/bevel>\` utför detta icke-destruktivt.` | Återställer rätt RST-länktext och UI:s *Bevel Modifier* → `Avfasningsmodifierare`. |
| `bevel.rst:38,42,139,143,162,166` | `Before beveling.` | `Före fasning.` | Kort bildtext med korrekt meshbetydelse. |
| `bevel.rst:42,46` | `Increased bevel width.` | `Ökad fasningsbredd.` | UI har *Bevel Width* som fasningsbredd i avfasningssammanhang. |
| `bevel.rst:46,50` | `Increased bevel segments.` | `Fler fasningssegment.` | Beskriver resultatet utan den felaktiga rörelsebetydelsen i nuvarande måltext. |
| `bevel.rst:61,65` | `Bevel the selected vertices, leaving the edges unchanged.` | `Fasa de markerade hörnpunkterna utan att ändra kanterna.` | Terminologin följer UI och bevarar operationens semantik. |
| `bevel.rst:111,115` | `Profile Shape :kbd:\`P\`` | `Profilform :kbd:\`P\`` | UI: *Profile Shape* → `Profilform`. |
| `bevel.rst:143,147` | `Loop Slide off.` | `Slingglidning av.` | UI: *Loop Slide* → `Slingglidning`; tillståndet återges idiomatiskt. |
| `bevel.rst:147,151` | `Loop Slide on.` | `Slingglidning på.` | Samma UI-term och parallell bildtext. |
| `bevel.rst:155,159` | `Same as *Mark Seams*, but for :ref:\`Sharp <bpy.ops.mesh.mark_sharp>\` edges.` | `Samma som *Markera sömmar*, men för :ref:\`skarpa kanter <bpy.ops.mesh.mark_sharp>\`.` | UI: *Mark Seams* → `Markera sömmar` och *Sharp Edges* → `Skarpa kanter`; RST-målet bevaras. |

## Avgränsning

Kandidaterna är avsiktligt begränsade till felöversatta eller uppenbart
föråldrade fuzzy-poster med direkt UI-belägg. Termer som `Face Strength`,
`Miter` och `Support Loops` lämnas tills deras specifika Blender-kontext är
kartlagd.
