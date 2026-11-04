# Införandeplan: Blender Manual — meshavfasning

Underlag: `agent-modeling-candidates-20261104.md` och den oberoende
motgranskningen i `agent-modeling-review-20261104.md`. Samtliga poster är
kontrollerade mot den lokala råexporten, Blender UI och terminologilistan.
RST-roller och destinationsmål ska bevaras exakt i nästa deltafil.

| Referens | Exakt `msgid` | Slutlig `msgstr` |
| --- | --- | --- |
| `bevel.rst:10,14` | `:menuselection:\`Vertex --> Bevel Vertices\`, :menuselection:\`Edge --> Bevel Edges\`` | `:menuselection:\`Hörnpunkt --> Fasa hörnpunkter\`, :menuselection:\`Kant --> Fasa kanter\`` |
| `bevel.rst:11,15` | `:kbd:\`Shift-Ctrl-B\` (Bevel Vertices), :kbd:\`Ctrl-B\` (Bevel Edges)` | `:kbd:\`Shift-Ctrl-B\` (Fasa hörnpunkter), :kbd:\`Ctrl-B\` (Fasa kanter)` |
| `bevel.rst:18,22` | `Cubes without and with bevel.` | `Kuber utan respektive med fasning.` |
| `bevel.rst:22,26` | `The :doc:\`/modeling/modifiers/generate/bevel\` does this non-destructively.` | `:doc:\`Avfasningsmodifieraren </modeling/modifiers/generate/bevel>\` utför detta icke-destruktivt.` |
| `bevel.rst:38,42,139,143,162,166` | `Before beveling.` | `Före fasning.` |
| `bevel.rst:42,46` | `Increased bevel width.` | `Ökad fasningsbredd.` |
| `bevel.rst:46,50` | `Increased bevel segments.` | `Fler fasningssegment.` |
| `bevel.rst:61,65` | `Bevel the selected vertices, leaving the edges unchanged.` | `Fasa de markerade hörnpunkterna utan att ändra kanterna.` |
| `bevel.rst:111,115` | `Profile Shape :kbd:\`P\`` | `Profilform :kbd:\`P\`` |
| `bevel.rst:143,147` | `Loop Slide off.` | `Slingglidning av.` |
| `bevel.rst:147,151` | `Loop Slide on.` | `Slingglidning på.` |
| `bevel.rst:155,159` | `Same as *Mark Seams*, but for :ref:\`Sharp <bpy.ops.mesh.mark_sharp>\` edges.` | `Samma som *Markera sömmar*, men för :ref:\`skarpa kanter <bpy.ops.mesh.mark_sharp>\`.` |

Alla tolv poster är klara för en separat deltafil. Före arkivering ska den
färdiga PO-filen kontrolleras med `msgfmt`, l10n-lint, svlang, Hunspell,
Gitleaks och `git diff --check`.
