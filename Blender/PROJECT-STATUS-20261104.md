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

Den aktuella komponenten omfattar 40 427 strängar och visas som 100 procent
översatt. Det betyder inte att hela katalogen är radgranskad: vyn visar även
18 403 strängar med förslag och 629 översatta strängar med avfärdade
kontroller. Fortsatt UI-arbete ska därför ske i avgränsade, kontextstyrda
delar och inte utifrån procenttalet ensamt.

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
