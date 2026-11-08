# Blender UI – OTIO, PLY, OBJ och STL

## Omfattning

25 tidigare ospårade och sinsemellan unika import-/exportsträngar har
kontrollerats under `source/blender/io/otio/`, `ply/`, `wavefront_obj/` och
`stl/`. De täcker tidslinjer, remsor, klipp, effekter, bildsekvenser,
samlingar, PLY-fel, OBJ/MTL-filer och STL-filer.

## Resultat

Samtliga 25 måltexter lämnas oförändrade. Förkortningarna `OTIO`, `PLY`,
`OBJ`, `MTL` och `STL` är formatnamn. Termerna `remsa`, `klipp`, `effekt`,
`bildsekvens`, `samling`, `minnesmappa` och `filformat` är riktiga i respektive
Blender-kontext. Den delade importdiagnostiken om en redigerbar samling räknas
endast en gång i denna grupp.

## Kontroller

Granskningen utgår från respektive importör och exportör i källhänvisningarna.
Ingen deltafil skapas: ingen måltext behövde ändras.
