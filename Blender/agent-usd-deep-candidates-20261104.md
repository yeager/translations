# Kandidater: Blender Manual — USD-exportens senare avsnitt

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`  
Område: `files/import_export/usd.rst`, huvudsakligen rader 578–729.  
Status: kandidatunderlag; råexporten är orörd och inget är skickat upp.

Kodvärden, RST-destinationer och URL:er nedan ska behållas exakt när en
deltafil eventuellt byggs.

| Källa (`msgid`) | Föreslagen `msgstr` | Motivering |
| --- | --- | --- |
| `USDZ Custom Downscale Size` | `Anpassad USDZ-nedsamplingsstorlek` | Rättar felaktig versalisering och särskrivning. |
| `The size in pixels of the *Custom* downsampling.` | `Storleken i pixlar för den *anpassade* nedsamplingen.` | Tar bort engelska restord och ger naturlig nominalfras. Kontrollera att *Custom* inte är en synlig, oöversatt UI-etikett vid byggning. |
| `Exporter Limitations` | `Exportörens begränsningar` | Källan beskriver USD-exportören, inte flera exportörer. |
| `Single-sided and Double-sided Meshes` | `Enkelsidiga och dubbelsidiga mesh` | Följer Blenders etablerade datatyp *mesh*. |
| `USD seems to support neither ...` | `USD verkar varken stödja dubbelsidighet per material eller per ytgrupp, så Blender använder flaggan från det första materialet för att markera hela meshen som enkel- eller dubbelsidig. Om det inte finns något material är den dubbelsidig som standard.` | Rättar den otydliga formen `enkel- / dubbelsidigt`; *face group* återges som ytgrupp. |
| `Only the parent strands are exported ...` | `Endast föräldrastråna exporteras, och då bara med en konstant färg. UV-koordinater och normalinformation exporteras inte.` | Återger hårsystemets parent strands utan den allmänna betydelsen *överordnade trådar*. |
| `Geometry Node Modifiers` | `Geometrinodmodifierare` | Följer terminologins *geometrinod*. |
| `Instancing/Referencing` | `Instansiering/referenser` | `Referentiering` är inte en etablerad svensk form. |
| `Exporting instanced objects and collections ...` | `Export av instansierade objekt och samlingar stöds genom ett experimentellt alternativ vid USD-export.` | Rättar det felaktiga *instansiella*. |
| `Scene instances, created by directly instancing collections or objects ...` | `Sceninstanser som skapas genom att samlingar eller objekt instansieras direkt skrivs till USD som referenser till originalet. Objekttyper som stöds är mesh, kurvor och punktmoln.` | Den befintliga måltexten tillför felaktigt att det är en experimentell funktion och upprepar källans engelska datatyper. |
| `Due to a current limitation in the USD library ...` | `På grund av en aktuell begränsning i USD-biblioteket kan UDIM-texturer inte ingå i USDZ-arkivet. Begränsningen kommer troligen att åtgärdas i en framtida USD-version. (Se `USD-pullförfrågan #2133 <https://github.com/PixarAnimationStudios/OpenUSD/pull/2133>`__.)` | Uppdaterar URL till OpenUSD enligt källan och tar bort fuzzy-status. |
| `USD Primvar data types` | `USD Primvar-datatyper` | Svensk sammansättning med bevarat API-begrepp. |
| `Blender type` | `Blender-typ` | Rättar sakfelet `Typ av mixer`. |
| `RGBA color with 32-bit floating-point values ...` | `RGBA-färg med 32-bitars flyttalsvärden. Som specialfall läses eller skrivs en Primvar eller ett attribut för USD:s ``displayColor`` som ``color3f``-data med en alfakomponent på 1,0.` | Bevarar kodtyper exakt och rättar enkel backtick-formatering samt ordföljd. |
| `USD does not provide a byte color equivalent ...` | `USD tillhandahåller ingen motsvarighet till bytefärg. Bytevärdena konverteras till ``float`` och exporteras som ``color4f``.` | Bevarar datatyper som kodidentifierare. |

## Avsiktligt utelämnat

- De sju USD-tillgänglighetsposterna är redan täckta av batch 12–13.
- `float`, `color4f`, `Byte Color` och `Quaternion` är delade strängar i
  flera manualavsnitt. Ändra dem först efter en projektomfattande
  kontextgranskning, inte enbart i USD-avsnittet.
- Den långa Geometry Nodes-beskrivningen vid rad 635 innehåller synliga
  Blender-datatypnamn och flera RST-roller. Den bör brytas ut för separat
  radgranskning snarare än att normaliseras mekaniskt.
