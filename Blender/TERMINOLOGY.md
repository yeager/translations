# Blender UI – svensk terminologi

Den här listan gäller Blender UI på Blender Translate. Den är ett stöd för
granskning, inte en ersättning för strängens sammanhang: kontrollera alltid
operator, panel, tooltip, Python-identifierare och närliggande strängar innan
du ändrar en översättning.

Senast uppdaterad: 2026-11-05.

## Grundtermer

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| asset library | tillgångsbibliotek / resursbibliotek | Båda förekommer i den etablerade Blender-katalogen. Följ närliggande UI och ändra inte mekaniskt mellan dem. I Asset Browser och dess inställningsbeskrivningar används *resursbibliotek* för att stämma med de omgivande UI-etiketterna. I övrig längre förklarande text är *tillgångsbibliotek* den vanligaste befintliga formen. |
| Asset Browser | resursbläddrare | Följer den aktuella svenska UI-etiketten. Den äldre manualformen *tillgångsbläddrare* ska inte dras in i ny UI-nära dokumentation. |
| access token | åtkomsttoken | Skriv ihop. Förklarande rubriker får precisera typen: *biblioteksåtkomsttoken* respektive *förrådsåtkomsttoken*. |
| remote asset library | fjärranslutet resursbibliotek | Skriv ut relationen i löpande text; undvik *fjärrresursbibliotek*, som blir svårläst med tre r. |
| remote assets | fjärranslutna resurser | Nätåtkomliga resurser i Asset Browser och dess filter. Undvik *fjärrresurser*, som får tre r i följd. |
| cache directory | cachekatalog | Etablerad teknisk sammansättning i Blender. Skriv ihop i UI-etiketter och statusmeddelanden: *diskcachekatalog*, *standardcachekatalog*. |
| cache layer | cachelager | Lager i en Blender-cachefil. Skriv ihop, utan bindestreck. |
| object path | objektsökväg | Sökväg för ett objekt i exempelvis en Alembic-arkivfil. |
| bake (rendering/simulation) | baka / bakning | Behåll Blenders etablerade verb i procedur- och inställningstexter: *Baka till aktiv kamera*, *bakningsdata*. Det gäller inte köksbetydelsen. |
| normal space | normalrymd | Val av koordinatrymd för normaldata vid bakning. De konkreta alternativen skrivs *tangentrymd*, *objektrymd* och *världsrymd*. |
| onion skinning | lökskalning | Animeringsvisning med spökbilder från närliggande bildrutor. Undvik bokstavliga former som *avskalning av lök*. |
| scope name | scope-namn | Behåll den tekniska källtermen i GPU-felsökningens fångstalternativ. Det är namnet som skickas till `--debug-gpu-scope-capture`, inte Blenders bildanalysvy *Scopes*. |
| Resolution Scale | upplösningsskala | Etablerad UI-term för skalan av teckensnitt och knappar vid visning. |
| File Browser | filbläddrare | UI-beteckning för den editor som öppnar och sparar filer. Anpassa bestämd form i löpande text. |
| file handler | filhanterare | RNA-typ och utbyggnadspunkt som registrerar import-, export- och släpphantering för filer. Översätt inte till *handtag*. |
| File Handler Type | filhanterartyp | UI-etikett för typen av filhanterare. |
| Maximize Area | Maximera område | Operatörsnamn. *Område* avser här ett Blender-area, inte ett skärmområde i allmän mening. |
| 3D Viewport | 3D-vyport | Etablerad UI- och manualterm. |
| 3D View | 3D-vy | Förklaringstext för den synliga Blender-vyn; böj som *3D-vyns* i sammansatta led. |
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
| duplicate and rename | Duplicera och byt namn | Operatör för kopiering av ben med efterföljande namnbyte. |
| working plane | arbetsplan | Etablerad term i Blenders TBX-ordlista. |
| internal clipboard | interna urklippet | UI-funktion, inte operativsystemets urklipp. |
| rigid body | styv kropp | Fysiksimuleringens etablerade term. |
| shader | shader | Behåll den etablerade facktermen i UI och nodnamn. |
| anti-aliasing | kantutjämning | Synlig inställning för text- och bildåtergivning. |
| Subpixel Anti-Aliasing | Kantutjämning på subpixelnivå | Följer den aktuella svenska UI-etiketten. |
| font hinting | teckensnittshintning | Inställning som styr teckenplacering och skärpa i textåtergivning. Den aktuella UI-exportens *Teckensnittshinting* bör hanteras som en separat UI-rättelse, inte kopieras in i manualprosan. |
| point sampling | punktprovtagning | Pipettläge som samplar enskilda punkter till en färggradient. Använd i förklarande UI-former; det dolda tangentbindningsnamnet är *Modal mappning för punktprovtagning med färggradients-pipett*. |
| multisampling | multisampling | Etablerad datorgrafikterm för flera bildprover per pixel, här i Dynamic Paints kantutjämning. Blanda inte ihop med *multisimulering*. |
| Dynamic Paint canvas surface | Dynamic Paint-dukyta | En simulerad yta som tar emot eller visar Dynamic Paint. I plural: *Dynamic Paint-dukytor*. |
| point cache | punktcache | Simuleringscache för punktsystem; skriv ihop. |
| timescale | tidsskala | Faktor som skalar simuleringens tidsförlopp. |
| curve mapping | kurvkartläggning | Kartläggning med kurvor; använd den här sammansättningen i RNA- och modifierarinställningar. |
| retiming key | tidsanpassningsnyckel | Nyckelpunkt i sekvensredigeraren som flyttar en bildruta i en remsa och därmed sträcker eller drar ihop tidsflödet. Följer den etablerade majoritetsformen i UI:t. Använd inte den otydliga och inkonsekventa formen *omtidningsnyckel*. |
| Interface Font | Teckensnitt för gränssnittet | Följer den aktuella svenska UI-etiketten. |
| lighting node | belysningsnod | Använd i saktext; behåll engelska nodnamn där de är produktnamn. |
| geometry node | geometrinod | Svensk sammansättning i förklarande UI-text. |
| node socket interface | noduttagsgränssnitt | RNA-typnamn för ett uttag i ett nodträdsgränssnitt. Behåll fog-s: *färgnoduttagsgränssnitt*, inte *färgnoduttaggränssnitt*. |
| Mix node | blandningsnod | Node Wranglers synliga menyval *Use Mix Nodes* är *Använd blandningsnoder*. |
| Math node | matematisk nod | Node Wranglers synliga menyval *Use Math Nodes* är *Använd matematiska noder*. |
| Divide | Dividera | Den matematiska nodoperationen i Node Wrangler. Använd inte den bredare handlingen *dela upp*. |
| mix factor | blandningsfaktor | Synlig faktor som styr blandning, inte ett kodidentifierarnamn. |
| Alpha Over | Alfa över | Synligt Blender-nodnamn. Som sammansättning: *Alfa över-nod*; Node Wranglers meny använder *alfa-över-noder*. |
| Batch Change | Batchändring / batchändra | Menyetiketten är *Batchändring*. Använd verbformen *batchändra* för en åtgärd, exempelvis en rubrik. |
| Compositor | Kompositör | Synligt Blender-namn för nodredigeraren. Använd *kompositören* i löpande text. |
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
| Grease Pencil | Grease Pencil | Produkt- och funktionsnamn; översätt inte. |
| Grease Pencil layer | Grease Pencil-lager | Lager som samlar relaterade Grease Pencil-ritningar. Behåll produktnamnet men översätt den svenska efterleden. |
| Grease Pencil frame | Grease Pencil-bildruta | Bildruta i ett Grease Pencil-lager; använd inte *ram* i animeringskontext. |
| Grease Pencil masking layer | maskeringslager för Grease Pencil | Lager som begränsar synligheten för Grease Pencil-innehåll. |
| onion skin | lökskal | Den visade tidigare eller senare ritningen. Funktionen heter *lökskalning*. |
| override | åsidosättning / överskrivning | Kontextstyrt. Generella UI-etiketter använder *åsidosättning*. *Library Override* är i den aktuella UI-katalogen *biblioteksåsidosättning*, men närliggande operatörsnamn använder också *biblioteksöverskrivning*. Normalisera aldrig utan att granska strängens sammanhang och närliggande förekomster. |

## Mesh och animering

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| vertex | hörnpunkt / hörn | I mesh- och verktygstext används normalt *hörnpunkt* och sammansättningen *hörnpunkts-*. Den korta etiketten *Vertex* förekommer också som *Hörn* i vissa vy- och orienteringssammanhang. Ändra inte mekaniskt mellan formerna. |
| vertex group | hörnpunktsgrupp | Behåll *VertexGroup* i Python-API, klassnamn och andra identifierare. |
| collision vertex group | hörnpunktsgrupp för kollision | Hörnpunktsgrupp som undantas från tygsimuleringens objektkollisioner. |
| selfcollision vertex group | hörnpunktsgrupp för självkollision | Hörnpunktsgrupp som undantas från tygsimuleringens självkollisioner. |
| tension stiffness | dragstyvhet | Materialets motstånd mot sträckning i tygsimuleringen. |
| vertex mass | hörnpunktsmassa | Massan för en enskild hörnpunkt i tygsimuleringen. |
| vertex color | hörnpunktsfärg | Gäller synlig UI-text. |
| vertex normal | hörnpunktsnormal | Gäller synlig UI-text. |
| vertex index | hörnpunktsindex | Gäller synlig UI-text. |
| edge | kant | Mesh-geometri, inte fönsterkant om UI-kontexten säger annat. |
| face | yta | Mesh-element; avgör i sammanhanget om *ansikte* är avsett i annan betydelse. |
| mesh | mesh | Behåll när det avser Blender-datatypen eller dess etablerade UI-beteckning. |
| bevel | avfasning / fasning | *Avfasning* för UI-egenskapen och modifieraren, *fasning* kan beskriva resultatet i löpande text. |
| Bevel Modifier | avfasningsmodifierare | Blender-modifierarens belagda UI- och manualform. |
| Bevel Vertices / Bevel Edges | Fasa hörnpunkter / Fasa kanter | Synliga operatörsnamn. |
| displacement | förskjutning | Material- och shaderkontext. |
| Vector Displacement | vektorförskjutning | Synlig UI- och manualterm. |
| opacity | opacitet | Använd i UI-reglage för genomskinlighet, till exempel *Opacitet för omarkerade* i F-kurvinställningarna. |
| default settings | standardinställningar | Rubrik för sparade standardval i Inställningar. Följer den befintliga UI-termen för *Defaults*. |
| Adaptive Subdivision | adaptiv underindelning | UI-belagd form; inte *adaptiv indelning*. |
| Material Output | materialutdata | UI-belagd renderings- och nodterm. |
| keyframe | nyckelbildruta | Använd i svensk förklarande text; ändra inte API-namn. |
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
| curve path duration | sökvägsvaraktighet | Antal bildrutor som används för att färdas längs en kurvas sökväg. |
| taper object / taper radius | avsmalningsobjekt / avsmalningsradie | Kurvinställningar som styr profilens bredd längs kurvan. |
| texture space | texturutrymme | Blender-egenskap för automatisk eller manuell texturkoordinering. |
| twist method | vridningsmetod | Beräkningsmetod för 3D-kurvans vridning. |
| translation path | förflyttningsbana | Kurvbana som styr ett underordnat objekts rörelse; inte en språklig översättning. |
| text box overflow | textruteöverflöde | Hantering när text inte ryms i Blenders textrutor. |
| small caps | kapitäler | Typografisk stil med små versaler; använd inte vardagsformen *små huvudstäder*. |
| shear | skjuvning | Geometrisk transformering eller textobjektets kursiveringsvinkel. |
| Freestyle line style | Freestyle-linjestil | Freestyles inställningsobjekt för den renderade konturlinjen. |
| stroke geometry | streckgeometri | Geometrin för ett Freestyle-streck; inte *slaggeometri*. |
| chain vertex | kedjehörnpunkt | Hörnpunkt i Freestyles kedja av funktionskanter. |
| chain splitting | kedjedelning | Freestyle-funktion som delar en kedja utifrån längd eller mönster. |
| split length | delningslängd | Kurvlinjär 2D-längd som används vid Freestyle-kedjedelning. |
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
| rig | rigg | Riggningens styrstruktur för en armatur. Behåll den svenska facktermen i löpande dokumentation. |
| meta-rig | metarigg | Rigifys förenklade armatur som används för att generera den färdiga riggen. Skriv ihop på svenska. |
| sub-rig | underrigg | Standardiserad Rigify-komponent. Skriv ihop i singular och i sammansättningar, till exempel *underriggtyp*. |
| Rigify Human | Rigify Human | Namn på Rigifys förinställda mänskliga metarigg; översätt inte som löpande text. |
| tweak control | finjusteringskontroll | En kontroll för lokala deformationer i Rigify. Använd inte det engelska *tweak* i förklarande svensk text. |
| unhide | visa | I Blenders hierarki betyder åtgärden att ett dolt objekt visas igen, inte att det döljs. |
| Armature modifier | armaturmodifierare | Modifieraren som kopplar en mesh till en armatur för deformering. |
| automatic weights | automatiska vikter | Viktmålningsmetod för att koppla meshens hörnpunkter till armaturens ben. |
| widget | widget | Rigifys redigerbara kontrollobjekt. I sammansättning används *widgetobjekt*, *widgetsamling* och *widgetmesh*. |
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
| bone collection | bensamling | Blender-samling för ben; skriv ihop i synlig UI-text. |
| Envelope deform | kuvertdeformering | Deformeringsmetoden som använder benens kuvertvolymer; använd i Bens/Armaturens egenskaper. |
| armature-relative | relativt riggskelett | Position eller orientering uttryckt i armaturens lokala koordinatsystem. |
| inherit scale | ärv skala | Armaturinställning som styr hur ett underordnat ben tar emot skalning från ett överordnat ben. |
| shear | skjuvning | Skev transformationskomponent i armatur- och matrisinställningar; använd inte vardagliga *saxning*. |
| bone tail | svans | Änden på ett Blender-ben i dataegenskaper. I vissa constraints används däremot den etablerade räknade formen *spets*. |
| connected bone | anslutet ben | Ett underordnat bens huvud är fast vid det överordnade benets svans. |
| envelope influence | kuvertets påverkan | Påverkan från ett bens Envelope-volym vid armaturdeformering. |
| relative parenting | relativ överordning | Armaturinställning som låter underordnade objekt använda relativ transformering. |
| scale easing | skalutjämning | B-Bone-inställning som skalar de slutliga utjämningsvärdena med Y-faktorerna för Skala in/ut. |
| library override | biblioteksöverskrivning | Lokal ändring av länkat biblioteksmaterial i aktuell Blender-fil. |
| effective visibility | effektiv synlighet | Synlighet som beror på både bensamlingen och alla dess överordnade samlingar. |
| selection set | urvalsuppsättning | Rigify-inställning som samlar ben för ett styrt urval. |
| color set | färguppsättning | Namngiven grupp av benfärger i Rigify. |
| brush capabilities | penselfunktioner | Skrivskyddad uppsättning tillgängliga egenskaper för en pensel. |
| brush | pensel | Använd för Blender-verktyget i målning, skulptering och Grease Pencil. Undvik den felaktiga formen *borste* i nya UI-strängar. |
| brush stroke | penseldrag | Ett sammanhängande drag med penseln. Skilj från Grease Pencil-*streck*, som är det ritade resultatet. |
| brush dab | penselavtryck | Enskilt delavtryck i ett penseldrag. |
| brush falloff | penselns avtagande | Hur penselns påverkan minskar med avståndet från centrum eller gräns. |
| falloff | avtagande | Använd i förklarande Blender-text. Behåll engelska namn när de är formella produkt- eller API-namn. |
| brush spacing | penselavstånd | Avståndet mellan penselavtryck; UI-värdet *Space* kan i relevant panel översättas *Avstånd*. |
| brush tip | penselspets | Penselns form och riktning vid målning eller skulptering. |
| mask texture | masktextur | Textur som begränsar en pensels påverkan. |
| texture overlay | texturöverlägg | Visas ovanpå arbetsytan vid målning. |
| plane offset | planförskjutning | Förskjuter skulpteringsplanet i förhållande till ytan. |
| plane trim | plantrimning | Begränsar hur långt från det förskjutna planet en hörnpunkt påverkas. |
| area normal | områdesnormal | Normal som används för ett område i skulpterings- och automaskningsinställningar. |
| view normal | visningsnormal | Normal uttryckt i förhållande till 3D-vyn. |
| face set | ansiktsuppsättning | Skulpteringsgrupp av meshytor. Skriv sammansättningar som *ansiktsuppsättningsgräns*. |
| radius falloff | radieavtagande | Avtagande som styrs av radie i pensel- och skulpteringsinställningar. |
| smooth stroke | jämnt penseldrag | Penselinställning som filtrerar markörens rörelse under draget. |
| space attenuation | avståndsdämpning | Dämpar penselstyrkan utifrån mellanrummet mellan penselavtryck. |
| sculpt capabilities | funktioner för skulptering | Skrivskyddad uppsättning tillgängliga egenskaper för skulpteringsverktyget. |
| vertex paint | hörnpunktsmålning | Målningsläge som tilldelar färgdata till meshens hörnpunkter. |
| weight paint | viktmålning | Målningsläge som tilldelar vikter till meshens hörnpunkter. |
| curve parameter falloff | avtagande längs kurvparametern | Gradvis förändring av en kurvpensels verkan från spetsen till roten. |
| curve radius | kurvradie | Radien för en kurva som skapas eller påverkas av kurvpenseln. |
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
| NDOF | NDOF | Behåll enhetens produktförkortning; översätt den efterföljande synliga åtgärden med liten begynnelsebokstav. |
| keyframe | nyckelbildruta | Grundterm för animeringspunkt på en F-kurva. |
| quartic/quintic interpolation | fjärdegradig/femtegradig interpolering | Matematiska interpoleringsord; inte kvadratisk eller engelska funktionsnamn. |
| Keying Set | nyckeluppsättning | Samling av egenskapsvägar som får nyckelbildrutor tillsammans. |
| Keying Set Path | sökväg för nyckeluppsättning | RNA-sökväg som hör till en nyckeluppsättning. |
| line style modifier | linjestilsmodifierare | Freestyle-modifierare för streckens egenskaper. |

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
