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

Den aktuella komponenten omfattar 40 427 strängar och visas som 100 procent
översatt. Det betyder inte att hela katalogen är radgranskad: vyn visar även
18 403 strängar med förslag och 629 översatta strängar med avfärdade
kontroller. Fortsatt UI-arbete ska därför ske i avgränsade, kontextstyrda
delar och inte utifrån procenttalet ensamt.

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
