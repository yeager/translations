# Blender Manual: svensk granskningsbatch 2

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 10 strängar från Node Wrangler och Rigify.

Batchen ersätter fuzzy-översättningar där källtexten ändrats eller där svensk
text fortfarande innehöll engelska gränssnittsetiketter och direktöversatta
idiom. Den följer aktuella Blender UI-termer:

- `Properties` → `Egenskaper`
- `Armatures` → `Armaturer`
- `Axis` → `Axel`
- `Target Rig` → `Målrigg`
- `Post Generation` → `Efter generering`

Efterkontrollen den 5 november ersätter den felaktiga formen
*Kompositering* med **Kompositör** i den synliga `:guilabel:`-etiketten.
Detta följer UI-katalogen och samma editorbenämning i Node Wrangler-batch 57.

Menynamnen i den första strängen följer den aktuella menystrukturen. Sphinx-
markeringen, interna namn som `RIG-`, `Shader` och Rigify-benens identifierare
är bevarade. Råexporten är oförändrad; detta är en separat deltafil.
