# Blender Manual: svensk granskningsbatch 4

Datum: 2026-11-04  
Källa: aktuell export av `manual-sv.po`.  
Omfattning: 19 strängar från glTF-exportens alfa, ljus och animering.

Batchen kompletterar saknade svenska måltexter och rättar fuzzy-poster med
felaktig betydelse. Särskilt viktiga avgränsningar:

- Numeriska tröskelvärden skrivs med svensk decimalkomma, medan uttrycket
  ``1 - (alpha < cutoff)`` behålls som kod.
- Blender-gränssnittets etablerade `Action Slot` → `åtgärdsslot` används.
- glTF-tillägg som `KHR_materials_dispersion` och
  `EXT_meshopt_compression` är registrerade protokollidentifierare och
  lämnas därför exakt oförändrade.
- Länkar går till källans `main`-gren.

`l10n-lint` kan markera de fyra registrerade protokollidentifierarna som
identiska med källtexten. Det är väntade falska positiva träffar; varje
identifierare måste vara byteidentisk med glTF-specifikationen.

Råexporten ändras inte. Detta är en separat deltafil och räknas in i den
kommande inskickssatsen på 500–1 000 strängar för manualkomponenten.
