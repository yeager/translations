# Blender UI – svensk terminologi

Den här listan gäller Blender UI på Blender Translate. Den är ett stöd för
granskning, inte en ersättning för strängens sammanhang: kontrollera alltid
operator, panel, tooltip, Python-identifierare och närliggande strängar innan
du ändrar en översättning.

Senast uppdaterad: 2026-11-06.

## Grundtermer

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| asset library | tillgångsbibliotek / resursbibliotek | Båda förekommer i den etablerade Blender-katalogen. Följ närliggande UI och ändra inte mekaniskt mellan dem. I Asset Browser och dess inställningsbeskrivningar används *resursbibliotek* för att stämma med de omgivande UI-etiketterna. I övrig längre förklarande text är *tillgångsbibliotek* den vanligaste befintliga formen. |
| Asset Browser | resursbläddrare | Följer den aktuella svenska UI-etiketten. Den äldre manualformen *tillgångsbläddrare* ska inte dras in i ny UI-nära dokumentation. |
| access token | åtkomsttoken | Skriv ihop. Förklarande rubriker får precisera typen: *biblioteksåtkomsttoken* respektive *förrådsåtkomsttoken*. |
| remote asset library | fjärranslutet resursbibliotek | Skriv ut relationen i löpande text; undvik *fjärrresursbibliotek*, som blir svårläst med tre r. |
| remote assets | fjärranslutna resurser | Nätåtkomliga resurser i Asset Browser och dess filter. Undvik *fjärrresurser*, som får tre r i följd. |
| cache directory | cachekatalog | Etablerad teknisk sammansättning i Blender. Skriv ihop i UI-etiketter och statusmeddelanden: *diskcachekatalog*, *standardcachekatalog*. |
| longitude / latitude (camera projection) | längdgrad / breddgrad | Vinklar i kamerans cylindriska och ekvirektangulära projektioner. |
| fisheye lens | fiskögeobjektiv | Kameraprojektion med extremt brett synfält; använd sammansättningen även för fiskögepolynom. |
| sensor fit | sensoranpassning | Anpassar kamerans bild och synfältsvinkel efter bildsensorns bredd eller höjd. |
| passepartout | passepartout | Den mörka överlagringen utanför bildområdet i kameravyn. |
| safe areas (camera) | säkra områden | Hjälplinjer för tv-titel och handling eller för mittbeskärning vid annat bildförhållande. |
| film gate | filmruta | Bildruta som anger den fysiska sensor- eller filmramen i kameravyn. |
| clipping distance | beskärningsavstånd | Kamerans närmaste eller bortre synliga gräns. |
| cache layer | cachelager | Lager i en Blender-cachefil. Skriv ihop, utan bindestreck. |
| prefetch | förhandsladdning | Läser in cache- eller animationsdata i förväg för snabbare uppdateringar. |
| Cycles Procedural cache | Cycles Procedural-cachen | Särskild cache för Cycles procedurbaserade inläsning. |
| object path | objektsökväg | Sökväg för ett objekt i exempelvis en Alembic-arkivfil. |
| bake (rendering/simulation) | baka / bakning | Behåll Blenders etablerade verb i procedur- och inställningstexter: *Baka till aktiv kamera*, *bakningsdata*. Det gäller inte köksbetydelsen. |
| normal space | normalrymd | Val av koordinatrymd för normaldata vid bakning. De konkreta alternativen skrivs *tangentrymd*, *objektrymd* och *världsrymd*. |
| screen space | skärmrymd | Koordinatrymd baserad på den aktuella vyportens skärmplan. |
| onion skinning | lökskalning | Animeringsvisning med spökbilder från närliggande bildrutor. Undvik bokstavliga former som *avskalning av lök*. |
| onion frame / ghost frame | lökskalsbildruta | Bildruta som visas före eller efter den aktuella bildrutan vid lökskalning. Undvik den missvisande formen *spökram*. |
| Grease Pencil 2D Layers / 3D Location | 2D-lager / 3D-position | Visningslägen som styr streckens djupordning. Använd *lager* i UI-kontext, och *3D-position* när det är den faktiska placeringen i 3D-rymden som avses. |
| Bake Location (motion paths) | beräkningsposition | Valet av benhuvud eller benspets när rörelsebanor beräknas. |
| scope name | scope-namn | Behåll den tekniska källtermen i GPU-felsökningens fångstalternativ. Det är namnet som skickas till `--debug-gpu-scope-capture`, inte Blenders bildanalysvy *Scopes*. |
| Resolution Scale | upplösningsskala | Etablerad UI-term för skalan av teckensnitt och knappar vid visning. |
| File Browser | filbläddrare | UI-beteckning för den editor som öppnar och sparar filer. Anpassa bestämd form i löpande text. |
| file handler | filhanterare | RNA-typ och utbyggnadspunkt som registrerar import-, export- och släpphantering för filer. Översätt inte till *handtag*. |
| File Handler Type | filhanterartyp | UI-etikett för typen av filhanterare. |
| Maximize Area | Maximera område | Operatörsnamn. *Område* avser här ett Blender-area, inte ett skärmområde i allmän mening. |
| 3D Viewport | 3D-vyport | Etablerad UI- och manualterm. |
| 3D View | 3D-vy | Förklaringstext för den synliga Blender-vyn; böj som *3D-vyns* i sammansatta led. |
| Console | konsol | Blenders inbyggda Python-konsol. RNA-beskrivningen *Space Console* använder formen *konsolens område*; `prompt` blir *kommandoprompt*. |
| Image Editor | bildredigerare | Redigeraren för bilder, UV-kartor, maskning och bildmålning. RNA-beskrivningen *Space Image Editor* använder formen *bildredigerarens område*. |
| UV Editor | UV-redigerare | Bildredigerarens läge för UV-redigering. |
| Info | informationsområde | Blender-området som visar rapporter, fel och operatörslogg. |
| NLA Editor | NLA-redigerare | Redigeraren för Nonlinear Animation-remsor och deras F-kurvor. |
| Timecode Style | tidskodstil | Inställning som bestämmer hur uppspelningens varaktighet visas. |
| System Memory | systemminne | UI-rubrik för uppskattad RAM-användning. |
| New Data | Nya data | Gäller nya Blender-datablock; inte *nya uppgifter*. |
| Color Picker Type | Färgväljarens typ | Följer den aktuella svenska UI-etiketten. |
| Header Position | rubrikposition | Följer UI-etiketten i Inställningar. Använd *rubrik* i närliggande manualtext för att undvika konkurrerande former. |
| Percentage | procentandel | UI-värde för faktorvisning. |
| Date Format | datumformat | UI-rubrik i Inställningar › Gränssnitt. Behåll konkreta formatmönster som `yyyy-mm-dd` och `dd/mm/yyyy` oförändrade. |
| Time Format | tidsformat | UI-rubrik i Inställningar › Gränssnitt. |
| 24-Hour / 12-Hour | 24-timmarsformat / 12-timmarsformat | Följer de aktuella UI-etiketterna. Klockexemplen `23:59` och `11:59 PM` är formatdata och ska inte lokaliseras. |
| Reduce Motion | Minska rörelse | Tillgänglighetsinställning som minskar gränssnittets animationer och rörelseeffekter. |
| Close Menu on Leave | Stäng meny när muspekaren lämnar den | Följer den aktuella UI-etiketten ordagrant; behåll den obestämda formen *meny*. |
| add-on / extension | tillägg | I Blender betecknar båda källtermerna samma utbyggbara funktion. Svenska använder samma form i singular och plural i korta UI-etiketter. I dokumentation som måste skilja undergruppen *add-ons* från samlingsnamnet *extensions* kan *tilläggsmoduler* användas för just undergruppen. |
| data-block | datablock | Skriv ihop. Behåll bindestrecket bara i bokstavliga API-namn. |
| runtime data | körtidsdata | Data som bara finns under aktuell Blender-körning och därför inte sparas i .blend-filen. |
| garbage collection | skräpinsamling | Automatisk frigöring av oanvända datablock; används i tekniska API-beskrivningar. |
| library weak reference | svag biblioteksreferens | Svag referens till ett datablock i en annan .blend-biblioteksfil. |
| object | objekt | Etablerad Blender-term. |
| collection | samling | Avser Blenders objektbehållare, inte en godtycklig lista. |
| collection exporter | samlingsexportör | Exportör som är kopplad till en specifik Blender-samling. |
| collection export handler | exporthanterare för samlingen | Hanterar konfigurerad export av en samling. |
| instance offset | instansförskjutning | Förskjutning från origo som används när en samling instansieras. |
| intersection priority | korsningsprioritet | Line Art-värde som bestämmer vilket objekt en korsningslinje hör till. |
| project | projekt | Avser Blenders projektkatalog och dess inställningar. |
| project settings | projektinställningar | Exempel: *Open Project Settings* → *Öppna projektinställningar*. |
| workspace | arbetsyta | Den etablerade UI-formen, exempelvis *Workspace* → *Arbetsyta*. |
| pie menu | cirkelmeny | Följer den aktuella svenska Blender-UI-katalogen. |
| Essentials | Grundresurser | Översatt UI-namn för Blenders medföljande resurser. I löpande text: *resursbiblioteket Grundresurser*. |
| Essentials Library | grundresursbiblioteket | Rubrik i manualen för det inbyggda biblioteket med *Grundresurser*. Använd inte detta för den fristående UI-etiketten *Essentials*, som är *Grundresurser*. |
| Cyclic | Cyklisk | Kurv- och splineinställning. Skriv vid behov *alternativet Cyklisk* för korrekt svensk kongruens. |
| endpoint clamping | slutpunktsinterpolation | NURBS-egenskap som gör att kurvan går genom den första och sista kontrollpunkten. Använd inte den otydliga allmänformen *begränsning vid slutpunkterna*. |
| Numeric Input Arrows | Numeriska inmatningspilar | Följer den faktiska svenska UI-etiketten. |
| application template | applikationsmall | Etablerad i den svenska manualen och i startskärmens dokumentation. |
| user preferences | användarinställningar | Gäller konfigurationsfil, inställningar och kommandoradsflaggor i manualen. UI-rubriken *Preferences* följer sin egen kontext. |
| extension repository | tilläggsförråd | Manualens etablerade term för Blenders paketkälla. Använd *fjärrförråd*, *användarförråd* och *systemförråd* när attributet är betydelsebärande. Behåll kommandon som `repo-info` exakt. |
| online asset repository | resursförråd på nätet | Nätbaserad källa för resurser. Skilj från *resursbibliotek*, som är den konfigurerade biblioteksplatsen i Blender. |
| Allow Online Access | Tillåt nätåtkomst | Etiketten i den aktuella UI-katalogen. Varianten *Tillåt onlineåtkomst* finns i ett separat operator-sammanhang; normalisera inte den utan att kontrollera kontexten. |
| timeout | tidsgräns | Exempel: *Animation Timeout* → *Animationstidsgräns*. |
| Link | Länk | Importmetodens UI-etikett. Använd verbet *länka* i löpande instruktioner, exempelvis *Länka resursen*. |
| Append | Lägg till | UI-operator och importmetod. I beskrivande text blir det participiala *tillagd*, exempelvis *tillagd kopia*. |
| blendfile | blendfil | Blenders egen filtyp i löpande svensk text. Skriv *.blend-fil* när filändelsen uttryckligen avses. |
| Blendfile Import Context | blendfilimportkontext | RNA-kontext för import, länkning och tillägg av data från blendfilsbibliotek. |
| source library | källbibliotek | Det bibliotek eller den blendfil som ett importerat datablock kommer från. |
| Append Action | tilläggsåtgärd | API-egenskap som anger hur ett ID hanterades när data lades till. |
| boid | boid | Etablerad simuleringsterm i Blenders flockningsfysik. Plural: *boider*. |
| Boid Rule | boidregel | Regel som styr en boids mål, undvikande, flockning eller strid. |
| banking | krängning | Rotation kring rörelseriktningen vid flygning eller sväng. |
| falloff | avtagande | Avtagande påverkan i fält, penslar och BoidState. |
| linked | länkad | Exempel: *linked object* → *länkat objekt*. |
| packed | packad | Exempel: *packed data-block* → *packat datablock*. |
| parent | förälder / överordnad | Kontextstyrt i Blender-hierarkin. Den fristående UI-egenskapen kan vara *Förälder*, medan objekt- och samlingshierarkier använder *överordnat objekt* eller *överordnad*. Normalisera inte mekaniskt. |
| Graph Editor | grafredigerare | UI-namn för redigeraren med F-kurvor. Använd bestämd form i löpande text: *i grafredigeraren*. |
| Dope Sheet | Dopeblad | UI-namn. Använd bestämd form i löpande text: *i dopebladet*. |
| Action Editor | åtgärdsredigerare | UI-namn; *åtgärdsredigeraren* i löpande text. |
| Value Slider | värdereglage | UI-term för ett specifikt reglage. Behåll *skjutreglage* för den generella regionen och etiketten *Show Sliders*. |
| Outliner | Outliner | Etablerat produktnamn i Blender-manualen. Behåll det på engelska; böj vid behov som *i Outliner*. |
| linked duplicate | länkad dubblett | Dokumentationens singularform för ett nytt objekt som delar samma objektdata. Den synliga pluraloperatören *Linked Duplicate* kan ha en egen UI-form. |
| parenting | föräldrarelation / överordnad relation | Beskriver relationen mellan objekt eller ben. Använd *föräldrarelation* i förklarande dokumentation; följ den exakta UI-kontexten för menyåtgärder som *Rensa överordnad*. |
| rest pose | viloposition | Använd i förklarande armaturtext. Bevara RST-termmål som `<rest pose>`. |
| constraint | begränsning | Blender-funktionen som styr eller begränsar ett objekts eller bens transformation. I sammansättningar: *rotationsbegränsning*, *skalbegränsning*. |
| Clamp To | Begränsa till | Begränsning som placerar ett objekt vid närmaste punkt på en målkurva. I den tekniska typetiketten används *Begränsning: Begränsa till*. |
| transform / transformation | transformera / transformation | Använd *transformation* för Blenders egenskap, begränsning och kanaler. Blanda inte med den bredare betydelsen *omvandling*. |
| offset | förskjutning | Relativ rotations-, positions- eller skaländring i en begränsning. |
| pivot | vridpunkt | Punkt kring vilken en constraint utför en rotation. Använd *vridpunkt*, inte den engelska formen *pivotpunkt* eller det tvetydiga *svängpunkt*. |
| face cull | ytborttagning | Utesluter målmeshens ytor vid Shrinkwrap-projektion beroende på normalriktning. Använd inte den felaktiga formen *utslaktning*. |
| IK stretching | IK-sträckning | Tillåter en IK-kedja att ändra benens längd för att nå målet. |
| Swing / Twist | svängning / vridning | Rotationens svängnings- och vridningsdel i Quaternion- och constraint-kontext. |
| envelope (armature) | omslutning | Armaturens volym runt ett ben som kan användas vid viktning. |
| Action | Action | Blenders datatyp för en animation. Behåll namnet i Action-begränsningens tekniska hjälptexter. |
| duplicate and rename | Duplicera och byt namn | Operatör för kopiering av ben med efterföljande namnbyte. |
| working plane | arbetsplan | Etablerad term i Blenders TBX-ordlista. |
| internal clipboard | interna urklippet | UI-funktion, inte operativsystemets urklipp. |
| rigid body | styv kropp | Fysiksimuleringens etablerade term. |
| shader | shader | Behåll den etablerade facktermen i UI och nodnamn. |
| anti-aliasing | kantutjämning | Synlig inställning för text- och bildåtergivning. |
| Subpixel Anti-Aliasing | Kantutjämning på subpixelnivå | Följer den aktuella svenska UI-etiketten. |
| font hinting | teckensnittshintning | Inställning som styr teckenplacering och skärpa i textåtergivning. Den aktuella UI-exportens *Teckensnittshinting* bör hanteras som en separat UI-rättelse, inte kopieras in i manualprosan. |
| point sampling | punktprovtagning | Pipettläge som samplar enskilda punkter till en färggradient. Använd i förklarande UI-former; det dolda tangentbindningsnamnet är *Modal mappning för punktprovtagning med färggradients-pipett*. |
| Color Ramp | färggradient | Gradient mellan definierade färgstopp; undvik det omotiverade lånet *färgramp*. |
| multisampling | multisampling | Etablerad datorgrafikterm för flera bildprover per pixel, här i Dynamic Paints kantutjämning. Blanda inte ihop med *multisimulering*. |
| Dynamic Paint canvas surface | Dynamic Paint-dukyta | En simulerad yta som tar emot eller visar Dynamic Paint. I plural: *Dynamic Paint-dukytor*. |
| Dynamic Paint canvas normal | duknormal | Normalriktningen för en Dynamic Paint-dukyta vid projektion av en pensel. |
| Dynamic Paint brush normal | penselnormal | Normalriktningen för Dynamic Paint-penselns yta vid projektion. |
| Dynamic Paint canvas settings | dukinställningar | Inställningar för en Dynamic Paint-duk, som kan innehålla flera ytlager. |
| Dynamic Paint paint surface | målningsyta | Dynamic Paint-ytlager av typen Paint; inte uppmaningen *måla ytan*. |
| wetmap | våtkarta | Svartvit utdata som visualiserar färgens våthet på en Dynamic Paint-dukyta. |
| solid radius | heltäckande radie | Radien inom vilken Dynamic Paint-färgen är heltäckande. |
| smooth radius | utjämningsradie | Den extra radien utanför den heltäckande radien som skapar ett jämnt avtagande. |
| smudge | smeta ut | Dynamic Paint-effekt som drar ut befintlig färg när penseln rör sig. |
| effector | effektor | Objekt eller fält som påverkar en Blender-simulering. Skriv sammansättningar som *effektorvikt* och *effektorsamling*. |
| Curve Guide | kurvguide | Kraftfältstyp som styr en simulering längs en kurva. |
| Drag | motstånd | Kraftfältstyp som bromsar rörelse; översätt inte med verbet *dra*. |
| Vortex | virvel | Kraftfältstyp som ger en roterande påverkan. |
| point cache | punktcache | Simuleringscache för punktsystem; skriv ihop. |
| geometry attribute | geometriattribut | Attribut kopplat till Blenders geometri. Skriv ihop, även i sammansättningar. |
| geometry color attribute | geometrifärgattribut | Färgattribut på geometri. Skriv ihop; undvik den särskrivna formen *geometri färgattribut*. |
| 8-bit value | 8-bitarsvärde | Värdetyp i RNA/API-kontext. Skriv ihop med bindestrecket som i *8-bitarsvärde*. |
| Byte Color | Bytefärg | Datatyp för färgattribut. Skriv ihop och behåll den tekniska typen *Byte*. |
| mesh | mesh | Blenders datatyp och samlingstyp. Behåll *mesh* även i plural; använd exempelvis *Huvudmesh* och *Samling av mesh*, inte *nät* eller *maskor*. |
| Float2 Attribute | Float2-attribut | RNA-attributtyp. Behåll typnamnet och fog med bindestreck till svenska *attribut*. |
| timescale | tidsskala | Faktor som skalar simuleringens tidsförlopp. |
| curve mapping | kurvkartläggning | Kartläggning med kurvor; använd den här sammansättningen i RNA- och modifierarinställningar. |
| retiming key | tidsanpassningsnyckel | Nyckelpunkt i sekvensredigeraren som flyttar en bildruta i en remsa och därmed sträcker eller drar ihop tidsflödet. Följer den etablerade majoritetsformen i UI:t. Använd inte den otydliga och inkonsekventa formen *omtidningsnyckel*. |
| Interface Font | Teckensnitt för gränssnittet | Följer den aktuella svenska UI-etiketten. |
| lighting node | belysningsnod | Använd i saktext; behåll engelska nodnamn där de är produktnamn. |
| point / sun / spot / area light | punktljus / solljus / strålkastare / områdesljus | Blenders ljustyper. Översätt efter ljuskontexten; *Point* är inte poäng, *Sun* är inte veckodagen och *Power* är effekt. |
| soft falloff / raytraced shadow | mjukt avtagande / strålspårad skugga | Ljusets avtagande respektive skugga som beräknas med strålspårning. Behåll inte det oöversatta *falloff*. |
| geometry node | geometrinod | Svensk sammansättning i förklarande UI-text. |
| node socket interface | noduttagsgränssnitt | RNA-typnamn för ett uttag i ett nodträdsgränssnitt. Behåll fog-s: *färgnoduttagsgränssnitt*, inte *färgnoduttaggränssnitt*. |
| Mix node | blandningsnod | Node Wranglers synliga menyval *Use Mix Nodes* är *Använd blandningsnoder*. |
| hotkey | snabbtangent | Tangentkombination som aktiverar ett verktyg eller kommando. |
| naming tag | namntagg | Node Wranglers etikett för ett möjligt namn vid Principled-texturinställning. |
| Math node | matematisk nod | Node Wranglers synliga menyval *Use Math Nodes* är *Använd matematiska noder*. |
| Divide | Dividera | Den matematiska nodoperationen i Node Wrangler. Använd inte den bredare handlingen *dela upp*. |
| mix factor | blandningsfaktor | Synlig faktor som styr blandning, inte ett kodidentifierarnamn. |
| Alpha Over | Alfa över | Synligt Blender-nodnamn. Som sammansättning: *Alfa över-nod*; Node Wranglers meny använder *alfa-över-noder*. |
| Batch Change | Batchändring / batchändra | Menyetiketten är *Batchändring*. Använd verbformen *batchändra* för en åtgärd, exempelvis en rubrik. |
| Compositor | Kompositör | Synligt Blender-namn för nodredigeraren. Använd *kompositören* i löpande text. |
| tone mapping / Tonemap | tonmappning | Bildbehandling som anpassar tonomfång. Etiketten *Tonemap Type* blir *Tonmappningstyp*. |
| movie tracking frame | bildruta | I filmspårning avser *frame* en bildruta, inte en fysisk ram. |
| Movie Clip Editor | klippredigerare | Redigeraren för filmklipp, filmspårning och stabilisering. |
| editor space | redigerarläge | Blenders interna typ för det innehåll som visas i ett område; använd inte det fysiska *utrymme*. |
| bounding box | begränsningsruta | Rektangeln som avgränsar ett mönster eller sökområde vid filmspårning. |
| mask spline | maskspline | Spline som avgränsar en mask i bild- och klippredigeraren. |
| track position | spårposition | Position från en filmspårningspunkt. Skilj från ett spårs plats i tidslinjen. |
| geometric translation / Translate | förskjutning / förskjut | Geometrisk bild- eller koordinatförflyttning; inte språklig översättning. |
| Function Node | funktionsnod | Nod som utför en matematisk, logisk eller geometrisk funktion. |
| input type / input value | indatatyp / indatavärde | I nodsammanhang avser *input* ett indatauttag eller dess värde. |
| float | flyttal | Numerisk datatyp. Skriv exempelvis *avrunda flyttalet uppåt*. |
| float attribute value | flyttalsattributvärde | Attributvärde med Blenders numeriska datatyp *float*. Skriv ihop i API-nära UI-etiketter. |
| float vector attribute value | flyttalsvektorattributvärde | Geometriattribut med flyttalsvektor; behåll sammansättningen i Blender-UI. |
| float color attribute value | flyttalsfärgattributvärde | Geometriattribut med färgvärden som flyttal; det är inte en allmän flytande färg. |
| 2D float attribute value | 2D-flyttalsattributvärde | Tvådimensionellt flyttalsattribut i Blenders geometriattribut-API. |
| vorticity | vorticitet | Hydromekanisk vektorstorhet för den lokala rotationen i ett strömningsfält. Behåll den etablerade facktermen i Mantaflow. |
| fluid guiding | vätskestyrning | Mantaflow-funktionen som styr flödet med hastigheter från en domän eller effektor. Använd *styrnings-* i sammansättningar som *styrningsdomän* och *styrningsobjekt*. |
| secondary particles | sekundära partiklar | Skum-, spray- och bubbelpartiklar som härleds från vätskesimuleringen. |
| byte color | bytefärg | 8-bitars färgattribut i geometri- och nodkontext. |
| byte color attribute | bytefärgsattribut | Geometriattribut som lagrar RGBA-färg med 8 bitar per kanal. |
| floating point matrix | flyttalsmatris | Matrisdatatyp med flyttalsvärden; skriv ihop i UI-etiketter. |
| signed integer vector | vektor med signerade 16-/32-bitars heltal | Datatyp för heltalsvektor; skriv *bitars heltal* med mellanrum. |
| integer math | heltalsmatematik | Matematiska operationer på heltal. |
| matrix determinant | matrisdeterminant | Determinanten för en matris. |
| greatest common divisor | största gemensamma delare | Matematikterm; förkorta bara till GCD där UI:t behöver den engelska akronymen. |
| Curve to Mesh | Kurva till mesh | Noden konverterar kurvgeometri till Blenders datatyp *mesh*. Översätt inte till det allmänna ordet *nät*. |
| curve circle / curve line | kurvcirkel / kurvlinje | Synliga nodnamn för kurvprimitiver. |
| poly spline | polyspline | Skriv ihop i nodbeskrivningar för polyline-baserade kurvor. |
| quadrilateral | fyrhörning | Geometrisk figur med fyra hörn. Skilj från adjektivet *fyrsidig*. |
| endpoint selection | ändpunktsurval | Urval av ett antal ändpunkter per spline. |
| face corner | ythörn | Meshens hörn som hör till en specifik yta. Skilj från en delad hörnpunkt. |
| grid volume | volymrutnät | Rutnät i en volym, exempelvis för punktdistribution. |
| Fillet Curve | Avrunda kurva | Kurvnod som skapar cirkelbågar vid hörn; *filé* är fel betydelse i svensk UI-text. |
| mesh vertex / vertex | mesh-hörnpunkt / hörnpunkt | Använd *hörnpunkt* i meshgeometri. Behåll *mesh* när Blender-datatypen behöver anges. |
| vertex neighbors / face group boundaries | hörnpunktsgrannar / ytgruppsgränser | Noder som hämtar topologiska grannar respektive kanter mellan ytgrupper. Sammansättningarna är avsiktliga. |
| Geometry Proximity | Geometrisk närhet | Nod som beräknar närmaste position på en målgeometri. |
| gizmo | gizmo | Etablerat Blender-UI-namn. Skriv sammansatt: *transformationsgizmo*. |
| gizmo collection | samling av gizmor | Samling av Blender-gizmor; översätt inte till den otydliga formen *prylar*. |
| sample (node operation) | provta | Noder som hämtar eller utvärderar data från kurvor, rutnät och ytor. Använd *provta*, inte substantivet *prov* eller *exempel*. |
| Simulation Input / Output | simuleringsindata / simuleringsutdata | In- och utgångsnoder för en Blender-simulering. |
| tangent space | tangentrymd | Etablerad Blender-term för normal- och riktningstolkning. |
| face set | ytuppsättning | Skulpteringsgrupp för mesh-ytor; använd inte *ansiktsuppsättning*. |
| Group Input / Output | gruppindata / grupputdata | Exponerar data mellan en nodgrupp och dess gränssnitt. |
| subsurface scattering | underytsspridning | Ljusets spridning under en materials yta; inte *underjordisk*. |
| clamp (node operation) | begränsa | Begränsar ett värde till ett intervall. Noden använder *begränsningstyp* och *min/max*. |
| normal mapping | normalkartläggning | Använd exempelvis *normalkartläggning i tangentrymd* och *i objektrymd*. |
| reroute | omdirigering | Blenders nod och Node Wrangler-funktion. Sammanfoga som *omdirigeringsnod*. |
| Detach Outputs | Koppla bort utgångar | Node Wrangler-operatör. Använd *utdata* i förklarande text. |
| Relative Path | Relativ sökväg | Synlig filsökvägsinställning. |
| Start Frame | Startbildruta | Synlig tids- och bildsekvensinställning. |
| Texture Coordinate | Texturkoordinater | Synligt Blender-nodnamn; singular engelska har plural svensk UI-form. |
| Mapping | Kartläggning | Synligt Blender-nodnamn. Använd *mappning* bara när sammanhanget inte avser denna specifika nod. |
| Environment Texture | Miljötextur | Synligt Blender-nodnamn. |
| Principled BSDF | Principiell BSDF | Synligt Blender-nodnamn. |
| Image Texture | Bildtextur | Synligt Blender-nodnamn. |
| Color Space | Färgrymd | Synlig Blender-inställning och teknisk fackterm. |
| illuminant | illuminant | Standardiserad ljuskälla i färghantering; skriv exempelvis *vitpunkt för illuminanten D65*, inte *belysningsstyrka*. |
| Filmic / AgX / ACES | behåll namn | Namn på Blenders och OCIO:s färgkodningar och visningstransformeringar; översätt endast den omgivande saktexten. |
| display transform / view transform | visningstransformering | Färghanteringens tekniska transformering inför visning; undvik anglicismen *displaytransform*. |
| Grease Pencil | Grease Pencil | Produkt- och funktionsnamn; översätt inte. |
| Grease Pencil layer | Grease Pencil-lager | Lager som samlar relaterade Grease Pencil-ritningar. Behåll produktnamnet men översätt den svenska efterleden. |
| Grease Pencil frame | Grease Pencil-bildruta | Bildruta i ett Grease Pencil-lager; använd inte *ram* i animeringskontext. |
| annotation frame | anteckningsbildruta | Bildruta som innehåller en anteckning; undvik *ram för anteckning*. |
| annotation layer | anteckningslager | Lager som samlar relaterade anteckningsstreck. |
| Grease Pencil sculpt guide | skulpteringsguide för Grease Pencil | Guide som hjälper till att styra Grease Pencil-streck vid ritning och skulptering. |
| auto-masking | automaskering | Begränsar verktygets påverkan till valt lager, material eller streck. |
| layer pass / material pass | lagerpass / materialpass | Filteregenskaper i Grease Pencil-modifierare. |
| fading | uttoning | Gradvis borttagning i Grease Pencil-bygg- och längdmodifierare. |
| Grease Pencil masking layer | maskeringslager för Grease Pencil | Lager som begränsar synligheten för Grease Pencil-innehåll. |
| Grease Pencil time modifier segment | tidsmodifierarsegment | Ett intervall som har egna tidsförskjutnings- och upprepningsinställningar. |
| onion skin | lökskal | Den visade tidigare eller senare ritningen. Funktionen heter *lökskalning*. |
| override | åsidosättning / överskrivning | Kontextstyrt. Generella UI-etiketter använder *åsidosättning*. *Library Override* är i den aktuella UI-katalogen *biblioteksåsidosättning*, men närliggande operatörsnamn använder också *biblioteksöverskrivning*. Normalisera aldrig utan att granska strängens sammanhang och närliggande förekomster. |

## Mesh och animering

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| vertex | hörnpunkt / hörn | I mesh- och verktygstext används normalt *hörnpunkt* och sammansättningen *hörnpunkts-*. Den korta etiketten *Vertex* förekommer också som *Hörn* i vissa vy- och orienteringssammanhang. Ändra inte mekaniskt mellan formerna. |
| vertex group | hörnpunktsgrupp | Behåll *VertexGroup* i Python-API, klassnamn och andra identifierare. |
| collision vertex group | hörnpunktsgrupp för kollision | Hörnpunktsgrupp som undantas från tygsimuleringens objektkollisioner. |
| selfcollision vertex group | hörnpunktsgrupp för självkollision | Hörnpunktsgrupp som undantas från tygsimuleringens självkollisioner. |
| goal (Soft Body / Cloth) | mål | Fysikinställning som drar en hörnpunkt mot dess målposition. Använd sammansättningarna *målstandard*, *måldämpning*, *målmaximum*, *målminimum* och *målstyvhet*. |
| angular bending springs | vinkelfjädrar | Tygsimuleringens fjädrar för vinkelbaserad böjning. |
| tension stiffness | dragstyvhet | Materialets motstånd mot sträckning i tygsimuleringen. |
| pin stiffness | fäststyvhet | Fjäderstyvhet för fästa hörnpunkter i tygsimuleringen, inte ett fysiskt stift. |
| shear stiffness | skjuvstyvhet | Materialets motstånd mot skjuvning i tygsimuleringen. |
| collision object / collider | kollisionsobjekt | Objekt som deltar i Blenders fysik- och tygkollisioner. |
| permeability | genomsläpplighet | Sannolikheten att partiklar passerar genom ett mesh vid kollision. |
| stickiness | vidhäftning | Hur starkt en partikel fäster vid en yta efter kollision. |
| vertex mass | hörnpunktsmassa | Massan för en enskild hörnpunkt i tygsimuleringen. |
| vertex color | hörnpunktsfärg | Gäller synlig UI-text. |
| vertex normal | hörnpunktsnormal | Gäller synlig UI-text. |
| vertex index | hörnpunktsindex | Gäller synlig UI-text. |
| edge | kant | Mesh-geometri, inte fönsterkant om UI-kontexten säger annat. |
| face | yta | Mesh-element; avgör i sammanhanget om *ansikte* är avsett i annan betydelse. |
| face corner | ythörn | Meshens hörn per yta; skiljs från en delad hörnpunkt. |
| Data Transfer | dataöverföring | Blender-modifieraren som överför meshdata mellan objekt. |
| mesh | mesh | Behåll när det avser Blender-datatypen eller dess etablerade UI-beteckning. |
| bevel | avfasning / fasning | *Avfasning* för UI-egenskapen och modifieraren, *fasning* kan beskriva resultatet i löpande text. |
| Bevel Modifier | avfasningsmodifierare | Blender-modifierarens belagda UI- och manualform. |
| Bevel Vertices / Bevel Edges | Fasa hörnpunkter / Fasa kanter | Synliga operatörsnamn. |
| boolean operation | boolesk operation | Används för meshkombinationerna union, differens och snitt. |
| manifold | manifold | Etablerad topologiterm i 3D-modellering; inte *fördelningsrör*. |
| displacement | förskjutning | Material- och shaderkontext. |
| Vector Displacement | vektorförskjutning | Synlig UI- och manualterm. |
| opacity | opacitet | Använd i UI-reglage för genomskinlighet, till exempel *Opacitet för omarkerade* i F-kurvinställningarna. |
| tint color / tint factor | toningsfärg / toningsfaktor | Grease Pencil-lagerfärg som färgar strecken; undvik den sönderdragna formen *färgton färg*. |
| default settings | standardinställningar | Rubrik för sparade standardval i Inställningar. Följer den befintliga UI-termen för *Defaults*. |
| Adaptive Subdivision | adaptiv underindelning | UI-belagd form; inte *adaptiv indelning*. |
| Material Output | materialutdata | UI-belagd renderings- och nodterm. |
| keyframe | nyckelbildruta | Använd i svensk förklarande text; ändra inte API-namn. |
| breakdown (keyframe type) | mellanpose | Nyckelbildruta som beskriver rörelsen mellan två nyckelposer. |
| moving hold (keyframe type) | rörlig hållning | Nyckelbildruta som ger liten rörelse kring en hållen pose. |
| extreme (keyframe type) | ytterläge | Nyckelbildruta som markerar ett ytterläge i rörelsen. |
| F-Curve | F-kurva | Behåll initialen och använd svenskt ord efter bindestrecket. |
| F-Curve modifier | F-kurvmodifierare | Modifierare som förändrar en F-kurvas värden eller förlopp. |
| frame range | bildruteintervall | Tidsintervall i animation och uppspelning. Använd *startbildruta* respektive *slutbildruta* för ändpunkterna. |
| curve frame range | kurvornas bildruteintervall | Actions sammanlagda intervall från de ingående F-kurvorna. |
| noise modifier | brusmodifierare | Modifierare som lägger slumpmässig variation på en F-kurva. Använd *brus*, inte det fysiska ljudordet *buller*. |
| stepped interpolation | stegad interpolation | F-kurvmodifierare som håller interpolerade värden flera bildrutor. |
| field falloff | fältets avtagande | Hur kraften från ett kraftfält minskar med avståndet. |
| keyframe range | nyckelbildruteintervall | Intervall av bildrutor mellan animeringens nyckelbildrutor. |
| driver (animation) | drivrutin | Funktions- eller uttrycksbaserad styrning av ett animerat egenskapsvärde. Använd *drivrutinstyp*, *drivrutinsvariabel*, *drivrutinsmål* och *drivrutins-F-kurva*. Skilj via sammanhang från enhetens drivrutin, men använd samma svenska huvudterm. |
| action | åtgärd | Animeringsdata i Blender. Behåll *Action* i formella datatyp- eller API-namn. |
| slot | slot | Etablerat i den aktuella Blender-dokumentationen och UI-kontexten. Böj som *en slot*, *slotten*, *slotar* och *slotarnas*. |
| action slot | åtgärdsslot | Slot som väljer den delmängd av en Action som en NLA-remsa eller Action Constraint använder. Använd *åtgärdsslot*, *åtgärdsslotten* och *åtgärdsslotar* i synlig UI-text; behåll `action_slot` i API-identifierare. |
| slotted action | åtgärd med slotar | Äldre API-hjälptext som avser en Action med Action Slots. Behåll den tekniska betydelsen och skriv inte engelska *slotted actions* i svensk löptext. |
| transform | transformation | Avser objektets position, rotation och skala i Constraint- och Action-kontext. Undvik den bredare formen *omvandling* i dessa etiketter. |
| Damped Track | Dämpad spårning | Begränsning som riktar en lokal axel mot målet med kortast möjliga rotation. Det är inte en järnvägsspårvidd. |
| Track Axis | riktningsaxel | Den lokala axel som pekar mot målet i Blenders spårningsbegränsningar. |
| Track To | Rikta mot | Synlig Constraint-etikett för att orientera objektet mot ett mål. Skilj från film- och rörelsespårning. |
| Shrinkwrap | Shrinkwrap | Behåll Blenders synliga funktionsnamn. Funktionen anpassar meshens hörnpunkter till en målyta; den är inte förpackningsmaterial som *krympfilm*. Sammansättningar skrivs *Shrinkwrap-modifierare* och *Shrinkwrap-begränsning*. |
| constraint | begränsning | Blender-relation som styr ett objekt eller ben. Skriv sammansättningar som *positionsbegränsning*, *rotationsbegränsning*, *skalbegränsning* och *avståndsbegränsning*. |
| project axis | projektionsaxel | Axeln som Shrinkwrap projicerar längs. Skilj från ett projekts egen axel. |
| target normal | målnormal | Normal från målets yta, till exempel i Shrinkwrap-projektion. |
| joint binding | ledbindning | Spline IK-inställning för leders relativa positioner längs kedjan. |
| curve mapping | kurvkartläggning | Verktyg som mappar färg-, vektor- eller skalärvärden via en användardefinierad kurva. |
| curve fill mode | kurvans fyllningsläge | Inställning för hur en 2D-kurva fylls. |
| curve bevel cross section | tvärsnitt för kurvans avfasningsgeometri | Profilen som gör en kurva till ett rör; kan vara en cirkel, ett separat kurvobjekt eller en profil. |
| curve path duration | sökvägsvaraktighet | Antal bildrutor som används för att färdas längs en kurvas sökväg. |
| taper object / taper radius | avsmalningsobjekt / avsmalningsradie | Kurvinställningar som styr profilens bredd längs kurvan. Avsmalningsobjektet fungerar som en skalningskurva, inte endast som en förminskning mot slutet. |
| Map Taper | Mappa avsmalning | Gör att avsmalningsobjektets ändpunkter följer den genererade, snarare än hela, kurvgeometrin. |
| Bounds Clamp | Begränsa till meshgränser | Begränsar en kurvdeformering till meshens gränser. |
| texture space | texturutrymme | Blender-egenskap för automatisk eller manuell texturkoordinering. |
| twist method | vridningsmetod | Beräkningsmetod för 3D-kurvans vridning. |
| translation path | förflyttningsbana | Kurvbana som styr ett underordnat objekts rörelse; inte en språklig översättning. |
| text box overflow | textruteöverflöde | Hantering när text inte ryms i Blenders textrutor. |
| small caps | kapitäler | Typografisk stil med små versaler; använd inte vardagsformen *små huvudstäder*. |
| Justify / Flush | justera / jämna marginaler | Båda justerar text mot vänster och höger marginal. *Justera* använder ordmellanrum vid radbrytning, medan *Jämna marginaler* alltid använder teckenavstånd. |
| character spacing (kerning) | teckenavstånd | Avstånd mellan tecken i Blenders textobjekt; används av läget *Jämna marginaler*. |
| shear | skjuvning | Geometrisk transformering eller textobjektets kursiveringsvinkel. |
| Freestyle line style | Freestyle-linjestil | Freestyles inställningsobjekt för den renderade konturlinjen. |
| stroke geometry | streckgeometri | Geometrin för ett Freestyle-streck; inte *slaggeometri*. |
| chain vertex | kedjehörnpunkt | Hörnpunkt i Freestyles kedja av funktionskanter. |
| chain splitting | kedjedelning | Freestyle-funktion som delar en kedja utifrån längd eller mönster. |
| split length | delningslängd | Kurvlinjär 2D-längd som används vid Freestyle-kedjedelning. |
| split pattern | delningsmönster | Freestyle-streckmönster som används för att dela en kedja. |
| Freestyle Butt cap | stumt ändlock | Platt ändlock som slutar exakt vid streckets beräknade ändpunkt. |
| Freestyle dash / gap | streck / mellanrum | Delarna i Freestyles streckmönster; samma termer används i delningsmönstret *Delningsstreck* och *Delningsmellanrum*. |
| Freestyle border edge | gränskant | Funktionskant vid en gräns, till exempel när ett objekt avgränsar scenen; skilj från en godtycklig *kant*. |
| Freestyle thickness position | tjockleksplacering | Var streckets tjocklek läggs i förhållande till silhuetter och gränskanter. |
| stroke depth order | streckens djupordning | Anger hur Grease Pencil-streck ordnas i 3D-rymden. |
| onion opacity | opacitet för lökskal | Opaciteten för Grease Pencil-bildrutor som visas före och efter aktuell bildruta. |
| render slot | renderingsplats | Sparad renderingsbuffert i Blenders bildredigerare. |
| seam margin | sömmarginal | Marginal vid fixering av UV-sömmar under målning. |
| UDIM tile | UDIM-platta | En platta i en UDIM-bildtextur. |
| float buffer | flyttalsbuffert | Bildbuffert som lagrar värden som flyttal. |
| library override | biblioteksåsidosättning | Lokal åsidosättning av länkat biblioteksmaterial. |
| light probe | ljussond | Objekt som fångar belysningsdata för indirekt ljus och reflektioner. |
| volume light probe | volymljussond | Ljussond som fångar belysningsdata i en 3D-volym. |
| dilation radius / threshold | utvidgningsradie / utvidgningströskel | Parametrar för att fylla ogiltiga prov i en volymljussonds rutnät; avser inte utspädning. |
| bias (light probe) | riktningsförskjutning, normalförskjutning, visningsförskjutning | Teknisk samplingförskjutning. Översätt inte som partiskhet eller fördom. |
| surfel | surfel | Punktbaserat ytelement för global belysning; plural *surfelar*. |
| backface culling | baksidesgallring | Renderingsteknik som döljer ytors baksidor. |
| ray tracing | strålspårning | Renderingsteknik; använd exempelvis *strålspårad transmission*. |
| texture slot | texturplats | Plats som kopplar en textur till ett material eller målningsverktyg. |
| mesh loop | meshloop | Intern meshtopologisk struktur vid ett ythörn; *looptriangel* används för triangulerat resultat. |
| UV loop layer | UV-looplager | UV-lager som hör till meshens loopar. Använd *UV-looplager*, inte *UV-loopskikt*. |
| vertex color / normal | hörnpunktsfärg / hörnpunktsnormal | Attribut på en mesh-hörnpunkt. |
| node tree | nodträd | Blenders sammanlänkade nodstruktur. Sammansättningar är exempelvis *geometrinodträd*, *kompositionsnodträd* och *shadernodträd*. |
| Node Editor | nodredigerare | UI-namn för redigeraren med nodträd. RNA-beskrivningen *Space Node Editor* använder formen *nodredigerarens område*. |
| Shader Editor | shaderredigerare | UI-namn för nodredigeraren för shaders. Behåll facktermen *shader* och skriv sammansättningen ihop. |
| Texture Node Editor | texturnodredigerare | UI-namn för nodredigeraren för texturer. |
| compositor | komposition | Blender-funktionen för bildkomposition; *Compositor Node Tree* blir *kompositionsnodträd*. |
| selection set | urvalsuppsättning | Namngiven samling av valbara element. |
| delta location | deltaförflyttning | Extra förflyttning som läggs till ett objekts position. |
| empty | tomobjekt | Blender-objekt utan egen geometri, till exempel för referensbilder eller hjälpkontroller. |
| material slot | materialplats | Koppling mellan ett objekt och ett av dess material. |
| world matrix | världsmatris | Transformationsmatris i världsrymden. |
| vertex paint / weight paint / texture paint | hörnpunktsmålning / viktmålning / texturmålning | Blenders respektive målningslägen. |
| gimbal lock | gimbal-låsning | Rotationsproblem i Euler-lägen. |
| instancer | instansierare | Objekt som skapar instanser av sina underordnade objekt eller sin instanssamling. |
| dynamic topology sculpting | skulptering med dynamisk topologi | Skulpteringsläge som ändrar meshtopologin dynamiskt. |
| child particle | barnpartikel | Partikel som härleds från en föräldrapartikel. |
| volume scatter | volymspridning | Spridning av ljus i ett volymmaterial. |
| guide hairs | guidehår | Hjälphår som visar eller styr partikelhårets form. |
| strand render | strårendering | Rendering av enskilda hår- eller partikelstrån. |
| subframe | delbildruta | Simuleringssteg mellan hela bildrutor. |
| particle path | partikelbana | Bana som en partikel följer över tid. |
| distance model | avståndsmodell | Modell som styr hur ljudets styrka minskar med avståndet. |
| subframe | delbildruta | Simuleringssteg mellan hela bildrutor. |
| sequencer | sekvensredigerare | Blenders redigerare för video- och ljudsekvenser. |
| noise (texture) | brus | Procedurtexturens variation; använd inte det fysiska ljudordet *buller*. |
| checker (image texture) | schackmönster | Bildtexturens växlande rutor. |
| normal map | normalkarta | Bild med RGB-värden som kodar ytans normalriktningar. |
| curve map point | kurvkartpunkt | Punkt i en kurvkartläggning. |
| paint curve | målningskurva | Kurva som styr penseldragets förlopp; det är inte en kurva för färg. |
| support loop | stödslinga | Topologisk loop som kontrollerar skärpan kring en meshdetalj. |
| mix mode | blandningsläge | Anger hur en Transform Constraint kombinerar position, rotation eller skala med det ursprungliga värdet. |
| curve slice | kurvsegment | En enskild kurva från ett curves-datablock. |
| curve spline | kurvspline | Spline som hör till en kurva; plural *kurvsplines*. |
| view layer | visningslager | Blender-datalager som bestämmer vilka samlingar och objekt som är synliga vid utvärdering och rendering. |
| dependency graph | beroendegraf | Blenders graf över datablock och deras beroenden vid utvärdering. |
| data path | datasökväg | RNA-sökväg till en egenskap; behåll Python-identifierare och bokstavliga sökvägsuttryck oförändrade. |
| transform space | transformationsrymd | Koordinatrymd som används för positions-, rotations- eller skaltransformering. |
| clipping plane | klippningsplan | Etablerad svensk CAD-/grafikterm. Använd inte *klippplan*, eftersom den formen får tre p i följd. |
| wireframe | trådram | Befintligt svenskt Blender-UI-namn. Skriv *trådramsläge* för *wireframe mode*. |
| shape key | formnyckel | Etablerad term i Blenders TBX-ordlista och UI. |
| Shape Key Editor | formnyckelredigerare | Redigeraren för formnycklars åtgärder och nyckelbildrutor. |
| Softbody | mjuk kropp | Simuleringstyp. Skriv *punktcache för mjuk kropp* i förklarande text, inte engelska *softbody-punktcache*. |
| rig | rigg | Riggningens styrstruktur för en armatur. Behåll den svenska facktermen i löpande dokumentation. |
| meta-rig | metarigg | Rigifys förenklade armatur som används för att generera den färdiga riggen. Skriv ihop på svenska. |
| sub-rig | underrigg | Standardiserad Rigify-komponent. Skriv ihop i singular och i sammansättningar, till exempel *underriggtyp*. |
| Rigify Human | Rigify Human | Namn på Rigifys förinställda mänskliga metarigg; översätt inte som löpande text. |
| tweak control | finjusteringskontroll | En kontroll för lokala deformationer i Rigify. Använd inte det engelska *tweak* i förklarande svensk text. |
| unhide | visa | I Blenders hierarki betyder åtgärden att ett dolt objekt visas igen, inte att det döljs. |
| Armature modifier | armaturmodifierare | Modifieraren som kopplar en mesh till en armatur för deformering. |
| automatic weights | automatiska vikter | Viktmålningsmetod för att koppla meshens hörnpunkter till armaturens ben. |
| widget | widget | Rigifys redigerbara kontrollobjekt. I sammansättning används *widgetobjekt*, *widgetsamling* och *widgetmesh*. |
| finalize script | slutskript | Rigify-skript som körs efter att en rigg har genererats för att tillämpa användaranpassningar. |
| library linking | bibliotekslänkning | Länkning av datablock eller samlingar från en annan Blender-fil. |
| pivot | vridpunkt | Roterande delars tekniska centrum i riggning; använd till exempel *ögats vridpunkt*. |
| merge point | sammanfogningspunkt | Delad punkt där två eller flera bens huvud eller svans överlappar. |
| bone roll | benrullning | Etablerad svensk UI-term för ett bens rotationsriktning kring längdaxeln. |
| B-Bone Roll In / Roll Out | inrullning / utrullning | Reglerar B-Bonens rullning i början respektive slutet. Hjälptexterna använder *rullningsförskjutning*. |
| feature set | funktionsuppsättning | Rigify-undertillägg som tillhandahåller metariggar eller riggtyper. |
| rig type | riggtyp | Typdefinition som bestämmer hur Rigify genererar en viss del av en rigg. |
| rig sample | riggprov | Fördefinierad Rigify-del som läggs till i en armatur eller metarigg som utgångspunkt. |
| parenting settings | överordningsinställningar | Inställningar för relationen mellan ett ben och dess överordnade ben. |
| Child Of constraint | Child Of-begränsning | Formellt Blender-namn med svensk sakterm. Behåll *Child Of* som identifierande del av begränsningens namn. |
| Bendy Bones | Bendy Bones | Synligt Blender-namn för böjliga ben; behåll produktnamnet i etiketter och den närliggande saktexten. |
| B-Bone handle offset | förskjutning av axelhandtaget | I riggningshjälptexter: *Förskjutning av X-axelhandtaget vid början av B-Bone-kurvan*. Behåll B-Bone som Blenders kortnamn. |
| B-Bone segment | B-Bone-segment | UI-egenskap för B-Bonens underindelning. Bindestrecket håller produktnamnet och den svenska efterleden läsbara. |
| Octahedral | oktaedrisk / oktaedrar | Använd adjektivet i UI-värdet och substantivet i beskrivningen av benens visningsform. |
| B-Spline | B-spline-kurva | Matematiskt kurvnamn i beskrivningar av B-Bones och trådvisning. |
| bone collection | bensamling | Blender-samling för ben; skriv ihop i synlig UI-text. |
| Envelope deform | kuvertdeformering | Deformeringsmetoden som använder benens kuvertvolymer; använd i Bens/Armaturens egenskaper. |
| armature-relative | relativt riggskelett | Position eller orientering uttryckt i armaturens lokala koordinatsystem. |
| inherit scale | ärv skala | Armaturinställning som styr hur ett underordnat ben tar emot skalning från ett överordnat ben. |
| shear | skjuvning | Skev transformationskomponent i armatur- och matrisinställningar; använd inte vardagliga *saxning*. |
| bone head / tail | benhuvud / benspets | Blenders ändpunkter för ett ben i armatur- och rörelsebanekontext. Använd formerna konsekvent även i dataegenskaper; skriv inte *svans* eller *stjärtände*. |
| connected bone | anslutet ben | Ett underordnat bens huvud är fast vid det överordnade benets spets. |
| envelope influence | kuvertets påverkan | Påverkan från ett bens Envelope-volym vid armaturdeformering. |
| relative parenting | relativ överordning | Armaturinställning som låter underordnade objekt använda relativ transformering. |
| scale easing | skalutjämning | B-Bone-inställning som skalar de slutliga utjämningsvärdena med Y-faktorerna för Skala in/ut. |
| library override | biblioteksåsidosättning | Lokal ändring av länkat biblioteksmaterial i aktuell Blender-fil. |
| effective visibility | effektiv synlighet | Synlighet som beror på både bensamlingen och alla dess överordnade samlingar. |
| selection set | urvalsuppsättning | Rigify-inställning som samlar ben för ett styrt urval. |
| color set | färguppsättning | Namngiven grupp av benfärger i Rigify. |
| brush capabilities | penselfunktioner | Skrivskyddad uppsättning tillgängliga egenskaper för en pensel. |
| brush | pensel | Använd för Blender-verktyget i målning, skulptering och Grease Pencil. Undvik den felaktiga formen *borste* i nya UI-strängar. |
| brush blending mode | penselblandningsläge | Inställning som styr hur penselns färg kombineras med befintliga pixlar eller värden. |
| Color Burn / Linear Burn | Färgbränn / Linjär bränn | Etablerade namn på mörkande blandningslägen; undvik omskrivningar som *efterbelys färg* och *linjär förbränning*. |
| Screen / Color Dodge | Raster / Färgskugga | Etablerade namn på ljusare färgblandningslägen i den här UI-kontexten. |
| Pin Light / Vivid Light | Punktljus / Levande ljus | Namn på färgblandningslägen; *stiftlampa* är inte korrekt. |
| kernel radius | kärnradie | Radien för pixelkärnan vid oskärpa och skärpning. |
| boundary falloff | avtagande vid gräns | Styr hur skulpteringspenselns deformation minskar från en meshgräns. |
| boundary deformation | gränsdeformering | Deformationsläge som påverkar ett område utifrån en meshgräns. |
| cloth damping | tygdämpning | Reglerar hur långt applicerade krafter fortplantas i penselns tygsimulering. |
| simulation falloff | simuleringsavklingning | Område där tygsimuleringens deformation gradvis avtar. |
| simulation area | simuleringsområde | Den del av meshen som beräknas medan ett penseldrag är aktivt. |
| pinch point | nypunkt | Deformationsläge som drar den simulerade ytan mot en bestämd punkt. |
| crease brush | veckpensel | Skulpteringspensel som skapar eller skärper fåror och åsar genom att nypa ihop meshens hörnpunkter. |
| crease brush pinch factor | nypfaktor för veckpensel | Styr hur starkt veckpenseln nyper ihop geometrin. |
| single color / gradient | enfärg / toning | Färgval för målning med en enda färg eller en övergång mellan färger. |
| crease / pinch factor | fåra-/nypningsfaktor | Skulpteringsfaktor som styr fårning eller nypning av ytan. |
| rake factor / topology rake | krattningsfaktor / topologisk krattning | Skulpteringsinställning som följer och riktar penseldrag efter topologin. |
| persistence | beständighet | Pensel- eller simuleringsfunktion som bevarar ett tillstånd över tid. |
| brush stroke | penseldrag | Ett sammanhängande drag med penseln. Skilj från Grease Pencil-*streck*, som är det ritade resultatet. |
| brush dab | penselavtryck | Enskilt delavtryck i ett penseldrag. |
| Slide Relax | glidutjämning | Skulpteringspensel som glider längs ytan samtidigt som den jämnar ut topologin. |
| Multires Displacement Eraser / Smear | Raderare för Multires-förskjutning / Smeta ut Multires-förskjutning | Skulpteringspenslar för Multires-förskjutning. |
| brush falloff | penselns avtagande | Hur penselns påverkan minskar med avståndet från centrum eller gräns. |
| area radius | områdesradie | Förhållande mellan penselradien och radien som används för att provta områdesplanets djup. |
| propagation steps | spridningssteg | Utökar automaskeringens mjuka gradient stegvis från en mesh- eller ansiktsgräns. |
| falloff | avtagande | Använd i förklarande Blender-text. Behåll engelska namn när de är formella produkt- eller API-namn. |
| brush spacing | penselavstånd | Avståndet mellan penselavtryck; UI-värdet *Space* kan i relevant panel översättas *Avstånd*. |
| brush stroke method | penseldragsmetod | Väljer hur penseldraget skapas; Grease Pencil använder samma penselstyrning. |
| airbrush | sprutpistol | Penselläget som fortsätter att applicera färg medan musknappen hålls nedtryckt. |
| adaptive spacing | adaptivt penselavstånd | Fördelar penselavtryck efter ytans riktning i stället för i skärmutrymmet. |
| smooth stroke | jämnt penseldrag | Styrning som låter penseln släpa efter markören och följa en jämnare bana. |
| vertex paint | hörnpunktsmålning | Målningsläge som målar färgvärden på meshens hörnpunkter. |
| wet persistence | våt beständighet | Mängden våt färg som stannar kvar i penseln efter målning. |
| deformation target | deformationsmål | Väljer om en pensel deformerar geometri direkt eller tygsimuleringens begränsningar. |
| falloff shape | avtagandeform | Väljer om penselns avtagande är projicerat eller sfäriskt. |
| Bi-Scale Grab / Tri-Scale Grab | Flytta i två skalor / Flytta i tre skalor | Elastisk deformeringsmetod för penseln; undvik de felaktiga formerna *gripdon* och *grepp*. |
| brush tip | penselspets | Penselns form och riktning vid målning eller skulptering. |
| mask texture | masktextur | Textur som begränsar en pensels påverkan. |
| mask stencil | maskschablon | Flyttbar och skalbar schablon som begränsar penselns målning i visningsområdet. |
| jitter unit | variationsenhet | Anger om penselns variation beräknas i skärmutrymmet eller relativt penselstorleken. |
| texture overlay | texturöverlägg | Visas ovanpå arbetsytan vid målning. |
| plane offset | planförskjutning | Förskjuter skulpteringsplanet i förhållande till ytan. |
| plane trim | plantrimning | Begränsar hur långt från det förskjutna planet en hörnpunkt påverkas. |
| normal weight | normalvikt | Styr hur starkt flyttverktyget drar meshens hörnpunkter bort från ytan. |
| Paint Curve | målningskurva | Kurva som styr penseldragets förlopp; den är inte en färgkurva. |
| area normal | områdesnormal | Normal som används för ett område i skulpterings- och automaskningsinställningar. |
| view normal | visningsnormal | Normal uttryckt i förhållande till 3D-vyn. |
| face set boundary | ytuppsättningsgräns | Gräns mellan skulpteringens ytuppsättningar. Grundtermen är *ytuppsättning*. |
| cavity mask | hålighetsmask | Automaskering som använder ytans krökning för att begränsa penselns påverkan vid toppar eller skåror. |
| mesh boundary auto-masking | automaskering av meshgräns | Utesluter hörnpunkter vid öppna meshgränser. |
| radius falloff | radieavtagande | Avtagande som styrs av radie i pensel- och skulpteringsinställningar. |
| smooth stroke | jämnt penseldrag | Penselinställning som filtrerar markörens rörelse under draget. |
| space attenuation | avståndsdämpning | Dämpar penselstyrkan utifrån mellanrummet mellan penselavtryck. |
| sculpt capabilities | funktioner för skulptering | Skrivskyddad uppsättning tillgängliga egenskaper för skulpteringsverktyget. |
| vertex paint | hörnpunktsmålning | Målningsläge som tilldelar färgdata till meshens hörnpunkter. |
| weight paint | viktmålning | Målningsläge som tilldelar vikter till meshens hörnpunkter. |
| curve parameter falloff | avtagande längs kurvparametern | Gradvis förändring av en kurvpensels verkan från spetsen till roten. |
| curve radius | kurvradie | Radien för en kurva som skapas eller påverkas av kurvpenseln. |
| Curves Sculpt brush | kurvskulpteringspensel | Pensel i Curves Sculpt-läget; använd sammansättningen i inställningsrubriker. |
| Curves Sculpt brush type | penseltyp | Väljare för verktygstyp i Curves Sculpt; använd inte *typ av borste*. |
| inverse square | omvänd kvadrat | Kurv- eller avtagandeförinställning; den svenska formen är inte *invers kvadrat*. |
| Density brush | täthetspensel | Kurvskulpteringspensel som lägger till eller tar bort kurvor utifrån deras minimiavstånd. |
| scale uniform | skala jämnt | Ändrar kurvors storlek jämnt i stället för att trimma eller extrapolera dem. |
| Vertex Color | hörnpunktsfärg | Färgdata som lagras per hörnpunkt; översätt både UI-läget och den förklarande texten. |
| caps type | ändtyp | Form på början och slutet av ett Grease Pencil-penseldrag. |
| curve jitter | slumpningskurva | Kurva som styr slumpvariationen för Grease Pencil-penseln. |
| curve sensitivity | känslighetskurva | Kurva som styr Grease Pencil-penselns känslighet. |
| curve strength | styrkekurva | Kurva som styr Grease Pencil-penselns styrka. |
| dilate/contract | utvidga/dra samman | Ändrar ett fyllningsområdes omfattning med ett antal pixlar. |
| dissolve | lös upp | Raderingsläge som tonar ned ett Grease Pencil-strecks punkter i stället för att ta bort dem direkt. |
| stroke point | streckpunkt | Punkt som utgör ett Grease Pencil-streck. |
| Grease Pencil sculpt brush type | penseltyp | Väljare för Grease Pencil-verktyg; använd inte *typ av borste*. |
| Gradient Spacing | toningsavstånd | Avståndet innan Grease Pencil-penselns toning går ett helt varv. |
| Gradient Fill Mode / Gradient Stroke Mode | fyllnadsläge för toning / penseldragsläge för toning | Skilda toningsinställningar för fyllning och penseldrag. |
| closure mode | slutningsläge | Hur Grease Pencil-streck förlängs eller kopplas för att täppa igen glapp vid fyllning. |
| closure size | storlek för slutning | Hur långt streckens ändar får förlängas för att täppa igen glapp. |
| jitter | slumpning | Slumpvariation i penselposition, radie eller andra streckegenskaper. |
| subdivision steps | underindelningssteg | Antal gånger Grease Pencil-streck delas upp för att bli mindre taggiga. |
| pin mode | fäst läge | Låser ett valt ritläge till den aktuella penseln. |
| stroke collision | streckkollision | Kontrollerar om förlängda Grease Pencil-streck kolliderar med andra streck. |
| pressure jitter | tryckslumpning | Gör penselns slumpvariation beroende av ritplattans tryck. |
| pin material | fäst material | Behåller det material som är tilldelat Grease Pencil-penseln. |
| stroke random | slumpning per streck | Slumpvariation som beräknas på Grease Pencil-strecknivå. |
| UV random | UV-slumpning | Slumpvariation för automatiskt skapad UV-rotation. |
| vertex color factor | hörnpunktsfärgfaktor | Faktor som blandar hörnpunktsfärg till Grease Pencil-streckets eller fyllningens slutliga färg. |
| Action constraint | Action-begränsning | Begränsning som styr en bens pose med en åtgärds bildrutor. Behåll *Action* som formellt Blender-namn. |
| target space | målkoordinatsystem | Koordinatsystemet som används för målbenets transformationskanal. |
| owner space | ägarkoordinatsystem | Koordinatsystemet som används för ägarens transformationskanal. |
| pose space | poseringsrymd | Armaturens poserade koordinatrymd; behåll inte den engelska RNA-etiketten i svensk UI-text. |
| default frame | standardbildruta | Bildruta som motsvarar transformationskanalens neutrala värde. |
| trigger | utlösare | Den styrande åtgärden i Rigifys korrigerande åtgärder. |
| AOV | AOV / godtyckliga utgångsvariabler | Behåll den korta UI-etiketten *AOV*. I förklarande terminologi används TBX-formen *godtyckliga utgångsvariabler*. |

## Namn, format och kod

| Källa | Hantering |
| --- | --- |
| Wavefront OBJ, OpenTimelineIO, Stanford PLY | Behåll oförändrade; det är etablerade format- eller produktnamn. |
| `.blend`, `SVG`, `PLY`, `glTF`, `KTX2` | Behåll oförändrade. |
| Python-namn, operatorer, enumvärden och egenskapsnycklar | Behåll exakt, till exempel `VertexGroup.add()` och `vertex_indices_set`. |
| Platshållare | Bevara exakt: `%s`, `%d`, `{}` och formatteringsflaggor får inte ändras. |

## USD i import- och exportdokumentationen

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| prim | prim / primitiv | Behåll *prim* när det är USD:s länkade fackterm eller identifierare; använd *primitiv* i svensk förklarande text. |
| root prim | rotprim | Avser roten i USD-hierarkin. Får inte normaliseras till *standardprim*. |
| default prim | standardprim | USD:s namngivna standardprim, inte nödvändigtvis hierarkins rot. |
| Point Cloud | punktmoln | Följer Blender-UI:ts etablerade term. |
| String Property | strängegenskap | Använd för Blenders anpassade egenskaper med strängvärde. Kodnamn och nycklar behålls oförändrade. |
| accessibility label | tillgänglighetsetikett | Gäller USD-tillgänglighetsmetadata. |
| USD stage | USD-scen | Kontextbundet i exporterad/importerad scendokumentation; översätt inte automatiskt i API- eller filformatsnamn. |
| up orientation | uppåtriktning | Använd när koordinatsystemets uppaxel beskrivs, till exempel *Y-uppåtriktning*. |
| USD Preview | USD Preview | Synligt produkt- och nodnamn; översätt inte till *USD-förhandsgranskning*. |
| `UsdGeom*`, `Scope`, `allPurpose`, `preview` | behåll exakt | Identifierare och normativa USD-värden. Översätt endast den omgivande förklarande texten. |

## Texturer, volymer och arbetsytor

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| noise (procedural texture) | brus | I Blenders procedurtexturer avser *noise* en brusfunktion, aldrig ljud eller buller. |
| Noise Texture | brustextur | Synlig texturtyp; skriv sammansatt. |
| procedural Musgrave/Voronoi texture | procedurell Musgrave-/Voronoi-textur | Behåll algoritmnamnet med versal och använd bindestreck före *textur*. |
| 3D Viewport | 3D-vyport | Använd den etablerade UI-termen när källan uttryckligen säger *viewport*. |
| frame (animation) | bildruta | Gäller sekvens-, volym- och Rigify-animering; inte fysisk ram. |
| Volume data-block | volymdatablock | Blenderdatatyp för 3D-volymrutnät. |
| extension/add-on | tillägg | Använd i inställnings- och tilläggshanteringskontext. |
| Asset Browser | resursbläddrare | Synlig Blender-funktion; *asset library* blir *resursbibliotek*. |
| Grease Pencil Vertex/Weight Paint | hörnpunktsmålning/viktmålning med Grease Pencil | Målningslägen i arbetsytans objektläge. |
| IK solver | IK-lösare | Lösare för invers kinematik; använd bindestreck. |
| stateful/stateless solver | tillståndsbaserad/tillståndslös lösare | Avser om lösaren bevarar tillstånd mellan steg. |
| lossy/lossless compression | komprimering med/utan förlust | Kodnings- och formatbeskrivning, inte *förlorad/förlustfri* blandat. |
| float image values | flyttalsbildvärden | Använd *flyttal*, inte engelska *float*, i förklarande UI-text. |
| keymap | tangentmappning | Blenders konfiguration som kopplar tangent- och musinmatning till operatorer. |
| keymap item | tangentmappningspost | En enskild post i en tangentmappning. |
| key configuration | tangentkonfiguration | Samling av Blender-tangentmappningar. |
| tile (UDIM/image) | platta | Bild- eller UDIM-platta; inte kakel. |
| Multi-View / views format | flera vyer / vyformat | Bildinställningar för parallella vyer, exempelvis stereo. Behåll inte engelska *Multi-View* i en svensk UI-etikett. |
| NDOF | NDOF | Behåll enhetens produktförkortning; översätt den efterföljande synliga åtgärden med liten begynnelsebokstav. |
| keyframe | nyckelbildruta | Grundterm för animeringspunkt på en F-kurva. |
| quartic/quintic interpolation | fjärdegradig/femtegradig interpolering | Matematiska interpoleringsord; inte kvadratisk eller engelska funktionsnamn. |
| Keying Set | nyckeluppsättning | Samling av egenskapsvägar som får nyckelbildrutor tillsammans. |
| Keying Set Path | sökväg för nyckeluppsättning | RNA-sökväg som hör till en nyckeluppsättning. |
| line style modifier | linjestilsmodifierare | Freestyle-modifierare för streckens egenskaper. |
| stroke (Freestyle) | streck | Freestyle-linjens synliga geometriska streck; inte *slag*. |
| backbone (Freestyle stroke) | streckets ryggrad | Den centrala geometri som modifierarna påverkar. |
| alpha transparency | alfagenomskinlighet | Freestyle-linjens transparens; undvik blandformen *alpha*. |
| line set (Freestyle) | linjeuppsättning | Urval av Freestyle-linjer med egna stilparametrar. |
| falloff (mask/proportional edit) | avtagande | Avser hur en effekt minskar med avståndet, inte *utfall*. |
| plane track (motion tracking) | planspår | Spårad plan yta i kameraspårning, inte ett flygplan. |
| UV Mapping | UV-mappning | Kartläggning av meshens UV-koordinater; inte mätning. |
| Hook (deformer) | krok | Blender-deformer och dess meny, inte engelska *hook*. |
| Specials (context menu) | särskilda åtgärder för | Meny med relaterade åtgärder, inte erbjudanden. |
| NLA Track | NLA-spår | Spår i Blenders Nonlinear Animation-redigerare; substantiv, inte verbet *spåra*. |
| NLA Strip | NLA-remsa | Ett klipp eller segment i Blenders Nonlinear Animation-redigerare. Skriv sammansatt med bindestreck. |
| strip time (NLA) | remstid | Den utvärderade tiden i en NLA-remsa; skilj från fysisk remsa och filmremsa. |
| movie tracking frame | bildruta | I filmspårning avser *frame* en bildruta, inte en fysisk ram. |
| translation (motion tracking) | förflyttning | Geometrisk positionsändring vid spårning eller stabilisering, aldrig språköversättning. |
| bundle (motion tracking) | rekonstruerad punkt | Den 3D-punkt som återuppbyggs från ett spår. |
| solver (motion tracking) | lösare | Beräkningsmetod för kamera- eller objektspårning; använd *lösare* i förklarande UI-text. |
| compositor | kompositör | Blenders nodbaserade miljö för bildkomposition; använd *kompositör*, inte det engelska *compositor*. |
| matte (keying) | matta | Friläggningsmask som beskriver genomskinlighet, inte en fysisk matt yta. |
| highlight (color correction) | högdager | Ljusaste tonområdet i bild- och färgkorrigeringskontext. |
| midtone (color correction) | mellanton | Mellanområdet i bildens tonomfång. |
| gain (color correction) | förstärkning | Färgkorrigeringsparametern för högdagrar eller mellantoner, inte ekonomisk vinst. |
| color key/distance key/difference key | färgnyckling/avståndsnyckling/skillnadsnyckling | Kompositörens friläggningsmetoder. Använd *nyckling*, inte en bokstavlig nyckel. |
| spill suppression | undertryck färgspill | Minskar kvarvarande färg från grön eller blå bakgrund i friläggning. |
| dilate/erode | utvidga/erodera | Morfologiska maskåtgärder i kompositören. |
| feather (mask) | uttoning | Mjuk övergång vid maskens kant, inte en fysisk fjäder. |
| Cryptomatte | Cryptomatte | Produkt- och formatnamn. Översätt omgivande text, men behåll namnet. |
| luminance key | luminansnyckling | Friläggningsmetod utifrån skillnader i luminans. |
| ID mask | ID-mask | Mask från objekt- eller materialindexpass. |
| straight alpha output | utdata med rak alfa | Utdatabuffert utan förmultiplicerad alfa. |
| lens distortion: barrel/pincushion | tunnformig/kuddformig förvrängning | Svenska optiska former för radiell linsförvrängning. |
| box sharpen | rutskärpning | Namn på kompositörens skärpningsfilter. |
| file output | filutdata | Nods utdata som skrivs till filer; inte fysisk utmatning. |
| output slot | filplats | Konfigurerbar plats för en fil- eller EXR-lagerutdata. |
| straight/premultiplied alpha | rak/förmultiplicerad alfa | Alfalägen i bildbehandlingsnoder. |
| Channel Packed | Kanalpackad | Alfaläge där olika bilder lagras i RGB- och alfakanalerna. Det är en egenskap, inte processen *kanalpackning*. |
| Radiance HDR | Radiance HDR | Filformatsnamn. Behåll produkt- och formatnamnet, översätt inte till *Strålning HDR*. |
| render layer | renderingslager | Lager från en scenrendering. |
| map UV | UV-mappning | Kompositörsnod som använder UV-koordinater för texturmappning. |
| power/logarithm/fraction | potens/logaritm/bråkdel | Matematiknodernas svenska operationstermer. |
| Keying (compositor) | nyckling | Kompositörens friläggnings-/keyingfunktion, inte nyckelbildrutor. |
| mesh edge/loop | meshkant/meshslinga | Meshens topologiska kant respektive slinga. |
| vertex (mesh API) | hörnpunkt | RNA-datatypen *MeshVertex* och dess egenskaper; använd sammansättningar som *hörnpunktsvikt*. |
| face (mesh API) | yta | Meshens polygonala yta; undvik det bokstavliga *ansikte* i denna kontext. |
| Freestyle edge/face mark | Freestyle-kant-/ytmarkering | Markerar vilka meshkanter eller -ytor som Freestyle får använda. |
| feature edge type | funktionskantstyp | Freestyles urvalskategori för funktionskanter; skriv *funktionskantstyper* i plural. |
| execution time | körtid | Modifierarens uppmätta utvärderingstid, inte verkställighetstid. |
| Geometry Nodes | geometrinoder | Blenders nodbaserade geometriarbetsflöde; svensk sammansättning. |
| Grease Pencil stroke | Grease Pencil-streck | Synlig ritad linje i Grease Pencil, inte *slag* eller *stroke*. |
| bevel modifier | avfasningsmodifierare | Modifierare som rundar av meshens kanter och hörnpunkter. |

| node socket | noduttag | Anslutningspunkt för in- eller utdata i en Blendernod. |
| node socket interface | noduttagsgränssnitt | Deklarationen som styr noduttag i en nodgrupp. |
| node tree interface item | nodträdsgränssnittselement | Gemensam term för ett uttag eller en panel i nodträdets gränssnitt. |
| node tree path | nodträdssökväg | Sökväg genom den redigerade nodträdshierarkin. |
| input/output | indata/utdata | Använd i teknisk nodkontext; undvik engelska *input/output*. |
| bake (Geometry Nodes) | baka/bakning | Beräknar och sparar data för en bildruta eller ett intervall; inte matlagning. |
| frame range (animation) | bildruteintervall | Sammanhängande intervall av animeringsbildrutor. |
| data-block | datablock | Blenders interna dataenhet; skriv sammansatt utan bindestreck. |
| asset tag | resursetikett | Etikett för sökning och kategorisering av en resurs i Asset Browser. |
| Line Art | linjekonst | Blenders funktion som härleder teckningslinjer ur scenens geometri. |
| Empty (object type) | tomt objekt | Blenderobjekt utan egen renderad geometri; skilj från en tom bild. |
| image empty | bildtomobjekt | Tomt objekt som visar en referensbild; en teknisk sammansättning i UI:t. |
| mesh plane | meshplan | Plan yta skapad som mesh; behåll *mesh* som Blender-datatyp. |
| rigid body | styv kropp | Fysiksimuleringens kroppstyp i Blender. |
| integrator | integrator | Renderingsalgoritm i Cycles; använd svensk böjning i sammansättningar. |
| Geometry Node Group | geometrinodgrupp | Nodgrupp som utvärderar geometri i Blender. |
| Geometry Node Modifier | geometrinodmodifierare | Modifierare som utvärderar en geometrinodgrupp. |
| keyframe | nyckelbildruta | En bildruta där ett animerat värde uttryckligen anges. |
| F-Curve | F-kurva | Kurvan som beskriver ett animerat värde över tid. |
| fade (sequencer) | uttoning | Gradvis övergång i bild eller ljud mellan remsor. |
| keymap configuration | tangentmappningskonfiguration | Sparad uppsättning Blender-tangentmappningar. |
| snap keyframes | fäst nyckelbildrutor | Flyttar nyckelbildrutor till bestämda tider, bildrutor eller markörer. |
| NLA stack | NLA-stapel | Lagerordningen för åtgärder och remsor i Nonlinear Animation. |
| keying set | nyckeluppsättning | Namngiven uppsättning animerbara egenskaper som används vid infogning och borttagning av nyckelbildrutor. |
| driver | drivare | Uttrycks- eller databaserad styrning av en egenskap; skilj från fysisk hårdvarudrivrutin. |
| Graph Editor | grafredigeraren | Redigeraren för F-kurvor och animerade värden. |
| bone collection | bensamling | Samling som organiserar riggens ben. |
| action | åtgärd | Blenderdatablock som lagrar animeringsdata; behåll *åtgärd* i den här API- och UI-kontexten. |
| action slot | åtgärdsplats | Identifierar vilken uppsättning animeringskanaler i en åtgärd som gäller för ett datablock. |
| layered Action | skiktad åtgärd | Nyare Action-struktur med lager och åtgärdsplatser. |
| legacy Action | äldre åtgärd | Äldre Action-struktur utan lager och åtgärdsplatser. |
| animation channel bag | animationskanalbehållare | API-objekt som samlar F-kurvor och grupper för en åtgärdsplats. |
| kernel optimization | kärnoptimering | Optimering av renderingskärnor i Cycles, inte operativsystemets kärna. |
| intersection | skärningsberäkning | Strålspårningens beräkning av en träff mellan stråle och geometri. |
| Graph Editor | grafredigeraren | Redigeraren för F-kurvor och animerade värden. |
| FriBidi | FriBidi | Egennamn på biblioteket; använd dess officiella skrivning. |
| action blending | blandning av åtgärd | Blandar den aktiva åtgärdens resultat med NLA-stapeln. |
| NLA track | NLA-spår | Spår i Nonlinear Animation som organiserar animeringsremsor. |
| motion path | rörelsebana | Visar ett bens eller objekts position över animeringens bildrutor. |
| Dope Sheet | Dopeblad | Blenderredigerare för tidpunkter, nyckelbildrutor och animationskanaler. |
| Video Sequencer | videosekvensredigerare | Blenderredigerare för videoremsor, ljud och övergångar. |
| asset representation | tillgångsrepresentation | API-objekt som gör det möjligt för tillgångssystemet att hantera en entitet som en tillgång. |
| asset weak reference | svag tillgångsreferens | Referens som inte nödvändigtvis håller tillgången vid liv. |
| normal space | normalrymd | Koordinatrymd för normaler vid exempelvis bakning. |
| cage extrusion | bursextrudering | Avstånd som bygger ut en bakningsbur från det aktiva objektet. |
| bake map | bakningskarta | Bild- eller attributdata som skapas genom att baka renderingsresultat. |
| emission | emission | Ljus som materialet själv avger i renderingskontext. |
| surface emission (fluid) | ytemission | Vätske- eller gasemission från en meshyta i Mantaflow. Skilj från materials ljusemission. |
| soft body | mjukkropp | Fysiksimulerad kroppstyp i Blender. |
| data-block | datablock | Blenders interna dataenhet; skriv som en sammansättning. |

## Kontrollerade UI-formuleringar

| Engelska | Svenska |
| --- | --- |
| Untitled Project | Namnlöst projekt |
| Folder already contains a project. | Mappen innehåller redan ett projekt. |
| Folder already part of a project | Mappen ingår redan i ett projekt |
| Missing project name | Saknat projektnamn |
| No valid selected objects to copy | Inga giltiga valda objekt att kopiera |
| Cannot copy the linked object '%s' to the internal clipboard | Det går inte att kopiera det länkade objektet ”%s” till det interna urklippet |

## Granskningsregel

Enhetlighet får aldrig gå före funktion. Ändra inte text som är ett formatnamn,
en identifierare eller ett nodnamn enbart för att den liknar en engelsk term.
Kontrollera först Blender-källans användning, Weblates ordlista och den
aktuella svenska UI-kontexten. Kör därefter l10n-lint, svlang och Hunspell på
exporterade ändringar.
