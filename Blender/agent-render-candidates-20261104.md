# Kandidater: Blender Manual — material och förskjutning

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`  
Avgränsning: `render/materials/components/displacement.rst` samt
`render/materials/legacy_textures/types/index.rst`. Inga befintliga
Blender-batcher innehåller posterna nedan.

| Referens | Exakt `msgid` | Föreslagen `msgstr` | Skäl |
| --- | --- | --- | --- |
| `components/displacement.rst:7` | `To create displacement, connect a :doc:\`Displacement </render/shader_nodes/displacement/displacement>\` or :doc:\`Vector Displacement </render/shader_nodes/displacement/vector_displacement>\` node to the displacement input of the Material Output node. Procedural, painted or baked textures can then be connected to these nodes.` | `För att skapa förskjutning ansluter du en :doc:\`Förskjutning </render/shader_nodes/displacement/displacement>\`- eller :doc:\`Vektorförskjutning </render/shader_nodes/displacement/vector_displacement>\`-nod till förskjutningsingången i Material Output-noden. Procedurella, målade eller bakade texturer kan sedan anslutas till dessa noder.` | Rättar två trasiga RST-destinationer, använder UI-formerna *Förskjutning* och *Vektorförskjutning* och följer manualens etablerade form *procedurella texturer*. |
| `components/displacement.rst:50` | `It requires the mesh to be finely subdivided, which can be memory intensive. :ref:\`Adaptive Subdivision <modifiers-generate-subsurf-adaptive-subdivision>\` is the best way to subdivide the mesh, so that exactly the right amount of subdivision is used depending on the distance of the object to the camera.` | `Det kräver att meshen är fint underindelad, vilket kan vara minneskrävande. :ref:\`Adaptiv indelning <modifiers-generate-subsurf-adaptive-subdivision>\` är det bästa sättet att underindela meshen, så att exakt rätt mängd underindelning används utifrån objektets avstånd till kameran.` | Bevarar korrekt `:ref:`-mål, ersätter felaktig `:doc:`-roll och följer UI-katalogens form *Adaptiv indelning*. |
| `legacy_textures/types/index.rst:4` | `Legacy Texture Types` | `Äldre texturtyper` | Befintlig måltext utelämnar *Types*; sammansättningen är sakligt och språkligt korrekt. |

## Medvetet utelämnat

Posten om derivataförskjutning i `clouds.rst:31` har en svensk språklig brist,
men dess exakta betydelse kräver först kontroll mot Blenders äldre
texturimplementering. Den tas därför inte med som säker kandidat.

Före införande ska varje källa åter hämtas från råexporten och resultatet
kontrolleras med msgfmt, l10n-lint, svlang, Hunspell, gitleaks och
`git diff --check`.
