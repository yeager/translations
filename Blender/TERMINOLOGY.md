# Blender UI – svensk terminologi

Den här listan gäller Blender UI på Blender Translate. Den är ett stöd för
granskning, inte en ersättning för strängens sammanhang: kontrollera alltid
operator, panel, tooltip, Python-identifierare och närliggande strängar innan
du ändrar en översättning.

Senast uppdaterad: 2026-11-04.

## Grundtermer

| Engelska | Svenska | Anmärkning |
| --- | --- | --- |
| asset library | tillgångsbibliotek / resursbibliotek | Båda förekommer i den etablerade Blender-katalogen. Följ närliggande UI och ändra inte mekaniskt mellan dem. I längre förklarande text är *tillgångsbibliotek* den vanligaste befintliga formen. |
| add-on / extension | tillägg | I Blender betecknar båda källtermerna samma utbyggbara funktion. Svenska använder samma form i singular och plural i korta UI-etiketter. |
| data-block | datablock | Skriv ihop. Behåll bindestrecket bara i bokstavliga API-namn. |
| object | objekt | Etablerad Blender-term. |
| collection | samling | Avser Blenders objektbehållare, inte en godtycklig lista. |
| project | projekt | Avser Blenders projektkatalog och dess inställningar. |
| project settings | projektinställningar | Exempel: *Open Project Settings* → *Öppna projektinställningar*. |
| workspace | arbetsyta | Den etablerade UI-formen, exempelvis *Workspace* → *Arbetsyta*. |
| pie menu | cirkelmeny | Följer den aktuella svenska Blender-UI-katalogen. |
| Essentials | Grundresurser | Översatt UI-namn för Blenders medföljande resurser. I löpande text: *resursbiblioteket Grundresurser*. |
| Cyclic | Cyklisk | Kurv- och splineinställning. Skriv vid behov *alternativet Cyklisk* för korrekt svensk kongruens. |
| Numeric Input Arrows | Numeriska inmatningspilar | Följer den faktiska svenska UI-etiketten. |
| timeout | tidsgräns | Exempel: *Animation Timeout* → *Animationstidsgräns*. |
| linked | länkad | Exempel: *linked object* → *länkat objekt*. |
| packed | packad | Exempel: *packed data-block* → *packat datablock*. |
| parent | förälder | Blender-hierarki, exempelvis *Parent* → *Förälder*. |
| parenting | föräldrarelation | Beskriver relationen mellan objekt eller ben. Använd inte *överordning* när det är själva relationsslaget som avses. |
| bone roll | benrullning | Etablerad svensk UI-term för ett bens rotationsriktning kring längdaxeln. |
| rest pose | viloposition | Använd i förklarande armaturtext. Bevara RST-termmål som `<rest pose>`. |
| duplicate and rename | Duplicera och byt namn | Operatör för kopiering av ben med efterföljande namnbyte. |
| working plane | arbetsplan | Etablerad term i Blenders TBX-ordlista. |
| internal clipboard | interna urklippet | UI-funktion, inte operativsystemets urklipp. |
| rigid body | styv kropp | Fysiksimuleringens etablerade term. |
| shader | shader | Behåll den etablerade facktermen i UI och nodnamn. |
| anti-aliasing | kantutjämning | Synlig inställning för text- och bildåtergivning. |
| subpixel anti-aliasing | subpixelutjämning | Variant av kantutjämning; skriv ihop. |
| font hinting | teckensnittshintning | Inställning som styr teckenplacering och skärpa i textåtergivning. |
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
