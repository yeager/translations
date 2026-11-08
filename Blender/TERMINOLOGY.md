# Blender UI – svensk terminologi

Den här listan gäller Blender UI på Blender Translate. Den är ett stöd för
granskning, inte en ersättning för strängens sammanhang: kontrollera alltid
operator, panel, tooltip, Python-identifierare och närliggande strängar innan
du ändrar en översättning.

Senast uppdaterad: 2026-11-08.

## Grundtermer

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| asset library | tillgångsbibliotek / resursbibliotek | Båda förekommer i den etablerade Blender-katalogen. Följ närliggande UI och ändra inte mekaniskt mellan dem. I Asset Browser och dess inställningsbeskrivningar används *resursbibliotek* för att stämma med de omgivande UI-etiketterna. I övrig längre förklarande text är *tillgångsbibliotek* den vanligaste befintliga formen. |
| Asset Browser | resursbläddrare | Följer den aktuella svenska UI-etiketten. Den äldre manualformen *tillgångsbläddrare* ska inte dras in i ny UI-nära dokumentation. |
| Asset Shelf / Asset Shelf Header | resurshylla / resurshyllans huvudrad | Den nedre snabbåtkomstytan för resurser i en redigerare. *Header* är regionens huvudrad, inte en dokumentrubrik. |
| Header / Show Header | rubrik / Visa rubrik | Synlig Blender-region och dess menyåtgärd. Använd inte den felaktiga förkortningen *huvud*. |
| fallback (WindowManager keymap) | reserv | Suffix för Blenders reservmappning av ett verktyg, exempelvis *kniv (reserv)*. Behåll inte engelska *fallback* i svenska tangentmappningsnamn. |
| access token | åtkomsttoken | Skriv ihop. Förklarande rubriker får precisera typen: *biblioteksåtkomsttoken* respektive *förrådsåtkomsttoken*. |
| remote asset library | fjärranslutet resursbibliotek | Skriv ut relationen i löpande text; undvik *fjärrresursbibliotek*, som blir svårläst med tre r. |
| remote assets | fjärranslutna resurser | Nätåtkomliga resurser i Asset Browser och dess filter. Undvik *fjärrresurser*, som får tre r i följd. |
| cache directory | cachekatalog | Etablerad teknisk sammansättning i Blender. Skriv ihop i UI-etiketter och statusmeddelanden: *diskcachekatalog*, *standardcachekatalog*. |
| aero (Soft Body) | aerodynamik | Soft Body-egenskap som styr hur kanter påverkas av omgivande media. Behåll inte den förkortade engelska etiketten *Aero* i svensk UI-text. |
| Transform Cache Constraint | transformationscachebegränsning | Begränsning som läser ett objekts transformationsdata från en extern cachefil, exempelvis ett Alembic-arkiv. |
| longitude / latitude (camera projection) | längdgrad / breddgrad | Vinklar i kamerans cylindriska och ekvirektangulära projektioner. |
| fisheye lens | fiskögeobjektiv | Kameraprojektion med extremt brett synfält; använd sammansättningen även för fiskögepolynom. |
| sensor fit | sensoranpassning | Anpassar kamerans bild och synfältsvinkel efter bildsensorns bredd eller höjd. |
| passepartout | passepartout | Den mörka överlagringen utanför bildområdet i kameravyn. |
| safe areas (camera) | säkra områden | Hjälplinjer i kameravyn och sekvensredigeraren. *Action Safe* blir *säkra marginaler för bildinnehåll*, medan *Title Safe* blir *säkra marginaler för text*; de centrerade varianterna gäller ett annat bildförhållande. |
| film gate | filmruta | Bildruta som anger den fysiska sensor- eller filmramen i kameravyn. |
| clipping distance | beskärningsavstånd | Kamerans närmaste eller bortre synliga gräns. |
| cache layer | cachelager | Lager i en Blender-cachefil. Skriv ihop, utan bindestreck. |
| prefetch | förhandsladdning | Läser in cache- eller animationsdata i förväg för snabbare uppdateringar. |
| Cycles Procedural cache | Cycles Procedural-cachen | Särskild cache för Cycles procedurbaserade inläsning. |
| Cycles / EEVEE | Cycles / EEVEE | Blenders egna renderare är produktnamn och lämnas oförändrade; sammansättningar skrivs exempelvis *Cycles-kurvor*. |
| object path | objektsökväg | Sökväg för ett objekt i exempelvis en Alembic-arkivfil. |
| bake (rendering/simulation) | baka / bakning | Behåll Blenders etablerade verb i procedur- och inställningstexter: *Baka till aktiv kamera*, *bakningsdata*. Det gäller inte köksbetydelsen. |
| normal space | normalrymd | Val av koordinatrymd för normaldata vid bakning. De konkreta alternativen skrivs *tangentrymd*, *objektrymd* och *världsrymd*. |
| index space | indexrymd | Koordinatrymd för ett rutnäts diskreta index. Följ samma UI-mönster som *objektrymd* och *världsrymd*; använd inte det mer vardagliga *indexrum*. |
| grid index space | rutnätsindexrymd | Rutnätsvolymens indexbaserade koordinatrymd. Skriv sammansatt och använd inte *rutnätsindexutrymme*. |
| local space / global space | lokal koordinatrymd / global koordinatrymd | Transformations- och geometritermer för objektens eller instansernas referenssystem. Använd inte de tvetydiga formerna *lokalt rum*, *global rymd* eller *globalt utrymme*. |
| screen space | skärmrymd | Koordinatrymd baserad på den aktuella vyportens skärmplan. |
| onion skinning | lökskalning | Animeringsvisning med spökbilder från närliggande bildrutor. Undvik bokstavliga former som *avskalning av lök*. |
| onion frame / ghost frame | lökskalsbildruta | Bildruta som visas före eller efter den aktuella bildrutan vid lökskalning. Undvik den missvisande formen *spökram*. |
| Grease Pencil 2D Layers / 3D Location | 2D-lager / 3D-position | Visningslägen som styr streckens djupordning. Använd *lager* i UI-kontext, och *3D-position* när det är den faktiska placeringen i 3D-rymden som avses. |
| Bake Location (motion paths) | beräkningsposition | Valet av benhuvud eller benspets när rörelsebanor beräknas. |
| scope name | scope-namn | Behåll den tekniska källtermen i GPU-felsökningens fångstalternativ. Det är namnet som skickas till `--debug-gpu-scope-capture`, inte Blenders bildanalysvy *Scopes*. |
| Scopes / Scope panel | omfång / omfångspanel | Bild- och filmklippsredigerarnas statistiska visning med histogram, vågform och vektorskop. Skilj från GPU-felsökningens `scope name` och skriv inte *Scope-panel* i svensk UI-text. |
| Resolution Scale | upplösningsskala | Etablerad UI-term för skalan av teckensnitt och knappar vid visning. |
| File Browser | filbläddrare | UI-beteckning för den editor som öppnar och sparar filer. Anpassa bestämd form i löpande text. |
| file handler | filhanterare | RNA-typ och utbyggnadspunkt som registrerar import-, export- och släpphantering för filer. Översätt inte till *handtag*. |
| File Handler Type | filhanterartyp | UI-etikett för typen av filhanterare. |
| Maximize Area | Maximera område | Operatörsnamn. *Område* avser här ett Blender-area, inte ett skärmområde i allmän mening. |
| 3D Viewport | 3D-vyport | Etablerad UI- och manualterm. |
| 3D View | 3D-vy | Förklaringstext för den synliga Blender-vyn; böj som *3D-vyns* i sammansatta led. |
| Console | konsol | Blenders inbyggda Python-konsol. RNA-beskrivningen *Space Console* använder formen *konsolens område*; `prompt` blir *kommandoprompt*. |
| Space [editor] / editor space data | [redigerarens] område / områdesdata | Rör Blenders interna RNA-område, inte ett fysiskt utrymme eller en arbetsyta. Exempel: *Space Graph Editor* → *Grafredigerarens område*. |
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
| invert collection | invertera samling | Etikett för Light Probe-inställningen `invert_visibility_collection`; använd verbform, inte *inverterad kollektion*. |
| collection exporter | samlingsexportör | Exportör som är kopplad till en specifik Blender-samling. |
| collection export handler | exporthanterare för samlingen | Hanterar konfigurerad export av en samling. |
| instance offset | instansförskjutning | Förskjutning från origo som används när en samling instansieras. |
| intersection priority | korsningsprioritet | Line Art-värde som bestämmer vilket objekt en korsningslinje hör till. |
| project | projekt | Avser Blenders projektkatalog och dess inställningar. |
| project settings | projektinställningar | Exempel: *Open Project Settings* → *Öppna projektinställningar*. |
| workspace | arbetsyta | Den etablerade UI-formen, exempelvis *Workspace* → *Arbetsyta*. Använd även *arbetsyta* i felmeddelanden och länkningsdialoger, inte den äldre synonymen *arbetsutrymme*. |
| pie menu | cirkelmeny | Följer den aktuella svenska Blender-UI-katalogen. |
| popup / popover | popupfönster | Synligt tillfälligt fönster eller meny. Undvik *poppuppfönster*, som ger tre `p` i följd. |
| Essentials | Grundresurser | Översatt UI-namn för Blenders medföljande resurser. I löpande text: *resursbiblioteket Grundresurser*. |
| Online Essentials | Grundresurser på nätet | Nätansluten variant av Blenders medföljande resursbibliotek. Använd *på nätet*, inte engelskpåverkade *online*. |
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
| linked / copied data-block | länkat / kopierat datablock | Resursbläddrarens importmetoder. Länkade datablock behåller kopplingen till originalet; kopierade datablock är fristående. |
| Append (Reuse Data) | Lägg till (återanvänd data) | Importmetod som återanvänder kapslade data, exempelvis materialtexturer eller ett objekts mesh, mellan flera instanser. |
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
| Around Frame / On Keyframes (motion paths) | Omkring bildrutan / Vid nyckelbildrutor | Lökskalningslägen för rörelsebanor. Återanvänd de svenska lägesnamnen i hjälptexter; behåll inte den engelska etiketten i citat. |
| Action Editor | Actionredigeraren | Redigerare för den formella Action-datatypen. Använd *Actionredigeraren* i löpande text; inte *åtgärdsredigeraren*. |
| Value Slider | värdereglage | UI-term för ett specifikt reglage. Behåll *skjutreglage* för den generella regionen och etiketten *Show Sliders*. |
| Outliner | Outliner | Etablerat produktnamn i Blender-manualen. Behåll det på engelska; böj vid behov som *i Outliner*. |
| linked duplicate | länkad dubblett | Dokumentationens singularform för ett nytt objekt som delar samma objektdata. Den synliga pluraloperatören *Linked Duplicate* kan ha en egen UI-form. |
| parenting | föräldrarelation / överordnad relation | Beskriver relationen mellan objekt eller ben. Använd *föräldrarelation* i förklarande dokumentation; följ den exakta UI-kontexten för menyåtgärder som *Rensa överordnad*. |
| rest pose | viloposition | Använd i förklarande armaturtext. Bevara RST-termmål som `<rest pose>`. |
| constraint | begränsning | Blender-funktionen som styr eller begränsar ett objekts eller bens transformation. I sammansättningar: *rotationsbegränsning*, *skalbegränsning*. |
| Maintain Volume Constraint | volymbevarande begränsning | Begränsning som kompenserar skalning längs de två icke-fria axlarna för att bevara objektets eller benets volym. Använd *fri axel*, *icke-fria axlar* och *viloposition*. |
| Copy Location / Copy Location Constraint | Kopiera position / Kopiera position-begränsning | Constraint som kopierar ett måls position. Använd *position*, inte den vardagliga och i 3D-kontexten tvetydiga formen *plats*. |
| Copy Rotation / Copy Rotation Constraint | Kopiera rotation / Kopiera rotation-begränsning | Constraint som kopierar ett måls rotation. Behåll *Euler* och axelordningen (`XYZ`, `XZY` osv.) i de tekniska rotationslägena. |
| Copy Scale / Copy Scale Constraint | Kopiera skala / Kopiera skala-begränsning | Constraint som kopierar ett måls skala. *Potens*, *additiv* och *Gör enhetlig* avser respektive exponentiering, additionsläge och jämn omfördelning av volymändring. |
| Copy Transforms / Copy Transforms Constraint | Kopiera transformationer / Kopiera transformationer-begränsning | Constraint som kopierar position, rotation och skala. Blandningslägenas hjälptext använder *fullständig ärvd skalning*, *justerad ärvd skalning* och *delade kanaler*. |
| Clamp To | Begränsa till | Begränsning som placerar ett objekt vid närmaste punkt på en målkurva. I den tekniska typetiketten används *Begränsning: Begränsa till*. |
| transform / transformation | transformera / transformation | Använd *transformation* för Blenders egenskap, begränsning och kanaler. Blanda inte med den bredare betydelsen *omvandling*. |
| offset | förskjutning | Relativ rotations-, positions- eller skaländring i en begränsning. |
| pivot | vridpunkt | Punkt kring vilken en constraint utför en rotation. Använd *vridpunkt*, inte den engelska formen *pivotpunkt* eller det tvetydiga *svängpunkt*. |
| face cull | ytgallring | Utesluter projektion mot en yta beroende på normalriktning. Funktionen raderar inte geometri. |
| IK stretching | IK-sträckning | Tillåter en IK-kedja att ändra benens längd för att nå målet. |
| Spline IK scale modes | Y-skalningsläge / Benets ursprungliga skala / Invers skala / Volymbevarande | Spline IK:s längdskalning följer kurvan längs Y-axeln, medan X- och Z-skalningen bestäms separat. *Anpassa till kurva* skalar benen över hela kurvlängden. |
| Kinematic Constraint | kinematisk begränsning | IK-begränsningens allmänna typ. Använd *kedjelängd*, *lösningsiterationer*, *polmål* och *polvinkel* i dess riggningsinställningar. |
| Swing / Twist | svängning / vridning | Rotationens svängnings- och vridningsdel i Quaternion- och constraint-kontext. |
| envelope (armature) | omslutning | Armaturens volym runt ett ben som kan användas vid viktning. |
| Action | Action | Blenders formella datatyp för animeringsdata. Behåll namnet i UI och API-saktext. |
| Action (böjning) | Actionen / Actioner / Actionerna | Böj det formella datatypsnamnet som ett svenskt utrumord i löpande UI-text. Ersätt inte dessa former med *åtgärden* eller *åtgärder* när Blender-datatypen avses. |
| Action channel / Action library | Action-kanal / Action-bibliotek | Animeringskanal respektive samling av Blenders Action-datatyp. Använd bindestreck för läsbar teknisk sammansättning. |
| Action data-block | Action-datablock | Datablock som innehåller en Action. Behåll *Action* med stor bokstav när typen uttryckligen anges. |
| duplicate and rename | Duplicera och byt namn | Operatör för kopiering av ben med efterföljande namnbyte. |
| working plane | arbetsplan | Etablerad term i Blenders TBX-ordlista. |
| internal clipboard | interna urklippet | UI-funktion, inte operativsystemets urklipp. |
| rigid body | styv kropp | Fysiksimuleringens etablerade term. |
| shader | shader | Behåll den etablerade facktermen i UI och nodnamn; använd inte *skuggare*. När en meny uttryckligen avser nodtypen används *shadernod* och *shadernoder*, inte den vidare saktermen *skuggning*. |
| shader program | shaderprogram | Program som körs för shaderberäkning; skriv sammansättningen ihop. |
| Shader Node | shadernod | Formell Blender-nodtyp. Skriv sammansättningen ihop: *shadernod*, *shadernoder*, *shadernodträd* och *shadernoduttag*. När *shader* i stället avser skuggningsberäkningen används den svenska saktermen *skuggning*. |
| shader socket | shaderuttag | Uttag med shaderdata i en nod eller ett nodgränssnitt. Det är inte detsamma som den fysiska processen *skuggning*. |
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
| geometry threshold | geometritröskelvärde | Tröskelvärde som styr en geometrioperation. Skriv sammansättningen utan bindestreck. |
| geometry color attribute | geometrifärgattribut | Färgattribut på geometri. Skriv ihop; undvik den särskrivna formen *geometri färgattribut*. |
| 8-bit value | 8-bitarsvärde | Värdetyp i RNA/API-kontext. Skriv ihop med bindestrecket som i *8-bitarsvärde*. |
| Byte Color | Bytefärg | Datatyp för färgattribut. Skriv ihop och behåll den tekniska typen *Byte*. |
| mesh | mesh / meshar | Blenders datatyp och samlingstyp. Använd *mesh* i singular och *meshar* i plural; exempelvis *Huvudmesh*, *Samling av meshar*, *kubmesh* och *meshliknande*. Ersätt inte med *nät* eller *maskor*. |
| mesh cache / mesh filter / mesh plane | meshcache / meshfilter / meshplan | UI-namn och tekniska sammansättningar för Blenders meshtyp. Skriv ihop dem och ersätt inte *mesh* med *nät*. |
| box mesh / cuboid mesh | kuboidmesh | Mesh som genereras som en låda eller kuboid i Geometry Nodes. Skriv sammansättningen ihop; använd inte *kuboidnät*. |
| mesh seam / mesh island / mesh instance | meshsöm / meshö / meshinstans | Tekniska delar och instanser av Blenders meshtyp. Skriv sammansättningarna ihop; använd inte *nätsöm*, *nätö* eller *nätinstans*. |
| mesh boundary / mesh symmetry | meshgräns / meshsymmetri | Topologisk gräns och symmetriinställning för en Blender-mesh, bland annat i QuadriFlow. Skriv sammansättningarna ihop. |
| mesh attribute / mesh normal | meshattribut / meshnormal | Tekniska data som hör till Blenders meshtyp. Skriv sammansättningarna ihop; använd inte *nätattribut* eller *nätnormal*. |
| mesh material | meshmaterial | Material som är kopplat till en Blender-mesh. Använd den etablerade sammansättningen, inte *nätmaterial*. |
| mesh geometry / mesh detail / mesh element | meshgeometri / meshdetalj / meshelement | Geometri, detalj och valbart element som hör till Blenders meshtyp. Skriv sammansättningarna ihop; använd inte *nätgeometri*, *nätdetalj* eller *nätelement*. |
| edit mesh / mesh overlay / mesh type | redigeringsmesh / meshöverlägg / meshtyp | Redigerbar mesh, dess visningsöverlägg och dess RNA-typ. Behåll *mesh* som led i de projektspecifika tekniska sammansättningarna. |
| source / destination mesh | källmesh / målmesh | Meshar som är källa respektive mål för dataöverföring. I bestämd form används *källmeshen* och *målmeshen*. |
| mesh source | meshkälla | Rigid Body-inställning som väljer vilken mesh som används för kollisionsformen. Använd inte *nätkälla*. |
| base / input mesh | basmesh / indatamesh | Mesh som utgör ursprungsgeometri respektive indata för en modifierare. I bestämd form används *basmeshen* och *indatameshen*; ersätt inte med *basnät* eller *indatanät*. |
| surface mesh | ytmesh | Mesh som utgör ytan som skulpteringsverktyget utvärderar. Använd *ytmeshen* i bestämd form; ersätt inte den tekniska typen med *ytnät*. |
| emitter mesh | emittermesh | Mesh som emitterar hårpartiklar. Använd *emittermeshen* i bestämd form; ersätt inte med *emitternät*. |
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
| viewer region / viewer node | visningsområde / visningsnod | Kompositörens avgränsade visningsyta och dess nod. Använd inte den personbetecknande formen *visare*. |
| Viewer Path | visningssökväg | Datastruktur som anger vilken visningsnods data kalkylbladsredigeraren visar. |
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
| fluid mesh / fluid noise | vätskemesh / vätskebrus | Bakningssteg och cachedata i Mantaflow. *Brus* avser simuleringsdetaljer, inte ljud. |
| Free Data / Free All (fluid cache) | rensa data / rensa allt | Tar bort beräknad simuleringscache; översätt inte med *gratis* eller *frigör*. |
| effector / effector object | effektor / effektorobjekt | Mantaflow-objekt som påverkar flödet genom kollision eller styrning. Använd inte den förväxlingsbara formen *effektobjekt*. |
| buoyancy density / buoyancy heat | flytkraft från densitet / flytkraft från värme | Mantaflow-gasdomänens separata flytkraftsparametrar. Formuleringen visar vilken fysisk storhet som styr flytkraften och undviker de tvetydiga sammansättningarna *flytkraftsdensitet* och *flytkraftsvärme*. |
| cache data format | filformat för cachelagring | Mantaflow-inställning för hur volym-, yt-, brus- eller partikeldata lagras. Bevara etablerade formatnamn som *Uni Cache* och *OpenVDB*. |
| Replay (fluid cache type) | uppspelning | Cachetyp som bakar simuleringen medan den spelas upp i visningsområdet. Översätt inte som den handlingsinriktade UI-kommandosträngen *Spela upp igen*. |
| Modular (fluid cache type) | modulär | Cachetyp vars simuleringssteg bakas separat; skild från cachetypen *All*, som bakar de valda inställningarna i ett steg. |
| flame grid / smoke flame grid | lågrutnät / rök- och lågrutnät | Mantaflow-datafält för den simulerade lågans respektive rökens och lågans värden. Använd inte direktlånet *Flame Grid* eller den felaktiga särskrivningen *rök flamma galler*. |
| FLIP ratio | FLIP-förhållande | Förhållandet mellan PIC- och FLIP-metoden i vätskesimuleringen. Behåll de tekniska akronymerna PIC och FLIP. |
| obstacle cell | hindercell | Cell i Mantaflow-domänens beräkningsrutnät som representerar ett hinder. Skriv ihop i hjälptexter och egenskapsbeskrivningar. |
| highlight range | markeringsintervall | Egenskap som avgränsar vilka rutnätsvärden som markeras visuellt. Använd inte den handlingsinriktade formen *Markera intervall* som fältetikett. |
| Color Gridlines | färglägg rutnätslinjer | Växling som färgsätter Mantaflow-rutnätets linjer utifrån ett valt simuleringsfält. |
| gridlines | rutnätslinjer | Linjer som visar cellindelningen i Mantaflow-domänen. Skilj från *rutnät*, som avser själva cellstrukturen eller datafältet. |
| color map (fluid display) | färgkartlägga | Funktion som kopplar Mantaflow-fältets voxelvärden till färgerna i en färggradient eller färgkod. Använd verbet *färgkartlägga*, inte det engelska *mappa*. |
| fractional obstacles | fraktionella hinder | Mantaflow-metod med högre upplösning vid gränsen mellan vätska och hinder. Använd konsekvent *fraktionella*, inte den felaktiga varianten *fraktionerade*. |
| slice direction / slices per voxel | skivriktning / skivor per voxel | Mantaflow- och volymvisningens kontroller för snitt genom voxeldata. Använd *skiva*, inte det orelaterade ordet *skär*. |
| single slice | en enda skiva | Visningsläge för ett enda snitt genom en Mantaflow-domän eller volym. Formulera handlingen som *Visa en enda skiva*. |
| heat grid / smoke heat grid | värmerutnät / rökens värmerutnät | Mantaflow-datafält för temperaturdata i en gasdomän. Den possessiva formen gör relationen till röken tydlig utan svårläst sammansättning. |
| particle level set | partikelnivåmängd | Nivåmängd som härleds från vätskepartiklar för Mantaflows meshyta. Använd den matematiskt precisa termen, inte den förkortade och missvisande *partikelnivå*. |
| mesh generator / mesh scale | meshgenerator / meshskala | Mantaflow-inställningar som väljer metod respektive upplösningsfaktor för den genererade meshen. Skriv sammansättningarna utan bindestreck. |
| secondary particles | sekundära partiklar | Skum-, spray- och bubbelpartiklar som härleds från vätskesimuleringen. |
| bubble drag / bubble buoyancy | bubbelmotstånd / bubblornas flytkraft | Mantaflow-parametrar som anger hur bubblor följer vätskan respektive stiger. Översätt *drag* med *motstånd*, inte med den orelaterade krafttypen *dragkraft*. |
| Combined Export | samlad export | Mantaflow-inställning som styr om sekundära partikeltyper skrivs till ett gemensamt eller separata partikelsystem. |
| clamping threshold (secondary particles) | begränsningströskel | Övre eller nedre tröskel som begränsar när sekundära vätskepartiklar skapas. Använd inte den ordagranna men missvisande formen *klämtröskel*. |
| wave crest cell | vågtoppscell | Mantaflow-cell som identifierats som en vågtopp vid generering av sekundära partiklar. |
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
| speed vectors | hastighetsvektorer | Cachelagrade hastigheter för meshens hörnpunkter, bland annat för rörelseoskärpa. |
| MAC Grid | MAC-rutnät | Marker-and-cell-rutnätet för Mantaflows vektor- och hastighetsdata. Behåll akronymen MAC. |
| fluid velocity / guide velocity | vätskehastighet / styrhastighet | Fält som visar vätskedomänens respektive styrningsobjektens hastigheter. Skriv sammansatt i fältetiketter. |
| vector magnitude | belopp | Vektorns längd i Mantaflows visningsinställning. Använd den svenska matematiktermen *belopp*, inte direktlånet *magnitud*. |
| viscosity base | viskositetsbas | Basvärde som i Mantaflow multipliceras med tio upphöjt till den negativa viskositetsexponenten. |
| flow / flow source | flöde / flödesobjekt | Mantaflow-objekt som tillför rök, eld eller vätska till en domän. Använd *emission* och *emitteras* när texten beskriver utsändningen från objektet. |
| surface emission / volume emission | ytemission / volymemission | Mantaflow-inställningar för emission från meshens yta respektive från dess inre. |
| absolute density | absolut densitet | Inställning som hindrar densitetsvärden i emissionsområdet från att adderas. |
| initial velocity / source velocity | initialhastighet / källhastighet | Hastighet när flödet emitteras respektive hastighet som hämtas från ett rörligt flödesobjekt. |
| Freestyle feature edge | funktionskant | Freestyles algoritmiskt identifierade kant för linjerendering. Skilj från en vanlig meshkant när Freestyle-kontexten behöver framgå. |
| crease edge / edge mark | veckkant / kantmarkering | Freestyle-kanttyp för skarpa ytvinklar respektive en manuellt markerad kant. Använd *veckkant*, inte den vaga formen *veckad kant*. |
| material boundary | materialgräns | Freestyle-kant där två material möts på samma objekt. |
| inclusive / exclusive (Freestyle) | inkluderande / exkluderande | Urvalslägen som anger om en samlings eller kanttyps träffar ska tas med eller tas bort. |
| face mark | ytmarkering | Freestyle-attribut för att markera meshytor och styra urvalet av funktionskanter. Använd inte den bokstavliga formen *ansiktsmärkning*. |
| quantitative invisibility (QI) | kvantitativ osynlighet (QI) | Freestyle-mått för hur många ytor som skymmer en funktionskant från kameran. |
| occluding / occluded object | skymmande / skymt objekt | Freestyle-synlighetskontext. Böj *skymt* till *skymda* före pluralformen *objekt*. Undvik de onödigt engelsknära formerna *ocklusiv* och *ockluderad*. |
| style module | stilmodul | Freestyle-Pythonmodul som anger hur linjer ska renderas. |
| view map / view map cache | vykarta / vykartscache | Freestyles beräknade synlighets- och kantdata respektive sparad cache av den. |
| Kr derivative epsilon | epsilon för Kr-derivatan | Numerisk tröskelparameter för Freestyles suggestiva konturer. Behåll förkortningen Kr och formulera resten som en tydlig svensk fackterm. |
| annotation frame / layer | anteckningsbildruta / anteckningslager | Bildruta respektive lager för Blenders ritade anteckningar. Översätt *frame* till *bildruta*, aldrig till den fysiska *ram*. |
| Hydra / Hydra Storm | Hydra / Hydra Storm | USD-baserade renderings- och exporttekniker; produktnamnen lämnas oförändrade. |
| onion skinning (annotations) | lökskalning | Visar närliggande anteckningsbildrutor som halvgenomskinliga spökbilder före eller efter den aktiva bildrutan. |
| drawing guide / speed guide | ritningshjälplinje | Grease Pencils hjälplinje som begränsar riktning eller placering under ritning. Använd inte engelsklånet *guide* i svensk UI-text. |
| guide spacing | avstånd mellan hjälplinjer | Avståndet mellan parallella eller rutnätsbaserade ritningshjälplinjer. |
| gizmo group | gizmogrupp | Grupp som registrerar och visar relaterade interaktiva gizmor. Skriv ihop enligt Blender-terminologin. |
| Gizmo Map | gizmokarta | Intern karta som håller en samling gizmor. Skriv ihop som annan Blender-terminologi med *gizmo*. |
| gizmo properties | gizmoegenskaper | Indata- och inställningsegenskaper för en enskild gizmo. Använd den sammanskrivna formen, inte *gizmo-egenskaper*. |
| VR controller/viewer pose indicator | indikator för VR-styrenheters positioner / indikator för VR-visarens position | VR-överläggets visuella indikatorer för handkontrollernas respektive visningsenhetens lägen. |
| audio scrubbing / OpenXR runtime | ljudskrubbning / OpenXR-körmiljö | Spela ljud vid tidslinjeskrubbning respektive systemets implementering av OpenXR. |
| offset matrix / world matrix | förskjutningsmatris / världsmatris | Transformationsmatriser för gizmons placering respektive slutliga position i världsrymden. |
| depth bias | djupförskjutning | Litet djupvärde som avgör urval eller rendering av en gizmo. |
| vertex neighbors / face group boundaries | hörnpunktsgrannar / ytgruppsgränser | Noder som hämtar topologiska grannar respektive kanter mellan ytgrupper. Sammansättningarna är avsiktliga. |
| Geometry Proximity | Geometrisk närhet | Nod som beräknar närmaste position på en målgeometri. |
| gizmo | gizmo | Etablerat Blender-UI-namn. Skriv sammansatt: *transformationsgizmo*. |
| gizmo collection | samling av gizmor | Samling av Blender-gizmor; översätt inte till den otydliga formen *prylar*. |
| sample (node operation) | provta | Noder som hämtar eller utvärderar data från kurvor, rutnät och ytor. Använd *provta*, inte substantivet *prov* eller *exempel*. |
| Sample (image, colour and weight tools) | provta | Interaktiva verktyg som hämtar ett färg-, pixel- eller viktvärde under pekaren. Använd verbet *provta*, inte lånet *sampla*. |
| Simulation Input / Output | simuleringsindata / simuleringsutdata | In- och utgångsnoder för en Blender-simulering. |
| tangent space | tangentrymd | Etablerad Blender-term för normal- och riktningstolkning. |
| face set | ytuppsättning | Skulpteringsgrupp för mesh-ytor; använd inte *ansiktsuppsättning*. |
| Group Input / Output | gruppindata / grupputdata | Exponerar data mellan en nodgrupp och dess gränssnitt. |
| subsurface scattering | underytsspridning | Ljusets spridning under en materials yta; inte *underjordisk*. |
| subsurface translucency | underytsgenomskinlighet | Materialinställning för genomsläppt ljus under ytan. Skilj från *underytsspridning*, som är scattering. |
| clamp (node operation) | begränsa | Begränsar ett värde till ett intervall. Noden använder *begränsningstyp* och *min/max*. |
| normal map / normal mapping | normalkarta / normalkartläggning | Datat är en *normalkarta*, medan processen och dess inställningar är *normalkartläggning*. Använd exempelvis *normalkartläggning i tangentrymd* och *i objektrymd*. |
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
| Grease Pencil drawing | Grease Pencil-ritning | Själva ritinnehållet som en Grease Pencil-bildruta refererar till. Använd *ritning*, inte den snävare betydelsen *teckning*. |
| keyframe / breakdown / extreme | nyckelbildruta / mellanpose / ytterläge | Animeringsbildruta, mellanliggande pose respektive pose i en rörelses ytterläge. |
| moving hold / jitter keyframe | rörlig hållning / slumpad nyckelbildruta | Animeringslägen där bilden hålls under rörelse respektive där en utfyllnadsbildruta används vid animering på ettor. |
| annotation frame | anteckningsbildruta | Bildruta som innehåller en anteckning; undvik *ram för anteckning*. |
| annotation layer | anteckningslager | Lager som samlar relaterade anteckningsstreck. |
| annotation stroke / annotation stroke point | anteckningsstreck / punkt i anteckningsstreck | Ritad markering respektive dess kontrollpunkt i Blenders anteckningsdata. Använd *streck*, inte *penseldrag*, eftersom termen avser dataresultatet och inte användarens penselrörelse. |
| Grease Pencil sculpt guide | skulpteringsguide för Grease Pencil | Guide som hjälper till att styra Grease Pencil-streck vid ritning och skulptering. |
| auto-masking | automaskering | Begränsar verktygets påverkan till valt lager, material eller streck. |
| layer pass / material pass | lagerpass / materialpass | Filteregenskaper i Grease Pencil-modifierare. |
| fading | uttoning | Gradvis borttagning i Grease Pencil-bygg- och längdmodifierare. |
| Grease Pencil masking layer | maskeringslager för Grease Pencil | Lager som begränsar synligheten för Grease Pencil-innehåll. |
| Grease Pencil time modifier segment | tidsmodifierarsegment | Ett intervall som har egna tidsförskjutnings- och upprepningsinställningar. |
| time modifier mode: normal / reverse / ping pong | vanlig / omvänd / Ping Pong | Riktning eller pendling för Grease Pencils tidsförskjutning. Behåll det etablerade lägesnamnet *Ping Pong*. |
| Grease Pencil layer tree / tree node | lagerträd / trädnod | Hierarki av Grease Pencil-lager och lagergrupper. Använd *dopeblad* för dess kanaler, aldrig *dope-ark*. |
| Grease Pencil dash modifier segment | streckmodifierarsegment | Del av Grease Pencils streckmodifierare som styr vilka ritpunkter som ingår i ett streck eller mellanrum. |
| dash / gap (Grease Pencil modifier) | streck / mellanrum | Beståndsdelar i Grease Pencils streckmodifierarsegment. |
| onion skin | lökskal | Den visade tidigare eller senare ritningen. Funktionen heter *lökskalning*. |
| override | åsidosättning / överskrivning | Kontextstyrt. Generella UI-etiketter använder *åsidosättning*. *Library Override* och dess API- och operatornamn är *biblioteksåsidosättning*; använd inte den äldre formen *biblioteksöverskrivning* för denna Blender-funktion. Andra betydelser av *override* måste fortfarande granskas i sin kontext. |
| Override Constraint | Åsidosatt begränsning | Statusetikett för RNA-egenskapen `Constraint.is_override_data`. Den beskriver att begränsningen kommer från en åsidosättning; den är inte en uppmaning att utföra åtgärden. |

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
| face data / face strength / face step | ytdata / ytstyrka / ytsteg | Meshdata och dess urvals- eller normalstyrkeegenskaper. Använd inte *ansikts-* här; behåll däremot *ansiktsrigg* när en Rigify-rigg för ett mänskligt ansikte avses. |
| face cull / face loop | ytgallring / ytslinga | Mesh- och Shrinkwrap-terminologi. *Ytgallring* avser bortval av geometri efter normalriktning; *ytslinga* är ett sammanhängande urval av meshyta. |
| face corner | ythörn | Meshens hörn per yta; skiljs från en delad hörnpunkt. |
| Data Transfer | dataöverföring | Blender-modifieraren som överför meshdata mellan objekt. |
| mesh | mesh | Behåll när det avser Blender-datatypen eller dess etablerade UI-beteckning. Böj som ett utrumord: *en mesh*, *meshen*, *meshar*, *meshens* och *denna mesh*. Skriv sammansättningar ihop, till exempel *meshobjekt*, *meshsymmetri*, *meshkanter*, *meshnormaler*, *meshhörnpunkt* och *meshindata*. |
| object bounding box | begränsningsbox | Objektets tredimensionella gränsvolym i objektrymd. Skilj från *begränsningsruta* i filmspårning och bildredigering. |
| bevel | avfasning / fasning | *Avfasning* för UI-egenskapen och modifieraren, *fasning* kan beskriva resultatet i löpande text. |
| Bevel Modifier | avfasningsmodifierare | Blender-modifierarens belagda UI- och manualform. |
| modifier space | modifierarens koordinatrum | Modifierarens egna koordinatsystem. Använd konstruktionen *i modifierarens koordinatrum*, inte den otydliga sammansättningen *modifieringsutrymme*. |
| modifier node group assets | resurser för modifierarnodgrupper | Resurser som utgör nodgrupper för modifierare. Använd den här explicita formen i Asset Browser-status, inte *modifieringsnodgruppsresurser*. |
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
| F-Curve modifier / F-Modifier | F-kurvmodifierare | Modifierare som förändrar en F-kurvas värden eller förlopp. Även den förkortade synliga formen *F-Modifier* använder den svenska termen *F-kurvmodifierare*. |
| frame range | bildruteintervall | Tidsintervall i animation och uppspelning. Använd *startbildruta* respektive *slutbildruta* för ändpunkterna. |
| curve frame range | kurvornas bildruteintervall | Actions sammanlagda intervall från de ingående F-kurvorna. |
| noise modifier | brusmodifierare | Modifierare som lägger slumpmässig variation på en F-kurva. Använd *brus*, inte det fysiska ljudordet *buller*. |
| roughness | grovhet | Delad Blender-term för både materialegenskap och fraktalt brus. Använd *grovhet* även när den beskriver mängden högfrekventa detaljer. |
| lacunarity | lacunaritet | Delad Blender-term för avståndet eller skalningsskillnaden mellan efterföljande frekvenser/oktaver. Följer Blenders svenska manual. |
| stepped interpolation | stegad interpolation | F-kurvmodifierare som håller interpolerade värden flera bildrutor. |
| field falloff | fältets avtagande | Hur kraften från ett kraftfält minskar med avståndet. |
| radial falloff power | exponent för radiellt avtagande | Kraftfältets exponent som anger hur snabbt den radiella påverkan minskar med avståndet. |
| rest length (harmonic field) | vilolängd | Jämviktslängd i ett harmoniskt kraftfält. Använd inte den engelskpåverkade formen *restlängd*. |
| Curl (texture force-field mode) | Curl | Synligt tekniskt namn för den vektoranalytiska curl-operationen i texturkraftfältet. Det är inte hårtermen *lock*. |
| root texture coordinates | rottexturkoordinater | Texturkoordinater från rotpartiklarnas positioner. Skriv sammansättningen ihop. |
| keyframe range | nyckelbildruteintervall | Intervall av bildrutor mellan animeringens nyckelbildrutor. |
| driver (animation) | drivrutin | Funktions- eller uttrycksbaserad styrning av ett animerat egenskapsvärde. Använd *drivrutinstyp*, *drivrutinsvariabel*, *drivrutinsmål* och *drivrutins-F-kurva*. Skilj via sammanhang från enhetens drivrutin, men använd samma svenska huvudterm. |
| action | åtgärd | Behåll *åtgärd* när ordet är ett vanligt substantiv eller verb; skriv *Action* när det betecknar Blenders datatyp. |
| slot | slot | Etablerat i den aktuella Blender-dokumentationen och UI-kontexten. Böj som *en slot*, *slotten*, *slotar* och *slotarnas*. |
| Action slot | Action-slot | Slot som väljer den delmängd av en Action som en NLA-remsa eller Action Constraint använder. Använd *Action-slot*, *Action-slotten* och *Action-slotar* i synlig UI-text, även när etiketten bara är *Slots*; behåll `action_slot` i API-identifierare. |
| slotted Action | Action med slotar | Äldre API-hjälptext som avser en Action med Action Slots. Behåll den tekniska betydelsen och skriv inte engelska *slotted actions* i svensk löptext. |
| transform | transformation | Avser objektets position, rotation och skala i Constraint- och Action-kontext. Undvik den bredare formen *omvandling* i dessa etiketter. |
| Damped Track / Damped Track Constraint | Dämpad spårning / Dämpad spårning-begränsning | Begränsning som riktar en lokal axel mot målet med kortast möjliga rotation. Det är inte en järnvägsspårvidd. |
| Follow Path / Follow Path Constraint | Följ bana / Följ bana-begränsning | Constraint som låser rörelsen till en målkurva. *Heading and banking* blir *riktning och krängning*; *banking* är rotation kring rörelseriktningen, inte en lutning. |
| In Front (Grease Pencil) | Framför | Återanvänd den synliga, lokaliserade objektetiketten även när den nämns i en Grease Pencil-hjälptext. Behåll inte den engelska formen i citat. |
| Track Axis | riktningsaxel | Den lokala axel som pekar mot målet i Blenders spårningsbegränsningar. |
| Track To | Rikta mot | Synlig Constraint-etikett för att orientera objektet mot ett mål. Skilj från film- och rörelsespårning. |
| Follow Track | Följ spår | Synlig Constraint-etikett som låser ett objekt till ett filmspår. Skilj från *Track To*, som styr objektets orientering. |
| Follow Track Constraint | Följ spår-begränsning | Formellt API-/UI-namn för begränsningen ovan. Bindestrecket gör sammansättningen läsbar. |
| Object Solver / Object Solver Constraint | objektlösare / objektlösarbegränsning | Begränsning som låser ett objekt till den rekonstruerade rörelsen hos ett filmspårningsobjekt. *Lösare* är Blenders etablerade term för beräkningsmetoden. |
| pivot / Pivot Constraint | vridpunkt / vridpunktsbegränsning | Rotationspunkt som kan ställas in för ett objekt. Använd *vridpunkt*, inte det engelska *pivot* eller *svängpunkt*. |
| Shrinkwrap | Shrinkwrap | Behåll Blenders synliga funktionsnamn. Funktionen anpassar meshens hörnpunkter till en målyta; den är inte förpackningsmaterial som *krympfilm*. Sammansättningar skrivs *Shrinkwrap-modifierare* och *Shrinkwrap-begränsning*. |
| hair curve / hair root / hair tip | hårkurva / hårrot / hårspets | Avser den hårgeometri som bearbetas av Blenders Hair Nodes. Skriv därför *hårkurvor*, *rot* och *spets* i de här nodernas beskrivningar, inte *hårets kurvor*, *topp* eller engelska *tips*. |
| hair curve profile | hårkurvprofil | Profil som styr radien längs en hårkurva. Använd den sammanskrivna UI-termen för noden *Set Hair Curve Profile*. |
| Roll Direction (Hair Nodes) | rullningsriktning | Riktningen som en hårkurva rullas kring sin axel. Använd *rullning* och *rullningsriktning*, inte det ospecificerade *riktning*. |
| Curve Info / Curve Root / Curve Segment / Curve Tip | Kurvinformation / Kurvrot / Kurvsegment / Kurvspets | Namn på noder som läser data ur hårkurvor. De är sammansättningar, inte fraser som *Kurva rot*. |
| hair attachment | hårinfästning | Hårkurvans fästning vid en meshyta. Använd exempelvis *infästnings-UV*, inte det felaktiga *bilaga-UV*. |
| feature awareness (Redistribute Curve Points) | detaljbevarande | Den här inställningen bevarar lokala kurvdetaljer och riktningsändringar när kontrollpunkter omfördelas. |
| Poisson Disk Distribution | Poisson-diskfördelning | Fördelningsmetod som upprätthåller ett minsta avstånd mellan genererade hårkurvors rotpunkter. |
| Density Mask (hair curves) | densitetsmask | Skalär mask som lokalt påverkar tätheten när hårkurvor skapas eller interpoleras. |
| hair attachment / surface normal | hårinfästning / ytnormal | Vid hårgenerering beskriver detta hur hårkurvans rot fästs vid meshytans UV-koordinat och normal. |
| clumping (hair particles) | klumpning | Samling av barnpartiklarnas hårstrån kring varandra. Använd *grad av klumpning* och *klumpningens form* för reglagen. |
| kink (hair particles) | nyck | Periodisk förskjutning som formar barnpartiklarna som lock, våg eller fläta. Använd *nyck*, inte det missvisande *knäck*. |
| guide index / guide map / guide mask | guideindex / guideindexkarta / guidemask | Datat som anger vilken guidekurva varje hårkurva använder. Skriv sammansättningarna ihop. |
| main guide curve | huvudguidekurva | Den guidekurva vars index styr en interpolerad hårkurva. |
| mesh islands (hair interpolation) | meshöar | Separata sammanhängande meshområden som hålls isär vid hårkurvsinterpolering. |
| flare (Braid Hair Curves) | utsvängning | Den öppna delen vid flätans spets där hårstråna lossnar eller sprider ut sig. Det är inte en *flärp* eller en mekanisk fläns. |
| Curve Sculpt / Mesh Sculpt | kurvskulptering / meshskulptering | Resurskataloger för skulptering av kurvor respektive Blenders meshdatatyp. Behåll *mesh* och skriv sammansättningarna ihop. |
| extension repository | tilläggsförråd | Det förråd som Blender Extensions hämtar eller installerar tillägg från. Skilj från ett Git-förråd och från en lokal resurskatalog. |
| coat / sheen (Principled BSDF) | beläggningsskikt / fiberlyster | *Coat* är ett övre skydds- eller lackskikt. *Sheen* modellerar fina fibrer, sammetseffekt eller damm och är inte samma sak som allmän glans. |
| emission color / strength | emissionsfärg / emissionsstyrka | Principled BSDF:s färg respektive styrka för ljus som sänds ut från materialytan. |
| constraint | begränsning | Blender-relation som styr ett objekt eller ben. Skriv sammansättningar som *positionsbegränsning*, *rotationsbegränsning*, *skalbegränsning* och *avståndsbegränsning*. |
| project axis | projektionsaxel | Axeln som Shrinkwrap projicerar längs. Skilj från ett projekts egen axel. |
| target normal | målnormal | Normal från målets yta, till exempel i Shrinkwrap-projektion. |
| target mesh object | målmeshobjekt | Meshobjektet som Shrinkwrap anpassar ett annat objekt till. Skriv sammansatt; ordet är en teknisk objekttyp. |
| Outside Surface | Utanför ytan | Shrinkwrap-läge där den beräknade punkten hålls på utsidan av målytan. Det är ett läge, inte en benämning på en fristående fysisk yta. |
| joint binding | ledbindning | Spline IK-inställning för leders relativa positioner längs kedjan. |
| curve mapping | kurvkartläggning | Verktyg som mappar färg-, vektor- eller skalärvärden via en användardefinierad kurva. |
| Curve Point / Curve control point | kurvpunkt / kurvkontrollpunkt | Punkt som beskriver en kurvas geometri respektive styr dess form. Skriv den tekniska sammansättningen ihop. |
| Curve Profile presets | Förval, Linje, Stödslingor, Gesimslist, Krönlist, Steg | Geometriska förinställningar i profilbaneredigeraren. *Gesimslist* och *Krönlist* är svenska byggnadstermer för profilernas arkitektoniska listformer. |
| Curve profile point / handle | profilpunkt / handtag | Profilbanans kontrollpunkt och dess Bézierhandtag. Använd *markeringsstatus*, *banpunkt* och *handtagstyp* i de närliggande hjälptexterna. |
| Curve Slice / Curve Splines | kurvsegment / kurvsplines | Ett kurvsegment är en enskild kurva i ett kurvdatablock. Behåll *spline* som Blenderterm och skriv *kurvspline* sammansatt. |
| Dependency Graph / evaluated data-block | beroendegraf / utvärderat datablock | Blenders graf över beroenden och de data som beräknats för aktuell vyport eller renderingen. Skriv API-pluralen *ID:n*. |
| Dependency Graph Object Instance | objektinstans i beroendegrafen | Instans som exponeras av beroendegrafens iterator. Använd *koordinatrymd*, *utvärderat objekt* och *beständigt ID* i API-hjälptexterna. |
| Dependency Graph Update | uppdatering av beroendegrafen | API-objekt som beskriver ett uppdaterat datablock. Statusposterna använder perfekt: *Objektets geometri/skuggning/transformation har uppdaterats*. |
| Dope Sheet filters | Dopebladets filter / filtreringssamling | Filter för animeringsredigerarnas kanaler. Skriv *F-kurvor*, *datablock* och *animeringsdata*; hjälptexterna använder den direkta formen *Visa även …*. |
| Curve Mapping: Clip / White Level | Klipp / Vitnivå | I kurvkartläggningen begränsar *Klipp* kurvvyn till en angiven gräns. *Vitnivå* anger för RGB-kurvor den färg som vitt mappas till. |
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
| FFmpeg audio/video codec | FFmpeg-ljudkodek / FFmpeg-videokodek | Skriv den tekniska sammansättningen ihop. Låt standard- och formatnamn som AAC, H.264, ProRes och WebM stå kvar. |
| sample rate | samplingsfrekvens | Antal ljudprov per sekund i FFmpeg- och ljudinställningar. |
| speaker pitch / mute | tonhöjd / tysta | Högtalarobjektets uppspelningsegenskaper; *Pitch* är inte programmet eller det engelska ordet *pitch*. |
| bitrate | bithastighet | Kodad data per tidsenhet; använd exempelvis *ljudbithastighet* och *konstant bithastighet*. |
| container (media) | behållare | Filformatets omslutande struktur, exempelvis Matroska eller WebM. Använd *behållare för utdatafilen* i hjälptext. |
| mux / mux packet | muxning / muxpaket | Sammanför ljud- och videoströmmar i en mediebehållare. Skriv sammansättningar ihop: *muxningshastighet*, *muxpaketstorlek*. |
| Constant Rate Factor (CRF) | Constant Rate Factor (CRF) | Synligt codec-namn som behålls på engelska med förkortningen CRF. Förklara på svenska som avvägningen mellan videokvalitet och filstorlek. |
| perceptually lossless | visuellt förlustfri | Kvalitetsläge där förlusten inte märks visuellt; undvik det mindre idiomatiska *perceptuellt förlustfri*. |
| seam margin | sömmarginal | Marginal vid fixering av UV-sömmar under målning. |
| UDIM tile | UDIM-platta | En platta i en UDIM-bildtextur. |
| float buffer | flyttalsbuffert | Bildbuffert som lagrar värden som flyttal. |
| library override | biblioteksåsidosättning | Lokal åsidosättning av länkat biblioteksmaterial. |
| ID Library Override Property | egenskap för ID-biblioteksåsidosättning | RNA-typen för en egenskap som hör till en ID-biblioteksåsidosättning. Skriv inte *åsidosättningsegenskap för ID-bibliotek*, eftersom den ordföljden ändrar relationen mellan leden. |
| override data | åsidosättningsdata | Data för en Library Override; använd inte den äldre formen *överskrivningsdata*. |
| system override | systemåsidosättning | Systemskapad Library Override i Outlinern. |
| material override | materialåsidosättning | View Layer-egenskap som ersätter andra material vid rendering. Skilj från en vanlig filöverskrivning. |
| override object | åsidosättningsobjekt | Objekt som styrs av en Blender-åsidosättning; använd med *bibliotekslänkat* när källan avser länkad biblioteksdata. |
| override collection | åsidosätt samling | Operatörsegenskap som skapar en åsidosättning av den valda länkade samlingen. |
| resync (library override) | omsynkronisera / omsynkronisering | Bygger om lokala biblioteksåsidosättningar från länkade referenser; använd inte den mer omständliga formen *synkronisera om* i denna UI-kontext. |
| light probe | ljussond | Objekt som fångar belysningsdata för indirekt ljus och reflektioner. |
| volume light probe | volymljussond | Ljussond som fångar belysningsdata i en 3D-volym. |
| dilation radius / threshold | utvidgningsradie / utvidgningströskel | Parametrar för att fylla ogiltiga prov i en volymljussonds rutnät; avser inte utspädning. |
| bias (light probe) | riktningsförskjutning, normalförskjutning, visningsförskjutning | Teknisk samplingförskjutning. Översätt inte som partiskhet eller fördom. |
| surfel | surfel | Punktbaserat ytelement för global belysning; plural *surfelar*. |
| backface culling | baksidesgallring | Renderingsteknik som döljer ytors baksidor. |
| ray tracing | strålspårning | Renderingsteknik; använd exempelvis *strålspårad transmission*. |
| hair transmission component | komponent som överförs in i håret, reflekteras mot hårets baksida och sedan överförs ut ur håret | Principled Hair BSDF:s fysikaliska ljuskomponent. Använd presens i egenskapsbeskrivningen; *transmitterats* beskriver i stället en redan avslutad strålgång. |
| shadow terminator / geometry, normal, shading offset | skuggterminator / geometriförskjutning, normalförskjutning, skuggningsförskjutning | Cycles gräns mellan ljus och mörker på lågpolygeometri. Offset-inställningarna minskar artefakter genom att justera strålarnas utgångspunkt eller skugggränsen. |
| texture slot | texturplats | Plats som kopplar en textur till ett material eller målningsverktyg. |
| mesh loop | meshloop | Intern meshtopologisk struktur vid ett ythörn; *looptriangel* används för triangulerat resultat. |
| node input / output | nodindata / nodutdata | Nodernas tekniska dataflöde. Använd inte den äldre formen *inmatning* eller *utmatning* i RNA-etiketter. |
| file output item | filutdataobjekt | Objekt som representerar en utdatafil i kompositorns nodstruktur. |
| UV loop layer | UV-looplager | UV-lager som hör till meshens loopar. Använd *UV-looplager*, inte *UV-loopskikt*. |
| remesh / remesher | ommeshning / ommeshare | Skapar om meshen med ny topologi. Ange geometri vid behov: *voxelommeshare* eller *fyrhörningsommeshare*. |
| Remesh Modifier | ommeshningsmodifierare | Modifierare som skapar om meshens topologi. Skriv sammansättningen ihop; ordet är en projektspecifik teknisk term och kan saknas i allmänna ordlistor. |
| remesher | ommeshningsverktyg | Verktyg eller process som bygger om en mesh. Skilj från den specifika *ommeshningsmodifieraren*. |
| pole (mesh topology) | pol | Topologisk samlingspunkt där ett ovanligt antal kanter möts. Översätt inte med den vardagliga betydelsen *stolpe*. |
| vertex color / normal | hörnpunktsfärg / hörnpunktsnormal | Attribut på en mesh-hörnpunkt. |
| node tree | nodträd | Blenders sammanlänkade nodstruktur. Sammansättningar är exempelvis *geometrinodträd*, *kompositionsnodträd* och *shadernodträd*. |
| Node Editor | nodredigerare | UI-namn för redigeraren med nodträd. RNA-beskrivningen *Space Node Editor* använder formen *nodredigerarens område*. |
| Shader Editor | shaderredigerare | UI-namn för nodredigeraren för shaders. Behåll facktermen *shader* och skriv sammansättningen ihop. |
| Texture Node Editor | texturnodredigerare | UI-namn för nodredigeraren för texturer. |
| compositor (process) | komposition | Blender-funktionen för bildkomposition; *Compositor Node Tree* blir *kompositionsnodträd*. |
| selection set | urvalsuppsättning | Namngiven samling av valbara element. |
| delta location | deltaförflyttning | Extra förflyttning som läggs till ett objekts position. |
| empty | tomobjekt | Blender-objekt utan egen geometri, till exempel för referensbilder eller hjälpkontroller. |
| material slot | materialplats | Koppling mellan ett objekt och ett av dess material. |
| world matrix | världsmatris | Transformationsmatris i världsrymden. |
| vertex paint / weight paint / texture paint | hörnpunktsmålning / viktmålning / texturmålning | Blenders respektive målningslägen. |
| gimbal lock | gimbal-låsning | Rotationsproblem i Euler-lägen. |
| instancer | instansierare | Objekt som skapar instanser av sina underordnade objekt eller sin instanssamling. |
| Instance Vertices / Align to Vertex Normal | instanshörnpunkter / Justera efter hörnpunktsnormal | Objektinstansiering från meshens hörnpunkter och dess orienteringsval. |
| alpha blending / alpha test | alfablandning / alfatest | Bildtomobjektens visningsmetoder. Lämna det korta UI-namnet *Alpha* som *alfa*. |
| simulation cache | simuleringscache | Cache för bildrutor vid uppspelning av simuleringsnoder. |
| dynamic topology sculpting | skulptering med dynamisk topologi | Skulpteringsläge som ändrar meshtopologin dynamiskt. |
| child particle | barnpartikel | Partikel som härleds från en föräldrapartikel. |
| distance attenuation | avståndsdämpning | Scenens ljudmodell som minskar ljudstyrkan med avståndet. |
| Doppler effect / pitch factor | dopplereffekt / tonhöjdsfaktor | Ljudinställningar i scenen; *pitch* avser tonhöjd, inte skala. |
| parting (child particles) | bena / benvinkel | Inställning som formar en hårbena bland barnpartiklar utifrån föräldratrådar. Minimi- och maximivärdet är vinklar från rot till spets. |
| Brownian motion | Brownsk rörelse / Brownska rörelser | Slumpmässig och oregelbunden rörelse i en partikelsimulering. |
| volume scatter | volymspridning | Spridning av ljus i ett volymmaterial. |
| ray visibility: camera, diffuse, glossy, shadow, transmission, volume scatter | synlighet för kamera, diffust ljus, blanka reflektioner, skuggor, transmission, volymspridning | Cycles kontroller för vilka stråltyper som kan se objektet. Beskrivningarna använder den mer exakta formen *synlighet för …strålar*. |
| guide hairs | guidehår | Hjälphår som visar eller styr partikelhårets form. |
| strand render | strårendering | Rendering av enskilda hår- eller partikelstrån. |
| subframe | delbildruta | Simuleringssteg mellan hela bildrutor. |
| Courant number | Couranttal | Dimensionslöst tal som begränsar partikelns relativa förflyttning per simuleringsteg. |
| jitter (particle sampling) | slumpvariation | Kontrollerad slumpförskjutning vid sampling, inte nätverksfördröjning. |
| keyed particle loop / keys step | upprepning av nycklar / steg mellan nycklar | Inställningar för partikelbanor med nycklar; avser inte tangentbordstangenter. |
| particle path | partikelbana | Bana som en partikel följer över tid. |
| distance model | avståndsmodell | Modell som styr hur ljudets styrka minskar med avståndet. |
| time remapping | tidsomappning | Omräkning av scenens tid så att bildrutor spelas upp eller renderas vid andra tidpunkter. |
| sequencer | sekvensredigerare | Blenders redigerare för video- och ljudsekvenser. |
| frame dropping | hoppa över bildrutor | Uppspelningsläge som utelämnar bildrutor för att hålla jämna steg med ljudet eller verklig tid. |
| preview range | förhandsgranskningsintervall | Alternativt bildruteintervall för uppspelning och visningsrenderingar. |
| noise (texture) | brus | Procedurtexturens variation; använd inte det fysiska ljudordet *buller*. |
| checker (image texture) | schackmönster | Bildtexturens växlande rutor. |
| normal map | normalkarta | Bild med RGB-värden som kodar ytans normalriktningar. |
| curve map point | kurvkartpunkt | Punkt i en kurvkartläggning. |
| paint curve | målningskurva | Kurva som styr penseldragets förlopp; det är inte en kurva för färg. |
| support loop | stödslinga | Topologisk loop som kontrollerar skärpan kring en meshdetalj. |
| mix mode | blandningsläge | Anger hur en Transform Constraint kombinerar position, rotation eller skala med det ursprungliga värdet. |
| curve slice | kurvsegment | En enskild kurva från ett curves-datablock. |
| curve spline | kurvspline | Spline som hör till en kurva; plural *kurvsplines*. |
| view layer | visningslager | Blender-datalager som bestämmer vilka samlingar och objekt som är synliga vid utvärdering och rendering. Använd inte den inkonsekventa kortformen *vylager*. |
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
| Armature constraint / target bones | armaturbegränsning / målben | Begränsningen använder viktade posetransformationer från ett eller flera målben. Skilj den från armaturmodifieraren. |
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
| Armature (WindowManager) | armatur | Blenders skelettobjekt i tangentmappningar och verktygsnamn. Använd inte *armering*, som är en byggteknisk term. |
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
| Brush Settings / Brush settings | Penselinställningar | Panel- och RNA-rubrik för inställningar som hör till den aktiva penseln. Använd inte *inställningar för borstar*. |
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
| area radius | områdesradie | Förhållande mellan penselradien och radien som används för att sampla områdets mittpunkt. |
| propagation steps | spridningssteg | Utökar automaskeringens mjuka gradient stegvis från en mesh- eller ansiktsgräns. |
| falloff | avtagande | Använd i förklarande Blender-text. Behåll engelska namn när de är formella produkt- eller API-namn. |
| brush spacing | penselavstånd | Avståndet mellan penselavtryck; UI-värdet *Space* kan i relevant panel översättas *Avstånd*. |
| brush stroke method | penseldragsmetod | Väljer hur penseldraget skapas; Grease Pencil använder samma penselstyrning. |
| airbrush | sprutpistol | Penselläget som fortsätter att applicera färg medan musknappen hålls nedtryckt. |
| adaptive spacing | adaptivt penselavstånd | Fördelar penselavtryck efter ytans riktning i stället för i skärmutrymmet. |
| smooth stroke | jämnt penseldrag | Styrning som låter penseln släpa efter markören och följa en jämnare bana. |
| vertex paint | hörnpunktsmålning | Målningsläge som målar färgvärden på meshens hörnpunkter. |
| wet persistence | våt beständighet | Mängden våt färg som stannar kvar i penseln efter målning. |
| wet paint radius | våtmålningsradie | Radie för färgsamplingen som blandas in vid våtmålning. |
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
| area plane mapping | områdesplansmappning | Formellt kartläggningsläge för vektorförskjutning; skilj från områdesradie. |
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
| Action constraint | Action-begränsning | Begränsning som styr en bens pose med en Actions bildrutor. Behåll *Action* som formellt Blender-namn. |
| Action constraint mix modes | före/efter originalet; fullständig/justerad ärvd skalning; delade kanaler | Blandningslägen för en Action-begränning. *Originalet* syftar på ägarens ursprungliga transformation; använd den svenska saktermen i förklaringen, men *Action* är fortsatt datatypnamn. |
| target space | målkoordinatsystem | Koordinatsystemet som används för målbenets transformationskanal. |
| owner space | ägarkoordinatsystem | Koordinatsystemet som används för ägarens transformationskanal. |
| pose space | poseringsrymd | Armaturens poserade koordinatrymd; behåll inte den engelska RNA-etiketten i svensk UI-text. |
| default frame | standardbildruta | Bildruta som motsvarar transformationskanalens neutrala värde. |
| trigger | utlösare | Den styrande åtgärden i Rigifys korrigerande åtgärder. |
| AOV | AOV / godtyckliga utgångsvariabler | Behåll den korta UI-etiketten *AOV*. I förklarande terminologi används TBX-formen *godtyckliga utgångsvariabler*. |
| Shader AOV | shader-AOV | Shaderpass som definieras av användaren. Använd bindestreck före förkortningen AOV; vid fristående etikett används *Shader-AOV*. |

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
| Voronoi Crackle | Voronoi-sprickmönster | Variant av Voronoi-brus som ger ett sprickliknande cellmönster. Undvik den missvisande ljudbetydelsen i *sprakande*. |
| 3D Viewport | 3D-vyport | Använd den etablerade UI-termen när källan uttryckligen säger *viewport*. |
| Viewport Compositor | vyportskompositör | Särskild interaktiv compositor som utvärderas i vyporten. Använd inte den otydliga omskrivningen *visningsområdeskompositör*. |
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
| Stereo 3D | stereoskopisk 3D | Väljs som vyformat för stereobilder och stereovideo. |
| Full precision | fullständig precision | Kompositorns explicita precisionsläge; skilj från tekniska formatnamn och kodekprofiler. |
| codec profile / codec profiles | kodekprofil / kodekprofiler | Använd för profiler som beskriver en kodeks kodningsalternativ. Produktnamn och själva profilvärdena, exempelvis *ProRes 422 HQ*, lämnas oförändrade. |
| codec | kodek | Använd *ljudkodek*, *videokodek* och *komprimeringskodek* i synlig UI-text. Lämna egenskapsnamn som `FFmpegSettings.codec` och formatidentifierare på engelska. |
| Constant Rate Factor (CRF) | Constant Rate Factor (CRF) | FFmpeg-parameter i Blenders videoutdata. Behåll den etablerade parameterbenämningen och förklara dess effekt på svenska. |
| raycast (XR-teleportering) | raycast | Teknisk term i XR-operatorns träffkontroll. Behåll termen men skriv den omgivande hjälprutan idiomatiskt, exempelvis *Färg för raycast vid träff*. |
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
| Camera Solver Constraint | kameralösarbegränsning | Begränsning som gör att en Blender-kamera följer den rekonstruerade rörelsen hos en fysisk kamera från ett filmklipp. |
| compositor (environment) | kompositör | Blenders nodbaserade miljö för bildkomposition; använd *kompositör*, inte det engelska *compositor*. |
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
| mesh edge / mesh face / mesh face corner / mesh loop | meshkant / meshyta / meshytehörn / meshslinga | Meshens topologiska kant, yta, ythörn respektive slinga. |
| vertex (mesh API) | hörnpunkt | RNA-datatypen *MeshVertex* och dess egenskaper; använd sammansättningar som *hörnpunktsvikt*. |
| face (mesh API) | yta | Meshens polygonala yta; undvik det bokstavliga *ansikte* i denna kontext. |
| Freestyle edge/face mark | Freestyle-kant-/ytmarkering | Markerar vilka meshkanter eller -ytor som Freestyle får använda. |
| tagged edge (sharpness) | markerad kant | Kant som har markerats som skarp i utjämningsinställningarna. Skilj från användarskapade *taggar* i tilläggs- och resursgränssnittet. |
| feature edge type | funktionskantstyp | Freestyles urvalskategori för funktionskanter; skriv *funktionskantstyper* i plural. |
| execution time | körtid | Modifierarens uppmätta utvärderingstid, inte verkställighetstid. |
| Geometry Nodes | geometrinoder | Blenders nodbaserade geometriarbetsflöde; svensk sammansättning. |
| Grease Pencil stroke | Grease Pencil-streck | Synlig ritad linje i Grease Pencil, inte *slag* eller *stroke*. |
| Annotation / Grease Pencil stroke | streck | Använd *streck* för det ritade resultatet i Annotation- och Grease Pencil-data. *Penseldrag* används bara när användarens penselhandling uttryckligen avses. |
| Action (animation data type) | Action | Formellt Blender-namn för ett animationsdatablock. Böj som *Actionen* och *Actioner*. Skriv sammansättningar som *Action-grupp*, *Action-lager*, *Action-remsa*, *Action-slot*, *Action-kanal* och *Action-nyckelbildruta*. De fristående etiketterna *Action* och *Actions* följer också denna form när de avser Dope Sheet, NLA, resursfilter eller datablockslistor. Översätt bara det vanliga verbet eller substantivet *action* när det inte betecknar denna datatyp. |
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
| mesh selection mode | val av meshelement | Väljer om hörnpunkter, kanter eller ytor markeras i Blenders Mesh-redigeringsläge. |
| mesh deformation | meshdeformering | Deformeringsmodifierare som använder en mesh eller andra meshobjekt som källa. |
| rigid body | styv kropp | Fysiksimuleringens kroppstyp i Blender. |
| integrator | integrator | Renderingsalgoritm i Cycles; använd svensk böjning i sammansättningar. |
| Geometry Node Group | geometrinodgrupp | Nodgrupp som utvärderar geometri i Blender. |
| Geometry Node Modifier | geometrinodmodifierare | Modifierare som utvärderar en geometrinodgrupp. Skriv *geometrinodmodifierarens gränssnitt*, inte den generiska formen *modifieringsgränssnittet för geometrinoder*. |
| keyframe | nyckelbildruta | En bildruta där ett animerat värde uttryckligen anges. |
| F-Curve | F-kurva | Kurvan som beskriver ett animerat värde över tid. |
| fade (sequencer) | uttoning | Gradvis övergång i bild eller ljud mellan remsor. |
| keymap configuration | tangentmappningskonfiguration | Sparad uppsättning Blender-tangentmappningar. |
| snap keyframes | fäst nyckelbildrutor | Flyttar nyckelbildrutor till bestämda tider, bildrutor eller markörer. |
| NLA stack | NLA-stapel | Lagerordningen för åtgärder och remsor i Nonlinear Animation. |
| keying set | nyckeluppsättning | Namngiven uppsättning animerbara egenskaper som används vid infogning och borttagning av nyckelbildrutor. |
| driver | drivrutin | Uttrycks- eller databaserad styrning av en egenskap; skilj från fysisk hårdvarudrivrutin. |
| bone collection | bensamling | Samling som organiserar riggens ben. |
| Action | Action | Blenderdatablock som lagrar animeringsdata; behåll *Action* i API- och UI-kontexten. |
| Action slot | Action-slot | Identifierar vilken uppsättning animeringskanaler i en Action som gäller för ett datablock. |
| Action keyframe | Action-nyckelbildruta | Nyckelbildruta som hör till en formell Action. |
| Action storage | Action-lagring | Tillfällig eller beständig lagring av en Action i animationsdatatypen. |
| Action Constraint | Action-begränsning | Begränsning som utvärderar en Action för ett objekt eller ben. |
| Action Clip | Action-klipp | NLA-remsa som refererar till en Action. |
| Action Clip Strip | Action-klippsremsa | NLA-remsa med en Action som klipp. |
| Pose Action | pose-Action | Action som innehåller en poses animeringsdata. |
| Fake User | falsk användare | Blender-flagga som får ett datablock, exempelvis en Action, att sparas även utan vanlig användare. |
| layered Action | skiktad Action | Nyare Action-struktur med lager och Action-slotar. |
| legacy Action | äldre Action | Äldre Action-struktur utan lager och Action-slotar. |
| animation channel bag | animationskanalbehållare | API-objekt som samlar F-kurvor och grupper för en Action-slot. |
| kernel optimization | kärnoptimering | Optimering av renderingskärnor i Cycles, inte operativsystemets kärna. |
| intersection | skärningsberäkning | Strålspårningens beräkning av en träff mellan stråle och geometri. |
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
| editor space (RNA) | område | Blenders interna `Space…`-typer beskriver ett redigerarområde, inte ett tredimensionellt rum. |
| editor space data (RNA) | områdesdata | Data för ett specifikt redigerarområde, exempelvis Outliner eller 3D-vyn. |
| Scene linear | scenlinjär | Färghanteringsvärden i arbetsfärgrymden; skriv sammansatt, inte *Scene-linjär*. |
| grid | rutnät | Simulerings-, volym- och partikelrutnät. Undvik det tvetydiga *nät*; undantaget är den synliga Mesh-menyposten *Grid* → *Nät*. |

## Kontrollerade UI-formuleringar

| Engelska | Svenska |
| --- | --- |
| Untitled Project | Namnlöst projekt |
| Folder already contains a project. | Mappen innehåller redan ett projekt. |
| Folder already part of a project | Mappen ingår redan i ett projekt |
| Missing project name | Saknat projektnamn |
| No valid selected objects to copy | Inga giltiga valda objekt att kopiera |
| Cannot copy the linked object '%s' to the internal clipboard | Det går inte att kopiera det länkade objektet ”%s” till det interna urklippet |

| TextLine | TextLine | Internt API-typnamn för en rad i ett Text-datablock; lämnas oförändrat i tekniska beskrivningar. |

## Granskningsregel

Enhetlighet får aldrig gå före funktion. Ändra inte text som är ett formatnamn,
en identifierare eller ett nodnamn enbart för att den liknar en engelsk term.
Kontrollera först Blender-källans användning, Weblates ordlista och den
aktuella svenska UI-kontexten. Kör därefter l10n-lint, svlang och Hunspell på
exporterade ändringar.
