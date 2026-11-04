# Oberoende granskning: Blender Manual, batch 20

Granskad fil: `blender-manual-sv-review-batch-20261104-20.po`  
Jämförd med: råexporten för Blender Manual och Blender-UI-katalogen.  
Omfattning: samtliga 8 poster.

| Källa | Bedömning | Kommentar |
| --- | --- | --- |
| USD-hierarkisammanslagning | Godkänd | `Xform` och ``UsdGeomGprims`` behålls som tekniska namn; svensk meningsstruktur är naturlig. |
| Triangulering | Godkänd | *Trianguleringsmodifieraren* återger RST-länkens synliga namn och behåller destinationen. |
| Materialdelmängder | Godkänd | *Geometridelmängd*, *Hydra-vyn* och `USD-ärende nr 542` återger sammanhanget korrekt; URL bevaras. |
| `Displacement Support` | Godkänd | Blender-UI använder konsekvent *förskjutning* för *Displacement*. |
| USD Preview Surface-nätverk | Godkänd | Produktnamnet är bevarat och svensk sammansättning används bara i den förklarande delen. |
| `opacityThreshold` | Godkänd | Kodvärdena ``opacityThreshold``, ``Round`` och formeln ``1 - (value < threshold)`` är oförändrade; decimaltecknet har lokaliserats i löptexten. |
| USDZ-nedsampling | Godkänd | Svensk sammansättning och pluralen *texturer* är korrekta. |

## Slutsats

Alla åtta poster godkänns utan följdrättelse. `msgfmt` och `l10n-lint`
är gröna. Informationsnivåns USD-träffar är kända falska positiva
valutaindikeringar, inte språk- eller formatfel.
