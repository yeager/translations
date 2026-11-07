# Blender: projektstatus 5 november 2026

Senaste lokala arbete: 7 november 2026.

Batch 626 granskar fyra `Library Override`-poster i Blender UI:s RNA- och
menykontext. Den normaliserar den synliga huvudformen och de tre beskrivande
strängarna till *biblioteksåsidosättning*, medan närliggande
operatörsspecifika former lämnas orörda. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-626-library-override-rna.po` har
kontrollerats med `msgfmt`, l10n-lint, diffkontroll och Gitleaks. Den väntar
på import i Blender Translate; aktuell API-nyckel var inte tillgänglig i
nyckelringen vid kontrollen.

Batch 627 granskar sex strängar för punktgeometri, shadergrupper,
renderingsfärghantering och meshverktyg. Den rättar teckensättning som måste
följa källans kompletta eller avsiktligt öppna mening, samt normaliserar
*shadergrupp* och *shadergruppnod* enligt UI-terminologin. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-627-punctuation-and-shader-groups.po`
har passerat `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
diffkontroll. Den är lokalt klar men ännu inte importerad i Blender Translate.

Batch 628 granskar sex strängar för mesh- och nodåtgärder, tilläggskataloger,
USD-import och den utfällbara panelen för verktygsinställningar. Den bevarar
namn som BVH, USD, Xform och UsdGeomGprims, men rättar avslutande
interpunktion och ersätter det felaktiga *poppupppanel* med *utfällbar panel*.
`l10n-lint` gav inga fel; dess enda informationspost är en falsk
valutaträff på förkortningen USD. `svlang` tolkar imperativ och tekniska namn
som möjliga avvikelser, men ingen faktisk svensk skrivavvikelse hittades.
Deltafilen är lokalt klar och ännu inte importerad i Blender Translate.

Batch 629 rättar XR-teleporteringens *Hit Color* till *Färg vid träff*.
Ändringen undviker den tidigare tredubbla `f`-följden i *Träfffärg* och följer
den redan använda parallellformen *Färg vid miss*. Deltafilen är lokalt klar
och ännu inte importerad i Blender Translate.

De 17 granskade posterna i batch 626–629 finns även i den samlade,
importklara filen
`blender-ui-sv-reviewed-20261107-batches-626-629-combined.po`. Den ersätter
inte de spårbara delbatcherna i arkivet, men är den fil som ska användas vid
en enda manuell import.

Batch 630 granskar tilläggens fjärranslutna resursbibliotek och hjälpraden
för *Save Copy*. Den ersätter den svårlästa formen *fjärrresursbibliotek*,
som innehåller tre `r` i följd, med *fjärranslutet resursbibliotek* samt
rättar den falska vännen *aktuella* i betydelsen *actual* till *faktiska*.
Deltafilen är lokalt klar och ännu inte importerad i Blender Translate.

De 20 posterna i batch 626–630 finns samlade i
`blender-ui-sv-reviewed-20261107-batches-626-630-combined.po`. Den ersätter
den tidigare samlingsfilen för batch 626–629 som rekommenderad fil för en
enda manuell import, men delbatcherna och den äldre samlingsfilen bevaras som
spårbart arbetsunderlag.

Batch 631 granskar felmeddelandet för Asset Browsers cachekatalog för
nedladdningar. Den ersätter den krystade sammansättningen
*nedladdningscachekatalogen* med *cachekatalogen för nedladdningar* och följer
den etablerade termen *fjärranslutna resursbibliotek*. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 632 granskar *Clip Planes* i 3D-vyn och Grease Pencil Line Art. Den
använder den etablerade grafiktermen *klippningsplan* i stället för
*klippplan*, som får tre `p` i följd, och skriver ut relationen mellan det
nära och det fjärran klippningsplanet i hjälptexten. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 633 granskar Asset Browsers meddelande om nätåtkomst. Den ersätter
*resurser online* med den idiomatiska formen *resurser på nätet* och
*Fjärrresurser* med den projektspecifika termen *Fjärranslutna resurser*.
Deltafilen är lokalt kontrollerad men ännu inte importerad i Blender
Translate.

Batch 634 gör den synliga etiketten och omladdningsåtgärden för *Remote Asset
Library* konsekventa med termposten *fjärranslutet resursbibliotek*. Den
förkortade formen *fjärrbibliotek* används inte, eftersom den tappar den
betydelsebärande kopplingen till Asset Browser-resurser. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 635 granskar den svaga biblioteksreferensen för datablock. Den ersätter
den onaturliga formen *biblioteks-.blend-fil* med *biblioteksfil (.blend)*
och normaliserar *tillgångar* till den etablerade termen *resurser*. Deltafilen
är lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 636 granskar API-egenskapen `ID.is_evaluated` mot Blenders aktuella
Python-API. Den skiljer uttryckligen körningsdata, utvärderat datablock och
ursprungliga data från en `.blend`-fil, där den tidigare formuleringen felaktigt
slog ihop de två första fallen. Deltafilen är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 637 granskar `NOOP`-åtgärden i biblioteksåsidosättningar. Den ersätter
den kontextmässigt felaktiga termen *överskrivningar* med
*biblioteksåsidosättningar* och gör uppmaningen idiomatisk. Deltafilen är
lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 638 normaliserar sex närliggande API- och Outliner-poster för *Library
Override*. Den använder konsekvent *biblioteksåsidosättning*, rättar den
felaktiga formen *biblioteksåsidosättanden* och skriver `.blend-fil` på ett
naturligt sätt. Deltafilen är lokalt kontrollerad men ännu inte importerad i
Blender Translate.

Batch 639 granskar Asset Browser-inställningarnas bibliotekskategorier. Den
skiljer *tilläggsresursbibliotek* från lokala och fjärranslutna
resursbibliotek, och förtydligar felmeddelandet för ett fjärranslutet
resursbibliotek. Deltafilen är lokalt kontrollerad men ännu inte importerad i
Blender Translate.

Batch 640 normaliserar nio synliga *Library Override*-operatorer och
API-etiketter till *biblioteksåsidosättning*. Projektets terminologilista
uppdateras samtidigt för att markera *biblioteksöverskrivning* som en äldre,
icke önskad variant för just denna Blender-funktion. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 641 granskar bibliotekets omsynkroniseringsmeddelanden för
biblioteksåsidosättningar. Den normaliserar den sista äldre formen
*biblioteksöverskrivningar*, använder *omsynkroniseras* och skriver `.blend`
som filformat i löpande text. Deltafilen är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 642 granskar sex lokala Library Override-åtgärder och deras
egenskapssamling. Den ersätter generisk *överskrivning* med den specifika
termen *biblioteksåsidosättning* och använder *beroendehierarki* för den
valda funktionens beroenderelationer. Deltafilen är lokalt kontrollerad men
ännu inte importerad i Blender Translate.

Den aktuella samlingsfilen för batch 626–642 är
`blender-ui-sv-reviewed-20261107-batches-626-642-combined.po` med 55
granskade poster. Den är den rekommenderade filen för nästa enda manuella
import och ersätter den tidigare samlingsfilen 626–641 för det ändamålet.

Den 6 november skapades en samlad Blender UI-delta med 5 681 unika, lokalt
granskade poster och sex importdelar om högst 1 000 poster. Användaren har
skickat in samtliga sex delar manuellt till Blender Translate. Importresultat
från Weblate har ännu inte verifierats i detta arkiv. De efterföljande lokala
batcherna 287 för Grease Pencil-lökskalning, 288 för bilders alfahantering,
289 för genererade bilder och UDIM samt 290 för ljustyper och penselresurser
och 291 för ljusinställningar och skuggor samt 292 för Light Probes är
arkiverade separat, liksom batch 293 för materialinställningar och 294 för
meshtopologi och UV-lager samt 295 för Movie Clip och kompositörvisning samt
296 för hårnodernas deformation och 297 för hårnodernas data och generering
samt 298 för hårinfästning och guidekurvor, 299 för tilläggsmetadata och
hårnoder samt 300 för tilläggskategorier och 301 för språk- och
resurskataloger samt 302 för filsparande och tilläggsarkiv, och ingår därför
inte i de redan inskickade sex delarna. Batch 303 för Principled BSDF:s
materialetiketter, batch 304 för grundläggande begränsningar, batch 305 för
Action-begränningen, batch 306 för dess blandningslägen, batch 307 för
armaturbegränsningen, batch 308 för Child Of-begränsningen, batch 309 för
kameralösarbegränsningen, batch 310 för Begränsa till-begränsningen, batch
311 för golvbegränsningen och batch 312 för Följ bana-begränsningen ingår
också endast lokalt. Batch 313 för Movie Clip hade en alltför bred deltafil och
är uttryckligen ersatt av batch 314, som endast innehåller den kontrollerade
ändringen `Track` → `Spår` i Movie Clip-kontext. Batch 313 får inte importeras.
De finns också samlade i den fristående, lokalt kontrollerade
uppföljningsfilen `blender-ui-sv-reviewed-20261107-post-upload-batches-287-500.po`
med 3 562 poster, som omfattar alla färdiga batcher efter sexdelsimporten,
Movie Clip-korrigeringen samt Follow Track-, Object Solver-, Pivot- och
Shrinkwrap-granskningarna. Den ersätter tidigare samlingsfiler för detta
intervall, är redo för manuell import och har inte skickats in eller
verifierats i Weblate.

Batch 315 granskar tio poster för Follow Track-begränsningen och dess
filmspårningskontext. Den normaliserar det formella namnet till
*Följ spår-begränsning*, använder *bildmaterial* för *footage* och förtydligar
föräldrarelationens distorsionskorrigerade position. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-315-follow-track-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 316 granskar fyra poster för Object Solver-begränsningen. Den bekräftar
*objektlösare* och *objektlösarbegränsning* utifrån Blenders API-dokumentation
och gör uttrycket för filmspårningsobjekt konsekvent med batch 315. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-316-object-solver-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 317 granskar 17 poster för Pivot-begränsningen mot Blenders API. Den
normaliserar rotationsetiketterna till exempelvis *-X-rotation*, tydliggör
skillnaden mellan mål och ägare och använder konsekvent *vridpunkt*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-317-pivot-constraint.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 318 granskar åtta grundposter för Shrinkwrap-begränsningens relation och
ytgallring. Den ersätter missvisande *borttagning* med *gallring*, eftersom
inställningen styr projektionen och inte raderar geometri. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-318-shrinkwrap-cull.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 319 granskar 22 poster för Shrinkwrap-projektion och algoritmval:
projektionsaxel, koordinatrymd, närmaste yt- eller hörnpunkt, målnormal och
alternativ projektion. Den gör också ytgallring konsekvent i den inverterade
projektionen. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-319-shrinkwrap-projection.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 320 granskar åtta Shrinkwrap-fästlägen. Den skiljer tydligt läget
*Utanför ytan* från en fysisk yta och använder konsekvent *position* i
avståndsförskjutningarnas förklaringar. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-320-shrinkwrap-snap-modes.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 321 granskar 20 poster för Spline IK:s kurvstyrda benkedjor och
volymvariation. Den bevarar parameterbeteckningen *n* och normaliserar
volymsträckningens minimi-, maximi- och utjämningstermer. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-321-spline-ik-volume.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 322 granskar åtta poster för Spline IK:s kurvradie, jämna fördelning och
ursprungliga skala. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-322-spline-ik-curve-scale.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 323 granskar fyra grundposter för Stretch To-begränsningen och
normaliserar typetiketten till *Sträck mot-begränsning*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-323-stretch-to-basics.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 324 granskar nio poster för Stretch To-begränsningens axelordning,
svängning, vilolängd och volymbevarande. Den använder *dämpad spårning* i
stället för det engelska UI-namnet där texten beskriver funktionen. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-324-stretch-to-axis-and-rest-length.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender
Translate.

Batch 489 granskar 15 poster för Lattice-objektets gitterpunkter och
interpolering. Den behåller Blenders synliga typnamn *Lattice*, använder
*gitter* i beskrivande text och lämnar algoritmnamnen *Catmull-Rom* och
*BSpline* oförändrade. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-489-lattice-grid-and-interpolation.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 500 granskar 16 poster för materialens metallic-egenskap, nodträd,
texturmålningsplatser och förhandsgranskningsobjekt. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-500-material-reflection-and-preview.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 501 granskar 23 poster för materialens dithrade och blandade
ytåtergivning, texturplatser, tjockleksmodell, baksidesgallring och
världsförhandsgranskning. Den behåller de vedertagna rendertermerna
*dithrad*, *baksidesgallring* och *ljussond*, använder *nodträd* i
materialkontexten och rättar den felaktiga konstruktionen *materialnodens
träd* till *materialets nodträd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-501-material-rendering.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-501.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 502 granskar 12 poster för materialens transparens, underytseffekt,
transparenta skuggor och volymskärning. Den förtydligar avaktiveringens
konsekvens för skuggor, rättar den felaktiga översättningen *grenrörsgeometri*
till projektets etablerade term *manifold geometri* och använder *gränsyta
för ett medium* för renderingsmetodens gränssnitt. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-502-material-transparency-and-volume.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-502.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 503 granskar 20 poster för mesh-datablockets grundläggande topologi:
kanter, ytor, ythörn, looptrianglar, polygoner och normaler. Den rättar
*Hörnnormal* till pluralformen *hörnnormaler*, ersätter den felaktiga
översättningen *ansiktshörn* med *ythörn* och använder projektets etablerade
termer *meshloop*, *ytindex* och *hörnpunktsnormal*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-503-mesh-normals-and-topology.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-503.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 504 granskar 25 poster för ommeshning, voxel- och
fyrhörningsommeshare, texturutrymme, markeringsräkning och topologispegling.
Den använder etablerade termer som *voxelommeshare*, *fyrhörningsommeshare*,
*adaptivitet*, *texturmesh* och *ytor*, samt gör hjälptesten konsekventa med
den översatta åtgärden *Korrigera poler*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-504-mesh-remesh-and-selection.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-504.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 505 granskar 28 poster för Mesh målning, symmetri, UV-looplager,
hörnpunktsfärger och hörnpunktsnormaler. Den håller isär markeringsmasker för
ytor och hörnpunkter, använder *UV-looplager* och *mesh* enligt projektets
terminologi och rättar den språkligt felaktiga formen *det nya meshet* till
*den nya meshen*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-505-mesh-painting-and-uv-data.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-505.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 506 granskar 13 grundposter för Metaball-datatypen: element,
polygoniseringsupplösning, påverkan och uppdateringslägen under redigering.
Den använder *metaboll* i löpande svensk text och behåller den tekniska
processen *polygonisering*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-506-metaball-basics.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-506.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 507 granskar 16 grundposter för Movie Clip: externa filmfiler,
bildfrekvens, bildrutor, källdata, proxyer och tidskod. Den behåller
Blenders API-namn *MovieClip* och produktnamnet *Grease Pencil*, men använder
svenska termer som *filmklipp*, *förhandsgranskningsproxy* och
*tidskodsindex*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-507-movie-clip-basics.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-507.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 508 granskar 23 poster för nodträdets grunddata, gruppgränssnitt,
färgmärkning och nodtyper. Den rättar kompositörtermen *Matte* från
adjektivet *matt* till substantivet *matta*, normaliserar *färgmärkning* och
bevarar etablerade tekniska namn som *shader* och *Grease Pencil*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-508-node-tree-basics.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-508.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 509 granskar 23 poster för kompositions-, geometri-, shader- och
texturnodträdens användning och lägen. Den normaliserar det felstavade
*Nodegruppen* till *Nodgruppen*, behåller typnamn som *Grease Pencil* och
*shader* och använder *geometrimodifierare* i rätt kontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-509-specialized-node-trees.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-509.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 510 granskar 22 grundposter för objekt: material-, urvals- och
formnyckeldata, viloposition, begränsningsbox, kollisionsobjekt och
begränsningar. Den rättar den felaktiga etiketten *Emulering av Bounding Box*
till *begränsningsbox* och kompletterar den projektspecifika terminologin för
att skilja den tredimensionella objektgränsen från filmspårningens
*begränsningsruta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-510-object-basics.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-510.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 511 granskar 17 poster för objektens visningsgränser och tomobjektens
visningsformer. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-511-object-display-basics.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-511.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 512 granskar 13 poster för bildtomobjekt, fysikfält och planar-,
sfäriska- och volymljussonder. Den rättar uttrycket
*Ursprung offset avstånd* till *avstånd för ursprungsförskjutning* och gör
volymljussondtermen konsekvent. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-512-object-images-and-light-probes.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-512.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 513 granskar 14 poster för objektinstanser och kompositörmattor. Den
rättar *Ansikten* till *ytor* i meshkontext och ersätter den felaktiga
översättningen *Avvaktande* av *Holdout* med *matta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-513-object-instancing-and-mattes.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-513.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 514 granskar 22 Cache File-poster för Alembic-filer, förhämtning,
bildrutetid, renderingsprocedurer och rörelseoskärpa. Den bekräftar de
etablerade termerna *cachefil*, *förhandsladdning*, *bildruteförskjutning*,
*hastighetsattribut* och *rörelseoskärpa* samt bevarar produktnamnen Alembic
och Cycles. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-514-cache-file-and-procedural.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-514.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 515 granskar 15 poster för kamerans datablock, synfält och centralt
cylindriska projektion. Den följer ordlistans *synfält*, *längdgrad* och
*breddgrad* samt rättar det oidiomatiska *Maximalt höjdvärde* till *Största
höjdvärde*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-515-camera-projection-basics.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-515.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 516 granskar sju Curve-poster för Cycles-mesh, 2D-/3D-kurvor och
parametrisk kurvposition. Den bekräftar *dimensioner*, *Z-axel* och
*Cycles-mesh* samt förtydligar hur positionen beräknas från
*Sökvägslängd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-516-curve-dimensions-and-path.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-516.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 517 granskar tolv Text Curve-poster för objektets X-/Y-förskjutning och
text som inte ryms i en textruta. Den ersätter den stela formen
*Textruteöverflöde* med *Överflöde i textruta*, använder idiomatiskt
*flöda över* och gör hjälptexten om textens beteende tydligare. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-517-text-curve-overflow.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-517.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 518 granskar fyra poster för bildtyper och ljusdatablock. Den bekräftar
de korta UI-termerna *flerlager*, *UV-test*, *renderingsresultat* och *ljus*
i respektive Image- och Light-kontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-518-image-types-and-light.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-518.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 519 granskar tio materialposter för diffus och spekulär färg, råhet,
transparenta baksidor, ytåtergivning och strålspårad transmission. Den
följer ordlistans *baksidesgallring*, *ljussond* och *strålspårning* samt
tydliggör att spegelreflektionen kan vara ljusstark. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-519-material-colors-and-raytracing.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-519.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 520 granskar den entydiga Mesh-inställningen *Remesh Mode* och
bekräftar den etablerade UI-termen *ommeshningsläge*. Den närliggande
strängen *Loops* lämnas medvetet för senare källverifiering, eftersom samma
okontekstualiserade sträng också används i partikelpanelen. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-520-mesh-remesh-mode.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-520.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 521 granskar 16 Object-poster för objektfärg, deltatransformationer,
dimensioner och visningsgränser. Den lokaliserar läget *Object Color* som
*Objektfärg*, gör Euler- och kvaternionrotationerna konsekventa och skriver
om varningen för upprepade dimensionsvärden till idiomatisk svenska. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-521-object-delta-and-display.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-521.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 522 granskar elva Object-poster för ytinstanser, skuggfångare,
ljuslänkning, linjeteckning, rotationslås och materialplatser. Den rättar
*ansiktsinstans* till *ytinstans*, ersätter *Linjekonst* med den etablerade
termen *Linjeteckning* och använder *Eulerrotationer* i stället för den
felaktiga pluralformen *Eulers*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-522-object-instancing-and-line-art.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-522.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 523 granskar nio Object-poster för transformationsmatriser och lägen.
Den normaliserar *föräldrarelativ transformationsmatris*, *deltavärden*,
*världsmatris* och beskrivningen av benföräldrarelationer. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-523-object-matrices-and-modes.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-523.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 524 granskar nio Object-poster för Grease Pencil-lägen, modifierare och
rörelsebanor. Den använder *viktmålning av Grease Pencil-streck* och
*hörnpunktsmålning av Grease Pencil-streck* för de särskilda målningslägena
och bekräftar *rörelsebana* och *modifierare*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-524-object-grease-pencil-and-motion.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-524.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 525 granskar 24 Object-poster för styva kroppar, Rigify och
rotationsrepresentationer. Den normaliserar *stelkroppsbegränsning*,
*Eulerrotation*, *Euler-vinklar*, *gimbal-låsning*, *axelvinkel* och
*kvaternionrotation*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-525-object-rigid-body-and-rotation.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-525.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 526 granskar sju Object-poster för Cycles skuggterminator. Den inför
den kontextbundna termen *skuggterminator* och skiljer mellan geometri-,
normal- och skuggningsförskjutning för korrigering av artefakter på
lågpolygeometri. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-526-object-shadow-terminator.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-526.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 527 granskar 48 Object-poster för visning, instansiering, formnycklar,
simuleringscache och objekttyper. Den normaliserar bland annat
*begränsningsbox*, *instansierare*, *tomobjekt*, *trådram*, *formnyckel* och
*alfablandning*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-527-object-display-and-instancing.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-527.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 528 granskar elva Object-poster för Cycles synlighet för kamera,
diffust ljus, blanka reflektioner, skuggor, transmission och volymspridning.
Den håller UI-etiketterna korta och använder uttryckligen *strålar* i
hjälptexterna. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-528-object-ray-visibility.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-528.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 529 granskar 35 poster för partiklars vinkelhastighet, effektorer,
barnpartiklar, Brownska rörelser och hårbenor. Den ersätter felöversättningen
*avsked* med den kontextkorrekta termen *bena* och normaliserar
*barnpartikel*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-529-particles-children-and-parting.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-529.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 530 granskar 29 poster för partiklars klumpning, kollisionsobjekt,
Couranttal, visningsläge och fördelning. Den rättar bland annat *ljud* till
*brus* i partiklarnas klumpningsinställning och återställer den trasiga
översättningen av partikelvisningens *Kors*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-530-particles-clumping-and-display.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-530.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 531 granskar 36 poster för partiklers emission, kraftfält, hår,
instanssamlingar, integrationsmetoder, vätskesimulering och nycklade banor.
Den ersätter bland annat *ramnummer* med *bildrutenummer* samt den otydliga
översättningen *tangenterna loopas* med *nycklarna upprepas*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-531-particles-emission-and-integration.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-531.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 532 granskar 65 poster för hårpartiklars nyckfunktioner, livslängd,
boider, materialplatser, partikelbanor, reaktioner och renderingsorientering.
Den följer ordlistans term *nyck* och rättar bland annat *materialspår* till
*materialplats* samt *Döds* till *Död*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-532-particles-kink-and-rendering.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-532.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 533 granskar 21 poster för hårpartiklars grovhet, stråform,
guidehår och partikelvisning. Den normaliserar *grovhet* och rättar bland
annat den felaktiga strängformen till *stråform*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-533-particles-roughness-and-guides.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-533.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 534 granskar 25 poster för delbildrutor, tidssteg, hårstrån och
spetsdiameter. Den ersätter oöversatta *subframes* och den felaktiga formen
*Stranddiameter bredd* med konsekventa svenska termer. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-534-particles-timing-and-strands.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-534.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 535 granskar 18 poster för partiklars klumpningskurvor, slumpvis
urval, livscykel, emission och jämn fördelning. Den normaliserar
*klumpningskurva* och *klumpbrus*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-535-particles-clumping-and-emission.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-535.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 536 granskar tolv poster för föräldrapartiklar, reaktioner, återväxt,
adaptiv rendering och rotation. Den ersätter bland annat oöversatta
*Multi React* med *Flera reaktioner*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-536-particles-reactions-and-rotation.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-536.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 499 granskar 20 poster för materialens verkliga och skenbara
förskjutning, Grease Pencil-material samt Freestyle-linjer. Den håller isär
*bumpmappning* och verklig *förskjutning*, och använder den etablerade
termen *linjeteckning* för Blenders Line Art. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-499-material-displacement-and-lines.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 498 granskar 15 poster för material, alfatröskel och
genomskinlighetslägen. Den normaliserar bland annat *klipptröskel*,
*alfaklippning* och *alfablandning*, använder *multisampling* för renderings-
sammanhanget och skiljer genomskinliga ytor från meshens interna termen
*ansikten*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-498-material-alpha-and-blending.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 497 granskar sex grundposter för Blender-masker, deras lager och deras
bildrutor. Den preciserar att maskdatablocket används för *bildkomposition*,
utan att blanda ihop kontexten med masktexturer eller maskgeometri. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-497-mask-data-basics.po` är lokalt
kontrollerad och arkiverad, men dess import till Blender Translate är inte
verifierad i detta arkiv.

Batch 496 granskar fyra återstående volymljussondposter: giltighetströskeln
och visningsförskjutningen. Den gör förklaringen konsekvent med
normalförskjutningen i batch 495 och använder *ljusläckage* i stället för den
mindre precisa formen *ljusblödning*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-496-volume-light-probe-validity.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 495 granskar 34 poster för en volymljussonds bakning, ljusinsamling och
rutnätsupplösning. Den förtydligar bland annat konsekvensen av att fånga
omvärldsljus och använder *normalförskjutning*, *riktningsförskjutning*,
*ytförskjutning* och *surfel* i den avsedda renderingskontexten. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-495-volume-light-probe-baking.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 494 granskar 38 poster för ljussonder och parallaxkorrigering. Den
rättar bland annat *Ljusprob* till *ljussond* och de felaktiga översättningarna
av rendertermen *bias* till kontextuella förskjutningar. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-494-light-probes-and-parallax.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 493 granskar 38 poster för områdes-, punkt-, strålkastar- och solljus.
Den rättar bland annat *Disk* från den felaktiga formen *Hårddisk*, använder
*ljuskägla* i strålkastarkontext och normaliserar avtoning, ljusvinkel,
skuggkaskader och formbeskrivningar. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-493-light-shapes-and-falloff.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 492 granskar tio poster för ljusens skuggfiltrering. Den rättar den
trasiga etiketten för *Shadow Jitter Overblur* till *Extra oskärpa vid
skuggslumpning*, förklarar att Percentage Closer Filtering minskar
kantartefakter och skiljer mjuk skuggstorlek från skuggkartans upplösning.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-492-light-shadow-filtering.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 491 granskar 31 poster för Blenders ljustyper och grundinställningar.
Den använder de etablerade typerna *punktljus*, *solljus*, *strålkastare* och
*områdesljus*, och håller isär ljusets effekt, färg, diffus och spekulär
reflektion samt transmissions- och volymfaktorer. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-491-light-types-and-basic-settings.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 490 granskar sex poster för externa `.blend`-bibliotek, länkade
datablock och biblioteksåsidosättningar. Den följer den projektspecifika
skillnaden mellan *biblioteksåsidosättning* och ett vanligt programbibliotek,
och använder *omsynkroniseras* för den tekniska åtgärden resync. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-490-linked-libraries-and-overrides.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 441 granskar 35 poster för gizmogruppers verktygsalternativ, regioner
och VR-indikatorer. Den rättar bland annat den tidigare trasiga
VR-styrenhetsetiketten, normaliserar *gizmokarta* och använder sammanfogade
Blender-termer som *gizmogrupp* och *gizmoegenskaper*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-441-gizmo-groups-and-regions.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 443 granskar 23 poster för Grease Pencil-ritningar och deras
animeringsbildrutor. Den bekräftar *nyckelbildruta*, *mellanpose*, *ytterläge*
och *rörlig hållning* som skilda animeringstyper samt gör skrivningen av
*Grease Pencil-ritning* konsekvent. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-443-grease-pencil-frames-and-keyframes.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 451 granskar åtta Action-poster för lager, poseringsmarkörer och
cyklisk uppspelning. Deltafilen är lokalt kontrollerad och arkiverad, men
dess import till Blender Translate är inte verifierad i detta arkiv.

Batch 465 granskar 81 poster för penslars rit-, skulpterings- och målningslägen,
marköröverlägg, automaskering, penselavstånd, tryckkänslighet och våtmålning.
Den normaliserar bland annat *viktmålning*, *hörnpunktsmålning*,
*tryckslumpning*, *3D-vyport*, *områdesplansmappning* och *våtmålningsradie*.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-465-brush-modes-wet-paint.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 466 granskar 79 kameraposter för beskärningsavstånd, anpassade
OSL-kameror, fiskögeobjektiv, ekvirektangulär och centralcylindrisk
projektion, panoramatyper samt sensoranpassning. Den använder konsekvent
*3D-vyport*, *fiskögeobjektiv*, *sensoranpassning*, *passepartout* och
*beskärningsavstånd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-466-camera-optics-and-projections.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 467 granskar 30 kameraposter för kompositionsguider, beskärnings- och
dimvisning, passepartout, säkra områden och filmruta. Den skiljer de generella
*säkra områdena* från *säkra marginaler för text* och *säkra marginaler för
bildinnehåll* i kameravyn. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-467-camera-composition-guides.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 468 granskar 43 poster för Blender-samlingar, färgmärken,
samlingsexportörer, instansförskjutning och linjekonstens
korsningsinställningar. Den använder de etablerade termerna *samling*,
*instansförskjutning*, *korsningsprioritet*, *korsningsmask* och *linjekonst*.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-468-collections-and-line-art.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 469 granskar 27 poster för kurvdatablockens avfasningsgeometri,
avfasningsfaktorer, tvärsnitt, profil, kurvobjekt och upplösning. Den följer
Blender-terminologin för *avfasning*, *kurvspline* och *tvärsnitt för kurvans
avfasningsgeometri*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-469-curve-bevel-geometry.po` är lokalt
kontrollerad och arkiverad, men dess import till Blender Translate är inte
verifierad i detta arkiv.

Batch 470 granskar 25 poster för kurvans extrudering, fyllningsläge,
förskjutning, sökvägsvaraktighet, U/V-upplösning och avsmalning. Den använder
de etablerade termerna *kurvans fyllningsläge*, *sökvägsvaraktighet*,
*kurvspline*, *avsmalningsobjekt* och *avsmalningsradie*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-470-curve-dimensions-and-taper.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 471 granskar 25 poster för texturutrymme, vridningsberäkning,
meshgränser, ändlock, kurvbanor och kurvdeformering. Den behåller den formella
axelbeteckningen *Z-Up* men använder *texturutrymme*, *vridningsmetod*,
*förflyttningsbana* och *kurvdeformering* i svensk UI-text. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-471-curve-texture-space-and-paths.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 472 granskar 21 poster för ytkurvor, textkurvor och textjustering.
Den bekräftar de typografiska lägena *Justera*, *Jämna marginaler*,
*övre baslinje*, *nedre baslinje* och *teckenavstånd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-472-text-curves-and-alignment.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 473 granskar 23 poster för textobjektens innehåll, teckenformat,
objektteckensnitt, kurvdeformerad text och markerad fetstil, kursiv,
kapitäler och understrykning. Den rättar den grammatiskt felaktiga
inställningsbeskrivningen till *Inställningar för redigering av
teckenformatering* och behåller de synliga Blender-namnen *Vertex Instancing*
och exempelidentifierarna `family-a` och `family-b`. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-473-text-curve-fonts-and-styles.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 474 granskar tio poster för textobjektens kursiveringsvinkel,
kapitäler, tecken-, rad- och ordavstånd, textrutor och understrykning samt
snabbredigering. Den bekräftar projektets etablerade termer *skjuvning*,
*teckenavstånd*, *textruteöverflöde* och *kapitäler*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-474-text-curve-spacing-and-overflow.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 475 granskar 15 poster för hårkurvors datablock, kontrollpunkter,
urvalsdomän, ytfäste, ytnormal, UV-karta, spegelsymmetri och
skulpteringskollision. Den normaliserar den återkommande terminologin till
*ytmesh*, *ytans UV-karta* och *hårinfästning*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-475-hair-curves-and-surface-attachment.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 476 granskar 29 poster för Freestyles linjestilar, aktiva texturplatser,
alfagenomskinlighet, 2D-vinkelstyrd kedjedelning, ändlock och kedjning. Den
använder projektets befintliga Freestyle-termer *linjeuppsättning*,
*funktionskant*, *kedjedelning*, *stumt ändlock* och *streck*, samt
normaliserar *alfagenomskinlighet*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-476-freestyle-line-styles-and-chains.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 477 granskar 27 poster för Freestyles linjefärg, färgmodifierare,
streck- och mellanrumsmönster, streckgeometri samt integrationsmetoder för
kedjehörnpunkter. Den ersätter den tvetydiga *baslinjefärg* med *grundfärg
för linjen*, och använder *medelvärde* som matematiskt korrekt etikett.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-477-freestyle-colors-dashes-and-integration.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 478 granskar 15 poster för Freestyles längdgränser, materialgränser,
inställningspaneler och rundor i skissartad kedjning. Den återställer den
utelämnade kedjekontexten i materialgränsbeskrivningen och gör
*alfagenomskinlighet* konsekvent även i panelbeskrivningen. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-478-freestyle-lengths-and-panels.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 479 granskar 28 poster för Freestyles sorteringsnycklar och
sorteringsordning samt delningsstreck, delningsmellanrum och delningslängd.
Den bekräftar de tidigare normaliserade Freestyle-termerna *kedjedelning*,
*delningsstreck*, *delningsmellanrum* och *delningslängd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-479-freestyle-sorting-and-split-patterns.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 480 granskar 30 poster för Freestyles texturplatser, texturavstånd,
grundtjocklek, tjockleksplacering, kedjning och längd- samt vinkelstyrd
kedjedelning. Den ersätter tvetydiga *baslinje*-sammansättningar med
*texturavstånd* och *linjens grundtjocklek* samt enhetliggör *kedjning*.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-480-freestyle-textures-and-thickness.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 481 granskar tio poster för Freestyles gemensamma objekt,
sorteringsfunktion, längd- och mönsterstyrd kedjedelning samt texturerade
streck. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-481-freestyle-activation-options.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 482 granskar 17 poster för Grease Pencil-datablock, lagergrupper och
lager samt lökskalningens opacitet, bildruteintervall och
nyckelbildrutefiltrering. Den bekräftar etablerade termer som *lökskal*,
*lökskalsbildruta*, *Grease Pencil-lager* och *nyckelbildruta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-482-grease-pencil-layers-and-onion-skinning.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 483 granskar 14 poster för Grease Pencil-streckens djupordning,
2D-lager och 3D-position, automatiskt lagerlås och lökskalningens färger,
uttoning och loopande animationer. Den följer den projektspecifika
terminologin för *streckens djupordning*, *lökskal* och
*lökskalsbildruta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-483-grease-pencil-depth-and-onion-display.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 484 granskar nio poster för externa och packade bilddatablock,
alfaomvandling, oassocierad och associerad alfa, förmultiplicering,
kanalpackning och helt ogenomskinliga bilder. Den förtydligar att
alfarepresentationen konverteras vid både lagring och inläsning. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-484-image-alpha-modes.po` är lokalt
kontrollerad och arkiverad, men dess import till Blender Translate är inte
verifierad i detta arkiv.

Batch 485 granskar 18 poster för bilders OpenGL-bindningskod, pixelbuffert,
färgrymd, bitdjup och visningsbildförhållande samt filformaten BMP, SGI IRIS,
JPEG, JPEG 2000, Targa, Cineon och DPX. Den ersätter bland annat den felaktiga
formen *Targa rå* med *Okomprimerad Targa*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-485-image-metadata-and-file-formats.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 486 granskar 22 poster för ytterligare bildformat, bild- och
filmfilnamn, bildvaraktighet och genererade bilders färg, storlek och typ
samt UV-rutnät. Den normaliserar *varaktighet*, *genereringstyp* och
*UV-mappningar*, men behåller filformatnamn som OpenEXR, WebP och FFmpeg.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-486-image-formats-and-generation.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 487 granskar 41 poster för bilddata i minne, packade filer,
bildpunkter, renderingsplatser, UV-sömmarginaler, bildkällor, UDIM-plattor
och stereo-/flervysformat. Den använder *visare för komponeringsnoder* och
förenklar bildsekvensbeskrivningen. Den enda l10n-lint-notisen gäller den avsiktligt
oförändrade formatetiketten *Stereo 3D*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-487-image-buffers-views-and-sources.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 488 granskar 23 poster för avflätning, flyttalsbuffertar, halva
flyttal, flervy, renderingsvisning, vyformat och formnycklar. Den förtydligar
stereoparets enskilda fil och gör den relativa formnyckelbeskrivningen
deklarativ i stället för användartilltal. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-488-image-views-and-shape-keys.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 450 granskar åtta Action-poster för F-kurvor och bildruteintervall.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-450-action-frame-ranges.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 449 granskar 14 poster för datablockens namn, ursprung, förhandsvisning,
sessionsidentifierare och användarstatus. Den bekräftar *biblioteksåsidosättning*,
*sessionsomfattande unik identifierare* och *falsk användare* i Blenders
datablockskontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-449-datablock-identity-and-users.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 448 granskar 16 poster för Blenders datablocksidentiteter,
länkbibliotek och körtidsdata. Den bekräftar projektets användning av
*datablock*, *körtidsdata*, *biblioteksreferens* och
*biblioteksåsidosättning*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-448-datablocks-and-library-links.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 447 granskar nio poster för histogrammets färgkanaler och lägen. Den
bekräftar att de standardiserade beteckningarna *RGB*, *R*, *G*, *B*, *A* och
*luma* behålls som tekniska UI-etiketter. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-447-histogram-color-channels.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 446 granskar 18 poster för Grease Pencil-lagergrupper, färgmärkningar
och aktiva lager. Den behåller produktnamnet *Grease Pencil*, normaliserar
*färgmärkning* och rättar den oidiomatiska statusen *utökad* till *utfälld* i
gränssnittskontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-446-grease-pencil-layer-groups.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 445 granskar 31 poster för Grease Pencil-lagrets materiallåsning,
transformeringar och renderingsval. Den bekräftar bland annat *maskeringslager*,
*passindex*, *radieförskjutning*, *visningslager* och den kontextbundna
transformeringstermer *förskjutning*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-445-grease-pencil-layer-properties.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 444 granskar 25 poster för Grease Pencils tidsmodifierare och lagerträd.
Den bekräftar *startbildruta*, *trädnod*, *kanalfärg* och *lökskal* och
normaliserar den tidigare inkonsekventa formen *dope-ark* till *dopeblad*.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-444-grease-pencil-time-and-layer-tree.po`
är lokalt kontrollerad och arkiverad, men dess import till Blender Translate
är inte verifierad i detta arkiv.

Batch 442 granskar 13 poster för Grease Pencils streckmodifierarsegment och
ritningar. Den bekräftar *streckmodifierarsegment*, *mellanrum* och
*materialindex* i den konkreta modifierarkontexten samt gör *Grease
Pencil-ritning* konsekvent med projektets tidigare terminologi. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-442-grease-pencil-dash-segments.po` är
lokalt kontrollerad och arkiverad, men dess import till Blender Translate är
inte verifierad i detta arkiv.

Batch 364 granskar tio Dopebladsfilter för Grease Pencil, hår, dolda
kanaler, gitter och ljus. Den fortsätter den konsekventa direktformen
*Visa även …* och ersätter den otydliga snedstrecksformen *objekt/ben* med
*objekt eller ben*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-364-dope-sheet-display-filters-a.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 325 granskar fyra poster för Track To-begränsningen mot Blenders
dokumentation. Den normaliserar komponentnamnet till *Rikta mot-begränsning*
och skiljer målets Z-axel från den globala Z-axeln i den beskrivande texten.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-325-track-to-constraint.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender
Translate.

Batch 326 granskar tre poster för Transform Cache-begränsningen och dess
Alembic-cache. Den använder *hämta* för uppslag av den externa
transformationsmatrisen och bevarar *cachefil* som teknisk UI-term.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-326-transform-cache-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 327 granskar 14 poster för Transform-begränningens källvärdesintervall.
Den gör att termerna *övre* och *undre gräns* tydligt avser källrörelse längs
respektive axel och ersätter lånordet *mappa* med *koppla* i komponentens
beskrivning. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-327-transform-source-ranges.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 328 granskar elva poster för Transform-begränningens rotationskanaler.
Den använder *källäge* för rotationsinmatning och konsekventa sammansättningar
som *X-vridning* för swing/twist-lägena. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-328-transform-rotation-modes.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 329 granskar tio poster för Transform-begränningens koppling mellan
käll- och målvärden. Den ersätter *mappa* med *koppla* och förtydligar vilken
källaxel som används för objektets X-, Y- och Z-axlar. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-329-transform-mapping.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 330 granskar elva poster för Transform-begränningens blandningslägen.
Den gör ersättning, addering och multiplikation konsekventa samt förklarar
rotationsordningen med *överordnat* och *underordnat objekt*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-330-transform-mix-modes.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 331 följer upp en underagents granskning av begränsningarnas
koordinatsystem mot den befintliga termlistan. Den rättar *Världs-rymd* till
*världsrymd*, normaliserar *målkoordinatsystem* och rättar sammansättningen
*armaturobjekt*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-331-constraint-coordinate-spaces.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender
Translate.

Batch 332 granskar 16 poster för Transform-begränningens utdataordning och
destinationsintervall. Den skiljer konsekvent käll- från destinationsrörelse
och normaliserar gränserna till *högsta* respektive *lägsta* värde längs varje
axel. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-332-transform-destination-ranges.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender
Translate.

Batch 333 granskar åtta poster för fler-målbegränsningar och målben. Den
förtydligar skillnaden mellan målobjekt, målben och målarmatur samt använder
den etablerade termen *blandningsvikt*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-333-constraint-targets.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 334 granskar tolv poster för kurvkartläggningens kontrollpunkter,
handtag och RGB-kurvor. Den normaliserar *kurvkartpunkt* enligt termlistan
och behåller de etablerade kurvtermerna *Bézier*, *vektorhandtag* och
*automatiskt handtag*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-334-curve-mapping-points.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 335 granskar 15 poster för kurvkartläggningens klippgränser,
extrapolering och tonlägen. Den ersätter ofullständiga engelska max-/min-
etiketter och gör den kombinerade RGB-kurvans färgtonseffekt tydligare.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-335-curve-mapping-range-and-tone.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender
Translate.

Batch 336 granskar 15 poster för kurvmålningens ritinställningar,
hörndetektering och kurvanpassning. Den normaliserar *djupprojektion* och
översätter *Refit* kontextuellt till *Anpassa om*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-336-curve-paint-drawing.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 337 granskar elva poster för kurvmålningens radie, tryck och
ritplan. Den förtydligar avsmalning längs kurvan och använder de geometriska
termerna *normal mot ytan* och *tangent mot ytan*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-337-curve-paint-radius-and-plane.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender
Translate.

Batch 338 granskar tio poster för kurvmålningens vyprojektion och
hörndetektering. Den anger att ritplanet är parallellt med vyporten och
ersätter lånordet *mappa* med det kontextuella *koppla* för ritplattans
tryckstyrning. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-338-curve-paint-projection.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 339 granskar tio etiketter och hjälptexter för begränsningstyper.
Den bevarar det formella UI-namnet *Child Of*, använder *löstagbar förälder*
för den faktiska relationen och godkänner de korrekta svenska texterna för
golv-, Följ bana-, Shrinkwrap- och Action-begränsningarna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-339-constraint-type-labels.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 340 granskar nio poster för Kopiera position-begränsningen och dess
gemensamma rigginställningar. Den normaliserar den synliga produktetiketten
till *Kopiera position-begränsning*, behåller B-Bone som Blenders namn och
använder konsekvent *benhuvud* och *benspets*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-340-copy-location-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 341 granskar 20 poster för Kopiera rotation-begränsningen. Den behåller
Euler och axelordningarna som tekniska benämningar, normaliserar
begränsningsetiketten och ersätter den engelska etiketten *Offset* med den
svenska UI-termen *Förskjutning* i hjälptexten. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-341-copy-rotation-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 342 granskar åtta poster för Kopiera skala-begränsningen. Den
normaliserar begränsningsetiketten och bekräftar den matematiska betydelsen av
*potens*, det additiva läget och jämn volymfördelning. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-342-copy-scale-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 343 granskar tolv poster för Kopiera transformationer-begränsningen.
Den översätter blandningslägenas tekniska hjälptexter till *fullständig ärvd
skalning*, *justerad ärvd skalning* och *delade kanaler* samt bekräftar
skjuvning som geometrisk term. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-343-copy-transforms-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 344 granskar fyra poster för Dämpad spårning-begränsningen. Den
normaliserar den synliga begränsningsetiketten, bekräftar den kortaste
rotationsvägen och använder *riktningsaxel* konsekvent. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-344-damped-track-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 345 granskar 15 poster för Följ bana-begränsningen. Den bekräftar
axel-, kurv- och förskjutningstermerna samt korrigerar *heading and banking*
till den tekniskt korrekta svenska termen *riktning och krängning*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-345-follow-path-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 346 granskar två poster i Följ spår-kontexten: kamerans relation till
rörelsespåret och filmspårningens kontextbundna etikett *Spår*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-346-follow-track-context.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 347 granskar 30 poster för den kinematiska IK-begränsningen. Den
normaliserar bland annat *kedjelängd*, *lösningsiterationer*, polmålet och
polvinkeln samt förtydligar inflytandesfärens begränsningslägen. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-347-kinematic-constraint.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 348 granskar fyra poster för Avståndsbegränsning, inklusive hur den
påverkar transformationer. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-348-limit-distance-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 349 granskar 21 poster för Positionsbegränsning och dess delade
axelgränser. Den normaliserar minimi- och maximiformerna samt deras
hjälptexter. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-349-limit-location-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 350 granskar 13 poster för Rotationsbegränsning och dess vinkelgränser.
Den gör formerna *övre* och *nedre* konsekventa för alla rotationsaxlar.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-350-limit-rotation-constraint.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 351 granskar fem poster för Skalbegränsning och Låst spårningsbegränsning.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-351-scale-and-locked-track-constraints.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 352 granskar 10 poster för Volymbevarande begränsning. Blenders
constraint-handbok bekräftar att fri axel behåller användarens skala medan de
två icke-fria axlarna kompenseras för att bevara volymen. Översättningen
använder därför *fri axel*, *icke-fria axlar*, *En axel* och *viloposition*
i stället för de mindre precisa formerna *enkel axel* och *i vila*.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-352-maintain-volume-constraint.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 353 granskar 13 poster för Spline IK:s skalningslägen. Blenders
handbok skiljer Y-skalning längs kurvans längd från X- och Z-skalning längs
dess normaler. Därför används *Y-skalningsläge*, *Benets ursprungliga skala*,
*Invers skala*, *Volymbevarande* och *Anpassa till kurva*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-353-spline-ik-scale-modes.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 354 granskar Transformationscachebegränsning. Den hämtar ett objekts
transformationsdata från en extern cachefil, exempelvis ett Alembic-arkiv;
den svenska sammansättningen är därför korrekt och har förts in i
terminologilistan. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-354-transform-cache-constraint.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 355 granskar fyra poster för kurvkartläggningens enskilda kurva,
klippning och vitnivå. *Klipp* begränsar här kurvvyn till en angiven gräns,
medan *Vitnivå* anger färgen som vitt mappas till för RGB-kurvor. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-355-curve-mapping-clip-and-white-level.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 356 granskar tre poster för kurvpunkter. Den förenar den tekniska
sammansättningen *kurvkontrollpunkt* med den kortare formen *kurvpunkt* och
gör indexhjälptexten naturlig svenska. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-356-curve-points.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 357 granskar 17 poster för profilbaneredigerarens geometri och
förinställningar. Byggnadstermerna *Gesimslist* och *Krönlist* ersätter
felöversättningarna för `Cornice Molding` och `Crown Molding`; `Line` blir
*Linje* i geometrikontext. Batchen gör också provtagningshjälptexterna
konsekventa. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-357-curve-profile-presets.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 358 granskar 21 poster för profilpunkter, kurvsegment och kurvsplines.
Den normaliserar bland annat *banpunkt*, *markeringsstatus*,
*kurvkontrollpunkt* och *kurvspline* samt gör den svenska datablokkonteksten
tydlig. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-358-curve-profile-points-and-splines.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 359 granskar 15 poster för Blenders beroendegraf. Den förenar
*beroendegraf*, *utvärderat datablock*, *visningslager* och den svenska
API-pluralen *ID:n*, och rättar den felaktiga hänvisningen till iteratorns
element. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-359-dependency-graph.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 360 granskar 23 poster för objektinstanser i beroendegrafen. Den
förtydligar iterator- och koordinatrymdskontexten, ersätter det felaktiga
*Visa själv* med *Visa objektet* och normaliserar API-termerna för utvärderade
objekt och beständiga ID:n. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-360-dependency-graph-object-instances.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 361 granskar sex statusposter för beroendegrafuppdateringar. Den
normaliserar datablock, ID och skuggning samt uttrycker uppdateringsstatus i
svenskt perfekt: *Objektets geometri/skuggning/transformation har
uppdaterats*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-361-dependency-graph-updates.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 362 granskar tio poster för kamerans säkra områden. Den ersätter
ordagranna och felaktiga former som *Åtgärd Säkra marginaler* med
*säkra marginaler för bildinnehåll* och gör motsvarande Title Safe-form till
*säkra marginaler för text*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-362-camera-safe-areas.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 363 granskar 16 poster för Dopebladets grundläggande filter. Den
normaliserar *filtreringssamling*, *F-kurvor*, *datablock* och
*animeringsdata* samt gör filterhjälptexterna konkreta med *Visa även …*.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-363-dope-sheet-filters.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

## Projektets aktualitet

Blender uppfyller aktualitetskravet. Den officiella nedladdningssidan anger
Blender **5.2.3 LTS**, släppt den 22 oktober 2026. Den officiella
releasesidan listar även 5.2 LTS och 4.5 LTS som aktiva LTS-grenar. Källor:

- <https://www.blender.org/download/>
- <https://www.blender.org/releases/>

## Lokal granskning

Den generiska komponenten **Blender Manual** har 868 unika, radvis granskade
svenska deltaöversättningar i batcherna 01–69. De har slagits ihop till en
samlad uppladdningsfil och delats i nio kandidater om högst 100 meddelanden:

| Kandidater | Antal meddelanden | Status |
| --- | ---: | --- |
| 01–08 | 100 per fil | Ingår i den samlade, importerade filen |
| 09 | 68 | Ingår i den samlade, importerade filen |

Råexporten i `exports/2026-11-04/` är oförändrad. Varje delta är kontrollerad
med syntax-, språk-, terminologi- och hemlighetsskanning; dokumenterade
undantag gäller endast RST-markup, produktnamn och tekniska termer.

## Upstreamstatus

### Blender UI

Den 5 november 2026 skickades den lokala deltafilen
`blender-ui-sv-reviewed-20261105-01.po` till komponenten **Blender UI / UI /
svenska** via Blender Translate. Filen innehåller 13 radvis granskade
korrigeringar från batcherna 01--03. Importen gjordes i läget *Lägg till som
översättning*, med översatta poster godkända vid importen. Blender Translate
bekräftade resultatet: **13 bearbetade, 13 uppdaterade, 0 hoppade över och 0
saknades**.

En ytterligare, avgränsad UI-delta med den kontextbundna korrigeringen
`tillgångsbibliotek` till `resursbibliotek` skickades därefter i
`blender-ui-sv-reviewed-20261105-02.po`. Blender Translate bekräftade även
den importen: **1 bearbetad, 1 uppdaterad, 0 hoppade över och 0 saknades**.

Två efterföljande UI-deltan justerade etiketten för resursbläddrarläget och
normaliserade *remote asset library* utan den felaktiga trippelkonsonanten i
`fjärrresursbibliotek`. Blender Translate bekräftade varje import:
`blender-ui-sv-reviewed-20261105-03.po` gav **1 bearbetad, 1 uppdaterad, 0
hoppade över och 0 saknades**, och
`blender-ui-sv-reviewed-20261105-04.po` gav **2 bearbetade, 2 uppdaterade, 0
hoppade över och 0 saknades**.

UI-inställningen *Hinting* hade dessutom den svenska stavningen
`Teckensnittshinting`. Den granskade rättelsen till `Teckensnittshintning`
skickades i `blender-ui-sv-reviewed-20261105-05.po`; Blender Translate
bekräftade **1 bearbetad, 1 uppdaterad, 0 hoppade över och 0 saknades**.

I samma UI-område användes *tillgångshylla* bara i regionetiketten *Asset
Shelf Header*, trots att den omgivande gränssnittsterminologin använder
*resurshylla*. Deltafilen `blender-ui-sv-reviewed-20261105-06.po` ändrar den
till `Resurshyllans rubrik`. Blender Translate bekräftade **1 bearbetad, 1
uppdaterad, 0 hoppade över och 0 saknades**.

Batch 07 rättade sex RNA-typnamn för noduttag där den svenska sammansättningen
hade tappat fog-s: `noduttaggränssnitt` blev `noduttagsgränssnitt`.
`blender-ui-sv-reviewed-20261105-07.po` importerades med resultatet **6
bearbetade, 6 uppdaterade, 0 hoppade över och 0 saknades**.

Batch 08 kompletterade de återstående UI-texterna för *remote asset library*
med `fjärranslutet resursbibliotek`, så att varken trippelkonsonanten i
`fjärrresursbibliotek` eller den ofullständiga formen *fjärrbibliotek* blir
kvar i denna kontext. `blender-ui-sv-reviewed-20261105-08.po` importerades
med resultatet **3 bearbetade, 3 uppdaterade, 0 hoppade över och 0 saknades**.

Efter språkgranskning av Batch 08 ersatte Batch 09 den onödigt täta
sammansättningen *nedladdningscachekatalogen* med `Cachekatalogen för
nedladdningar från fjärranslutna resursbibliotek`. Denna form är tydligare i
systeminställningens kontext. `blender-ui-sv-reviewed-20261105-09.po`
importerades med resultatet **1 bearbetad, 1 uppdaterad, 0 hoppade över och 0
saknades**.

Batch 10 rättade två avhuggna statusmeddelanden i Inställningar.
`blender-ui-sv-reviewed-20261105-10.po` ändrar dem till `Inga anpassade
MatCaps har konfigurerats` respektive `Inga anpassade HDRIs har
konfigurerats`. Blender Translate bekräftade **2 bearbetade, 2 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 11 rättade den ogrammatiska etiketten för opaciteten hos omarkerade
F-kurvor. Källkoden visar att reglaget är `fcurve_unselected_alpha` i
panelen F-Curves. `blender-ui-sv-reviewed-20261105-11.po` använder därför
`Opacitet för omarkerade`. Blender Translate bekräftade **1 bearbetad, 1
uppdaterad, 0 hoppade över och 0 saknades**.

Batch 12 normaliserade rubriken för de sparade valen för relativa sökvägar,
filkomprimering och inläsning av gränssnittet. Källan använder rubriken
`Default To`, medan samma inställningsvy redan använder `Standardinställningar`
för `Defaults`. `blender-ui-sv-reviewed-20261105-12.po` använder därför
`Standardinställningar`. Blender Translate bekräftade **1 bearbetad, 1
uppdaterad, 0 hoppade över och 0 saknades**.

Batch 13 skiljde dialogen för nyligen öppnade projekt från motsvarande
fillista. Källkoden för `WM_OT_clear_recent_projects` rensar uttryckligen
projektlistan, men den otextade katalogposten hade felaktigt samma måltext som
fillistan. `blender-ui-sv-reviewed-20261105-13.po` ändrar den till
`Rensa listan över senaste projekt`. Blender Translate bekräftade **1
bearbetad, 1 uppdaterad, 0 hoppade över och 0 saknades**.

Batch 14 rättade det interna tangentbindningsnamnet för färggradientpipettens
punktprovtagning. Källans `eyedropper_colorband.cc` visar att läget samplar
enskilda punkter till en färggradient. Därför ersätter
`blender-ui-sv-reviewed-20261105-14.po` den felstavade och oklara formen
`Mappning för punktsamplig med färggradients-pipett` med
`Modal mappning för punktprovtagning med färggradients-pipett`. Blender
Translate bekräftade **1 bearbetad, 1 uppdaterad, 0 hoppade över och 0
saknades**.

Batch 15 rättade Dynamic Paint-inställningens sakterm. Källans
`rna_dynamicpaint.cc` definierar alternativet som femfaldig *multisampling*
för att jämna ut målningskanter, inte som flera simuleringar.
`blender-ui-sv-reviewed-20261105-15.po` ändrar därför `multisimulering` till
`multisampling`. Blender Translate bekräftade **1 bearbetad, 1 uppdaterad, 0
hoppade över och 0 saknades**.

Batch 16 normaliserade två hjälptester för nätåtkomliga resurser. De använder
nu `fjärranslutna resurser`, i linje med komponentens term
`fjärranslutet resursbibliotek`, i stället för den svårlästa formen
`fjärrresurser` med tre r i följd. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-16.po`: **2 bearbetade, 2 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 17 normaliserar *Retiming Key* i sekvensredigeraren till
`tidsanpassningsnyckel`. Blender-källan och den officiella manualen visar att
nycklarna flyttar en bildruta i en remsa och därmed sträcker eller drar ihop
tidsflödet. Formen följer den redan vanligaste svenska UI-termen och ersätter
den otydliga, inkonsekventa formen `omtidningsnyckel` i tretton kontextbundna
poster. Blender Translate bekräftade `blender-ui-sv-reviewed-20261105-17.po`:
**13 bearbetade, 13 uppdaterade, 0 hoppade över och 0 saknades**.

Batch 18 rättar två kvarvarande hänvisningar till Blenders separata interna
urklipp i sekvensredigeraren respektive posläget. Den felaktigt konkreta
formen `interna klippbordet` ersätts med samma term som den omgivande UI-texten
redan använder: `interna urklippet`. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-18.po`: **2 bearbetade, 2 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 19 fortsätter samma avgränsade granskning av Blenders interna urklipp.
Fyra rester med felaktigt obestämd `det interna urklipp` eller `internt
urklipp` får den konsekventa och grammatiskt korrekta formen `det interna
urklippet`. Poster gäller nyckelrutor, rörelsespår och material. Lokal
kvalitetssäkring är klar. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-19.po`: **4 bearbetade, 4 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 20 rättar API-hjälptexten för `ActionSlot.active`. Blender-källan
definierar `action.slots.active` som det faktiska Python-egenskapsnamnet, så
det lämnas exakt oförändrat. Den svenska hjälptipsmeningen rättas däremot till
`Anger om detta är den aktiva slotten och kan ställas in genom att tilldela
action.slots.active` och följer den dokumenterade böjningen av *slot*.
Lokal kvalitetssäkring är klar. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-20.po`: **1 bearbetad, 1 uppdaterad, 0
hoppade över och 0 saknades**.

Batch 21 rättar den ogrammatiska etiketten för
`DopeSheet.show_only_slot_of_active_object`. Den längre hjälptexten till samma
egenskap använder redan den naturliga och sakligt korrekta formen `sloten för
det aktiva objektet`; etiketten normaliseras till samma formulering. Lokal
kvalitetssäkring är klar. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-21.po`: **1 bearbetad, 1 uppdaterad, 0
hoppade över och 0 saknades**.

Batch 22 granskar animeringssystemets tekniska *slots* i deras riktiga
Action-kontext. Sju texter blandade tidigare ihop datatypen med vanliga
`platser` eller den avvikande sammansättningen `åtgärdsplatser`. Källreferenser
från `bpy.types.Action`, `ANIM_OT_*`, Rigify och
`animrig/intern/keyframing.cc` visar att samtliga avser Blenders Action Slots.
De använder nu konsekvent `åtgärdsslotar` eller `slotar` där åtgärdskontexten
redan är given. Lokal kvalitetssäkring är klar. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-22.po`: **7 bearbetade, 7 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 23 följer samma terminologi i fyra fel- och spärrmeddelanden. Blender-
källan visar att de två första avser egenskapen `action_slot` i
`bl_operators/anim.py` och att de två andra validerar `ActionSlot` i
`rna_action.cc`. `Action slot` är här ett översättningsbart användargränssnitt,
inte ett API-identifierarnamn; meddelandena använder därför konsekvent
`åtgärdsslot` och dess naturliga plural. Lokal kvalitetssäkring är klar;
Blender Translate bekräftade `blender-ui-sv-reviewed-20261105-23.po`:
**4 bearbetade, 4 uppdaterade, 0 hoppade över och 0 saknades**.

Batch 24 åtgärdar tre verkliga fall av tre identiska konsonanter. Strängarna
för Grease Pencil Line Art och `RegionView3D` skrev tidigare `klippplan` med
tre p. Språkrådets konsonantstrykningsregel och etablerad svensk CAD-
terminologi ger formen `klippningsplan`, som nu används i etiketter och
hjälptext. Lokal kvalitetssäkring är klar. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-24.po`: **3 bearbetade, 3 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 25 följer Blenders egen UI-term för *Wireframe*. Den synliga etiketten
är `Trådram`, medan en hjälprad tidigare skrev `trådmodellläge`, med tre l i
följd. I dess specifika lägeskontext blir `trådramsläget` både konsekvent med
etiketten och språkriktigt. Lokal kvalitetssäkring är klar. Blender Translate
bekräftade `blender-ui-sv-reviewed-20261105-25.po`: **1 bearbetad, 1
uppdaterad, 0 hoppade över och 0 saknades**.

Batch 26 granskar de återstående direkta hänvisningarna till *Asset Browser*
i UI-komponenten. Den etablerade synliga termen är `resursbläddrare`, inte den
äldre formen `tillgångsbläddrare`. Nio sammanhängande poster rättar därför
bland annat importinställningar, Pose Library-meddelanden och kataloghjälp för
nodgruppstillgångar. `blender-ui-sv-reviewed-20261105-26.po` är lokalt
kontrollerad med `msgfmt`, l10n-lint, Hunspell, diffkontroll och Gitleaks.
Blender Translate bekräftade **9 bearbetade, 8 uppdaterade, 1 hoppad över och
0 saknade**. Den överhoppade posten räknas inte som bekräftad ändring.

Batch 27 fortsätter samma begränsade UI-granskning med elva återstående
inställningar, etiketter och hjälprader som fortfarande lämnade *Asset
Browser* på engelska eller använde den äldre termen. Den normaliserar
`resursbläddrare` och `resursbibliotek` i deras konkreta gränssnittskontext.
`blender-ui-sv-reviewed-20261105-27.po` har klarat lokal syntax-, språk-,
stavnings-, diff- och hemlighetskontroll. Blender Translate bekräftade **11
bearbetade, 7 uppdaterade, 4 hoppade över och 0 saknade**. De fyra överhoppade
posterna räknas inte som bekräftade ändringar.

Batch 28 granskar cacheinställningar för vätskesimulering och
sekvensredigeraren. UI-texterna hade växlat mellan onödigt avstavade former
som `Cache-katalog` och `Diskcache-katalog` samt otydliga omskrivningar.
Termlistan har kompletterats med `cachekatalog`; deltafilen använder också
`diskcachekatalog`, `standardcachekatalog` och `cachesökväg` i sina respektive
inställnings- och felmeddelandekontexter. Den är lokalt kontrollerad med
`msgfmt`, l10n-lint, Hunspell, diffkontroll och Gitleaks. Blender Translate
bekräftade **6 bearbetade, 3 uppdaterade, 1 hoppad över och 2 saknade**.
De saknade strängarna, `Disk Cache Directory` och `Override default directory`,
har försvunnit eller ändrats uppströms och räknas inte som importerade.

Batch 29 granskar *bake* i den sammanhang där Blender beräknar
rörelsebanor, normaldata och texturattribut. Den rättar fyra uppenbara
engelskrester och tre otydliga hjälprader: `Bake` används konsekvent som
`baka` eller `bakning`, medan kamerarummet behålls som komponentens redan
etablerade term för *camera space*. `blender-ui-sv-reviewed-20261105-29.po`
och termlistan har klarat lokal syntax-, språk-, stavnings-, diff- och
hemlighetskontroll. Blender Translate bekräftade **7 bearbetade, 7 uppdaterade,
0 hoppade över och 0 saknade**.

Batch 30 granskar den intilliggande inställningen *Normal Space*. Blender
Manual använder redan `tangentrymd`, `objektrymd` och `världsrymd` för de
värden som denna inställning väljer mellan. Den tidigare ordagranna formen
`normalt utrymme` är därför tvetydig; UI-termen normaliseras till
`normalrymd` i både etikett och hjälptext. Deltafilen och termlistan är lokalt
kontrollerade med `msgfmt`, l10n-lint, Hunspell, diffkontroll och Gitleaks.
Blender Translate bekräftade **2 bearbetade, 0 uppdaterade, 2 hoppade över och
0 saknade**. Servern hade alltså redan samma eller nyare värden; batchen räknas
inte som en bekräftad upstreamändring.

Batch 31 granskar Animation Editors rörelsebanor och lökskalning. Tidigare
strängar blandade engelskan *Onion-skinning* med den felaktiga ordagranna
formen `avskalning av lök`; två texter hade dessutom `Slutbild` respektive
felstavade `Startram` i stället för bildrutor. Batchen använder konsekvent
`lökskalning`, `startbildruta`, `slutbildruta` och de synliga lägena
`Omkring bildrutan` respektive `På nyckelrutor`. Deltafilen och termlistan är
lokalt kontrollerade med `msgfmt`, l10n-lint, Hunspell, diffkontroll och
Gitleaks. Blender Translate bekräftade **6 bearbetade, 6 uppdaterade, 0
hoppade över och 0 saknade**.

Batch 32 granskar riggningspanelens B-Bone-kontroller. Sex hjälprader blandade
engelska `offset` med felaktig svensk ordföljd och skiftande skrivning av
B-Bone-kurvan. De använder nu konsekvent `förskjutning`, `vridningsförskjutning`
och tydliga X-/Z-axelhandtag utan att ändra det synliga Blender-namnet
`B-Bone`. Deltafilen och terminologin är lokalt kontrollerade med `msgfmt`,
l10n-lint, Hunspell, diffkontroll och Gitleaks. Blender Translate bekräftade
**6 bearbetade, 6 uppdaterade, 0 hoppade över och 0 saknade**.

Batch 33 fortsätter med B-Bonens mappningsläge, rullning och skalning.
Reglernas svenska text använder `Böjd`, `inrullning`, `utrullning` och
`rullningsförskjutning`, medan B-Bone behålls som det synliga Blender-namnet.
Deltafilen och terminologin har passerat `msgfmt`, l10n-lint, Hunspell,
diffkontroll och Gitleaks. `svlang` flaggar B-Bone- och vilopos-ord samt
bisatsernas verbföljd, men dessa är manuellt bedömda som korrekta i den
tekniska UI-kontexten. Blender Translate bekräftade **10 bearbetade, 6
uppdaterade, 4 hoppade över och 0 saknade**. De överhoppade posterna hade
alltså redan samma eller nyare värden på servern.

Batch 34 granskar B-Bonens segmentering, visningsmått samt två armaturtexter
om underordnade ben och bensamlingar. Den normaliserar bland annat
`B-Bone-segment`, `B-Bone-visningsbredd i X/Z` och `bensamlingar`.
Deltafilen och termlistan har passerat `msgfmt`, l10n-lint, svlang, Hunspell,
diffkontroll och Gitleaks; Hunspell-orden utgörs av B-Bone-namn och PO-metadata.
Blender Translate bekräftade **8 bearbetade, 0 uppdaterade, 8 hoppade över och
0 saknade**. Samtliga poster hade alltså redan samma eller nyare värden på
servern.

Batch 35 granskar armaturens kuvertdeformation och huvudpositioner. Den
använder konsekvent `kuvertdeformering`, `riggskelett` och svenska termer för
benets huvudände utan att ändra Blender-namnet *Envelope*. Deltafilen och
termlistan har passerat `msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll och
Gitleaks. `svlang` markerar två nominala UI-etiketter utan finit verb; de är
manuellt verifierade som korrekta. Blender Translate bekräftade **9 bearbetade,
0 uppdaterade, 9 hoppade över och 0 saknade**. Samtliga poster hade redan samma
eller nyare värden på servern.

Batch 36 granskar armaturens inställning för ärvd skalning. Tidigare svenska
texter blandade vardagsord som `förälder`, `barn`, `saxen` och engelska
`Legacy`; batchen använder i stället den tekniskt korrekta hierarkin
`överordnat`/`underordnat`, `skjuvning` och `äldre version`. Deltafilen och
termlistan har passerat `msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll och
Gitleaks. `svlang` markerar en korrekt bisats och en kort uppmaning; de är
manuellt verifierade. Blender Translate bekräftade **10 bearbetade, 0
uppdaterade, 10 hoppade över och 0 saknade**. Samtliga poster hade redan samma
eller nyare värden på servern.

Batch 37 granskar motsvarande armaturtexter för svansänden, kuvertets
svansradie, anslutna ben och cyklisk förskjutning. I den här dataegenskapsvyn
är `svans` korrekt för *Tail*, medan constraints kan använda den etablerade
formen `spets`. Batchen har passerat `msgfmt`, l10n-lint, svlang, Hunspell,
diffkontroll och Gitleaks. `svlang`-markeringarna är två nominala egenskaper
och en korrekt inledd bisats; de är manuellt verifierade. Blender Translate
bekräftade **10 bearbetade, 0 uppdaterade, 10 hoppade över och 0 saknade**.
Samtliga poster hade redan samma eller nyare värden på servern.

Batch 38 granskar armaturens deformering, rullning, kuvertpåverkan, lokal
position och relativ överordning. Den normaliserar framför allt *Vertex Group*
till `hörnpunktsgrupp` enligt den projektspecifika termlistan, i stället för
den för grova formen `hörngrupp`. Deltafilen och termlistan har passerat
`msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll och Gitleaks. De fyra
Hunspell-träffarna är tekniska sammansättningar och en UI-uppmaning; de är
manuellt verifierade. Blender Translate bekräftade **12 bearbetade, 4
uppdaterade, 8 hoppade över och 0 saknade**. De fyra uppdateringarna omfattar
terminologin för hörnpunktsgrupper och underordnade objekt.

Batch 39 granskar skalutjämning och de närliggande texterna för bensamlingar.
Den ersätter engelsk etiketttext i hjälptexten med de synliga svenska reglagen
`Skala in/ut` och använder konsekvent `datablock` samt `riggskelett`. Deltafilen
och termlistan har passerat `msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll
och Gitleaks. Blender Translate bekräftade **4 bearbetade, 1 uppdaterad, 3
hoppade över och 0 saknade**. Uppdateringen ersätter den engelska hjälpetiketten
för Skala in/ut.

Batch 40 granskar bensamlingarnas hierarki, biblioteksöverskrivningar och
effektiva synlighet. Den använder `överordnad`, `bensamling`,
`biblioteksöverskrivning` och `effektiv synlighet` konsekvent i Blenderns
trädvy. Deltafilen och termlistan har passerat `msgfmt`, l10n-lint, svlang,
Hunspell, diffkontroll och Gitleaks. Svlangs låga katalogpoäng kommer från
korta booleska egenskapstexter och imperativ; de är manuellt verifierade.
Blender Translate bekräftade **12 bearbetade, 0 uppdaterade, 12 hoppade över
och 0 saknade**. Samtliga poster hade redan samma eller nyare värden på
servern.

Batch 41 granskar Rigify-egenskaper och metadata för bensamlingar: färg- och
urvalsuppsättningar, panelknappar, medlemskap och aktiv bensamling. `ID` och
andra formella identifierare behålls, medan synlig svensk UI-text använder
`färguppsättning`, `urvalsuppsättning` och `bensamling`. Deltafilen och
termlistan har passerat `msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll och
Gitleaks. Den enda svlang-markeringen gäller en korrekt parentetisk
UI-beskrivning. Blender Translate bekräftade **15 bearbetade, 0 uppdaterade,
15 hoppade över och 0 saknade**. Samtliga poster hade redan samma eller nyare
värden på servern.

Batch 42 granskar egenskaperna för benfärger och deras paletter. Den rättar
svensk ordföljd och kommatering, och använder det etablerade `i stället för`.
Deltafilen med fyra poster samt arbetskatalogen har passerat `msgfmt`,
l10n-lint, svlang, Hunspell, diffkontroll och Gitleaks. Svlangs enda träff
gäller det avsiktligt bevarade API-värdet `CUSTOM`. Blender Translate
bekräftade **4 bearbetade, 1 uppdaterad, 3 hoppade över och 0 saknade**.

Batch 43 granskar penselverktygens kapacitetsbeskrivningar för bildmålning,
skulptering, hörnpunktsmålning och viktmålning. Den ersätter felöversatta
etiketter som `skulpterat flygplan` med domänkorrekta termer och dokumenterar
`jämnt penseldrag` samt `avståndsdämpning`. Batchen är lokalt kontrollerad och
arkiverad. Blender Translate bekräftade **20 bearbetade, 10 uppdaterade, 10
hoppade över och 0 saknade**.

Batch 44 granskar de första inställningarna för kurvskulpteringspenslar.
Den normaliserar bland annat kurvlängd, kurvradie, täthetspensel och
avtagande längs kurvparametern, samt rättar den felaktiga UI-termen `Poäng per
kurva`. Svlangs V2-markeringar gäller avsiktligt korta UI-etiketter och
imperativ, inte fullständiga satser. Blender Translate bekräftade **18
bearbetade, 13 uppdaterade, 5 hoppade över och 0 saknade**.

Batch 45 granskar Grease Pencil-penslarnas rit- och forminställningar. Den
ersätter bland annat kvarvarande engelska `Vertex Color` med
`hörnpunktsfärg`, normaliserar ändtyp och kurvslumpning och rättar den
ogiltiga formen `Dilatat/kontrakt`. Blender Translate bekräftade **16
bearbetade, 11 uppdaterade, 5 hoppade över och 0 saknade**.

Batch 46 granskar Grease Pencil-penslarnas raderings- och fyllningslägen.
Den rättar bland annat `Poäng` till `Punkt`, `Poseringsläge` till
`Slutningsläge` och engelska rester i hjälptexterna. Blender Translate
bekräftade **21 bearbetade, 18 uppdaterade, 3 hoppade över och 0 saknade**.

Batch 47 granskar efterbehandling och slumpning av Grease Pencil-streck.
Den ersätter bland annat `Jitter` med den kontextuella svenska termen
`slumpning`, normaliserar underindelningssteg och rättar egenskapen för
streckkollision. Blender Translate bekräftade **19 bearbetade, 16
uppdaterade, 3 hoppade över och 0 saknade**. Svlangs V2-markeringar gäller
korta UI-beskrivningar med underordnade satser.

Batch 48 granskar Grease Pencil-inställningar för tryck, material, slumpning
och hörnpunktsfärg. Förslagen från parallella delgranskningar har jämförts med
de exakta Blender-källkommentarerna innan de införts; breda delade poster som
`Stroke` lämnas orörda. Blender Translate bekräftade **22 bearbetade, 13
uppdaterade, 6 hoppade över och 3 saknade**. De saknade posterna var de tre
kontextspecifika hjälptexterna för hörnpunktsfärgens lägen; servern rapporterade
att deras källsträngar inte längre finns, så de har inte ersatts mekaniskt.

Batch 49 granskar CacheFile- och kamerabakgrundens rader. Den normaliserar
tekniska sammansättningar som *cachelager* och *objektsökväg* samt skiljer
kameraobjektens djupplacering *bakom/framför* från allmän riktning. Batchen är
lokalt kontrollerad och arkiverad. Blender Translate bekräftade **13
bearbetade, 6 uppdaterade, 7 hoppade över och 0 saknade**.

Batch 50 granskar kamera- och tygsimuleringens särskilda inställningar.
Den normaliserar bland annat fotografins *bländartal*, stereokamerans
polsammanfogning samt fysiktermerna *restitutionskoefficient* och
*impulsbegränsning*. Förslagen har verifierats mot respektive RNA-kontext och
oberoende parallella granskningar. Blender Translate bekräftade **24
bearbetade, 13 uppdaterade, 11 hoppade över och 0 saknade**.

Batch 51 granskar tygsimuleringens fjäder- och massinställningar. Termerna
*dragstyvhet*, *hörnpunktsmassa* och *hörnpunktsgrupp för självkollision* har
kontrollerats både mot den exakta RNA-kontexten och oberoende delgranskningar.
Blender Translate bekräftade **20 bearbetade, 11 uppdaterade, 9 hoppade över
och 0 saknade**.

Batch 52 granskar de följande tyg- och samlingsraderna. Den normaliserar
hörnpunktsgrupper, voxelrutnät och lösarresultat samt rättar den hierarkiska
termen *underordnad samling*. Blender Translate bekräftade **15 bearbetade, 9
uppdaterade, 6 hoppade över och 0 saknade**.

Batch 53 granskar kollisions- och färghanteringens UI-etiketter. Profilnamn
och färgstandarder lämnas medvetet orörda; endast kontextbundna UI-termer som
*bildskärmsenhet*, *ingångsfärgrymd* och *visningstransformering* ingår.
Batchen är lokalt validerad och arkiverad. Blender Translate bekräftade **10
bearbetade, 3 uppdaterade, 4 hoppade över och 3 saknade**. De saknade
katalogposterna var `Display Device`, `Display device name` och `View
Transform`; servern har inte längre motsvarande källsträngar.

Batch 54 granskar färgrampsredigeringens konkreta UI-rader. Den rättar en
felaktigt delad sammansättning, en uppenbart förvanskad HSV-översättning, en
felaktig interpolationsterm och böjningen i hjälptipsen för färgstopp. Den
avgränsade deltafilen är lokalt validerad och arkiverad. Blender Translate
bekräftade **5 bearbetade, 3 uppdaterade, 2 hoppade över och 0 saknade**.

Batch 55 granskar begränsningarnas och animeringssystemets konkreta
gränssnitt. Den rättar maskinöversatta begränsningsetiketter och fullföljer
den etablerade termen *åtgärdsslot* för `ActionConstraint` och NLA-remsor.
Två oberoende, skrivskyddade delgranskningar har jämförts med den exakta
RNA-kontexten. Deltafilen är lokalt validerad och arkiverad. Blender Translate
bekräftade **12 bearbetade, 4 uppdaterade, 8 hoppade över och 0 saknade**.

Batch 56 granskar de konkreta Copy Constraint-typerna och deras egenskaper.
Den ersätter maskinöversatta sammansättningar, normaliserar *position* och
*transformation* samt rättar den felaktiga statusetiketten `DEPRECATED`.
Deltafilen är lokalt validerad och arkiverad. Blender Translate bekräftade
**10 bearbetade, 7 uppdaterade, 3 hoppade över och 0 saknade**.

Batch 57 granskar kamera- och objektspårning samt IK-begränsningars tydliga
etiketter. Den rättar bland annat en omvänd villkorssats, X/Y/Z-positioner,
filmklippskontext och `IK-typ`. Deltafilen är lokalt validerad och arkiverad.
Blender Translate bekräftade **9
bearbetade, 3 uppdaterade, 6 hoppade över och 0 saknade**.

Batch 58 tillämpar den verifierade Constraint-terminologin för riktnings- och
banbegränsningar. *Shrinkwrap* behålls medvetet som Blenders synliga
funktionsnamn; den felaktiga betydelsen `Krympfilm` tas bort. Deltafilen är
lokalt validerad och arkiverad. Blender Translate bekräftade **10 bearbetade,
4 uppdaterade, 6 hoppade över och 0 saknade**. Servern markerade den avsiktligt
oförändrade produkttermen *Shrinkwrap* som kontrollvarning; det är en
förväntad falsk positiv enligt projektets terminologibeslut.

Batch 59 granskar IK-, begränsnings- och Shrinkwrap-kontroller rad för rad.
Tre oberoende, skrivskyddade delgranskningar har jämförts med samma RNA- och
UI-kontext. Den lokalt validerade deltafilen normaliserar bland annat
*hörnpunkt*, *projektionsaxel*, *målnormal* och de konkreta
begränsningstyperna. Deltafilen är arkiverad i översättningsförrådet.
Blender Translate bekräftade **31 bearbetade, 16 uppdaterade, 15 hoppade över
och 0 saknade**.

Batch 60 granskar Spline IK, Transform Constraint och kurvverktyg rad för
rad. Tre oberoende, skrivskyddade delgranskningar har kontrollerats mot
RNA-kontexten. Den lokalt validerade deltafilen normaliserar
begränsningsetiketter, blandningslägen, kurvkartläggning och topologitermen
*stödslinga*. Deltafilen är arkiverad i översättningsförrådet. Blender
Translate bekräftade **31 bearbetade, 11 uppdaterade, 20 hoppade över och 0
saknade**.

Batch 63 granskar Dynamic Paint och RNA-egenskaper rad för rad. Två oberoende, skrivskyddade delgranskningar har jämförts med RNA- och Dynamic Paint-kontext. Deltafilen är arkiverad i översättningsförrådet. Blender Translate bekräftade **13 bearbetade, 3 uppdaterade, 10 hoppade över och 0 saknade**.

Batch 64 granskar Dynamic Paint, redigeringsben, F-kurvor och FFmpeg-inställningar rad för rad. Tre skrivskyddade delgranskningar har jämförts med RNA- och panelkontext; huvudgranskningen avgränsar ändringarna till 62 säkra strängar. Deltafilen är arkiverad i översättningsförrådet. Blender Translate bekräftade **62 bearbetade, 39 uppdaterade, 22 hoppade över och 1 saknad**. Den saknade strängen, *Phase Multiple*, fanns inte längre i serverkatalogen och kräver därför ingen manuell åtgärd.

Batch 65 normaliserar animationssystemets *Driver* till *drivrutin* i dess exakta RNA-, Graph Editor- och operatörskontext. Två oberoende terminologigranskningar och den lokala Blender-manualen bekräftar termen; hårdvarudrivrutiner har lämnats orörda. Deltafilen innehåller 20 säkra UI-strängar och är arkiverad i översättningsförrådet. Blender Translate bekräftade **20 bearbetade, 10 uppdaterade, 10 hoppade över och 0 saknade**.

Batch 66 granskar F-kurvmodifierare och en liten, avgränsad mängd kraftfältsinställningar rad för rad. Tre skrivskyddade delgranskningar har jämförts med den svenska Blender-manualen, RNA-kontext och tidigare terminologi. Deltafilen innehåller 15 säkra UI-strängar, är lokalt validerad och arkiveras för import.

Batch 67 granskar filbläddraren och resursbläddrarens datablockfilter rad för rad. Tre oberoende, skrivskyddade delgranskningar har jämförts med RNA-kontexten och den lokala Blender-terminologin. Deltafilen innehåller 29 säkra UI-strängar och normaliserar bland annat *datablock*, *resursbläddrare*, *filhanterare* och *nodträd*. Den är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 68 granskar resursbläddrarens importmetoder rad för rad. Tre oberoende, skrivskyddade delgranskningar har verifierat skillnaden mellan *Länk*, *Lägg till* och *Lägg till (återanvänd data)* i exakt RNA-kontext. Deltafilen innehåller 10 säkra UI-strängar, är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 69 granskar vätskesimuleringens cache- och visningsinställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har kontrollerats mot Mantaflow- och RNA-kontexten. Deltafilen innehåller 27 säkra UI-strängar och rättar bland annat *cachekatalog*, *brusskala*, *FLIP*, cacheformat och vätskerutnät. Den är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 70 granskar vätskesimuleringens rutnät, mesh- och brusinställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har kontrollerats mot RNA-kontexten. Deltafilen innehåller 23 säkra UI-strängar och normaliserar bland annat *temperaturrutnät*, *MAC-rutnät*, *vätskemesh*, *vätskebrus*, *hörnpunktsgrupp* och *initialhastighet*. Den är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 71 granskar Fluid Flow-inställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har jämförts med samma RNA-kontext. Deltafilen innehåller 11 säkra UI-strängar och rättar bland annat *hörnpunktsgrupp*, *initialhastighet*, *volymemission*, *meshytan* och *Z-förskjutning*. Den är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 72 granskar Freestyle-inställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har jämförts med renderer- och RNA-kontext. Deltafilen innehåller 14 säkra UI-strängar och normaliserar bland annat *Freestyle-linjeuppsättning*, *linjestil*, *kanttypskombination*, *bortgallring* och *vykartscache*. Den är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 73 granskar Grease Pencil- och annotationsinställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har verifierat den konkreta UI-kontexten. Deltafilen innehåller 15 säkra UI-strängar och rättar bland annat *lökskalning*, *vinkelsnäppning*, streckprojektion, *geometriattribut* och *färgattribut*. Den är lokalt validerad och arkiveras för import; något importresultat finns ännu inte.

Batch 74 granskar Grease Pencil-lager, maskeringslager och lagerträd rad för rad. Tre oberoende, skrivskyddade delgranskningar har verifierats mot RNA-kontexten och projektets befintliga terminologi. Deltafilen innehåller 43 säkra UI-strängar och normaliserar bland annat *Grease Pencil-bildrutor*, *maskeringslager*, *lökskalning*, *visningslager*, *Grease Pencil-lagergrupp* och *lagrets förflyttning*. Den är lokalt validerad och arkiveras för import till Blender Translate; något importresultat finns ännu inte.

Batch 75 granskar Actions bildruteintervall, armaturvisning och penselinställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har kontrollerats mot RNA-kontexten. Deltafilen innehåller 58 säkra UI-strängar och normaliserar bland annat *bildruteintervall*, *bensamling*, *viloposition*, *penseldatablock*, *hörnpunkt*, *gränsavtagande* och *oskärpeläge*. Den är lokalt validerad och arkiveras för import till Blender Translate; något importresultat finns ännu inte.

Batch 76 granskar penslars tygsimulering, avtagande, Grease Pencil-verktyg och viktmålning rad för rad. Tre oberoende, skrivskyddade delgranskningar har jämförts med RNA-kontext och Blender-terminologin. Deltafilen innehåller 48 säkra UI-strängar och rättar bland annat *penselns egenskaper*, *simuleringsavtagande*, *meshen*, *penseldragsprov*, *hörnpunktsgrupp*, *streckpunkt* och *Grease Pencil-inställningar*. Den är lokalt validerad och arkiveras för import till Blender Translate; något importresultat finns ännu inte.

Batch 77 granskar penselns mask-, plan- och poseringsinställningar rad för rad. Tre oberoende, skrivskyddade delgranskningar har jämförts med RNA-kontext. Deltafilen innehåller 28 säkra UI-strängar och rättar bland annat *masktexturplats*, *planförskjutning*, *poserings-IK-segment*, *ansiktsuppsättningar*, *utjämningsiterationer*, *stencilmått* och *radieavtagande*. Den är lokalt validerad och arkiveras för import till Blender Translate; något importresultat finns ännu inte.

Batch 78 granskar penselns automaskning, tryckinställningar och kamerans visningsparametrar rad för rad. Tre oberoende, skrivskyddade delgranskningar har kontrollerats mot RNA-kontexten. Deltafilen innehåller 24 säkra UI-strängar och normaliserar bland annat *områdesnormal*, *visningsnormal*, *marköröverlägg*, *planförskjutning*, *slumpningstryck*, *bildruteförskjutning* och *synfält*. Den är lokalt validerad och arkiveras för import till Blender Translate; något importresultat finns ännu inte.

Batch 79 granskar kamera-, samlings- och kurvinställningar rad för rad. Tre
oberoende, skrivskyddade delgranskningar har jämförts med RNA-kontext och
terminologilistan. Deltafilen innehåller 67 säkra UI-strängar, bland annat
*panoramatyp*, *samlingsfärg*, *korsningsprioritet*, *fyllningsläge*,
*sökvägsvaraktighet* och *vridningsmetod*. `msgfmt` och diffkontrollen
passerar; l10n-lint visar endast en förväntad avslutande skiljeteckensskillnad
mot en källsträng med citerad inställning. Svlang- och Hunspell-träffarna är
fackord och sammansättningar som har kontrollerats manuellt. Batchen är lokalt
validerad och arkiveras för import till Blender Translate; något importresultat
finns ännu inte.

Batch 80 granskar kurvbanor, textobjekt och Freestyle rad för rad. Tre
oberoende, skrivskyddade delgranskningar har jämförts med RNA-kontext och
terminologilistan. Deltafilen innehåller 57 säkra UI-strängar och rättar bland
annat *förflyttningsbana*, *kurvdatablock*, *brödtext*, *kapitäler*,
*textruteöverflöde*, *Freestyle-linjestil*, *streckgeometri* och
*sorteringsnyckel*. `msgfmt`, l10n-lint och diffkontrollen passerar. Svlang-
och Hunspell-träffarna är förväntade Blender-fackord och svenska
sammansättningar som har kontrollerats manuellt. Batchen är lokalt validerad
och arkiveras för import till Blender Translate; något importresultat finns
ännu inte.

Batch 81 granskar Freestyle-kedjor, Grease Pencil-lager och bildinställningar
rad för rad. Tre oberoende, skrivskyddade delgranskningar har arbetat med
avgränsade stränggrupper och jämförts mot RNA-kontexten. Deltafilen innehåller
44 säkra UI-strängar och normaliserar bland annat *kedjedelning*,
*streckgeometri*, *lökskal*, *nyckelbildruta*, *renderingsplats* och
*sömmarginal*. `msgfmt`, l10n-lint och diffkontrollen passerar. Svlang-
träffarna är kontrollerade tekniska sammansättningar och korta UI-etiketter.
Batchen är lokalt validerad och arkiveras för import till Blender Translate;
något importresultat finns ännu inte.

Batch 82 granskar bildkällor, gitter, biblioteksåsidosättningar, ljus och
ljussonder i tre separata radintervall. Tre oberoende delgranskningar har
jämförts mot RNA-kontext och terminologilistan. Deltafilen innehåller 41 säkra
UI-strängar, bland annat *UDIM-platta*, *flyttalsbuffert*, *formnyckel*,
*biblioteksåsidosättning*, *Cycles-ljusinställningar* och *ljussond*.
`msgfmt`, l10n-lint och diffkontrollen passerar. Hunspell-träffarna är
kontrollerade Blender-termer och sammansättningar. Batchen är lokalt validerad
och arkiveras för import till Blender Translate; något importresultat finns
ännu inte.

Batch 61 granskar kurvdata, beroendegrafen och Dope Sheet-filter rad för rad.
Två oberoende, skrivskyddade delgranskningar har jämförts med RNA-kontext och
befintlig Blender-terminologi. Den lokalt validerade deltafilen normaliserar
bland annat *kurvsegment*, *kurvspline*, *visningslager* och
*beroendegraf*. Deltafilen är arkiverad i översättningsförrådet. Blender
Translate bekräftade **18 bearbetade, 8 uppdaterade, 10 hoppade över och 0
saknade**. Den oförändrade Workspace-etiketten *Shading* ingick medvetet som
en etablerad Blender-beteckning; serverns kontrollvarning för identisk
käll- och måltext är därför en förväntad falsk positiv.

Batch 62 granskar Dope Sheet-filtren och deras närmaste RNA-etiketter rad
för rad. Två oberoende, skrivskyddade delgranskningar har kontrollerats mot
panelens egenskaper och den befintliga Action Slot-terminologin. Den lokalt
validerade deltafilen normaliserar filteretiketter, `datasökväg` och
`transformationsrymd`. Deltafilen är arkiverad i översättningsförrådet.
Blender Translate bekräftade **13 bearbetade, 5 uppdaterade, 8 hoppade över
och 0 saknade**.

Den aktuella komponenten omfattar 40 427 strängar och visas som 100 procent
översatt. Det betyder inte att hela katalogen är radgranskad: vyn visar även
18 403 strängar med förslag och 629 översatta strängar med avfärdade
kontroller. Fortsatt UI-arbete ska därför ske i avgränsade, kontextstyrda
delar och inte utifrån procenttalet ensamt.

Batch 83 granskar volymljussonder, material och meshtopologi i tre separata
radintervall. Tre oberoende skrivskyddade delgranskningar har jämförts mot
RNA-kontext och terminologilistan. Den lokalt validerade deltafilen innehåller
79 säkra UI-strängar, bland annat *utvidgningsradie*, *ljussond*,
*baksidesgallring*, *strålspårad transmission*, *texturplats* och
*hörnpunktsmarkering*. `msgfmt` och l10n-lint passerar. svlang-träffarna är
förväntade korta UI-etiketter och Blender-fackord. Batchen är lokalt validerad
och arkiveras för import till Blender Translate; något importresultat finns
ännu inte.

Batch 84 granskar UV-lager, metabollar, filmklipp, nodträd och objektdata i
tre separata radintervall. Tre oberoende skrivskyddade delgranskningar har
jämförts mot RNA-kontext och terminologilistan. Den lokalt validerade
deltafilen innehåller 61 säkra UI-strängar, bland annat *UV-looplager*,
*hörnpunktsnormaler*, *proxykatalog*, *geometrinodträd* och
*urvalsuppsättning*. `msgfmt` och l10n-lint passerar. Hunspell-träffarna är
kontrollerade Blender-sammansättningar; svlang-träffarna är förväntade korta
UI-etiketter och Blender-fackord. Batchen är lokalt validerad och arkiveras
för import till Blender Translate; något importresultat finns ännu inte.

Batch 85 granskar objekttransformering, tomobjekt, instanssamlingar,
materialplatser, föräldrarelationer och rotationslägen i tre separata
radintervall. Tre oberoende skrivskyddade delgranskningar har jämförts mot
RNA-kontext och terminologilistan. Den lokalt validerade deltafilen innehåller
66 säkra UI-strängar, bland annat *deltaförflyttning*, *tomobjekt*,
*världsmatris*, *hörnpunktsmålning*, *viktmålning* och *gimbal-låsning*.
`msgfmt` och l10n-lint passerar. Hunspell-träffarna är kontrollerade
Blender-sammansättningar; svlang-träffarna är förväntade korta UI-etiketter
och Blender-fackord. Batchen är lokalt validerad och arkiveras för import till
Blender Translate; något importresultat finns ännu inte.

Batch 135 granskar kurvkontrollpunkter, handtag, mjukkroppar och
åtgärdsdatablock. Deltafilen innehåller 7 granskade UI-strängar. `msgfmt`,
l10n-lint och diffkontroll passerar. Batchen är arkiverad för import till
Blender Translate; något importresultat finns ännu inte.

Batch 136 granskar datablocketiketter för Grease Pencil, hårkurvor, bilder,
mesh, målningskurvor och formnycklar. Deltafilen innehåller 8 granskade
UI-strängar. `msgfmt`, l10n-lint och diffkontroll passerar. Batchen är
arkiverad för import till Blender Translate; något importresultat finns ännu
inte.

Batch 86 granskar 3D-visning, formnycklar och partikelinställningar i tre
separata radintervall. Tre oberoende skrivskyddade delgranskningar har
jämförts mot RNA-kontext och terminologilistan. Den lokalt validerade
deltafilen innehåller 41 säkra UI-strängar, bland annat *instansierare*,
*skulptering med dynamisk topologi*, *simuleringscache*, *barnpartikel* och
*volymspridning*. Två meddelanden med samma engelska källtext men orelaterad
kontext togs uttryckligen bort ur deltafilen. `msgfmt` och l10n-lint passerar.
Hunspell-träffen är den kontrollerade Blender-sammansättningen
*hörnpunktsgrupper*; svlang-träffarna är förväntade korta UI-etiketter och
Blender-fackord. Batchen är lokalt validerad och arkiveras för import till
Blender Translate; något importresultat finns ännu inte.

Batch 87 granskar partikelhår, partikelrendering och närliggande scen- och
ljudegenskaper i tre separata radintervall. Tre oberoende skrivskyddade
delgranskningar har jämförts mot RNA-kontext och terminologilistan. Den lokalt
validerade deltafilen innehåller 37 säkra UI-strängar, bland annat
*materialplats*, *partikelbana*, *guidehår*, *strårendering*,
*delbildruta* och *punktmolnsdatablock*. `msgfmt` och l10n-lint passerar.
Hunspell-träffen är den kontrollerade Blender-sammansättningen
*strårendering*; svlang-träffarna är förväntade korta UI-etiketter och
Blender-fackord. Batchen är lokalt validerad och arkiveras för import till
Blender Translate; något importresultat finns ännu inte.

Batch 88 granskar ljudets avståndsmodeller, scen- och sekvensinställningar
samt textredigerarens status i tre separata radintervall. Tre oberoende
skrivskyddade delgranskningar har jämförts mot RNA-kontext och
terminologilistan. Den lokalt validerade deltafilen innehåller 39 säkra
UI-strängar, bland annat *avståndsmodell*, *delbildruta*,
*sekvensredigerare*, *cachelagring* och *ljuddatablock*. `msgfmt` och
l10n-lint passerar. Hunspell-träffarna är kontrollerade Blender-sammansättningar;
svlang-träffarna är förväntade korta UI-etiketter och Blender-fackord. Batchen
är lokalt validerad och arkiveras för import till Blender Translate; något
importresultat finns ännu inte.

Batch 89 granskar textredigerarens urval och ett avgränsat urval av
procedur- och bildtexturer. Tre oberoende skrivskyddade delgranskningar har
jämförts mot RNA-kontext och terminologilistan. Den lokalt validerade
deltafilen innehåller 13 säkra UI-strängar, bland annat *brusbas*,
*cellbrus*, *schackmönsteravstånd*, *förvrängningsmängd* och *normalkarta*.
`msgfmt` och l10n-lint passerar. Hunspell-träffen är den kontrollerade
sammansättningen *schackmönsteravstånd*; svlang-träffarna är förväntade korta
UI-etiketter och Blender-fackord. Batchen är lokalt validerad och arkiveras
för import till Blender Translate; något importresultat finns ännu inte.

En helkatalogskörning den 5 november med `l10n-lint` gav 1 132 träffar.
Genomgången visar att merparten är förväntade produktnamn, formatnamn,
kodidentifierare, standardskrivning och tekniska sammansättningar. De får inte
massändras. Samma export gav `svlang check` en missvisande katalogpoäng, eftersom
verktyget behandlar varje kort UI-etikett och varje PO-huvudrad som löpande
prosa. Den riktade kontrollen av Batch 11 gav däremot 10,0 av 10 för naturlig
svenska; `msgfmt`, l10n-lint, Hunspell, diffkontroll och Gitleaks passerade.

### Blender Manual

Den 5 november 2026 importerades den samlade filen
`upload-candidates/2026-11-04/blender-manual-sv-reviewed-all.po` till den
generiska Manual-komponenten via Blender Translate. Historiken bekräftar
följande importresultat i läget *Lägg till som översättning*:

- 868 meddelanden bearbetades.
- 856 meddelanden uppdaterades.
- 11 meddelanden hoppades över.
- 1 meddelande hittades inte.

En omedelbar dubblettimport gav 0 uppdateringar, 867 hoppade över och samma
1 saknade meddelande. Det bekräftar att den första importen genomfördes.
Det saknade meddelandet behöver identifieras mot en ny export innan det kan
åtgärdas. Importen innebär inte att hela Manual-komponenten är färdiggranskad
eller uppströmsgranskad.

Batch 90 granskar klassiska procedurtexturer, Voronoi- och volyminställningar,
tilläggshanteringen, Rigify, Grease Pencil och världsinställningar i tre
separata radintervall. Tre primära delgranskningar och två oberoende
slutgranskningar har jämförts mot RNA-kontext och terminologilistan. Den
lokalt validerade deltafilen innehåller 70 säkra UI-strängar, bland annat
*brustextur*, *Voronoi-funktionsvikt*, *3D-vyport*, *bildruteintervall*,
*resursbläddrare* och *Cycles-världsinställningar*. `msgfmt` och l10n-lint
passerar. Hunspell-träffarna är kontrollerade Blender-sammansättningar;
svlang-träffarna är förväntade korta UI-etiketter och Blender-fackord.
Batchen är lokalt validerad och arkiveras för import till Blender Translate;
något importresultat finns ännu inte. Den 5 november stoppade Cloudflare
Blender Translates API-filändpunkt före autentisering med HTTP 403 och en
challenge-sida. Deltafilen är därför inte felaktigt markerad som uppladdad;
den väntar på import via den redan inloggade webbläsaren.

Batch 91 granskar världar, biblioteksåsidosättningar, invers kinematik och
bildformat i tre separata radintervall. Tre primära delgranskningar och en
oberoende slutgranskning har jämförts mot RNA-kontext och terminologilistan.
Den lokalt validerade deltafilen innehåller 60 säkra UI-strängar, bland annat
*biblioteksåsidosättning*, *IK-lösare*, *tillståndsbaserad lösare*,
*bildruteintervall*, *färghantering* och *komprimering med förlust*.
`msgfmt` och l10n-lint passerar. Hunspell-träffarna är kontrollerade
Blender-sammansättningar; svlang-träffarna är förväntade korta UI-etiketter,
kodnamn och Blender-fackord. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 124 granskar Blender API:ts noduttag, nodträdsgränssnitt och
geometrinodernas bakningsinställningar. Tre oberoende delgranskningar har
jämförts med RNA-kontexten. Den lokalt validerade deltafilen innehåller 88
granskade UI-strängar, bland annat *noduttag*, *noduttagsgränssnitt*,
*indata*, *utdata*, *bildruteintervall* och *datablock*. `msgfmt`,
`l10n-lint` och diffkontroll passerar. Hunspell- och svlang-träffarna gäller
avsiktliga Blender-sammansättningar och korta UI-etiketter; inga språkfel
hittades. Batchen är arkiverad för import till Blender Translate; något
importresultat finns ännu inte.

Batch 123 granskar vektormatematik, vågtexturer och nodgränssnitt i tre
separata radintervall. Tre oberoende genomgångar har kontrollerats mot
Blender-nodernas RNA-kontext och den projektspecifika terminologin. Den
lokala deltafilen `blender-ui-sv-reviewed-20261105-123.po` innehåller 28
granskade UI-strängar, bland annat *vektormatematik*, *bandriktning*,
*principiell volym*, *bakningsobjekt*, *nodindata*, *nodutdata* och
*verktygstips*. `msgfmt`, `l10n-lint`, Hunspell, diffkontroll och Gitleaks
passerar. `svlang` ger 10,0/10; de noterade fackorden är avsiktliga
sammansättningar. Filen är lokalt validerad och arkiverad men väntar på
importresultat från Blender Translate.

Batch 122 granskar shaderutdata, texturer, partiklar och himmelsnoder i tre
separata radintervall. Tre oberoende genomgångar har kontrollerats mot
Blenders shader- och texturkontext samt den projektspecifika terminologin.
Den lokala deltafilen `blender-ui-sv-reviewed-20261105-122.po` innehåller 42
granskade UI-strängar, bland annat *AOV-utdata*, *materialutdata*,
*texturkoordinater*, *miljötextur*, *hörnpunktsfärglager*, *markalbedo* och
*funktionsutdata*. `msgfmt`, `l10n-lint`, diffkontroll och Gitleaks passerar.
Filen är lokalt validerad och arkiverad men väntar på importresultat från
Blender Translate.

Batch 121 granskar UV-, grupp-, material- och shadernoder i tre separata
radintervall. Tre oberoende genomgångar har kontrollerats mot nodernas
RNA-kontext, shadertermer och den projektspecifika terminologilistan. Den
lokala deltafilen `blender-ui-sv-reviewed-20261105-121.po` innehåller 38
granskade UI-strängar, bland annat *grupputdata*, *Fresnel-typ*,
*underytsspridningsmetod*, *begränsningstyp*, *objektrymd*,
*spekulär BSDF* och *normalkartläggning i tangentrymd*. `msgfmt`,
`l10n-lint`, diffkontroll och Gitleaks passerar. Hunspell markerar endast
de dokumenterade sammansättningarna *färgparametrisering* och *indatafärger*.
`svlang` ger endast förväntade heuristiska träffar för relativa satser och
nodverb. Filen är lokalt validerad och arkiverad men väntar på importresultat
från Blender Translate.

Batch 120 granskar kurv-, simulerings-, provtagnings- och nodramstexter i tre
separata radintervall. Tre oberoende genomgångar har kontrollerats mot
Blender-nodernas RNA-kontext och projektets terminologilista. Den lokala
deltafilen `blender-ui-sv-reviewed-20261105-120.po` innehåller 56 granskade
UI-strängar, bland annat *provta*, *kurvnormal*, *Grease Pencil-djup*,
*tangentrymd*, *simuleringsindata*, *splineupplösning*, *flyttalsvektor* och
*ytuppsättning*. `msgfmt`, `l10n-lint`, diffkontroll och Gitleaks passerar.
Hunspell markerar enbart de dokumenterade sammansättningarna
*splinelängd*, *indatasträngar* och *splineupplösning*. `svlang` ger en
förväntad heuristisk träff på en kort nominell etikett. Filen är lokalt
validerad och arkiverad men väntar på importresultat från Blender Translate.

Batch 119 granskar geometri-, mesh- och volymnoder i tre separata
radintervall. Tre oberoende genomgångar har kontrollerats mot nodernas
RNA-kontext, Blender-TBX och den befintliga UI-terminologin. Den lokala
deltafilen `blender-ui-sv-reviewed-20261105-119.po` innehåller 96 granskade
UI-strängar, bland annat *avrunda kurva*, *rutnät till mesh*,
*instansgränser*, *hörnpunktsgrannar*, *ythörn*, *volymrutnät* och
*geometrisk närhet*. `msgfmt`, `l10n-lint`, diffkontroll och Gitleaks
passerar. Hunspell markerar enbart de avsiktliga och dokumenterade
sammansättningarna *hörnpunktsgrannar* och *ytgruppsgränser*. `svlang` ger
enbart väntade heuristiska träffar för korta facktermer, imperativ och
nominella noder. Filen är lokalt validerad och arkiverad men väntar på
importresultat från Blender Translate.

Batch 118 granskar geometri- och kurvnoder i tre separata radintervall. Tre
oberoende genomgångar har kontrollerats mot nodernas RNA-kontext, mesh- och
kurvterminologin samt befintlig Blender-TBX. Den lokala deltafilen
`blender-ui-sv-reviewed-20261105-118.po` innehåller 68 granskade UI-strängar,
bland annat *geometrinod*, *funktionsnod*, *ythörn*, *hörnpunkt*,
*flyttal*, *kurvcirkel*, *Fyrhörning*, *Grease Pencil* och *volymrutnät*.
`msgfmt`, `l10n-lint`, Hunspell, diffkontroll och Gitleaks passerar; `svlang`
rapporterar enbart väntade heuristiska träffar för korta nodetiketter,
facktermer och imperativ. Filen är lokalt validerad och arkiverad men väntar
på importresultat från Blender Translate.

Batch 117 granskar tonmappning, filmspårning och funktionsnoder för logik,
heltal och matriser i tre separata radintervall. Tre oberoende genomgångar
har sedan kontrollerats mot UI-sammanhanget och Blender-terminologin. Den
lokala deltafilen `blender-ui-sv-reviewed-20261105-117.po` innehåller 60
granskade UI-strängar, bland annat *tonmappning*, *spårposition*,
*bildruta*, *förskjutning*, *funktionsnod*, *flyttal*, *heltalsmatematik*
och *matrisdeterminant*. `msgfmt`, `l10n-lint`, Hunspell, diffkontroll och
Gitleaks passerar; `svlang` ger endast väntade heuristiska träffar på korta
UI-etiketter, facktermer och satser som inleds med *Sant när*. Filen är
lokalt validerad och arkiverad men väntar på importresultat från Blender
Translate.

Batch 116 granskar matematik-, filutdata- och kompositörsnoder i tre separata
radintervall. Tre oberoende delgranskningar har jämförts mot RNA-kontext och
terminologilistan. Den lokalt validerade deltafilen innehåller 54 säkra
UI-strängar, bland annat *potens*, *arkussinus*, *filutdata*, *filplatser*,
*UV-mappning*, *renderingslager* och *rak alfa*. `msgfmt` och l10n-lint
passerar. Hunspell-träffarna är kontrollerade Blender-, matematik- och
bildbehandlingstermer; svlangs enda V2-varning är en falsk positiv för en
kort egenskapsetikett. Batchen är lokalt validerad och arkiveras för import
till Blender Translate; något importresultat finns ännu inte.

Batch 115 granskar kompositörens mask-, nycklings-, filter- och
linsförvrängningsnoder i tre separata radintervall. Tre oberoende
delgranskningar har jämförts mot RNA-kontext och terminologilistan. Den lokalt
validerade deltafilen innehåller 43 säkra UI-strängar, bland annat
*uttoningsavstånd*, *luminansnyckling*, *friläggningsmatta*, *UV-mappning*,
*brusig* och *utdata med rak alfa*. `msgfmt` och l10n-lint passerar.
Hunspell-träffarna är kontrollerade Blender- och bildbehandlingstermer;
svlangs V2-varningar är falska positiv för tekniska etiketter och
underordnade satser. Batchen är lokalt validerad och arkiveras för import till
Blender Translate; något importresultat finns ännu inte.

Batch 114 granskar kompositörens färgkorrigering, Cryptomatte, brusreducering
och friläggningsnoder i tre separata radintervall. Tre oberoende
delgranskningar har jämförts mot RNA-kontext och terminologilistan. Den lokalt
validerade deltafilen innehåller 49 säkra UI-strängar, bland annat
*färgnyckling*, *avståndsnyckling*, *friläggningsmatta*, *undertryck
färgspill*, *brusreduceringskvalitet* och *Cryptomatte-lager*. `msgfmt` och
l10n-lint passerar. Hunspell-träffarna är kontrollerade Blender- och
bildbehandlingstermer; svlangs V2-varningar är falska positiv för tekniska
etiketter och grammatiska underordnade satser. Batchen är lokalt validerad och
arkiveras för import till Blender Translate; något importresultat finns ännu
inte.

Batch 113 granskar NLA-spår och kompositörsnoder för oskärpa, nyckling och
färgkorrigering i tre separata radintervall. Tre oberoende delgranskningar
har jämförts mot RNA-kontext och terminologilistan. Den lokalt validerade
deltafilen innehåller 53 säkra UI-strängar, bland annat *NLA-remsa*,
*kompositörsnod*, *rektangulär mask*, *matta*, *högdagerförstärkning* och
*mellantonförstärkning*. `msgfmt` och l10n-lint passerar. Hunspell-träffarna
är kontrollerade Blender- och bildbehandlingstermer; svlangs V2-varningar är
falska positiv för UI-etiketter och korrekta underordnade satser. Batchen är
lokalt validerad och arkiveras för import till Blender Translate; något
importresultat finns ännu inte.

Batch 112 granskar filmspårning och NLA-animering i tre separata
radintervall. Tre oberoende delgranskningar har jämförts mot Movie Tracking-
och NLA-RNA-kontext samt terminologilistan. Den lokalt validerade deltafilen
innehåller 68 säkra UI-strängar, bland annat *bildruta* i filmspårning,
*förflyttningsspår*, *rekonstruerad punkt*, *NLA-remsa*, *remstid* och
*nyckelbildruta*. `msgfmt` och l10n-lint passerar. Hunspell-träffarna är
kontrollerade Blender-sammansättningar; svlangs V2-varningar är falska
positiv för korta UI-etiketter och grammatiska underordnade satser. Batchen
är lokalt validerad och arkiveras för import till Blender Translate; något
importresultat finns ännu inte.

Batch 111 granskar modifierar- och filmspårningsetiketter. Den lokalt
validerade deltafilen innehåller 13 säkra UI-strängar, bland annat
*planspår*, *pixelbildförhållande*, *nyckelbildsatt* och
*mönstrets begränsningsruta*. `msgfmt` och l10n-lint passerar. Batchen är
arkiverad för import till Blender Translate; något importresultat finns ännu
inte.

Batch 110 granskar modifieraretiketter för UV-förvrängning,
hörnpunktsgruppsvikter, volym-till-mesh, våg, viktade normaler, svetsning och
trådram. Den lokalt validerade deltafilen innehåller 15 säkra UI-strängar.
`msgfmt` och l10n-lint passerar. Batchen är arkiverad för import till Blender
Translate; något importresultat finns ännu inte.

Batch 109 granskar modifieraretiketter för Particle System, Remesh, Simple
Deform, Soft Body och Solidify. Den lokalt validerade deltafilen innehåller 11
säkra UI-strängar. `msgfmt` och l10n-lint passerar. Batchen är arkiverad för
import till Blender Translate; något importresultat finns ännu inte.

Batch 108 granskar modifieraretiketter för Mirror, Multires, noder,
bakning, Normal Edit, Ocean och partikelinstanser. Den lokalt validerade
deltafilen innehåller 12 säkra UI-strängar. `msgfmt` och l10n-lint passerar.
Batchen är arkiverad för import till Blender Translate; något importresultat
finns ännu inte.

Batch 107 granskar modifieraretiketter för Shrinkwrap, Grease Pencil,
Laplacian Smooth, Lattice, Mask och Mesh to Volume. Den lokalt validerade
deltafilen innehåller 16 säkra UI-strängar. `msgfmt` och l10n-lint passerar.
Batchen är arkiverad för import till Blender Translate; något importresultat
finns ännu inte.

Batch 106 granskar Grease Pencil Multiply, Noise och Offset i tre oberoende
radintervall. Den lokalt validerade deltafilen innehåller 24 säkra
UI-strängar, bland annat *multiplikatormodifierare*, *uttoningscentrum*,
*brusmodifierare*, *nyckelbildruta*, *brusfrö* och
*Grease Pencil-förskjutningsmodifierare*. `msgfmt` och l10n-lint passerar.
Batchen är arkiverad för import till Blender Translate; något importresultat
finns ännu inte.

Batch 105 granskar Grease Pencil Dash, Envelope, Hook och Length i tre
oberoende radintervall. Den lokalt validerade deltafilen innehåller 26 säkra
UI-strängar, bland annat *Grease Pencil-streckmodifierare*,
*Grease Pencil-kuvertmodifierare*, *streckpunkt*, *överordnat objekt*,
*förskjutning* och *tilläggslängd*. `msgfmt` och l10n-lint passerar. Batchen
är arkiverad för import till Blender Translate; något importresultat finns
ännu inte.

Batch 104 granskar Explode, Fluid och Grease Pencil-modifierare i tre
oberoende radintervall. Den lokalt validerade deltafilen innehåller 36 säkra
UI-strängar, bland annat *hörnpunktsgrupp*, *lagerpass*, *materialpass*,
*slumpfrö*, *uttoning* och *Grease Pencil-färgmodifierare*. `msgfmt` och
l10n-lint passerar. Batchen är arkiverad för import till Blender Translate;
något importresultat finns ännu inte.

Batch 103 granskar Data Transfer, Decimate och närliggande modifierar-UI i
tre oberoende radintervall. Den lokalt validerade deltafilen innehåller 59
säkra UI-strängar, bland annat *ythörn*, *hörnpunktsmappning*,
*dataöverföring*, *decimeringsmodifierare*, *kantkollapsning* och
*texturkoordinater*. `msgfmt` och l10n-lint passerar. Batchen är arkiverad för
import till Blender Translate; något importresultat finns ännu inte.

Batch 102 granskar avfasnings-, booleska och korrigerande
utjämningsmodifierare i tre oberoende radintervall. Den lokalt validerade
deltafilen innehåller 38 säkra UI-strängar, bland annat *hörnpunktsgrupp*,
*avfasningsmängd*, *boolesk operation*, *manifold*, *självskärning* och
*korrigerande utjämning*. `msgfmt`, l10n-lint, diffkontroll och Gitleaks
passerar. Batchen är arkiverad för import till Blender Translate; något
importresultat finns ännu inte.

Batch 101 granskar Grease Pencil-, deformerings- och avfasningsmodifierare i
tre separata radintervall. Tre oberoende delgranskningar har jämförts mot
modifierar- och RNA-kontext. Den lokalt validerade deltafilen innehåller 26
säkra UI-strängar, bland annat *geometrinoder*, *Grease Pencil-streck*,
*armaturmodifierare*, *korrigerande utjämning* och *avfasningsmodifierare*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 100 granskar meshdatatyper, UV-redigering, metabollar och modifierare i
tre separata radintervall. Tre oberoende delgranskningar har jämförts mot RNA-
och modifierarkontext. Den lokalt validerade deltafilen innehåller 99 säkra
UI-strängar, bland annat *meshhörnpunkt*, *meshslingtriangel*,
*Freestyle-ytmarkering*, *UV-projektion*, *hörnpunktsvikter* och *körtid*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 99 granskar NLA-, nod-, sekvenserar- och meshgränssnittet i tre
separata radintervall. Tre oberoende delgranskningar har jämförts mot RNA- och
menykontext. Den lokalt validerade deltafilen innehåller 52 säkra UI-strängar,
bland annat *NLA-spår*, *nyckling*, *ID-data*, *UV-markeringsläge*,
*meshslinga* och *särskilda åtgärder*. `msgfmt` och l10n-lint passerar.
Batchen är lokalt validerad och arkiveras för import till Blender Translate;
något importresultat finns ännu inte.

Batch 98 granskar Grease Pencil-material, 3D- och animeringsmenyer samt
kameraspårning i tre separata radintervall. Tre oberoende delgranskningar har
jämförts mot respektive RNA- och meny-kontext. Den lokalt validerade
deltafilen innehåller 43 säkra UI-strängar, bland annat *UV-mappning*,
*resurser*, *planspår*, *hörnpunktsgrupper* och *särskilda åtgärder*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 96 granskar Freestyle-linjestilens alfa-, färg-, geometri- och
tjockleksmodifierare i tre separata radintervall. Tre oberoende
delgranskningar har jämförts mot Freestyle-RNA-kontext och den svenska
terminologilistan. Den lokalt validerade deltafilen innehåller 38 säkra
UI-strängar, bland annat *alfagenomskinlighet*, *streckets ryggrad*,
*Perlin-brus*, *rumsligt brus* och *tjockleksmodifierare för linjestil*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 95 granskar nyckeluppsättningar, lagersamlingar och Freestyle-
linjestilsmodifierare i tre separata radintervall. Tre oberoende
delgranskningar har jämförts mot RNA- och F-kurvkontext. Den lokalt validerade
deltafilen innehåller 23 säkra UI-strängar, bland annat *nyckelbildruta*,
*nyckeluppsättning*, *ID-datablock*, *hörnpunktsgrupp*, *visningslager* och
*linjestilsmodifierare*. `msgfmt` och l10n-lint passerar. Batchen är lokalt
validerad och arkiveras för import till Blender Translate; något importresultat
finns ännu inte.

Batch 94 granskar KeyMap-händelser och närliggande animeringsetiketter i tre
separata radintervall. Tre oberoende delgranskningar har jämförts mot
KeyMap- och F-kurvkontext. Den lokalt validerade deltafilen innehåller 19
säkra UI-strängar, bland annat *tangentmappningshändelse*, *händelsetyp*,
*fjärdegradig lättnad*, *femtegradig lättnad* och *NDOF-anpassning*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 93 granskar tangent- och händelseetiketter för tangentbord, media och
NDOF-enheter i tre separata radintervall. Tre oberoende delgranskningar har
jämförts mot den konkreta KeyMap-kontexten. Den lokalt validerade deltafilen
innehåller 24 säkra UI-strängar, bland annat *vänsterpil*, *Retur*,
*NDOF-anpassning* och korrekta funktions- och medietangentetiketter.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 92 granskar bilddata och Blenders tangent- och musinmatning i tre
separata radintervall. Tre oberoende delgranskningar har jämförts mot
RNA-kontext och terminologilistan. Den lokalt validerade deltafilen innehåller
30 säkra UI-strängar, bland annat *flyttalsbildpixlar*, *bildrutenummer*,
*tangentmappning*, *tangentmappningspost*, *musknapp* och *radmatning*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 97 granskar Freestyle-linjestilar, maskkurvor och Grease Pencil-material
i tre separata radintervall. Tre oberoende delgranskningar har jämförts mot
respektive RNA-kontext och terminologilistan. Den lokalt validerade deltafilen
innehåller 50 säkra UI-strängar, bland annat *linjeuppsättning*,
*maskens splinepunkter*, *planspår*, *avtagande* och *Grease Pencil-färg*.
`msgfmt` och l10n-lint passerar. Batchen är lokalt validerad och arkiveras för
import till Blender Translate; något importresultat finns ännu inte.

Batch 125 granskar objekt-, kameraspårnings-, tilläggs- och nodoperatorer i
tre separata radintervall. Tre oberoende delgranskningar har jämförts mot
Blenders RNA- och operatorcontext. Den lokalt validerade deltafilen innehåller
69 granskade UI-strängar, bland annat *objektbas*, *visningslager*,
*hörnpunktsmoln*, *resursetikett*, *vätskeförinställning* och
*panelväxling*. `msgfmt`, l10n-lint och diffkontroll passerar. Hunspell- och
svlang-träffarna gäller avsiktliga Blender-sammansättningar, formatnamn och
korta UI-etiketter; inga språkfel hittades. Batchen är arkiverad för import
till Blender Translate; något importresultat finns ännu inte.

Batch 126 granskar nod-, objekt-, tangentmappnings-, renderings- och
fysikoperatorer i tre separata radintervall. Tre oberoende delgranskningar har
jämförts mot Blender API- och UI-kontexten. Den lokalt validerade deltafilen
innehåller 79 granskade UI-strängar, bland annat *geometrinodgrupp*,
*tangentmappningspost*, *styv kropp*, *bildruteintervall* och
*Grease Pencil-penselförinställning*. `msgfmt`, l10n-lint och diffkontroll
passerar. Hunspell- och svlang-träffarna gäller avsiktliga Blender-
sammansättningar och korta UI-etiketter; inga språkfel hittades. Batchen är
arkiverad för import till Blender Translate; något importresultat finns ännu
inte.

Batch 127 granskar sekvenserare, UV-redigering, i18n-verktyg, kontextoperatorer
och F-kurvredigering i tre separata radintervall. Tre oberoende
delgranskningar har jämförts mot Blender UI- och operatorcontext. Den lokalt
validerade deltafilen innehåller 97 granskade UI-strängar, bland annat
*uttoning*, *tangentmappningskonfiguration*, *F-kurva*, *nyckelbildruta* och
*geometrinodgrupp*. `msgfmt`, l10n-lint och diffkontroll passerar. Hunspell-
och svlang-träffarna gäller avsiktliga Blender-sammansättningar, tekniska
formatnamn och korta UI-etiketter; inga språkfel hittades. Batchen är
arkiverad för import till Blender Translate; något importresultat finns ännu
inte.

Batch 128 granskar F-kurvors nyckelbildrutor, inklistring, urval och
fästning i tre separata radintervall. Tre oberoende delgranskningar har
jämförts mot Graph Editor- och NLA-kontexten. Den lokalt validerade deltafilen
innehåller 51 granskade UI-strängar, bland annat *nyckelbildrutatyp*,
*NLA-stapel*, *lassomarkering*, *förhandsgranskningsintervall* och
*fäst nyckelbildrutor*. `msgfmt`, l10n-lint och diffkontroll passerar.
Hunspell- och svlang-träffarna gäller avsiktliga Blender-sammansättningar och
korta UI-etiketter; inga språkfel hittades. Batchen är arkiverad för import
till Blender Translate; något importresultat finns ännu inte.

Batch 129 granskar animationens nyckelbildrutor, nyckeluppsättningar,
åtgärdsplatser, drivare, förhandsgranskningsintervall, grafredigeraren och
bensamlingar i tre separata radintervall. Tre oberoende delgranskningar har
jämförts mot Blender UI- och operatorcontext. Den lokalt validerade deltafilen
innehåller 94 granskade UI-strängar, bland annat *nyckeluppsättning*, *plats*,
*drivare*, *grafredigeraren* och *bensamling*. `msgfmt`, l10n-lint och
diffkontroll passerar. Hunspell- och svlang-träffarna gäller avsiktliga
Blender-sammansättningar och korta UI-etiketter; inga språkfel hittades.
Batchen är arkiverad för import till Blender Translate; något importresultat
finns ännu inte.

Batch 130 granskar Actions API, åtgärdsplatser, Cycles-kärnor, MetalRT,
glTF-inställningar, Node Wrangler och Blender i18n-inställningar i tre
separata radintervall. Tre oberoende delgranskningar har jämförts mot
Blender API- och UI-kontexten. Den lokalt validerade deltafilen innehåller
69 granskade UI-strängar, bland annat *åtgärdsplats*,
*animationskanalbehållare*, *kärnoptimering*, *skärningsberäkning* och
*stavningscache*. `msgfmt`, l10n-lint och diffkontroll passerar. Hunspell-
och svlang-träffarna gäller avsiktliga Blender-sammansättningar, API-namn och
korta UI-etiketter; inga språkfel hittades. Batchen är arkiverad för import
till Blender Translate; något importresultat finns ännu inte.

Batch 131 granskar NLA-blandning, åtgärdsplatser, drivare, rörelsebanor och
redigerarnas gränssnittstexter i tre separata radintervall. Tre oberoende
delgranskningar har jämförts mot Blender API- och UI-kontexten. Den lokalt
validerade deltafilen innehåller 48 granskade UI-strängar, bland annat
*blandning av åtgärd*, *NLA-spår*, *rörelsebana*, *Dopeblad* och
*videosekvensredigerare*. `msgfmt`, l10n-lint och diffkontroll passerar.
Hunspell- och svlang-träffarna gäller avsiktliga Blender-sammansättningar och
korta UI-etiketter; inga språkfel hittades. Batchen är arkiverad för import
till Blender Translate; något importresultat finns ännu inte.

Batch 132 granskar tillgångskataloger, tillgångshylla och svaga
tillgångsreferenser. Den lokalt validerade deltafilen innehåller 12 granskade
UI-strängar. `msgfmt`, l10n-lint och diffkontroll passerar. Batchen är
arkiverad för import till Blender Translate; något importresultat finns ännu
inte.

Batch 133 granskar geometriattribut och Cycles-bakning. Deltafilen innehåller
20 granskade UI-strängar. `msgfmt`, l10n-lint och diffkontroll passerar.
Batchen är arkiverad för import till Blender Translate; något importresultat
finns ännu inte.

Batch 134 granskar Cycles-bakning, bursextrudering, normalrymder, bilddata och
renderingspass. Deltafilen innehåller 17 granskade UI-strängar. `msgfmt`,
l10n-lint och diffkontroll passerar. Batchen är arkiverad för import till
Blender Translate; något importresultat finns ännu inte.

Batch 137 granskar hela API-avsnittet för blendfilimport: importkontext,
blendfilbibliotek, länkning, tillägg, datablock och
biblioteksåsidosättningar. Tre oberoende granskningar har jämförts mot
Blenders RNA-kontext och den projektspecifika termlistan. Deltafilen innehåller
34 granskade UI-strängar, bland annat *blendfilimportkontext*,
*tilläggsåtgärd*, *källbibliotek* och *biblioteksåsidosättning*. En felaktigt
inklistring av en orelaterad Tux Paint-text i strängen *Source Libraries* har
ersatts med rätt svensk UI-term. `msgfmt` och diffkontroll passerar; återstående
språkverktyg körs före arkivering. Batchen är lokalt granskad och väntar på
import i Blender Translate; något importresultat finns ännu inte.

Batch 138 slutför samma avsnitt i den lokala arbetskatalogen: samtliga 52
radgranskade importkontextposter är nu markerade som översatta. Batchen
normaliserar även blendfilsökvägar, tomma objekt och neutrumformen för ID:n.
`msgfmt`, l10n-lint och diffkontroll passerar. Deltafilen är arkiverad för
Blender Translate; något importresultat finns ännu inte.

Batcherna 139 och 140 granskar Boids flockningsfysik och Blender-RNA. De två
deltafilerna innehåller 90 respektive 17 strängar och håller därmed
uppladdningar under gränsen på 100 strängar. Granskningen rättar bland annat
felimporterna *Sändningstid* för *In Air* och en orelaterad musiktext för
*Fight*, samt normaliserar *boidregel*, *krängning*, flyghöjd och
markfästkraft. `msgfmt`, l10n-lint och diffkontroll passerar. Batcherna är
arkiverade för import i Blender Translate; något importresultat finns ännu
inte.

Batch 141 granskar 27 B-Bone- och armatursträngar: handtagsförskjutningar,
utjämning, kurvrullning och hörnpunktsmappning. `msgfmt`, l10n-lint och
diffkontroll passerar. Deltafilen är arkiverad för import i Blender Translate;
något importresultat finns ännu inte.

Batch 142 granskar 38 ytterligare ben- och armatursträngar: ärvd skalning,
skjuvning, riggskelettrelativa matriser och positioner, trådram, kuvertdeformering,
benhierarki samt B-Bone-rullning. Tre oberoende granskningar har jämförts mot
Blenders egen termlista. Alla kontrollerade strängar är markerade som
översatta i den lokala arbetskatalogen; uppladdningsfilen har inga
`fuzzy`-markeringar. `msgfmt`, l10n-lint och diffkontroll passerar. `svlang`
och Hunspell rapporterar endast avsiktliga facktermer som *riggskelett*,
*hörnpunktsgrupp* och *skalutjämning*. Batchen är arkiverad för import i
Blender Translate; något importresultat finns ännu inte.

Batch 143 granskar 27 strängar för bensamlingar: biblioteksåsidosättningar,
synlighet, sololäge, urvalsuppsättningar, paneltexter och armaturens aktiva
bensamling. Tre oberoende granskningar har jämförts mot projektets termlista.
De berörda posterna är lokalt markerade som översatta och deltafilen saknar
`fuzzy`-markeringar. `msgfmt`, l10n-lint och diffkontroll passerar. Batchen
är arkiverad för import i Blender Translate; något importresultat finns ännu
inte.

Batch 144 granskar 10 strängar för Curves Sculpt och Grease Pencil. Den
normaliserar bland annat *kurvskulpteringspensel*, *täthetsläge*,
*täthetspensel*, *Grease Pencil-pensel* och enhetlig skalning. Tre oberoende
granskningar har använts. De berörda posterna är lokalt markerade som
översatta och deltafilen saknar `fuzzy`-markeringar. `msgfmt`, l10n-lint och
diffkontroll passerar. Batchen är arkiverad för import i Blender Translate;
något importresultat finns ännu inte.

Batch 145 ersätter två Batch 144-poster så att de följer termlistans
*Skala jämnt*. Batch 146 granskar Grease Pencil-egenskapen *Aktiv utjämning*.
Båda deltafilerna är syntax- och språkgranskade, hemlighetsskannade och
arkiverade för import i Blender Translate; något importresultat finns ännu
inte.

### Bekräftad import: samlad batch 142--147

Den 6 november 2026 importerades den samlade filen
`blender-ui-sv-reviewed-20261106-batches-142-147.po` i **Blender UI / UI /
svenska**. Blender Translate rapporterade **77 bearbetade** strängar: **54
uppdaterade**, **19 hoppade över** och **4 saknade**. De 19 hoppade över var
redan identiska på servern. De fyra saknade källsträngarna finns inte längre i
den aktuella serverkatalogen och räknas därför inte som importerade ändringar.
Importen bekräftar 54 upstreamuppdateringar; arbetskopians 77 granskade poster
är fortfarande arkiverade för spårbarhet.

Batch 148 granskar tolv UI-strängar för Grease Pencil, bilddata och
samlingar. Den normaliserar bland annat *streck*, *lager*, *pensel*,
*utjämningsgrad*, *bildanvändare*, *bildruta* och
*biblioteksåsidosättning*. Ändringarna är radvis jämförda med RNA-kontexten
och Blender-terminologin. Deltafilen
`blender-ui-sv-reviewed-20261106-148.po` innehåller enbart de tolv
granskade posterna utan `fuzzy`-markeringar. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerar; svlang- och Hunspell-träffar i hela
arbetskatalogen gäller sedan tidigare facktermer och orelaterade poster.

Batch 149 granskar 18 animations- och armatursträngar, med två oberoende
terminologigranskningar. Den rättar bland annat *åtgärdsremsa*,
*nyckelbildruteanimeringsremsa*, *NLA-justeringsläge*, *rörelsebana*,
*armaturens redigeringsben*, *bensamling* och *kuvertdeformering*. Den
felinsatta texten i etiketten *Heads* ersätts med `Huvuden`. Deltafilen
`blender-ui-sv-reviewed-20261106-149.po` innehåller endast de 18 granskade
poster som saknar `fuzzy`-markeringar. `msgfmt`, l10n-lint, diffkontroll och
Gitleaks passerar.

Batch 150 granskar elva sammanhängande poster för Blenders animationssystem:
Action Slots, remsor, F-kurvor och NLA-stapeln. Termlistans motstridiga äldre
poster har rensats; den aktuella, detaljerade definitionen fastslår
`action slot` som *åtgärdsslot*. Batchen rättar bland annat felimporterna
*Action-spelautomater*, *Samling av paletter* och *handlingsluckan*.
Deltafilen `blender-ui-sv-reviewed-20261106-150.po` saknar `fuzzy`-markeringar
och passerar `msgfmt`, l10n-lint, diffkontroll och Gitleaks.

Batch 151 granskar 20 tydliga ClothSettings-poster med en separat
fysikterminologisk peer review. Den normaliserar *mesh*, *hörnpunkt*,
*hörnpunktsgrupp* och *dragstyvhet*, utan att översätta Blenders begrepp
*mesh* till nät. Deltafilen `blender-ui-sv-reviewed-20261106-151.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks.

Batch 152 granskar tolv B-Bone- och benhierarkiposter med två oberoende
terminologigranskningar. Den följer projektets former *B-Bone-segment*,
*Skala in*, *underordnat ben*, *kuvertdeformering* och
*kuvertdeformeringsvikt*, samt gör X- och Z-ledsetiketterna begripliga i UI:t.
Deltafilen `blender-ui-sv-reviewed-20261106-152.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks.

Batch 153 tillämpar den fastställda termen *åtgärdsslot* konsekvent på sju
närliggande etiketter och beskrivningar för AnimData och Action. Den
normaliserar också pluralformen *rörelsebanor* i inställningar för visning.
Deltafilen `blender-ui-sv-reviewed-20261106-153.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks.

Batch 154 granskar tio strängar för cachefiler och kameras bilddata. Den
rättar bland annat filbläddrarens *sökväg*, *filmklippsanvändare*,
*inpassningsmetod*, bländarens *lameller* och den delade kanal-/kameratermen
*stereo*. Deltafilen `blender-ui-sv-reviewed-20261106-154.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks.

Batch 155 granskar åtta kurv- och kurvkartläggningssträngar genom en separat
peer review. Den ersätter felaktiga *bana* och *kurvmappning* med projektets
termer *kurva* och *kurvkartläggning*, och normaliserar bland annat
*kurvdatablock*, *kurvförskjutningar* och *klumpavsmalning*. Deltafilen
`blender-ui-sv-reviewed-20261106-155.po` saknar `fuzzy`-markeringar och
passerar `msgfmt`, l10n-lint, diffkontroll och Gitleaks.

För manuell import finns dessutom den samlade deltafilen
`blender-ui-sv-reviewed-20261106-batches-148-155.po`. Den innehåller **86**
unika, granskade strängar från batch 148--155 och ligger under Weblates
100-strängarsgräns. Den har inga `fuzzy`-markeringar och passerar `msgfmt`,
l10n-lint, diffkontroll och Gitleaks. Något importresultat för denna samlade
fil är ännu inte verifierat.

Batch 156 granskar två attributetiketter för geometri med oberoende
fackgranskning. Den rättar särskrivningarna *8-bitars värde* och *Geometri
färgattribut* till `8-bitarsvärde i geometriattribut` respektive
`Geometrifärgattribut`. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-156-geometry-attributes.po` innehåller
endast dessa två poster utan `fuzzy`-markeringar och passerar `msgfmt`,
l10n-lint och diffkontroll. Den är arkiverad men ännu inte verifierat
importerad till Blender Translate.

Batch 157 granskar elva sammanhängande poster för animationskanaler och
Alembic-cache med två separata peer reviews. Den tillämpar konsekvent
*åtgärdsslot*, *nyckelbildruta*, *rörelsebana*, *bildruteintervall* och
*cachelager*, samt rättar CacheFiles tekniska sökvägs- och
bildruteformuleringar. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-157-animation-cache.po` innehåller
endast de granskade posterna utan `fuzzy`-markeringar och passerar `msgfmt`,
l10n-lint och diffkontroll. Den är arkiverad men ännu inte verifierat
importerad till Blender Translate.

Batch 158 granskar åtta RNA-poster för geometriattribut och meshdatatyper med
en oberoende peer review. Den normaliserar bland annat `Bytefärg`,
`Float2-attribut`, `4x4-matrisattribut`, 2D-vektorattribut samt Blenders
etablerade term *mesh* i samlingstyper. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-158-geometry-datatypes.po` innehåller
endast de granskade posterna utan `fuzzy`-markeringar och passerar `msgfmt`,
l10n-lint och diffkontroll. Den är arkiverad men ännu inte verifierat
importerad till Blender Translate.

Batch 159 granskar 18 poster för Action-systemet, bakning och begränsningar
med tre kontextspecifika genomgångar. Den normaliserar *åtgärdsslot*,
*nyckelbildruta*, *passfilter*, *ägarutrymme*, *linjestil* och flera
transformations- och bakningsbeskrivningar. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-159-animation-render-constraints.po`
innehåller endast de granskade posterna utan `fuzzy`-markeringar och passerar
`msgfmt`, l10n-lint och diffkontroll. Den är arkiverad men ännu inte
verifierat importerad till Blender Translate.

För manuell import finns dessutom den samlade deltafilen
`blender-ui-sv-reviewed-20261106-batches-156-159.po`. Den innehåller **39**
unika, granskade strängar från batch 156--159 och ligger under Weblates
100-strängarsgräns. Den har inga `fuzzy`-markeringar och passerar `msgfmt`,
l10n-lint och diffkontroll. Blender Translate bekräftade importen med **39
bearbetade, 29 uppdaterade, 9 hoppade över och 1 saknad** post. Den saknade
posten var `Action F-Curves`; den finns inte längre i serverns aktuella
källkatalog och ska inte skickas på nytt utan en ny export. Efter importen
visar Blender Translate **100 %** för UI-katalogen.

## Importgräns

Blender Translate accepterar granskade importbatchar om högst **1 000
strängar**. Större filer ska delas upp före uppladdning eftersom importen kan
hänga.

För manuell import finns även den samlade deltafilen
`blender-ui-sv-reviewed-20261106-batches-160-174.po`. Den innehåller **121**
unika, lokalt granskade poster från batch 160--174 och ligger långt under
Blender Translates gräns på 1 000 strängar. Den ersätter inte de enskilda
batchfilerna i arkivet, men gör det möjligt att importera den sammanhängande
granskningen i en enda uppladdning. Den är ännu inte verifierat importerad.

Batch 160 granskar fjorton noder, geometrioperationer och exportetiketter med
tre parallella kontextgenomgångar. Den normaliserar bland annat
`4x4-matris`, vektorer med signerade 16- och 32-bitarsheltal, *sinus*,
*utjämning*, Blenders pluralform *mesh* och uppåtriktade koordinataxlar.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-160-nodes-geometry.po`
innehåller endast de granskade posterna utan `fuzzy`-markeringar och passerar
`msgfmt`, l10n-lint och diffkontroll. Den är arkiverad men ännu inte
verifierat importerad till Blender Translate.

Batch 161 fortsätter normaliseringen av Action-systemets synliga etiketter och
beskrivningar. Den ersätter den utfasade termen *åtgärdsplats* med
*åtgärdsslot* i tre närliggande F-kurvposter. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-161-action-slots.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint och diffkontroll. Den är
arkiverad men ännu inte verifierat importerad till Blender Translate.

Batch 162 granskar fyra filbläddrar- och resurskatalogsetiketter. Den
normaliserar *filvalsparametrar*, *filvalspost* och *datablock* samt tar bort
ett felaktigt kolon från etiketten *Tillgångskatalog*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-162-file-browser.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint och diffkontroll. Den är
arkiverad men ännu inte verifierat importerad till Blender Translate.

Batch 163 rättar Principled BSDF-parametern `Transmission`: den felaktiga
fordonstermen *Växellåda* ersätts med den etablerade shadertermen
*Transmission*, som här avser ljusgenomsläpp. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-163-shader-transmission.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint och diffkontroll. Den är
arkiverad men ännu inte verifierat importerad till Blender Translate.

Batch 164 granskar fyra Asset Browser-poster. Den återställer betydelsen av
*user asset library* som `användarresursbibliotek` och normaliserar
*resursbibliotek* i relaterade etiketter. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-164-asset-libraries.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint och diffkontroll. Den är
arkiverad men ännu inte verifierat importerad till Blender Translate.

Batch 165 granskar fjorton poster i Action-systemets API-hjälp och
operatorstexter. Den rättar bland annat de semantiskt felaktiga formerna
*åtgärdsplats*, *handlingslucka*, *spår* och *spelautomat* till den
projektspecifika termen *åtgärdsslot*. Python-identifierare som
`action.slots.active`, `animated_id`, `constraint` och `nla_strip` lämnas
oförändrade. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-165-action-slots.po` innehåller 14
poster, saknar `fuzzy`-markeringar och passerar `msgfmt`, l10n-lint,
diffkontroll och Gitleaks. `svlang` rapporterar endast falska positiva för
API-identifierare, understrecksmarkering och den tekniska termen
*åtgärdsslot*. Filen är arkiverad och väntar på manuell import till Blender
Translate.

Batch 166 granskar tio strängar i renderings- och bildhanteringsgränssnittet.
Den rättar sammansättningar som `bilddatablock` och `renderingsmotor`, använder
*renderingslager* konsekvent samt ersätter otydliga former som
`visningsportalen` och `animationsområdet` med kontextbundna svenska
formuleringar. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-166-rendering-ui.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, Hunspell för de tio
måltexterna, diffkontroll och Gitleaks. `svlang` rapporterar bara falska
positiva för tekniska sammansättningar och den grammatiskt korrekta bisatsen
`som ska packas upp`. Filen är arkiverad och väntar på manuell import till
Blender Translate.

Batch 167 granskar fem filbläddrar- och datablocksetiketter. Den normaliserar
*kameradatablock*, *Freestyle-linjestilsdatablock*, *texturplats för
partikelinställningar* och *tillgångskataloger* enligt den befintliga
Blender-terminologin. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-167-file-types.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks. Hunspell och `svlang` markerar endast de projektspecifika
sammansättningarna *kameradatablock* och *linjestilsdatablock*. Filen är
arkiverad och väntar på manuell import till Blender Translate.

Batch 168 granskar tretton sammanhängande RNA-etiketter för Blenders
datablockstyper samt en Action Slot-hjälptext. Den normaliserar bland annat
*armaturdatablock*, *cachefildatablock*, *gitterdatablock*,
*ljussonddatablock* och *linjestilsdatablock*, och rättar den sista förekomsten
av *åtgärdsplats* i den aktuella Action Slot-kontexten. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-168-datablock-labels.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks.
Hunspell och `svlang` markerar enbart avsedda, projektspecifika sammansättningar
och korrekta underordnade satser. Filen är arkiverad och väntar på manuell
import.

Batch 169 granskar fjorton NLA- och bakningsposter, inklusive två förekomster
av *Sync Action Length*. Den rättar felaktiga ordagranna eller ogrammatiska
former till bland annat `Synkronisera åtgärdslängd`, `Baka benens
transformationer`, `Slutbildruta för bakning` och `Visuell
nyckelbildsättning`. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-169-nla-baking.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, Hunspell för måltexterna,
diffkontroll och Gitleaks. `svlang` markerar bara den projektbundna
sammansättningen *nyckelbildsättning* och två grammatiska underordnade satser.
Filen är arkiverad och väntar på manuell import.

Batch 170 granskar tolv renderings-, shader- och filbläddrartexter. Den
rättar bland annat *Lambertisk emissionsshader*, *studioljus*,
*renderingsläget Solitt*, *samling av remsor* och de fyra felaktigt engelska
Bläddra-etiketterna för mesh-, kurv-, metaboll- och linjestilsdata.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-170-rendering-browse.po`
saknar `fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, riktad Hunspell,
diffkontroll och Gitleaks. `svlang` markerar enbart tekniska
sammansättningar och korrekta underordnade satser. Filen är arkiverad och
väntar på manuell import.

Batch 171 granskar sex Metaball-poster i datablocks-, filbläddrar- och
animeringssammanhang. Den normaliserar den etablerade Blender-formen
*metaboll* i sammansättningar som `metabolldatablock` och
`metabollredigering`, och förtydligar den tekniska ytbeschrivningen som
`sammanflytande ytor`. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-171-metaballs.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, riktad Hunspell,
diffkontroll och Gitleaks. `svlang` markerar endast tekniska sammansättningar
och korrekta infinitivfraser. Filen är arkiverad och väntar på manuell import.

Batch 172 granskar den längre tooltippen för Eevees spekulära shader. Den
ersätter blandade engelska fackord med den kontextbundna formuleringen
*Principiell BSDF*, *spekulärt arbetsflöde* och *metalliskt arbetsflöde*, och
bevarar den fysiskt korrekta förklaringen om reflektionsfärg och energi.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-172-specular-shader.po`
saknar `fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, riktad Hunspell,
diffkontroll och Gitleaks. `svlang` godkänner textens naturlighet och markerar
endast den avsedda akronymen *BSDF*. Filen är arkiverad och väntar på manuell
import.

Batch 173 granskar sjutton sammanhängande RNA-etiketter för BlendDatas
datablockstyper. Den ersätter konsekvent särskrivna former med svenska
sammansättningar, exempelvis `filmklippsdatablock`, `nodgruppsdatablock`,
`punktmolnsdatablock`, `fönsterhanterardatablock` och `världsdatablock`.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-173-datablock-types.po`
saknar `fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, riktad Hunspell,
diffkontroll och Gitleaks. `svlang` ger 10/10 i naturlighet och markerar bara
de avsedda, projektspecifika sammansättningarna. Filen är arkiverad och väntar
på manuell import.

Batch 174 granskar åtta API-hjälprader och etiketter i Action-systemet. Den
normaliserar *Action* till *åtgärd* i svensk löptext, ersätter den felaktiga
formen *åtgärdsplats*, använder `Alla åtgärdsnyckelbildrutor` och förtydligar
Action Constraint- och Slot Handle-kontexten utan att ändra verkliga
API-typen `ActionKeyframeStrip` eller `ActionChannelbag`. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-174-action-api.po` saknar
`fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, diffkontroll och
Gitleaks. `svlang` ger 10/10 i naturlighet; rapporterade ovanliga ord är
projektets API-namn och avsedda facktermer. Filen är arkiverad och väntar på
manuell import.
Batch 175 granskar fyra Movie Tracking-/Dopeblad-poster. Den ersätter
blandade engelska och felaktiga direktöversättningar med *filmspårningsdopeblad*,
*dopebladsvyn* och en kontexttrogen förklaring av data för rörelsespårning.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-175-movie-tracking.po`
saknar `fuzzy`-markeringar och passerar `msgfmt`, l10n-lint, riktad Hunspell,
diffkontroll och Gitleaks. `svlang` ger 10/10 i naturlighet och rapporterar
bara den avsedda Blender-termen *dopeblad*. Filen är arkiverad och väntar på
manuell import.

Batch 176 granskar tolv sammanhängande poster för dopebladet. Den rättar en
felaktig hänvisning till *exponeringsblad*, engelska UI-rester och flera
inkonsekventa former för datablock, action-slotar och ungefärlig filtrering.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-176-dopesheet-ui.po`
passerar `msgfmt`, l10n-lint, diffkontroll och Gitleaks. `svlang` bedömer
texten som naturlig; de enda sällsynta orden är avsedda Blender-termer och
identifieraren `ID_SCE`. Filen är arkiverad och väntar på manuell import.

Batch 177 granskar nitton poster för nodredigeraren. Den ersätter blandad
engelska och felaktiga ordgrupper med konsekventa Blender-termer som
*nodredigerare*, *nodträd*, *geometrinoder*, *shaderredigerare* och
*texturnodredigerare*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-177-node-editor.po` passerar `msgfmt`,
l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang` rapporterar
bara avsedda och sällsynta Blender-sammansättningar. Filen är arkiverad och
väntar på manuell import.

Batch 178 granskar sjutton poster för tyg- och mjukkroppssimulering samt
MetalRT. Den normaliserar självkollisioner, vinkelfjädrar, målpositionernas
inställningar och skärningsfrågor. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-178-physics-simulation.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. l10n-lints
tre informationsrader för parentesernas olika position är förväntade och
semantiskt korrekta. `svlang` ger 10/10 och rapporterar bara avsedda
Blender-termer. Filen är arkiverad och väntar på manuell import.

Batch 179 granskar sexton poster för dopebladsredigeraren. Den normaliserar
redigerarens namn, cache- och bakningsdata, mjuka kroppar, formnycklar,
posemarkörer och nyckelbildrutor. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-179-dope-sheet-editor.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang` ger
10/10 och rapporterar bara avsedda Blender-sammansättningar. Filen är
arkiverad och väntar på manuell import.

Batch 180 granskar tjugoen poster för klippredigeraren och filmspårningen.
Den rättar bland annat kanaler, spårfel, begränsningsrutor, tidskod,
stabiliserat filmmaterial och dopebladsvyn. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-180-movie-clip-editor.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar bara avsedda Blender-sammansättningar och en falsk V2-träff för
en imperativ UI-etikett. Filen är arkiverad och väntar på manuell import.

Den samlade importfilen `blender-ui-sv-reviewed-20261106-batches-175-180.po`
innehåller 98 granskade ändringar från batch 175–180 och bygger på den
bekräftat importerade basen efter batch 160–174. Den saknar `fuzzy`-poster och
rymmer väl inom Blender Translates gräns på 1 000 strängar. Blender Translate
bekräftade den 2026-11-06: **98 bearbetade, 64 uppdaterade, 33 hoppade över
och 1 saknad**. Den saknade källsträngen var `Node Tool Tree`; den har ändrats
eller försvunnit uppströms och räknas inte som importerad. Filen har
kontrollerats med `msgfmt`, l10n-lint, diffkontroll och Gitleaks.
De enskilda deltafilerna för batch 175–180 finns kvar för spårbarhet men ska
inte laddas upp på nytt, eftersom samlingsfilen representerade dem i importen.

Batch 181 granskar nio poster för den inbyggda Python-konsolen. Den ersätter
felöversatta interna områdesnamn och normaliserar teckenstorlek,
kommandoradsprompt och kommandoutgång. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-181-python-console.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang` ger
10/10. Filen är arkiverad och väntar på manuell import.

Batch 182 granskar fjorton poster för bild- och UV-redigeraren. Den rättar
felöversatta områdesnamn, överlägg, rotations-/skalningsvridpunkt,
maskredigeraren, stereoskopiskt 3D-läge och bildfästning. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-182-image-editor.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang` ger
10/10. Filen är arkiverad och väntar på manuell import.

Batch 183 granskar nitton poster för informations- och NLA-redigeraren. Den
normaliserar områdesnamn, felsökningsrapporter, åtgärdslokala markörer samt
kontroll- och påverkans-F-kurvor. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-183-info-nla-editors.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar bara akronymen NLA och en falsk V2-träff för en imperativ
UI-etikett. Filen är arkiverad och väntar på manuell import.

Batch 184 granskar tolv poster för Outliners filter och markeringar. Den
normaliserar datablock, underordnade objekt, tomobjekt, Grease Pencil-objekt,
mesh, visningslager och markeringar i Outliner. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-184-outliner-filters.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang` ger
bara väntade träffar när fristående UI-etiketter läses som löptext:
Blender-termer och en falsk V2-varning. Filen är arkiverad och väntar på
manuell import.

Batch 185 granskar tretton poster för actionsystemets animationskanaler,
åtgärdsslotar och F-kurvor. Den normaliserar särskilt den gemensamma
UI-termen *slot*, lägesangivelsen för F-kurvor och animeringskanalernas
beskrivningar. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-185-action-channel-slots.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar väntat en konstgjord lång mening och en falsk V2-varning när
fristående UI-etiketter analyseras som löptext. Filen är arkiverad och väntar
på manuell import.

Batch 186 granskar sjutton poster för åtgärdsgrupper, åtgärdslager och
posemarkörer. De befintliga svenska texterna är sakligt och terminologiskt
korrekta; deras `fuzzy`-markeringar har därför tagits bort efter radvis
kontroll. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-186-action-groups-layers.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar bara en konstgjord lång mening när de fristående etiketterna
sammanfogas inför analys. Filen är arkiverad och väntar på manuell import.

Batch 187 granskar tolv poster för åtgärdsslotens egenskaper. Den normaliserar
markerings- och utfällningsstatus, mål-ID-typ och datablockstyp samt granskar
API-namnen `ActionKeyframeStrip` och `ActionChannelbag` i sin riktiga
API-kontext. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-187-action-slot-properties.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang` ger
10/10 och rapporterar endast den avsedda Blender-termen *åtgärdsslot*. Filen
är arkiverad och väntar på manuell import.

Batch 188 granskar femton poster för åtgärdsslotars ID-typer och
åtgärdsremsor. Den rättar *Key* till *Formnyckel*, *Paint Curve* till
*Målningskurva* och den synliga *Keyframe*-etiketten till *Nyckelbildruta*.
Den kompletterar även terminologilistan med *paint curve → målningskurva*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-188-action-types-strips.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar bara förväntade Blender-sammansättningar. Filen är
arkiverad och väntar på manuell import.

Batch 189 granskar femton poster i Node Wrangler. Den ersätter engelska
*Mix*-rester med *blandningsnod*, använder *shadernoder* i rätt nodkontext
och normaliserar uppmaningar till *Fäll ut*. Terminologilistan kompletteras
med *hotkey → snabbtangent* och *naming tag → namntagg*. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-189-node-wrangler.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar väntade Blender-termer och en falsk V2-varning när korta
UI-etiketter sammanfogas till löptext. Filen är arkiverad och väntar på
manuell import.

Batch 190 granskar elva utvecklarinställningar för Blenders
översättningsverktyg. Den bevarar filändelser, bibliotek och kodtermer,
men använder *Git-förrådet* i svensk löptext. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-190-i18n-settings.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar bara väntade produkt- och kodnamn samt en falsk V2-varning från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 191 granskar åtta poster för den aktiva åtgärden och blandning med
NLA-stapeln. Den bekräftar den projektspecifika terminologin *åtgärd*,
*blandning av åtgärd*, *NLA-stapel* och *kvaternionmatematik*. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-191-animation-blending.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar bara en falsk V2-varning när korta UI-etiketter sammanfogas till
löptext. Filen är arkiverad och väntar på manuell import.

Batch 192 granskar tjugoåtta poster för animationsdata, NLA-extrapolering,
åtgärdsslotar, drivrutiner och NLA-justeringsläge. Den rättar
*animeringsdatablock* till den etablerade sammansättningen
*animationsdatablock*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-192-animation-data-nla.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar väntade Blender-termer samt längd- och V2-varningar som uppstår
när oberoende UI-etiketter fogas ihop till löptext. Filen är arkiverad och
väntar på manuell import.

Batch 193 granskar trettiofyra poster för rörelsebanor. Den rättar särskilt
felaktiga benändar, *Baka position*, *Startram*, *Slutbild* och den
felöversatta *avskalning av lök*. Terminologilistan kompletteras med
*beräkningsposition*, *benhuvud* och *benspets*. Samtliga granskade poster
har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-193-motion-paths.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar väntade sammansättningar samt konstgjorda längd- och
V2-varningar när UI-etiketter fogas ihop till löptext. Filen är arkiverad och
väntar på manuell import.

Batch 194 granskar fem poster för visning och kamerakoordinater för
rörelsebanor. Den ersätter de missvisande formerna *sökvägar för poseringar*
och *Baka till aktiv kamera* med rörelsebane- och koordinatsystemtermer.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-194-motion-path-display.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` ger 10/10. Filen är arkiverad och väntar på manuell import.

Batch 195 granskar nio poster för gränssnittsområden och redigerare. Den
normaliserar Blenders interna *editor space* till *redigerarläge* och återför
*Movie Clip Editor* till den etablerade termen *klippredigerare*.
Terminologilistan kompletteras med *editor space → redigerarläge*. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-195-editor-areas.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar bara den avsedda sammansättningen *videosekvensredigerare*. Filen
är arkiverad och väntar på manuell import.

Batch 196 granskar tio beskrivningar av Blenders redigerare: Dopeblad,
grafredigerare, NLA, textredigerare, Python-konsol, informationslogg,
Outliner och inställningar. Etablerade Blendernamn som *Dopeblad* och
*Outliner* behålls; övriga formuleringar är idiomatiska och kontextkontrollerade.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-196-editor-descriptions.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast de avsiktliga Blendernamnen *Dopeblad* och
*Outliner*. Filen är arkiverad och väntar på manuell import.

Batch 197 granskar fyrtioåtta poster för områdens redigerarlägen,
armaturredigering och tillgångssystemet. Den ersätter felaktiga *utrymmen*
med Blenders interna *redigerarlägen*, normaliserar
*resursbibliotek* i Asset Browser-kontexten och rättar bland annat
*Katalog enkelt namn*, *Förhandsvisning storlek* och den engelska
API-blandningen *key-map-objekt*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-197-area-and-assets.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar enbart en konstgjord längd- och V2-varning när korta
UI-etiketter fogas ihop till löptext. Filen är arkiverad och väntar på
manuell import.

Batch 198 granskar fyra datatyper för geometriattribut: bytefärg samt
signerade 16- och 32-bitars heltalsvektorer. Den rättar sammansättningen
*16-bitarsheltal* till *16-bitars heltal* och dokumenterar datatyperna i
terminologilistan. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-198-geometry-attribute-types.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar bara den avsedda facktermen *bytefärg* samt en
konstgjord V2-varning när fristående datatyper fogas ihop till löptext.
Filen är arkiverad och väntar på manuell import.

Batch 199 granskar fem geometriattribut- och kurvtermer. Den normaliserar
*Matris med flyttal* till den etablerade sammansättningen *flyttalsmatris*
och rättar *Bytefärgattribut* till *bytefärgsattribut*. *Spline* behålls som
Blenders etablerade tekniska term. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-199-geometry-matrices-and-splines.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` ger 10/10 och rapporterar enbart förväntade Blender-termer. Filen
är arkiverad och väntar på manuell import.

Batch 200 granskar trettiofyra klasser och beskrivningar för
geometriattribut. Den rättar grammatiska fel som *aktiv attribut* och
*geometriattributer*, normaliserar heltals- och flyttalsvektorer samt
bevarar det etablerade RNA-typnamnet *Float2-attribut*. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-200-geometry-attribute-classes.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar enbart förväntade sammansatta Blendertermer och
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen
är arkiverad och väntar på manuell import.

Batch 201 granskar tjugosex inställningar för bakning av renderingsdata:
bursextrudering, normalrymd, axelkanaler, avstånd, marginaler och
bakningspass. Den rättar bland annat *Vertikal dimension av bakningskartan*
till *Bakningskartans höjd* och normaliserar formuleringarna för
efterbehandling och burens mesh-kontext. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-201-bake-settings.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar enbart förväntade facktermer samt konstgjorda längd- och
V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och väntar
på manuell import.

Batch 202 granskar trettioett poster för bakningens utdata: sparläge,
bilddatablock, materialuppdelning, burstrålar, ljusbidrag och målyta.
Den rättar bland annat *Vald till aktiv* till *Valda till aktiv*, ersätter
den oidiomatiska utmatningsformuleringen med *Var den bakade kartan ska
lagras* och behåller *Transmission* som Blenders etablerade shaderterm.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-202-bake-output.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar enbart förväntade Blendertermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 203 granskar tretton poster för Bézierkurvor, kontrollpunkter,
handtagsmarkering, mjukkroppsmål, åtgärdsdatablock och äldre
Grease Pencil-annoteringar. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-203-curves-actions-annotations.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt en
konstgjord V2-varning från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 204 granskar tjugoen samlingstyper för BlendData: mesh, formnycklar,
målningskurvor, åtgärder, annoteringar, Grease Pencil och linjestilar. Den
rättar bland annat *Samling av samlingar* till *Samling av annoteringar* och
*Huvudfärgkurvor* till *Huvudmålningskurvor*. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-204-blend-data-collections.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` ger 10/10 och rapporterar enbart avsedda Blendertermer. Filen är
arkiverad och väntar på manuell import.

Batch 205 granskar tjugofem poster för B-Bones: kurvhandtag, in- och
utgående axlar, Bézierhandtag och beräkning från viloposition. Den
normaliserar bland annat *Bézier-handtag* till *Bézierhandtag* och rättar
*viloposen* till projektspecifika *vilopositionen*. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-205-bbone-handles.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar enbart förväntade Blendertermer samt en konstgjord längdvarning
från sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell
import.

Batch 206 granskar trettiotvå B-Bone-poster för skalning, utjämning,
mappning, rullning och kuvertdeformering. Den ersätter kvarvarande engelska
UI-referenser som *Scale Easing* med *Skalutjämning* och använder
*vilopositionen* konsekvent. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-206-bbone-mapping-and-deform.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar enbart förväntade Blendertermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 207 granskar arton poster för armaturbenens ändpunkter och deras
valbarhets-, matris- och skalningsbeskrivningar. I specifika benkontexter
används *benhuvud* och *benspets*, medan den delade, flerkontextuella
UI-etiketten *Tail* lämnas som *Svans* eftersom den också används för
partikelsystem. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-207-bone-head-tail-context.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar enbart en konstgjord längd- och V2-varning från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 208 granskar elva poster för bensamlingar, urvalsuppsättningar och
Rigify-paneler. Den ersätter den felaktiga tekniska betydelsen *matris* med
*fält* för Blenders interna array av bensamlingar och förkortar den långa
hjälptexten utan informationsförlust. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-208-bone-collections.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
ger 10/10. Filen är arkiverad och väntar på manuell import.

Batch 209 granskar arton poster för kurvskulptering och Grease
Pencil-penslar. Den ersätter engelska skulpteringstermer med
*fåra-/nypningsfaktor*, *krattningsfaktor*, *topologisk krattning* och
*beständighet*, som samtidigt dokumenteras i terminologilistan. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-209-brush-curves.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt en konstgjord
längdvarning från sammanfogade UI-etiketter. Filen är arkiverad och väntar
på manuell import.

Batch 210 granskar tretton Grease Pencil-poster för fyllningsgränser,
slumpning, känslighet och styrka. Den normaliserar de generiska
formuleringarna till *slumpningskurva*, *kurva som styr känsligheten* och
*kurva som styr styrkan* i enlighet med projektets terminologi. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-210-grease-pencil-curves.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar enbart den etablerade facktermen *slumpningskurva*
och konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter.
Filen är arkiverad och väntar på manuell import.

Batch 211 granskar trettio Grease Pencil-poster för förenkling,
indataprover, fyllningsgränser, streckkollision, UV och suddgummi. Den
normaliserar bland annat *Indataprover*, *skärmrymd* och *vyport* samt
ersätter den engelska etiketten *Occlude Eraser* med den funktionsbeskrivande
formen *Endast synliga streck*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-211-grease-pencil-brush-controls.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 212 granskar 46 Grease Pencil-, cache- och kameraposter. Den
normaliserar penselinställningar till *slumpning*, förtydligar ritplattans
tryckstyrning och använder den etablerade termen *redigerarläge* i
hjälptexterna för filmklipp och bilder. Kamerans tidigare oidiomatiska
*ortovy* skrivs som *ortografisk vy*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-212-grease-pencil-and-camera.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 213 granskar 51 kameraposter för bakgrundsbild, skärpedjup och
stereoskopi. Den rättar den för snäva formen *bildförhållande* till
*förhållande*, använder *inåtvinklad* för stereoläget *Toe-in* och följer
terminologins *vridpunkt* för *Pivot*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-213-camera-background-depth-stereo.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 214 granskar 39 poster för animeringsdrivrutiner, barnpartiklar och
tygsimuleringens kollisioner. Den ersätter det interna engelska namnet
*ChannelDriver* med den begripliga UI-termen *drivrutinsvariabler*, skriver
*barnpartikel* ihop och förtydligar skillnaden mellan kollision och
kollisionssvar. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-214-drivers-particles-cloth-collision.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 215 granskar 54 poster för tygsimuleringens material-, fjäder- och
tryckinställningar. Den normaliserar *fäststyvhet* för låsta hörnpunkter,
*skjuvning* för `shear` och *dragfjäderdämpning* för dämpning vid sträckning;
de två styvhetstermerna dokumenteras i terminologilistan. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-215-cloth-settings.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 216 granskar 33 poster för tygsimuleringens hörnpunktsgrupper och
lösarens resultatdiagnostik. Den normaliserar *hörnpunktsgrupp*,
*voxelrutnät*, *antal iterationer* och *indata* samt gör felstatusernas
hjälptexter idiomatiska. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-216-cloth-solver.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 217 granskar 48 poster för samlingsbaserad ljuslänkning och
fysikkollisioner. Den rättar grammatiskt trasiga ljuslänkningsbeskrivningar,
normaliserar *samling*, *genomsläpplighet* och *vidhäftning* samt skiljer
tydligt mellan kollision, kollisionsobjekt och genomträngning. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-217-collections-collisions.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 218 granskar 46 poster för färghantering och standardiserade
färgrymder. ACES, AgX, Filmic, FilmLight och Khronos bevaras som namn, medan
svenska beskrivningar normaliseras, särskilt *vitpunkt för illuminanten D65*
i stället för den sakligt felaktiga *belysningsstyrka*. Terminologilistan
dokumenterar dessa namn och *illuminant*. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-218-color-management.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 219 granskar 24 poster för färgvisning, HDR, vitbalans och
visningstransformering. Den ersätter de felaktiga formerna *display* och
*vytransformator* med *visning* respektive *visningstransformering* och
använder den etablerade Blender-termen *vyport*. Samtliga granskade poster
har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-219-color-view-settings.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 220 granskar femton poster för texturernas färgmappning och
blandningslägen. Den ersätter otydliga eller engelska former med bland annat
*färg som blandas med texturens utdatafärg*, *blandningstyp*, *Blanda*,
*Mörkare*, *Täcka över* och *Dividera*. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-220-texture-color-mapping.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 221 granskar 28 poster för färggradienter, färgstopp och
interpolering. Den ersätter det onödiga lånet *färgramp* med
*färggradient*, normaliserar *färginterpolering* och rättar de matematiska
interpoleringstyperna *Utjämnad*, *Kardinal* och *B-spline*. Terminologilistan
har uppdaterats med den återkommande UI-termen. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-221-color-gradients.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 222 granskar fjorton poster för färgstopp, filutdata och den interaktiva
konsolen. Den följer den nya termen *färggradient*, normaliserar
*filutdataplatser* och skiljer användarens *konsolinmatning* från tekniska
*indata*. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-222-color-stops-console.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade Blender- och facktermer samt konstgjorda längd-
och V2-varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 223 granskar 39 poster för begränsningar och deras koordinatrymder.
Den normaliserar *ägarkoordinatsystem*, *poseringsrymd* och *lokal rymd*, samt
använder den etablerade betydelsen *biblioteksöverskrivning* för `Library
Override`. Terminologilistan utökas med de återkommande rymdtermerna.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-223-constraints-coordinate-spaces.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade Blender- och facktermer samt
konstgjorda längd- och V2-varningar från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 224 granskar 33 poster för Blender-begränsningar, Action och armaturer.
Den normaliserar bland annat *avståndsbegränsning*, *positionsbegränsning*,
*transformationskanal*, *förskjutning* och *vridpunkt*. Blender-datatypen
`Action` bevaras i teknisk hjälptext, medan de svenska etiketter och
beskrivningar som omger den rättas. Terminologilistan utökas med termer för
begränsningar, transformation, armaturens omslutningar och Action. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-224-constraints-actions.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast facktermer och en konstgjord längdvarning från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 225 granskar åtta ytterligare poster för kurvbegränsningar och benmål.
Den rättar den missvisande ordagranna formen *Klämma till* till
*Begränsa till*, använder *begränsningsruta* i stället för *begränsningsbox*
och normaliserar den armatursspecifika skalan *benhuvud/benspets*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-225-constraints-bone-targets.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade facktermer och en konstgjord
ordföljdsvarning från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 226 granskar 25 poster för rotations-, skalkopierings-,
transformations- och filmspårningsbegränsningar. Den ersätter otydliga eller
felaktiga former såsom *Applicera*, *euler-komponentsvärden*, *Offset* och
*Undistort* med kontextuellt korrekta svenska motsvarigheter. Den normaliserar
också föräldrarelations- och begränsningsavståndstexten. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-226-constraints-rotation-tracking.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast etablerade facktermer och konstgjorda längd- och
ordföljdsvarningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 227 granskar 41 poster för IK, rotationsintervall, vridpunkter,
Shrinkwrap och Spline-IK. Den ersätter felaktiga allmänord och oöversatta
etiketter med bland annat *IK-sträckning*, *benspets*, *vridpunktsbegränsning*,
*ytborttagning*, *axelrymd* och *fästläge*. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-227-constraints-ik-shrinkwrap.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast facktermer samt konstgjorda längd- och
ordföljdsvarningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 228 granskar 41 poster för Spline-IK, Stretch To, Transform Cache och
Transform-begränsningar. Den normaliserar bland annat *volymbevarande*,
*kvaternionrotation*, *svängning och vridning*, *transformationscache* samt
käll- och utdataaxlar. Terminologilistan utökas med återkommande
constraint-termer. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-228-constraints-spline-transform.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast facktermer samt konstgjorda längd- och
ordföljdsvarningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 229 granskar 14 poster för kurvkartläggning och kurvmålning. Den rättar
bland annat en korrupt Bézier-översättning, normaliserar *vitnivå*,
*kurvkartläggningspunkt*, *streck* och *förskjutning* samt följer Blenders
etablerade term *vyport*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-229-curves-paint.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast facktermer och konstgjorda längd- och ordföljdsvarningar
från sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell
import.

Batch 230 granskar 13 poster för kurvprofiler, beroendegrafen och
instansobjekt. Den ersätter oidiomatiska former som *prov på* och *prova*
med det korrekta fackverbet *provta*, rättar *linje*, *slingor*,
*transformationsmatris*, *bildrutor* och rymdbenämningar. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-230-profiles-depsgraph.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerad fackterminologi samt konstgjorda längd- och
ordföljdsvarningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 231 granskar 30 poster för Dynamic Paint-penseln. Den normaliserar
bland annat *färggradient*, *närhetsavtagande*, *våtkarta*, *duknormal*,
*penselnormal*, *utjämningsradie*, *heltäckande radie* och *smetning* enligt
Blenders Dynamic Paint-dokumentation. Terminologilistan kompletteras med de
återkommande Dynamic Paint-termerna. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-231-dynamic-paint-brush.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade facktermer samt konstgjorda längd- och
ordföljdsvarningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 232 granskar 25 poster för Dynamic Paint-duken och dess ytlager. Den
rättar bland annat *dukinställningar*, *målningsyta*, *penselsamling*,
*radieskala*, *färgtorkning*, *heltäckande radie*, simuleringsbildrutorna
och utdatafälten. Terminologilistan kompletteras med termer för dukens
inställningar, målningsytor och våtkartor. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-232-dynamic-paint-canvas.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade facktermer och en konstgjord längdvarning från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 233 granskar 16 återstående poster för Dynamic Paint-ytor. Den rättar
bland annat *kantutjämning*, *upplösning*, *våthet*, *utdata*, *utjämning*,
*fjäder* och *Dynamic Paint-dukytor*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-233-dynamic-paint-surface.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast etablerade facktermer och en konstgjord längdvarning från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 234 granskar 10 poster för armaturernas redigeringsben. Den normaliserar
*benhuvud*, *benspets*, *rullning*, *längdaxel*, *armaturens rymd* och
*transformeras*. Terminologilistan rättas så att benens ändpunkter inte längre
blandas ihop med *svans* eller *stjärtände*. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-234-edit-bones.po` passerar `msgfmt`,
l10n-lint, riktad Hunspell, diffkontroll, Gitleaks och `svlang`. Filen är
arkiverad och väntar på manuell import.

Batch 235 granskar 14 poster för kraftfältens effektorvikter. Den normaliserar
*effektor*, *effektorvikt*, *effektorsamling*, *kurvguide*, *motstånd* och
*virvel* efter Blenders egna kraftfältstyper. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-235-effector-weights.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast domänspecifika kraftfältstermer och en konstgjord
ordföljdsvarning från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 236 granskar 16 poster för F-kurvor och nyckelbildrutor. Den rättar
engelska kvarlevor och felaktiga former till bland annat *nyckelbildruta*,
*Action-grupp*, *Grafredigeraren*, *modifierare*, *provtagna punkter* och
*F-kurvprov*. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-236-fcurves-keyframes.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast facktermer och konstgjorda varningar från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 237 granskar 10 FFmpeg- och utdataetiketter med uppenbart korrupta
översättningar. Den rättar bland annat *Inget ljud*, *Ingen video*,
*FFmpeg-videokodek*, *H.264*, *Ogg*, *Medelhög kvalitet* och *Låg kvalitet*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-237-ffmpeg-output.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast tekniska namn och en konstgjord ordföljdsvarning
från sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell
import.

Batch 238 granskar 15 poster för F-kurvmodifierare och cyklisk interpolation.
Den normaliserar *påverkan*, *F-kurvmodifierare*, *stegad interpolation* och
*nyckelbildruteintervall* samt tar bort engelska kvarlevor i hjälptexterna.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-238-fcurve-modifiers.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
Filen är arkiverad och väntar på manuell import.

Batch 239 granskar 14 poster för F-kurvmodifierare och kraftfält. Den rättar
bland annat *äldre brus*, *avtagandeexponent*, *linjärt motstånd*,
*kvadratiskt motstånd* och *brus för kraftens styrka*. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-239-fmodifiers-fields.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. Filen är
arkiverad och väntar på manuell import.

Batch 240 granskar 7 kurvguide- och kraftfältsalternativ. Den rättar
*förskjutning*, *knäck*, *fläta*, *radiell*, *rullning*, *rotation* och
*harmonisk dämpning*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-240-field-guides.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. Filen är
arkiverad och väntar på manuell import.

Batch 241 granskar 9 ytterligare kraftfältssträngar. Den normaliserar
*brusets frö*, *gradient*, *effektor*, *Lennard-Jones-potentialen*,
*gravitationsavtagande* och *avstånd*. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-241-field-forces.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. Filen är
arkiverad och väntar på manuell import.

Batch 242 granskar 18 filter och hjälptexter i filbläddraren. Den normaliserar
Blenders datatypnamn till bland annat *ljussondsdatablock*,
*målningskurvdatablock*, *partikelinställningar*, *Action-datablock* och
*filvals-ID-filter*, och följer den etablerade UI-terminologin för resurser
och Freestyle. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-242-file-browser-types.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast sammansatta Blender-termer och en konstgjord
ordföljdsvarning från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 243 granskar 14 resurs- och importsträngar i filbläddraren. Den
normaliserar *resurskatalog*, *resursmetadata*, *resursvalsparametrar*,
*etikettsfilter*, Blender-ID-typer och import av länkade eller kopierade
datablock. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-243-file-browser-assets.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast sammansatta Blender-termer och konstgjorda
ordföljdsvarningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 244 granskar 20 geometriattribut och Mantaflow-strängar för vätske-,
rök- och eldvolymer. Den normaliserar bland annat
*flyttalsattributvärde*, *matrisattributvärde*, *brusdata*,
*rökdensitetsrutnät*, cachetyp och rökvisning i vyporten. Terminologilistan
har kompletterats med de återkommande formerna för flyttalsattribut.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-244-fluid-domain-attributes.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast facktermer och en konstgjord längdvarning från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 245 granskar 20 Mantaflow-strängar för rök- och vätskedomänens
styrning, celltyper och rutnät. Den normaliserar bland annat *vorticitet*,
*styrningsvikt*, *styrningsdomän*, *styrningsobjekt*, *värmerutnät*,
*flaggrutnät* och FLIP-simuleringens stänkeffekt. Terminologilistan har
kompletterats med den hydromekaniska facktermen *vorticitet*. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-245-fluid-guides-grids.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast tekniska termer och konstgjorda varningar från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 246 granskar 20 Mantaflow-strängar för sekundära vätskepartiklar och
styrningsläge. Den rättar bland annat *bubbelmotstånd*,
*begränsningströskel*, *potentialradie*, *styrhastighetsfält*,
*viskositetsbas*, *kollision* och *åsidosätt*. Terminologilistan har
kompletterats med *vätskestyrning* och *sekundära partiklar*. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-246-fluid-secondary-particles.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast en konstgjord längd- och ordföljdsvarning från
sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 247 granskar 12 Mantaflow-strängar för simuleringssteg, cache,
rutnätsvisning och vektorvisning. Den normaliserar bland annat
*rutnätsvisning*, *färggradient*, *mesh-hörnpunkt*, *cachen*, *lösare* och
vektorernas *belopp*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-247-fluid-display-cache.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast en konstgjord ordföljdsvarning från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 248 granskar 15 Mantaflow-strängar för effektorer och flödeskällor.
Den normaliserar bland annat *delbildrutor*, *effektorobjekt*,
*vätskeemission*, *ytemission*, *initialhastighet* och
*slumphastighetens storlek*. Terminologilistan har kompletterats med
*ytemission* i Mantaflow-kontext. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-248-fluid-flow-settings.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast en konstgjord ordföljdsvarning från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 249 granskar 25 Freestyle-strängar för linjeuppsättningar och
funktionskantsurval. Den normaliserar bland annat *gränskant*,
*funktionskantstyp*, *ytmarkering*, *linjeuppsättning*, *streckrendering*,
*visningslagerdatablock* och *ytjämnhet*. Terminologilistan har
kompletterats med *funktionskantstyp*. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-249-freestyle-line-sets.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast facktermer och konstgjorda varningar från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 250 granskar 25 strängar för Grease Pencil-anteckningar,
anteckningslager och lökskalning. Den normaliserar bland annat *bildruta*,
*anteckningsbildruta*, *anteckningslager*, *lökskalning*, *lökskal*,
*bildrutenummer* och *linjallager*. Terminologilistan har kompletterats med
*anteckningsbildruta* och *anteckningslager*. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-250-annotation-frames.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar endast tekniska egennamn, ovanliga sammansättningar och
konstgjorda varningar från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 251 granskar 25 Grease Pencil-strängar för skulpteringsguider,
automaskering och strecktjocklek. Den normaliserar bland annat
*skulpteringsguide för Grease Pencil*, *radiell*, *streckkorsning*,
*penselns avtagande*, *automaskering*, *strecktjocklek* och
*anteckningsstreckpunkt*. Terminologilistan har kompletterats med
*skulpteringsguide för Grease Pencil* och *automaskering*. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-251-grease-pencil-sculpt.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast tekniska egennamn, ovanliga sammansättningar och
en konstgjord längdvarning från sammanfogade UI-etiketter. Filen är arkiverad
och väntar på manuell import.

Batch 252 granskar 18 strängar för Blender-gizmor och tangentmappningar. Den
rättar bland annat *samling av gizmor*, *tangentmappning*,
*förskjutningsmatris*, *skalbas*, *urvalsförskjutning*, *skärmrymd* och
*zoomnivå*. Terminologilistan har kompletterats med *samling av gizmor*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-252-gizmos-keymaps.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast det avsiktliga Blender-låneordet *gizmo*,
facktermen *skalbas* och konstgjorda varningar från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 253 granskar 22 strängar för GizmoGroup-alternativ, Blender-regioner
och gizmoegenskaper. Den normaliserar bland annat *interaktion*,
*verktygsinitiering*, *tangentmappning för reservverktyg*, *regiontyp*,
*flytande område*, *utförandeknappar*, *redigerarläge* och *indataegenskaper*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-253-gizmo-groups.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast det avsiktliga Blender-låneordet *gizmo*,
ovanliga sammansättningar och konstgjorda varningar från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 254 granskar 17 Grease Pencil-strängar för strecksegment, ritningar
och nyckelbildrutor. Den normaliserar bland annat *streckmodifierarsegment*,
*mellanrum*, *cykliskt läge*, *Grease Pencil-ritning*,
*Grease Pencil-bildruta*, *bildrutenummer* och *nyckelbildrutetyp*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-254-grease-pencil-segments.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast tekniska egennamn, ovanliga sammansättningar och
en konstgjord längdvarning från sammanfogade UI-etiketter. Filen är arkiverad
och väntar på manuell import.

Batch 255 granskar 20 Grease Pencil-strängar för maskeringslager,
anteckningslager och tidsmodifierarsegment. Den normaliserar bland annat
*maskeringslagernamn*, *aktivt anteckningslager*, *tidsmodifierarsegment*,
*förskjutning*, *överordnad lagergrupp*, *lökskal* och *radieändring*.
Terminologilistan har kompletterats med *tidsmodifierarsegment*. Samtliga
granskade poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-255-grease-pencil-layers.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast ovanliga sammansättningar och konstgjorda
varningar från sammanfogade UI-etiketter. Filen är arkiverad och väntar på
manuell import.

Batch 256 granskar 15 Grease Pencil-strängar för lagertransformationer,
toningsfärg och lagergrupper. Den rättar bland annat *lagrets skala*,
*toningsfärg*, *toningsfaktor*, *förskjutning*, *visningslager*,
*Grease Pencil-grupp* och *aktiv lagergrupp*. Terminologilistan har
kompletterats med *toningsfärg* och *toningsfaktor*. Samtliga granskade
poster har fått sina `fuzzy`-markeringar borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-256-grease-pencil-layer-transforms.po`
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast tekniska egennamn och en konstgjord
ordföljdsvarning från sammanfogade UI-etiketter. Filen är arkiverad och
väntar på manuell import.

Batch 257 granskar 9 animeringstermer för Grease Pencil-nyckelbildrutor.
Blenders manual har använts för att fastställa typernas funktion: en
*mellanpose* beskriver rörelsen mellan nyckelposer, en *rörlig hållning* ger
liten rörelse kring en hållen pose och ett *ytterläge* anger ett extremt
rörelseläge. Även beskrivningarna för slumpade och verktygsgenererade
nyckelbildrutor har rättats. Terminologilistan har kompletterats med dessa
tre typer. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-257-keyframe-types.po` passerar
`msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks. `svlang`
rapporterar enbart de fackliga sammansättningarna *mellanpose* och
*nyckelposer*. Filen är arkiverad och väntar på manuell import.

Batch 258 granskar 19 API-strängar för Blender-ID:n och datablock. Den
normaliserar bland annat *skräpinsamling*, *körtidsdata*, *svag
biblioteksreferens*, *biblioteksåsidosättning* och *ID-datablock*.
Terminologilistan har kompletterats med de nya
datablocks- och körtidstermerna och den motstridiga formen
*biblioteksöverskrivning* har ersatts av *biblioteksåsidosättning*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna i
deltafilen `blender-ui-sv-reviewed-20261106-batch-258-id-datablocks.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks. `svlang` rapporterar bara en konstgjord längdvarning från
sammanfogade API-beskrivningar. Filen är arkiverad och väntar på manuell
import.

Batch 259 granskar 18 API-strängar för Actions, F-kurvor och den nyare
lager- och åtgärdsplatsstrukturen. Den ersätter bland annat engelska
*slot*, *slotted actions* och *loopar* med *åtgärdsplats*, *skiktad
åtgärd*, *äldre åtgärd* och svenska beskrivningar av upprepning. Den
klargör också bildruteintervall och äldre API-beteende. Terminologilistan
har kompletterats med *åtgärdsplats*, *skiktad åtgärd* och *äldre åtgärd*.
Samtliga granskade poster har fått sina `fuzzy`-markeringar borttagna i
deltafilen `blender-ui-sv-reviewed-20261106-batch-259-actions.po`. Filen
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` varnar endast när den behandlar flera sammanfogade UI-etiketter
som en 60 ord lång mening samt för fackordet *bildruteintervall*. Filen är
arkiverad och väntar på manuell import.

Batch 260 granskar 14 armatursträngar för benaxlar, visningslägen,
viloposition och relationslinjer. Den rättar bland annat *benaxlarnas
position*, *oktaedrar*, *B-spline-kurvor*, *benspets* och *Slutför skript*.
Terminologilistan har kompletterats med formerna för *Octahedral* och
*B-Spline*. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-260-armature-display.po`. Filen
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` markerar bara fackordet *B-spline-kurvor* och konstgjorda
varningar från sammanfogade UI-etiketter. Filen är arkiverad och väntar på
manuell import.

Batch 261 granskar 22 Rigify-strängar för rigggenerering, widgetar,
målrigg och teman. Den rättar bland annat *slutskript*, *widgetmesher*,
*länkade dubbletter* och namngivningen av metariggar. Rigifys interna
temavärden `THEME01`–`THEME20` bevaras exakt som kodvärden. Terminologin
har kompletterats med *slutskript*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-261-rigify-generation.po`. Filen
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
Hunspell och `svlang` rapporterar enbart de avsiktliga temavärdena och den
projektspecifika sammansättningen *widgetmesher*. Filen är arkiverad och
väntar på manuell import.

Batch 262 granskar 7 strängar för penselns områdesradie och automaskering.
Den rättar särskilt områdesradien så att den korrekt avser provtagning av
områdesplanets djup, samt normaliserar *spridningssteg*, *automaskering* och
gradient för avtagande. Terminologilistan har kompletterats med
*områdesradie* och *spridningssteg*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-262-brush-automasking.po`. Filen
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
Hunspell och `svlang` rapporterar endast den korrekta fackformen
*kavitetsmasken* och en konstgjord ordföljdsvarning från sammanfogade
UI-etiketter. Filen är arkiverad och väntar på manuell import.

Batch 263 granskar 28 strängar för penselns färgblandningslägen och en
delad nodträdsvariant av *Color Burn*. Den använder Blenders dokumentation
för att bevara blandningslägenas funktion och den tidigare granskade
Blender-exporten för deras etablerade svenska UI-namn: *Färgbränn*, *Linjär
bränn*, *Raster*, *Färgskugga*, *Punktljus*, *Uteslutning* och *Levande
ljus*. Hjälpraderna har samtidigt normaliserats till konsekvent svenska.
Terminologilistan har kompletterats med penselblandningsläge och de
återkommande färgblandningslägena. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-263-brush-blending-modes.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks. `svlang` rapporterar endast konstgjorda längd- och
ordföljdsvarningar eftersom separata UI-etiketter analyseras som en enda
mening. Filen är arkiverad och väntar på manuell import.

Batch 264 granskar 2 strängar för penselns pixelkärna vid oskärpa och
skärpning. Den ersätter omskrivningen *radie för kärnan* med den etablerade
UI-termen *kärnradie* och klargör att värdet anges i pixlar. Terminologilistan
har kompletterats med *kärnradie*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-264-brush-blur-kernel.po`. Filen
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
`svlang` rapporterar endast en svag, icke åtgärdbar passivvarning för den
tekniska beskrivningen. Filen är arkiverad och väntar på manuell import.

Batch 265 granskar 11 strängar för skulpteringspenselns gränsdeformering.
Den skiljer deformationslägena *Böjning*, *Expandera*, *Blås upp*, *Flytta*
och *Vridning* från vanliga verb i andra delar av gränssnittet. Den
normaliserar också *avtagande vid gräns*, formuleringen för cykliska
slingsmönster och penselns funktioner. Terminologilistan har kompletterats
med *gränsavtagande* och *gränsdeformering*. Samtliga granskade poster har
fått sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-265-brush-boundary-deformation.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks. Hunspell markerar endast imperativet *Loopa*, som används
avsiktligt för Blenders cykliska slingsalternativ, och `svlang` rapporterar
en konstgjord ordföljdsvarning från sammanfogade UI-etiketter. Filen är
arkiverad och väntar på manuell import.

Batch 266 granskar 8 strängar för tygsimuleringspenselns dämpning och
deformationslägen. Den rättar bland annat *tygdämpning*, *Nypunkt*, *Nyp
vinkelrätt*, *Tryck*, *simuleringsavklingning* och beskrivningen av hur
krafter fortplantas genom tyget. Terminologilistan har kompletterats med
tygsimuleringens återkommande termer. Samtliga granskade poster har fått
sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-266-brush-cloth-settings.po`. Filen
passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och Gitleaks.
Hunspell och `svlang` markerar enbart de avsiktliga facksammansättningarna
*nypunkt* och *simuleringsavklingning* samt en konstgjord ordföljdsvarning
från sammanfogade UI-etiketter. Filen är arkiverad och väntar på manuell
import.

Batch 267 granskar 5 strängar för tygsimuleringens aktiva område och
begränsning. Den förtydligar var simuleringens deformationsverkan avtar,
att begränsningsfaktorn relateras till radien och att det aktiva
simuleringsområdet flyttas med penseln. Terminologilistan har kompletterats
med *simuleringsområde*. Samtliga granskade poster har fått sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-267-brush-cloth-simulation-area.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks. Hunspell markerar endast den etablerade Blenderformen *meshen*.
Filen är arkiverad och väntar på manuell import.

Batch 268 granskar 6 strängar för penselns färgval, veckpensel och
markörfärg. Den ersätter engelska och felaktiga uttryck med *enfärg*,
*toning*, *veckpensel*, *nypfaktor för veckpensel* och *Markörens färg vid
tillägg*. Terminologilistan har kompletterats med dessa verktygs- och
färgtermer. Samtliga granskade poster har fått sina `fuzzy`-markeringar
borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-268-brush-color-and-crease.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks. Hunspell och `svlang` markerar bara de avsiktliga
facksammansättningarna *enfärg*, *veckpensel* och *nypfaktor*. Filen är
arkiverad och väntar på manuell import.

Batch 269 granskar 7 strängar för kurvornas avtagande och Curves
Sculpt-penslar. Den ersätter den felaktiga verktygsformen *Typ av borste* med
*Penseltyp*, använder de etablerade kurvnamnen *Jämn* och *Omvänd kvadrat*
och översätter verktyget *Puff* efter dess funktion till *Blås upp*. Även
beskrivningarna av streckcykelns provtagning har normaliserats. Terminologin
har kompletterats med *penseltyp* och *omvänd kvadrat*. Samtliga granskade
poster får sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-269-curves-sculpt-and-dashes.po`.
Filen kontrolleras med `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks före arkivering. Filen väntar därefter på manuell import.

Batch 270 granskar 14 strängar för penselns elastiska deformering och
avtagande. Den rättar de missvisande verktygsnamnen *Tvåskaligt gripdon* och
*Grepp i tre skalor* till *Flytta i två skalor* respektive *Flytta i tre
skalor*. Den normaliserar dessutom *deformationsmål*, *avtagandeform*,
*fyllningströskel* och flera geometriska hjälprader. Terminologilistan har
kompletterats med de återkommande inställningstermerna. Samtliga granskade
poster får sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-270-elastic-deform-and-falloff.po`.
Filen kontrolleras med `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks före arkivering. Filen väntar därefter på manuell import.

Batch 271 granskar 16 strängar för Grease Pencil-penslarnas skulptering,
kloning och toning. Den ersätter engelska och inkonsekventa verktygsnamn med
*Penseltyp*, *Tryck*, *Vridning*, *Nyp*, *Klon* och *Smeta*. Den rättar också
den engelska formen *strokepunkter* och skiljer toningens fyllnads- och
penseldragslägen åt. Terminologilistan har kompletterats med Grease
Pencil-penseltyp och toningsinställningarna. Samtliga granskade poster får
sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-271-grease-pencil-sculpt-and-gradient.po`.
Filen kontrolleras med `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks före arkivering. Filen väntar därefter på manuell import.

Batch 272 granskar 20 strängar för penselns begränsning, hårdhet,
tryckmodulering, slumpvariation och maskschablon. Den ersätter bland annat
de direkta engelska formerna *Jitter*, *Jittering* och *Mask Stencil* med
*variation*, *variationsenhet* och *maskschablon*. Den normaliserar även våt
beständighet och förbättrar de tekniska beskrivningarnas svenska ordföljd.
Terminologilistan har kompletterats med *maskschablon* och
*variationsenhet*. Samtliga granskade poster får sina `fuzzy`-markeringar
borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-272-brush-jitter-and-mask-stencil.po`.
Filen kontrolleras med `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks före arkivering. Filen väntar därefter på manuell import.

Batch 273 granskar 22 strängar för skulpteringsplan, normalradie,
målningskurvor och poseringsverktyg. Den återställer projektets etablerade
termer *målningskurva*, *hörnpunkt*, *mesh* och *ytuppsättning* och ersätter
kvarvarande engelska former som *Squash & Stretch*. Terminologin har också
städats så att den motstridiga dubbleringen för Face Set inte längre styr
nya översättningar fel. Samtliga granskade poster får sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-273-sculpt-plane-and-pose.po`.
Filen kontrolleras med `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks före arkivering. Filen väntar därefter på manuell import.

Batch 274 granskar 23 strängar för skulpteringspenslarnas verktygsnamn,
penselavtryck och schabloninställningar. Den översätter bland annat
*Slide Relax*, *Blob*, *Multires Displacement Eraser* och *Multires
Displacement Smear* konsekvent. Den rättar också felöversättningen
*buskar* till *penselavtryck* och använder *ytuppsättningar* i Face Set-
verktyget. Terminologilistan har kompletterats med glidutjämning och
Multires-penslarna. Samtliga granskade poster får sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-274-sculpt-brushes-and-stencils.po`.
Filen kontrolleras med `msgfmt`, l10n-lint, riktad Hunspell, diffkontroll och
Gitleaks före arkivering. Filen väntar därefter på manuell import.

Batch 275 granskar 28 strängar för penseldragsmetoder, penselavtryck,
ytutjämning och topologisk krattning. Blenders egen manual bekräftar att
*Spacing* styr avståndet mellan penselavtryck och att *Topology Rake* riktar
kanterna efter penseldragets riktning. Därför används bland annat
*penseldragsmetod*, *Avstånd*, *penselavtryck*, *sprutpistol*,
*hörnpunkt* och *topologisk krattning*. Terminologilistan har kompletterats
med de återkommande inställningsnamnen. Samtliga granskade poster får sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-275-brush-stroke-and-smoothing.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` ger endast en konstgjord varning eftersom korta UI-etiketter läses
som en sammanfogad mening. Gitleaks körs före arkivering. Filen väntar
därefter på manuell import.

Batch 276 granskar 32 strängar för skulpteringens automaskering,
simuleringsgräns och relaterade penselinställningar. Blenders dokumentation
beskriver automaskering efter bland annat meshgräns, ytuppsättning,
ytkrökning, normal och ocklusion. Översättningen använder därför konsekvent
*hörnpunkt*, *ytuppsättning*, *ytuppsättningsgräns*, *automaskering* och
*penselavtryck*. Terminologilistan har kompletterats med hålighetsmask och
automaskering av meshgräns. Samtliga granskade poster får sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-276-sculpt-automasking.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markerar endast de avsiktliga Blender-sammansättningarna och en
konstgjord varning från sammanfogade UI-etiketter. Gitleaks körs före
arkivering. Filen väntar därefter på manuell import.

Batch 277 granskar 28 strängar för pensellägen, penselavstånd,
ritplattans tryck och våt målning. Den ersätter felöversatta termer som
*slag*, *tablett*, *offset*, *vertex*, *jitter*, *strokeposition* och
*smidig slaglängd* med konsekvent Blender-svenska. Terminologilistan har
kompletterats med *jämnt penseldrag*, *hörnpunktsmålning* och *våt
beständighet*. Samtliga granskade poster får sina `fuzzy`-markeringar
borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-277-brush-modes-and-pressure.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markerar endast tekniska sammansättningar och en konstgjord varning
från sammanfogade UI-etiketter. Gitleaks körs före arkivering. Filen väntar
därefter på manuell import.

Batch 278 granskar 10 strängar för Alembic-cachefiler, Cycles
förhandsladdning och hastighetsenheter. Blenders Alembic-dokumentation
bekräftar att cachefilen kan vara uppdelad i en filsekvens och att den läses
in som animerad geometri. Översättningen skiljer därför cachefilen från
allmänt cacheminne och använder *förhandsladdning* för *prefetch*.
Terminologilistan har kompletterats med Cycles Procedural-cachen.
Samtliga granskade poster får sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-278-cachefile-and-alembic.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell, `svlang` och
diffkontroll. Gitleaks körs före arkivering. Filen väntar därefter på
manuell import.

Batch 279 granskar 30 strängar för kameraobjektiv, synfält,
beskärningsavstånd och panoramisk projektion. Källkontexten i Blenders
kameradokumentation visar att longitude och latitude är projektionens
vinkelkoordinater. De normaliseras därför till *längdgrad* och *breddgrad*.
Batchen rättar även en felmappad översättning av *Custom Shader* samt
använder *fiskögeobjektiv* och *beskärningsavstånd* konsekvent.
Terminologilistan har kompletterats med kamerans projektionstermer.
Samtliga granskade poster får sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-279-camera-projection.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markerar endast tekniska produktnamn, facktermer och en konstgjord
varning från sammanfogade UI-etiketter. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Batch 280 granskar 18 strängar för panoramaprojektion, sensoranpassning,
passepartout och beskärningsvisning. Den normaliserar `Fisheye` till
*fisköge*, förklarar den ekvidistanta fullkupolprojektionen och ersätter
felaktiga adjektivformer i sensorinställningarna med svenska uppmaningar.
Terminologilistan har kompletterats med *sensoranpassning* och
*passepartout*. Samtliga granskade poster får sina `fuzzy`-markeringar
borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-280-camera-panorama-and-sensor.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markerar endast facktermerna och en konstgjord varning från
sammanfogade UI-etiketter. Gitleaks körs före arkivering. Filen väntar
därefter på manuell import.

Batch 281 granskar 10 strängar för kamerans kompositionsguider,
passepartout och säkra områden. Blenders kameradokumentation bekräftar att
säkra områden är hjälplinjer för tv-sändning och olika bildförhållanden.
Översättningen använder därför *säkra områden för tv-titel och handling* och
*säkra områden för mittbeskärning*. Terminologilistan har kompletterats med
de termerna samt *filmruta*. Samtliga granskade poster får sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-281-camera-guides-and-safe-areas.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markerar endast avsiktliga sammansättningar och en konstgjord
varning från sammanfogade UI-etiketter. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Batch 282 granskar 19 strängar för kurvors avfasning, tvärsnitt,
avsmalningsobjekt och kurvdeformering. Blenders geometrihandbok bekräftar
att en kurvas avfasning bygger ett rör med ett cirkulärt, objektbaserat eller
profilbaserat tvärsnitt. Den förklarar också att ett avsmalningsobjekt är en
skalningskurva längs den genererade geometrin, inte bara en förminskning vid
slutet. Översättningen använder därför konsekvent *kurvspline*, *tvärsnitt*,
*avsmalningsobjekt* och *avsmalningsradie*. Terminologilistan har
kompletterats med kurvans avfasningstvärsnitt, Mappa avsmalning och
meshgränser. Samtliga granskade poster får sina `fuzzy`-markeringar borttagna
i deltafilen `blender-ui-sv-reviewed-20261106-batch-282-curve-bevel-and-taper.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markeringar rapporteras separat. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Batch 283 granskar 10 strängar för textobjektens styckejustering,
teckenavstånd och typsnittsval. Blenders textdokumentation skiljer mellan
*Justify*, som fyller radens mellanrum vid radbrytning, och *Flush*, som
alltid fyller raden med teckenavstånd. Den tidigare översättningen *Spola*
är därför ett sakfel och ersätts av *Jämna marginaler*. Terminologilistan
anger nu skillnaden samt *teckenavstånd* som svensk term för den aktuella
kerninginställningen. Samtliga granskade poster får sina `fuzzy`-markeringar
borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-283-text-alignment-and-fonts.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markeringar rapporteras separat. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Den samlade importdeltafilen
`blender-ui-sv-reviewed-20261106-all-changes.po` sammanför de 288
arkiverade, granskade batcherna till 5 667 unika poster med respektive
senaste översättning. Filen är avsedd som fullständig lokal referens och
passerar `msgfmt`. För Weblate används i stället sex lokala importdelar med
högst 1 000 poster: fem delar om 1 000 och en slutdel om 667. Detta följer
den etablerade gränsen för att undvika att serverns import låser sig.

Batch 284 granskar 21 strängar för Freestyle-linjers ändlock,
streckmönster och kedjedelning. Blenders Freestyle-dokumentation beskriver
`Butt` som ett platt ändlock som slutar exakt vid streckets ändpunkt och
beskriver Dash/Gap som streck och mellanrum i både streckning och
delningsmönster. Därför ersätts det oöversatta *Butt*, engelska
*Split Dash/Gap* och inkonsekventa former som *gapet*, *luckan* och
*klyvning*. Terminologilistan har kompletterats med *stumt ändlock*,
*delningsstreck* och *delningsmellanrum*. Samtliga granskade poster får sina
`fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-284-freestyle-strokes-and-splitting.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markeringar rapporteras separat. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Batch 285 granskar 9 strängar för Freestyle-kedjors urval och
tjockleksplacering. Blenders Freestyle-dokumentation använder
*border edges* för funktionskanter vid gränser; översättningen normaliserar
dem till *gränskanter* i stället för de inkonsekventa och felaktiga formerna
*kantkanter* och *kantlinjer*. Den normaliserar också *Thickness Position*
till *tjockleksplacering* samt den kurvlinjära 2D-längden. Terminologilistan
har kompletterats med Freestyles gränskant och tjockleksplacering. Samtliga
granskade poster får sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-285-freestyle-thickness-position.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markeringar rapporteras separat. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Batch 286 granskar 10 strängar för Freestyle-kedjning, längdurval och
delningsmönster. Blenders dokumentation beskriver *Split Pattern* som ett
streckmönster som delar en kedja, inte ett redan delat mönster. Därför
normaliseras termen till *delningsmönster*, och urval efter antal kedjor
eller maximal/minimal 2D-längd skrivs som konkreta svenska UI-uppmaningar.
Terminologilistan har kompletterats med *delningsmönster*. Samtliga
granskade poster får sina `fuzzy`-markeringar borttagna i deltafilen
`blender-ui-sv-reviewed-20261106-batch-286-freestyle-chain-selection.po`.
Filen passerar `msgfmt`, l10n-lint, riktad Hunspell och diffkontroll.
`svlang` markeringar rapporteras separat. Gitleaks körs före arkivering.
Filen väntar därefter på manuell import.

Batch 365 granskar åtta återstående Dopebladsfilter för material, mesh,
metabollar och saknade NLA-data. Den använder den direkta hjälptextformen
*Visa även …*, behåller Blenders datatypnamn *mesh* och använder den
svenska UI-termen *metaboll*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-365-dope-sheet-display-filters-b.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 366 granskar tio Dopebladsfilter för modifierardata, filmklipp, noder,
fel och urval. Hjälptexterna normaliseras till direkta filterinstruktioner
med *Visa även* eller *Visa endast*, och *utvalda* ersätts med Blenders
konsekventa UI-term *valda*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-366-dope-sheet-filtering-and-selection.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 367 granskar tio Dopebladsfilter för partiklar, punktmoln, scener,
formnycklar och högtalare. Den normaliserar hjälptexterna till *Visa även …*
och rättar den missvisande personbeteckningen *talarrelaterade* till
*högtalarrelaterade*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-367-dope-sheet-display-filters-c.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 368 granskar åtta Dopebladsfilter för sammanfattning, texturer,
transformationer, volymer och värld. Den gör samtliga förklaringar direkta
med *Visa även …* och behåller den etablerade Blendertermen
*transformationer*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-368-dope-sheet-display-filters-d.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 369 granskar tio poster för Blenders uttrycks- och databaserade
drivrutiner. Den normaliserar termen *drivrutin* i termlistan, gör den
övergripande beskrivningen tydligare och rättar *Genomsnittligt värde* till
den etablerade UI-sammansättningen *Genomsnittsvärde*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-369-driver-basics.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 370 granskar åtta Driver-poster för gränsvärden, `self`, variabler och
drivrutinsmål. Den behåller `self` som namnrymdens kodnamn i stället för den
felaktiga betydelsen *själv*, och använder konsekvent *indata* för
drivrutinernas egenskapsvärden. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-370-driver-variables-and-targets.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 371 granskar tio Driver Target-poster för bennamn, kontextegenskaper,
aktuell scen och aktuellt vylager, RNA-sökvägar samt reservvärden. Den rättar
den felaktiga formen *använd fastighet* till *den egenskap som används* och
normaliserar *Bennamn* samt *Kontextegenskap*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-371-driver-target-context.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 372 granskar tio Driver Target-poster för reservvärden, ID-datablock,
rotationsläge och transformationsrymd. Den ersätter oöversatta former som
*fallback*, *parenting*, *restpose* och *constraints* med projektets svenska
termer *reservvärde*, *föräldraskap*, *viloposition* och *begränsningar*.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-372-driver-target-fallback-and-space.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 373 granskar tio poster för lokal transformationsrymd, reservläge och
Driver Variable. Den rättar det oöversatta *W Rotation* till *W-rotation*,
normaliserar *Använd reservvärde* och använder *i stället för* i den svenska
felhanteringstexten. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-373-driver-variable-basics.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 374 granskar åtta Driver Variable-poster för namnregler, indatakällor
och egenskaps-, transformations-, rotations- och kontextvariabler. Den
förtydligar vilka data som används vid utvärderingen och gör svenskans
subjektrelation tydlig i transformationsvärdet. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-374-driver-variable-sources.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 375 granskar tio Dynamic Paint-poster för inre närhet, målningsalfa,
målningsfärg, närhetsavstånd och färggradient. Den ersätter oöversatta
former av *proximity falloff* med *närhetsavtagande* och förtydligar att
avståndet styr var målningens färg påverkas. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-375-dynamic-paint-proximity.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 376 granskar tio Dynamic Paint-poster för målningskälla, objektcentrum,
meshvolym, färgens våthet, partikelsystem och avtagande. Den gör
*objektcentrum* konsekvent svenskt och förtydligar att partikelsystemet
används för målning. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-376-dynamic-paint-source-and-wetness.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 377 granskar tio Dynamic Paint-poster för närhetsavtagande,
strålriktning och projektion. Den använder *Jämn* som namn på ett
avtagandeläge, inte uppmaningen *Utjämna*, och förtydligar när ett
penselobjekt målas längs den valda strålriktningen. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-377-dynamic-paint-falloff-and-rays.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 378 granskar nio Dynamic Paint-poster för utjämnings- och heltäckande
radie, smetningsstyrka, absolut alfa och inverterad volympåverkan. Den
normaliserar etiketten *Absolut alfa* till svensk versalsättning och
förtydligar jämförelsen med det befintliga alfavärdet. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-378-dynamic-paint-radii-and-alpha.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 379 granskar tio Dynamic Paint-poster för radering, partikelradie,
projektion inom närhetsavstånd, smetning och alfamultiplikation. Den ersätter
snedstrecksformen *Radera/ta bort* med idiomatiska *Radera eller ta bort* och
gör skillnaden mellan närhet och närhetsavstånd tydlig. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-379-dynamic-paint-erase-and-smudge.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 380 granskar tio Dynamic Paint-poster för hastighetsberoende alfa,
färg och djup samt maximal hastighet, hastighetsfärggradient och
vågbegränsning. Den gör begreppet *hastighetsfärggradient* konsekvent i
samtliga hjälptexter. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-380-dynamic-paint-velocity.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 381 granskar tio Dynamic Paint-poster för vågpåverkan, vågtyp,
duk och målningsyta. Den ersätter den felaktiga formen *borste* med
*pensel* och normaliserar användningen av *målningsyta* i listetiketterna.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-381-dynamic-paint-waves-and-canvas.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 382 granskar tio Dynamic Paint-poster för målningsytans grundinställningar:
lager, penselsamling, påverkan, radie samt torkning och spridning av färg.
Den förtydligar att det är penselobjektens påverkan som justeras och att
färger övergår till bakgrunden när våthetsnivån sjunker. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-382-dynamic-paint-surface-basics.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 383 granskar tio Dynamic Paint-poster för maximal förskjutning,
upplösning samt droppningens acceleration och hastighet. Den gör
hjälptexten om upplösningstid idiomatisk och anger förskjutningens styrka
med en rakare satskonstruktion. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-383-dynamic-paint-displace-and-drip.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 384 granskar tio Dynamic Paint-poster för torktid, effekttyp,
droppning, krympning och simuleringens delsteg. Den använder den kompakta
UI-termen *effekttyp* och förtydligar att extra bildrutor beräknas mellan
scenens bildrutor. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-384-dynamic-paint-timing-and-effects.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 385 granskar tio Dynamic Paint-poster för bildutdata och målningsytans
initiala tillstånd. Den bekräftar etablerade UI-termer för utdatasökväg,
utdatabild och UV-textur samt behåller filformatens egna namn. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-385-dynamic-paint-output-and-initial-state.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 386 granskar tio Dynamic Paint-poster för cache, ytnamn, utdatanamn,
krympning och spridning. Den gör växlingshjälptexten idiomatisk genom att
uttrycka valet mellan att bearbeta och ignorera ytan. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-386-dynamic-paint-surface-output-and-effects.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 387 granskar tio Dynamic Paint-poster för ytformat, bildsekvens,
kantutjämning och upplösning av ytförändringar. Den normaliserar *Yttyp*
som kompakt UI-term. Termen *multisampling* har efter kontroll mot
terminologilistan återställts i batch 390. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-387-dynamic-paint-format-and-dissolve.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 388 granskar tio Dynamic Paint-poster för droppning, torkning,
inkrementell förskjutning och utdatalager. Den skiljer mellan beräkning av
droppningseffekten och användarens val samt skriver *inmatning till Blender*
i stället för den otympliga sammansättningen *Blender-inmatning*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-388-dynamic-paint-drying-and-output.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 389 granskar tio Dynamic Paint-poster för krympning, spridning, öppna
kanter, UV-karta och vågdämpning. Den gör processhjälptexterna konsekventa
med *Beräkna* och föredrar den korta formen *UV-kartans namn*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-389-dynamic-paint-waves-and-uv.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 390 granskar tio Dynamic Paint-poster för vågornas branthet,
utbredning, fjäderkraft, tidsskala och aktiva dukytor samt rättar en tidigare
termavvikelse. Den återställer den etablerade datorgrafiktermen
*multisampling* efter kontroll mot projektets terminologilista. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-390-dynamic-paint-wave-controls.po`
innehåller därför elva poster och är lokalt kontrollerad men ännu inte manuellt
importerad till Blender Translate.

Batch 391 granskar tio Blender-poster för armaturers redigeringsben:
huvudände, spets, matris, överordnat ben och rullning. Den använder
*armaturens koordinatsystem* för den tekniska betydelsen av *armature space*
och gör hjälpen om benets längd grammatisk. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-391-armature-edit-bone-basics.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 392 granskar tio Blender-poster för markering av armaturers ben och
effektorvikter. Den använder de mer idiomatiska formerna *hårväxt* och
*vikt för alla effektorer*, medan *Boid* behålls som Blender-namn. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-392-armature-selection-and-effectors.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 393 granskar tio Blender-poster för fysikens effektorfält och deras
vikter: laddning, kurvguide, motstånd, kraft, gravitation och harmonisk
påverkan. Den bevarar facktermer som *Kurvguide* och gör ägandekonstruktionerna
konsekventa med *effektorns vikt*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-393-physics-effector-fields.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 394 granskar tio Blender-poster för resterande effektortyper:
harmonisk, Lennard-Jones, magnetisk, vätskeflöde, textur, turbulens och
virvel. Den använder bindestreck i *Lennard-Jones-effektorns vikt* och
normaliserar alla viktetiketter. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-394-physics-effector-types.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 395 granskar tio Blender-poster för virvel- och vindeffektorer samt
RNA-objektens enum-egenskaper. Den behåller *enum* och *RNA* som tekniska
kodtermer, men granskar deras svenska omgivande text och identifierare.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-395-effectors-and-rna-enums.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 396 granskar tio Blender-poster för F-kurvor, RNA-arrayindex och
automatiska handtag i grafredigeraren. Den använder projektets etablerade
form *F-kurva* och skriver *F-kurvans färg i grafredigeraren* med korrekt
svensk ordföljd. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-396-animation-fcurve-handles.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 397 granskar tio Blender-poster för F-kurvors färglägen,
användardefinierade färger, RNA-sökväg och drivrutin. Den översätter
etiketternas *Auto* till *Automatiskt* men behåller koordinat- och
färgförkortningarna XYZ, RGB och YRGB. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-397-animation-fcurve-color-and-driver.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 398 granskar 28 poster för F-kurvors egenskaper och data: drivrutiner,
extrapolering, nyckelbildrutor, modifierare, provpunkter och urval. Den
normaliserar bland annat *Graph Editor* till *grafredigeraren* och
*user-editable keyframes* till *redigerbara nyckelbildrutor* i enlighet med
projektets terminologi. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-398-animation-fcurve-properties.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 399 granskar 22 poster för FFmpeg-ljudinställningar: bithastighet,
kanalantal, mono/stereo/surround och ljudkodekar. Den använder *FFmpeg-ljudkodek*
som sammansatt teknisk term och skiljer mellan ljudutdata och själva renderingen.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-399-ffmpeg-audio-settings.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 400 granskar 23 poster för FFmpeg-videoinställningar: samplingsfrekvens,
videoutdata, buffertstorlek och videoformat/-kodekar. Den behåller etablerade
formatnamn och använder *FFmpeg-videokodek* som den svenska tekniska
sammansättningen. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-400-ffmpeg-video-settings.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 401 granskar 27 poster för FFmpeg-kodningens kvalitetsläge, hastighet och
ProRes-profiler. Den behåller det synliga codec-namnet *Constant Rate Factor
(CRF)* men gör dess svenska hjälpttext idiomatisk och använder *visuellt
förlustfri* för det perceptuellt förlustfria kvalitetsläget. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-401-ffmpeg-rate-and-prores.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 402 granskar 29 poster för FFmpeg-behållare, GOP-intervall, B-bildrutor,
muxning och bithastighetsgränser. Den normaliserar bland annat *container* till
*behållare*, *keyframe interval* till *nyckelbildruteintervall* och *max/min
rate* till högsta/lägsta bithastighet. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-402-ffmpeg-containers-and-rates.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 403 rättar först FFmpeg-hjälptexten för standardvalet och granskar sedan
36 poster för grundläggande F-kurvmodifierare: intoning, uttoning, påverkan,
generatorer, kuvert, cykler, brus, gränser och stegad interpolation. Den
normaliserar *F-Curve modifier* till *F-kurvmodifierare* och *Blend In/Out* till
*Tona in/ut*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-403-ffmpeg-correction-and-fcurve-modifiers.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 404 granskar 31 poster för F-kurvornas cykel- och kuvertmodifierare.
Den använder *Cykel-F-kurvmodifierare* och *Kuvert-F-kurvmodifierare*, gör
cyklingslägenas etiketter riktningstydliga och normaliserar
nyckelbildruteintervallets upprepningsbeskrivningar. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-404-fcurve-cycles-and-envelope.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 405 granskar 29 poster för F-kurvans funktions- och
generatormodifierare: matematiska funktioner, fas, additiv tillämpning,
koefficienter och polynom. Den använder bland annat *fasmultiplikator*,
*generatormodifierare* och *begränsningsmodifierare*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-405-fcurve-function-and-generator.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 406 granskar 24 poster för brusmodifierarens och den stegade
interpolationens parametrar, samt kuvertmodifierarens kontrollpunkt. Den
använder bland annat *slumpfrö*, *stegstorlek* och *kuvert-F-kurvmodifierare*.
De bredare, delade termerna *roughness* och *lacunarity* lämnas avsiktligt till
en senare tvärgående kontextgranskning. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-406-fcurve-noise-and-stepped.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 407 granskar sex grundposter för F-kurvans brusmodifierare och
normaliserar den till den projektspecifika termen *brusmodifierare*. De delade
shadertermerna *roughness* och *lacunarity* omfattas inte av batchen utan
väntar på bredare kontextgranskning. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-407-fcurve-noise-basics.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 408 gör den tvärgående kontextgranskningen av *roughness* och
*lacunarity*. Blenders svenska manual använder *grovhet* respektive
*lacunaritet*, vilket nu också är dokumenterat i projektets termlista.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-408-fcurve-noise-roughness-and-lacunarity.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 409 granskar 13 grundposter för fysikens fältinställningar: partikelns
position och rotation, räckvidd, avtagande, sfär och effektorflöde. Den följer
den etablerade terminologin *fältets avtagande* och *effektor*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-409-physics-field-basics.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 410 granskar 17 poster för hårguiders klumpning och nyckning. Den
använder *grad av klumpning*, *klumpningens form* och *nyck* konsekvent, samt
förtydligar den guidefria tiden som tiden före slutet av partikelns livstid.
Deltafilen
`blender-ui-sv-reviewed-20261106-batch-410-hair-guide-clumping-and-kink.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 411 granskar 32 parametrar för kraftfält: harmonisk dämpning,
motstånd, brus, radiellt avtagande, vilolängd, fältets ursprung och
domänobjekt. Den normaliserar bland annat *exponent för radiellt avtagande*,
*vilolängd* och *hörnpunkt*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-411-physics-field-parameters.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 412 granskar 47 poster för kraftfältens textur- och fälttyper,
koordinater, avtagande och kraftbegränsningar. Den bevarar det tekniska
lägesnamnet *Curl* i vektoranalyskontext, använder *rottexturkoordinater* och
formulerar övriga hjälptexter utan engelska låneord. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-412-physics-field-types-and-modes.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 413 granskar 20 resurs- och filvalsfilter. Den använder konsekvent
*datablock*, sammansatta typnamn som *cachefilsdatablock* och projektets
etablerade namn *Freestyle-linjestil* och *ljussond*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-413-file-asset-filters.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 414 granskar 24 poster för filbläddrarens bokmärken, filhanterarens
API-hjälptexter och filtyper. Den bevarar kodidentifierare som
`bl_file_extensions` och `bl_idname`, men normaliserar bland annat
*bildremsa*, *filmremsa* och *resursdata*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-414-file-browser-and-handlers.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 415 granskar sju ID-filter och kategorier i filbläddraren. Den använder
*ID-filter för filval*, behåller Blendertermen *mesh* och normaliserar
Freestyle-sammansättningen till *Freestyle-linjestilar*. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-415-file-browser-id-filters.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 416 granskar åtta sök- och sorteringsposter i filbläddraren: skalmönster,
ID- och etikettfilter samt resurskatalogernas sorteringsregler. Den använder
*Unix-skal-liknande*, *avgränsade med* och *plattad kataloghierarki* i den
tekniska hjälptexten. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-416-file-browser-search-and-sorting.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 417 granskar sju poster för resursbläddrarens importmetoder. Den skiljer
tydligt mellan länkade och kopierade datablock samt beskriver återanvändning av
kapslade data utan att ändra Blenders tekniska innebörd. Deltafilen
`blender-ui-sv-reviewed-20261106-batch-417-asset-browser-import-methods.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 418 granskar tolv API-nära etiketter för geometriattributens flyttals-,
vektor- och matrisvärden. Den följer den etablerade termlistan för
*flyttalsattributvärde*, *geometriattribut* och *skrivskyddad vektor*.
Deltafilen `blender-ui-sv-reviewed-20261106-batch-418-geometry-attribute-values.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 419 granskar 18 Mantaflow-poster för gasdomänens adaptiva marginal,
flytkraft, cacheformat och återupptagbar bakning. Den använder *flytkraft från
densitet* respektive *flytkraft från värme*, bevarar formatnamnen *Uni Cache*
och *OpenVDB* samt normaliserar cachebeskrivningarna till *cachelagring*.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-419-fluid-domain-cache-and-buoyancy.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 420 granskar 16 Mantaflow-poster för cachelägen, CFL, volymklippning,
färgkartläggning och interpolation. I cachetypens konkreta UI-kontext används
*uppspelning* för *Replay*, medan *modulär* bevaras för stegvis bakning.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-420-fluid-cache-and-display.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 421 granskar 15 Mantaflow-poster för gasdomänens visning, röklösning,
flamrutnät och FLIP-parametrar. Den rättar särskilt manusbeskrivningens
missvisande *cacheminnet* och *visningsrutor* till *cachen* och *rutnät* samt
använder *lågrutnät* för det tekniska datafältet *Flame Grid*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-421-fluid-gas-display-and-flames.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 422 granskar 24 Mantaflow-poster för fraktionella hinder och
rutnätsvisning. Den normaliserar bland annat *celltyp*, *markeringsintervall*,
*färglägg rutnätslinjer* och den kontextspecifika termen *hindercell*.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-422-fluid-obstacles-and-gridlines.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 423 granskar tio Mantaflow-poster för vätskestyrning. Den följer den
etablerade termlistan för *vätskestyrning*, *styrningsdomän*, *styrningsobjekt*
och *effektor* samt förtydligar att styrningsobjekten används just för denna
simuleringsfunktion. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-423-fluid-guiding.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 424 granskar fem Mantaflow-poster för rökens värmedata och högupplöst
sampling. Den bekräftar *värmerutnät*, *rökens värmerutnät* och *närmaste*
samt förtydligar läget *Full Sample* till *fullständig provtagning*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-424-fluid-heat-and-sampling.po` är
lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 425 granskar tolv Mantaflow-poster för vätskemeshning. Den normaliserar
*meshgenerator*, *meshskala* och konkavitetsgränser och rättar den tidigare
missvisande översättningen av *union particle level set* till *unionens
partikelnivåmängd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-425-fluid-liquid-meshing.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 426 granskar 20 Mantaflow-poster för OpenVDB-komprimering,
partikelupplösning och rutnätsvisning. Den tar bort ett felaktigt kolon från
*Kompression*, använder *vätskedomän* i stället för det engelska lånordet
*fluiddomän* och skiljer *rutnätslinjer* från själva rutnätet. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-426-fluid-cache-particles-and-grid-display.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 427 granskar 17 Mantaflow-poster för FLIP/APIC-metoder, volymskivor och
sekundära partiklar vid domängränsen. Den bevarar de tekniska metodnamnen,
men rättar *skärriktning* till *skivriktning* och normaliserar skivkontrollerna
till *skivor per voxel*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-427-fluid-methods-slices-and-boundary-particles.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 428 granskar 15 Mantaflow-poster för sekundära partiklars flytkraft,
motstånd och export. Den följer den etablerade facktermen *motstånd* i stället
för den missvisande *dragkraft* och normaliserar exportetiketten till *samlad
export*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-428-fluid-secondary-particle-export.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 429 granskar 22 Mantaflow-poster för sekundära partiklars livslängd,
potentialer och provtagning. Den normaliserar konsekvent *övre/nedre
begränsningströskel*, *vågtoppscell* och *partikellivslängd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-429-fluid-secondary-particle-potentials.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 430 granskar 13 Mantaflow-poster för tidsskala, adaptiv domän,
adaptiva tidssteg och domängränskollisioner. Den normaliserar de riktade
gränserna till bestämda uttryck som *den vänstra domängränsen*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-430-fluid-timing-adaptive-domain-and-borders.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 431 granskar 23 Mantaflow-poster för visning, diffusion, rökupplösning,
fraktionella hinder, partikeltyper och viskositetslösaren. Den ersätter
onödiga engelska *mappa* med *färgkartlägga*, använder konsekvent
*fraktionella hinder* och rättar *skärning* till *skiva* i volymvisningens
kontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-431-fluid-display-and-features.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 432 granskar 21 Mantaflow-poster för hastighets- och vektorfältsvisning,
MAC-rutnät, rörelseoskärpa, viskositet och vorticitet. Den etablerar *belopp*
för vektorstorlek, *vätskehastighet* och *styrhastighet* för de olika
hastighetsfälten samt rättar viskositetsbasens potensuttryck. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-432-fluid-vectors-and-viscosity.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 433 granskar 17 Mantaflow-poster för effektorers kollision, styrning,
bildruteinterpolering och avstånd till meshyta. Den normaliserar
*styrningsobjekt*, förtydligar att gränsavståndet räknas som en del av
effektorn och dokumenterar terminologin för *effektorobjekt*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-433-fluid-effectors.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 434 granskar 40 Mantaflow-poster för flödeskällor, rök, eld, vätska,
emission, texturkoordinater och initiala hastigheter. Den använder konsekvent
*emission* och *emitteras* för flödesobjektens utsändning och skiljer
*ytemission* från *volymemission*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-434-fluid-flow-sources.po` är lokalt
kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 435 granskar 31 Freestyle-poster för linjeuppsättningars samlingar,
urvalslogik och kanttyper. Den etablerar *funktionskant*, *veckkant* och
*materialgräns*, samt gör de motsatta urvalslägena konsekvent inkluderande
respektive exkluderande. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-435-freestyle-line-set-edge-types.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 436 granskar 42 Freestyle-poster för ytmarkeringar, synlighet,
silhuetter och kanturval. Den ersätter felaktig *ansiktsmärkning* med
*ytmarkeringar*, använder *veckkanter* konsekvent och rättar den tidigare
oidiomatiska beskrivningen av skymmande och skymda objekt. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-436-freestyle-face-marks-and-visibility.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 437 granskar 30 Freestyle-poster för stilmoduler, renderingspass,
veckvinkel, vykarta och stilparametrar. Den gör *veckkanter* konsekvent med
föregående batch, ersätter den svårlästa formen *Kr Derivat Epsilon* med
*epsilon för Kr-derivatan* och normaliserar *åsar och dalar*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-437-freestyle-style-modules-and-settings.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 438 granskar 38 Blender-poster för anteckningsbildrutor,
anteckningslager, interpolation och lökskalning. Den rättar den otydliga
fysiska betydelsen *ram för anteckningar* till den animeringsspecifika
*anteckningsbildruta* och gör lökskalningskontrollerna konsekventa. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-438-annotation-frames-and-layers.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 439 granskar 22 Grease Pencil-poster för ritningshjälplinjer,
referenspunkter, rutnät och snäppning. Den ersätter de engelsknära formerna
*guide* och *hastighetsguide* med den funktionsbeskrivande termen
*ritningshjälplinje*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-439-grease-pencil-drawing-guides.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 440 granskar 32 Blender-poster för gizmor, deras matriser,
visning, händelser och verktygstips. Den normaliserar *gizmogrupp*,
*förskjutningsmatris*, *världsmatris* och *djupförskjutning* enligt den
projektspecifika termlistan. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-440-gizmo-controls-and-matrices.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 452 granskar 15 poster för Rigifys widgetsamling samt armaturers
visnings- och penselinställningar. Den förtydligar att speglingen träffar
motsvarande ben på X-axelns andra sida och rättar områdesradien från en
felaktig hänvisning till områdesplanets djup till områdets mittpunkt.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-452-rigify-armature-brush.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 453 granskar 13 penselposter för automaskering av meshgränser och
håligheter. Den ersätter den inkonsekventa termen *kavitetsmask* med den
projektspecifika termen *hålighetsmask* och gör beskrivningen av maskens
oskärpning idiomatisk. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-453-brush-automasking.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 454 granskar 38 penselposter för färgblandningslägen, alfa och
oskärpning. Den följer terminologins etablerade blandningslägen, bland annat
*Färgbränn*, *Färgskugga*, *Levande ljus* och *Punktljus*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-454-brush-blending-modes.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 455 granskar 38 penselposter för deformation, gränsavtagande och
tygsimulering. Den behåller de etablerade UI-termerna *nypunkt*, *ormkrok* och
*simuleringsavklingning* samt rättar den engelsknära etiketten *Loopa och
invertera* till *Slinga och invertera*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-455-brush-deformation-and-cloth.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 456 granskar 29 poster för penselns avtagandekurvor, kurvskulptering,
streck och deformationsmål. Den återanvänder kurvförinställningarnas svenska
värden mellan pensel-, UV- och modifierarkontexter och bekräftar
*streckförhållande* samt *strecklängd* i penselinställningarna. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-456-brush-curves-and-dashes.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 457 granskar 14 penselposter för riktning, elastisk deformation och
avtagande. Den bekräftar de kontextspecifika UI-termerna *avtagandevinkel*,
*avtagandeform*, *Poisson-tal* och *Flytta i två/tre skalor*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-457-brush-direction-and-falloff.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 458 granskar 27 Grease Pencil-poster för skulptering, punktfärg och
viktmålning. Den bekräftar *streckpunkter*, *hörnpunktsgrupp*, *nyp*, *smeta*
och *ormkrok* i deras verktygskontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-458-grease-pencil-sculpt-tools.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 459 granskar 34 penselposter för toning, tryckmodulering, variation och
maskschabloner. Den normaliserar den inkonsekventa formen *filsökväg* till
*filväg* för penselikonen och bekräftar *masktexturplats* i penselkontexten.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-459-brush-pressure-jitter-and-masks.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 460 granskar 36 penselposter för plan, poseringsdeformation och
ytuppsättningar. Den rättar det missvisande *toppar* till *hörnpunkter* för
meshens vertexar och normaliserar *FK-deformation* i poseringsverktygets
hjälptext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-460-brush-planes-and-pose.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 461 granskar 41 poster för skulpteringspenslar, deras plan och
utjämning. Den normaliserar *Boundary* till *Gräns* och använder den
terminologiskt fastställda formen *sprutpistolen* i Airbrush-hjälptexten.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-461-sculpt-brush-tools.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 462 granskar 42 penselposter för streckmetoder, spets, texturprov och
topologisk krattning. Den bekräftar *penselavtryck*, *penselspets*,
*topologisk krattning*, *lågpoly-mesher* och *oprojicerad radie* i deras
respektive UI-kontexter. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-462-brush-strokes-and-tips.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 463 granskar 18 automaskeringsposter för meshgränser, håligheter,
ytuppsättningar, normaler och ocklusion. Den återanvänder konsekvent
*automaskering*, *hålighetsmask*, *ytuppsättningsgräns* och *meshgräns*.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-463-brush-automasking-protection.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 464 granskar 25 penselposter för framåtvända ytor, tryck, ursprungsplan
och radieenheter. Den ersätter den oidiomatiska formen *Inverst jämnt tryck*
med *Omvänt utjämningstryck* och bekräftar *radieenhet* i penselkontexten.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-464-brush-frontface-and-pressure.po`
är lokalt kontrollerad men ännu inte manuellt importerad till Blender Translate.

Batch 537 granskar 23 partikelposter för modifieringsstapel, massa, föräldrar,
grovhet, instansskala, egenpåverkan, storleksavböjning, strårendering,
vridning, samlingar, utsläpp per yta och virtuella föräldrar. Den bekräftar
*samling*, *yta* och *virtuella föräldrar* enligt projektets terminologi,
ersätter den oidiomatiska etiketten *Storlek Avböjning* med
*storleksavböjning* och rättar *strandprimitiv* till *stråprimitiv* i
hårpartikelkontexten. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-537-particle-controls-and-collections.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-537.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 538 granskar 22 poster för scenens ljudmodell och bakgrundsdata:
avståndsdämpning, inversa, linjära och exponentiella modeller,
Dopplerfaktor, ljudhastighet, bakgrundsscen, aktiv kamera och rotsamling.
Den rättar *Exponent* till *Exponentiell* och den missvisande
*tonskalfaktor* till *tonhöjdsfaktor*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-538-scene-audio-and-background.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-538.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 539 granskar sju poster för scenens renderare och visningsinställningar.
Den behåller produktnamnen *Cycles* och *EEVEE*, rättar den felaktiga
betydelsen *cykliska kurvor* till *Cycles-kurvor* och skriver om den otydliga
enhetsbeskrivningen till idiomatisk svenska. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-539-scene-renderers-and-display.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-539.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 540 granskar 12 poster för scenens bildrutor och
förhandsgranskningsintervall. Den använder *delbildruta* konsekvent,
normaliserar *tidsomappning* och rättar de felaktiga formerna *slutram* och
*startbild* till *slutbildruta* respektive *startbildruta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-540-scene-frames-and-preview.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-540.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 541 granskar sju poster för Grease Pencil-anteckningar och
Hydra/Hydra Storm. Den bekräftar *anteckningar* och *Grease Pencil-datablock*
i 3D-vy-kontexten samt behåller produktnamnen *Hydra* och *Hydra Storm*.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-541-scene-annotations-and-hydra.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-541.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 542 granskar 17 Scene-poster för nyckeluppsättningar, låst
bildruteval, kompositionsnodträd, renderingsdata, sekvensredigerarens
färgrymd, delbildrutor och simuleringsintervall. Den normaliserar
*kompositionsnodträd* och ersätter felaktig *ram* med *bildruta* i
animeringskontexten. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-542-scene-keys-sequencer-and-simulation.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-542.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 543 granskar 19 Scene-poster för uppspelningssynkronisering,
bildrutehoppning, transformeringsorientering, enheter, ljud, simulering,
förhandsgranskning och färghantering. Den ersätter den oidiomatiska etiketten
*Tappa rutor* med *Hoppa över bildrutor* och normaliserar
*bildruteintervall* i stället för den fysiska betydelsen *ram*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-543-scene-playback-and-ranges.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-543.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 544 granskar 11 Scene-poster för ljudskrubbning och OpenXR. Den ersätter
engelska *Sequence Editor*, *scrubbing*, *Controller Actions*, *runtimes*,
*input* och *gamepad* med kontextuella svenska former, men behåller
produktnamnen för styrenhetsmodellerna. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-544-scene-audio-scrubbing-and-openxr.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-544.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 545 granskar 13 poster för skärmdatablock, områden, animeringsuppspelning,
skrubbling och berörda redigerare. Den ersätter det engelska
*Screen data-block*, korrigerar *skrubbar sig igenom tiden* till
*skrubbar genom tidslinjen* och normaliserar bestämd form i redigerartext.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-545-screen-layout-and-editors.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-545.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 546 granskar 22 poster för högtalarobjektets ljuddatablock,
avståndsdämpning, riktningskoner, referensavstånd, tonhöjd och volym. Den
normaliserar *Pitch* till *tonhöjd* och *Mute* till *Tysta* i högtalarkontexten
samt skriver om konbeskrivningarna till idiomatisk svenska. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-546-speaker-distance-and-volume.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-546.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 547 granskar 16 poster för Text-datablock, tecken- och radpositioner,
urval samt registrering av Python-skript. Den behåller API-typen *TextLine*
men använder svenska former för markering och radindex, samt rättar den
felaktiga etiketten *Välj index för ändraden*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-547-text-editor-selection-and-script.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-547.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 548 granskar fem grundposter för Textur-datablocket: dess användning i
material, ljus, världar och penslar, RGB-faktorer samt nodträd. Den rättar den
engelska ordföljden *Faktor Blå/Grön/Röd* till *Blå/Grön/Röd faktor*.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-548-texture-basics.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-548.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 549 granskar fem poster för äldre procedurtexturer och deras
intensitetsinställningar. Den bevarar egennamnen *Musgrave*, *Stucci* och
*Voronoi*, följer termbasens *färggradient* i stället för *färgramp* och
återanvänder den synliga UI-etiketten *Beräkna alfa*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-549-procedural-texture-terms.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-549.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 550 granskar 37 poster för nodgruppen *Braid Hair Curves*: guideindex,
guideindexkartor, flätans radie, hårstrånas tjocklek, utsvängning och
hårsnodd. Den ersätter den felaktiga generella *sträng* med hårkontextens
*strå*, använder termbasens *guideindexkarta* genomgående och rättar den
ofullständiga etiketten *Tjocklek* till *Tjockleksform*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-550-braid-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-550.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 551 granskar 11 poster för tillgången *Curl Hair Curves*: hårkurvor
som formas till lockar kring guidekurvor, lockningsstart, radie, frekvens och
slumpvariation. Den rättar etiketten *Faktor Start* till *Startfaktor*,
normaliserar *Lockningens start* och använder *åtgärd* i stället för det
onödiga engelska lånet *operation*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-551-curl-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-551.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 552 granskar 18 poster för *Roll Hair Curves*, som rullar upp
hårkurvornas spetsar och kan behålla deras ursprungliga flöde. Den använder
*rullningsbana*, *rullradie*, *rulldjup*, *rullkona* och *rullningsriktning*
konsekvent och förtydligar utjämningsinställningens funktion. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-552-roll-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-552.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 553 granskar åtta poster för *Frizz Hair Curves* och hårkurvsbrus:
slumpmässiga små förskjutningar som ger en frissig form. Den använder
*förskjutningsvektor*, *ackumulerad förskjutning* och *avståndsfaktor* och
rättar den missvisande formuleringen *krusa* till *gör hårkurvor frissiga*.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-553-frizz-hair-curves.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-553.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 554 granskar tio poster för *Hair Curves Noise*, noden som deformerar
hårkurvor med en procedurbaserad brustextur. Den rättar det felaktiga
*Hårkurvor Buller* till *Hårkurvsbrus*, ersätter engelska *Offset* med
*Förskjutning* och normaliserar skalningstexterna. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-554-hair-curves-noise.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-554.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 555 granskar sju poster för *Smooth Hair Curves*, som jämnar ut
hårkurvors form genom upprepade beräkningar. Den gör reglagen tydligare med
*utjämningsgrad*, *antal utjämningssteg* och *vikt för utjämning* samt rättar
hjälptexten så att alla spetsars position låses. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-555-smooth-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-555.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 556 granskar tre poster för *Straighten Hair Curves*, som riktar varje
hårkurva längs en linje mellan rot och spets. Den ersätter det oidiomatiska
*Mängd uträtning* med *Uträtningsgrad*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-556-straighten-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-556.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 557 granskar tolv poster för *Trim Hair Curves*, som kortar eller
skalar hårkurvor till en bestämd längd. Den rättar *Längd Faktor* till
*Längdfaktor*, använder *Förankra* när en kurva fixeras vid en parameter och
skriver *åtgärd* i stället för *operation*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-557-trim-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-557.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 558 granskar åtta poster för *Rotate Hair Curves*: rotationsvinkel,
rotationsaxel och slumpvariation per hårkurva. Den förtydligar att den låser
kurvans **ändpunkter**, inte obestämda ändar. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-558-rotate-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-558.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 559 granskar elva poster för *Shrinkwrap Hair Curves*, som anpassar
hårkurvor efter en meshyta. Den behåller Blenders funktionsnamn *Shrinkwrap*
enligt terminologin, men ersätter engelska *Offset* med
*Förskjutningsavstånd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-559-shrinkwrap-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-559.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 560 granskar tolv poster för *Displace Hair Curves*, vektorstyrd
förskjutning av hårkurvor i objektrymd eller efter en ytnormal. Den
normaliserar *den övergripande förskjutningen* och bevarar etablerade termer
som *förskjutningsvektor* och *ytgeometri*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-560-displace-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-560.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 561 granskar elva poster för *Clump Hair Curves*, som grupperar
hårkurvor kring guidekurvor. Den använder *klumpning*, *guidekurva*,
*guideindexkarta* och *slumpfrö* i enlighet med terminologin och ersätter
engelska *operation* med *åtgärd*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-561-clump-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-561.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 562 granskar sju poster för *Create Guide Index Map*, som skapar ett
attribut som kopplar varje hårkurva till närmaste guidekurva. Den ersätter den
felaktiga frasen *Styr kurvorna* med *Guidekurvor*, och normaliserar
*guideurval* och *guideindexkarta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-562-create-guide-index-map.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-562.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 563 granskar nio poster för *Curve Info*, som läser data om varje
hårkurva. Den normaliserar den felaktiga särskrivningen *Kurva Index* till
*kurvindex* och använder *ytinfästningens UV-koordinater* för det UV-värde som
hör till en kurvas fästpunkt. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-563-curve-info.po` och den ersättande
samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-563.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 564 granskar nio poster för *Curve Root*, som läser en hårkurvas
rotpunkt, rotsegment och rotindex. Den använder *roturval* i stället för den
otydliga frasen *markering av rötter*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-564-curve-root.po` och den ersättande
samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-564.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 565 granskar elva poster för *Curve Segment* och *Restore Curve Segment
Length*. Den rättar den missvisande pluralformen *Index för grannar* till
*grannindex* och bevarar terminologin för kurvsegment, referensposition och
deformation. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-565-curve-segments.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-565.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 566 granskar nio poster för *Curve Tip*, som läser hårkurvornas
spetspunkter. Den normaliserar *spetsurval*, *spetspunkt* och den korrekta
formen *booleskt* i stället för *booleanskt*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-566-curve-tip.po` och den ersättande
samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-566.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 567 granskar elva poster för *Hair Attachment Info*, som läser
hårkurvornas fäste vid en meshyta. Den gör *meshyta* och *meshytans
normalriktning* konsekventa med terminologin och uppdaterar även
terminologiposterna för hårinfästning. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-567-hair-attachment-info.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-567.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 568 granskar sjutton poster för *Attach Hair Curves to Surface*. Den
normaliserar *ytmesh* till *meshyta* och granskar UV-fäste, snäppning mot
ytan, ytnormal och viloposition i den faktiska nodkontexten. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-568-attach-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-568.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 569 granskar fem poster för *Blend Hair Curves*, som medelvärdesbildar
närliggande hårkurvors form inom en radie. Den gör reglaget till den
substantiviska termen *blandningsgrannar* och använder *grannkurvor* i
beskrivningen. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-569-blend-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-569.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 570 granskar tio poster för *Duplicate Hair Curves*, som skapar
hårkurvsdubbletter runt guidekurvor. Den använder *dubbletter*,
*fördelningsform* och *guidekurvor*, och förtydligar att jämn tjocklek
bibehålls i fördelningen. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-570-duplicate-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-570.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 571 granskar tretton poster för *Generate Hair Curves*, som skapar
hårkurvor från nya punkter på en meshyta. Den normaliserar *densitetsmask*,
*Poisson-diskfördelning* och *3D-vyport*, och dokumenterar de två återkommande
fördelningstermerna i terminologilistan. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-571-generate-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-571.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 572 granskar elva poster för *Interpolate Hair Curves*, som bygger nya
hårkurvor utifrån befintliga guidekurvor. Den rättar den felaktiga
*huvudledarkurva* till *huvudguidekurva*, använder *meshöar* för separata
sammanhängande ytområden och uppdaterar terminologilistan för båda begreppen.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-572-interpolate-hair-curves.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-572.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 573 granskar fyra poster för *Redistribute Curve Points*, som
omfördelar befintliga kurvkontrollpunkter jämnt. Den behåller den etablerade
termen *detaljbevarande* för den enkla algoritm som ska skydda lokala
kurvdetaljer och riktningsändringar. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-573-redistribute-curve-points.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-573.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 574 granskar posten för *Restore Curve Segment Length*, som återställer
varje kurvsegments ursprungliga längd med ett tidigare, odistorserat tillstånd
som referens. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-574-restore-curve-segment-length.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-574.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 575 granskar beskrivningen av *Roll Hair Curves*, som rullar hårkurvor
inåt från spetsarna. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-575-roll-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-575.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 576 granskar åtta poster för *Set Hair Curve Profile*, som styr
hårkurvornas radie längs deras längd med en profil. Den normaliserar
*hårkurvprofil*, *Ersätt radie* och de närliggande radiereglernas texter.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-576-set-hair-curve-profile.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-576.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 577 granskar nodnamnet *Braid Hair Curves*. Den bekräftar
*Fläta hårkurvor* för verktyget som formar befintliga hårkurvor till flätor
med guidekurvor. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-577-braid-hair-curves.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-577.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 578 granskar beskrivningen av *Blend Hair Curves*. Den klargör att
verktyget blandar formen hos näraliggande hårkurvor inom en angiven radie.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-578-blend-hair-curves.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-578.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 579 granskar beskrivningen av *Curve Root*, noden som läser data från
varje hårkurvas rotpunkt. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-579-curve-root-description.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-579.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 580 granskar beskrivningen av *Curve Segment*, noden som läser data om
varje kurvpunkts föregående kurvsegment. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-580-curve-segment-description.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-580.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 581 granskar beskrivningen av *Curve Tip*, noden som läser data från
varje hårkurvas spets. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-581-curve-tip-description.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-581.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 582 granskar beskrivningen av *Generate Hair Curves*. Den rättar den
engelskpåverkade sammansättningen *ytmesh* till *meshyta*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-582-generate-hair-curves-description.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-582.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 583 granskar beskrivningen av *Set Hair Curve Profile*, som anger
radieattributet för hårkurvor med en profilform. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-583-set-hair-curve-profile-description.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-583.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 584 granskar två hårkurvsbeskrivningar: *Braid Hair Curves* formar
befintliga hårkurvor till flätor med guidekurvor, och *Redistribute Curve
Points* fördelar kontrollpunkterna jämnt längs varje kurva. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-584-hair-curve-descriptions.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-584.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 585 granskar *Animation Visualization* och dess hjälptext för
inställningar som visualiserar rörelse. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-585-animation-visualization.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-585.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 586 granskar B-Bones starthandtagstyp och hjälptexten för hur handtaget
beräknas. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-586-bbone-start-handle.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-586.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 587 granskar Action slots i animeringsdata. Den normaliserar
*åtgärdsslot* och *åtgärdsslotar*, och rättar den felaktiga *åtgärdsluckor* i
meddelandet om lagerindelade åtgärder. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-587-action-slots.po` och den ersättande
samlingsfilen `blender-ui-sv-reviewed-20261107-post-upload-batches-287-587.po`
är lokalt kontrollerade och arkiverade, men deras import till Blender Translate
är inte verifierad i detta arkiv.

Batch 588 granskar sexton Cycles-inställningar för beräkningsenheter,
kärnoptimering, hårdvarustrålspårning och delat GPU-minne. Produkt- och
tekniknamnen *MetalRT*, *HIP RT*, *Embree*, *RDNA2* och *NVLink* behålls.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-588-cycles-device-and-kernel-settings.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-588.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 589 granskar sju tygfysikinställningar för kollision, kompressionsfjädrar
och kompressionsstyvhet. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-589-cloth-compression-settings.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-589.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 590 granskar tygfysikens Målvolym och sömnad. Den ersätter den
engelskpåverkade *initial volym* med *startvolym* och förtydligar *Sy ihop
tyg*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-590-cloth-volume-and-sewing.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-590.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 591 granskar Grease Pencil-reglaget för fyllningsgränsens noggrannhet.
Högre värden ger noggrannare men långsammare fyllning. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-591-grease-pencil-fill-boundary.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-591.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 592 granskar tygsimuleringens hörnpunktsgrupper för sömnad, böjstyvhet,
interna fjädrar, fastsättning och tryck. Den följer projektets etablerade term
*hörnpunktsgrupp*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-592-cloth-vertex-groups.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-592.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 593 granskar färghanteringens visningsenhet, färgrymd och scenlinjära
färgrymd. Termerna följer Blenders färghanteringsmodell och den lokala
terminologilistan. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-593-color-management-display-settings.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-593.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 594 granskar Blender Extensions-tilläggsförråd, paketidentifierare och
installationsmål. Den rättar bland annat felaktig *Kolli-ID* och den helt
felaktiga *Temporär katalog*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-594-extension-repositories.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-594.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 595 granskar filbläddrarens resurspaketering, bokmärken,
kataloghantering och filborttagning. Den använder *återvinningskorgen* i stället
för den felaktiga *återvinningsfacket*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-595-file-browser-bookmarks.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-595.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 596 granskar filbläddrarens externa filåtgärder och rättar bland annat
felaktiga mapptexter från ett orelaterat tillståndsgränssnitt. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-596-file-browser-external-operations.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-596.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 597 granskar de externa filåtgärdernas visning, uppspelning, bläddring,
utskrift, installation, kommandotolk och egenskapsdialog. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-597-file-browser-external-operation-options.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-597.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 598 granskar filbläddrarens filväljare, saknade filer, sökvägar,
paketering av externa resurser och katalognavigering. Den rättar bland annat
*banor* och *vägarna* till tekniskt korrekta *sökvägar*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-598-file-browser-navigation-and-packaging.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-598.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 599 granskar filmarkering, mjuk rullning, sortering och uppackning av
inbäddade resurser. Den följer termbasen med *packad* för *packed* och rättar
bland annat felaktiga *border*, *scrollning* och *förpackningen*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-599-file-browser-selection-and-unpacking.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-599.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 600 granskar Mantaflows bakning och rensning av simuleringscache för
data, vätskestyrning, mesh, brus och partiklar. Den ersätter bland annat de
helt felaktiga formerna *Gratis Alla* och *Bake Fluid Data*. Termbasen har
utökats med *vätskemesh*, *vätskebrus* och cachebetydelsen av *Free*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-600-fluid-cache-baking.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-600.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 601 granskar textobjektens skiftläge, teckenkod och teckenavstånd. Den
skiljer korrekt mellan *gemener*, *versaler*, *tecken* och *teckenstorlek*.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-601-font-case-and-spacing.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-601.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 602 granskar textobjektens markörnavigering, markering, stil och
Unicode-inmatning. Den rättar bland annat *Nästa linje*, *Förgående sida*,
*Flytta Välj* och *Tydlig stil*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-602-font-text-navigation-and-style.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-602.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 603 normaliserar de återanvända animations- och sekvensredigerartermerna
*Mute* till *Tysta* och *Strips* till *Remsor*, i enlighet med termbasens
kontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-603-animation-mute-and-strips.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-603.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 604 granskar glTF-tilläggets inställningstexter. Den behåller tekniska
identifikatorer och formatnamn oförändrade, men normaliserar Blender-termerna
*Material Output*, *Shader Editor* och menyalternativet *Output* till
*Materialutdata*, *shaderredigerare* respektive *Utdata*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-604-gltf-addon-preferences.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-604.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 605 granskar Cycles inställningar för kärnoptimering. *Intersection
only*, *Full* och den automatiska metoden har korrekta kontextuella svenska
översättningar och har därför markerats som granskade utan betydelseändring.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-605-cycles-kernel-optimization.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-605.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 606 granskar återanvända etiketter för panelplacering, RNA-typer och
resursbibliotek. *Bottom*, *Any Type*, dess RNA-beskrivning och *All Libraries*
har rätt respektive kontextuella svenska former och har markerats som
granskade. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-606-general-rna-and-assets.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-606.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 607 granskar RNA-informationen om beroendegrafens uppdateringar. Den
behåller den etablerade termen *beroendegraf* och rättar beskrivningen till
den idiomatiska formen *Information om det ID som uppdaterades*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-607-dependency-graph-update.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-607.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 608 granskar den delade reglagetexten för ljusstyrka. Den tidigare
översättningen begränsade felaktigt reglaget till texturer, trots att den även
används för färgmappning. Texten är nu den kontextneutrala *Justera
ljusstyrkan*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-608-shared-brightness-control.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-608.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 609 granskar Curve Profile-punktens beskrivning. *Bana* används här för
profilens definierande path och ger en korrekt, neutral UI-beskrivning.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-609-curve-profile-point.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-609.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 610 granskar Cycles- och bake-passens komponentetiketter. *Emit*,
*Direct* och *Indirect* har de korrekta svenska formerna *Emittera*, *Direkt*
och *Indirekt* i denna UI-kontext. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-610-cycles-bake-pass-labels.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-610.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 611 normaliserar *Brush Settings* och *Brush settings* till
*Penselinställningar*. Termbasen har uppdaterats för att förhindra den
inkonsekventa formen *Inställningar för borstar*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-611-brush-settings.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-611.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 612 granskar Dynamic Paint, punktcache, kurvkartläggning, benrotation
och gemensamma RNA-etiketter. Alla nio poster har korrekta och kontextuellt
entydiga svenska översättningar; *kurvkartläggning* följer termbasen.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-612-dynamic-paint-and-rna-labels.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-612.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 613 granskar Dope Sheets fel-, sammanfattnings- och linjestilsfilter.
De svenska UI-formerna är korrekta i animationskontexten och har markerats som
granskade utan betydelseändring. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-613-dope-sheet-filters.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-613.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 614 granskar Dope Sheets filter för den aktiva slotten. Den följer
termbasens tekniska term *slot* och förbättrar ordföljden till *Visa endast det
aktiva objektets slot*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-614-active-object-slot.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-614.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 615 granskar Grease Pencil-skulpteringsinställningar, axellås och
styrkurvor. *Align* normaliseras till det riktningsspecifika *Rikta* när
strecken anpassas till ett vyplan eller en 3D-markörs orientering. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-615-grease-pencil-sculpt-settings.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-615.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 616 granskar Grease Pencil-automaskering, avtagande och strecktjocklek.
De svenska formerna är konsekventa med den etablerade pensel- och
streckterminologin och har markerats som granskade. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-616-grease-pencil-automasking.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-616.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 617 granskar Grease Pencil-annoteringar, streckpunkter och koordinater.
Sammansättningarna *anteckningsstreck*, *anteckningsstreckpunkt* och
*frihandskurva* är sakliga i Blenders datamodell. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-617-grease-pencil-annotations.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-617.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 618 granskar GizmoGroup-API:ts operatörstexter. API-namnet behålls
oförändrat, medan förklarande text normaliseras till *körs*, *efter körning*,
*skala efter zoomnivån* och presensformen *skyms*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-618-gizmo-group-api.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-618.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 619 granskar armaturers bensamlingar, visningsformer och poser. Den
rättar armaturtermen *Envelope* till termbasens *Omslutning* och kontrollerar
viloposition, poseringsläge, B-Bone och redigeringsläge. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-619-armature-display-and-poses.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-619.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 620 granskar armaturens relationslinjer. Den förtydligar den överordnade
och underordnade benrelationen i startpositionsbeskrivningen och bekräftar
övriga korrekta etiketter. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-620-armature-relation-lines.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-620.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 621 granskar Rigifys slutskript, widgetar, målrigg och namngivning. Den
följer termbasens former *rigg*, *metarigg*, *widgetmesh* och *slutskript*, och
behåller kodvärdena `metarig`, `rig`, `META`, `RIG` och `RIG-` oförändrade.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-621-rigify-target-and-widgets.po` och
den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-621.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 622 granskar penselinställningen *Auto-Smooth*. Den svenska termen
*Automatisk utjämning* och dess beskrivning är korrekta i penseldragskontexten.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-622-brush-auto-smooth.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-622.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 623 granskar objektens föräldrarelationer till objekt, gitter,
hörnpunkter och ben. Den följer den etablerade termen *föräldrarelation*;
hörnpunktsindexens särskilda hjälptext lämnas för separat kontextgranskning.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-623-object-parenting-types.po` och den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-623.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 624 granskar pose, styv kropp och partikelinstansiering. *Pose* behålls
som den etablerade Blender-etiketten; *styv kropp*, *instansobjekt* och
*slumpmässig storlek* följer termbasen. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-624-pose-rigid-body-and-particles.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-624.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Batch 625 granskar scenens aktiva filmklipp för rörelsespårning och
kamerabakgrund. *Aktivt filmklipp* är korrekt och kontextuellt tydligt.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-625-active-movie-clip.po`
och den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-post-upload-batches-287-625.po` är lokalt
kontrollerade och arkiverade, men deras import till Blender Translate är inte
verifierad i detta arkiv.

Den samlade deltafilen
`blender-ui-sv-reviewed-20261107-all-changes-batches-287-625.po` innehåller
alla lokalt granskade ändringar i batch 287–625 och är klar för manuell import.

