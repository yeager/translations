# Oberoende granskning: Blender Manual, batch 15

Granskad fil: `blender-manual-sv-review-batch-20261104-15.po`  
Jämförd med: `exports/2026-11-04/blender-manual-manual-sv.po` och den
svenska Blender-UI-katalogen.  
Omfattning: samtliga 11 poster.

| Källa | Bedömning | Kommentar |
| --- | --- | --- |
| `Coordinate System Orientation` | Godkänd | `Koordinatsystemets orientering` är idiomatiskt och tydligare än den gamla, ordagranna formuleringen. |
| `If the imported USD is Y up …` | Godkänd | *uppåtriktning* stämmer med UI-katalogens tekniska bruk. Rotobjekt och Z-uppåtriktning återger transformationsriktningen korrekt. |
| `Import Options` | Godkänd | `Importalternativ` är etablerad Blender- och svensk UI-terminologi. |
| `Import UsdGeomCamera primitives …` | Godkänd | Kodidentifieraren, bindestrecket i `UsdGeomCamera`-primitiver och RST-referensen är bevarade. `kameraobjekt` används i UI-katalogen. |
| `Supported camera attributes include:` | Godkänd | Rättar det sakfel där den gamla texten felaktigt nämnde GPU:er. |
| `Projection type (perspective and orthographic)` | Korrigera | Byt exakt till `Projektionstyp (perspektivisk eller ortografisk)`. Nuvarande `perspektiv och ortografisk` blandar substantiv och adjektiv och *och* antyder felaktigt att båda lägen gäller samtidigt. |
| `Depth of field distance.` | Godkänd | `Skärpedjupsavstånd` är ett kompakt fackuttryck; UI-katalogens längre formulering `Avstånd till fokuspunkten för skärpedjupet` stödjer innebörden. |
| `F-stop (aperture).` | Godkänd | `Bländartal` är UI-katalogens term för *F-Stop*; förklaringen *bländaröppning* bevarar källans parentes. |
| `Clipping start and end.` | Godkänd | `Klippningsstart och -slut` är korrekt sammansatt och bevarar intervallbetydelsen. |
| `Sensor shift (tilt) X and Y.` | Godkänd | `Sensorförskjutning` är kontextuellt korrekt; `i X- och Y-led` gör axelrelationen tydlig. |
| `Sensor size (aperture width and height).` | Godkänd | `Sensorstorlek` ligger i linje med UI-katalogen. Parentesen återger källans tekniska precisering utan att förlora bredd/höjd. |

## Slutsats

Tio av elva poster kan godkännas. En språklig rättelse behövs för
projektionstyperna innan batchen arkiveras som slutligt kvalitetssäkrad.
Inga RST-markup-, platshållar- eller identifierarproblem hittades.

## Huvudgranskning

Genomgången är kontrollerad mot källsträngen och godkänns. Den enda
föreslagna ändringen förs in som en separat korrigeringsdeltafil, så att
den tidigare arkiverade batchen förblir spårbar. Ingen annan ändring
behövs i batch 15.
