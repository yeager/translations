# Oberoende granskning: Blender Manual batch 19

Granskad fil: `blender-manual-sv-review-batch-20261104-19.po`
Underlag: råexportens `files/import_export/usd.rst:336–457`, Blender-UI:s
svenska katalog samt projektets USD-terminologigranskning.

## Resultat per post

| Källpost | Bedömning | Motivering eller exakt följdrättelse |
| --- | --- | --- |
| USDZ export package | **Korrigera** | Byt slutet `USD och dess beroenden till texturfiler.` mot `USD och dess texturfilberoenden.`. Den senare formen är idiomatisk teknisk svenska och motsvarar precis *texture file dependencies*. Bevara URL, RST-markup och ``.usdz``. |
| Root Prim | Godkänd | `Rotprim` är den etablerade, särskilda termen för rotprimitiven i USD-hierarkin. |
| Root Prim-beskrivning | Godkänd | `transformprimitiv`, `USD-scen` och parent-relationen återger exportinställningens funktion korrekt. |
| Blender Data | Godkänd | `Blender-data` följer UI-katalogens form och svensk sammansättningspraxis. |
| Blender Names | Godkänd | `Skapa USD-anpassade attribut …` återger verbet *Author* i denna UI-kontext och behåller objekt- respektive objektdata-nivån. |
| Units / ``metersPerUnit`` | Godkänd | `USD-scenens` och kodidentifieraren är korrekta; `det valda måttet` fungerar för den valda mätinställningen. |
| Mesh Objects | Godkänd | `meshobjekt` följer projektets beslut att behålla *mesh* som Blender-fackord i denna objekt-/datatypskontext. |
| Light Objects / ``UsdLuxShapingAPI`` | Godkänd | `ljusobjekt` är UI-konsekvent; API-identifieraren och RST-rollen är oförändrade. *Spotlights* är en etablerad svensk teknisk benämning här. |
| Camera Objects | Godkänd | `kameraobjekt` och `perspektivkameror` är idiomatiska och semantiskt exakta. |
| Curve Objects | Godkänd | `kurvobjekt` är konsekvent med Blender-UI. |
| Point Cloud Objects | Godkänd | `punktmolnsobjekt` följer Blender-UI:s `Punktmoln` och sammansättningsformen för objekt. |
| Volume Objects | Godkänd | `volymobjekt` är korrekt fackterm. |
| Parent hair strands | Godkänd | `föräldrahårstrån` anger korrekt de hårstrån som är föräldrar i kurvsystemet; meningen har inte längre råexportens dubbla verb. |
| UV Maps | Godkänd | `UV-koordinater`, `mesh` och `UV-kartan` är konsekventa. Ingen kod- eller formatmarkering har ändrats. |

## Markup- och terminologikontroll

- Samtliga RST-roller (`:doc:`), deras destinationssökvägar, URL:en,
  dubbelbacktick-formateringen och API-identifierarna är bevarade.
- `Rotprim`, `USD-scen`, `punktmoln` och `mesh` stämmer med de tidigare
  dokumenterade USD-besluten och Blender-UI-katalogen.
- Enda följdrättelsen är den svenska sammansättningen `texturfilberoenden`.
  Inga övriga sak-, språk- eller markupfel hittades.
