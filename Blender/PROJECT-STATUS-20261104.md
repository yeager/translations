# Blender: projektstatus 5 november 2026

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
l10n-lint och diffkontroll. Något importresultat för denna samlade fil är ännu
inte verifierat.
