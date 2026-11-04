# Huvudgranskning av USD-kandidater — senare exportavsnitt

Datum: 2026-11-04  
Underlag: `agent-usd-deep-candidates-20261104.md`, råexporten och
Blender-UI-katalogen.

| Kandidat | Bedömning | Slutlig rekommendation |
| --- | --- | --- |
| `USDZ Custom Downscale Size` | Korrigera | `Anpassad storlek för USDZ-nedsampling`. Denna ordföljd gör det tydligt att storleken gäller nedsamplingen. |
| `The size in pixels of the *Custom* downsampling.` | Godkänn | `Storleken i pixlar för den *anpassade* nedsamplingen.` UI-katalogens svenska använder den motsvarande betydelsen i saktext. |
| `Exporter Limitations` | Godkänn | `Exportörens begränsningar`. |
| `Single-sided and Double-sided Meshes` | Godkänn | `Enkelsidiga och dubbelsidiga mesh`. *Mesh* är etablerad Blender-datatyp. |
| USD:s dubbelsidighet | Godkänn | Använd `ytgrupp` och `enkelsidig eller dubbelsidig`; undvik den tidigare trasiga formen `enkel- / dubbelsidigt`. |
| `Only the parent strands ...` | Korrigera | `Endast föräldrahårstråna exporteras, och då bara med en konstant färg. UV-koordinater och normalinformation exporteras inte.` Det matchar den redan granskade formen i batch 19. |
| `Geometry Node Modifiers` | Godkänn | `Geometrinodmodifierare`. |
| `Instancing/Referencing` | Godkänn | `Instansiering/referenser`; *referentiering* är inte en etablerad svensk term. |
| `Exporting instanced objects ...` | Godkänn | `Export av instansierade objekt och samlingar stöds genom ett experimentellt alternativ vid USD-export.` |
| `Scene instances ...` | Godkänn | Kandidatens svenska återger källan och tar bort felaktig tillagd information i befintlig måltext. |
| UDIM/USDZ-begränsning | Godkänn | Behåll OpenUSD-URL:en exakt. `USD-pullförfrågan #2133` är acceptabel svensk teknisk term. |
| `USD Primvar data types` | Godkänn | `USD Primvar-datatyper`. |
| `Blender type` | Godkänn | `Blender-typ`; den befintliga formen `Typ av mixer` är ett sakfel. |
| `RGBA color ... displayColor ...` | Korrigera | `RGBA-färg med 32-bitars flyttalsvärden. Som specialfall hanteras en Primvar eller ett attribut för USD:s ``displayColor`` som ``color3f``-data med en alfakomponent på 1,0.` Detta bevarar kodtermer men undviker kandidatens ogrammatiska passiv. |
| `USD does not provide a byte color equivalent ...` | Korrigera | `USD har ingen motsvarighet till bytefärg. Bytevärdena konverteras till flyttal och exporteras som color4f.` Lägg inte till ny kodformatering där källan inte har någon. |

## Avgränsning

Kandidater med delade `msgid`-värden utanför USD-avsnittet ska fortsatt
granskas i projektomfattande kontext innan de ändras. Det gäller bland annat
rubrikerna `float`, `color4f`, `Byte Color` och `Quaternion`.

Resultat: 11 kandidater kan användas oförändrade, 4 kan användas med de
exakta justeringarna ovan. Inga kandidatfiler, råexporter eller tidigare
deltafiler är ändrade av denna granskning.
