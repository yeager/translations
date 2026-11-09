# Blender UI — granskning av Action och åtgärd

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

45 poster med *Action* i källtexten men utan **Action** i den svenska
måltexten har kontrollerats rad för rad. Det omfattar VR/XR-åtgärder,
tangent- och musåtgärder, operatorer, säkra marginaler och egenskaper i
importsammanhang.

## Resultat

De granskade förekomsterna avser vanliga handlingar, inte Blender-datatypen
*Action*. **åtgärd**, **åtgärdskarta**, **åtgärdssats** och relaterade
sammansättningar är därför korrekta i dessa sammanhang.

Egenskapen `BlendImportContextItem.append_action` kontrollerades mot Blenders
API-dokumentation: den beskriver hur ett datablock hanterades av
*append*-operationen. Därför är **tilläggsåtgärd** korrekt och ska inte
förväxlas med en animerings-Action.

## Avgränsning

Blender-datatypen och synliga UI-termer som *Action Slot* behåller **Action**
enligt projektets terminologi. Inga ytterligare ändringar eller deltafiler
behövdes för detta pass. Dokumentet bekräftar lokal granskning, inte import.
