# Blender UI – Alembic-import och -export

## Omfattning

22 Alembic-strängar under `source/blender/io/alembic/` har
kontrollerats i läsarnas, importörens och exportörens diagnostikkontext.
De omfattar samlingar, objektvägar, typerna `Camera`, `Curves`, `PolyMesh`,
`SubD`, `NURBS`, `Points` och `XForm`, punktprov, arkiv, scen och förlopp.

## Resultat

Samtliga 22 strängar är korrekta och lämnas oförändrade. Två delade
importdiagnostiker var redan bokförda i USD-gruppen; därför tillför denna
grupp 20 nya identiteter till täckningsmätningen. `Alembic`,
`Camera`, `Curves`, `PolyMesh`, `SubD`, `NURBS`, `Points` och `XForm` är
formatspecifika eller synliga typnamn och behålls avsiktligt. De svenska
termerna `samling`, `objekttyp`, `objektsökväg`, `punktprov`, `arkiv` och
`aktuell scen` är både idiomatiska och konsekventa med Blender UI.

## Kontroller

Granskningen använde den befintliga PO-exportens källhänvisningar och
kontexten i respektive Alembic-importör/-exportör. Ingen deltafil skapas,
eftersom inga måltexter ändrades.
