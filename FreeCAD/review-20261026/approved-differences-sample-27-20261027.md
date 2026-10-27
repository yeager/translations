# FreeCAD: tjugosjunde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
6690654–6691582, mot XLIFF-kontexten, den granskade FreeCAD-översättningen
och etablerad CAM-terminologi. Platshållaren `{e}` och uttrycket
`{current_name or self.library.label}` är bevarade. Inga ändringar eller röster
skickades till Crowdin.

## Bedömning

- Tretton av 20 kandidater är godtagbara i sitt sammanhang.
- `verktygsdefinition`, `verktygsbana`, `avgradning`, `planfräsning`,
  `brotsch`, `V-fräs`, `hörnradiefräs` och `mätning` används korrekt.
- Tankstrecket i bibliotekets rubrik är korrekt svenskt typografiskt tecken.

## Rättelser att kontrollera i Crowdin

- 6644244 och 6674862 `Array` ska vara `Matris`, inte `Mönster`.
- 6681254 och 6674864 ska använda `matris` i stället för `mönster`.
- 6690032 ska vara `Väljare för verktygsdefinitioner`, inte den imperativa
  formuleringen `Välj verktygsdefinition`.
- 6690052 ska vara `Formval för verktygsdefinition`, inte `Välj
  verktygsdefinitionens form`.

## Slutsats

De sex rättelserna ska först jämföras med Crowdins aktuellt valda måltexter.
Övriga 13 poster kräver inga nya Crowdin-förslag.

Noteringen om sträng-id 6644262 har tagits bort: id:t gäller `Deburr` och
inte en matrissträng. Det var en felaktig id-koppling i det tidigare
granskningsunderlaget.

## Kontroll i Crowdin 27 oktober 2026

Följande aktuellt godkända måltexter verifierades i CAM.ts och behöver
ersättas när uppladdning eller redigering i Crowdin uttryckligen godkänns:

- `CAM_Array['Array']`: `Array` → `Matris`.
- `CAM_Array['Creates an array from selected toolpaths']`:
  `Skapar en array från valda verktygsbanor` →
  `Skapar en matris från valda verktygsbanor`.
- `CAM_DressupArray['Creates an array from a selected toolpath']`:
  `Skapar en array från en vald verktygsbana` →
  `Skapar en matris från en vald verktygsbana`.

Ändringarna är ännu inte sparade i Crowdin.
