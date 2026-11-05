# Blender UI – svensk terminologi

Den här listan gäller Blender UI på Blender Translate. Den är ett stöd för
granskning, inte en ersättning för strängens sammanhang: kontrollera alltid
operator, panel, tooltip, Python-identifierare och närliggande strängar innan
du ändrar en översättning.

Senast uppdaterad: 2026-11-05.

## Grundtermer

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| asset library | tillgångsbibliotek / resursbibliotek | Båda förekommer i den etablerade Blender-katalogen. Följ närliggande UI och ändra inte mekaniskt mellan dem. I längre förklarande text är *tillgångsbibliotek* den vanligaste befintliga formen. |
| Asset Browser | resursbläddrare | Följer den aktuella svenska UI-etiketten. Den äldre manualformen *tillgångsbläddrare* ska inte dras in i ny UI-nära dokumentation. |
| access token | åtkomsttoken | Skriv ihop. Förklarande rubriker får precisera typen: *biblioteksåtkomsttoken* respektive *förrådsåtkomsttoken*. |
| remote asset library | fjärranslutet resursbibliotek | Skriv ut relationen i löpande text; undvik *fjärrresursbibliotek*, som blir svårläst med tre r. |
| scope name | scope-namn | Behåll den tekniska källtermen i GPU-felsökningens fångstalternativ. Det är namnet som skickas till `--debug-gpu-scope-capture`, inte Blenders bildanalysvy *Scopes*. |
| Resolution Scale | upplösningsskala | Etablerad UI-term för skalan av teckensnitt och knappar vid visning. |
| File Browser | filbläddrare | UI-beteckning för den editor som öppnar och sparar filer. Anpassa bestämd form i löpande text. |
| Maximize Area | Maximera område | Operatörsnamn. *Område* avser här ett Blender-area, inte ett skärmområde i allmän mening. |
| 3D Viewport | 3D-vyport | Etablerad UI- och manualterm. |
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
| parent | förälder | Blender-hierarki, exempelvis *Parent* → *Förälder*. |
| Graph Editor | grafredigerare | UI-namn för redigeraren med F-kurvor. Använd bestämd form i löpande text: *i grafredigeraren*. |
| Dope Sheet | Dopeblad | UI-namn. Använd bestämd form i löpande text: *i dopebladet*. |
| Action Editor | åtgärdsredigerare | UI-namn; *åtgärdsredigeraren* i löpande text. |
| Value Slider | värdereglage | UI-term för ett specifikt reglage. Behåll *skjutreglage* för den generella regionen och etiketten *Show Sliders*. |
| Outliner | Outliner | Etablerat produktnamn i Blender-manualen. Behåll det på engelska; böj vid behov som *i Outliner*. |
| linked duplicate | länkad dubblett | Dokumentationens singularform för ett nytt objekt som delar samma objektdata. Den synliga pluraloperatören *Linked Duplicate* kan ha en egen UI-form. |
| parenting | föräldrarelation | Beskriver relationen mellan objekt eller ben. Använd inte *överordning* när det är själva relationsslaget som avses. |
| bone roll | benrullning | Etablerad svensk UI-term för ett bens rotationsriktning kring längdaxeln. |
| rest pose | viloposition | Använd i förklarande armaturtext. Bevara RST-termmål som `<rest pose>`. |
| duplicate and rename | Duplicera och byt namn | Operatör för kopiering av ben med efterföljande namnbyte. |
| working plane | arbetsplan | Etablerad term i Blenders TBX-ordlista. |
| internal clipboard | interna urklippet | UI-funktion, inte operativsystemets urklipp. |
| rigid body | styv kropp | Fysiksimuleringens etablerade term. |
| shader | shader | Behåll den etablerade facktermen i UI och nodnamn. |
| anti-aliasing | kantutjämning | Synlig inställning för text- och bildåtergivning. |
| Subpixel Anti-Aliasing | Kantutjämning på subpixelnivå | Följer den aktuella svenska UI-etiketten. |
| font hinting | teckensnittshintning | Inställning som styr teckenplacering och skärpa i textåtergivning. Den aktuella UI-exportens *Teckensnittshinting* bör hanteras som en separat UI-rättelse, inte kopieras in i manualprosan. |
| Interface Font | Teckensnitt för gränssnittet | Följer den aktuella svenska UI-etiketten. |
| lighting node | belysningsnod | Använd i saktext; behåll engelska nodnamn där de är produktnamn. |
| geometry node | geometrinod | Svensk sammansättning i förklarande UI-text. |
| Grease Pencil | Grease Pencil | Produkt- och funktionsnamn; översätt inte. |
| override | åsidosättning / överskrivning | Kontextstyrt. Generella UI-etiketter använder *åsidosättning*. *Library Override* är i den aktuella UI-katalogen *biblioteksåsidosättning*, men närliggande operatörsnamn använder också *biblioteksöverskrivning*. Normalisera aldrig utan att granska strängens sammanhang och närliggande förekomster. |

## Mesh och animering

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| vertex | hörnpunkt / hörn | I mesh- och verktygstext används normalt *hörnpunkt* och sammansättningen *hörnpunkts-*. Den korta etiketten *Vertex* förekommer också som *Hörn* i vissa vy- och orienteringssammanhang. Ändra inte mekaniskt mellan formerna. |
| vertex group | hörnpunktsgrupp | Behåll *VertexGroup* i Python-API, klassnamn och andra identifierare. |
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
| Adaptive Subdivision | adaptiv underindelning | UI-belagd form; inte *adaptiv indelning*. |
| Material Output | materialutdata | UI-belagd renderings- och nodterm. |
| keyframe | nyckelbildruta | Använd i svensk förklarande text; ändra inte API-namn. |
| F-Curve | F-kurva | Behåll initialen och använd svenskt ord efter bindestrecket. |
| action | åtgärd | Animeringsdata i Blender. Behåll *Action* i formella datatyp- eller API-namn. |
| slot | slot | Etablerat i den aktuella Blender-dokumentationen och UI-kontexten. |
| shape key | formnyckel | Etablerad term i Blenders TBX-ordlista och UI. |
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
