# Andra granskning: Blender Manual batch 20

Granskad fil: `blender-manual-sv-review-batch-20261104-20.po`
Underlag: råexportens `files/import_export/usd.rst:467–567` samt
`blender-ui-ui-sv.po` från 2026-11-04.

## Bedömning per post

| Källa | Bedömning | Motivering eller exakt följdrättelse |
| --- | --- | --- |
| USD-hierarki | Godkänd | `Xform-förälder`, ``UsdGeomGprims`` och de mellanliggande Xform-primitiverna återges korrekt. Kodmarkeringen är bevarad. |
| Triangulering | Godkänd | `meshen` och `trianguleringsmodifieraren` är kontextuellt riktiga och RST-destinationen är oförändrad. |
| Materialdelmängder | Godkänd | `geometridelmängd` beskriver USD-objektet exakt. `Hydra-vyn` är en begriplig dokumentationsterm, och URL samt länkmarkering är bevarade. |
| Displacement Support | Godkänd | `Stöd för förskjutning` följer UI-katalogens `Displacement` → `Förskjutning`. |
| Displacement-beskrivning | Godkänd | Den svenska meningen återger den felaktiga engelska källans avsedda innebörd, och RST-länktexten använder den bekräftade UI-termen `Förskjutning`. |
| USD Preview Surface Network | **Korrigera** | UI-katalogen har exakt `USD Preview Surface Network` → `Nätverk för USD Preview Surface`. Byt därför `USD Preview Surface-nätverk` mot den bekräftade formen. |
| ``opacityThreshold`` | **Korrigera** | Följ synliga Blender-etiketter: *Math* → `Matematik`, *Round* → `Runda`, *Alpha* → `Alfa` och *Principled BSDF* → `Principiell BSDF`. Rekommenderad måltext: `För att stödja ``opacityThreshold``, ibland kallat ”Alfabegränsning”, måste nodträdet antingen använda en Matematik-nod inställd på ``Runda`` om det önskade tröskelvärdet är 0,5, eller ett par Matematik-noder som implementerar ``1 - (value < threshold)``. Resultatet ska anslutas till Alfa-uttaget på Principiell BSDF-noden.` Formeln och kodidentifieraren ska vara oförändrade. |
| USDZ Texture Downsampling | **Korrigera** | Skriv `Nedsampling av USDZ-texturer`. Sammansättningen placerar produktformatet intill sitt huvudord och är idiomatisk svensk rubrikform. |

## Kontrollspår

- UI-belägg: *Displacement* → `Förskjutning`, *USD Preview Surface Network* →
  `Nätverk för USD Preview Surface`, *Math* → `Matematik`, *Round* → `Runda`,
  *Alpha* → `Alfa` och *Principled BSDF* → `Principiell BSDF`.
- Samtliga RST-roller, destinationssökvägar, URL:er och den oföränderliga
  formeln ska bevaras vid följdrättelsen.
- Ingen råexport eller deltafil har ändrats i denna granskning.
