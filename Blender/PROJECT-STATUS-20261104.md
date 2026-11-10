# Blender: projektstatus 5 november 2026

Senaste lokala arbete: 10 november 2026.

Projektets aktualitet är verifierad 9 november 2026: Blender 5.2 LTS
släpptes den 14 juli 2026 enligt Blenders officiella releasesida. Projektet
uppfyller därmed 48-månadersregeln för fortsatt omfattande granskning.

> Den aktuella källexporten är `blender-ui-ui-sv (7).po`, hämtad 10 november
> 2026. Den är arbetsreferensen för nya deltafiler. Jämförelser med tidigare
> exporter bekräftar att manuella importer har fått genomslag, men en deltafil
> räknas inte som importerad förrän importresultatet är verifierat.

## Batch 1 652 — API-definierad

UI-statusen `API Defined` använder nu adjektivet **API-definierad** i stället
för substantivet *API-definition*. Deltafilen
`blender-ui-sv-reviewed-batch-1652-api-defined-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll,
Gitleaks, Hunspell och svlang passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 651 — Rigify: exempel

Rigifys kommando `Add sample` avser ett metariggsexempel och använder nu
**Lägg till exempel** i stället för det missvisande *sampel*. Deltafilen
`blender-ui-sv-reviewed-batch-1651-rigify-sample-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll,
Gitleaks, Hunspell och svlang passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 650 — Rigify: funktionsuppsättningens arkiv

Rigifys felmeddelande använder nu **funktionsuppsättningens arkiv** i stället
för det otydliga *funktionsarkiv*. Deltafilen
`blender-ui-sv-reviewed-batch-1650-rigify-feature-set-archive-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Hunspell och svlang
rapporterade endast Python-filnamnet `__init__.py`. Ingen import är verifierad
för denna batch.

## Batch 1 649 — Node Wrangler: blandningsfaktor

Node Wranglers kommando för att öka Mix Factor med 0,01 använder nu samma
term, **blandningsfaktor**, som de angränsande kommandona. Deltafilen
`blender-ui-sv-reviewed-batch-1649-node-wrangler-mix-factor-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll, Gitleaks, Hunspell och svlang passerade utan anmärkningar. Ingen
import är verifierad för denna batch.

## Batch 1 648 — Cycles vyport

Cycles UI använder nu **vyport**, **vyporter** och **rendering i vyporten**
konsekvent i stället för *visningsområde*. Deltafilen
`blender-ui-sv-reviewed-batch-1648-cycles-viewport-terminology-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Hunspell och svlang
rapporterade endast projekttermerna *vyport*, *BVH* och
*blåbrussamplingsmönster*. Ingen import är verifierad för denna batch.

## Batch 1 647 — gizmons fästning

Den allmänna gizmons nyckelåtgärder använder nu **Aktivera fästning** och
**Inaktivera fästning** i stället för *snäppning*. Deltafilen
`blender-ui-sv-reviewed-batch-1647-gizmo-snap-terminology-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 646 — fästpunkter och provtagning

Transformeringsverktygets åtgärder använder nu **fästbas**, **fästpunkt** och
**fästning** i stället för *snäpp*. Pipettens åtgärder använder svenskans
**provtagning** i stället för lånet *sampling*. Deltafilen
`blender-ui-sv-reviewed-batch-1646-transform-snap-sampling-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 645 — invertera fästning

Nod- och transformeringsverktygets åtgärd *Snap Invert* använder nu
**Invertera fästning** i stället för *snäppning*. Deltafilen
`blender-ui-sv-reviewed-batch-1645-node-snap-invert-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad.

## Batch 1 644 — axelfästning

3D-vyns tangentbordsåtgärder använder nu **axelfästning** i stället för
det inkonsekventa lånet *axelsnäppning*. Deltafilen
`blender-ui-sv-reviewed-batch-1644-axis-snap-terminology-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 643 — skulpteringsfästning och gåläge

Skulpteringsverktyget använder **Fäst utvidgningen vid ytuppsättningar** och
gålägets avslutsåtgärd anger nu korrekt **hopptangenten**. Två relaterade
nyckelåtgärder använder också **fästning** i stället för *snäppning*.
Deltafilen `blender-ui-sv-reviewed-batch-1643-sculpt-snap-walk-keymap-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 642 — fästning i tangentbordsåtgärder

Tangentbordsåtgärdernas **Snap** och **Snapping** använder nu den etablerade
Blender-termen **fäst/fästning**. Det ersätter det inkonsekventa och onödiga
lånet *snäpp*. Deltafilen
`blender-ui-sv-reviewed-batch-1642-snap-keymap-terminology-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 641 — kurvhandtag och vinkelinfästning

Två kurvredigerarposter använder nu saktermen **handtag** i stället för den
felaktiga **markör**. Vinkelinfästning följer den befintliga Blender-termen
**fäst**; både tangentbordsåtgärden och kurvpennans etikett är normaliserade.
Deltafilen `blender-ui-sv-reviewed-batch-1641-curve-handle-snap-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 640 — kurvverktygets slumpning

Kurvredigerarens kommandetikett använder nu verbet **slumpa**, i samma
verktygskontext som den tidigare granskade meshetiketten. Den felaktiga
adjektivformen *slumpmässigt* är borttagen. Deltafilen
`blender-ui-sv-reviewed-batch-1640-curve-tool-label-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad för denna
batch.

## Batch 1 626 — kamerafixering och markeringsläge

Tre UI-poster från arbetsreferensen har granskats i sin Blender-RNA-kontext.
*Camera Fix* använder nu konsekvent **kamerafixering** för rotation och skala,
och Grease Pencils inställning *Select Mode* är **Markeringsläge**, i linje
med övriga Blender-etiketter. Deltafilen
`blender-ui-sv-reviewed-batch-1626-camera-fix-selection-mode-20261110.po` är
lokal och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll och
Gitleaks passerade; inga varningar eller hemligheter rapporterades. Ingen
import är verifierad för denna batch.

## Batch 1 627 — fästning och projicering

Två verktygsinställningar har normaliserats i sin konkreta
fästnings-/transformationskontext: *Snap Animation Element* är
**Fästelement för animering** och *Project Mode* är **Projiceringsläge**.
Deltafilen `blender-ui-sv-reviewed-batch-1627-snap-terminology-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 628 — vyport vid verktygsdragning

En verktygshjälptext använder den etablerade Blender-termen **vyport** i
stället för det generiska *visningsfönster*. Deltafilen
`blender-ui-sv-reviewed-batch-1628-viewport-wording-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad för denna
batch.

## Batch 1 629 — vyportens bakgrundsfärg

En 3D-vyhjälptext är normaliserad till den etablerade Blender-termen
**vyport**: inaktiv geometri tonas ut med **vyportens bakgrundsfärg**.
Deltafilen `blender-ui-sv-reviewed-batch-1629-viewport-background-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 630 — vyportöverlägg och siktförhållanden

Fyra 3D-vyhjälptexter använder nu konsekvent **vyport**. En sakfelaktig
subjektsrelation vid retopologi är också rättad: urvalet **skymms av**
inaktiv geometri, inte tvärtom. Deltafilen
`blender-ui-sv-reviewed-batch-1630-viewport-overlay-wording-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 631 — vyport vid skuggningsinställningar

Två 3D-skuggningshjälptexter använder nu konsekvent **vyport**. Deltafilen
`blender-ui-sv-reviewed-batch-1631-viewport-shading-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad för denna
batch.

## Batch 1 632 — vyport i renderings- och förhandsvisningsinställningar

Fyra relaterade 3D-skuggningsposter använder nu konsekvent **vyport**:
renderingspass, skuggning, kompositörsförhandsvisning och skärpedjup.
Deltafilen `blender-ui-sv-reviewed-batch-1632-viewport-shading-terms-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 633 — volymvisning och felmeddelande

Två volymposter är rättade: visningssammanhanget är **vyporten** och
felmeddelandet anger nu korrekt att inläsningen av rutnät misslyckades.
Deltafilen `blender-ui-sv-reviewed-batch-1633-volume-display-wording-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 634 — XR-åtgärdsposer

En XR-hjälptext skiljer nu korrekt mellan den generella *action* och Blenders
datatyp **Action**: **Åtgärdsposerna** används för VR-kontrollernas grepp.
Deltafilen `blender-ui-sv-reviewed-batch-1634-xr-action-terminology-20261110.po`
är lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 635 — XR-navigation och vyport

Sex XR-poster har rättats i sin API-kontext: användarväg, smidig svängning,
basposetyp och VR-vyportens klippavstånd. Deltafilen
`blender-ui-sv-reviewed-batch-1635-xr-navigation-wording-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 636 — XR-kontrollenhetsstil

Tre stilalternativ för XR-kontrollenheter har fått svensk och konsekvent
formulering: **kontrollenhet** och **stråle**. Deltafilen
`blender-ui-sv-reviewed-batch-1636-xr-controller-style-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad för denna
batch.

## Batch 1 637 — Gizmo-etiketten Press

Gizmo-inställningens etikett *Press* är rättad från den ofullständiga
uppmaningen **Tryck på** till **Tryck**. Deltafilen
`blender-ui-sv-reviewed-batch-1637-gizmo-press-label-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad för denna
batch.

## Batch 1 638 — MMB-åtgärd i vyporten

Hjälptexten för mittersta musknappens dragåtgärd använder nu konsekvent
**vyporten**. Deltafilen
`blender-ui-sv-reviewed-batch-1638-mmb-viewport-wording-20261110.po` är
lokalt kontrollerad och klar för manuell import. `msgfmt`, l10n-lint,
diffkontroll och Gitleaks passerade utan anmärkningar. Ingen import är
verifierad för denna batch.

## Batch 1 639 — etiketter för meshverktyg

Två verktygsetiketter är normaliserade så att reserv- och standardvägen har
samma verbform: **mäta** respektive **slumpa**. Deltafilen
`blender-ui-sv-reviewed-batch-1639-mesh-tool-labels-20261110.po` är lokalt
kontrollerad och klar för manuell import. `msgfmt`, l10n-lint, diffkontroll
och Gitleaks passerade utan anmärkningar. Ingen import är verifierad för denna
batch.

## Verifierad manuell import — 10 november 2026, efter kl. 07.00

Den samlade lokala deltafilen
`blender-ui-sv-reviewed-since-0700-20261110.po` importerades manuellt i
Blender Translate. Resultatet som visades av tjänsten var **233 behandlade**
poster: **169 uppdaterade**, **64 hoppade över** och **0 saknade**. Importen
är därmed verifierad. Upstreamgranskning, eventuell senare källsynkning och
merge har inte verifierats i detta steg.

## Helkatalogskontroll av export `(6)`

Måltexterna i hela UI-exporten kontrollerades 9 november med msgfmt,
l10n-lint, svlang och Hunspell-sv. Svengelska rapporterar endast `startup`,
som avsiktligt behålls eftersom det är ett synligt standardkatalognamn.
Skrivregelsträffarna gäller kod- och formatexempel, bland annat
`(dot(B, C) < 0) ? A : -A`, `{:d} .. {:d}`, tangentetiketten `Numpad .` och
platshållarsträngar med `%s`; de ska inte svenskredigeras. Hunspell-sv:s
vanligaste träffar är etablerade Blender- och 3D-termer som *mesh*, *Grease
Pencil*, *Action*, *modifieraren*, *nodgrupp* och *vyport*. Ingen ny
högsäker svensk rättning skapades i denna kontroll.

`svlang check` ger på hela PO-filen tusentals heuristiska V2- och
naturlighetsträffar eftersom Blender-RNA, Python, formatnamn och UI-fragment
tolkas som vanlig prosa. Resultatet används därför bara för att välja ut
kandidater till radgranskning, aldrig för automatiska rättningar eller som
ett kvalitetsmått. De sju interpunktionsindikeringarna pekar på formaterad
käll-/kodtext, inte svenska måltexter.

## Batch 1 361 — samlad importfil för godkända UI-rättningar

Den här importfilen samlar de 20 redan kontextgranskade posterna från
batcherna 1 354–1 359 i en enda PO-fil, baserad direkt på export `(6)`.
Den omfattar generell *rendering*, Cycles relativa renderingshastighet,
bestämda index-, världs- och objektrymder, *tangentmappning* och
*visningsnod*. Den ersätter inte de enskilda batcharnas dokumentation, men
gör manuell import enklare. Filen
`blender-ui-sv-reviewed-batch-1361-approved-deltas-20261109.po` är lokal och
klar för manuell import; ingen Blender Translate-import är verifierad för den.

`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Hunspell-sv träffar endast avsiktliga Blender-/tekniknamn och synliga
katalognamn: *BSDF:er*, *EEVEE*, *OpenPBR-modellen*, *add-ons*, *modules*,
*presets*, *visningsnoden* och *voxeln*. Svlang föreslår en översättning av
`startup`, men termen är avsiktligt kvar som Blenders synliga underkatalognamn.
SHA-256 är `39ee41ab3f0700af59053bd71aa25ea8ca0f86757ae460dbbd43228d84f6d7ce`.

## Batch 1 354 — generisk renderings-terminologi

Batchen normaliserar sex aktuella UI-poster från den färska exporten:
*full rendering*, renderingsbeskrivningar för hår, ytmaterial och
materialutdata, Shader to RGB samt *Textrendering*. Den skiljer den generella
Blender-processen **rendering** från den mer specifika termen *återgivning*.
Deltafilen `blender-ui-sv-reviewed-batch-1354-rendering-terminology-20261109.po`
är lokal och klar för manuell import; ingen import har utförts i detta steg.
`msgfmt`, l10n-lint, svlang (konsistens, skrivregler och svengelska), Hunspell-sv
och Gitleaks har körts. Hunspell-sv:s enda träffar är de avsiktliga
fack-/produkttermerna *BSDF:er*, *EEVEE* och *OpenPBR-modellen*.

## Batch 1 355 — kataloglistans skiljetecken

En granskad hjälprad för en alternativ skriptsökväg saknade kolon före listan
med Blenders formella underkatalognamn. Deltafilen
blender-ui-sv-reviewed-batch-1355-script-directory-punctuation-20261109.po
är lokal och klar för manuell import. Kontrollerna msgfmt, l10n-lint,
svlang, Hunspell-sv och Gitleaks är genomförda. Svlang rapporterar
startup som en anglicism, men termen behålls avsiktligt eftersom den är
ett synligt katalognamn i Blenders standardlayout.

## Batch 1 356 — Cycles kärnoptimeringens renderingshastighet

Två korta Cycles-beskrivningar hade formen *långsammaste/snabbaste
renderingen*, trots att de beskriver relativa hastighetslägen. De är
normaliserade till *långsammast/snabbast rendering*. Deltafilen
blender-ui-sv-reviewed-batch-1356-cycles-rendering-speed-20261109.po är lokal
och klar för manuell import; någon import har inte genomförts här. Msgfmt,
l10n-lint, svlang och Gitleaks är godkända.

## Batch 1 357 — indexrymder i Geometry Nodes

Sex Geometry Nodes-hjälptexter syftar på den specifika referensrymden för
voxel- och rutnätskoordinater. Bestämd form används därför konsekvent:
*i indexrymden* och *i rutnätsindexrymden*. Deltafilen
blender-ui-sv-reviewed-batch-1357-index-space-definiteness-20261109.po är
lokal och klar för manuell import. Msgfmt, l10n-lint, svlang och Gitleaks är
godkända.

## Batch 1 358 — tangentmappning, visningsnod och världsrymd

Fyra UI-poster återställs till etablerad Blender-terminologi: *keymap* blir
*tangentmappning*, *Viewer Node* blir *visningsnod* och den aktuella
referensrymden blir *världsrymden*. Deltafilen
blender-ui-sv-reviewed-batch-1358-keymap-viewer-world-space-20261109.po är
lokal och klar för manuell import. Msgfmt, l10n-lint, svlang och Gitleaks är
godkända.

## Batch 1 359 — kamerans objektrymdsbegränsning

Kameraprojektionens hjälptext preciseras så att varje sida hör till
*objektrymdens begränsningsruta*, i stället för den tvetydiga formuleringen
om en begränsningsbox i objektrymd. Deltafilen
blender-ui-sv-reviewed-batch-1359-camera-object-space-bounds-20261109.po är
lokal och klar för manuell import. Msgfmt, l10n-lint, svlang och Gitleaks är
godkända.

## Verifierad manuell import 9 november 2026

Två manuella Blender Translate-importer är dokumenterade i arbetsloggen. Den
första bearbetade 213 strängar: 111 uppdaterades, 102 hoppades över och inga
saknade. Den senare bearbetade 411 strängar: 242 uppdaterades, 169 hoppades
över och inga saknades. Det bekräftar importernas tekniska utfall för de
uppladdade filerna, men specificerar inte säkert vilka arkiverade batchar som
ingick. Därför betraktas tidigare deltafiler fortfarande som möjliga dubbletter
tills en ny export jämförs med dem.

## Termbasunderhåll: Action Blending

Två äldre termbasposter använde formerna *Actionblandning* och
*Åtgärdsblandning*. I den aktuella Blender-kontexten
`bpy.types.AnimData.action_blend_type` är **Action** ett namngivet datatypnamn,
inte det generella ordet för åtgärd. Den kanoniska formen är därför
*Action-blandning*. Korrigeringen är verifierad mot den arkiverade
animationsbatchen med SHA-256
`9b04b83aa77e4c0100e1f1d6a40f29fb25363b8dcb9bfd6571c416b52ee230d8`.

Termbasuppdateringen är publicerad i
`yeager/swedish-foss-terminology` som commit `1ca3b0b`. Den ändrar inte någon
ny UI-post och innebär inte i sig en verifierad Blender Translate-import.

## Blender-TM: synkning av kontextgranskade UI-poster

Blender-TM jämfördes mot de lokalt granskade UI-batcherna 1 214–1 352. Av 412
unika deltafält avvek 29 från äldre TM-formuleringar. De synkroniserades till
de kontextgranskade formerna, bland annat `Action-slot`, `rymd`,
`kompositering` och `operatör`. Endast de 29 berörda PO-posterna och deras 29
motsvarande TMX-segment ändrades; exportens befintliga projektmetadata
bevarades.

`scripts/validate.py`, `msgfmt`, diffkontroll och Gitleaks passerade.
Uppdateringen är publicerad i `yeager/swedish-tm` som commit `6cd4475`. Den
är minnesunderhåll och bevisar inte i sig en Blender Translate-import.

Samma dag synkroniserades 94 kontextverifierade poster för Blenders
Asset-familj mot den aktuella kontextgranskade exporten i
\`yeager/swedish-foss-terminology\` (commit \`eb76823\`) och
\`yeager/swedish-tm\` (commit \`308b1c6\`). Den följer \`resurs\` där
UI-kontexten gör det rätt, men ersätter inte mekaniskt etablerade
specialformer. Ändringen är verktygsunderhåll, inte ett påstående om
ytterligare import eller upstream-granskning.

Termbasens felaktiga post *Arbetsutrymme Interop ID* rättades också till
*Interop-ID för arbetsfärgrymd* efter kontroll mot Blenders dokumentation om
färghantering. Den korrigerade termbasen är publicerad i commit \`891a1ed\`.

Fyra poster för förskjutningsbakning synkroniserades efter kontroll av deras
koordinatkontext: *Displacement Space*, objekt- och tangentrymd använder
*rymd*, inte det generella *utrymme*. Termbasuppdateringen är publicerad i
commit \`237e9f2\`; den skapar ingen ny UI-import eftersom den lokala
referensexporten redan har de godkända formuleringarna.

Den 9 november synkroniserades ytterligare 20 aktuella UI-poster från
batcherna 1 354–1 359 till Blender-TM. De omfattar generell
*rendering*, Cycles prestandabeskrivningar, index-/världs-/objektrymder,
*tangentmappning* och *visningsnod*. Äldre TM-poster behålls som spårbar
historik, medan de nya posterna markerar vilken formulering som är
kontextgranskad mot export `(6)`. JSONL-källan samt den kanoniska Blender
PO- och TMX-exporten har återskapats och kontrollerats med
\`scripts/reviewed.py\`, msgfmt, diffkontroll och Gitleaks på staged-diffen.
Synkningen är publicerad i \`yeager/swedish-tm\` som commit \`6443c60\`.
Den är minnesunderhåll och innebär inte en verifierad Blender
Translate-import.

Sex fler termbasposter synkroniserades med den kontextgranskade UI-exporten:
svensk gemen stil för *online*, meningar och importmetod, den idiomatiska
egenskapsbeskrivningen för osparade ändringar, attributets datatyp,
oktaedriska ben och SI-enheten *kelvin*. Uppdateringen är publicerad i
\`yeager/swedish-foss-terminology\` som \`41499e2\` och kräver ingen
ytterligare UI-import.

Fyra termbasposter för Geometry Nodes rättades från den engelska formen
*Socket* till svenska *uttaget* i felbeskrivningar. Projektets etablerade term
är *noduttag*; den aktuella UI-exporten använder den naturliga bestämda formen
*uttaget*. Uppdateringen är publicerad i commit \`eb050d8\` och kräver ingen
ytterligare UI-import.

## Batch 1 353 — Cycles kärnoptimering och delat GPU-minne

Cycles begär vid renderingsstart optimerade beräkningskärnor för den aktuella
scenen. Fyra beskrivningar normaliseras till idiomatisk svenska: `sceninnehåll`
blir *scenens innehåll*, den konkreta cacheformen blir *cachen*, och de korta
statusbeskrivningarna använder *långsammast/snabbast rendering*. Hjälptexten
för NVLink-funktionen förtydligas till att större scener kan rymmas när minnet
fördelas mellan sammankopplade enheter i stället för att dupliceras.

Deltafilen `blender-ui-sv-reviewed-batch-1353-cycles-kernel-optimization.po`
innehåller fyra ändrade poster och har SHA-256
`b1754d337fabe699b0d0862c4647cc11435f3b441a1cc8d623dd3ca1e4e54839`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Hunspell-sv markerar endast tekniknamnet `NVLink`, vilket avsiktligt behålls.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad för just denna batch.

## Batch 1 352 — kompositerat resultat

Renderingsinställningen för Video Sequencer behandlar även det resultat som
har passerat kompositeringen. Den vardagliga formen *komponerade resultatet*
byter därför till den projektspecifika termen *kompositerade resultatet*.

Deltafilen `blender-ui-sv-reviewed-batch-1352-composited-result-20261109.po`
innehåller en ändrad post och har SHA-256
`c1eb3f40155e05aba7c41c5d485168bcadd6046276f84ea3d30e7e8bb04c441b`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade. Blender-TM har synkats med samma post. Batchen är lokalt färdig och
redo för manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 351 — renderingskedjor

Blenders renderingsinställningar beskriver både kompositering, Video
Sequencer och EEVEE:s strålspårning som tekniska kedjor av bearbetningssteg.
De onödiga engelska formerna *pipeline* ersätts därför med
*kompositeringskedja* respektive *bearbetningskedja*. Produktnamnet
**Blender Studio Pipeline Tool** berörs inte.

Deltafilen `blender-ui-sv-reviewed-batch-1351-pipelines-20261109.po`
innehåller fyra ändrade poster och har SHA-256
`2913fa83d3bf37049746ddf72892a8edc183690cd937d13795ae9a1a78e2a284`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade. Blender-TM har synkats med samma fyra poster samt den äldre,
likvärdiga kompositeringsposten. Batchen är lokalt färdig och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 350 — Action-slot för animationskanalbehållare

Hjälptexten för `ActionChannelbag.slot` pekar ut vilken Action-slot som
animationsdatan i behållaren hör till. Den tidigare formuleringen vände på
relationen och lästes som om slotten innehöll data. Den rättas till en
idiomatisk beskrivning av datans tillhörighet och följer projektets term
*animationskanalbehållare* för `Animation Channel Bag`.

Deltafilen `blender-ui-sv-reviewed-batch-1350-action-channelbag-20261109.po`
innehåller en ändrad post och har SHA-256
`6ec59604a15083605ed0239c22b180ab96ea91618e3fdb38848e02000723e352`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade. Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 333 — resurs i skriptets hyll-ID

Hjälptexten för `AssetShelf.bl_idname` beskriver en resurs som får ett
anpassat ID. Det generella *tillgången* ersätts med projektets etablerade
*resursen*, medan Python-identifierarna och exemplen lämnas oförändrade.

Deltafilen `blender-ui-sv-reviewed-batch-1333-asset-shelf-id.po` innehåller
en ändrad post och har SHA-256
`14c2332119a67b08434c6ec2ef088f06c4fcf10bb894d0d2aae1046a5e631813`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 332 — resurshyllans huvudrad

`Asset Shelf Header` är den synliga huvudraden för resursverktyget. Den
ofullständiga och felaktiga formen *Tillgångshyllans huvud* ersätts med
*Resurshyllans huvudrad*, i linje med övrig svensk resurshantering i Blender.

Deltafilen `blender-ui-sv-reviewed-batch-1332-asset-shelf-header.po`
innehåller en ändrad post och har SHA-256
`47246cdfe33ae6896d933baaefdafbc268ccaa60bb47fdf2a121d70de18807b6`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 331 — ID- och kantmarkeringar

Blenders interna *tag*-funktion markerar data eller meshkanter med ett
tillstånd för senare bearbetning. De svenska svengelska formerna *tagga data*
och *taggade kanter* normaliseras till *märka data* och *markerade kanter*.
Den fristående API-etiketten `Tag` lämnas oförändrad.

Deltafilen `blender-ui-sv-reviewed-batch-1331-id-data-tagging.po` innehåller
två ändrade poster. Batchen är lokalt färdig och redo för manuell import;
ingen Blender Translate-import är verifierad här.

## Batch 1 330 — Geometry Nodes-indataobjekt

Geometry Nodes-noden **Object Info** läser geometri, position, rotation och
skala från ett objekt som är indata till noden. Den trunkerade formen
*indatobjekt* rättas till den korrekta sammansättningen *indataobjekt* i båda
beskrivningarna av nodens transformationsläge.

Deltafilen `blender-ui-sv-reviewed-batch-1330-geometry-nodes-input-object.po`
innehåller två ändrade poster. Batchen är lokalt färdig och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 329 — White Noise-indatafrö

White Noise-noden beräknar ett slumpvärde från ett inmatat frö. Den felaktiga
formen *indatofrö* rättas till den svenska sammansättningen *indatafrö*.

Deltafilen `blender-ui-sv-reviewed-batch-1329-white-noise-input-seed.po`
innehåller en ändrad post och har SHA-256
`0845d6d3c5c5e85f555a6db08e41b0981d4b4b11adc439d146ca76175d09d707`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
markerar den korrekta tekniska sammansättningen `indatafrö`, som saknas i
ordlistan. Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 328 — Hair Dynamics deltatid

Hair Dynamics beräknar varje simuleringssteg mot tidsintervallet *delta time*.
Den tidigare felstavningen *deltattiden* rättas till den svenska bestämda
formen *deltatiden*.

Deltafilen `blender-ui-sv-reviewed-batch-1328-hair-dynamics-delta-time.po`
innehåller en ändrad post och har SHA-256
`1f587ecebe5eabc9c6e3746dcf888bfefcf8c5d5f8529b8fc6c9281d9fc14bb2`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
markerar den korrekta tekniska sammansättningen `deltatiden`, som saknas i
ordlistan. Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 327 — sRGB:s styckevisa kodning

Färghanteringen beskriver sRGB IEC 61966-2-1 som en sammansatt, styckevis
kodning. Den tidigare formuleringen *bitvis kodning* blandar felaktigt ihop
funktionsstycken med bitoperationer och rättas till *styckevis kodning*.

Deltafilen `blender-ui-sv-reviewed-batch-1327-srgb-piecewise-encoding.po`
innehåller en ändrad post och har SHA-256
`4f301d0152edb1c507ca5278066da5408b2450d4ff1823a4be07eedda608c0d4`.
`msgfmt`, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
`l10n-lint` rapporterar endast standardidentifieraren `IEC 61966-2-1` som ett
falskt positivt talintervall. Batchen är lokalt färdig och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 326 — Simple Deform-koordinatrymd

Simple Deform tillämpar vridning, böjning, avsmalning och sträckning runt
modifierarens Z-axel i ett tekniskt referenssystem. Formerna normaliseras till
*modifierarens koordinatrymd*. Hunspell-sv markerar ordet `modifierarens`,
vilket är en väntad falsk positiv för den korrekta fackformuleringen.

Deltafilen `blender-ui-sv-reviewed-batch-1326-simple-deform-coordinate-space.po`
innehåller fyra ändrade poster och har SHA-256
`827369b71d82f44f97953f1075256aa56158c8daebe01db53213b3eead969785`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 325 — logaritmiskt färgrum

Nodgruppen *Tune Image* använder logaritmiskt kodade färgvärden för att
undvika färgklippning. Det vaga *logaritmiskt utrymme* normaliseras därför
till den tekniska termen *logaritmiskt färgrum*.

Deltafilen `blender-ui-sv-reviewed-batch-1325-logarithmic-color-space.po`
innehåller en ändrad post och har SHA-256
`bf920fee661c1b7e93210354075159215828643ae15edbf2f10e487f6f25dc3c`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 324 — adaptiv rymd

Delningsmodifierarens *Adaptive Space* väljer om polygoner delas efter
pixelstorlek eller kantlängd i objektrymd. Den tekniska UI-etiketten
normaliseras därför från *Adaptivt utrymme* till *Adaptiv rymd*.

Deltafilen `blender-ui-sv-reviewed-batch-1324-adaptive-subdivision-space.po`
innehåller en ändrad post och har SHA-256
`e5be201e19b85244bf3b722a537973cc9dfb1b401863d08bfabea9a89797b8d7`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 323 — FBX rymdtransformering

FBX-importen och -exporten bakar vid behov en global transformering mellan
Blenders och målformatets koordinatrymder. Den tidigare formen
*rumstransformering* normaliseras till projektets etablerade
*rymdtransformering*.

Deltafilen `blender-ui-sv-reviewed-batch-1323-fbx-space-transform.po`
innehåller två ändrade poster och har SHA-256
`142af35885ae8747a2aff04060d7ec8d13226da7a253448dcb93bdcece0bdb5b`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 322 — Cycles kameragallring

Cycles beskriver *camera space culling* som gallring av objekt mot kamerans
synvolym. Det är en optimeringsmetod, inte en egen koordinatrymd, och
normaliseras därför från *kamerautrymmesgallring* till *kameragallring*.

Deltafilen `blender-ui-sv-reviewed-batch-1322-camera-culling.po` innehåller
två ändrade poster och har SHA-256
`5606291f353a1fe49ccf8a9677b44ac5131240e97611eaca08640e3ecac806c0`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 321 — Geometry Nodes koordinatdomäner

Blenders Geometry Nodes beskriver rutnätsgränser i världsrymd, voxlar i
indexrymd och punktdata i lokala koordinatrymder. De berörda tekniska
koordinatdomänerna normaliseras från vaga former av *utrymme* till
*världsrymd*, *rutnätsindexrymd*, *indexrymd* och *lokal koordinatrymd*.

Deltafilen `blender-ui-sv-reviewed-batch-1321-geometry-coordinate-domains.po`
innehåller tretton ändrade poster och har SHA-256
`3400995bfa274d5a92c55808904357f950ab0f2044b9380438be4739a1e5098c`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 320 — visnings- och regionkoordinater

Geometry Nodes-noderna *Mouse Position* och *Viewport Transform* arbetar med
pixelpositioner respektive matristransformeringar mellan objekt-, visnings- och
regionkoordinater. De vardagliga formerna *utrymme* normaliseras därför till
*visningsrymd* och *regionrymd*. För muspositionen används den förklarande
formen *regionens koordinatsystem*.

Deltafilen `blender-ui-sv-reviewed-batch-1320-viewport-coordinate-spaces.po`
innehåller fem ändrade poster och har SHA-256
`832b7aaf054dc9e99bf77569430f18202cf85c6bd0a59ad667ddaab36fce58de`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 319 — CrCb-färgrymd i Chroma Key

Chroma Key-noden jämför vinkeln mellan färg och nyckelfärg i CrCb-färgkoordinater.
Det allmänna *CrCb-utrymme* normaliseras därför till *CrCb-färgrymd*, i linje
med Blenders etablerade färgrymdsterminologi.

Deltafilen `blender-ui-sv-reviewed-batch-1319-crcb-color-space.po` innehåller
två ändrade poster och har SHA-256
`21a17f79242a5f1aba2d6800ddde91c464a62796f0a969c32ed3d3d1f11d692d`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
flaggar `CrCb-färgrymden` och `nycklas`; båda är väntade falska positiva
(färgkoordinatförkortning respektive Chroma Key-nodens fackverb). Batchen är
lokalt färdig och redo för manuell import; ingen Blender Translate-import är
verifierad här.

## Batch 1 318 — normaliserade maskkoordinater

Maskoperatorernas positionsparameter är en 0–1-normaliserad koordinat, inte
ett vardagligt utrymme. Hjälptexten normaliseras därför från *normaliserat
utrymme* till *normaliserade koordinater*.

Deltafilen `blender-ui-sv-reviewed-batch-1318-normalized-mask-coordinates.po`
innehåller en ändrad post och har SHA-256
`21c69cc16b6a6a68da1037a6726ea02c9ec899198eb06bf61397e0850b142392`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 317 — spårningsrymd i Compositor

Track Position-noden returnerar en markörs position och hastighet relativt
rörelsespårningens nollpunkt. Termen avser en koordinatdomän och normaliseras
därför från *spårningsutrymme* till *spårningsrymd*.

Deltafilen `blender-ui-sv-reviewed-batch-1317-tracking-space.po` innehåller
en ändrad post och har SHA-256
`7e4ed75018cd1ed22139d34333807ea3e8ce49bcb5d2a39aeb536960ba17a238`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 316 — global visningsrymd för Spin och Screw

Spin- och Screw-operatorerna anger axel och centrum som globala
visningskoordinater. De två inkonsekventa formerna *vyutrymme* och
*visningsutrymme* normaliseras därför till *global visningsrymd*.

Deltafilen `blender-ui-sv-reviewed-batch-1316-global-view-space.po`
innehåller två ändrade poster och har SHA-256
`24cbc082c663576cf73203857e5bc6fd8b543da6d884144291e6734d30d5fe69`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 315 — 3D-, UV- och UDIM-rymder

Tre verktygsbeskrivningar avser uttryckligen koordinatdomäner: en
rörelsespårningsoperation i 3D och två UV-packningsoperationer. De
normaliseras från *utrymme* till *rymd*. För den kombinerade UV/UDIM-domänen
används den läsbara sammansättningen *UV-/UDIM-rymd*; förkortningen UDIM är
ett etablerat formatnamn och lämnas oförändrad.

Deltafilen `blender-ui-sv-reviewed-batch-1315-3d-and-uv-spaces.po`
innehåller tre ändrade poster och har SHA-256
`4a0907aa7855fd16a9217aa82d3408c43a153c0e94d906a9648b40903ec12e8a`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Hunspell-sv känner inte igen formatförkortningen `UDIM`, vilket är en väntad
falsk positiv. Batchen är lokalt färdig och redo för manuell import; ingen
Blender Translate-import är verifierad här.

## Batch 1 314 — relativ koordinatrymd i Geometry Nodes

Geometry Input- och Array-nodernas `Relative Space` väljer mellan objekt- och
världsrymd när geometri transformeras. Den vaga etiketten *Relativt utrymme*
och den otydliga hjälptexten är därför normaliserade till *Relativ
koordinatrymd* och en beskrivning av ingångarnas inbördes transformeringar.

Deltafilen `blender-ui-sv-reviewed-batch-1314-relative-coordinate-space.po`
innehåller två ändrade poster och har SHA-256
`0e76a0c3961fa9ba06d58ed73f9d5a44b3765e79bb6094e8dc059a720fff71a0`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 313 — kamerarymd för rörelsespårningsdjup

Följningsbegränsningen projicerar ett objekt för att bestämma djup i
kamerans tredimensionella referenssystem. Det tidigare *kamerarum* är därför
normaliserat till projektets etablerade *kamerarymd*.

Deltafilen `blender-ui-sv-reviewed-batch-1313-camera-space-depth.po`
innehåller en ändrad post och har SHA-256
`22f7ae73cb3c74b65cc5578d56db1c65abcb285c589f8cd1ca26cc1e0340044f`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 312 — Geometry Nodes: objektrymd i vyporttransformering

Viewport Transform-noden transformerar punkter från *object space* till
visningsrymden. Den vaga sammansättningen *objektutrymme* normaliseras till
*objektrymd*. Texten för visnings- och regionrymder lämnas oförändrad tills
dess egen specifika UI-kontext har granskats.

Deltafilen `blender-ui-sv-reviewed-batch-1312-object-space-viewport-transform.po`
innehåller en ändrad post och har SHA-256
`884fddea442ba519f2884c24244753497fdd3eebdd8d42ae789c099f859bb340`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 311 — OBJ-importens begränsningsbox

Wavefront OBJ-importens `clamp_size` begränsar den importerade
3D-geometrins *bounding box*. Etiketten och hjälptexten normaliseras från
*begränsningsram* till *begränsningsbox*.

Deltafilen `blender-ui-sv-reviewed-batch-1311-obj-import-bounding-box.po`
innehåller två ändrade poster och har SHA-256
`08d3a444188adf92b8df21df079707b8387abe15c8fb11408ca6b1b36f6a1762`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 310 — Geometry Nodes: klippningsbegränsningsbox

Geometry Nodes Grid Clip beräknar X-, Y- och Z-gränser för en tredimensionell
klippningsvolym. De sex beskrivningarna normaliseras från
*klippningsbegränsningsruta* till *klippningsbegränsningsbox*, i enlighet med
projektets 3D-terminologi.

Deltafilen `blender-ui-sv-reviewed-batch-1310-grid-clipping-bounding-box.po`
innehåller sex ändrade poster och har SHA-256
`3efeba50d4f290adbbe24143e819e39ff4907dd7e71b85499eb936147302a5d7`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 309 — anpassade normaler i lokal koordinatrymd

Mesh-triangelns anpassade normalvektorer anges uttryckligen i *local space*.
Den inkonsekventa formen *lokalt koordinatrum* normaliseras till
*lokal koordinatrymd*, i linje med övriga Blender-termer för referenssystem.

Deltafilen `blender-ui-sv-reviewed-batch-1309-local-coordinate-space-custom-normals.po`
innehåller en ändrad post och har SHA-256
`608f3343fbfe54ea6eac51f2f69bccd1995a14b85593b7cfb7e8dadd9b799777`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 308 — tangent i lokal koordinatrymd

Meshens tangentvektor beskriver uttryckligen en vektor i *local space*.
Den tvetydiga formen *lokalt rum* ersätts därför av den etablerade
Blender-termen *lokal koordinatrymd*. Kodidentifieraren `calc_tangents`
behålls oförändrad.

Deltafilen `blender-ui-sv-reviewed-batch-1308-local-coordinate-space-tangent.po`
innehåller en ändrad post och har SHA-256
`72a1522f64ab35c3e1e28611484b3e97953c2624f6cc904d8879fa18adec55dd`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 307 — intern märkning och skarpa kanter

Två olika betydelser av *tag* skiljs åt. Den interna flaggan
`bpy.types.ID.tag` beskriver att data *märks* för verktygens egen användning,
medan en *tagged edge* i utjämningsinställningen är en *markerad kant*.
Användarskapade synliga taggar berörs inte.

Deltafilen `blender-ui-sv-reviewed-batch-1307-internal-tags-and-sharp-edges.po`
innehåller två ändrade poster och har SHA-256
`b77396966b8d3c3ffc653f88b6cdae6117e5bf8163c3bc5de799c162e99ad462`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 306 — volymers begränsningsboxar

Två visningsbeskrivningar för Volumes trådramsläge syftar på
tredimensionella omslutande volymer, inte på bild- eller spårningsrutor.
De normaliseras därför till *begränsningsbox* respektive
*begränsningsboxar*.

Deltafilen `blender-ui-sv-reviewed-batch-1306-volume-bounding-boxes.po`
innehåller två ändrade poster och har SHA-256
`47a89ed834d6090c4969f55f478d6a913365c9c8a5611531b8f0c7c3d9a8d4c8`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 305 — positionsöverskrivning i objektrymd

Penselverktygens interna `override_location`-parameter räknar om
muspositioner till positioner i *object space*. Den otydliga formuleringen
*objektets positioner i rymden* ersätts av den etablerade koordinattermen
*positioner i objektrymd*. Kodidentifierarna `location` och `mouse_event`
behålls oförändrade.

Deltafilen `blender-ui-sv-reviewed-batch-1305-object-space-positions.po`
innehåller en ändrad post och har SHA-256
`b018c4a3b58b01d669946d4b45f5256915665ba9e6d279e7d07be333244edd05`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 304 — tredimensionella begränsningsboxar

Fyra 3D-kontexter i Object-verktyg och Geometry Nodes normaliseras till
*begränsningsbox*: beräkning och användning av objektets bounding box, den
geometrinod som producerar en omslutande kub samt volymkontrollen för samma
3D-volym. Bildspårningens och andra tvådimensionella begränsningsrutor berörs
inte.

Deltafilen `blender-ui-sv-reviewed-batch-1304-3d-bounding-box.po` innehåller
fyra ändrade poster och har SHA-256
`62eb288180e5c2e56a0b914395cbe356d438b2f2ed9909ca7224acbff730d788`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 303 — objektets begränsningsbox

Två egenskaper för Array- och Curve-verktygen syftar uttryckligen på ett
objekts tredimensionella *bounding box*. De normaliseras från
*begränsningsruta* och *begränsningsram* till den etablerade Blender-termen
*begränsningsbox*.

Deltafilen `blender-ui-sv-reviewed-batch-1303-object-bounding-box.po`
innehåller två ändrade poster och har SHA-256
`11177cd6988ce229e876402451ff87b60b48eee4343f4aae6e2ac9eb83df675a`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 302 — objektprojektion i objektrymd

Bildtexturens boxprojektion beräknas mot objektets tredimensionella
avgränsningsvolym. Den korrigeras därför från *begränsningsrutan i
objektrummet* till *begränsningsboxen i objektrymd*, enligt Blender-termerna
*object bounding box* och *object space*.

Deltafilen `blender-ui-sv-reviewed-batch-1302-object-space-projection.po`
innehåller en ändrad post och har SHA-256
`fb778658db70f73de63de571aa81d10596958bf198269c547e2a544a3ee77da7`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 301 — UV-rymd i lightmap-packning

Inställningen för marginalandel i operatören *Lightmap Pack* räknas i samma
tvådimensionella UV-koordinatdomän som andra UV-packningsinställningar. Den
normaliseras därför från *UV-utrymmet* till den etablerade termen *UV-rymden*.

Deltafilen `blender-ui-sv-reviewed-batch-1301-lightmap-uv-space.po`
innehåller en ändrad post och har SHA-256
`1f3c82c3b2b1e00a20233ea319c2d69534f38c25be9acb4c25ecd224f337962a`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks passerade.
Batchen är lokalt färdig och redo för manuell import; ingen Blender
Translate-import är verifierad här.

## Batch 1 300 — kontextuttag

I nodoperatorn *Link operation to execute on the context socket* betyder
*socket* ett noduttag. Den avgränsade korrigeringen ersätter därför
*kontextsockeln* med *kontextuttaget* och lämnar den etablerade termen
*länkoperation* oförändrad.

Deltafilen `blender-ui-sv-reviewed-batch-1300-context-socket.po` innehåller
en ändrad post och har SHA-256
`8738941fd7d12fa4febd8d6c47ae922b0d323cc84565f68ccd4727f0f3043626`.
`msgfmt`, l10n-lint, svlang, den uppdaterade Hunspell-sv-ordlistan,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och redo för
manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 299 — noduttagsnamn

RNA-egenskapen *Socket name* används både för ett noduttag och för ett uttag
i ett nodträdsgränssnitt. Den korrigeras därför från den hårdvarubundna
felöversättningen *Sockelnamn* till *Uttagsnamn*, i linje med projektets
etablerade term *noduttag*.

Deltafilen `blender-ui-sv-reviewed-batch-1299-node-socket-name.po` innehåller
en ändrad post och har SHA-256
`df31daa1de524f452f15e60d5bebb47f6e1a227fbf2d7f828fcaffcb980d59b0`.
`msgfmt`, l10n-lint, svlang, den uppdaterade Hunspell-sv-ordlistan,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och redo för
manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 298 — kompositering

En rad-för-rad-granskning av 43 UI-strängar där källan uttryckligen använder
*compositing* normaliserar 29 översättningar till *kompositering*. Det gäller
bland annat *kompositeringsnodgrupp*, *kompositeringspass*,
*scenkompositering* och *kompositeringsrymd*. Verbformen *komponera* behålls
när strängen beskriver en faktisk handling. Valet följer Blender-manualens
svenska term [Kompositering](https://docs.blender.org/manual/sv/5.2/render/layers/introduction.html)
och ersätter tidigare lokala formuleringar med *komposition* i just denna
Blender-kontext.

Deltafilen `blender-ui-sv-reviewed-batch-1298-compositing-terminology.po`
innehåller 43 granskade poster, varav 29 ändras jämfört med den lokala
referensexporten, och har SHA-256
`b5bdd8074ddeaf0b53211987d6e58fe93b88a52be9e6790a59eb6ff04f092ce6`.
`msgfmt`, svlang, diffkontroll och Gitleaks passerade. l10n-lint rapporterar
en avsiktlig skiljeteckensskillnad: svenskans *obs!* ersätter källans
*Note:*. Hunspell-sv har uppdaterats separat med den belagda grundformen
*kompositering*; den längre Blender-specifika sammansättningen lämnas som
granskningssignal tills den har bredare belägg. Batchen är lokalt färdig och
redo för manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 297 — kompositeringsrymd

En socketbeskrivning för standardindatan *Uniform Image Coordinates* använder
Blenders svenska term *kompositering* och gör tydligt att det rör en
koordinatdomän: *kompositeringsrymd*, inte *komponeringsutrymme*.

Deltafilen `blender-ui-sv-reviewed-batch-1297-compositing-space.po`
innehåller en post och har SHA-256
`0005a6a9bd163c2c91f8877d0d9d04054c771e1b73114c5b55737109a1d5671e`.
Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och redo för
manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 296 — UV-rymd i packning och rutnät

Tre kontexter i Geometry Nodes och UV-redigeraren använder nu *UV-rymd* för
den tvådimensionella koordinatdomänen: packning av UV-öar, jämförande val av
ytarea och UV-redigerarens rutnätsindelning. Det skiljer dem från
*texturutrymme*, som i Blender är en separat 3D-box för texturkoordinater.

Deltafilen `blender-ui-sv-reviewed-batch-1296-uv-coordinate-space.po`
innehåller tre poster och har SHA-256
`7478ba138af0d3f3d6504b711fee350c665691eb420e442ca4201851994734bb`.
Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och redo för
manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 295 — UV- och 3D-rymd

Blenders UV-redigerare jämför längd och area antingen i UV-kartan eller i den
underliggande 3D-geometrin. Fyra hjälptexter normaliseras därför från de
vardagliga formerna *UV-rummet* och *3D-rummet* till de avgränsade
koordinattermerna *UV-rymd* respektive *3D-rymd*. Källkontexten verifierades
mot Blender-manualens avsnitt om *Select Similar*.

Deltafilen `blender-ui-sv-reviewed-batch-1295-uv-spaces.po` innehåller fyra
poster och har SHA-256
`74aa07a5c29f573e96b9a95ee12300767fa9866e39eb56fd7a43e566d6108f57`.
Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och redo för
manuell import; ingen Blender Translate-import är verifierad här.

Batch 1082 granskar två etiketter i Constraint-egenskapernas RNA-kontext.
Den gör den booleska statusetiketten *Override Constraint* till *Åsidosatt
begränsning*, inte den felaktiga imperativformen *Åsidosätt begränsning*, och
gör *Constraint name* idiomatiskt till *Begränsningens namn*. Deltafilen är
lokalt klar och väntar på manuell import i Blender Translate.

Batch 1083 normaliserar tre etiketter för Mesh-verktyget *Extrude Manifold*.
Den ersätter den felaktiga allmänspråkliga termen *mångfald* med den etablerade
topologitermen *manifold* i verktygets reservetikett och normalbaserade
extrudering. Deltafilen är lokalt klar och väntar på manuell import i Blender
Translate.

Importfilen `blender-ui-sv-reviewed-import-20261108-batches-1271-1274.po`
samlar batch 1 271–1 274 i åtta poster för manuell Blender Translate-import.
Den är lokalt validerad men saknar fortfarande verifierat importresultat.

## Batch 1 274 — viktmålning

Batch 1 274 rättar två felaktigt särskrivna förekomster av *Weight Paint* i
operator- och tangentmappningskontext till den etablerade UI-termen
*Viktmålning*. Den vanliga lägesetiketten var redan korrekt. Deltafilen
`blender-ui-sv-reviewed-batch-1274-weight-paint-contexts.po` innehåller två
poster och har SHA-256
`0d8fc0a5d099f0642e4ed810293a167060f30792a17de753e4f9f62fac4bf7aa`.
Den är lokalt validerad men ännu inte verifierad som importerad i Blender
Translate.

## Batch 1 273 — fysik- och animeringstermer

Batch 1 273 normaliserar tre återkommande Blender-termer enligt den
projektspecifika termtabellen: *Soft Body* → *Mjukkropp*, *Subsurface
Scattering* → *Underytsspridning* och *Onion Skin* → *Lökskal*. Varje post
är avgränsad till sin fysiska, shader- respektive annotationskontext.
Deltafilen `blender-ui-sv-reviewed-batch-1273-physics-and-animation-terms.po`
innehåller tre poster och har SHA-256
`2a6c0b29098fae791aab0bfea9fc20402040a89e1211edde7066f1ffca0cb1e6`.
Den är lokalt validerad men ännu inte verifierad som importerad i Blender
Translate.

## Batch 1 272 — tomt objekt

Batch 1 272 granskar den avgränsade operatorn för 3D-vyns meny för att lägga
till objekt. Där betyder *Empty* objektklassen, inte en tom volym eller ett
tomt värde, och blir därför *Tomt objekt*. Den generella TM-posten för
*Empty* ändras inte eftersom den saknar denna kontext. Deltafilen
`blender-ui-sv-reviewed-batch-1272-empty-object-menu.po` innehåller en post
och har SHA-256
`61ba9112c728712b4cac6bc9ea7ee130a78101503387b4d82f94db05f034af56`.
Den är lokalt validerad men ännu inte verifierad som importerad i Blender
Translate.

Batch 1084 normaliserar 27 synliga UI- och feltexter för F-kurvmodifierare i
Graf- och NLA-redigerarna. Den ersätter den blandade kortformen
*F-modifierare* med den etablerade och entydiga termen
*F-kurvmodifierare*, även för Cykel- och kuvertmodifieraren. Deltafilen är
lokalt klar och väntar på manuell import i Blender Translate.

Batch 1085 rättar den enda kvarvarande vardagliga formen *istället* i två
synliga UI-hjälptexter till standardspråkets *i stället*. Deltafilen är
lokalt klar och väntar på manuell import i Blender Translate.

Projektets åldersregel är verifierad den 7 november 2026: Blender 5.2.3 LTS
släpptes 22 oktober 2026 och Blender 5.3 var i release-candidate-fas. Projektet
har alltså en aktiv release långt inom 48-månadersgränsen.

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
interpunktion och ersätter den felaktiga sammanskrivningen av *popup* och
*panel* med *utfällbar panel*.
`l10n-lint` gav inga fel; dess enda informationspost är en falsk
valutaträff på förkortningen USD. `svlang` tolkar imperativ och tekniska namn
som möjliga avvikelser, men ingen faktisk svensk skrivavvikelse hittades.
Deltafilen är lokalt klar och ännu inte importerad i Blender Translate.

Batch 629 rättar XR-teleporteringens *Hit Color* till *Färg vid träff*.
Ändringen undviker den tidigare tredubbla `f`-följden i den sammanskrivna
träffärgsetiketten och följer
den redan använda parallellformen *Färg vid miss*. Deltafilen är lokalt klar
och ännu inte importerad i Blender Translate.

De 17 granskade posterna i batch 626–629 finns även i den samlade,
importklara filen
`blender-ui-sv-reviewed-20261107-batches-626-629-combined.po`. Den ersätter
inte de spårbara delbatcherna i arkivet, men är den fil som ska användas vid
en enda manuell import.

Batch 630 granskar tilläggens fjärranslutna resursbibliotek och hjälpraden
för *Save Copy*. Den ersätter den svårlästa sammanskrivningen som uppstår när
fjärransluten resurs kombineras med bibliotek, och som innehåller tre `r` i
följd, med *fjärranslutet
resursbibliotek* samt
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
den sammanskrivna formen av *klipp* och *plan*, som får tre `p` i följd, och
skriver ut relationen mellan det
nära och det fjärran klippningsplanet i hjälptexten. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 633 granskar Asset Browsers meddelande om nätåtkomst. Den ersätter
*resurser online* med den idiomatiska formen *resurser på nätet* och
den sammanskrivna formen av *fjärr* och *resurser* med den projektspecifika
termen *Fjärranslutna resurser*.
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

Batch 643 granskar elva statusposter i Outlinerns vy för
biblioteksåsidosättningar. Den normaliserar data- och egenskapsbenämningarna
och gör de additiva, subtraktiva, multiplikativa, anpassade och okända
åsidosättningarna konsekventa som substantiv. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 644 granskar Volym-visningens *wireframe mode*. Den ersätter
den sammanskrivna formen av *trådmodell* och *läge*, som har tre `l` i följd,
med Blenders etablerade term
*trådramsläge*. Den virtuellt sammanslagna UI-katalogen innehåller därefter
inga återstående strängar med tre identiska konsonanter i följd. Deltafilen är
lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 645 granskar Data Transfer-modifierarens närhetsbegränsning. Den
ersätter den bokstavliga och svårlästa formen *granngeometri* med
*närliggande geometri*, vilket stämmer med inställningens avståndskontext.
Deltafilen är lokalt kontrollerad men ännu inte importerad i Blender
Translate.

Batch 646 granskar Asset Browser-inställningen för Essentials. Den använder
*fjärranslutna resurser* i stället för den svårlästa sammanskrivningen av
*fjärr* och *resurser*, och det svenska UI-namnet *Grundresurser* för
Essentials-resursbiblioteket.
Deltafilen är lokalt kontrollerad men ännu inte importerad i Blender
Translate.

Batch 647 förenklar två beskrivningar i inställningsgränssnittet: den ersätter
den bokstavliga formuleringen *relaterade till visning av data* med
*för visning av data* och gör synlighetsväxlarna för huvud- och sidofält
tydliga. Deltafilen är lokalt kontrollerad men ännu inte importerad i Blender
Translate.

Batch 648 granskar CollectionChild- och CollectionObject-beskrivningarna.
Den ersätter den svårlästa sammansättningen *samlingsrelaterade inställningar*
med den tydliga formuleringen *inställningar relaterade till samlingen*.
Deltafilen är lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 649 normaliserar två Dope Sheet-filter för relaterade animationsdata.
*Ljussondsrelaterade animationsdata* och *linjestilsrelaterade
animationsdata* följer de omgivande filtrens struktur och Blenders etablerade
termer *ljussond* och *linjestil*. Deltafilen är lokalt kontrollerad men ännu
inte importerad i Blender Translate.

Batch 650 rättar Outlinerns etikett för *Library Overrides*. Den tidigare
formen *biblioteksåsidosättanden* ersätts med den korrekta och konsekventa
pluralformen *biblioteksåsidosättningar*. Deltafilen är lokalt kontrollerad
men ännu inte importerad i Blender Translate.

Batch 651 normaliserar status- och åtgärdstexter för att återbygga lokala
biblioteksåsidosättningar från länkade referenser. Termen är
*omsynkronisera*/*omsynkronisering*; den äldre omskrivningen
*synkronisera om* används inte längre i denna kontext. Deltafilen är lokalt
kontrollerad men ännu inte importerad i Blender Translate.

Batch 652 korrigerar batch 649 enligt projektets terminologilista:
*light probe* är *ljussond*, alltså *ljussondsrelaterade animationsdata*.
Deltafilen ersätter den tidigare, ännu ej importerade termen *ljusprob*.

Batch 653 tillämpar termen *ljussond* konsekvent i 35 UI- och felposter för
*Light Probe*, bland annat i EEVEE-inställningar, Asset Shelf, Dope Sheet,
objektåtgärder och felmeddelanden. Den rättar även sammansättningar som
*ljussondsobjekt* och skriver *volympoolen för ljussonder* i stället för en
svårläst kedjesammansättning. Deltafilen är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 654 rättar två UI-nära förekomster av den äldre termen
*tillgångsbläddrare*. I enlighet med den lokala Blender-terminologin används
*resursbläddrare* i Asset Browser-läget och dess hjälptext. Deltafilen är
lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 655 tillämpar *resursbibliotek* i 18 Asset Browser-, tilläggs- och
inställningsposter. De är den avgränsade UI-kontext där ordlistan föreskriver
*resursbibliotek*, medan äldre *tillgångsbibliotek* i annan löpande text inte
ändras mekaniskt. Deltafilen är lokalt kontrollerad men ännu inte importerad
i Blender Translate.

Batch 656 granskar tre hjälptexter för Outlinerns Library Override-åtgärder.
De använder nu konsekvent *biblioteksåsidosättning* och beskriver
beroendehierarkier utan den äldre, ospecifika formen *överskrivning*.
Deltafilen ingår i den verifierat importerade samlingsfilen nedan.

Den 7 november importerades samlingsfilen för batch 626–656 i Blender
Translate. Weblate behandlade 138 poster: 115 uppdaterades, 23 hoppades över
och 0 saknades. Importen är därmed verifierad.

Den importerade samlingsfilen för batch 626–656 är
`blender-ui-sv-reviewed-20261107-batches-626-656-combined.po` med 138
granskade poster och ersätter den tidigare samlingsfilen 626–655.

Batch 657 normaliserar 18 Brush-poster till den etablerade Blender-termen
*pensel*/*penslar*. Den omfattar bland annat datablock, Dynamic Paint,
Grease Pencil, skulptering, partikelpenslar och resursreferenser. De äldre
formerna *borste* och *borstar* används inte för dessa verktyg. Deltafilen är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 952 granskar tolv Geometry Nodes- och modifierarposter. Den använder
*provta* i stället för det engelskpåverkade *sampla*, behåller den formella
Blender-datatypen *mesh*, normaliserar *modifierarstack* och rättar den
felaktiga formen *Tillämpade modifierare* till *Tillämpad modifierare*.
Deltafilen är lokalt kontrollerad och ännu inte importerad i Blender
Translate.

Batch 953 granskar elva synliga Asset Browser- och tilläggstexter. Den
använder *resurser* i resursbläddrarens kontext samt *på nätet* och
*nätåtkomst* i stället för engelskpåverkade former med *online*. Deltafilen
är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 954 granskar femton Geometry Nodes-poster för kurv-, mesh-, ljud- och
UV-provtagning. Den använder den fastställda nodtermen *provta*, behåller
Blender-datatypen *mesh* och normaliserar bland annat *källmeshen* och
*indatameshen*. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Batch 955 granskar fjorton ytterligare Geometry Nodes-poster för booleska
operationer, punktfördelning, dualmesh, extrudering, underindelning,
volymrutnät och triangulering. Den ersätter den generiska formen *nät* med
Blenders datatyp *mesh* och använder rätt böjning, till exempel *meshen* och
*meshar*. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Batch 956 granskar fem fel- och exportmeddelanden för meshdata i FBX, USD,
partiklar och snabbeffekter. Den använder konsekvent *meshen* och
*meshens UV-karta* när den formella Blender-datatypen avses. Deltafilen är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 957 inleder nästa importomgång efter att den föregående samlingsfilen
har nått 997 poster. Den granskar fem modifierar- och Geometry Nodes-texter
och använder *meshobjekt* i sammansättningar samt *mesh* för typen i
spridningsnoden. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Batch 958 granskar tio tilläggs- och resursbläddrartexter för nätåtkomst.
Den använder konsekvent *nätåtkomst* och *på nätet*, medan den tekniska
startflaggan `--offline-mode` lämnas exakt som i källtexten. Batch 957–958
har en separat samlingsfil med 15 poster och är lokalt kontrollerad men ännu
inte importerad i Blender Translate.

Batch 959 granskar sex Asset Browser- och katalogtexter. Den använder
*resurs* och *resurskatalog* i den avgränsade resursbläddrarkontexten och
gör markering och lokala resurser idiomatiska på svenska. Deltafilen är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 960 granskar sju mesh-egenskaper, fel och skulpteringsposter. Den
normaliserar *meshattribut*, *meshdetaljer*, *meshnormaler* och den böjda
formen *meshen*. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Batch 961 granskar tolv Action- och NLA-poster. Den använder de fastställda
termerna *Action*, *Actionen*, *Actioner* och *Action-slot* när Blender
avser den formella animeringsdatatypen. Den separata samlingsfilen för
batch 957–961 innehåller 40 poster och är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 962 granskar fyra penselposter för viktmålning, verktygsval,
skulpteringsdetaljer och penselresurser. Den ersätter den äldre formen
*borste* med den fastställda Blender-termen *pensel*. Samlingsfilen för
batch 957–962 innehåller 44 poster och är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 963 granskar två UI-poster för Blenders meshtyp och meshobjekt. Den
behåller typnamnet *Mesh* för ID-kontexten och använder sammansättningen
*meshobjekt* i redigeringsfelmeddelandet. Samlingsfilen för batch 957–963
innehåller 46 poster och är lokalt kontrollerad men ännu inte importerad i
Blender Translate.

Batch 964 granskar tre inmatnings- och F-kurvemeddelanden. Den normaliserar
citattecken för `Tilde Action` och gör slutpunktsanvändningen konsekvent med
källsträngarna. Samlingsfilen för batch 957–964 innehåller 49 poster och är
lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 965 granskar tretton RNA-poster för Blenders formella animeringsobjekt.
Den använder *Actiongrupp*, *Action-lager*, *Action-slot* och *Action-remsa*
konsekvent, så att de inte förväxlas med vanliga åtgärder i gränssnittet.
Samlingsfilen för batch 957–965 innehåller 62 poster och är lokalt kontrollerad
men ännu inte importerad i Blender Translate.

Batch 966 granskar fem beskrivningar för Action-slotar. Den skiljer genomgående
den formella datatypen *Action*, dess slotar och dess datablock från vanliga
åtgärder i användargränssnittet. Samlingsfilen för batch 957–966 innehåller
67 poster och är lokalt kontrollerad men ännu inte importerad i Blender
Translate.

Batch 967 granskar tolv animerings- och importposter för Action-datatypen.
Den normaliserar bland annat *Action-blandning*, *Action-extrapolering*,
*Action-datablock* och *Huvud-Actioner* och behåller vanlig *hantering* när
källans `action` inte är själva datatypen. Samlingsfilen för batch 957–967
innehåller 79 poster och är lokalt kontrollerad men ännu inte importerad i
Blender Translate.

Batch 968 granskar tio Action Constraint-, NLA- och åtgärdsredigerarposter.
Den gör Action-slotar, Action-begränsningar och Action-redigeraren tydliga i
sammanhang där de är namn på Blenders formella animeringsobjekt. Samlingsfilen
för batch 957–968 innehåller 89 poster och är lokalt kontrollerad men ännu
inte importerad i Blender Translate.

Batch 969 granskar elva operator- och statusposter för byte av Action. Den
skiljer *Ersätt Action*, *ersättnings-Action*, *Action-begränsning* och
*Action-slot* från generiska åtgärder. Samlingsfilen för batch 957–969
innehåller 100 poster och är lokalt kontrollerad men ännu inte importerad i
Blender Translate.

Batch 970 granskar sex egenskapsbeskrivningar för Action. Den normaliserar
referenser till Actionens bildruteintervall, Action-lager, äldre Actioner och
Actionens posemarkörer. Samlingsfilen för batch 957–970 innehåller 106 poster
och är lokalt kontrollerad men ännu inte importerad i Blender Translate.

Batch 971 rättar två pluralfel för Compositor- och renderutdata:
*filformatstillägget* blir *filformatstilläggen* när källsträngen avser flera
tillägg. `l10n-lint` varnar enbart för att svenskans *t.ex.* saknar källans
engelska exempelkolon; detta är en avsiktlig svensk formulering. Samlingsfilen
för batch 957–971 innehåller 108 poster och är lokalt kontrollerad men ännu
inte importerad i Blender Translate.

Batch 972 granskar tio synliga inställningar för resursbläddraren. Den
normaliserar *resurs*, *Resursåtkomst* och *resurskatalog* i filtrering,
nätåtkomst och importval, men lämnar API- och RNA-namnen `Asset Data` och
`Asset Representation` orörda. Samlingsfilen för batch 957–972 innehåller
118 poster och är lokalt kontrollerad men ännu inte importerad i Blender
Translate.

Batch 973 granskar tio synliga texter i resurshyllan: filtrering, miniatyrer,
dragning och val av resursbibliotek. Den ersätter inkonsekvent *tillgång* med
*resurs* i den konkreta Asset Browser-kontexten. Samlingsfilen för batch
957–973 innehåller 128 poster och är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 974 granskar tio modifierar- och meshegenskaper. Den använder Blenders
formella typnamn *Mesh* och de svenska böjningarna *meshen*, *meshens* och
*meshobjekt*, i stället för det tvetydiga *nät*. Samlingsfilen för batch
957–974 innehåller 138 poster och är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 975 granskar nio booleska, deform- och ommeshningsposter. Den
normaliserar *meshobjekt*, *basmesh*, *indatamesh* och *meshen* i exakt de
modifierarkontexter där Blender arbetar med Mesh-datatypen. Samlingsfilen för
batch 957–975 innehåller 147 poster och är lokalt kontrollerad men ännu inte
importerad i Blender Translate.

Batch 976 granskar tio Mesh-poster för skulptering, ytdeformering, adaptiv
underindelning och volymkonvertering. Den använder konsekvent *meshen*,
*basmesh*, *målmesh* och *meshdata*. Samlingsfilen för batch 957–976
innehåller 157 poster och är lokalt kontrollerad men ännu inte importerad i
Blender Translate.

Batch 658 normaliserar 16 UI- och hjälpposter för *screen space* till
*skärmrymd*. Den ersätter inkonsekventa former som *skärmutrymme*,
*skärmyta* och *skärmrummet* i bland annat Grease Pencil, knivverktyget,
skärmdumpar, proportionell redigering, EEVEE-strålspårning och nodresurser.
Deltafilen är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 659 normaliserar tio RNA-poster för `BlendImportContext` till den
etablerade API-termen *blendfilimportkontext*. Den rättar bland annat
*blend-filimport*, *blend-filbibliotek* och *blend-fil-sökvägar* till
tydliga, konsekventa former. Deltafilen är lokalt kontrollerad och ännu inte
importerad i Blender Translate.

Batch 660 granskar elva pensel- och automaskningsposter. Den normaliserar
bland annat *våtmålning*, *3D-vyport*, *hörnpunktsvikt* och den etablerade
facktermen *icke-manifold*. Det synliga lägesnamnet `Area Plane` behålls på
engelska i den tekniska hjälptexten. Deltafilen är lokalt kontrollerad och
ännu inte importerad i Blender Translate.

Batch 661 granskar sex FFmpeg-poster för videoutdata. Den normaliserar
*utdatakvalitet*, *förlustfria utdata*, `Constant Rate Factor (CRF)` och
*muxpaketstorlek*. Förvalets hjälptext anger tydligt att detta är standardvalet
för de flesta användningsområden. Deltafilen är lokalt kontrollerad och ännu
inte importerad i Blender Translate.

Batch 662 förtydligar två poster i inställningarna för resursbibliotek. Den
använder *resursbibliotek* i rätt UI-kontext och ändrar den tidigare krystade
formen *nedladdningscachekatalog* till *cachekatalog för nedladdning av
fjärranslutna resursbibliotek*. Deltafilen är lokalt kontrollerad och ännu inte
importerad i Blender Translate.

Batch 663 granskar elva API-beskrivningar för `BlendImportContext` och
färgstyrning. Den normaliserar bland annat *blendfil*,
*biblioteksåsidosättning* och *resursbibliotek*, samt tar bort slutpunkter där
källtexten uttryckligen saknar dem. Verktyget svlang rapporterar tekniska
API-namn och fragment som ovanliga; dessa är avsiktliga. Deltafilen är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 664 granskar sex hjälptexter för översättningsinställningar, resurser,
Grease Pencil, vätskesimulering och OpenColorIO. Den rättar formalia i
metadatatexter, behåller tekniska identifierare och tar bort slutpunkter där
källtexten saknar dem. Deltafilen är lokalt kontrollerad och ännu inte
importerad i Blender Translate.

Batch 665 granskar tre poster för Action Slots i begränsningar och
dope sheet. Den rättar bland annat genitivformen *det aktiva objektet* och
gör den sammanhängande beskrivningen av åtgärdsslotar idiomatisk. Deltafilen
är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 666 granskar två förval- och Geometry Nodes-poster. Den normaliserar
den svenska anmärkningen i DVD-förvalet och tar bort en slutpunkt som saknas i
källtexten. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Batch 667 normaliserar 14 poster för tilläggsförråd i inställningar,
åtgärder och felmeddelanden. Den ersätter den inkonsekventa formen
*tilläggsarkiv* med den etablerade termen *tilläggsförråd*. Deltafilen är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 668 granskar två synliga etiketter som felaktigt lämnats på engelska.
Renderingsformatets *Stereo 3D* blir *Stereoskopisk 3D* och kompositorns
precisionsläge *Full precision* blir *Fullständig precision*. Codec-, format-
och produktnamn lämnas medvetet orörda. Deltafilen är lokalt kontrollerad och
ännu inte importerad i Blender Translate.

Batch 669 rättar två synliga hjälprader där källans slutpunkt saknades i den
svenska texten. Namnet `Realize Instances` behålls som ett synligt tekniskt
nodnamn; svlang markerar det och ordet *Instances* som ovanliga, men inte som
svenska språkfel. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Batch 670 rättar åtta Rigify-, pensel- och nodhjälprader där den svenska
texten hade slutpunkt trots att respektive källsträng saknar den. Innehåll och
tekniska namn, som Rigify och `Sequencer`, är oförändrade. Deltafilen är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 671 normaliserar 16 hjälprader för NLA, kompositorn och Geometry Nodes
så att deras avslutande skiljetecken följer respektive källsträng. Bland annat
bevaras de synliga tekniska namnen `Bokeh Blur`, `Cryptomatte`,
`Realize Instances` och `Join Geometry`. Deltafilen är lokalt kontrollerad och
ännu inte importerad i Blender Translate.

Batch 672 rättar åtta återstående UI- och felmeddelandeposter för `extension
repository`. Den konsekventa svenska termen är *tilläggsförråd*; den äldre
formen *tilläggsarkiv* används inte längre i batchen. Deltafilen är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 673 normaliserar 27 Asset Browser-, inställnings- och
felmeddelandeposter till *resursbibliotek*. Därmed används inte
*tillgångsbibliotek* i denna UI-nära kontext. Förändringen omfattar även
närliggande *asset*-referenser där de tydligt betyder resurser. Deltafilen är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 674 är en oberoende kontextgranskning av fem poster från batch 673. Den
använder *fjärranslutet resursbibliotek*, *grundresursbiblioteket*,
*tilläggsförråd* och *fjärr-URL* i de specifika Asset Browser- och
tilläggsinställningarna. Deltafilen är lokalt kontrollerad och ännu inte
importerad i Blender Translate.

Batch 675 granskar fem pensel- och automaskningsbeskrivningar i RNA-kontext.
Den förtydligar alfa-låsning, simuleringsavklingning, områdesplansmappning,
3D-vyporten och icke-manifolda gränskanter. Deltafilen är lokalt kontrollerad
och ännu inte importerad i Blender Translate.

Batch 676 granskar två FFmpeg-inställningar i exporteringskontext. Den använder
det synliga tekniknamnet `Constant Rate Factor (CRF)` och rättar bestämd form i
inställningen för fyrkanaligt ljud. Deltafilen är lokalt kontrollerad och ännu
inte importerad i Blender Translate.

Batch 677 rättar etiketten för begränsning till aktiv åtgärdsslot i Dope Sheet.
Den följer den närliggande hjälpradens uttryck *det aktiva objektets slot*.
Deltafilen är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 678 normaliserar elva ActionSlot-poster efter en oberoende genomgång av
RNA-kontexten. Den skiljer den tekniska termen *slot* från ordet *slott* och
använder korrekta former som *slotten*, *slothandtag* och *slotidentifierare*.
Deltafilen är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 679 tillämpar samma ActionSlot-terminologi i fjorton animationsoperatorer.
Den ersätter *plats* och *åtgärdsplats* med *slot* respektive *åtgärdsslot*
och bevarar API-identifierarna i exempelkommandona. Deltafilen är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 680 normaliserar tretton ActionSlot-etiketter och diagnoser i Rigify,
NLA, Outliner och animeringssystemet. Den använder *åtgärdsslot* även i
felmeddelanden och föråldrade användargränssnittssträngar. Deltafilen är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 681 granskar fyra kvarvarande ActionSlot-identifierare och
versionsdiagnoser. Den rättar böjningen *åtgärdsslotten*, ersätter äldre
*Action-plats* och bevarar samtliga fem `%s`-platshållare. Deltafilen är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 682 rättar tre kontextbundna UI-poster för *Brush*. Datatypen,
Dynamic Paint-läget och operatörsetiketten använder nu konsekvent *pensel*,
inte *borste*. Deltafilen är lokalt kontrollerad och ännu inte importerad i
Blender Translate.

Nästa separata importfil är
`blender-ui-sv-reviewed-20261107-batches-680-683-combined.po` med 32 unika
granskade poster. Den innehåller bara batch 680–683 och överlappar alltså inte
den redan importerade samlingsfilen för batch 626–679.

Batch 683 fortsätter penselterminologin i nio UI- och hjälpposter. Den ersätter
*borste* med *pensel*, *täthetspensel*, *partikelpensel* och
*penselresursreferens* i respektive kontext. Deltafilen är lokalt kontrollerad
och ännu inte importerad i Blender Translate.

Den 7 november importerades samlingsfilen
`blender-ui-sv-reviewed-20261107-batches-626-679-combined.po` manuellt i
Blender Translate. Servern behandlade 323 poster: 135 uppdaterades, 183
hoppades över och fem hittades inte eftersom motsvarande källsträngar har
ändrats eller försvunnit. Därmed är batch 626–679 inskickade; resultatet
innebär inte att samtliga äldre formuleringar har skrivits över.

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
den tidigare sammanskrivningen. Blender Translate bekräftade varje import:
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
med `fjärranslutet resursbibliotek`, så att varken trippelkonsonanten i den
tidigare sammanskrivningen eller den ofullständiga formen *fjärrbibliotek*
blir kvar i denna kontext.
`blender-ui-sv-reviewed-20261105-08.po` importerades
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
`fjärranslutet resursbibliotek`, i stället för den svårlästa sammanskrivningen
av *fjärr* och *resurser* med tre r i följd. Blender Translate bekräftade
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
för Grease Pencil Line Art och `RegionView3D` slog tidigare ihop *klipp* och
*plan* med tre p. Språkrådets konsonantstrykningsregel och etablerad svensk CAD-
terminologi ger formen `klippningsplan`, som nu används i etiketter och
hjälptext. Lokal kvalitetssäkring är klar. Blender Translate bekräftade
`blender-ui-sv-reviewed-20261105-24.po`: **3 bearbetade, 3 uppdaterade, 0
hoppade över och 0 saknades**.

Batch 25 följer Blenders egen UI-term för *Wireframe*. Den synliga etiketten
är `Trådram`, medan en hjälprad tidigare slog ihop *trådmodell* och *läge*,
med tre l i följd. I dess specifika lägeskontext blir `trådramsläget` både konsekvent med
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
Den ersätter engelsk etikett-text i hjälptexten med de synliga svenska reglagen
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

## Batch 1 621 — tema och vyport

Tre temanposter använder nu den etablerade Blender-termen **vyport** och
konsekvent grammatisk form för scenremsintervallets överlägg.

`blender-ui-sv-reviewed-batch-1621-theme-vyport-terms-20261110.po` innehåller
tre radgranskade poster med SHA-256
`0239559a3c2ea6e7d676c582e809e0d2685390d62f41c79ee6a19a0ad9796a2e`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar endast de avsiktliga Blender-termerna
*scenremsintervallet* och *vyporten*. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 622 — temaikoner och vyport

Fyra temaegenskaper har normaliserats: en sista kvarvarande **vyport** och
korrekta bestämda former för fel- och varningsikonerna samt egenskapsikonen.

`blender-ui-sv-reviewed-batch-1622-theme-info-vyport-20261110.po` innehåller
fyra radgranskade poster med SHA-256
`ae24562e9bb0c5c76916eaaf6a1d027a44d3b4c4fd5e19492db97550fe3bc734`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 625 — objektursprung

Hjälptexten för objektursprungets storlek nämner nu uttryckligen **ursprung**.

`blender-ui-sv-reviewed-batch-1625-object-origin-display-20261110.po`
innehåller en radgranskad post med SHA-256
`f41ea14cf60ac28852f8d39764f4c6ace4fa8a97585344aed818a31247beced5`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 624 — paneltema

Tre temaegenskaper för paneler och menyer använder nu idiomatisk svensk
samordning i stället för den krystade formen *panel/meny*.

`blender-ui-sv-reviewed-batch-1624-panel-theme-wording-20261110.po`
innehåller tre radgranskade poster med SHA-256
`db114ed95f34bf4e3737045028919bd07553bbcfebc6ff20a18eea460e27e39f`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 623 — konsekventa temaetiketter

Tre temarubriker använder nu konsekvent ordval: **vald**, **tema för
egenskaper** och **gemensamma områdesegenskaper**.

`blender-ui-sv-reviewed-batch-1623-theme-label-consistency-20261110.po`
innehåller tre radgranskade poster med SHA-256
`d63ca32f8503ab41073762f289fc35f023f757809b332ab4e61f796ea4d9fae2`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 620 — animationstema

Sex egenskaper i animationstemats färginställningar använder nu konsekventa
termer: **gemensamma** egenskaper, **darrningsnyckelbildruta** samt
**förhandsvisningsintervall**.

`blender-ui-sv-reviewed-batch-1620-animation-theme-terms-20261110.po`
innehåller sex radgranskade poster med SHA-256
`ea3e6196c82f7e587dacb3aaff0b1172f44ef7ef48deb2abb8088c1a3d20fbed`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar bara den kontextkorrekta sammansättningen
*darrningsnyckelbildruta*. Batchen är lokalt arkiverad och väntar på manuell
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

## Batch 1 420 — Grease Pencil-nyckelbildstyper

Grease Pencil-operatörens *Breakdowns* är en Blender-typ för
nyckelbildruta och normaliseras från den otydliga formen *mellanbildrutor*
till **mellanposer**. Hjälptexten beskriver därmed korrekt att befintliga
mellanposer kan uteslutas som ytterlägen vid interpolering.

\`blender-ui-sv-reviewed-batch-1420-grease-pencil-keyframe-types-20261109.po\`
innehåller två granskade poster. \`msgfmt\`, l10n-lint och Gitleaks passerade.
Svlang klassar bara den korrekta projektspecifika termen *mellanposer* som
ovanlig; Hunspell-sv träffar dessutom PO-metadata och engelska källsträngar.
Filen väntar på manuell import.

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

## Batch 1 267 — Tilläggsåtgärd

API-egenskapen `BlendImportContextItem.append_action` har fått projektets
korrekta term *tilläggsåtgärd*. Deltafilen
`blender-ui-sv-reviewed-batch-1267-append-action.po` innehåller en post och
har SHA-256
`fb81e5f8c077f4dab2d04b2f9859534b1c9e5efe068e28cc4f03c664033c5619`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är arkiverad och pushad i commit
`bdf5f401`; TM-ändringen är pushad i `swedish-tm`-commit `606d36d`.
Ingen Weblate-import är verifierad; batchen är lokalt färdig och redo för
manuell import.

## Terminologirevision 2026-11-09 — Action och Action-slot

Blenders formella animationsdatatyp ska konsekvent behålla namnet *Action* i
synliga UI- och API-kontexter. Den svenska löptexten böjer namnet som
*Actionen*, *Actioner* och *Actionerna*. För den tillhörande datastrukturen
används *Action-slot*, med böjningarna *Action-slotten* och *Action-slotar*.

Två äldre, motstridiga tabellrader med *åtgärdsslot* har därför tagits bort
från `TERMINOLOGY.md`; de riskerade att felaktigt överstyra den senare,
kontextgranskade terminologin. Ändringen rör endast granskningsunderlaget och
skapar ingen Blender Translate-deltafil eller något påstående om import.
Terminologirevisionen är arkiverad och pushad i commit `d8464906`.

## Batch 1 337 — ActionSlot-egenskaper

Tre egenskaper i `bpy.types.ActionSlot` använde fortfarande den äldre,
motstridiga formen *åtgärdsslot*: handtag, identifierare och visningsnamn.
De normaliseras till *Action-slot* enligt den aktuella, synliga
Blender-UI-terminologin. Deltafilen
`blender-ui-sv-reviewed-batch-1337-action-slot-properties.po` innehåller
endast dessa tre poster och har SHA-256
`26a8115fa33872fa56cc4b176763cf2eff8c99d0b00f3bcfa6bc6c91952ff03f`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade. `msgfmt` gav endast förväntade metadata-varningar för den lilla
deltafilens minimala PO-huvud. Batchen är lokalt färdig och arkiverad för
manuell Blender Translate-import; inget importresultat för just denna batch
är verifierat.

Tre motsvarande, strikt kontextbundna poster har lagts till i
`swedish-foss-terminology` (commit `7e6aac6`). Den generiska
översättningsminnesposten för *Slot Handle* ändrades inte, eftersom den saknar
`ActionSlot`-kontext och används även för andra typer av slotar.

## Batch 1 338 — fästning i 3D-mätverktyget

Hjälptexten för 3D-vyns mätverktyg använder Ctrl-tangenten för att fästa
en mätning. Den tidigare formen *snäppa* ersätts med det etablerade Blender-
verbet *fästa*. Denna avgränsade ändring påverkar inte sekvensredigerarens
särskilda term *snäppning*. Deltafilen
`blender-ui-sv-reviewed-batch-1338-ruler-snapping.po` innehåller en post och
har SHA-256
`bfde9b57866fb9067e4cec9e720d44502cd40d30d76feacb06200aaa207abc6a`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv och Gitleaks passerade. `msgfmt`
gav endast förväntade metadata-varningar för deltafilens minimala PO-huvud.
Batchen är lokalt färdig och arkiverad för manuell Blender Translate-import;
inget importresultat för just denna batch är verifierat.

## Batch 1 339 — Alt-verktygsåtkomst

Inställningen `Prefs.use_alt_tool` normaliseras från den oidiomatiska formen
*Alt-verktygstillgång* till *Alt-verktygsåtkomst*. Formen följer den
parallella inställningen *Alt-marköråtkomst* och beskriver åtkomst via
Alt-tangenten, inte tillgång till ett verktyg. Deltafilen
`blender-ui-sv-reviewed-batch-1339-alt-tool-access.po` innehåller en post och
har SHA-256
`debfacfa5869bf3394cfff5d877ba2fc4c5c9d78df7cb7ca5a2229963deb077e`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv och Gitleaks passerade. `msgfmt`
gav endast förväntade metadata-varningar för deltafilens minimala PO-huvud.
Batchen är lokalt färdig och arkiverad för manuell Blender Translate-import;
inget importresultat för just denna batch är verifierat.

Den felaktiga Blender-posten i `swedish-foss-terminology` har uppdaterats med
samma kontext och evidens i commit `0c37755`.

## Samlad import — batch 1 337–1 339

`blender-ui-sv-reviewed-manual-import-20261109-batches-1337-1339.po` samlar
de fem unika och kontextgranskade posterna från batch 1 337–1 339 i en enda
manuell importfil. Den har SHA-256
`02d4824d5b0605e8b9ed7cbf06d5df32b86dcec02f11865df4939066ed2cb83c`.
Filen har verifierats med `msgfmt`, l10n-lint, svlang, diffkontroll och
Gitleaks. Ingen Blender Translate-import av den samlade filen är verifierad.

## Batch 1 335 — cache för fjärrresurser

Katalognamnet *Nedladdningscachekatalogen* ersätts av den naturligare och mer
läsbara formuleringen *Cachekatalogen för nedladdningar från fjärranslutna
resursbibliotek*. Den undviker också tre identiska konsonanter i följd.
Deltafilen `blender-ui-sv-reviewed-batch-1335-remote-asset-download-cache.po`
innehåller en post.

`msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll och Gitleaks passerade.
Batchen är arkiverad och pushad i commit `b566d5ef`; Blender-TM synkades i
`swedish-tm`-commit `ede255b`. Weblate-import är inte verifierad; batchen är
lokalt redo för manuell import.

## Terminologi — Fill Solver

Termbasposten för `Fill Solver` rättades från den felaktiga uppmaningen
*Fyll i lösaren* till den tekniska inställningsetiketten *Fyllningslösare*.
Den används för fyllning i kurvor, masker och Grease Pencil och följer den
kontextgranskade UI-exporten. Uppdateringen är publicerad i
`swedish-foss-terminology`-commit `857cc9f` och kräver ingen ytterligare
UI-import.

## Batch 1 334 — Visningstyp

Den generella UI-etiketten `Display Type` rättas från det engelska lånordet
*Displaytyp* till *Visningstyp*. Källsträngen används för objekt, riggskelett,
3D-vy samt import- och exportdialoger; den avser hur innehållet visas, inte en
teknisk display-enhet. Deltafilen
`blender-ui-sv-reviewed-batch-1334-display-type.po` innehåller en post.

`msgfmt`, l10n-lint, svlang och Hunspell passerade. Termbasen uppdaterades och
pushades i `swedish-foss-terminology`-commit `4ca71d5`; Blender-TM synkades i
`swedish-tm`-commit `5de1c8e`. Weblate-import är inte verifierad; batchen är
lokalt redo för manuell import.

## Blender-TM — Action-slotar

Den redan kontextgranskade batch 1 678 används för att ta bort fem äldre
felposter ur Blender-TM: *Slott*, *Slotthandtag*, *Slottidentifierare*,
*Slottvisningsnamn* samt den felaktiga ägarkonstruktionen för aktivt objekt.
TM-posterna är nu *slot*, *slothandtag*, *slotidentifierare*,
*slotvisningsnamn* och *Visa endast slotten för det aktiva objektet*.
Ändringen är publicerad i `swedish-tm`-commit `f32ddf0`; den skapar ingen ny
UI-delta, eftersom rättningen redan finns i den arkiverade UI-batchen.

## Blender-TM — samlad UI-synk

Blender-TM synkades mot alla 385 arkiverade, kontextgranskade UI-batchfiler.
Endast 2 068 källsträngar med en entydig granskad måltext användes: 1 898
befintliga TM-poster rättades och 60 saknade poster lades till. 64 strängar
med flera möjliga måltexter lämnades medvetet utanför, eftersom TM saknar
Blenders specifika kontext. PO- och TMX-pariteten har validerats efter synken.
Ändringen är pushad i `swedish-tm`-commit `30dcc9a`.

## Batch 1 336 — märkning av data och kanter

Två anglicismer ersätts: verbet *tagga* blir *märka* för Blenders interna
datamärkning och *Taggade kanter* blir *Märkta kanter*. De tekniska
katalognamnen `startup`, `add-ons`, `modules` och `presets` berörs inte.
Deltafilen `blender-ui-sv-reviewed-batch-1336-data-and-edge-marking.po`
innehåller två poster.

`msgfmt`, l10n-lint, svlang, Hunspell, diffkontroll och Gitleaks passerade.
Batchen är arkiverad och pushad i commit `c8275c98`; Blender-TM synkades i
`swedish-tm`-commit `f16eb04`. Weblate-import är inte verifierad; batchen är
lokalt redo för manuell import.

## Batch 1 290 — geometri- och bildrymd

Batch 1 290 normaliserar sex Blender-kontexter där *geometry space* och
*image space* beskriver koordinatdomäner, inte allmänt utrymme. I Grease
Pencil Line Art används därför *geometrirymd* respektive *bildrymd*; samma
benämning används i Geometry Nodes och i längdmodifierarens absoluta läge.
Deltafilen `blender-ui-sv-reviewed-batch-1290-geometry-space.po` innehåller
sex poster och har SHA-256
`88b11f7e17e15590ee5bd8bbf4bfdff200666251e84512e067e7357bb6ccdec2`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och redo för
manuell Blender Translate-import. Något importresultat är inte verifierat.

## Batch 1 291–1 293 — referensrymder

De följande små deltorna slutför ytterligare kontextberoende normalisering av
Blenders referensrymder i den lokala exporten:

- Batch 1 291 använder *kraftrymd* för Geometry Nodes-gruppen Custom Force.
- Batch 1 292 rättar *lokalt koordinatrum* och modifierarens referensrymd till
  *lokal koordinatrymd* respektive *modifierarens koordinatrymd*.
- Batch 1 293 använder *armaturens koordinatrymd* i Edit Bone och
  *modifierarens koordinatrymd* i Simple Deform.

Deltafilerna innehåller fyra, två respektive två poster. De har SHA-256
`e44cb011ea035594c24cc4316b882437a5335abc273b40dbff668fe9695388f5`,
`44ec76fcdc96ac133e08121cb59167c1f4f32734a0ba90ae049d332ea879dbff` och
`c4ba06a4d4acc9ed0a2b7995c9c06bfb5335700c6bb612fb1a4bd77e9503d74f`.
Alla passerar `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks. De är arkiverade och TM-synkroniserade men saknar
verifierat importresultat i Blender Translate.

## Batch 1 276 — cache och kamerarymd

Sju UI-strängar normaliserar facktermerna *cachelagrad* och *kamerarymd*.
Det gäller cachevärden, renderings- och simuleringscache samt en
kameraspårningsbeskrivning; inga redan arkiverade motsvarigheter ingår.
Deltafilen `blender-ui-sv-reviewed-batch-1276-cache-camera-space.po`
innehåller sju poster och har SHA-256
`a99fa1e9cc6decc1b8c1ff86dedbbba14ed4957200eb341ae71504fcccb81b48`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell saknar de korrekta tekniska sammansättningarna
*hörnpunktskoordinater* och *geometrinodmodifierare*. Batchen är lokalt
färdig och redo för manuell import; ingen Blender Translate-import är
verifierad här.

## Batch 1 277 — lokal koordinatrymd

En mesh-tangentbeskrivning använder den precisa koordinattermen *lokal
koordinatrymd* i stället för det tvetydiga *lokalt rum*. Deltafilen
`blender-ui-sv-reviewed-batch-1277-local-coordinate-space.po` innehåller en
post och har SHA-256
`0bd901d9ec62c4ded1f657c9cd720e33b5ee3f4baed54e67807de2149f2dcd06`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig och redo för manuell import;
ingen Blender Translate-import är verifierad här.

## Batch 1 289 — 3D-rymd

Fyra hjälprader och tillgångsnamn i filmklippning, annoteringar och
Geometry Nodes normaliserar *3D space* från det vardagliga *3D-utrymme* till
Blenders koordinatterm *3D-rymd*. Deltafilen
`blender-ui-sv-reviewed-batch-1289-3d-space.po` innehåller fyra poster och
har SHA-256
`ea55f1e6a62989ad69cca721c92658c4157b13afae571fec5692b34402db3254`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig, arkiverad och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 288 — koordinatrymder

Två databeskrivningar för kameraspårning och mesh-tangenter normaliserar
*camera space* och *local space* till de precisa Blender-termerna
*kamerarymd* respektive *lokal koordinatrymd*. Deltafilen
`blender-ui-sv-reviewed-batch-1288-coordinate-spaces.po` innehåller två
poster och har SHA-256
`da9e1cabf85ff44bf130cd657cf4bd9bec1f14849319adbc3fafa4a519e4c24f`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig, arkiverad och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 287 — operatörer i hjälprader

Åtta hjälprader och etiketter från Geometry Nodes, informationsredigeraren,
egenskapsåterställning, Alembic, XR och skulptering använder konsekvent
Blenders svenska API-term *operatör*. Deltafilen
`blender-ui-sv-reviewed-batch-1287-operator-contexts.po` innehåller åtta
poster och har SHA-256
`6b375acc755d7907c80576ba2c78c340b33d6fef7c62f9b08bec85443f944bc5`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell markerar det avsiktligt bibehållna synliga
Blender-namnet *Symmetrize*. Batchen är lokalt färdig, arkiverad och redo för
manuell import; ingen Blender Translate-import är verifierad här.

## Batch 1 286 — återstående operatörstermer

Tio UI-hjälprader och etiketter från tangentkartor, i18n-verktyg,
resursbibliotek, grafredigeraren och skulpteringen normaliserar Blenders
API-åtgärdstyp från *operator* till *operatör*. Deltafilen
`blender-ui-sv-reviewed-batch-1286-operator-terms.po` innehåller tio poster
och har SHA-256
`9aa465b8452fbb7e2db5b316c3614be6366d17eb9081ae13014338144588a84b`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell saknar den korrekta domänspecifika
sammansättningen *i18n-filuppdateringsoperatörerna*. Batchen är lokalt
färdig, arkiverad och redo för manuell import; ingen Blender Translate-import
är verifierad här.

## Batch 1 285 — sökoperatör

Två sammanhängande UI-strängar i Blenders globala operatörssökning
normaliseras från *operator* till den etablerade facktermen *operatör*.
Deltafilen `blender-ui-sv-reviewed-batch-1285-search-operator.po` innehåller
två poster och har SHA-256
`4ce3ae8025c58cf5e633374f95fe3c3e2d3a69d0280607b711f310fbe8dcf9db`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig, arkiverad och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 284 — operatörer och tangentkartor

Åtta API-etiketter och hjälprader i resursbläddraren och tangentkartor
normaliseras från engelska *operator* till Blenders svenska fackterm
*operatör*. Deltafilen
`blender-ui-sv-reviewed-batch-1284-operators-keymaps.po` innehåller åtta
poster och har SHA-256
`c5b876320644dd41403025ab3bbda17995349b928f7bc8155f66f49316451a25`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell saknar den korrekta tekniska sammansättningen
*resursreferensegenskaper*. Batchen är lokalt färdig och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 283 — shaderkompilering

Systeminställningens etikett *Shader Compilation Workers* normaliseras från
den felaktigt försvenskade formen *skuggarkompilering* till Blenders
etablerade fackterm *shaderkompilering*. Deltafilen
`blender-ui-sv-reviewed-batch-1283-shader-compilation-workers.po` innehåller
en post och har SHA-256
`11014e53b9a9cd76cffd782bbd7897c63148135e193bdfd6e7ff1a7300578c3f`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell saknar facktermen *shaderkompilering*, som är
korrekt i Blender-kontexten. Batchen är lokalt färdig och redo för manuell
import; ingen Blender Translate-import är verifierad här.

## Batch 1 282 — fästbas i tangentmappning

Tangentmappningsvarianten för *Set Snap Base* normaliseras från *snäppbas*
till samma 3D-transformeringsterm, *fästbas*, som övriga UI-strängar
använder. Deltafilen `blender-ui-sv-reviewed-batch-1282-snap-base-off.po`
innehåller en post och har SHA-256
`498255e4e5cced7f7186d3f505bca4b9cb0038d6a50edd6659635c34b2326684`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell saknar facktermen *fästbas*, som är korrekt i
denna kontext. Batchen är lokalt färdig och redo för manuell import; ingen
Blender Translate-import är verifierad här.

## Batch 1 281 — beskärningsstart

En gemensam kamera-, vyport-, XR- och Geometry Nodes-etikett normaliseras
från *Start på klippning* till den etablerade termen *Beskärningsstart*.
Deltafilen `blender-ui-sv-reviewed-batch-1281-clip-start.po` innehåller en
post och har SHA-256
`83d859839e00b72eb26b2778079fc03c80cba0e0c985f1f72421d1f8c239518b`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig och redo för manuell import;
ingen Blender Translate-import är verifierad här.

## Batch 1 280 — gör lokala

Två egenskaper för länkade tillagda data använder Blenders etablerade verb
*gör … lokala*, i stället för den geografiska betydelsen *lokalisera*.
Deltafilen `blender-ui-sv-reviewed-batch-1280-make-local.po` innehåller två
poster och har SHA-256
`1f7793ef67f83f19739b58f810b37a727ba534695c363a030ff1a0489a55fb12`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig och redo för manuell import;
ingen Blender Translate-import är verifierad här.

## Batch 1 279 — valbarhet

Fyra XR-, 3D-vy- och armatursträngar skiljer korrekt på *valbar* och
*markerbar*. Resultatet använder Blenders konsekventa tillståndstermer
*valbar*, *icke-valbar* och *icke-valbart*. Deltafilen
`blender-ui-sv-reviewed-batch-1279-selectable.po` innehåller fyra poster och
har SHA-256
`84b340c809fbd3b4748b93cfd5ea64d2a8869e8768e9d9f09e31b1b5ee212efc`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Hunspell saknar API-termen *raycast-resultatet*, som
avsiktligt behålls i XR-hjälptextens tekniska kontext. Batchen är lokalt
färdig och redo för manuell import; ingen Blender Translate-import är
verifierad här.

## Batch 1 278 — senast använda mappar

Filbläddarens historiketikett rättas från den ofullständiga formen *Senaste
mappar* till *Senast använda mappar*, i linje med de intilliggande
egenskaperna för aktiv senast använd mapp. Deltafilen
`blender-ui-sv-reviewed-batch-1278-recent-folders.po` innehåller en post och
har SHA-256
`338c32f806262716577539f4d5d3ddcb037efe2ab2721f6e3ec6b0a7a7879372`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning och
Gitleaks passerade. Batchen är lokalt färdig och redo för manuell import;
ingen Blender Translate-import är verifierad här.

## Batch 1 275 — transformationsorientering

Sju etiketter och hjälprader för Blenders 3D-transformationsorientering
normaliseras från *transformeringsorientering* till den etablerade
projektspecifika termen *transformationsorientering*. Ändringen gäller endast
denna orienteringsfunktion och ändrar inte färghanteringens
*visningstransformering*, där termen har en annan betydelse. Deltafilen
`blender-ui-sv-reviewed-batch-1275-transform-orientation.po` innehåller sju
poster och har SHA-256
`d4e245e843d200a2af4f2348b03b8b861302609543da00b338ad5d2f389efd35`.

`msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning, diffkontroll och
Gitleaks passerade för deltan. Hunspell markerar bara facktermen *ytnormalen*,
som är korrekt i 3D-kontexten. Batchen är arkiverad och pushad i commit
`09329af3`. Den kontextbevarande TM-posten är uppdaterad och pushad i
`swedish-tm`-commit `f05b63c`. Ingen Blender Translate-import är verifierad
för just denna batch; den är lokalt färdig för manuell import.
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

## Batch 1 457 — UV-fäststatus

UV-redigerarens egenskap använder nu den korrekta sammansättningen
**UV-fäststatus** i stället för särskrivningen *UV-fäst status*.

`blender-ui-sv-reviewed-batch-1457-uv-pin-status-compound-20261109.po`
innehåller en granskad post med SHA-256
`768445bc6ef8b34e5286eacee2efd2ee3757b6903779afcc0ca6144087623578`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
den korrekta sammansättningen som sällsynt; detta är en granskad
informationssignal. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 458 — samplingslängd

Grease Pencil-konturens algoritmiska egenskap *Sample Length* använder nu
**Samplingslängd** i stället för den oidiomatiska frasen *Provets längd*.

`blender-ui-sv-reviewed-batch-1458-outline-sampling-length-20261109.po`
innehåller en granskad post med SHA-256
`a018914a4386bbdac120d34ce4a790332bdd06172636ea18e97a87243870a86a`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 493 — Action-slotar

Action-API:ts *slots* behåller den synliga UI-benämningen **Action-slotar** i
stället för den otydliga generiska termen *platser*.

`blender-ui-sv-reviewed-batch-1493-action-slots-20261109.po` innehåller två
granskade poster med SHA-256
`557dc423b9933e72ab6d00aa6099b991586f5861333ae363c505844ee034e62f`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
endast Action-typnamnet respektive korrekt imperativ ordföljd. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 494 — benens namn

Rigify-hjälptexten använder korrekt possessivform: **benens namn**.

`blender-ui-sv-reviewed-batch-1494-flip-bone-names-20261109.po` innehåller en
granskad post med SHA-256
`9da06fe4ab20b7a6f1fa9bc7e2449d19767cc204bf1b5fb494e9d0effe00e1d7`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 495 — spårningskontroller och cachearkiv

Åtta UI-poster har fått idiomatisk och konsekvent svensk formulering i
egenskapsredigeraren, cachearkivet och rörelsespårningen. Ändringarna
omfattar bland annat *kontextmeny*, synliga datablock, objektens sökvägar,
lösningens skala och medelvärdesberäkning av spår.

`blender-ui-sv-reviewed-batch-1495-tracking-controls-20261109.po` innehåller
åtta granskade poster med SHA-256
`4fb145585a5c8ce59b0a0b1715d07d37d02004e1d34bb49f0bfd43d5371f16d5`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. Svlang markerar två
korrekta relativa bisatser som möjliga V2-avvikelser; ingen ändring behövs.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 496 — spårningskontrollers formuleringar

Tre ytterligare hjälprader i rörelsespårningen använder nu tydligare svenska:
en marginal uttryckt i pixlar, en åtgärd för inaktivering och markeringens
låsning.

`blender-ui-sv-reviewed-batch-1496-tracking-controls-20261109.po` innehåller
tre granskade poster med SHA-256
`e56526574fb95a4be38b39ac88397a8bb0080812c8c26279e7322ccff88050e0`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. Svlang markerar den
korrekta relativa bisatsen i hjälpraden som en möjlig V2-avvikelse. Batchen
är lokalt arkiverad och väntar på manuell import.

## Batch 1 497 — kameraberäkning och spårningsaxlar

Kameralösningens och rekonstruktionsbuntarnas UI-formuleringar har
normaliserats: **beräknade spår**, **lösarens nyckelbildruta** och
**beräkna kamerarörelse**. X- och Y-axlar använder samma konstruktion som
den valda axeln.

`blender-ui-sv-reviewed-batch-1497-camera-solving-20261109.po` innehåller
åtta granskade poster med SHA-256
`e118c380a6a22ca93947b5d3830a69e9e6231be31cb0a3d6e290cbc5df77a337`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. Svlang markerar den
korrekta relativa bisatsen om riktning som möjlig V2-avvikelse. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 498 — bildvy samt samlingsimport och -export

Bildvyns kommandon använder nu bestämd form: **Anpassa vyn**, **Centrera vyn
på markören** och **Zooma vyn**. Samlingshanteringen har också fått korrekt
possessiv form i *exportörsindex*, en tydlig flyttriktning och formuleringen
*filändelser för ”Glob”*.

`blender-ui-sv-reviewed-batch-1498-view-import-export-20261109.po` innehåller
sex granskade poster med SHA-256
`74179dcc508ac1383d29a6a89a6cbeea1c2f48bfb5d1cd1e96683a2f3e10bc8f`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. Svlang markerar den
korrekta relativa bisatsen om exportörens riktning; Hunspell saknar den
korrekta sammansättningen *exportörsindex*. Batchen är lokalt arkiverad och
väntar på manuell import.

## Batch 1 499 — konsol och begränsningar

Fem hjälprader är normaliserade i konsolen och begränsningspanelen:
historik läggs till vid markörens position, markering görs vid förflyttning
och begränsningar kopieras till markerade objekt eller ben. Sökvägsanimation
använder *omfatta* för antal bildrutor och indexets riktning uttrycks med en
relativ bisats.

`blender-ui-sv-reviewed-batch-1499-console-constraints-20261109.po`
innehåller fem granskade poster med SHA-256
`d0e3cd1d485c1270c1fa7c9415eee8456aa2c85cba6039280573968dba2cd20e`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. Svlang markerar tre
korrekta relativa bisatser och en kontextberoende imperativ som möjliga
V2-avvikelser. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 500 — kurvverktyg och skulptering

Tolv kurvrelaterade UI-poster har normaliserats. De använder *världsrymd*,
konsekvent verbform för redigeringsläge, tydligare hårpartikelsystem och
svenska uttryck för urvalets början/slut. Handtagstyper, cykliska kurvor och
kurvskulpteringsläget är samtidigt förtydligade.

`blender-ui-sv-reviewed-batch-1500-curves-20261109.po` innehåller tolv
granskade poster med SHA-256
`7a85846219ae202579a36daddcc8cce7ea9f2f9d959441acb87c2b311c0337c0`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
endast etablerade Blender-termer eller en korrekt imperativ konstruktion.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 501 — cykliskt läge i delad UI-sträng

Strängen *Toggle Cyclic* används både för kurvor och maskverktyget. Den
kurvspecifika formuleringen i batch 1 500 ersätts därför med den generella
och korrekta UI-formen **Växla cykliskt läge**. Batch 1 501 ska användas
före batch 1 500 om båda ingår i en manuell import.

`blender-ui-sv-reviewed-batch-1501-toggle-cyclic-context-20261109.po`
innehåller en granskad post med SHA-256
`8764e53284eeef73ded826ee53212b0c5d380453c085ceb3cc004749be1c00e5`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 502 — kurvor mot yta

Fem kurvverktygssträngar är förtydligade: kurvor fästs **mot ytan**,
rotpunkten behåller samma term genom hela hjälpraden och riktningen för
cyklisk yta uttrycks idiomatiskt. Transformkommandona använder dessutom
svensk ordföljd för kurva respektive mask.

`blender-ui-sv-reviewed-batch-1502-curve-surface-tools-20261110.po`
innehåller fem granskade poster med SHA-256
`5431d1bc14ce12347e5fbd61e0ae36b401b43c99f379d4d6b7d4d5b38ffd1c2d`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. Svlangs enda träff
är en korrekt relativ bisats. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 503 — kurvhandtag och utjämning

Sex UI-poster för kurvredigering har normaliserats: *vektorhandtag*,
avsmalning av avfasning, schackvis avmarkering samt utjämning av kurvradie,
kurvlutning och kurvvikt.

`blender-ui-sv-reviewed-batch-1503-curve-handles-20261110.po` innehåller sex
granskade poster med SHA-256
`1d431fdafbf679824fe0b0fe6a88504960741f04eb4d630ffe093dc1f709d7ec`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv markerar de korrekta
Blender-sammansättningarna *schackvis*, *kurvlutningen* och *kurvvikten*;
svlang ger 10/10. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 504 — Dynamic Paint och FBX-armatur

Fem strängar i Dynamic Paint och FBX-exporten har förtydligats: typens
aktiva status, varje bens underordnade och armaturens FBXNode-typ. De två
FBX-noderna använder konsekventa svenska citattecken.

`blender-ui-sv-reviewed-batch-1504-dynamic-paint-fbx-20261110.po` innehåller
fem granskade poster med SHA-256
`9d6f75622ccd139bfdb2a5e56a19d421827090ee3b9bfbc55f92df8bfb9c8d9f`.
`msgfmt`, l10n-lint och Gitleaks passerade. Verktygens träffar gäller
produktnamnen FBXNode, Root och LimbNode samt korrekta relativa bisatser.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 505 — FBX-exportens Actioner och utjämning

Sex FBX-exportposter har förtydligats och normaliserats: varje *Action* blir
en separat *AnimStack*, exporten skiljer normal- från kant- och ytutjämning,
och deformerande ben samt Catmull-Rom-underindelning beskrivs med korrekt
Blender-kontext. Formuleringen för modifierare använder semikolon i stället
för strecktecken eftersom källan använder bindestreck.

`blender-ui-sv-reviewed-batch-1505-fbx-export-20261110.po` innehåller sex
granskade poster med SHA-256
`1475e7e8018c2f44442ba2badc57674d2e51751506153c9f6cc679a1b3870366`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
korrekta Blender- och formatnamn, sammansättningar samt imperativ i relativa
bisatser. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 506 — glTF-exportens skiljetecken

En glTF-exportpost ersätter strecktecknet före varningen med semikolon.
Källtexten använder bindestreck, inte ett tankstreck, och svenskans två
självständiga satsdelar blir tydligare med semikolon.

`blender-ui-sv-reviewed-batch-1506-gltf-export-punctuation-20261110.po`
innehåller en granskad post med SHA-256
`f6834d272c320637701d974bfe4fbcc957188241512b25c39ed54819ae92ed3b`.
`msgfmt`, l10n-lint, svlang och Gitleaks passerade. Hunspell-sv markerar den
korrekta Blender-sammansättningen *meshobjekt*. Batchen är lokalt arkiverad
och väntar på manuell import.

## Batch 1 507 — glTF-exportens format och ljus

Tre glTF-exportposter har korrigerats: GPU-instansens begränsning nämner nu
underordnade *objekt*, förkortningen **PBR** har korrekt versalisering och
Blenders etablerade term *strålkastare* ersätter det engelsknära *spotljus*.

`blender-ui-sv-reviewed-batch-1507-gltf-export-terminology-20261110.po`
innehåller tre granskade poster med SHA-256
`226606fe83c67a37f63244ba4c8f9766d1335702c388b1ea944efce25cfd1e6e`.
`msgfmt`, l10n-lint och Gitleaks passerade. L10n-lints enda notis är ett
förväntat skiljeteckensbyte kring ett API-namn. Hunspell-sv och svlang
markerar korrekta format- och API-namn samt en korrekt relativ bisats.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 508 — Animation Pointer-lägen

Animation Pointer-beskrivningen använder nu samma synliga UI-namn som
exportörens lägesval: *NLA-spår* och *Scen*, inte engelska strängar.

`blender-ui-sv-reviewed-batch-1508-animation-pointer-labels-20261110.po`
innehåller en granskad post med SHA-256
`475de0b5ccec7a62facd9ac6b86f8fa5c038f2fa58568fcb6c9d4108cb4b8189`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
det korrekta UI-namnet *NLA-spår* och en förkortad sats. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 509 — tilläggsförråd och filåtgärder

Två felstavade förekomster av *förvaret* har rättats till **förrådet** i
tilläggsadministrationen. Avbrott av filoperationer använder dessutom den
konsekventa UI-termen **filåtgärd**.

`blender-ui-sv-reviewed-batch-1509-extension-repository-file-actions-20261110.po`
innehåller fyra granskade poster med SHA-256
`2c390c43f6c09e3bf6ff2f7e50ab3d40106b84ffbfce2355a8ff212325e5d203`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 510 — F-kurvors Bézier-handtag

Tre besläktade kommandon för att equalize Bézier-handtag använder nu den
konsekventa svenska verbformen **Jämna ut**, i stället för en blandning av
*Utjämna* och *Jämna ut*.

`blender-ui-sv-reviewed-batch-1510-fcurve-handle-wording-20261110.po`
innehåller tre granskade poster med SHA-256
`70361d9d7a312856d9ca1936a81c634a4505d27d12b0b639ae40f3d3656d6ad2`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 511 — F-kurvors skjut/dra-kommando

Kommandonamnet för *Push Pull Keyframes* använder nu den idiomatiska formen
**Skjut/dra nyckelbildrutor**, utan det krystade bindestrecksförledet.

`blender-ui-sv-reviewed-batch-1511-fcurve-push-pull-20261110.po` innehåller
en granskad post med SHA-256
`44359e1ef68d72fa0990e4dff1f62df89a963b66e8ea61aa735959a42cf5f3e5`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 512 — ljudets bakning till sampel

Ljudvågsverktygets beskrivning använder nu den etablerade Blender-termen
**Bakar**, i linje med övriga bakningsåtgärder, i stället för det missvisande
*Beräknar*.

`blender-ui-sv-reviewed-batch-1512-sound-bake-20261110.po` innehåller en
granskad post med SHA-256
`7924a1c412e0f81e8f60f7736fb732f16b8f22b9c8d826637aecc859ff39bece`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. Svlangs enda träff
är den korrekta imperativformen. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 513 — Grease Pencil-typografi

Två Grease Pencil-poster följer nu svensk typografi: ordet efter
varningskolonet inleds med gemen och *mellanbilder* har svenska citattecken.

`blender-ui-sv-reviewed-batch-1513-grease-pencil-typography-20261110.po`
innehåller två granskade poster med SHA-256
`abd9141e981a00d2f0dbed03c5ab9f4ea8a49a1c5a4ea2a17048ce429746e987`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade;
hunspell-sv markerar endast produktnamnet Grease Pencil. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 514 — Grease Pencil-gruppens färgmärkning

Grease Pencil-gruppens färgetikett använder nu den projektgemensamma termen
**Färgmärkning**, i stället för den svårlästa sammansättningen
*gruppfärgmarkering*.

`blender-ui-sv-reviewed-batch-1514-grease-pencil-color-tag-20261110.po`
innehåller en granskad post med SHA-256
`00740c8e64017cd8d7040ac073fbfcfd683eddda66609cf3f84d84b1ae93ff5c`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade;
hunspell-sv markerar endast produktnamnet Grease Pencil. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 515 — Grease Pencil och inklistringsordning

Kommandot *Paste on Back* använder nu **Klistra in längst bak**. Det beskriver
streckens visningsordning, inte en fysisk baksida.

`blender-ui-sv-reviewed-batch-1515-grease-pencil-paste-order-20261110.po`
innehåller en granskad post med SHA-256
`3b664ec3a410a626ea7812f581c311dc448255bb7a126c6c0e864afe50b6243c`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 516 — Grease Pencil-urval

Beskrivningen för sammanslagning efter avstånd använder nu den genomgående
UI-termen **markerade punkter**, inte *utvalda punkter*.

`blender-ui-sv-reviewed-batch-1516-grease-pencil-selection-20261110.po`
innehåller en granskad post med SHA-256
`75888e70cc5e81003a059a8afb6374723582ec67535dfdcb386ea4b05fad2559`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. Svlangs enda träff
är den korrekta imperativformen. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 517 — Grease Pencil-bildspårningens mål

Bildspårningsverktyget använder nu **Målobjekt för Grease Pencil**, vilket
stämmer med egenskapens två alternativ *Nytt objekt* och *Valt objekt*.

`blender-ui-sv-reviewed-batch-1517-grease-pencil-trace-target-20261110.po`
innehåller en granskad post med SHA-256
`dc71d0e06294416dcccaf155838eed69b7d6946aa7c7842a9ec4d564b22cc636`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade;
hunspell-sv markerar endast produktnamnet Grease Pencil. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 518 — bildplansimportens renderingsmetod

Bildplansimporten använder nu den tydliga tekniska formuleringen
**hashbaserad transparens**. De två UI-valen för positiv Y- respektive
Z-riktning har också fått det saknade verbet **Vänd**.

`blender-ui-sv-reviewed-batch-1518-image-plane-render-method-20261110.po`
innehåller tre granskade poster med SHA-256
`8d484a52e166dbbf8807928b96ebbb824e725f7060eabb0c52a8705e2d87cf8b`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. Svlangs enda träff
är den korrekta imperativformen. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 519 — BVH-importens benorientering

BVH-importens hjälptext anger korrekt att benets huvudaxel ska riktas in
**med underordnade ben**, inte *mot* dem.

`blender-ui-sv-reviewed-batch-1519-bvh-bone-orientation-20261110.po`
innehåller en granskad post med SHA-256
`fe636b22ca71664970de047eaf3a0d092c077d3400bcb19c0c33f526b44c52f0`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. Svlang markerar den
korrekta imperativformen som möjlig V2-avvikelse. Batchen är lokalt arkiverad
och väntar på manuell import.

## Batch 1 520 — rapportåtgärder

Rapportåtgärderna använder nu det sakliga UI-verbet **Kör om** för replay och
den konsekventa borttagningsåtgärden **Ta bort**.

`blender-ui-sv-reviewed-batch-1520-report-actions-20261110.po` innehåller tre
granskade poster med SHA-256
`65f36fa7bc5e66dcc9d09891b6403700e5638a7c54389ce34d7d6eb1a03e4bbb`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 521 — regelbundet gitter

Gitterverktyget avser kontrollpunkterna i plural och heter därför **Gör
regelbundna**.

`blender-ui-sv-reviewed-batch-1521-lattice-make-regular-20261110.po`
innehåller en granskad post med SHA-256
`640e6efa27adee44c7f2eca79e239c2c10cfc6767ce7f5cb1c5caab61fa88a00`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 522 — maskens glidning

Maskverktygets rörelseåtgärd använder konsekvent **skjut**.

`blender-ui-sv-reviewed-batch-1522-mask-slide-20261110.po` innehåller en
granskad post med SHA-256
`04e6e3c31f8157f08133c4a4071589075834b0b1eb17976b20d2094f5f1fc61e`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 523 — avfasningens glidning

Avfasningsverktyget använder den etablerade Blender-termen **skjuta** i stället
för kalkeringen *glida*.

`blender-ui-sv-reviewed-batch-1523-bevel-slide-20261110.po` innehåller en
granskad post med SHA-256
`530202309bfe708176e5ca77fd356b5fd1e053cdcc243348fc7e27ef161b8d88`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 524 — böj kantslingor

Meshkommandot använder verbet **Böj**: engelska *Curve* beskriver åtgärden,
inte ett substantiv.

`blender-ui-sv-reviewed-batch-1524-curve-edge-loops-20261110.po` innehåller
en granskad post med SHA-256
`715b0f175f7c81b25859c3ed27daf44e91704bb176ad17a31064dc1bbe942ffc`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 525 — ta bort kantslinga

Meshkommandot och dess hjälptext använder konsekvent den svenska termen
**kantslinga** i stället för *kantloop*.

`blender-ui-sv-reviewed-batch-1525-delete-edge-loop-20261110.po` innehåller
två granskade poster med SHA-256
`ac01a6fea34dbbd1a009449b5c54be44503ccaa5f495ca9c900ae496c70797b4`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 526–533 — kantslingor och veckvikt

Följande lokalt granskade UI-deltan normaliserar meshverktygens svenska
terminologi: **ytslinga**, **kantslinga**, **slingklipp**, **förskjuten
kantslinga**, **gränsslinga** och **veckvikt**. Terminologin följer
verktygens konkreta meshkontext; produkt- och API-namn lämnas oförändrade.

- `blender-ui-sv-reviewed-batch-1526-face-loop-20261110.po` — SHA-256
  `63932e270a7eac0b33b341229cfcf08e80137a87f21b82e4803169e640ecad0f`
- `blender-ui-sv-reviewed-batch-1527-fill-edge-loops-20261110.po` — SHA-256
  `7d487933af71b2550cbb5649664b3c39a3cd0888f2ae855fb7ca4efcde3bde9d`
- `blender-ui-sv-reviewed-batch-1528-inset-faces-20261110.po` — SHA-256
  `d0a66e09b5c42c59501e63e025360b1386be867cec37473dc1fdf581bf6a4e27`
- `blender-ui-sv-reviewed-batch-1529-loop-terminology-20261110.po` — SHA-256
  `12a40c3e58380b1270a513c4a9b77129dcedd970a3c6bb6207541b0b0f51bad5`
- `blender-ui-sv-reviewed-batch-1530-offset-edge-loop-20261110.po` — SHA-256
  `8a4c83991d50eb7dd155ec846a4b806f07ee9aa36461cf1a0c63053edd9b39aa`
- `blender-ui-sv-reviewed-batch-1531-relax-edge-loops-20261110.po` — SHA-256
  `175b986c6046bbd7cd7f1135ada10aeca8dde362025d12482d57ef44ae541d73`
- `blender-ui-sv-reviewed-batch-1532-loop-consistency-20261110.po` — SHA-256
  `c2527694f595820e37b12d4f9eac38dd8f29119f2b79437ebd1de60c486093e1`
- `blender-ui-sv-reviewed-batch-1533-wireframe-crease-20261110.po` — SHA-256
  `b58f92d8532bf633aeb83eb1a276b0e0fef0c3c164d8d58c8ae2d2b98d218df6`

`msgfmt`, l10n-lint, svlang och Gitleaks passerade. Hunspell-sv bekräftar
allmänsvenskan men saknar några domänspecifika sammansättningar, bland annat
*ytslinga* och *veckvikt*; de har granskats i Blender-kontext. Batcherna är
lokalt arkiverade och väntar på manuell import.

## Batch 1 534–535 — fullföljd kantslinge- och NLA-kontext

Alla gränssnittskontexter för **slingklipp** och **förskjutna kantslingor** är
nu enhetliga. NLA-verktyget använder **rutmarkering** och den etablerade
Blender-beteckningen **NLA-remsor**.

`blender-ui-sv-reviewed-batch-1534-edge-loop-contexts-20261110.po` innehåller
elva granskade poster med SHA-256
`e681a21bf5b8fea60d8523a7556ff1f6725e97f317b67475c96ddc80c8115fc3`.
`blender-ui-sv-reviewed-batch-1535-nla-selection-stack-20261110.po` innehåller
två granskade poster med SHA-256
`405f2406cb8770e03a47c3fff96de9972cb889f90c99c0117da0083deb979ddb`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade; ordlistornas
återstående markeringar gäller Blender-termer. Batcherna är lokalt arkiverade
och väntar på manuell import.

## Batch 1 536 — nodåtgärd

Node Wrangler använder **åtgärd** konsekvent i valet för föregående
blandningstyp eller åtgärd.

`blender-ui-sv-reviewed-batch-1536-node-batch-operation-20261110.po`
innehåller en granskad post med SHA-256
`c18910fa7c59a94f4d259aaa2c2ae601db447b8fa73cb8205f1b894e7fe2a9a2`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 537 — Node Wrangler-etiketter och visning

Node Wranglers kommandon anger nu uttryckligen att de växlar **visningen** av
nodalternativ respektive nodförhandsgranskning. Hjälptexten för ersättning är
också idiomatisk svenska.

`blender-ui-sv-reviewed-batch-1537-node-label-and-display-20261110.po`
innehåller tre granskade poster med SHA-256
`a823cba01eee054b1875298fb45f39ed8ed5e2124a3d0eba322e641ea7e0c283`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 538 — rutmarkering i nodredigeraren

Nodredigerarens valverktyg använder den etablerade Blender-termen
**rutmarkering**, i linje med övriga markeringsverktyg.

`blender-ui-sv-reviewed-batch-1538-node-box-selection-20261110.po`
innehåller en granskad post med SHA-256
`c986efef561c9aef28444b44344c35c6bbbd00ca2db9e3cee4ac6caab562f517`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 539–540 — skärmutrymme och bakningsutdata

Objektplacering använder den etablerade Blender-termen **skärmutrymme**.
Bakningsgränssnittet använder naturliga svenska för kartans höjd och
passfiltrering.

`blender-ui-sv-reviewed-batch-1539-object-screen-space-20261110.po`
innehåller två granskade poster med SHA-256
`6132337431b487ac0369f765069c148ac919ed28a9625162ab0684cd99f5c15f`.
`blender-ui-sv-reviewed-batch-1540-bake-output-wording-20261110.po`
innehåller två granskade poster med SHA-256
`cbb87b7438ea338ac283767b7d9bbfcd23df17ef962c8f61f3ebc85617da8ede`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batcherna är
lokalt arkiverade och väntar på manuell import.

## Blender Translate-import 2026-11-10 08:07 CET

Den manuella importen av
`blender-ui-sv-reviewed-sedan-kl-16-20261109-till-20261110-0807.po` är
verifierad i Blender Translate: **413** strängar behandlades, **240**
uppdaterades, **173** hoppades över som redan identiska och **0** strängar
saknades. Detta bekräftar importen till Blender Translate; det är inte ett
påstående om att ändringarna är mergade i Blenders källkod.

## Batch 1 541 — bakningskartans bredd

Bakningskartans horisontella dimension använder motsvarande korta
gränssnittsterm **Bredd**, med samma externa avgränsning som höjdinställningen.

`blender-ui-sv-reviewed-batch-1541-bake-output-width-20261110.po` innehåller
en granskad post med SHA-256
`bd7c41df1da017cc4cf35f63e8da1ceb2f4b06ef077f0899f606cbacda0e7b23`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 542 — nästlad nod-ID

Den tekniska UI-beteckningen följer projektets etablerade versalisering:
**nod-ID**.

`blender-ui-sv-reviewed-batch-1542-nested-node-id-20261110.po` innehåller en
granskad post med SHA-256
`0797dbd5fcf7d1dc9a5c2ec5ab9250ef0f6ff7891eb6e93f4f5e1c2c40f520ea`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 543 — länka eller överför data

Åtgärdsnamnet använder konsekvent verbformen **Länka/överför data**, i stället
för det felaktiga substantivet *Länk*.

`blender-ui-sv-reviewed-batch-1543-link-transfer-data-20261110.po` innehåller
två granskade poster med SHA-256
`ddb9d7710be65a0bc84bb0c326556a948a3942bedfd8dee8938741f494b8b9b2`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 544 — cacha objektets yta

Hjälptexten uttrycker cachelagringen idiomatiskt: **lagra objektets yta i
cache**, i stället för det onödiga verbet *cacha*.

`blender-ui-sv-reviewed-batch-1544-cache-object-area-20261110.po` innehåller
en granskad post med SHA-256
`5801bd9eb3968cba08ad72c32c95734063d9eed6ba898bb94027fc68757e2983`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang rapporterar
en möjlig passivkonstruktion, men formuleringen är en saklig hjälptext och
korrekt svenska. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 545 — aktiv nyckeluppsättning

Hjälptexten använder bestämd form med korrekt genus: **den aktiva
nyckeluppsättningen**.

`blender-ui-sv-reviewed-batch-1545-keying-set-grammar-20261110.po` innehåller
en granskad post med SHA-256
`9f6e9509e14d5f836c6dfa89a34f2989d7a85d3b520dd69274307366ea529c3b`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 546 — spegla hörnpunktsgrupp

Hjälptexten för spegling av hörnpunktsgrupp har delats upp i begripliga
imperativsatser och har nu ett tydligt subjekt i bestämd form.

`blender-ui-sv-reviewed-batch-1546-mirror-vertex-group-help-20261110.po`
innehåller en granskad post med SHA-256
`4d922b92bcdce6d80e1b6c951acdc0d3c97637d54bcd06b8f02bac03f206db41`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar
imperativsatsernas ordföljd samt den etablerade Blender-termen
**hörnpunktsgruppen**; båda är falska positiva. Batchen är lokalt arkiverad
och väntar på manuell import.

## Batch 1 547 — utöka eller minska vikter

Den engelskinfluerade formuleringen *expandera/komprimera* är normaliserad
till den konsekventa svenska gränssnittstermen **Utöka/minska vikter**.

`blender-ui-sv-reviewed-batch-1547-expand-contract-weights-20261110.po`
innehåller en granskad post med SHA-256
`307901f1ddea14951f011790e8df07dae70d3eefe9c22ab97bfa452c0c1dbf6e`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 548 — Outliner-drivrutiner

Outliner-hjälptexterna använder samma etablerade Blender-term som övriga
gränssnittet: **drivrutiner**, inte *drivare*.

`blender-ui-sv-reviewed-batch-1548-outliner-drivers-20261110.po` innehåller
två granskade poster med SHA-256
`3ae1cc2b960cf92ae333019736f567e7045fc6e74021daac191d399df2f46e71`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar
korrekta imperativsatser som möjliga V2-avvikelser; det är falska positiva.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 549 — mappa om datablock

Hjälptexten anger nu uttryckligen vad det klickade elementet är:
**det aktuella (klickade) datablocket**.

`blender-ui-sv-reviewed-batch-1549-remap-data-block-20261110.po` innehåller
en granskad post med SHA-256
`ed08ef06e4754ffe3f3b3be9ce7ef7884c0e49603e9bdd19e84b0124201d1f3d`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar den
korrekta bisatsen som möjlig V2-avvikelse; det är en falsk positiv. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 550 — Outliner-element

Två hjälprader använder nu konsekvent **element** i Outliner-kontext och har
en direkt formulering för att växla mellan öppet och stängt läge.

`blender-ui-sv-reviewed-batch-1550-outliner-item-clarity-20261110.po`
innehåller två granskade poster med SHA-256
`25fb99d97ef84b038dfae691e6d0e01ebab112e5da374c08ca91a59cb53de3e2`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlangs möjliga
V2-avvikelse för den korrekta relativsatsen är en falsk positiv. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 551 — modifierare i vyporten

Modifierarens synlighetsåtgärd använder etablerad Blender-terminologi:
**Växla användning i vyporten**, inte *visningsvy*.

`blender-ui-sv-reviewed-batch-1551-modifier-viewport-20261110.po` innehåller
en granskad post med SHA-256
`ef81e25e1fe1fc7d7258db6857d7a6c9fae197adff596a573466aa769f255fe0`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar den
etablerade Blender-termen **vyporten** som sällsynt; det är en falsk positiv.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 552 — Outliner-rutmarkering

Outliner använder den etablerade Blender-termen **rutmarkering** konsekvent,
i stället för den engelskinfluerade varianten *boxmarkering*.

`blender-ui-sv-reviewed-batch-1552-outliner-box-selection-20261110.po`
innehåller två granskade poster med SHA-256
`b1402881713fcf45805eb4199a3bf8a76210b8f78425c0d786b37528f499b973`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar
den etablerade facktermen **rutmarkering** som sällsynt; det är en falsk
positiv. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 553 — målningsplats och hörnpunkter

Två gränssnittstermer är normaliserade: **målningsplats** används konsekvent
för *paint slot*, och *vertices* är **hörnpunkter**, inte *hörn*.

`blender-ui-sv-reviewed-batch-1553-paint-slot-vertices-20261110.po`
innehåller två granskade poster med SHA-256
`f1cbcf355273b7007a42fbbbbe5c4039b3fbc501c2ec1fef1cf2de49d4a764e0`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar
den sammansatta facktermen **materialskiktstyp** som sällsynt; det är en falsk
positiv. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 554 — Paint-gester

Paint-åtgärderna namnger nu arbetsflödet uttryckligt med **lassomarkering**,
**linje** och **polylinje**. Den sammanhängande termen för *Mask Box Gesture*
är **maskrutgest**.

`blender-ui-sv-reviewed-batch-1554-paint-gesture-terms-20261110.po`
innehåller fyra granskade poster med SHA-256
`8099c335f569dabe4c884376428e69e507fc5379b5cd9abcb1cd584e67053f23`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar
projektets facktermer som sällsynta; det är falska positiva. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 555 — hörnpunktsmarkering

Paint-hjälptexterna använder nu **hörnpunkter** konsekvent och har en tydlig
ordföljd för att dölja omarkerade hörnpunkter.

`blender-ui-sv-reviewed-batch-1555-vertex-selection-20261110.po` innehåller
två granskade poster med SHA-256
`a682335c069cf61347f89b9cdc8b231d21ef09fe748499cead05157f96bb8a51`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 556 — högdagervinkel

Inställningen för ljusa områden i hörnpunktsfärgningen använder nu den
idiomatiska facktermen **Högdagervinkel**, i stället för den felaktiga
uppmaningen *Markera vinkel*.

`blender-ui-sv-reviewed-batch-1556-highlight-angle-20261110.po` innehåller
en granskad post med SHA-256
`e33baae3428c57491ded08ad1779270ba5b0887fabe0f804ad366306cb56edcd`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 557 — växla partikelredigeringsläge

Åtgärdsnamnet har en fullständig imperativform utan det felaktiga
prepositionsvalet *växla mellan partikelredigeringsläge*.

`blender-ui-sv-reviewed-batch-1557-particle-edit-toggle-20261110.po`
innehåller en granskad post med SHA-256
`9163f50d6261c9b41ee37ffef652abffa998bb2a8b748f98b3d7dfb54c3989f3`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar den
etablerade sammansättningen **partikelredigeringsläge** som sällsynt; det är en
falsk positiv. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 558 — partikelvikters nycklar

Hjälptexten för partikelviktens interpolering använder **nycklarnas vikt**;
det tidigare *tangenternas vikt* syftade på fel Blender-begrepp.

`blender-ui-sv-reviewed-batch-1558-particle-weight-keys-20261110.po`
innehåller en granskad post med SHA-256
`d84c6378fbac4ca21d0125becc6767fb8ef1d66b70bb99d3b2ed1978cc8a8df0`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 559 — posens ben

Pose-resursens hjälptext hänvisar nu korrekt till **denna pose**, inte till
*denna position*.

`blender-ui-sv-reviewed-batch-1559-pose-bones-20261110.po` innehåller en
granskad post med SHA-256
`45b4caa68cb647deca96426d433fbdcdae1a6d645522540e00baa643156266b9`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlang markerar den
korrekta relativa satsen som en möjlig passivkonstruktion; det är en falsk
positiv. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 560 — pose och bensamlingar

Posespridning avser en Blender-**Action**, inte en generell *åtgärd*.
Beninsamlingar har dessutom normaliserats till den etablerade termen
**bensamling** i Rigify-referenslistan.

`blender-ui-sv-reviewed-batch-1560-pose-propagate-bone-collections-20261110.po`
innehåller tre granskade poster med SHA-256
`5e93f76577d14cc99867a91853d3e19505af08795c7c128372c7efa917829fb0`.
`msgfmt`, l10n-lint och Gitleaks passerade. hunspell-sv och svlang markerar
det avsiktliga Blender-namnet *Actionen* som ovanligt; ingen rättning behövs.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 561 — urvalsuppsättningar

Blenders **Selection Set** är nu konsekvent **urvalsuppsättning**. Den äldre
termen *markeringsuppsättning* hade blandats in i poseringsverktyg, meddelanden
och Rigify-relaterade menyer.

`blender-ui-sv-reviewed-batch-1561-selection-sets-20261110.po` innehåller 21
granskade poster med SHA-256
`dcfa42d1d8584820f2f8bac373ce31ec441b274d304e6ab0f5ec737b005bcb8d`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade. svlangs två
V2-varningar är falska positiva. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 562 — vyportsrendering

Renderingskommandot använder nu den etablerade Blender-termen **vyport** i
stället för det inkonsekventa *visningsvy*.

`blender-ui-sv-reviewed-batch-1562-viewport-render-20261110.po` innehåller två
granskade poster med SHA-256
`604a70c4cc08f0778057014a64eaa933ea92198eb1bef28aa0989aa6d58bb5cb`.
`msgfmt`, l10n-lint och Gitleaks passerade. hunspell-sv och svlang markerar
den etablerade Blender-termen *vyport* som ovanlig; ingen rättning behövs.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 563 — filkoppling

Den tekniska termen **filkoppling** används nu konsekvent i stället för
*filassociation*.

`blender-ui-sv-reviewed-batch-1563-file-association-20261110.po` innehåller en
granskad post med SHA-256
`d91562659e07d30f189449d4bc646450f483ca654e59925cc1ea58311651657b`.
`msgfmt`, l10n-lint, hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 564 — tidigare åtgärder

Menyn **Repeat History** heter nu **Tidigare åtgärder**, med en idiomatisk
hjälptext.

`blender-ui-sv-reviewed-batch-1564-repeat-history-20261110.po` innehåller två
granskade poster med SHA-256
`161d987c89a3aa9ef68870bece841b25c852b2833b4ef67621cfa3401c91de40`.
Samtliga lokala kontroller passerade. Batchen väntar på manuell import.

## Batch 1 565 — utöka i skulptering

Den engelska åtgärden **Expand** heter nu konsekvent **Utöka** i pensel- och
skulpteringsverktygen, i stället för låneformen *Expandera*.

`blender-ui-sv-reviewed-batch-1565-sculpt-expand-20261110.po` innehåller två
granskade poster med SHA-256
`2ed6686de506835fdb3f24495b39c8f336ac1bab6c1876670e73472d8e30dc44`.
Samtliga lokala kontroller passerade. Batchen väntar på manuell import.

## Batch 1 566 — rutgest för ytuppsättning

**Face Set Box Gesture** följer nu den etablerade Blender-termen **rutgest**.

`blender-ui-sv-reviewed-batch-1566-face-set-box-gesture-20261110.po`
innehåller en granskad post med SHA-256
`b09af6b2b207337dd6ce67301d627e207c93589d563342a1553bae04b0351ef3`.
`msgfmt`, l10n-lint, hunspell-sv och Gitleaks passerade; svlang-varningen för
den fackspecifika sammansättningen är falsk positiv. Batchen väntar på manuell
import.

## Batch 1 567 — vyport för ytuppsättningar

Ytuppsättningarnas förhandsvisning använder nu den etablerade termen
**vyporten** i stället för *visningsvyn*.

`blender-ui-sv-reviewed-batch-1567-face-set-viewport-20261110.po` innehåller
en granskad post med SHA-256
`22c4e2fdc1031866b850f725833e288529f7e863cad4aa6e3af5815d4f3121c2`.
`msgfmt`, l10n-lint och Gitleaks passerade. De projektspecifika termerna som
hunspell-sv och svlang markerar är korrekta. Batchen väntar på manuell import.

## Batch 1 593 — Cycles ljuskälla vid sampling

Cycles-hjälptexten för baksidesemission använder nu konsekvent
**ljuskälla vid sampling**, i stället för det oprecisa *ljus för provtagning*.

Deltafilen
`blender-ui-sv-reviewed-batch-1593-cycles-light-sampling-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint och Gitleaks passerade.

## Batch 1 594 — källtroget skiljetecken

117 svenska UI-poster följer nu källans skiljetecken: när källan saknar
tankstreck används inte heller ett svenskt tankstreck. Poster där källan har
tankstreck har lämnats oförändrade.

Deltafilen
`blender-ui-sv-reviewed-batch-1594-source-punctuation-20261110.po` väntar på
manuell import. `msgfmt` och Gitleaks passerade. l10n-lint rapporterar endast
förväntade stilvarningar för sifferintervall som följer källans bindestreck.

## Batch 1 595 — BVH-typ i vyport

Cycles-inställningen **Viewport BVH Type** använder nu projektets etablerade
term **vyport** i stället för det oprecisa *visningsområde*.

Deltafilen `blender-ui-sv-reviewed-batch-1595-viewport-bvh-20261110.po`
innehåller en granskad post med SHA-256
`be29ef63b865917af18c4aa64b8ac3aeca625c48f32bdb47c298c91173f3e529`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 596 — Cycles brusreducering i vyport

Cycles återstående hjälprader och etiketter för **Viewport** använder nu
konsekvent **vyport**: bland annat brusreducerare, indata- och förfilterpass
samt adaptiv rendering.

Deltafilen `blender-ui-sv-reviewed-batch-1596-viewport-cycles-20261110.po`
innehåller sju granskade poster med SHA-256
`512c858f57b0409031ba2a5a8ce5cce8461c36163528b69fc62fc2065b01f68f`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 597 — Cycles vyportinställningar

Ytterligare Cycles-inställningar använder konsekvent **vyport**, bland annat
indelning, sampel, blandningsavstånd, texturgränser och snabb global
belysning.

Deltafilen `blender-ui-sv-reviewed-batch-1597-cycles-viewport-20261110.po`
innehåller elva granskade poster med SHA-256
`3222c6d442dc0d70251c509776377f68219e64511d3148a6b6b9710d687a2d76`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 598 — Cycles vyport och transmission

Den återstående adaptiva provtagningsraden och brusreduceringen använder nu
**vyporten**. Renderingspasset för `Transmission Color` använder konsekvent
**transmissionsfärg**, i stället för den otydliga allmänna termen
*överföringsfärg*.

Deltafilen
`blender-ui-sv-reviewed-batch-1598-cycles-viewport-transmission-20261110.po`
innehåller tre granskade poster med SHA-256
`8c27bbbfe89c988a1595e18b2993a6c54a3307fa75e46a21a45baf25df77f68e`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 599 — Rigify ögonlocksföljning

Rigify-hjälptexten anger tydligt att de separata X- och Z-reglagen styr
**ögonlocksföljningens inverkan**, i stället för den oidiomatiska och tvetydiga
frasen *ögonlocks följningspåverkan*.

Deltafilen `blender-ui-sv-reviewed-batch-1599-eyelid-follow-20261110.po`
innehåller en granskad post med SHA-256
`58c4312082468ded8dee4a67cd7a8bcb90858146c4caaaa302b9fac77ff82299`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 600 — Rigify kontrollterminologi

Rigify använder nu konsekvent **IK-påverkan**, korrekt konstruktion i
**stöd för enhetlig skalning**, **handflatans rotationsaxel** samt de enhetliga
axelvalen `X-manual`, `Y-manual` och `Z-manual`.

Deltafilen `blender-ui-sv-reviewed-batch-1600-rigify-controls-20261110.po`
innehåller sju granskade poster med SHA-256
`c6ea5f102e981dd117424358954d6b132c209f8fd2c77ca9bb233e54ebb0979b`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 601 — Rigify och EEVEE terminologi

Rigify använder nu idiomatiska former för mittkontroll, förälderns rotation och
skala, målets lokala koordinatrymd samt `Y-axeln`. EEVEE:s inställning avser
utstrålning från **baksidan**.

Deltafilen `blender-ui-sv-reviewed-batch-1601-rigify-eevee-20261110.po`
innehåller fem granskade poster med SHA-256
`32755351ed1a9437ebc7555ded976758668217f0b07f6d2eb69fcbea03c85ad6`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 602 — RegionView3D-vyport

RegionView3D-hjälptexterna använder nu konsekvent **vyport** när den renderade
vyn pausas eller återupptas, i stället för det generiska *visningsområde*.

Deltafilen `blender-ui-sv-reviewed-batch-1602-region-viewport-20261110.po`
innehåller två granskade poster med SHA-256
`f48f6d5c51d7dc9cdd6f208158b5c45a48dd88e6390b0a27fa7c93f130538657`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 603 — kompositörens vyport

Kompositörens hjälptext för interaktiv brusreducering använder nu **vyporten**
i stället för det generiska *visningsområdet*.

Deltafilen
`blender-ui-sv-reviewed-batch-1603-compositor-viewport-20261110.po`
innehåller en granskad post med SHA-256
`e926e61e8d8cfb8e5d4327d168721e410180758a43185c45778b3d66fadfe246`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 605 — styva kroppar och renderingsvyer

Femton Blender-RNA-poster har språkgranskats: aktivt index hänvisar till
**samlingen av renderingsvyer**, objekt med styv kropp uttrycks idiomatiskt,
och dämpning samt styvhet använder konsekvent **för** respektive axel.

Deltafilen `blender-ui-sv-reviewed-batch-1605-rigidbody-terminology-20261110.po`
innehåller 15 granskade poster med SHA-256
`776f1d05f6edf50f89e7da1d766bed8f35cf965cedb2443c2e6964a591b4fbef`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 606 — fysikens axlar och SPH

Tolv hjälptexter och etiketter i simuleringarna för styv kropp och SPH är
språkgranskade. Fjäder-, hastighets- och flytkraftstexterna är idiomatiska,
och **avstötningsfaktor** används konsekvent för repulsion.

Deltafilen `blender-ui-sv-reviewed-batch-1606-physics-terminology-20261110.po`
innehåller 12 granskade poster med SHA-256
`e27fcfb6a78d0942864d41dce37491cf75721ed4a573f77e0e7df57919320646`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 607 — EEVEE och vyport

Fyra EEVEE-poster är språkgranskade: **vyport** ersätter den generiska
benämningen, `Bias` har den tekniska betydelsen **förskjutning**, och två
villkorsmeningar har fått fullständig svensk satsstruktur.

Deltafilen `blender-ui-sv-reviewed-batch-1607-eevee-terminology-20261110.po`
innehåller fyra granskade poster med SHA-256
`4d741fe72d773d4c57162431d5f23141bd8767554427109fe4c7e6602f917a60`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 608 — EEVEE:s vyport och rörelseoskärpa

Fem EEVEE-poster är språkgranskade: läckagebias har den tekniska termen
**läckageförskjutning**, och vyport används konsekvent i skugg- och
brusreduceringsinställningarna.

Deltafilen `blender-ui-sv-reviewed-batch-1608-eevee-viewport-20261110.po`
innehåller fem granskade poster med SHA-256
`ee84d610594fc4daa3ed2b478a4912f291592d7713d73907568a78763ff0322a`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 609 — SMAA i vyport

SMAA-inställningens etikett använder nu konsekvent projekttermen **vyport**.
Deltafilen `blender-ui-sv-reviewed-batch-1609-smaa-viewport-20261110.po`
innehåller en granskad post med SHA-256
`c56b9e9fc93236d65309e57e03b80da67081eeaa3b9ce8049ced115fed2706f6`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 604 — renderingsvyport

Tre renderingsposter använder nu projektets etablerade term **vyport**:
pixelstorlek, fyllda Grease Pencil-streck och visning av meshar.

Deltafilen `blender-ui-sv-reviewed-batch-1604-render-viewport-20261110.po`
innehåller tre granskade poster med SHA-256
`96c09852110e099a6424bf7ccbc9835e4bf0ce28e4185a84426ef8280bc71570`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen väntar på manuell import.

## Batch 1 592 — Rigify Action-inställning

Rigify-hjälptexten behåller Blender-datatypen **Action** i
**Action-inställning**, i stället för den missvisande allmänna betydelsen
*åtgärd*.

Deltafilen `blender-ui-sv-reviewed-batch-1592-rigify-action-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint och Gitleaks passerade.

## Batch 1 591 — procent som egenskapstyp

Egenskapstypen `Percentage` använder konsekvent den etablerade UI-termen
**Procent**. Förklarande löptext behåller vid behov ordet *procentandel*.

Deltafilen
`blender-ui-sv-reviewed-batch-1591-percentage-property-20261110.po` väntar
på manuell import. `msgfmt`, l10n-lint och Gitleaks passerade.

## Batch 1 590 — SMPTE-tidskodens skiljetecken

Hjälptexten för kompakt SMPTE-tidskod följer nu källtextens bindestreck i
stället för ett em dash.

Deltafilen `blender-ui-sv-reviewed-batch-1590-smpte-punctuation-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint och Gitleaks passerade.

## Batch 1 589 — menyetikett

Inställningsetiketten **Close Menu on Leave** använder nu den idiomatiska
bestämda formen: **Stäng menyn när muspekaren lämnar den**.

Deltafilen `blender-ui-sv-reviewed-batch-1589-menu-label-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint och Gitleaks passerade.

## Batch 1 588 — språklistans skiljetecken

En andra post i språklistan hade ett em dash där källtexten använder
bindestreck. Den följer nu källtexten: **Swahili - Kiswahili**.

Deltafilen `blender-ui-sv-reviewed-batch-1588-language-labels-20261110.po`
väntar på manuell import. `msgfmt` och Gitleaks passerade; l10n-lint har
enbart en informationsnotis om att språknamnet avsiktligt är identiskt med
källtexten.

## Batch 1 587 — språklistans skiljetecken

En post i språklistan använde felaktigt ett em dash, trots att källtexten har
bindestreck. Svenskan följer nu källans skiljetecken: **Kroatiska - Hrvatski**.

Deltafilen
`blender-ui-sv-reviewed-batch-1587-language-labels-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint och Gitleaks passerade.

## Batch 1 586 — vyport och visningsinställningar

Fyra UI-poster i system- och visningsinställningarna är granskade.
`Viewport` följer den etablerade Blender-termen **vyport**, och
faktorvisningens `Percentage` heter **Procent**.

Deltafilen
`blender-ui-sv-reviewed-batch-1586-viewport-display-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar endast avsiktliga Blender-termer och
UI-fragment.

## Batch 1 585 — system och videoproxyer

Fem systemposter är granskade. Apple-API:t **Metal** behålls som produktnamn,
*Ambient Color* använder **omgivningsfärg**, och sekvensredigerarens
videoproxyer heter **proxyfiler**, inte proxyservrar.

Deltafilen
`blender-ui-sv-reviewed-batch-1585-system-media-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.
Svlang markerar bara det avsiktliga produktnamnet *Metal*.

## Batch 1 584 — vyportsnavigering och ljud

Fyra UI-poster är granskade. Navigeringsinställningarna använder konsekvent
**vyporten**, och ljudenhetsraden följer källans punktlösa UI-format utan att
införa ett tankstreck.

Deltafilen
`blender-ui-sv-reviewed-batch-1584-navigation-audio-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.

## Batch 1 583 — inmatning och navigering

Fyra poster i textredigerarens och 3D-musens inställningar är granskade.
Tabbar anges som **tabbtecken**, `Viewport` följer **vyporten**, och
kameranavigeringen har en idiomatisk svensk hjälptext.

Deltafilen
`blender-ui-sv-reviewed-batch-1583-input-navigation-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar bara avsiktliga Blender-sammansättningar.

## Batch 1 582 — vyport och filsökvägar

Sex UI-poster i experiment- och filsökvägsinställningarna är granskade.
**Viewport** använder **vyporten**, äldre ångring och blendfilformat har
idiomatiska etiketter, och cachar anges tydligt som cachekataloger.

Deltafilen
`blender-ui-sv-reviewed-batch-1582-filepaths-viewport-20261110.po` väntar
på manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar endast avsiktliga Blender-sammansättningar.

## Batch 1 581 — redigerings- och experimentinställningar

Sju poster i redigerings- och experimentinställningarna är granskade.
**Global Undo** använder nu *Global ångring*, produktnamnet **Cycles** har
återställts, och ett tankstreck som saknas i källtexten har ersatts med kolon.
Fjärranslutna resursbibliotek skrivs utan den otillåtna trippelkonsonanten.

Deltafilen
`blender-ui-sv-reviewed-batch-1581-experimental-preferences-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks
passerade. Hunspell-sv och svlang rapporterar endast produktnamn,
förkortningar och en falsk V2-träff i en imperativ UI-text.

## Batch 1 580 — inställningar för redigering

Sex poster i Blenders inställningar för redigering har språkgranskats:
Blender-versionen i `userpref.blend`, synlighetsväxlar för regioner och
sidofält, F-kurvors opacitet, nyckelkanaler samt ångringssteg.

Deltafilen
`blender-ui-sv-reviewed-batch-1580-preferences-editing-20261110.po` väntar
på manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.
Hunspell-sv markerar endast filnamnet *userpref.blend*, och svlang markerar
felaktigt den grammatiskt korrekta indirekta frågan om nyckelkanaler.

## Batch 1 579 — poseringsben, IK och kanalmatris

Fem UI-poster för poseringsben är språkgranskade. IK-gränsernas oöversatta
*Minimum* använder nu **minimum**, och kanalmatrisens hjälptext anger tydligt
att dess kanaler avser position, rotation och skalning. **Pose Tail Position**
heter **Benspetsposition för pose**.

Deltafilen
`blender-ui-sv-reviewed-batch-1579-pose-bone-ik-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar endast den korrekta Blender-sammansättningen
*benspetsposition*.

## Batch 1 578 — vyport, provtagning och fästning

Åtta UI-poster i Cycles, bildverktyg och sekvensredigeraren är
kontextgranskade. `Viewport` följer **vyport**, verktyget *Sample* använder
**provta**, och sekvensredigerarens *snapping* använder den etablerade termen
**fästning**.

Deltafilen
`blender-ui-sv-reviewed-batch-1578-viewport-sampling-snapping-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks
passerade. Hunspell-sv och svlang markerar endast de avsiktliga
Blender-termerna *hörnpunktsgrupp* och *vyport*.

## Batch 1 577 — vyport, XR och filhantering

Tio UI-poster i filhantering, USD-export, XR-navigering och paneler är
kontextgranskade. **Remap Relative** anger nu tydligt att det är relativa
**sökvägar** som mappas om. XR:s *snap turn* är **stegvis vridning**, och
samtliga nya `Viewport`-förekomster följer termen **vyport**. En
skulpteringsbeskrivning använder semikolon i stället för ett tankstreck som
saknas i källtexten.

Deltafilen
`blender-ui-sv-reviewed-batch-1577-viewport-xr-filehandling-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks
passerade. Hunspell-sv markerar bara avsiktliga Blender-/USD-termer, och
svlang markerar en grammatisk korrekt parentes som falsk V2-positiv.

## Batch 1 576 — vyport, begränsningsbox och vycentrering

Tio UI-poster i navigerings- och exportverktygen är kontextgranskade.
**Viewport** använder konsekvent den etablerade Blender-termen **vyport**,
**bounding box** är **begränsningsbox**, och kommandot *Center View to Mouse*
anger uttryckligen **muspekaren**. Lasso-urvalet heter
**lassomarkering**.

Deltafilen
`blender-ui-sv-reviewed-batch-1576-viewport-bounds-navigation-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint, diffkontroll och Gitleaks
passerade. Hunspell-sv markerar endast avsiktliga Blender- och formatord:
*vyport*, *lassomarkering*, *modifierarinställningar*, *SVG* och
*flerupplösningsmodifierare*. Svlang markerar två grammatiskt korrekta
UI-fragment som falska V2-positiv.

## Batch 1 575 — UV-sömnad och uppackning

Två UV-poster är språk- och terminologigranskade: det lagrade
åtgärdsläget heter **Sparat åtgärdsläge**, och hjälptexten för
**Packa upp** följer knappens etablerade UI-term. Deltafilen
`blender-ui-sv-reviewed-batch-1575-uv-stitch-unwrap-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint och Gitleaks passerade; svlang markerar
endast den avsiktliga Blender-termen *meshen*.

## Batch 1 574 — UV-begränsningsboxar och hörnpunkter

Tio UV-poster är normaliserade till den etablerade Blender-terminologin
**begränsningsbox** och **UV-hörnpunkt**. Deltafilen
`blender-ui-sv-reviewed-batch-1574-uv-bounding-box-vertices-20261110.po`
väntar på manuell import. `msgfmt`, l10n-lint och Gitleaks passerade;
Hunspell-sv och svlang har kontrollerats separat före arkivering.

## Batch 1 573 — UV-klippning till gränser

UV-projiceringens *Clip to Bounds* använder nu verbet **klipp** i både
etikett och hjälprad, i stället för den tautologiska formuleringen
*begränsa till gränser*. Deltafilen
`blender-ui-sv-reviewed-batch-1573-uv-clip-bounds-20261110.po` väntar på
manuell import. `msgfmt`, l10n-lint, svlang och Gitleaks passerade utan
rapporter.

## Batch 1 572 — transformering och UV-terminologi

Sju Transform-/UV-poster är normaliserade: fästning ersätter den onödiga
engelska låneformen *snäppning*, *trackball* följer den svenska UI-termen
**styrkula**, och UV-verktygens provtagning, inriktning och
**begränsningsbox** är kontextmässigt konsekventa. Deltafilen
`blender-ui-sv-reviewed-batch-1572-transform-uv-terminology-20261110.po`
väntar på manuell import.

`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv markerar enbart
den avsiktliga sammansättningen *styrkulestil*. Svlang markerar två
imperativformer som heuristiska falska positiva träffar.

## Batch 1 571 — sekvens, ljud, ytnurbs och textredigerare

Sju kontextgranskade poster korrigerar sekvensredigerarens ljudpåslag för
omarkerade remsor, använder **nedmixning** konsekvent, normaliserar NURBS
*surface patch* till **ytplatta** och gör filslutet/interna textfiler
idiomatiska. Deltafilen
`blender-ui-sv-reviewed-batch-1571-sequencer-sound-text-20261110.po`
väntar på manuell import.

`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv markerar den
fackspecifika termen *ytplatta*; svlang markerar en imperativform som en
heuristisk falsk positiv träff.

## Batch 1 570 — sekvensredigerarens tystning och färgprovtagning

Två sekvensredigerarposter är förtydligade: åtgärden för tystning av remsor säger
nu uttryckligen **omarkerade remsor**, och färgprovtagningen använder samma
Blender-term **provta** som övriga provtagningsverktyg. Deltafilen
`blender-ui-sv-reviewed-batch-1570-sequencer-mute-sampling-20261110.po`
innehåller endast dessa två poster och väntar på manuell import.

`msgfmt`, l10n-lint, svlang, Hunspell-sv och Gitleaks passerade utan
rapporter i deltat.

## Batch 1 569 — UV-utjämning och rutskärning

UV-skulpteringens *relax*-verktyg använder nu **utjämning** i stället för
det missvisande *avslappning*. Dessutom är videosekvensredigerarens två
*Box Blade*-etiketter och dess hjälptext normaliserade till **rutskärning**.
Deltafilen `blender-ui-sv-reviewed-batch-1569-uv-relax-box-blade-20261110.po`
omfattar tio kontextgranskade poster och väntar på manuell import.

`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
enbart avsiktliga Blender-/matematiktermer och två imperativformuleringar som
heuristiska falska positiva träffar.

## Batch 1 568 — skulpteringsoperatorer

Tre skulpteringsposter är kontextgranskade. Kommandot *Rebuild BVH* är
normaliserat till **Bygg om BVH**, den onödigt tunga målkonstruktionen i
detaljprovtagningen är förenklad, och den booleska unionen benämns
konsekvent **unionsoperation**. Deltafilen
`blender-ui-sv-reviewed-batch-1568-sculpt-operators-20261110.po` innehåller
endast dessa tre poster och väntar på manuell import.

`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
enbart den avsiktliga fackförkortningen *BVH*.

## Batch 1 492 — klistra in drivrutin

Driver-menyn använder konsekvent Blender-termen **drivrutin**, inte *drivare*.

`blender-ui-sv-reviewed-batch-1492-paste-driver-20261109.po` innehåller en
granskad post med SHA-256
`3cf17eec39848dd1b825abaf796f7a242ec905f7adf7fd331df5f06a5192ec19`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 491 — tvinga bort

Kommandot **Tvinga bort** använder svensk åtgärdsform i stället för det
onaturliga substantivet *Tvinga borttagning*.

`blender-ui-sv-reviewed-batch-1491-force-delete-20261109.po` innehåller en
granskad post med SHA-256
`e0ed47f40b2486535089f73dc4ac434acc472a74a79a6311f4e5a2a7065c8e61`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 489 — utjämning för F-kurvor

F-kurvornas *easing* använder den etablerade Blender-termen **utjämning**, inte
*lättnad*.

`blender-ui-sv-reviewed-batch-1489-easing-terminology-20261109.po` innehåller
två granskade poster med SHA-256
`a60346950331664fff402a7ee31c0c2b4a17569c6c21b6d9e3d99d4a2a19a2ec`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv saknar den korrekta
sammansättningen **F-kurvsegmenten**, och svlang markerar den korrekta relativa
satsen som möjlig V2-avvikelse. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 490 — markering och spegling av nyckelbildrutor

Menyerna använder nu **valda kanaler** och beskriver tidspegling korrekt som
utförd **kring** den aktuella bildrutan eller markören.

`blender-ui-sv-reviewed-batch-1490-keyframe-selection-mirror-20261109.po`
innehåller tre granskade poster med SHA-256
`94da6e8155b0c89f90599fb24fd5e6049f5a3e6d55b7217b25d3c3cce6b929b6`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 488 — byt namn på flera

Åtgärdsetiketten **Byt namn på flera** är tydligare och idiomatiskt svensk än
substantivet *Massomdöpning*.

`blender-ui-sv-reviewed-batch-1488-batch-rename-20261109.po` innehåller en
granskad post med SHA-256
`8bc104f06f66247fcef03fb89c918210d575a567f223612208a33cce2b465a03`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 487 — fastsättning

Pinning-inställningen använder **fastsättning**, konsekvent med den närliggande
knapptexten.

`blender-ui-sv-reviewed-batch-1487-pinning-terminology-20261109.po` innehåller
en granskad post med SHA-256
`3bc2970d85d3a925a492390f5dce817245282576f81f2743244d986621cb47dc`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 485 — växla en visningsnod

Kortkommandot växlar en angiven visningsnod, inte mellan flera noder.

`blender-ui-sv-reviewed-batch-1485-viewer-node-toggle-20261109.po` innehåller
en granskad post med SHA-256
`e3e68141dfc99d87eb3e999c27e28c610332b1978bd18b9f2f7728dada6f852a`.
`msgfmt`, Hunspell-sv, svlang och Gitleaks passerade. l10n-lint rapporterar
endast den engelska källsträngens ovanliga talföljd och tre punkter. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 486 — namnmönster

Urvalsoperatören använder den korta och etablerade termen **namnmönster**.

`blender-ui-sv-reviewed-batch-1486-naming-pattern-20261109.po` innehåller en
granskad post med SHA-256
`44b72314403b19d17457385a28152d3c1a1408caf1ca1eb4fccc9f11e51508b9`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 483 — samplingsintervall

OpenEXR-hjälptexten använder **samplingsintervall**, inte det geografiska
*samplingsområden*, för intervall av provvärden.

`blender-ui-sv-reviewed-batch-1483-sample-ranges-20261109.po` innehåller en
granskad post med SHA-256
`82fadc09514db3b31659a7518ae9ae144720307aaf1fea248331f596516b2ea6`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlang markerar bara
formatnamnet **OpenEXR** som sällsynt. Batchen är lokalt arkiverad och väntar
på manuell import.

## Batch 1 484 — element i nodegränssnittet

Nodegränssnittets *items* använder den konsekventa UI-termen **element**, inte
*objekt*.

`blender-ui-sv-reviewed-batch-1484-interface-elements-20261109.po` innehåller
två granskade poster med SHA-256
`ff9f27ef521d3d6c335d8729fd402b59c61e4cf3a0555743f62d70365df4c00e`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 465 — aktiva filmspår

Filmspårningens hjälptexter använder nu den korrekta betydelsen av *active*:
**Aktivt spår** och **Aktivt planspår**, inte *aktuellt*.

`blender-ui-sv-reviewed-batch-1465-active-tracks-20261109.po` innehåller två
granskade poster med SHA-256
`8e41ef395d9cbb58f6beb2b89b77544ed6a80e119211bb2de09e0729ae30b834`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlangs träffar är
enbart kodidentifierarna `objects[name].plane_tracks.active`.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 480 — vald panel

Statushjälptexten för nodträdsgränssnittet uttrycker ett tillstånd: panelen
**är vald**, inte att den väljs.

`blender-ui-sv-reviewed-batch-1480-panel-selected-state-20261109.po`
innehåller en granskad post med SHA-256
`47efde200a25a678812e15c8b0f3fe9e52e4efbbf2c4a8753062ff6c1bc0d9d0`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 479 — Node Tree Interface-element

Rotpanelens hjälptext använder **element** för Node Tree Interface-poster,
vilket är konsekvent med den omgivande gränssnittsterminologin.

`blender-ui-sv-reviewed-batch-1479-root-panel-elements-20261109.po`
innehåller en granskad post med SHA-256
`328e854a5b1e973d13bcbcb6006d74e4e54d4f5749dfa42f9f6081f49ac9bfbf`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlang markerar den
korrekta relativa bisatsens ordföljd som en falsk positiv.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 478 — Rasterize-terminologi

Geometrinodernas hjälptexter använder nu **rasterisera**, konsekvent med
övrig Blender-UI, i stället för den felaktiga formen *rastrera*.

`blender-ui-sv-reviewed-batch-1478-rasterize-terminology-20261109.po`
innehåller två granskade poster med SHA-256
`981867a944377505e735f545fcb5e1991d11e8c3b97f55b5c94425aa4d04b022`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
den etablerade facktermen *rasterisera* som sällsynt.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 477 — Checker Texture

Texturnodens *Checker* har rättats från den felaktiga personbeteckningen
*Kontrollant* till **Schackmönster**, konsekvent med Image Texture.

`blender-ui-sv-reviewed-batch-1477-checker-texture-20261109.po` innehåller
en granskad post med SHA-256
`dc7b94e438cb3df826208ec08275664e4b902b9a6eecd5b6466210cbef1c1cf3`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 476 — Sky Texture-ozon

Sky Texture-hjälptexten har stavningsrättats från *stadsözon* till
**stadsozon**.

`blender-ui-sv-reviewed-batch-1476-sky-ozone-typo-20261109.po` innehåller en
granskad post med SHA-256
`d76e862391369098f459541d9fd4f2add4f4e03571add3581ac105f8b45a1c1d`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
den korrekta sammansättningen *stadsozon* som sällsynt.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 475 — Float Curve-ordval

Float Curve-noden använder nu **Avbilda** och **mata ut**, konsekvent med
Map Range och andra funktionsnoder, i stället för *Mappa* och *returnera*.

`blender-ui-sv-reviewed-batch-1475-float-curve-wording-20261109.po`
innehåller en granskad post med SHA-256
`d2861413bfb6c870080d1cb65ee8f18b4273122ac0ced156cbb22b2725ac0685`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlang markerar
imperativsatsernas korrekta ordföljd och *indataflyttal* som falska positiva.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 474 — vektortyper för rutnät

Rutnätstyperna använder nu **Dubbelprecisionsvektor** för *Double Vector* och
den korrekt avstavade formen **3D-heltalsvektor**.

`blender-ui-sv-reviewed-batch-1474-grid-vector-types-20261109.po`
innehåller två granskade poster med SHA-256
`e48010589ac35ebf096485afa458829bbbb94ae0e27f7227f215fabc3493a451`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlang markerar
det korrekta fackordet *dubbelprecisionsvektor* som sällsynt.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 473 — Sample Curve-metod

Sample Curve-nodens hjälptext använder det idiomatiska **Metod för att provta
indata**, i stället för den felaktiga formen *samplade indata*.

`blender-ui-sv-reviewed-batch-1473-sample-curve-method-20261109.po`
innehåller en granskad post med SHA-256
`8eca367f6ea5b69b861077b734d15d56cf18439d1b9cb4fc77035219d507d513`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 472 — List Length-element

List Length-noden använder **element** för generiska värden i en lista, i
stället för det alltför specifika *objekt*.

`blender-ui-sv-reviewed-batch-1472-list-length-elements-20261109.po`
innehåller en granskad post med SHA-256
`3b695573dfedbb120407c5084b2361d5b50ecd383dd76569b55d00fe9de93443`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 471 — Filter List-element

Filter List-noden använder **element** för generiska listelement, inte det
för snäva Blender-begreppet *objekt*.

`blender-ui-sv-reviewed-batch-1471-filter-list-elements-20261109.po`
innehåller en granskad post med SHA-256
`c3f0c8237415957f6f80409f769d4e3a8c8f778531c46e1739835b6cd1359b63`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 470 — Poisson-diskfördelning

Poisson-disk-noden använder **Fördela** och det exakta fackordet
**minimiavstånd**, i stället för det engelsknära *Distribuera*.

`blender-ui-sv-reviewed-batch-1470-poisson-distribution-20261109.po`
innehåller en granskad post med SHA-256
`93eb659b864788324052843b804e21a02456889ea10710f75d471cc682a66199`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 469 — Collection Info-transformering

Collection Info-nodens hjälptext använder nu den etablerade tekniska termen
**transformeringen** i stället för den oidiomatiska formen *transformerandet*.

`blender-ui-sv-reviewed-batch-1469-collection-info-transformation-20261109.po`
innehåller en granskad post med SHA-256
`ff8c79174ec615faa156a34732e58eb41c080ba9fbbdb044f4049fdc5ae8c032`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
det korrekta tekniska sammansättningsordet *instansutdata* som sällsynt.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 468 — index för aktivt element

Den generiska nodetiketten **Active Item Index** använder **Index för aktivt
element**, i enlighet med sin hjälptext och de berörda nodernas breda kontext.

`blender-ui-sv-reviewed-batch-1468-active-item-index-20261109.po`
innehåller en granskad delad post med SHA-256
`4c51187a4bebef14e446681031f0097261084a021039d5dff885af752338ecd9`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 467 — Cryptomatte Pick-utdata

Cryptomatte-hjälptexten använder **Pick-utdata** konsekvent för det synliga
uttaget `Pick`.

`blender-ui-sv-reviewed-batch-1467-cryptomatte-pick-output-20261109.po`
innehåller en granskad post med SHA-256
`885ab0bae7cd6dacb51d2fa926eb88dd83bd42e6bfe1b1a2448ff82b9e294d26`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
det korrekta fackordet *mattningen* som sällsynt.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 466 — aktivt utfasat filmspår

Den utfasade egenskapens hjälptext använder också **Aktivt spår**, konsekvent
med de aktuella spåregenskaperna.

`blender-ui-sv-reviewed-batch-1466-deprecated-active-track-20261109.po`
innehåller en granskad post med SHA-256
`2eea6774035b10257e2aaf20d2875a2adbc450a148a3a530ae9f5d86cacabbd9`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlangs träffar är
enbart kodidentifierarna `objects[name].tracks.active`.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 462 — karta över sprutriktning

Ocean-hjälptexten använder nu den idiomatiska formuleringen **kartan över
sprutriktning** i stället för den svårtolkade sammansättningen
*sprutriktningkartan*.

`blender-ui-sv-reviewed-batch-1462-ocean-spray-direction-grammar-20261109.po`
innehåller en granskad post med SHA-256
`70fc631071ae68bb674f490ce744ee311c11dbc253389ce6568526067d67b3ce`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlangs passiv-varning
gäller den naturliga relativa satsen *som används* och är en falsk positiv.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 464 — index för aktivt objekt

Hjälptexten för aktivt objekt använder singular: **Index för det aktiva
objektet**, inte ett index över flera objekt.

`blender-ui-sv-reviewed-batch-1464-active-object-index-20261109.po`
innehåller en granskad post med SHA-256
`8d51bb880e37bfbcb1afa74a56ac4d5094ddd20226442a7629699777eb9978ad`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 463 — texturkoordinaternas källa

Två frågor om texturkoordinater använder nu korrekt svensk ordföljd:
**Från vilket ben/objekt texturkoordinaterna ska hämtas**.

`blender-ui-sv-reviewed-batch-1463-texture-coordinate-question-grammar-20261109.po`
innehåller två granskade poster med SHA-256
`ec66c8ac76f388b662993d6a130bca5b40be1c0766bf95b087c1d0bde9eb7e58`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlangs V2-varning
gäller indirekta frågesatser och är en falsk positiv. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 460 — namnändelse för speglade hörnpunktsgrupper

Exemplet för spegling av hörnpunktsgrupper bevarar nu det funktionella
Blender-mönstret **.R->.L**. De tidigare borttagna punkterna förändrade de
namnändelser som ska matchas.

`blender-ui-sv-reviewed-batch-1460-mirror-vertex-group-pattern-20261109.po`
innehåller en granskad post med SHA-256
`18ba455971e244517e94a8a09b27defb31fdd34fa0751aeb6059d18b6ba7058d`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
facktermen samt kodmönstret som ovanliga; detta är granskade informationssignaler.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 461 — slumpfrö

Det delade Blender-fältet *Random Seed* är nu konsekvent **Slumpfrö**. Den
tidigare termen *Slumptal* avvek från den etablerade benämningen och från
fältets funktion som startvärde för en slumptalsgenerator.

`blender-ui-sv-reviewed-batch-1461-random-seed-terminology-20261109.po`
innehåller en granskad post med SHA-256
`aed030ce3c0cadb654c271884d92e74b4ec3aa38e0314b10148ec8b385ec0894`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 459 — anpassningsmetod

Den delade UI-rubriken *Fit Method* använder nu **Anpassningsmetod** i stället
för den otydliga formen *Passformmetod*. Strängen återanvänds för både
texturmodifierare, kurvritning och sekvenserarens inpassning.

`blender-ui-sv-reviewed-batch-1459-texture-fit-method-terminology-20261109.po`
innehåller en granskad post med SHA-256
`a86217ea80752a4af59ed80ee0e0c99bfd827f144060770f8751689e8fc0c8f2`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 454 — Overlay som blandningsläge

Det återanvända blandningsläget *Overlay* är nu **Överlägg**, samma term som
i Blenders övriga färgkontext. Den tidigare verbformen *Täcka över* var inte
en korrekt eller konsekvent benämning på ett blandningsläge.

`blender-ui-sv-reviewed-batch-1454-overlay-blend-mode-terminology-20261109.po`
innehåller en granskad post med SHA-256
`7a295575a2a49e64821bb0ddd1938d6107bce311747d8414df9365389f4a4930`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 456 — handtagsmarkering

Tre maskhandtags beskrivningar använder nu **markeringstillstånd**, i stället
för den avvikande och mindre precisa formen *valstatus*.

`blender-ui-sv-reviewed-batch-1456-handle-selection-status-20261109.po`
innehåller tre granskade poster med SHA-256
`d3b012caf6b2e0bd9eefde0dd9cf0704dbe68162fb4f24456fd92dd2eeffd35c`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlangs V2-varning
för den frasformade etiketten är en falsk positiv. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 455 — linjeuppsättning

*Line Set* använder konsekvent **linjeuppsättning**. Indexetiketten hade den
avvikande formen *linjesats* och är nu normaliserad.

`blender-ui-sv-reviewed-batch-1455-line-set-consistency-20261109.po`
innehåller en granskad post med SHA-256
`c87642db3178d1624d05e359113e0191e68933f5836bb417dbd82ed993cca36b`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

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

Batch 261 granskar 22 Rigify-strängar för rigg-generering, widgetar,
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
formulerar övriga hjälptexter utan engelska lånord. Deltafilen
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

Batch 684 granskar Asset Shelf-regionens rubrik. *Asset Shelf* är Blenders
snabbåtkomstyta för resurser, och *Header* är en gränssnittsregion. Därför
ersätts den oprecisa texten *Rubrik för tillgångshylla* med *Resurshyllans
huvudrad*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-684-asset-shelf-header.po` är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 685 granskar menyåtgärden för Blenders Header-region. Den felaktiga och
ofullständiga formen *Visa huvud* ändras till *Visa rubrik*, i linje med
katalogens etablerade UI-etiketter *Rubrik* och *Verktygsrubrik*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-685-show-header.po` är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 686 korrigerar en felkopplad WindowManager-sträng för Grease Pencil.
Den beskrev tidigare en pipett för färggradient trots att källsträngen gäller
reservmappningen för Trim-verktyget. Den ersätts med den konsekventa
verktygstexten *3D-vyverktyg: måla Grease Pencil, trimma (reserv)*.
Deltafilen
`blender-ui-sv-reviewed-20261107-batch-686-grease-pencil-trim-fallback.po` är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 687 normaliserar Carver-verktygets två Grease Pencil-tangentmappningar
till samma struktur som intilliggande verktyg: *3D-vyverktyg: måla Grease
Pencil, skärare* och dess reservmappning. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-687-grease-pencil-carver-keymap.po` är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 688 granskar 24 WindowManager-poster för 3D-vyverktygens
reservmappningar. Deras i övrigt svenska verktygsnamn hade den engelska
ändelsen *fallback*, som konsekvent ändras till *reserv* utan att ändra
verktygsnamn, platshållare eller API-termer. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-688-keymap-fallback-suffixes.po` är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 689 rättar WindowManager-gruppen för armaturredigering. *Armering* är
en byggteknisk term och ersätts av Blenders korrekta *armatur* i gruppetiketten
och tio verktygsnamn. Formen *3D-vyverktyg* och suffixet *(reserv)* görs
samtidigt konsekventa inom just denna verktygsgrupp. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-689-armature-keymaps.po` är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 690 granskar FFmpeg- och OpenEXR-texternas kodektermer. Den använder
*kodek*, *videokodek* och *komprimeringskodek* i synlig svensk UI-text, men
behåller format-, API- och parameternamnen **FFmpeg**, **FFV1**, **OpenEXR**
och **Constant Rate Factor (CRF)**. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-690-codec-terminology.po` är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 691 normaliserar 24 WindowManager-tangentmappningar för mesh-, kurv-
och skulpteringsverktyg. Källsträngarnas `(fallback)` behålls för att Weblate
ska kunna matcha dem, medan den synliga svenska texten använder `(reserv)`.
Den samordnar också *3D-vyverktyg*, *armatur*, *kantloopsnitt* och
verktygsformen *slumpa*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-691-keymap-fallbacks-mesh-curve-sculpt.po`
är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 692 granskar XR-teleporteringens färgåterkoppling för raycast-träffar.
Den behåller den tekniska termen *raycast* men ersätter det tvetydiga
pronomenet i hjälprutan med *Färg för raycast vid träff*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-692-xr-raycast-color.po` är lokalt
kontrollerad och ännu inte importerad i Blender Translate.

Batch 693 fortsätter samma XR-granskning. Den normaliserar *VR viewer* till
den etablerade termen *VR-visaren* och gör träff-, miss- och reservfallens
raycast-hjälper konsekventa. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-693-xr-teleportation-context.po` är
lokalt kontrollerad och ännu inte importerad i Blender Translate.

Batch 694 rättar återstående modifier- och verktygsbeskrivningar där Blenders
skelettobjekt *armature* felaktigt hade översatts med byggtermen *armering*.
Den använder konsekvent *armatur* och *armaturobjekt*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-694-armature-modifiers-and-tools.po`
är lokalt kontrollerad och ännu inte importerad i Blender Translate.

Den samlade deltafilen
`blender-ui-sv-reviewed-20261107-batches-684-689-combined.po` innehåller
alla 38 unika, lokalt kontrollerade och ännu ej importerade ändringar. Där
nya batcher överlappar äldre poster innehåller den den senast granskade
formuleringen och är klar för manuell import.

Den ersättande samlade deltafilen
`blender-ui-sv-reviewed-20261107-batches-684-690-combined.po` innehåller 44
unika, lokalt kontrollerade och ännu ej importerade ändringar och är klar för
manuell import. Den ersätter samlingsfilen för batch 684–689.

Den senaste samlade deltafilen
`blender-ui-sv-reviewed-20261107-batches-684-691-combined.po` innehåller
fortfarande 44 unika ändringar: batch 691 rättar befintliga
tangentmappningsposter i stället för att lägga till nya. Den ersätter
samlingsfilen för batch 684–690 och är klar för manuell import.

Den samlade filen för all ännu ej importerad, lokalt granskad Blender UI-text
är `blender-ui-sv-reviewed-20261107-all-pending-batches-680-694.po`. Den
innehåller 86 unika poster från batch 680–694, med de nyare formuleringarna
valda vid eventuell överlappning, och ryms inom den överenskomna
uppladdningsgränsen på 1 000 strängar.

Batch 695 rättar två felskrivningar i operatören som rensar
förhandsvisningar: *Tydliga förhandsvisningar* blir *Rensa
förhandsvisningar*. Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-695.po` innehåller
88 unika, lokalt kontrollerade och ännu ej importerade poster. Den ersätter
samlingen 680–694 och är klar för manuell import.

Batch 696 granskar material för mesh, armaturer, trådram och shadernoder i
deras konkreta Blender-kontext. Den behåller datatypen *mesh* även i plural,
använder *armatur* för skelettobjekt, *trådram* för `Wire`-visningsläget och
*shadernod* där det gäller materialnoder. Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-696.po` innehåller
101 unika, lokalt kontrollerade och ännu ej importerade poster. Den ersätter
samlingen 680–695 och ryms inom den överenskomna uppladdningsgränsen.

Batch 697 granskar FFmpeg-panelens mediaformat. En *container* är här en
mediebehållare, inte ett oförändrat engelskt UI-ord. *Mux* används som den
tekniska processen *muxning*, med sammansättningarna *muxningshastighet* och
*muxpaketstorlek*. Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-697.po` innehåller
107 unika, lokalt kontrollerade och ännu ej importerade poster. Den ersätter
samlingen 680–696 och ryms inom den överenskomna uppladdningsgränsen.

Batch 698 tillämpar terminologin *mesh* konsekvent i den booleska
modifieraren och i glTF-exporten. Blenders datatyp ersätter därför de
allmänna formerna *nät* och *maskor*; *geometrinoder* och *materialplats* är
projektets etablerade UI-termer. Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-698.po` innehåller
110 unika, lokalt kontrollerade och ännu ej importerade poster. Den ersätter
samlingen 680–697 och ryms inom den överenskomna uppladdningsgränsen.

Batch 699 gör den synliga operatörstermen konsekvent: *previews* är
*förhandsvisningar* i Blender UI, inte *förhandsgranskningar*. Den ersättande
samlingsfilen `blender-ui-sv-reviewed-20261107-all-pending-batches-680-699.po`
innehåller 113 unika, lokalt kontrollerade och ännu ej importerade poster.
Den ersätter samlingen 680–698 och ryms inom den överenskomna
uppladdningsgränsen.

Batch 700 förbättrar hjälptexten för fjärranslutna resursbiblioteks
nedladdningscache. Den krystade sammansättningen *nedladdningscachekatalogen*
ersätts med den tydligare formuleringen *cachekatalogen för nedladdning*.
Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-700.po` innehåller
114 unika, lokalt kontrollerade och ännu ej importerade poster. Den ersätter
samlingen 680–699 och ryms inom den överenskomna uppladdningsgränsen.

Batch 701 rättar två tidigare batchers lokala ordval efter kontroll mot hela
Blender UI-katalogen: den etablerade UI-termen för *Preview* är
*förhandsgranskning*, inte *förhandsvisning*. Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-701.po` innehåller
fortfarande 114 unika, lokalt kontrollerade poster, eftersom fem tidigare
poster ersätts i stället för att läggas till. Den ersätter samlingen 680–700
och ryms inom den överenskomna uppladdningsgränsen.

Batch 703 slutför ytterligare tre kontextbundna *wireframe*-texter med
Blenders etablerade term *trådram*: ett bens visningsläge, dess opacitet och
volymvisningens läge. Batch 702 skapades inte, eftersom dess armaturposter
vid en kontroll visade sig redan vara korrekt täckta av batch 694. Den
ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-703.po` innehåller
117 unika, lokalt kontrollerade och ännu ej importerade poster. Den ersätter
samlingen 680–701 och ryms inom den överenskomna uppladdningsgränsen.

Batch 704 fortsätter den kontextstyrda *mesh*-normaliseringen i fem
hjälptexter för resurser, tygsimulering, kollision och Shrinkwrap. De
allmänna formerna *nät*, *basnät* och *målnät* ersätts där de uttryckligen
avser Blenders datatyp. Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-all-pending-batches-680-704.po` innehåller
122 unika, lokalt kontrollerade poster. Den ersätter samlingen 680–703 och
ryms inom den överenskomna uppladdningsgränsen.

Den 7 november 2026 verifierades importen av samlingsfilen för batch
680–704 i Blender Translate. Weblate behandlade **122** strängar, hoppade
över **36**, hittade inga saknade strängar och uppdaterade **86**. Det
bevisar uppladdning och serverbearbetning, men inte projektets separata
granskning eller framtida merge/utgivning.

Batch 705 fortsätter efter den verifierade importen med Node Wranglers
sammanslagningsmeny. Den använder *shadernoder*, i linje med den befintliga
termbasens *shadernod* och med granngruppens *geometrinoder*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-705-node-wrangler-shaders.po`
innehåller en lokalt kontrollerad, ännu ej importerad ändring.

Batch 706 normaliserar tio synliga mesh-etiketter för Blender-datatypen,
datablock, ytor, hörn och samlingar. Den använder *mesh* även i plural och
de svenska facksammansättningarna *meshdatablock*, *meshkant* och *meshyta*.
Den samlade deltafilen
`blender-ui-sv-reviewed-20261107-pending-batches-705-706.po` innehåller
elva unika, lokalt kontrollerade och ännu ej importerade ändringar från
batch 705–706.

Batch 707 fortsätter i Mesh-RNA:s kärnegenskaper: kanter, polygoner,
hörnpunkter, texturutrymme och attribut. Den samlade deltafilen
`blender-ui-sv-reviewed-20261107-pending-batches-705-707.po` innehåller
22 unika, lokalt kontrollerade och ännu ej importerade ändringar. Den
ersätter den mindre samlingen 705–706.

Batch 708, som även har granskats oberoende, normaliserar modifierar- och
geometrinodgruppen: *Mesh till volym*, *Volym till mesh*, kurv- och
punktkonverteringar, automaskering och meshvalidering. Den samlade
deltafilen `blender-ui-sv-reviewed-20261107-pending-batches-705-708.po`
innehåller 34 unika, lokalt kontrollerade kandidater. Den ersätter samlingen
705–707, men måste ombaseras mot en färsk serverexport före uppladdning.

Efter importen konstaterades att den lokala huvudexporten
`/Users/danielnylander/Downloads/blender-ui-ui-sv.po` är äldre än flera
redan uppladdade batcher. Den 7 november 2026 blockerade Blender Translates
Cloudflare-utmaning en direkt, skrivskyddad `curl`-export med HTTP 403.
Nästa breda radgranskning ska därför utgå från en ny export som hämtas via
den inloggade webbläsaren eller ett fungerande API, så att tidigare
serveruppdateringar inte dupliceras.

Den 7 november 2026 hämtades en ny, auktoritativ UI-export via webbläsaren:
`/Users/danielnylander/Downloads/blender-ui-ui-sv (4).po` (40 427 aktiva
strängar). Kandidaterna från batch 705–708 jämfördes nyckel för nyckel med
den exporten. Tolv av 34 var redan identiska på servern och togs bort från
den fortsatta deltafilen. De återstående 22 kontextgranskade ändringarna
ligger i `blender-ui-sv-reviewed-20261107-rebased-batches-705-708.po`.
Filen är kontrollerad med `msgfmt`, `l10n-lint` och `git diff --check`.
Den är lokalt klar för import, men ännu inte uppladdad efter ombasningen.

Batch 709 granskar den nya exporten med tre oberoende, kontextuppdelade
kontroller (nodsystem, riggning/animation samt media/utdata). Förslagen
kontrollerades sedan mot den färska PO-filen och denna termbas. Batchen
normaliserar 21 säkra förekomster av *mesh*, *shadernod*, *geometrinod* och
specialiserade nodträd samt rättar tre felaktigt förkortade tidslinjebeskrivningar.
Förslaget att genomgående ersätta synliga *åtgärdsslotar* med engelska
*Action-slotar* avvisades: termbasen skiljer uttryckligen mellan det formella
datatypnamnet `Action` och den svenska UI-termen *åtgärdsslot*. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-709-nodes-mesh-context.po` är lokalt
granskad och ännu inte importerad.

Batch 710 går vidare med modifierargruppens explicita `Mesh`-datatyper.
Sjutton etiketter och hjälptexter för bakning, texturdata, avfasning,
underindelning, deformation och partikelinstanser använder nu konsekvent
*mesh* där källan avser Blenders datatyp; vanliga *rutnät* har inte ändrats.
Deltafilen `blender-ui-sv-reviewed-20261107-batch-710-mesh-modifiers.po` är
lokalt granskad och ännu inte importerad.

Efter batch 712 ersätts den tidigare samlingsfilen av
`blender-ui-sv-reviewed-20261107-pending-batches-705-712.po`. Den innehåller
90 unika ändringar, samtliga ombaserade mot exporten från 7 november och
fortfarande långt under Weblates gräns på 1 000 strängar. Detta är den
rekommenderade enda importfilen för batch 705–712.

Samlingsfilen har dessutom kontrollerats med `svlang` och `hunspell-sv`.
Deras enda avvikelser är förväntade, projektspecifika fackord och
sammansättningar som redan omfattas av termbasen, bland annat *mesh*,
*shadernod*, *geometrinod*, *tessellering* och *färggradient*. Inga nya
språkfel eller otillåtna tredubbla konsonanter hittades.

Batch 713 är en fristående lokal granskningsfil med 40 kontextbundna
rättelser inom målningskurvor, ytuppsättningar, Grease Pencil-ritningar,
linjekonst och sekvensredigeraren. Den tar hänsyn till att samma engelska
källa förekommer i flera Weblate-kontexter och omfattar därför fler PO-poster
än de 36 unika källfraserna. Filen
`blender-ui-sv-reviewed-20261107-batch-713-paint-grease-sequencer.po` är
lokalt kontrollerad och ännu inte importerad.

Den rekommenderade importfilen är nu
`blender-ui-sv-reviewed-20261107-pending-batches-705-713.po`. Den samlar 130
unika, ombaserade ändringar från batch 705–713 och ligger fortfarande långt
under gränsen på 1 000 strängar per Blender Translate-import.

Batch 711 rättar fyra återstående synliga sammansättningar inom shader- och
textur-nodsystemet: *shadernoder*, *texturnod* och *shaderskriptnod*.
Produktnamn och osäkra generatorsträngar har lämnats oförändrade. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-711-shader-texture-nodes.po` är lokalt
granskad och ännu inte importerad.

Den ersättande samlingsfilen
`blender-ui-sv-reviewed-20261107-pending-batches-705-711.po` innehåller 64
unika, ombaserade och lokalt kontrollerade ändringar från batch 705–711. Den
utgår från exporten hämtad den 7 november och ryms inom Blender Translates
överenskomna gräns på 1 000 strängar per import. De fyra delbatcherna finns
kvar för spårbarhet; samlingsfilen är den rekommenderade importfilen.

Batch 712 normaliserar 26 lokalt kontrollerade UI-texter i tre avgränsade
områden: extensions använder konsekvent *tilläggsförråd*, tygsimuleringen
skiljs från Dynamic Paints *duk*, och färghanteringen använder
*visningstransformering* samt *färggradient* enligt termbasen. Deltafilen
`blender-ui-sv-reviewed-20261107-batch-712-repositories-physics-color.po` är
lokalt granskad och ännu inte importerad.

Batch 714 rättar tio kontextkontrollerade UI-texter för *vyport*, *gizmo*,
*poseringsrymd* och *transformationsmatris*. Batch 715 lägger till arton
kontrollerade rättelser för uttryckligen 3D-bundna vyporter samt färghantering,
världsrymd och kompositionsremsor. Båda batcherna är lokalt kontrollerade och
ännu inte importerade.

Den ersättande rekommenderade importfilen är
`blender-ui-sv-reviewed-20261107-pending-batches-705-715.po`. Den innehåller
155 unika ändringar, samtliga verifierade mot exporten från 7 november: ingen
post saknas från exporten och ingen återger exportens befintliga översättning.
Den ryms väl inom gränsen på 1 000 strängar per import. `msgfmt`,
`l10n-lint`, sammanslagningskontroll, diffkontroll och Gitleaks passerade.

Batch 716 samlar 27 ytterligare, oberoende kontrollerade ändringar: Blenders
`Mesh`-datatyp använder konsekvent *mesh* i meshöar, meshtopologi och
meshobjekt; Extensions använder *förråd*; och simuleringarnas *punktcache*,
*gizmo*, *partikelvätska* och *bakning* följer termbasen. Batchen är lokalt
kontrollerad och ännu inte importerad.

Den ersättande rekommenderade importfilen är
`blender-ui-sv-reviewed-20261107-pending-batches-705-716.po`. Den innehåller
178 unika ändringar. Samtliga finns i exporten från 7 november och skiljer
sig från exportens aktuella översättning; ingen post är därför en överflödig
omimport. Filen är fortfarande väl under gränsen på 1 000 strängar.

Blender Translate-importen av batch 705–713 är verifierad den 7 november.
Servern behandlade 130 poster: 119 uppdaterades, 11 hoppades över och 0
saknades. Den tidigare samlingsfilen för 705–713 ska därför inte laddas upp
igen. Den äldre exporten på lokal disk är nu delvis föråldrad och används bara
för fortsatt lokal terminologigranskning tills en ny export har hämtats.

Batch 717 fortsätter med armaturens ID-typ och bendata, skulpteringens
meshdatatyp samt fler Extensions-texter. Den bevarar det synliga produktnamnet
*Bendy Bones*, men normaliserar bland annat *armatur*, *viloposition*,
*texturnod* och *förråd*. Operator-kontexten för ”Add Repository…” verifierades
separat vid sammanslagningen.

Batch 718 normaliserar nod- och animationsbegrepp enligt termbasen:
*shadernod*, *visningsnod*, *kompositör*, *dopeblad*, *drivrutin* och
*filutdata*. Ändringarna är begränsade till explicita datatyper, operatorer och
paneler; generiska och tvetydiga viewer-strängar har lämnats orörda.

Blender Translate-importen av batch 714–718 är verifierad den 7 november.
Servern behandlade 109 poster: 97 uppdaterades, 12 hoppades över och 0
saknades. Filen `blender-ui-sv-reviewed-20261107-pending-batches-714-718.po`
ska därför inte laddas upp igen. Nästa deltafil byggs endast av senare,
separat granskade batcher.

Batch 719 är den nästa fristående, lokalt kontrollerade deltafilen. Den
normaliserar 17 kontextbundna material-, kompositör- och meshtermer, bland
annat *färggradient*, *underytsspridning*, *meshkant* och *meshyta*. Den är
ännu inte importerad och ska inte blandas ihop med de redan behandlade
batcherna 705–718.

Batch 720 kompletterar den lokala granskningen med 20 specifika förekomster av
*geometrinod*, *geometrinodmodifierare*, *kompositionsnodträd* och
*sekvensredigerare*. Arbetsytor, skärmlayouter och filhantering granskades
samtidigt men krävde inga säkra ändringar.

Den aktuella rekommenderade importfilen är
`blender-ui-sv-reviewed-20261107-pending-batches-719-720.po`. Den innehåller
37 lokalt kontrollerade, ännu ej importerade poster och har passerat `msgfmt`,
`l10n-lint`, sammanslagningskontroll, diffkontroll och Gitleaks.

Batch 721 utökar den lokala granskningen med 26 kontextbundna rättelser inom
riggning, fysik och Extensions. Den följer termbasens *armatur*, *styv kropp*,
*punktcache* och *tilläggsförråd* och lämnar produktnamn samt tvetydiga
generella UI-texter orörda.

Batch 722 granskar nio explicit kompositörsbundna texter och normaliserar
*kompositör*, *kompositionsnodgrupp* och *visningsnod*. Batch 723 granskar tio
Grease Pencil- och anteckningssträngar: data som avser ritade markeringar heter
*streck*, medan verbet för verktygets åtgärd inte felaktigt byts ut mot ett
databegrepp.

Den aktuella rekommenderade importfilen är
`blender-ui-sv-reviewed-20261107-pending-batches-719-723.po`. Den innehåller
82 lokalt kontrollerade och ännu ej importerade poster från batch 719–723. Den
bygger på exporten från 7 november men utesluter uttryckligen de redan
serververifierade batcherna 705–718. `msgfmt`, `l10n-lint`, sammanslagnings- och
diffkontroll samt Gitleaks passerade. `svlang` och svensk Hunspell gav bara
förväntade tekniska Blender-sammansättningar och UI-fragment; inga konkreta
språkfel identifierades.

Batch 724 granskar ytterligare tio otvetydiga förekomster i Grease Pencil- och
anteckningsdata. Den normaliserar dataresultatet *stroke* till *streck* i
strecksamlingar, streckpunkter, radering, kloning och målningslägen, men låter
*penseldrag* vara kvar där källtexten uttryckligen beskriver penselns rörelse.
Batchfilen är lokalt kontrollerad och separat från den ännu ej importerade
samlingsfilen 719–723, eftersom den lokala källexporten saknar de senaste
serverändringarna.

Blender Translate-importen av batch 719–723 är verifierad den 7 november.
Servern behandlade 82 poster: 65 uppdaterades, 17 hoppades över och 0 saknades.
Filen `blender-ui-sv-reviewed-20261107-pending-batches-719-723.po` ska därför
inte laddas upp igen. Batch 724 är den nästa lokalt kontrollerade, ännu ej
importerade filen; en ny källexport behövs innan fler delbatcher säkert kan
sättas samman till en gemensam importfil.

Batch 725 granskar sju explicita egenskaper för nodin- och utdata. Formella
synliga noder behåller Blenders etablerade term *utgångsnod*, medan verkliga
dataobjekt använder *indata* och *utdata*: exempelvis *slutningsindataobjekt*
och *filutdataobjekt*. Batchen är lokalt kontrollerad och ännu inte importerad.

Batch 727 fortsätter den avgränsade Action-granskningen i operatörer och
NLA-redigeraren. Den använder *Action-datablock* i löpande text när det gör
det formella namnet böjbart och lättläst, samt *Action-slot*, *Action-remsa*
och *Action-clippremsa* i synliga UI-etiketter. Batchen är lokalt kontrollerad
och ännu inte importerad.

Batch 728 granskar 20 kärnposter för Action-grupper, -lager, -posemarkörer,
-slotar och -remsor. Den behåller API-klasserna `ActionChannelbag` och
`ActionKeyframeStrip` oförändrade men använder svenska, läsbara sammansättningar
runt dem. Batchen är lokalt kontrollerad och ännu inte importerad.

Batch 729 granskar 16 beskrivningstexter för samma datatyp. Den använder
*Action-datablock* där den tekniska betydelsen behöver förtydligas, men behåller
vanlig svensk sakprosa för hanteringsåtgärder. Batchen är lokalt kontrollerad
och ännu inte importerad.

Batch 730 avslutar den här Action-serien med 14 användarsynliga status- och
feltexter i Action- och NLA-redigerarna. Den använder konsekvent
*Action-redigeraren*, *Action-slot* och *Action* där meddelandet avser den
formella animationsdatatypen. Batchen är lokalt kontrollerad och ännu inte
importerad.

Efter den serververifierade importen av batch 719–723 återstår följande
separata, lokalt kontrollerade deltafiler: batch 724 (10), 725 (7), 726 (22),
727 (19), 728 (20), 729 (16), 730 (14), 731 (10), 732 (9) och 733 (7) —
sammanlagt 134 poster. De har inte slagits ihop, eftersom exporten från 7
november saknar de senare serverändringarna. Varje fil är betydligt mindre än
gränsen på 1 000 poster per Blender Translate-import och kan därför importeras
självständigt utan att blanda in redan verifierade batcher.

Batch 731 normaliserar tio explicita `3D Viewport`-förekomster till
*3D-vyport* enligt termbasen. Den lämnar generiska visningsfönster utan denna
formella Blender-källterm oförändrade. Batchen är lokalt kontrollerad och ännu
inte importerad.

Batch 732 normaliserar nio explicit shadernodbundna UI- och feltexter.
*Shadernod*, *shadernodträd* och *shadernodredigerare* följer termbasen;
generella skuggningsbegrepp utan nodkontext har inte ändrats. Batchen är lokalt
kontrollerad och ännu inte importerad.

Batch 733 normaliserar sju explicita Color Ramp-åtgärder och hjälprutor till
*färggradient* och *färgstopp*. Batchen är lokalt kontrollerad och ännu inte
importerad.

Batch 734 rättar tre etiketter för Blenders formella animationsdatatyp
*Action*. Den tidigare formen *Åtgärd* blandade ihop datatypen med en allmän
handling. Den nya formen *Action* följer terminologilistan i ID-, NLA-,
Dope Sheet- och Rigify-kontext. Batchen är lokalt kontrollerad och ännu inte
importerad.

Batch 735 kompletterar kompositörens redan normaliserade precisionsläge genom
att använda *fullständig precision* också i dess förklarande hjälptext.
Batchen är lokalt kontrollerad och ännu inte importerad.

Batch 736 rättar skiljetecknet i ett statusmeddelande i grafredigeraren, så
att det följer källtextens UI-form. Batchen är lokalt kontrollerad och ännu
inte importerad.

Batch 737 normaliserar EEVEE-inställningen *Full resolution* till
*Fullständig upplösning*. Batchen är lokalt kontrollerad och ännu inte
importerad.

Batch 738 rättar ett felaktigt statusmeddelande i grafredigeraren: samplade
F-kurvor kan inte ta emot nyckelbildrutor. Batchen är lokalt kontrollerad och
ännu inte importerad.

För manuell import finns även
`blender-ui-sv-reviewed-20261107-pending-batches-724-733.po`. Den förenar
batcherna 724–733 till 132 unika poster. De två poster som förekommer i både
batch 728 och 729 har identisk svensk översättning och har därför avdubbletterats.
Samlingsfilen är lokalt kontrollerad men ännu inte importerad.

Den nyare samlingsfilen
`blender-ui-sv-reviewed-20261107-pending-batches-724-737.po` innehåller alla
138 unika poster från batch 724–737 och ersätter 724–733-filen när samtliga
ännu väntar på import. Den är lokalt kontrollerad men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-724-738.po` är den aktuella
samlingsfilen. Den innehåller 139 unika poster från batch 724–738 och ersätter
724–737-filen. Blender Translate-importen är verifierad den 7 november:
servern behandlade 139 poster, uppdaterade 129, hoppade över 10 och saknade 0.
Filen ska därför inte laddas upp igen.

Batch 739 fortsätter med Grease Pencil- och anteckningsdata. I denna
datamodell avser *stroke* det ritade dataobjektet, inte användarens
penselrörelse; den konsekventa svenska termen är därför *streck*. Deltafilen
innehåller tio lokalt granskade ändringar.

Batch 740 tillämpar samma åtskillnad på samlingar, penselinställningar och
visningsfilter för Grease Pencil. Anteckningsstreck och streckpunkter är
dataobjekt, medan *penseldrag* behålls när texten beskriver användarens
faktiska rörelse. Deltafilen innehåller tolv lokalt granskade ändringar.

Batch 741 rättar ett enda nodgränssnitt: ett inaktivt uttag påverkar nodens
*utdata*, inte den generiska *utmatningen*. Deltafilen är lokalt granskad.

Batch 742 korrigerar tre lokala sammanhang där Blender-datatypen *mesh*
felaktigt blivit *nät*. I modifierar- och cachekontext behålls *mesh* enligt
den projektspecifika terminologin. Deltafilen är lokalt granskad.

`blender-ui-sv-reviewed-20261107-pending-batches-739-742.po` är den aktuella
samlade importfilen för de fyra efterföljande batcherna. Den innehåller 26
unika, lokalt granskade ändringar och ryms väl inom Blender Translates gräns
på 1 000 strängar per import.

Batch 743 följer termlistans beslut att behålla Blenders synliga namn
*Outliner*. Tjugo operatörs- och hjälprader som tidigare använde det generiska
*översikten* får därför konsekvent det faktiska UI-namnet. Deltafilen är
lokalt granskad.

Batch 744 granskar vidare Outliner-referenser i egenskaper, synkronisering,
redigeringslägen och felmeddelanden. Namnet behålls också i sammansättningar
som *Outliner-trädet* och *Outliner-region*. Deltafilen innehåller tretton
lokalt granskade ändringar.

Batch 745 fullföljer samma normalisering i fem felmeddelanden där användaren
behöver öppna eller tolka det faktiska Outliner-trädet. Deltafilen är lokalt
granskad.

Batch 746 avslutar den lokalt identifierade Outliner-normaliseringen i
hjälptext och tema. Den rättar dessutom fyra sammanhang där *Action* är
Blenders formella animationsdatatyp, inte den vanliga svenska handlingen
*åtgärd*. Deltafilen innehåller sju lokalt granskade ändringar.

Batch 747 tillämpar Shrinkwrap-terminologin på modifierarens målegenskaper:
det synliga funktionsnamnet *Shrinkwrap* behålls, medan objektet som används
som mål blir *målmeshobjekt*. Deltafilen innehåller fyra lokalt granskade
ändringar.

`blender-ui-sv-reviewed-20261107-pending-batches-739-743.po` ersätter
739–742-samlingen. Den innehåller 46 unika, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261107-pending-batches-739-744.po` ersätter
739–743-samlingen. Den innehåller 59 unika, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261107-pending-batches-739-745.po` ersätter
739–744-samlingen. Den innehåller 64 unika, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261107-pending-batches-739-746.po` ersätter
739–745-samlingen. Den innehåller 71 unika, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261107-pending-batches-739-747.po` ersätter
739–746-samlingen. Den innehåller 75 unika, lokalt granskade ändringar.
Blender Translate-importen är verifierad den 7 november: servern behandlade
75 poster, uppdaterade 57, hoppade över 18 och saknade 0. Filen ska därför
inte laddas upp igen.

Batch 748 normaliserar åtta data- och API-rader till termbasens *visningslager*
för Blender-begreppet *view layer*. Den äldre kortformen *vylager* ersätts i
den aktiva arbetsytan, Cycles-inställningarna och egenskaper för samling,
material och sampling. Deltafilen är lokalt granskad och ännu inte importerad.

Batch 749 granskar de återstående UI-raderna för *wireframe*. Den tekniska
modifierarbeskrivningen blir *modifierare för trådramseffekt*, och
visningsmeddelandet anger de faktiska skuggningslägena i *3D-vyporten*.
Deltafilen är lokalt granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-749.po` är den samlade
importfilen för de två nya batcherna. Den innehåller tio unika, lokalt
granskade ändringar och ryms väl inom Blender Translates gräns på 1 000
strängar per manuell import.

Batch 750 granskar den formella animationsdatatypen *Action* i dess egna
RNA-, NLA- och posebibliotekskontexter. Här behålls produktnamnet i former
som *Action-slot* och *skiktad Action*; vanliga åtgärder och XR-händelser har
medvetet lämnats utanför. Deltafilen innehåller arton lokalt granskade
ändringar och är ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-750.po` ersätter
748–749-samlingen. Den innehåller 28 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 751 normaliserar fem RNA- och UI-rader från den generella *dataväg* till
termbasens exakta *datasökväg*. Det omfattar Freestyle-nyckeluppsättningar,
kopieringskommandot i egenskapsmenyn och radiella kontrollers primära och
sekundära sökvägar. Deltafilen är lokalt granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-751.po` ersätter
748–750-samlingen. Den innehåller 33 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 752 slutför den närliggande nodterminologin med *indataobjekt* för
geometrinodernas samling av inmatningsobjekt. Den följer batch 725:s
normalisering av explicita nodindata och är lokalt granskad men ännu inte
importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-752.po` ersätter
748–751-samlingen. Den innehåller 34 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 753 synkroniserar Outlinerns felmeddelande för bibliotekslänkade
åsidosättningsobjekt med den etablerade svenska formulering som redan används
i motsvarande meddelande i skärmområdet. Deltafilen är lokalt granskad och
ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-753.po` ersätter
748–752-samlingen. Den innehåller 35 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 754 normaliserar tre ytterligare *Library Override*-rader till
*biblioteksåsidosättning* och *samlingsåsidosättning*. Här avser *override*
Blenders formella åsidosättningsfunktion, inte filöverskrivning. Deltafilen
är lokalt granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-754.po` ersätter
748–753-samlingen. Den innehåller 38 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 755 rättar fyra felmeddelanden om *override data* till
*åsidosättningsdata*. De avser Blenders egenskaps- och
biblioteksåsidosättningar, inte filöverskrivning. Deltafilen är lokalt
granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-755.po` ersätter
748–754-samlingen. Den innehåller 42 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 756 normaliserar en Grease Pencil Line Art-beskrivning från den
avvikande formen *skärmkoordinatrum* till den etablerade Blender-termen
*skärmrymd*. Deltafilen är lokalt granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-756.po` ersätter
748–755-samlingen. Den innehåller 43 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 757 normaliserar två animeringsrader till termbasens
*förhandsgranskningsintervall*. I Blender är *Preview Range* ett valt
bildruteintervall, inte ett generellt område. Deltafilen är lokalt granskad
och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-757.po` ersätter
748–756-samlingen. Den innehåller 45 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 758 korrigerar Grease Pencil Line Arts avvikande *baksidesklippning*
till den etablerade renderingstermen *baksidesgallring*. Deltafilen är lokalt
granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-758.po` ersätter
748–757-samlingen. Den innehåller 46 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 759 rättar den kvarvarande modifierarbenämningen för *Remesh* till
termbasens *ommeshning*: *ommeshningsmodifierare*. Deltafilen är lokalt
granskad och ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-759.po` ersätter
748–758-samlingen. Den innehåller 47 unika, lokalt granskade och ännu inte
importerade ändringar.

Batch 760 normaliserar fem interna mesh-topologitermer till *meshloop* och
*looptriangel*. Granskningen är begränsad till RNA-klasserna `MeshLoop` och
`MeshLoopTriangle`; generella loopar i andra UI-kontexter lämnas orörda.
Deltafilen är lokalt granskad och ännu inte importerad.

Den 7 november importerades samlingsfilen för batch 748–760 i Blender
Translate. Weblate behandlade 52 poster: 51 uppdaterades, 1 hoppades över och
0 saknades. Importen är därmed verifierad. Filen
`blender-ui-sv-reviewed-20261107-pending-batches-748-760.po` bevaras som
spårbart underlag och ska inte importeras på nytt.

Batch 761 granskar 18 avgränsade Annotation-/Grease Pencil- och nodposter.
Den skiljer det ritade resultatet *streck* från en användarhandling med
pensel, normaliserar trådrammodifierarens hjälptext och använder termbasens
*nodindata*/*nodutdata* för nodernas tekniska dataflöde. Deltafilen har
passerat `msgfmt` och `l10n-lint`; `svlang` flaggar endast de avsiktliga
projektspecifika sammansättningarna och en falsk V2-varning i en nominal
etikett. Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-748-761.po` är ett
historiskt samlat arkiv med 70 unika ändringar. Eftersom batch 748–760 redan
är importerade ska den inte användas för nästa import. Nästa importfil är
i stället enbart batch 761 med 18 nya poster.

Batch 762 normaliserar fem ytterligare, tydligt avgränsade UI-texter. Den
använder *skärmrymd* för penselns skärmrelaterade koordinater och
*indata*/*nodutdata* för tekniska nodvärden. Deltafilen har passerat
`msgfmt` och `l10n-lint`; `svlang` rapporterar endast facktermer och en falsk
V2-varning i en etikett. Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-762.po` är den aktuella
manuella importfilen. Den innehåller 23 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 763 normaliserar fem operatörs- och feltexter för nodernas
gruppindata, Cryptomatte-indata och zonindata. De följer den fastställda
distinktionen *nodindata* snarare än den generella formen *inmatning*.
Deltafilen har passerat `msgfmt` och `l10n-lint`; `svlang` rapporterar endast
projektspecifika sammansättningar och en falsk V2-varning i en etikett. Den
är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-763.po` är den aktuella
manuella importfilen. Den innehåller 28 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 764 normaliserar tre parnings- och valideringstexter för zon- och
grupputdatanoder. Den använder konsekvent *indatanod*/*utdatanod*, i linje
med den dokumenterade Group Input/Output-terminologin. Deltafilen har
passerat `msgfmt` och `l10n-lint`; `svlang` flaggar en teknisk nominalfras
och projektspecifika sammansättningar, men ingen faktisk språkavvikelse.
Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-764.po` är den aktuella
manuella importfilen. Den innehåller 31 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 765 rättar två bildkällsetiketter för kompositörens Viewer-nod.
Den ersätter den personbetecknande formen *visare* med termbasens
*visningsnod*. Deltafilen har passerat `msgfmt`, `l10n-lint` och `svlang`.
Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-765.po` är den aktuella
manuella importfilen. Den innehåller 33 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 766 rättar fem popup- och popovertexter och Asset Shelfs
redigerarlägesbeskrivning. Den ersätter *poppuppfönster* med *popupfönster*
och den felaktiga arbetsytekontexten med Blenders tekniska *redigerarläge*.
Deltafilen har passerat `msgfmt` och `l10n-lint`; `svlang` ger endast en
falsk V2-varning i en infinitivfras. Den är lokalt klar men ännu inte
importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-766.po` är den aktuella
manuella importfilen. Den innehåller 38 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 767 granskar fyra Asset Browser-texter för nätanslutna resurser. Den
använder den idiomatiska formen *på nätet* och skiljer
*Grundresurser på nätet* från det lokala resursbiblioteket Grundresurser.
Deltafilen har passerat `msgfmt`, `l10n-lint` och `svlang` utan anmärkning.
Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-767.po` är den aktuella
manuella importfilen. Den innehåller 42 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 768 granskar elva RNA- och feltexter för redigerarområden, arbetsytor
och visningslager. Den rättar den äldre, bokstavliga formen *utrymme* till
*område* för Blenders `Space*`-typer, normaliserar *arbetsyta* och använder
termbasens *visningslager*. Deltafilen har passerat `msgfmt` och `l10n-lint`;
`svlang` rapporterar bara en teknisk nominalfras. Den är lokalt klar men ännu
inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-768.po` är den aktuella
manuella importfilen. Den innehåller 53 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 769 normaliserar tolv UI- och feltexter för Blenders Viewer-noder. Den
ersätter den personbetecknande formen *visare* med termbasens
*visningsnod*/*visningsnoder* i kompositions-, textur- och geometrinodernas
kontext. Deltafilen har passerat `msgfmt`, `l10n-lint` och `svlang`; dess
enda ovanliga ord är avsiktliga Blenderfacktermer. Den är lokalt klar men ännu
inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-769.po` är den aktuella
manuella importfilen. Den innehåller 65 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 770 rättar den tekniska datastrukturen `ViewerPath` till
*visningssökväg*. Den följer samma avgränsning som Viewer-noderna och lämnar
VR-visaren orörd. Deltafilen har passerat `msgfmt`, `l10n-lint` och `svlang`
utan anmärkning. Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-770.po` är den aktuella
manuella importfilen. Den innehåller 66 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 771 granskar de återstående RNA-etiketterna för Blenders interna
`Space…`-typer: klippredigeraren, filbläddraren, Outliner, inställningarna,
projektet, egenskaper, kalkylbladet och 3D-vyn. I den kontexten är *område*
och *områdesdata* korrekt, medan *utrymme* och *rumsdata* är missvisande.
Batchen har passerat `msgfmt` och `l10n-lint`; `svlang` känner inte igen
Blenders sammansättningar och produktnamn men visar ingen verklig språkavvikelse.
Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-771.po` är den aktuella
manuella importfilen. Den innehåller 83 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 772 rättar fyra beskrivningar för mask-, bild-, text- och 3D-vydata.
I löpande hjälptext används den etablerade termen *redigerarläge* för den
interna `Space…`-kontexten. Batchen har passerat `msgfmt`, `l10n-lint` och
`svlang` utan anmärkning. Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-772.po` är den aktuella
manuella importfilen. Den innehåller 87 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 773 normaliserar fyra ytterligare editor- och nodtermer: en
tangentmappnings redigerartyp, uttagets indatavärde, nodredigerarens
trädsökväg och rensning av områdesdata. Batchen har passerat `msgfmt`,
`l10n-lint` och `svlang`; den enda ovanliga termen är den avsiktliga
Blender-sammansättningen *nodredigerarens*. Den är lokalt klar men ännu inte
importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-773.po` är den aktuella
manuella importfilen. Den innehåller 91 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 774 normaliserar fem Node API- och uttagstexter till *indata* och
*utdata*: samlingar, uttagsvärden, olänkade uttag, interna länkar och
sorterade fleringångar. Batchen har passerat `msgfmt`, `l10n-lint` och
`svlang`; de enda ovanliga orden är avsiktliga Blender-sammansättningar.
Den är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261107-pending-batches-761-774.po` är den aktuella
manuella importfilen. Den innehåller 96 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 775 granskar två geometri- och skuggarnodtexter. *Input* avser här
nodindata och översätts därför som *indatageometri* respektive *den andra
indatan*. `msgfmt` och `l10n-lint` passerar. `svlang` flaggar bara den
inledande imperativformen som en felaktig V2-varning; Hunspell saknar den
förväntade Blender-sammansättningen *indatageometri*. Batchen är lokalt klar
men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-775.po` är den aktuella
manuella importfilen. Den innehåller 98 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 776 granskar elva operatörs- och typtexter för noder, zoner och uttag.
Den normaliserar *indatanod*, *utdatanod*, *indatalänk* och
*indata-/utdatauttag*. `msgfmt` och `l10n-lint` passerar. `svlang` ger enbart
falska V2-varningar för etiketter och imperativ; Hunspell saknar de avsedda
Blender-sammansättningarna. Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-776.po` är den aktuella
manuella importfilen. Den innehåller 109 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 777 granskar nio validerings- och feltexter för nodgruppers gränssnitt.
Den använder konsekvent *geometriutdata*, *utdatauttag*, *färgindata* och
*indata-/utdatariktning*. `msgfmt` och `l10n-lint` passerar. `svlang` och
Hunspell rapporterar endast avsiktliga, tekniska Blender-sammansättningar
och två falska V2-varningar i korrekta satsdelar. Batchen är lokalt klar men
ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-777.po` är den aktuella
manuella importfilen. Den innehåller 118 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 778 granskar sju filtertexter för Asset Browser. Den följer
terminologin för *resurser*, *på nätet* och *lokalt* i stället för den
inkonsekventa blandningen av *tillgångar* och engelska *online/offline*.
`msgfmt` och `l10n-lint` passerar. `svlang` har bara falska V2-varningar för
korrekta uppmaningar, och Hunspell har inga svenska ordvarningar. Batchen är
lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-778.po` är den aktuella
manuella importfilen. Den innehåller 125 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 779 granskar elva Asset Browser- och Asset Shelf-texter för bibliotek,
kataloger, filter och förhandsvisningar. Den använder konsekvent *resurs*,
*resurstyp* och *resursbibliotek* i den synliga användargränssnittskontexten,
men rör inte API-begrepp som *asset representation*, vilka fortsatt är
*tillgångsrepresentation*. Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-779.po` är den aktuella
manuella importfilen. Den innehåller 136 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 780 granskar tre resurshylletexter för miniatyrbilder och dragning.
*Asset* används här om de synliga resurserna i hyllan och blir därför
*resurs*; den tidigare formuleringen blandade annars ihop *resurshylla* med
*tillgångar*. Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-780.po` är den aktuella
manuella importfilen. Den innehåller 139 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 781 granskar åtta Asset Browser-texter för importmetod och namnbyte.
Den rättar bland annat den felaktiga översättningen *nätet* för Blenders
*mesh* i en importbeskrivning: här avses ett meshdatablock, inte internet.
I dessa UI-handlingar används konsekvent *resurs* och *resursdatablock*.
Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-781.po` är den aktuella
manuella importfilen. Den innehåller 147 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 782 granskar tre tekniska nodtexter: en zonindatanod, en indatasträng
och en längdindata. *Input* är därmed konsekvent *indata* i den faktiska
nod- och uttagskontexten. Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-782.po` är den aktuella
manuella importfilen. Den innehåller 149 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 783 granskar tolv kompositörtexter för färghantering, UV-kartläggning,
brusreducering, cache och nodgrupper. Den etablerade uppdelningen behålls:
*kompositör* för redigeraren och dess körning, *komposition* för processen,
*kompositionspass* för passet och *visningstransformering* i färghanteringen.
Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-783.po` är den aktuella
manuella importfilen. Den innehåller 161 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 784 granskar fem valideringsfel för nodträd. Sammansättningarna följer
terminologin: *kompositionsnodträd*, *geometrinodträd* och *shadernodträd*.
Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-784.po` är den aktuella
manuella importfilen. Den innehåller 166 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 785 granskar fem UI- och diagnostiktexter för kompositionsnodgrupper.
*Compositing* är processen och blir därför *komposition* i sammansättningen
*kompositionsnodgrupp*; den synliga redigeraren heter däremot fortsatt
*kompositör*. Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-785.po` är den aktuella
manuella importfilen. Den innehåller 171 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 786 granskar två handlingar för visningsnoder. De avser den synliga
redigeraren *Kompositör* och använder därför den bestämda löptextformen
*kompositören*. Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-786.po` är den aktuella
manuella importfilen. Den innehåller 173 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 787 granskar tolv Kompositör- och sekvensredigerartexter för effekter,
modifierare, noder och renderpass. Åtgärderna utför bildkomposition och får
därför *kompositionseffekt*, *kompositionsmodifierare* och
*kompositionsnod*, medan det synliga verktyget fortsatt heter *kompositör*.
Batchen är lokalt klar men ännu inte importerad.

`blender-ui-sv-reviewed-20261108-pending-batches-761-787.po` är den aktuella
manuella importfilen. Den innehåller 185 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 788 granskar tre felmeddelanden för inmatning och tangentbord. Den
ersätter de satsfragment som saknade subjekt med idiomatiska systemmeddelanden
(*Ett tal förväntades* och *En talmatris förväntades*) samt normaliserar
*Unsupported key: Unknown* till samma struktur som den närliggande
tangentbordsdiagnostiken: *Tangent som inte stöds: okänd*. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-788.po` är den aktuella
manuella importfilen. Den innehåller 188 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 789 granskar tretton diagnostiktexter från skärmredigeraren. Den
ersätter återkommande satsfragment som *Förväntade …* med fullständiga,
idiomatiska felmeddelanden och använder etablerade Blender-namn som
*Dopeblad*, *grafredigerare* och *NLA-redigerare*. Tekniska `editmesh`- och
API-poster ingår inte i batchen. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-789.po` är den aktuella
manuella importfilen. Den innehåller 201 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 790 granskar sex felmeddelanden från operatorer och redigerarlägen.
De fullständiga svenska diagnostiktexterna skiljer mellan ett *meshobjekt*,
ett *redigeringsmesh* och ett *textobjekt i redigeringsläge*. Platshållaren
`{!r}` är bevarad i zip-filsmeddelandet. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-790.po` är den aktuella
manuella importfilen. Den innehåller 207 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 791 normaliserar tre återstående förekomster av *Dope Sheet* i
spårnings- och transformationskontext. Det synliga Blender-namnet är
*Dopeblad*, vilket ger *Dopebladssortering*, *Dopebladskanaler* och
*Dopebladsredigeraren*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-791.po` är den aktuella
manuella importfilen. Den innehåller 210 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 792 granskar tre synliga Dope Sheet-etiketter i kortkommandon och
grafredigeraren. De använder samma etablerade UI-namn *Dopeblad* som övriga
granskade redigerartexter. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-792.po` är den aktuella
manuella importfilen. Den innehåller 213 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 793 tillämpar den projektspecifika termen *klippredigerare* i två
återstående Movie Clip Editor-texter: en spårningsfärg och
temainställningarna. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-793.po` är den aktuella
manuella importfilen. Den innehåller 215 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 794 granskar 23 UI- och feltexter där Blenders datatyp eller objektklass
`mesh` tidigare översatts som *nätobjekt*. Den projektspecifika termen är
*mesh* och sammansättningen *meshobjekt*. Åtgärden omfattar Boolean,
konvertering, skulptering, UV-projektion och objektverktyg, men lämnar den
separata betydelsen *mesh items* utanför. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-794.po` är den aktuella
manuella importfilen. Den innehåller 238 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 795 granskar nio RNA-, operator- och feltexter för Blenders
meshdatablock. Den samordnar den tidigare inkonsekventa formen *nätdata* till
den projektspecifika termen *meshdata* i kopiering, överföring, sammanslagning
och utvärderade objektdata. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-795.po` är den aktuella
manuella importfilen. Den innehåller 247 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 796 rättar Outlinerns synliga etikett för *System Overrides* till
*Systemåsidosättningar*. Den ersätter den inkonsekventa formen
*Systemöverskrivningar* och följer samma terminologi som det närliggande
systemåsidosättningsfiltret. Batchen är lokalt klar men ännu inte importerad
i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-796.po` är den aktuella
manuella importfilen. Den innehåller 248 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 797 granskar tolv modifierar- och volymtexter där *mesh* syftar på
Blenders datatyp, inte på ett rutnät. Den använder därför *meshen*,
*basmeshen* och *målmeshen*, medan verkliga `grid`-poster fortfarande är
*rutnät*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-797.po` är den aktuella
manuella importfilen. Den innehåller 260 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 798 granskar elva redigerings- och skulpteringstexter där *mesh* är
Blenders datatyp. De använder därför *meshen* och *ytmeshen*, medan
rutnätsbegrepp inte ändras. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-798.po` är den aktuella
manuella importfilen. Den innehåller 271 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 799 normaliserar 32 texter om Blenders datatyper *Mesh object* och
*Mesh data*. De använder konsekvent *meshobjekt* och *meshdata*. I kommandon
som avser ett enskilt element används *meshelement*, inte *meshobjekt*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-799.po` är den aktuella
manuella importfilen. Den innehåller 303 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 800 granskar tolv modifierar- och geometrioperationer där *base*,
*source*, *target*, *input* och *surface mesh* alla är Blenders datatyp.
Den använder därför bland annat *basmeshen*, *källmesh*, *målmeshen*,
*indatameshen* och *ytmeshen*. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-800.po` är den aktuella
manuella importfilen. Den innehåller 315 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 801 normaliserar fyra återstående, explicita *Mesh data*-referenser i
en shadernod, en inställning och två felmeddelanden till *meshdata* och
*meshdatablock*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-801.po` är den aktuella
manuella importfilen. Den innehåller 319 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 802 granskar tretton dataöverförings- och geometri-nodtexter. När två
datatyper avses används *käll- och målmesh*; när en bestämd datatyp avses
används exempelvis *källmeshen* och *målmeshen*. Batchen är lokalt klar men
ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-802.po` är den aktuella
manuella importfilen. Den innehåller 332 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 803 granskar arton funktioner, exporter och felmeddelanden som
uttryckligen avser Blender-typen *mesh object*. De normaliseras till
*meshobjekt*; en enskild *target mesh* blir *målmesh*. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-803.po` är den aktuella
manuella importfilen. Den innehåller 350 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 804 granskar tio kurv-, hår- och geometri-nodtexter som uttryckligen
avser en *surface mesh* eller *base mesh*. De använder formerna *ytmesh*,
*ytmeshen*, *basmesh*, *basmeshen* och *indataytmeshen*. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-804.po` är den aktuella
manuella importfilen. Den innehåller 360 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 805 granskar sex Multires- och underindelningsoperationer där *base
mesh* och *displaced mesh* är konkreta Blender-datatyper. Den använder
*basmesh*, *basmeshen*, *basmeshpositionerna* och *den förskjutna meshen*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-805.po` är den aktuella
manuella importfilen. Den innehåller 366 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 806 granskar sju synliga typnamn och geometri-nodetiketter. Blenders
egen datatyp heter *Mesh* och behålls därför som *Mesh*, medan en
objektbaserad validering använder *meshobjekt*. Batchen är lokalt klar men
ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-761-806.po` är den aktuella
manuella importfilen. Den innehåller 373 nya, lokalt granskade poster och
utesluter de redan verifierat importerade batcherna 748–760.

Batch 807 granskar femton synliga nod-, modifierar- och exportetiketter som
börjar med Blenders datatyp *Mesh*. Den behåller *Mesh* som projektspecifik
term men översätter resten, till exempel *Mesh till volym*, *Meshfasning* och
*Meshinställningar*.

Importresultat 2026-11-08: den samlade filen
`blender-ui-sv-reviewed-20261108-pending-batches-761-807.po` importerades i
Blender Translate. Weblate bearbetade 351 poster, uppdaterade 312, hoppade
över 39 och saknade 0. Batcherna 761–807 är därmed verifierat importerade;
de överhoppade posterna var redan aktuella.

Batch 808 granskar elva egenskapsdomäner, verktyg och inställningar som avser
Blenders datatyp *Mesh*. Den använder bland annat *Meshkant*, *Meshnormaler*,
*Meshfilter* och *Meshstatistik*. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-808-mesh-properties.po` är den
aktuella manuella deltafilen för nästa import. Den innehåller endast de elva
nya, lokalt granskade posterna.

Batch 809 granskar nio Mesh-diagnoser om UV-data, färgattribut, ytor och
storlek. Den använder de konsekventa böjningarna *meshen*, *meshens* och
*meshytor*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-809-mesh-diagnostics.po` är en
separat, efterföljande deltafil med endast dessa nio nya poster.

Batch 810 granskar arton socketbeskrivningar för geometri-noder. När *Mesh*
är nodindata behålls datatypsnamnet, med svenska beskrivningar som *Mesh vars
kanter ska delas* och *Mesh som ska trianguleras*. Batchen är lokalt klar men
ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-810-mesh-node-sockets.po` är en
separat, efterföljande deltafil med endast dessa arton nya poster.

`blender-ui-sv-reviewed-20261108-pending-batches-808-810.po` är den aktuella
samlade manuella deltafilen. Den innehåller 38 nya, lokalt granskade poster
och ligger väl under Blender Translates uppladdningsgräns.

`REVIEW-COVERAGE-20261108.md` är den reproducerbara källan för den aktuella
täckningsmätningen. Den mäter lokal radgranskning, inte Weblates status eller
ett importresultat.

Hela den lokala UI-katalogen har även körts genom `l10n-lint`. De kvarvarande
träffarna har bedömts rad för rad: de gäller format- och färgprofilnamn,
avsiktligt oförändrade identifierare, svensk decimalnotation eller medvetna
tekniska formuleringar. Inga ytterligare säkra massrättningar härleddes ur
verktygsvarningarna.

Batch 726 granskar 22 UI- och API-texter för Blenders formella
animationsdatatyp *Action*. Datatypnamnet behålls i *Action-slot*,
*Action-kanal*, *Action-längd* och *Action-nyckelbildruta*, medan vanliga
svenska åtgärder utanför datatypskontexten lämnas oförändrade. Batchen är
lokalt kontrollerad och ännu inte importerad.

Batch 811 granskar åtta etiketter och hjälprader för skulpteringsdetalj,
meshredigeringsläge och meshfilter. Den normaliserar den gamla termen *nät*
till Blenders etablerade datatypsnamn *Mesh*: *Meshdetaljer*,
*Meshredigeringsläge*, *Meshfilter* och *Meshplan*. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-811-mesh-editing.po` är en separat
manuell deltafil med endast dessa åtta nya, lokalt granskade poster.

Batch 812 granskar tretton reservmappningar för 3D-vyns meshverktyg och
inställningen för automatisk maskning. Den ersätter den äldre interna termen
*nät* med *mesh* i verktygskontext, exempelvis *redigera mesh* och
*skulptera, meshfilter*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-812-mesh-tool-fallbacks.po` är en
separat manuell deltafil med endast dessa tretton nya, lokalt granskade
poster.

Batch 813 granskar sju meddelanden för Dopebladet och nodredigerarna. Den
använder de fastställda projektsammansättningarna *Dopebladsredigeraren*,
*kompositionsnodträd*, *shadernodträd* och *geometrinodträd*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-813-node-editor-terms.po` är en
separat manuell deltafil med endast dessa sju nya, lokalt granskade poster.

Batch 814 granskar tolv etiketter för komposition och kompositören. Den
normaliserar bland annat *kompositionsnoder*, *Kompositörprecision*,
*Kompositörsremsa* och *Cache för kompositörens bildrutor*. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-814-compositor-terms.po` är en separat
manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

Batch 815 granskar elva kontexttexter för färghantering, komposition och
kompositören. Den använder *visningstransformering*, *komposition*,
*kompositionspass* och rätt böjning av *kompositör*. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-815-compositor-context.po` är en
separat manuell deltafil med endast dessa elva nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-815.po` samlar batch
811–815 för en manuell import. Den innehåller 51 poster och ligger långt under
Blender Translates gräns på 1 000 poster per uppladdning. Den är lokalt
validerad men inte importerad.

Batch 816 granskar tre entydiga RNA-datatyper för animationsdatablocket
*Action*: *Action-grupp*, *Action-lager* och *Action-remsa*. Mer generella
Action-etiketter och Action-slotar lämnas oförändrade, eftersom de använder
den separata åtgärdsterminologin i sina egna UI-kontexter. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-816-action-datatypes.po` är en separat
manuell deltafil med endast dessa tre nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-816.po` är den aktuella
samlade manuella deltafilen för batch 811–816. Den innehåller 54 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 817 granskar sex kvarvarande Mesh-texter som inte täcks av tidigare
arkiverade batcher. Den använder *meshen*, *meshelement*, *meshdeformering*
och *meshobjekt* konsekvent i skulpterings- och modifierarkontext. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-817-mesh-deformation.po` är en separat
manuell deltafil med endast dessa sex nya, lokalt granskade poster.

Batch 818 granskar den osammanhangsmarkerade etiketten *Compositor*, som delas
av sekvensredigeraren, paneler och nodredigeraren. Den normaliserar den till
det fastställda synliga Blender-namnet *Kompositör*. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-818-compositor-label.po` är en separat
manuell deltafil med denna enda, lokalt granskade post.

`blender-ui-sv-reviewed-20261108-pending-batches-811-818.po` är den aktuella
samlade manuella deltafilen för batch 811–818. Den innehåller 61 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 819 granskar fem indataetiketter för geometrinoder. Den normaliserar
*geometritröskelvärde* och gör tre beskrivningar av geometri vars element
bearbetas idiomatiska på svenska. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-819-geometry-inputs.po` är en separat
manuell deltafil med endast dessa fem nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-819.po` är den aktuella
samlade manuella deltafilen för batch 811–819. Den innehåller 66 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 820 granskar en maskredigeringsåtgärd som refererar till Dope Sheet.
Den använder den etablerade bestämda formen *dopebladet* och förtydligar att
det är bildrutorna som har markerats. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-820-dope-sheet-context.po` är en
separat manuell deltafil med denna enda, lokalt granskade post.

Batch 821 granskar tolv grundläggande Mesh-meddelanden för skulptering,
formnycklar, UV-avbildning och primitivverktyg. Den ersätter den tvetydiga
översättningen *nät* med Blenders datatyp *mesh* och använder konsekvent
formerna *meshen*, *meshobjekt* och *en mesh i redigeringsläge*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-821-mesh-core-context.po` är en
separat manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

Batch 822 granskar tolv verktygstexter som skapar Mesh-primitiver. Den
använder *mesh* som Blenders datatyp även för primitivernas former, till
exempel *kubmesh*, *cirkelmesh*, *torusmesh* och *Suzanne-mesh*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-822-mesh-primitives.po` är en separat
manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-822.po` är den aktuella
samlade manuella deltafilen för batch 811–822. Den innehåller 91 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 823 granskar tretton Mesh-texter för modifierare, export och
felmeddelanden. Den normaliserar *meshens*, *meshen*, *meshdata* och
*meshobjekt* samt förtydligar bur- och ytdeformeringskontexten. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-823-mesh-operations.po` är en separat
manuell deltafil med endast dessa tretton nya, lokalt granskade poster.

Batch 824 granskar nio texter för meshkonvertering, UV och export. Den
normaliserar bland annat *en mesh*, *meshen*, *meshplan* och felmeddelanden
för utvärderad mesh. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-824-mesh-conversion.po` är en separat
manuell deltafil med endast dessa nio nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-824.po` är den aktuella
samlade manuella deltafilen för batch 811–824. Den innehåller 113 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 825 granskar tolv Mesh-texter för skulptering, hårsystem, Dynamic Paint
och synlighetsverktyg. Den normaliserar *meshkanter*, *meshdetaljer*,
*emittermeshen*, *dukmeshen* och bestämda former av *mesh*. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-825-mesh-sculpting.po` är en separat
manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

Batch 826 granskar tio Mesh-texter för Alembic-, USD- och glTF-export samt
två tekniska diagnoser. Den använder *mesh* som datatyp, *meshobjekt* för
exporterade objekt och *meshprov* för diagnosens provdata. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-826-mesh-export.po` är en separat
manuell deltafil med endast dessa tio nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-826.po` är den tidigare
samlade manuella deltafilen för batch 811–826. Den innehåller 135 poster och
passerar lokal syntax- och lintkontroll.

Batch 827 granskar tolv Mesh-texter för geometri, QuadriFlow och skulptering
med dynamisk topologi. Den normaliserar *mesh*, *meshen* och *meshdetaljer* i
genererings-, remeshing- och detaljinställningskontext. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-827-mesh-topology.po` är en separat
manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-827.po` är den tidigare
samlade manuella deltafilen för batch 811–827. Den innehåller 147 poster och
passerar lokal syntax- och lintkontroll.

Batch 828 granskar tolv Mesh-texter för geometri, normala, remeshing och
skulpteringsverktyg. Den använder konsekvent *mesh* för Blenders datatyp,
bland annat i *meshattribut*, *meshnormaler*, *meshytor* och
*meshhörnpunkter*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-828-mesh-elements.po` är en separat
manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-828.po` är den tidigare
samlade manuella deltafilen för batch 811–828. Den innehåller 159 poster och
passerar lokal syntax- och lintkontroll.

Batch 829 granskar tolv Mesh-texter för vätskeemission, geometri, skulptering
och felhantering. Den normaliserar *meshytan*, *meshens topologi*,
*meshmaterial* och *meshen* i både användartexter och tekniska diagnoser.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-829-mesh-context.po` är en separat
manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-829.po` är den tidigare
samlade manuella deltafilen för batch 811–829. Den innehåller 171 poster och
passerar lokal syntax- och lintkontroll.

Batch 830 granskar elva Mesh-texter för UV, export, ommeshning och
objektkonvertering. Den använder konsekvent *meshattribut*, *meshplan*,
*meshtyp* och *meshens* i inställnings- och exportkontext. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-830-mesh-data.po` är en separat
manuell deltafil med endast dessa elva nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-830.po` är den tidigare
samlade manuella deltafilen för batch 811–830. Den innehåller 182 poster och
passerar lokal syntax- och lintkontroll.

Batch 831 granskar tolv Mesh-texter för import, USD-export, underindelning och
skulptering. Den normaliserar *mesh*, *meshen*, *meshdetaljer* och
*meshens färgattribut* i både filformat- och redigeringskontext. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-831-mesh-import-export.po` är en
separat manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

Batch 832 granskar tolv Mesh-texter för QuadriFlow, normaler, USD-attribut,
skulptering och Shrinkwrap. Den normaliserar *meshelement*, *meshnormaler*,
*meshens topologi* och *meshattribut*. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-832-mesh-normal-topology.po` är en
separat manuell deltafil med endast dessa tolv nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-832.po` är den tidigare
samlade manuella deltafilen för batch 811–832. Den innehåller 206 poster och
passerar lokal syntax- och lintkontroll.

Batch 833 granskar elva Mesh-texter för dataöverföring, UV, Cycles och
underindelning. Den normaliserar *mesh* i plural, *målmesh*, *den aktiva
meshen* och *resultatmeshen* utan att ändra Blenders tekniska innebörd.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-833-mesh-transfer.po` är en separat
manuell deltafil med endast dessa elva nya, lokalt granskade poster.

Batch 834 granskar två återstående Mesh-texter. Den använder *meshen* för
Blenders typnamn i UV-feltexten och *ommeshningsverktyget* för den process som
inte kan arbeta med länkade eller åsidosatta data. Batchen är lokalt klar men
ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-834-remeshing.po` är en separat manuell
deltafil med endast dessa två nya, lokalt granskade poster.

Batch 835 granskar två Voronoi-texter i de äldre procedurtexturerna. Den
ersätter den ljudbetonade och upprepade formuleringen *spräckande Voronoi* med
det geometriskt korrekta *Voronoi-sprickmönster*. Batchen är lokalt klar men
ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-835-voronoi-crackle.po` är en separat
manuell deltafil med endast dessa två nya, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-834.po` är den tidigare
samlade manuella deltafilen för batch 811–834. Den innehåller 219 poster och
passerar lokal syntax- och lintkontroll.

`blender-ui-sv-reviewed-20261108-pending-batches-811-835.po` är den aktuella
samlade manuella deltafilen för batch 811–835. Den innehåller 221 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 837 granskar 32 NLA-, export- och animeringsetiketter där *Action* är
Blenders formella animationsdatablock. Den använder konsekvent *Action*,
*Actionen* och *Actioner* samt sammansättningar som *Action-klipp*,
*Action-filter* och *armatur-Actioner*. Vanliga betydelser av *action* är
utanför batchens kontext. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-837-action-nla-export-ui.po` är en
separat manuell deltafil med endast dessa 32, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-837.po` är den aktuella
samlade manuella deltafilen för batch 811–837. Den innehåller 253 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 838 rättar tre fel i begränsningskontext. Den skiljer Blenders
*constraint* från ett logiskt villkor och ändrar de felaktiga verbformerna
*tillämpade* och *kopierade begränsning* till adjektiven *tillämpad* och
*kopierad begränsning*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-838-constraint-grammar.po` är en
separat manuell deltafil med endast dessa tre, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-838.po` är den aktuella
samlade manuella deltafilen för batch 811–838. Den innehåller 256 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 839 normaliserar 44 etiketter för 3D-vyns redigeringsverktyg. Den
ersätter den generiska geometribetydelsen *nät* med Blenders etablerade
datatypsnamn *mesh* i hela den sammanhållna verktygsgruppen. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-839-mesh-edit-tool-labels.po` är en
separat manuell deltafil med endast dessa 44, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-839.po` är den aktuella
samlade manuella deltafilen för batch 811–839. Den innehåller 289 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 840 normaliserar 16 centrala Mesh-etiketter för objekt, lägen,
konvertering, filter och export. Den använder *Mesh*, *meshcache*,
*meshfilter*, *meshplan* och *meshkomprimering* i stället för den generiska
geometriöversättningen *nät*. Batchen är lokalt klar men ännu inte importerad
i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-840-mesh-core-ui.po` är en separat
manuell deltafil med endast dessa 16, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-840.po` är den aktuella
samlade manuella deltafilen för batch 811–840. Den innehåller 304 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 841 normaliserar 15 kontextbundna meddelanden för meshkonvertering,
filter, skulptering, export och geometri. Den använder Blenders datatyp
*mesh* och svensk böjning som *meshen* konsekvent, i stället för den generiska
geometribetydelsen *nät*. Även beskrivningen av en konvex omslutning är
justerad så att den beskriver tätt anpassad geometri i stället för
förpackningsmaterial. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-841-mesh-context-messages.po` är en
separat manuell deltafil med endast dessa 15, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-841.po` är den aktuella
samlade manuella deltafilen för batch 811–841. Den innehåller 319 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 842 normaliserar 20 kontextbundna inställningar och modifierarbeskrivningar
för Blenders datatyp *mesh*: normaler, topologi, målobjekt, partikelinstanser,
utjämning och booleska operationer. Den ersätter den generiska
geometribetydelsen *nät* med *mesh*, *meshen*, *meshyta*, *meshobjekt* och
*meshtopologi*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-842-mesh-modifier-ui.po` är en separat
manuell deltafil med endast dessa 20, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-842.po` är den aktuella
samlade manuella deltafilen för batch 811–842. Den innehåller 336 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 843 normaliserar 21 modifierarbeskrivningar för datatypen *mesh*,
bland annat meshcache, dataöverföring, spegling, avfasning, deformation och
flernivåmesh. Den använder svenska, kontextbundna sammansättningar som
*meshcache*, *meshö*, *meshobjekt*, *meshvecksinformation* och *basmesh*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-843-mesh-modifier-details.po` är en
separat manuell deltafil med endast dessa 21, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-843.po` är den aktuella
samlade manuella deltafilen för batch 811–843. Den innehåller 354 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 844 normaliserar 16 kontextbundna geometri-noder för generering,
konvertering, interpolation och analys av Blenders *mesh*. Den använder
bland annat *meshkanter*, *meshattribut*, *meshelement* och *meshens ytor*
i stället för den generiska geometribetydelsen *nät*. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-844-mesh-geometry-nodes.po` är en
separat manuell deltafil med endast dessa 16, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-844.po` är den aktuella
samlade manuella deltafilen för batch 811–844. Den innehåller 359 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 845 normaliserar 16 beskrivningar för topologi, ommeshning,
underindelning och geometri-noder. Den använder etablerade Blender-termer som
*basmesh*, *målmesh*, *meshkomponent*, *meshhörnpunkt* och *ytmesh* i stället
för den generiska geometribetydelsen *nät*. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-845-mesh-topology-and-remesh.po` är en
separat manuell deltafil med endast dessa 16, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-845.po` är den aktuella
samlade manuella deltafilen för batch 811–845. Den innehåller 372 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 846 normaliserar 18 import- och exportinställningar för FBX, glTF,
Draco, Meshopt och meshplan. Den använder *mesh*, *meshobjekt*, *meshplan*,
*meshkomprimering* och *meshens primitivgrupper* i stället för den generiska
geometribetydelsen *nät*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-846-mesh-import-export.po` är en
separat manuell deltafil med endast dessa 18, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-846.po` är den aktuella
samlade manuella deltafilen för batch 811–846. Den innehåller 380 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 847 normaliserar 19 strängar för meshredigering: borttagning, loopar,
normaler, urval, utjämning och skapande av primitiv. Den använder *meshdata*,
*meshloop*, *meshelement*, *cirkelmesh*, *kubmesh* och *Suzanne-mesh* i stället
för den generiska geometribetydelsen *nät*. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-847-mesh-edit-tools.po` är en separat
manuell deltafil med endast dessa 19, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-847.po` är den aktuella
samlade manuella deltafilen för batch 811–847. Den innehåller 388 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 848 normaliserar 17 objekt- och dataöverföringssträngar för mesh,
kurvor, Multires och QuadriFlow. Den använder bland annat *meshobjekt*,
*basmesh*, *målmesh* och *modifieraren för meshdeformering* i stället för den
generiska geometribetydelsen *nät*. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-848-mesh-object-data.po` är en separat
manuell deltafil med endast dessa 17, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-848.po` är den aktuella
samlade manuella deltafilen för batch 811–848. Den innehåller 397 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 849 normaliserar 18 skulpteringssträngar för detaljer, masker,
ytuppsättningar och meshfilter. Den använder konsekvent *mesh*, *meshen*,
*meshens topologi* och *meshobjekt* i stället för den generiska
geometribetydelsen *nät*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-849-mesh-sculpt-actions.po` är en
separat manuell deltafil med endast dessa 18, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-849.po` är den aktuella
samlade manuella deltafilen för batch 811–849. Den innehåller 409 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 850 normaliserar 10 UV- och projekteringssträngar. Den använder former
som *meshaxel*, *meshen* och *packad mesh* i stället för den generiska
geometribetydelsen *nät*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-850-mesh-uv-tools.po` är en separat
manuell deltafil med endast dessa 10, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-850.po` är den aktuella
samlade manuella deltafilen för batch 811–850. Den innehåller 417 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 851 normaliserar 18 QuadriFlow-, symmetri- och visningssträngar för
Blender-mesh. Den använder bland annat *meshgräns*, *meshkanter*, *meshen*
och *meshens topologi* i stället för den generiska geometribetydelsen *nät*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-851-mesh-remesh-tools.po` är en separat
manuell deltafil med endast dessa 18, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-851.po` är den aktuella
samlade manuella deltafilen för batch 811–851. Den innehåller 423 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 852 normaliserar 12 strängar för voxelommeshning, emittermesh och
skulpteringsdetaljer. Den använder *sluten mesh*, *emittermesh*, *meshen* och
*meshdetalj* i stället för den generiska geometribetydelsen *nät*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-852-mesh-sculpt-detail.po` är en separat
manuell deltafil med endast dessa 12, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-852.po` är den aktuella
samlade manuella deltafilen för batch 811–852. Den innehåller 431 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 853 normaliserar åtta skulpteringssträngar för booleska trimverktyg,
maskextraktion och utjämning. Den använder *meshen* och *meshobjekt* i stället
för den generiska geometribetydelsen *nät*. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-853-mesh-sculpt-trim.po` är en separat
manuell deltafil med endast dessa åtta, lokalt granskade poster.

`blender-ui-sv-reviewed-20261108-pending-batches-811-853.po` är den aktuella
samlade manuella deltafilen för batch 811–853. Den innehåller 437 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 854 normaliserar 30 modifierar- och dataegenskaper för mesh, bland annat
Bevel, Build, Multiresolution, QuadriFlow och Mesh Deform. Den använder
*mesh*, *meshen*, *meshobjekt*, *meshcache*, *meshdeformering* och
*ommeshning* i stället för den generiska geometribetydelsen *nät*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-854-mesh-modifiers.po` är en separat
manuell deltafil med endast dessa 30, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-854.po` är den aktuella
samlade manuella deltafilen för batch 811–854. Den innehåller 446 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 855 normaliserar 21 animations- och nodträdstermer. Blenders formella
datatyp *Action* skrivs som *Action-grupp*, *Action-lager*, *Action-slot* och
*Action-remsa*, medan *Dope Sheet* blir *Dopeblad*. För nodträd används
*kompositionsnodträd*, *shadernodträd* och *geometrinodträd*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-855-animation-and-node-terminology.po`
är en separat manuell deltafil med endast dessa 21, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-855.po` är den aktuella
samlade manuella deltafilen för batch 811–855. Den innehåller 457 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 856 normaliserar 17 strängar för booleska operationer, modifierare,
Fluid, Line Art och dataöverföring. Den använder *mesh*, *meshen*, *meshobjekt*,
*källmesh*, *målmesh* och *manifold-meshar* där API:t avser Blenders datatyp,
inte den generiska geometribetydelsen *nät*. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-856-mesh-modifier-context.po` är en
separat manuell deltafil med endast dessa 17, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-856.po` är den aktuella
samlade manuella deltafilen för batch 811–856. Den innehåller 459 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 857 granskar fyra Shrinkwrap-beskrivningar. *Shrinkwrap* behålls som
Blenders funktionsnamn, medan verbfraserna beskriver att objektet anpassas
tätt över målet. Den felaktiga förpackningsmetaforen *krympfilm* ersätts med
en tekniskt korrekt Shrinkwrap-jämförelse. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-857-shrinkwrap-descriptions.po` är en
separat manuell deltafil med endast dessa fyra, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-857.po` är den aktuella
samlade manuella deltafilen för batch 811–857. Den innehåller 462 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 858 normaliserar 23 meshsträngar för maskning, ommeshning,
underindelning, deformering och volymkonvertering. Den använder bland annat
*meshen*, *basmesh*, *indatamesh*, *målmesh*, *meshdata*, *meshveck* och
*manifold-mesh* i den konkreta modifierarkontexten. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-858-mesh-modifier-geometry.po` är en
separat manuell deltafil med endast dessa 23, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-858.po` är den aktuella
samlade manuella deltafilen för batch 811–858. Den innehåller 464 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 859 normaliserar 20 strängar för geometri-noder som arbetar med mesh,
bland annat topologi, kanter, attribut, primitiv och kurvkonvertering. Den
använder *kubmesh*, *konmesh*, *cylindermesh*, *meshkomponent*, *meshkant*,
*meshattribut* och *meshelement*. Batchen ersätter tidigare lokala formuleringar
i samma poster men ändrar inte antalet poster i den samlade deltafilen.

`blender-ui-sv-reviewed-20261108-batch-859-geometry-node-mesh.po` är en
separat manuell deltafil med endast dessa 20, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-859.po` är den aktuella
samlade manuella deltafilen för batch 811–859. Den innehåller 464 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 860 normaliserar 15 meshsträngar för normaler, kanter, underindelning,
triangulering och redigeringsverktyg. Den använder bland annat *meshnormal*,
*meshkant*, *meshyta*, *meshdatablock*, *meshplan*, *torusmesh* och *ytmesh*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-860-mesh-normal-and-tools.po` är en
separat manuell deltafil med endast dessa 15, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-860.po` är den aktuella
samlade manuella deltafilen för batch 811–860. Den innehåller 472 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 861 normaliserar 20 FBX- och glTF-strängar för export, förenkling,
komprimering, primitivgrupper och bildplansimport. Format- och API-namn som
Draco, Meshopt, gltfpack och EXT_meshopt_compression bevaras, medan
Blender-typen skrivs *mesh*, *meshobjekt*, *meshplan*, *meshmaterial* och
*meshkomprimering*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-861-mesh-export.po` är en separat
manuell deltafil med endast dessa 20, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-861.po` är den aktuella
samlade manuella deltafilen för batch 811–861. Den innehåller 475 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 862 normaliserar åtta importsträngar för FBX, glTF, USD och STL. Den
använder *alfamesh*, *mesh*, *meshattribut*, *meshens färgattribut* och
*meshen*, men behåller filformat, USD Primvars och POINTS som tekniska namn.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-862-mesh-import.po` är en separat
manuell deltafil med endast dessa åtta, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-862.po` är den aktuella
samlade manuella deltafilen för batch 811–862. Den innehåller 479 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 863 normaliserar 27 grundläggande meshsträngar i modifierare,
vätskesimulering, datadelning och booleska operationer. Den skiljer konsekvent
Blenders datatyp *mesh* från ett allmänt nät och använder bland annat *meshen*,
*meshyta*, *meshcache*, *meshö*, *meshtopologi*, *meshobjekt* och
*manifold-mesh*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-863-mesh-core.po` är en separat
manuell deltafil med endast dessa 27, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-863.po` är den aktuella
samlade manuella deltafilen för batch 811–863. Den innehåller 479 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 864 normaliserar 40 meshsträngar i UV-projektion, USD-export,
retopologi, skulptering och API-felmeddelanden. Den använder bland annat
*mesh*, *meshen*, *meshtyp*, *meshö*, *meshelement*, *mesh-hörnpunkt*,
*meshgeometri*, *meshdetalj* och *manifold-mesh*. Batchen är lokalt klar men
ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-864-mesh-ui-and-api.po` är en separat
manuell deltafil med endast dessa 40, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-864.po` är den aktuella
samlade manuella deltafilen för batch 811–864. Den innehåller 518 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 865 granskar 24 operatorer i Blenders Mesh-redigeringsläge: rensning,
slingverktyg, normaler, primitiv, urval och utjämning. Den normaliserar bland
annat *meshdata*, *meshslinga*, *kantslinga*, *meshplan*, *meshytor* och
*meshelement*, samt använder *kubmesh*, *konmesh*, *cylindermesh* och
*Suzanne-mesh* där typen är en del av verktygets objekt. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-865-mesh-edit-operators.po` är en
separat manuell deltafil med endast dessa 24, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-865.po` är den aktuella
samlade manuella deltafilen för batch 811–865. Den innehåller 521 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 866 granskar 20 skulpteringsoperatorer för tyg, topologi,
ytuppsättningar och meshfilter. Den ersätter oprecisa nätformer med
*meshen*, *meshtopologi*, *meshobjekt* och *meshö*, och använder den
verktygsspecifika etiketten *Relaxa mesh* för filtret `Relax`. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-866-mesh-sculpt-operators.po` är en
separat manuell deltafil med endast dessa 20, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-866.po` är den aktuella
samlade manuella deltafilen för batch 811–866. Den innehåller 521 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 867 granskar 15 fel- och verktygssträngar för meshobjekt, interaktiv
primitivskapning, dynamisk målning och redigeringsläge. Den skiljer
konsekvent på *meshobjekt*, *meshelement*, *meshen*, *dukmesh* och
*redigeringsmesh*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-867-mesh-object-errors.po` är en
separat manuell deltafil med endast dessa 15, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-867.po` är den aktuella
samlade manuella deltafilen för batch 811–867. Den innehåller 530 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 868 granskar 15 Quadriflow-, ytdeformerings- och voxelommeshningssträngar.
Den använder *fyrhörningsbaserad mesh*, *meshen*, *meshgräns*,
*utdata-mesh* och *manifold-mesh*. Den tidigare formuleringen *slutet nät*
ersätts eftersom manifold inte alltid innebär att en mesh är sluten. Batchen
är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-868-quadriflow-mesh.po` är en separat
manuell deltafil med endast dessa 15, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-868.po` är den aktuella
samlade manuella deltafilen för batch 811–868. Den innehåller 530 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 869 granskar tio valideringsfel från Blenders dataöverföring. Den skiljer
kort och idiomatiskt mellan *källmesh*, *målmesh* och *källmeshen* samt
behåller de synliga mappningsnamnen `Edge` och `Face`. Batchen är lokalt klar
men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-869-data-transfer-mesh.po` är en
separat manuell deltafil med endast dessa tio, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-869.po` är den aktuella
samlade manuella deltafilen för batch 811–869. Den innehåller 540 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 870 granskar 18 fel- och valideringssträngar för sammanfogning,
bakning, dataöverföring, ommeshning, ytdeformering och samlingar. Den
normaliserar *meshdata*, *meshobjekt*, *ytmesh*, *källmesh* och *målmesh*,
och skiljer mellan den specifika *voxelommesharen* och det generella
*ommeshningsverktyget*. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-870-mesh-validation-errors.po` är en
separat manuell deltafil med endast dessa 18, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-870.po` är den aktuella
samlade manuella deltafilen för batch 811–870. Den innehåller 558 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 871 granskar 61 strängar för Shrinkwrap, geometri­noder, UV, kurvor,
modifierare och simuleringsresurser. Den ersätter äldre nätformer med
*meshen*, *meshobjekt*, *meshplan*, *meshö*, *meshinstans*, *ytmesh* och
*målmesh*, samt använder verbet *ommesha* för operatören `Remesh`. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-871-mesh-geometry-nodes.po` är en
separat manuell deltafil med endast dessa 61, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-871.po` är den aktuella
samlade manuella deltafilen för batch 811–871. Den innehåller 619 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 872 granskar 16 Animation- och nodträdstermer. Den behåller det formella
Blendernamnet *Action* i sammansättningar som *Action-grupp*, *Action-lager*,
*Action-slot* och *Action-remsa*, använder *Dopeblad* i redigerarnamnet och
normaliserar *kompositionsnodträd*, *shadernodträd* och *geometrinodträd*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-872-action-node-tree.po` är en separat
manuell deltafil med dessa 16, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-872.po` är den aktuella
samlade manuella deltafilen för batch 811–872. Den innehåller 619 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 873 granskar nio strängar för filmspårningsdopebladet och
Dopebladsredigeraren. Den rättar bland annat sorteringsetiketter, kanaler,
markering av bildrutor och den synliga växlingsåtgärden. Batchen är lokalt
klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-873-dopeblad.po` är en separat manuell
deltafil med dessa nio, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-873.po` är den aktuella
samlade manuella deltafilen för batch 811–873. Den innehåller 627 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 874 granskar två återstående shadernodträdstermer: ett infogat
shadernodträd och ett felmeddelande vid sökning efter material eller ljus.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-874-shader-node-tree.po` är en separat
manuell deltafil med dessa två, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-874.po` är den aktuella
samlade manuella deltafilen för batch 811–874. Den innehåller 629 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 875 granskar sju kompositionssträngar för scenen, sekvensredigeraren
och kompositorns nodgrupper. Den normaliserar *kompositionsnodgrupp*,
*kompositionseffekt*, *scenkomposition* och *sekvenserarkomposition*.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-875-composition.po` är en separat
manuell deltafil med dessa sju, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-875.po` är den aktuella
samlade manuella deltafilen för batch 811–875. Den innehåller 636 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 876 granskar åtta validerings- och operatorsträngar för Blenders
formella animationsdatatyp Action. Den använder konsekvent *Action-slot* och
*Action-slotar* i stället för den oprecisa formen *åtgärdsslot*. Batchen är
lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-876-action-slot-errors.po` är en
separat manuell deltafil med dessa åtta, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-876.po` är den aktuella
samlade manuella deltafilen för batch 811–876. Den innehåller 644 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 877 granskar tio kärntexter för Action-slotar: kanaler, markering,
utfällning, datablockstyp, aktiv slot och F-kurvremsor. Den använder den
formella benämningen *Action-slot* och böjningen *Actionen* konsekvent.
Batchen är lokalt klar men ännu inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-877-action-slot-core.po` är en separat
manuell deltafil med dessa tio, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-877.po` är den aktuella
samlade manuella deltafilen för batch 811–877. Den innehåller 654 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 878 granskar tio Action-slot-texter för handtag, tillfällig lagring,
identifierare, NLA och borttagning av tilldelningar. Den normaliserar även
sammansättningen *huvud-Action-slot*. Batchen är lokalt klar men ännu inte
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-878-action-slot-storage.po` är en
separat manuell deltafil med dessa tio, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-878.po` är den aktuella
samlade manuella deltafilen för batch 811–878. Den innehåller 664 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 879 granskar 17 beskrivningar och meddelanden för Action-slotar,
Action-begränsningar och äldre Actioner. Den använder konsekvent de formella
datatypsnamnen *Action*, *Action-slot* och *Action-begränsning*, inklusive
böjningen *Actionen* och pluralen *Actioner*. Batchen är lokalt klar men ännu
inte importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-879-action-slot-descriptions.po` är
en separat manuell deltafil med dessa 17, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-879.po` är den aktuella
samlade manuella deltafilen för batch 811–879. Den innehåller 681 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 880 rättar nodterminologin i färgrymdsinställningen: *shader* används
konsekvent som Blenders fackterm, parallellt med *kompositionsnoder* och
*geometrinoder*. Batchen är lokalt klar men ännu inte importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-880-node-processing-terminology.po`
är en separat manuell deltafil med denna lokalt granskade ändring.

`blender-ui-sv-reviewed-20261108-pending-batches-811-880.po` är den aktuella
samlade manuella deltafilen för batch 811–880. Den innehåller 682 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 881 rättar den formella Blender-datatypen *mesh* i ett meddelande från
geometrinoder: *Ytan har ingen mesh* ersätter den oprecisa översättningen
”Ytan har inget nät”. Batchen är lokalt klar men ännu inte importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-881-surface-mesh-terminology.po` är
en separat manuell deltafil med denna lokalt granskade ändring.

`blender-ui-sv-reviewed-20261108-pending-batches-811-881.po` är den aktuella
samlade manuella deltafilen för batch 811–881. Den innehåller 682 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 882 normaliserar tolv UI-strängar i modifierar- och geometriområdet.
Den behåller Blenders formella datatyp *mesh* i stället för ”nät”, medan
*rutnät* lämnas oförändrat där källtermen är *grid*. Batchen är lokalt klar
och pushad till vårt arkiv, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-882-mesh-terminology.po` är en
separat manuell deltafil med dessa tolv, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-882.po` är den aktuella
samlade manuella deltafilen för batch 811–882. Den innehåller 682 poster,
passerar lokal syntax- och lintkontroll och är ännu inte importerad i Blender
Translate.

Batch 883 fortsätter normaliseringen av *mesh* i tolv modifierarsträngar,
bland annat för meshcache, meshobjekt, meshyta och meshens böjning. Batchen
är lokalt klar och pushad till vårt arkiv, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-883-mesh-modifiers.po` är en separat
manuell deltafil med dessa tolv, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-883.po` är den aktuella
samlade manuella deltafilen för batch 811–883. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 884 granskar åtta Shrinkwrap-strängar. Funktionsnamnet *Shrinkwrap*
behålls, medan de beskrivande texterna använder *anpassa meshen* och
*mesh-mål* i stället för den oidiomatiska formen ”krympinpacka”. Batchen är
lokalt klar och pushad till vårt arkiv, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-884-shrinkwrap-terminology.po` är en
separat manuell deltafil med dessa åtta, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-884.po` är den aktuella
samlade manuella deltafilen för batch 811–884. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 885 granskar tio modifierarsträngar för Blenders datatyp *mesh*, bland
annat meshdata, meshdeformation, målmeshen och adaptiv underindelning.
Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte verifierad
som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-885-mesh-modifiers.po` är en separat
manuell deltafil med dessa tio, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-885.po` är den aktuella
samlade manuella deltafilen för batch 811–885. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 886 granskar tio geometri-nodsträngar som uttryckligen använder
Blenders datatyp *mesh*. Batch 887 rättar den svenska böjningen till
*meshens ytor*. Båda batcherna är lokalt klara och pushade till vårt arkiv,
men ännu inte verifierade som importerade i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-886-geometry-mesh.po` och
`blender-ui-sv-reviewed-20261108-batch-887-mesh-inflection.po` är separata
manuella deltafiler med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-887.po` är den aktuella
samlade manuella deltafilen för batch 811–887. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 888 granskar sex geometri-nodsträngar och normaliserar *meshnormaler*,
*meshkanter*, *meshytor*, *meshgeometri* och *meshdatablock*. Batchen är
lokalt klar och pushad till vårt arkiv, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-888-geometry-mesh.po` är en separat
manuell deltafil med dessa sex, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-888.po` är den aktuella
samlade manuella deltafilen för batch 811–888. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 889 granskar sex modifierarsträngar och normaliserar bland annat
*basmeshen*, *ingångsmeshen*, *manifold-mesh* och *meshveck*. Batchen är
lokalt klar och pushad till vårt arkiv, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-889-mesh-modifiers.po` är en separat
manuell deltafil med dessa sex, lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-889.po` är den aktuella
samlade manuella deltafilen för batch 811–889. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 890 granskar sex geometri- och meshsträngar och använder bland annat
*kubmesh*, *meshhörn*, *meshkanter* och *meshattribut*. Batch 891 granskar
fem relaterade strängar och normaliserar *källmesh*, *meshobjekt* och
*meshens lokala rum*. Batch 892 rättar den formella Blender-termen *shader
node* till *shadernod* i en renderingspassbeskrivning. Dessa batcher är
lokalt klara och pushade till vårt arkiv, men ännu inte verifierade som
importerade i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-890-geometry-mesh.po`,
`blender-ui-sv-reviewed-20261108-batch-891-mesh-data.po` och
`blender-ui-sv-reviewed-20261108-batch-892-shader-node-terminology.po` är
separata manuella deltafiler med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-892.po` är den aktuella
samlade manuella deltafilen för batch 811–892. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 893 skiljer på Blenders formella data-/UI-term *Shader Node*, som blir
*Shadernod*, och pluralformen *Shaders* i Node Wranglers sammanslagningskommando,
som blir *skuggningar*. Batchen är lokalt klar och pushad till vårt arkiv,
men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-893-shader-node-terminology.po` är en
separat manuell deltafil med dessa två lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-893.po` är den aktuella
samlade manuella deltafilen för batch 811–893. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 894 normaliserar tre böjningsformer av den formella datatypen *Shader
Node* till *shadernoder* i inställningarna för nodförhandsgranskning.
Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte verifierad
som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-894-shader-node-inflection.po` är en
separat manuell deltafil med dessa tre lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-894.po` är den aktuella
samlade manuella deltafilen för batch 811–894. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 895 granskar två modifierarhjälptexter. Den använder den naturliga
formen *modifierarens resultat* och normaliserar *modifier space* till
*modifierarens koordinatrum*. Batchen är lokalt klar och pushad till vårt
arkiv, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-895-modifier-space-and-result.po` är
en separat manuell deltafil med dessa två lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-895.po` är den aktuella
samlade manuella deltafilen för batch 811–895. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 896 rättar en hjälptexts genus för Blenders datatyp *mesh*: *denna
mesh* i stället för neutrumformen *detta mesh*. Batchen är lokalt klar och
pushad till vårt arkiv, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-896-mesh-grammatical-gender.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-896.po` är den aktuella
samlade manuella deltafilen för batch 811–896. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 897 granskar två hjälptexter för masköverordning och ersätter en felaktig
ordföljd med *det överordnade objektet … som används för överordning*.
Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte verifierad
som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-897-mask-parenting-help.po` är en
separat manuell deltafil med dessa två lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-897.po` är den aktuella
samlade manuella deltafilen för batch 811–897. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 898 normaliserar Blenders tekniska term *packed* till *packat* i en
datablockshjälptext. Batchen är lokalt klar och pushad till vårt arkiv, men
ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-898-packed-datablock-terminology.po`
är en separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-898.po` är den aktuella
samlade manuella deltafilen för batch 811–898. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 899 granskar nio meshsträngar. Den rättar böjningen till *meshen* och
*meshens* och skriver etablerade sammansättningar som *meshobjekt*,
*meshsymmetri*, *meshkanter*, *meshnormaler* och *meshhörnpunkt* utan
bindestreck. Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-899-mesh-compounds-and-inflection.po`
är en separat manuell deltafil med dessa nio lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-899.po` är den aktuella
samlade manuella deltafilen för batch 811–899. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 900 normaliserar nio tydliga pluralformer av Blenders datatyp *mesh*
till *meshar*, bland annat i datablockslistor, geometri- och bakningshjälptexter
och booleska meshoperationer. Batchen är lokalt klar och pushad till vårt
arkiv, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-900-mesh-plural-forms.po` är en
separat manuell deltafil med dessa nio lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-900.po` är den aktuella
samlade manuella deltafilen för batch 811–900. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 901 rättar två vanliga mesh-sammansättningar till *meshindata* och
*meshhörnpunkter*. Den närliggande ellipsformen *mesh- eller
gitterhörnpunktsgrupp* är medvetet oförändrad. Batchen är lokalt klar och
pushad till vårt arkiv, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-901-mesh-compound-cleanup.po` är en
separat manuell deltafil med dessa två lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-901.po` är den aktuella
samlade manuella deltafilen för batch 811–901. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 902 normaliserar felmeddelandets Mantaflow-etikett från engelska
*Fluid:* till svenska *Vätska:* så att den följer de närliggande
cachemeddelandena. Den tekniska termen *cachesökväg* och platshållaren `%s`
är oförändrade. Batchen är lokalt klar och pushad till vårt arkiv, men ännu
inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-902-fluid-label.po` är en separat
manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-902.po` är den aktuella
samlade manuella deltafilen för batch 811–902. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 903 granskar en byggstatus för ommeshning och ersätter det engelska
produktuttrycket *Remesh-modifieraren* med den fastställda tekniska termen
*ommeshningsmodifieraren*. Batchen är lokalt klar och pushad till vårt arkiv,
men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-903-remesh-modifier-status.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-903.po` är den aktuella
samlade manuella deltafilen för batch 811–903. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 904 granskar 22 centrala UI- och felmeddelandesträngar där Blenders
formella datatyp *mesh* tidigare hade översatts som *nät*. Den behåller
*mesh* i datatyper och etiketter, använder böjningarna *meshen* och *meshar*
och skriver tekniska sammansättningar som *meshsymmetri*, *meshgräns* och
*meshcache*. Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-904-mesh-datatype-core.po` är en
separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-904.po` är den aktuella
samlade manuella deltafilen för batch 811–904. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 905 granskar åtta tekniska meshsträngar i bland annat Rigify,
Freestyle, modifierare och geometrinoder. Den använder de etablerade
formerna *widgetmesh*, *meshdeformering*, *meshsekvenscache*,
*meshinläsning* och *provta*. Batchen är lokalt klar och pushad till vårt
arkiv, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-905-mesh-technical-compounds.po` är
en separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-905.po` är den aktuella
samlade manuella deltafilen för batch 811–905. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 906 rättar en filutdatahjälptext från singular till plural:
*filformatstilläggen*. Lintverktyget noterar en ofarlig skiljeteckensskillnad
eftersom källans engelska exempel använder kolon i *eg:* medan svenskans
*t.ex.* är korrekt utan kolon. Batchen är lokalt klar och pushad till vårt
arkiv, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-906-file-extension-plural.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-906.po` är den aktuella
samlade manuella deltafilen för batch 811–906. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 907 rättar motsvarande pluralfel i renderingsinställningen till
*filformatstilläggen*. Precis som i batch 906 är lintverktygets
skiljeteckensanmärkning väntad: engelskans *eg:* motsvaras av svenskans
*t.ex.* utan kolon. Batchen är lokalt klar och pushad till vårt arkiv, men
ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-907-render-file-extension-plural.po`
är en separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-907.po` är den aktuella
samlade manuella deltafilen för batch 811–907. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 908 rättar *taggade kanter* till *markerade kanter* i inställningen som
bevarar skarpa kanter vid mjuk skuggning. Här avser *tagged* den interna
markeringen för skärpa, inte de användarskapade taggar som finns i andra delar
av Blender. Terminologilistan har uppdaterats med distinktionen. Batchen är
lokalt klar och pushad till vårt arkiv, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-908-tagged-sharp-edges.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-908.po` är den aktuella
samlade manuella deltafilen för batch 811–908. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 909 normaliserar bildredigerarens färgprovtagning från *sampla* till
*provta*. Scope-panelerna behålls som synligt namn på bildanalysvyerna; det
är skilt från det interna GPU-uttrycket *scope name*. Batchen är lokalt klar
och pushad till vårt arkiv, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-909-image-sampling.po` är en separat
manuell deltafil med dessa två lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-909.po` är den aktuella
samlade manuella deltafilen för batch 811–909. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 910 ersätter lånet *sampla* med *provta* i nio bild-, viktmålnings- och
geometriverktyg. Den omfattar färg-, pixel-, vikt-, hörnpunktsgrupps- och
ljudfrekvensprovtagning och uppdaterar terminologilistan med verktygskontexten.
Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-910-sample-tool-verbs.po` är en
separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-910.po` är den aktuella
samlade manuella deltafilen för batch 811–910. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 911 rättar två återstående provtagningssträngar där handlingen tidigare
hade översatts som ett substantiv. Den använder *Provta vikt* i
viktmålningsverktyget och *Metod för att provta indata* i geometrinoden.
Batchen är lokalt klar och pushad till vårt arkiv, men ännu inte verifierad
som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-911-sampling-action-grammar.po` är en
separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-911.po` är den aktuella
samlade manuella deltafilen för batch 811–911. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 912 normaliserar fyra tekniska sammansättningar: *meshcache*,
*cacheinformation*, *shaderprogram* och *cacheläsare*. Terminologilistan
anger nu även pluralformen *meshar* för Blender-datatypen *mesh*. Batchen är
lokalt klar, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-912-technical-compounds.po` är en
separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-912.po` är den aktuella
samlade manuella deltafilen för batch 811–912. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 913 tar bort den inkonsekventa bindestrecksformen *shader-noder* i två
material- och ljusinställningar. Enligt den projektspecifika terminologin är
*shadernod* den formella Blender-nodtypen. Batchen är lokalt klar, men ännu
inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-913-shader-node-compounds.po` är en
separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-913.po` är den aktuella
samlade manuella deltafilen för batch 811–913. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 914 tillämpar den etablerade sammansättningen *shadernod* i en
världsinställning och en shaderskriptnod. Batchen är lokalt klar, men ännu
inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-914-shader-node-terms.po` är en
separat manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-914.po` är den aktuella
samlade manuella deltafilen för batch 811–914. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 915 sammanfogar fem sammansättningar kring datatypen *mesh*:
*meshobjekt* och *meshsymmetri*. Batchen är lokalt klar, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-915-mesh-compounds.po` är en separat
manuell deltafil med dessa lokalt granskade ändringar.

`blender-ui-sv-reviewed-20261108-pending-batches-811-915.po` är den aktuella
samlade manuella deltafilen för batch 811–915. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 916 normaliserar den synliga nodträdsetiketten till *Shadernoder* i
enlighet med termposten *shadernod*. Batchen är lokalt klar, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-916-shader-node-label.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-916.po` är den aktuella
samlade manuella deltafilen för batch 811–916. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 917 ersätter det vaga lånet *tagga data* med den svenska
åtgärdsbeskrivningen *märka data* i en API-relaterad förklaring. Batchen är
lokalt klar, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-917-data-tagging.po` är en separat
manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-917.po` är den aktuella
samlade manuella deltafilen för batch 811–917. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 918 rättar endast den kontextmärkta Blender-datatypen `Action`. Den
vanliga svenska handlingstermen påverkas inte. Batchen är lokalt klar, men
ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-918-action-id-datatype.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-918.po` är den aktuella
samlade manuella deltafilen för batch 811–918. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 919 använder projektnamnet *dopebladet* i en förklaring om omberäkning
av animeringsdata. Batchen är lokalt klar, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-919-dope-sheet-recalculation.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-919.po` är den aktuella
samlade manuella deltafilen för batch 811–919. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 920 anger den formella animationsetiketten *Action-slot* med
produktnamnet `Action` bevarat. Batchen är lokalt klar, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-920-action-slot-label.po` är en
separat manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-920.po` är den aktuella
samlade manuella deltafilen för batch 811–920. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 921 uppdaterar två hjälprader för den formella Blender-datatypen
*Action-slot*. Den vanliga handlingstermen påverkas inte. Batchen är lokalt
klar, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-921-action-slot-help.po` är en separat
manuell deltafil med de lokalt granskade ändringarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-921.po` är den aktuella
samlade manuella deltafilen för batch 811–921. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 922 normaliserar fyra NLA- och AnimData-etiketter där `Action` är
Blenders formella animationsdatablock, inte den vanliga handlingstermen.
Batchen är lokalt klar, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-922-active-action-datatype.po` är en
separat manuell deltafil med de lokalt granskade ändringarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-922.po` är den aktuella
samlade manuella deltafilen för batch 811–922. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 923 normaliserar modifierar- och Geometry Nodes-etiketten *Volym till
mesh*. Den kompletterar den redan granskade parallellformen *Mesh till volym*.
Batchen är lokalt klar, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-923-volume-to-mesh.po` är en separat
manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-923.po` är den aktuella
samlade manuella deltafilen för batch 811–923. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 924 kompletterar Geometry Nodes-etiketten *Mesh till punkter* enligt
den etablerade *mesh*-terminologin. Batchen är lokalt klar, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-924-mesh-to-points.po` är en separat
manuell deltafil med den lokalt granskade ändringen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-924.po` är den aktuella
samlade manuella deltafilen för batch 811–924. Antalet unika poster ska
beräknas från filen före varje import eftersom flera batcher kan korrigera
samma källsträng.

Batch 925 normaliserar Geometry Nodes- och modifieraretiketterna *Mesh till
kurva* och *Mesh till volym*. I dessa lägen är `Mesh` ett formellt
Blender-datablocknamn och ska inte översättas som *nät*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-925-mesh-conversion-labels.po` är den
separata manuella deltafilen med de två rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-925.po` är den samlade
manuella deltafilen för batch 811–925. Den innehåller 784 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 926 rättar Geometry Nodes-etiketten *Mesh till densitetsrutnät*. Precis
som för de övriga konverteringsnoderna är `Mesh` här ett formellt
datablocknamn, inte det allmänna ordet *nät*. Batchen är lokalt granskad, men
ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-926-mesh-to-density-grid.po` är den
separata manuella deltafilen med rättningen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-926.po` är den samlade
manuella deltafilen för batch 811–926. Den innehåller 785 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 927 normaliserar de tekniska meshtopologi- och komponentetiketterna
*Meshkant*, *Meshyta*, *Meshytehörn* och *Meshkomponent*. De avser Blenders
formella meshtyp och följer därför den etablerade `mesh`-terminologin i stället
för den generiska formen *nät*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-927-mesh-topology-domains.po` är den
separata manuella deltafilen med de fyra rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-927.po` är den samlade
manuella deltafilen för batch 811–927. Den innehåller 789 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 928 normaliserar fyra Geometry Nodes-etiketter till *Meshö*,
*Meshavfasning*, *Meshcirkel* och *Meshlinje*. De avser Blenders formella
meshtyp; *Meshavfasning* följer dessutom den etablerade UI-termen
*avfasning*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-928-mesh-geometry-node-labels.po` är
den separata manuella deltafilen med de fyra rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-928.po` är den samlade
manuella deltafilen för batch 811–928. Den innehåller 793 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 930 normaliserar RNA-beskrivningen *Meshdatablock som definierar
geometriska ytor*. Den sammanskrivna formen följer projektets etablerade
`mesh`-terminologi och ersätter den inkonsekventa formen *Mesh-datablock*.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-930-mesh-datablock-label.po` är den
separata manuella deltafilen med rättningen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-930.po` är den samlade
manuella deltafilen för batch 811–930. Den innehåller 794 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 931 normaliserar de synliga 3D-vyportsetiketterna *Använd 3D-vyport*
och *Alla 3D-vyportar*. Formen följer den etablerade Blender-termen
*3D-vyport* när källtexten uttryckligen avser `3D Viewport`. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-931-3d-viewport-labels.po` är den
separata manuella deltafilen med de två rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-931.po` är den samlade
manuella deltafilen för batch 811–931. Den innehåller 796 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 932 normaliserar vyportskontexten i kompositörbeskrivningen och
temakategorin till *3D-vyport* samt rättar etiketten *Storlek i
visningsområdet*. Rättningarna följer den etablerade projektterminologin och
svensk bestämd form. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-932-viewport-context-labels.po` är
den separata manuella deltafilen med de tre rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-932.po` är den samlade
manuella deltafilen för batch 811–932. Den innehåller 799 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

Batch 933 normaliserar RNA-etiketterna *Geometrinoduttag* och
*Heltalsvektornoduttag*. De följer de befintliga formerna
*geometrinoduttagsgränssnitt* och *heltalsvektornoduttagsgränssnitt* samt
Blenders konsekventa sammanskrivning av nodtermer. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-933-node-socket-compounds.po` är den
separata manuella deltafilen med de två rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-933.po` är den samlade
manuella deltafilen för batch 811–933. Den innehåller 801 översättningsposter
och ryms därför inom gränsen på 1 000 strängar för en Blender Translate-import.

En lokal sammanslagning av den nedladdade UI-filen och batch 811–922 har
kontrollerats med `msgfmt` och `svlang svengelska`. De enda återstående
anglicismträffarna är det synliga Blender-namnet *Scope* i *Scope-panelerna*
och de bokstavliga katalognamnen `startup`, `add-ons`, `modules` och
`presets`. Formerna *shader-nod*, *mesh-*, *cache-*, *åtgärdsslot* och
*Dopesheet* förekommer inte längre som svenska måltexter i den effektiva
lokala sammanställningen. Detta är lokal QA och inte ett importresultat från
Blender Translate.

## Manuellt verifierat importresultat (2026-11-08)

Användaren har visat Blender Translates importresultat för en manuell
deltaimport: **351** strängar behandlades, **312** uppdaterades och **39**
hoppades över. Resultatet bekräftar importen av den valda filen, men anger
inte på egen hand vilka lokala batchnummer som ingick. Senare batcher ska
därför fortsatt behandlas som lokalt granskade tills deras egen import kan
verifieras.

## Batch 934 — resurs i resursbläddraren

Batch 934 rättar den kontextspecifika beskrivningen för val av
resursbibliotek. I Blenders resursbläddrare är *asset* en **resurs**; den
tidigare formuleringen *visa tillgångar från* ersätts därför med *visa
resurser från*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-934-asset-library-resource-label.po`
är den separata manuella deltafilen med rättningen.

`blender-ui-sv-reviewed-20261108-pending-batches-811-934.po` är den samlade
manuella deltafilen för batch 811–934. Den innehåller 802
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 935 — resurstermer i resursbläddraren

Batch 935 normaliserar tolv synliga etiketter och hjälprader för
resursbläddraren. I den här konkreta Blender-kontexten motsvarar *asset*
**resurs**, vilket ger bland annat *resursdata*, *resursrepresentation*,
*resurstyper* och *resursernas förhandsvisningsminiatyrer*. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-935-asset-browser-resource-terms.po`
är den separata manuella deltafilen med de tolv rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-935.po` är den samlade
manuella deltafilen för batch 811–935. Den innehåller 814
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 936 — Action-datablock

Batch 936 rättar åtta UI-etiketter som syftar på Blenders formella
animationsdatatyp *Action*. Etiketterna använder därför produktnamnet, till
exempel *Action-blandning*, *Action-extrapolering*, *Action-påverkan* och
*Action-redigerare*, i stället för det generella ordet *åtgärd*. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-936-action-datablock-labels.po`
är den separata manuella deltafilen med de åtta rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-936.po` är den samlade
manuella deltafilen för batch 811–936. Den innehåller 822
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 937 — resursbläddrarens detaljer

Batch 937 fortsätter den kontextspecifika normaliseringen av *asset* till
*resurs* i resursbläddrarens inställningar och filter: *resursåtkomst*,
*resursreferens*, *resursdatablock* och resurskatalogernas visningsfilter.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-batch-937-asset-browser-resource-details.po`
är den separata manuella deltafilen med de tio rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-937.po` är den samlade
manuella deltafilen för batch 811–937. Den innehåller 832
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 938 — resursimport och metadata

Batch 938 rättar sju informations- och operatörstexter för resursimport,
resurskatalogfilter samt resursers licens- och upphovsrättsmetadata. Den
fortsätter den kontextspecifika formen *resurs* utan att ändra Blenders
produktnamn eller kodtermer. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-938-asset-browser-import-details.po`
är den separata manuella deltafilen med de sju rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-938.po` är den samlade
manuella deltafilen för batch 811–938. Den innehåller 839
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 939 — gräns mellan UI och API

Batch 939 korrigerar sju API-nära *asset*-poster efter kontroll mot den
projektspecifika terminologin. Asset Browser använder *resurs* i sin synliga
UI, medan RNA/API-typerna *Asset Data*, *Asset Representation* och
*Asset Weak Reference* använder *tillgång*; exempelvis
*tillgångsrepresentation* och *svag tillgångsreferens*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-939-asset-api-context-corrections.po`
är den separata manuella deltafilen med kontextkorrigeringarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-939.po` är den samlade
manuella deltafilen för batch 811–939. Den innehåller fortsatt 839
översättningsposter, eftersom batchen ersätter tidigare formuleringar i
samma identiteter.

## Batch 940 — resurser på nätet och interaktion

Batch 940 granskar resursbläddrarens interaktion och onlinefilter. Den
normaliserar synlig UI till *resurs* och använder *på nätet* i stället för
det engelskpåverkade *online*, medan de API-nära posterna från batch 939
fortsätter använda *tillgång*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-940-asset-browser-online-and-interaction.po`
är den separata manuella deltafilen med de nio rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-940.po` är den samlade
manuella deltafilen för batch 811–940. Den innehåller 848
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 941 — Action-datablockets beskrivningar

Batch 941 granskar nio beskrivningar som uttryckligen avser Blenders
animationsdatatyp *Action*. Produktnamnet bevaras därför i böjda och
sammansatta former, exempelvis *Actionen*, *Actioner* och
*Action-kanaler*, medan det generella svenska *åtgärd* lämnas kvar i
obesläktade handlingskontexter. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-941-action-datablock-descriptions.po`
är den separata manuella deltafilen med de nio rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-941.po` är den samlade
manuella deltafilen för batch 811–941. Den innehåller 857
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 942 — Action- och NLA-operatorer

Batch 942 granskar elva ytterligare strängar där *action* enligt RNA- eller
operatörskontexten är animationsdatatypen *Action*: NLA-remsors bildrutor,
bakning till en Action, Action-listor och scenmarkörer. Svenska böjningar och
sammansättningar följer därför den etablerade projektspecifika formen
*Actionen*, *Actioner* och *Action-lista*. Den generella betydelsen
"åtgärd" berörs inte. Batchen är lokalt granskad, men ännu inte verifierad
som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-942-action-nla-operators.po` är den
separata manuella deltafilen med de elva rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-942.po` är den samlade
manuella deltafilen för batch 811–942. Den innehåller 868
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 943 — Action-referenser i NLA

Batch 943 granskar femton NLA- och animationsoperatorer som läser, lagrar,
byter, bakar eller refererar till Blenders formella animationsdatatyp
*Action*. Termerna normaliseras till *Action*, *Actionen* och *Actioner*;
*Action Constraints* blir *Action-begränsningar*. Det vanliga ordet
"åtgärd" i generella gränssnittskommandon ändras inte. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-943-action-nla-data-references.po` är
den separata manuella deltafilen med de femton rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-943.po` är den samlade
manuella deltafilen för batch 811–943. Den innehåller 883
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 944 — Action i export och redigerare

Batch 944 granskar femton strängar i FBX- och glTF-exportörerna samt
Action- och Dopebladsredigerarnas lägen. Där *actions* är Blenders
animationsdatatyp skrivs den konsekvent *Actioner*; *Action* behålls i
benämningar på datatypen och dess funktioner. Tekniska namn som FBX,
AnimStack, glTF och NLA lämnas avsiktligt oförändrade. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-944-action-export-and-editor.po` är
den separata manuella deltafilen med de femton rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-944.po` är den samlade
manuella deltafilen för batch 811–944. Den innehåller 898
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 945 — Action-slotar och NLA-egenskaper

Batch 945 granskar femton ytterligare RNA-egenskaper för Action-slotar,
NLA-spår och Action-redigeraren. Här är *action* otvetydigt
animationsdatatypen *Action*, även i sammansättningar som
*NLA-Action-spår* och *Action-redigeraren*. Generella åtgärder utanför
animationsdata lämnas oförändrade. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-945-action-slot-and-editor.po` är den
separata manuella deltafilen med de femton rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-945.po` är den samlade
manuella deltafilen för batch 811–945. Den innehåller 913
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 946 — nodträd och modifierare

Batch 946 granskar nio strängar för kompositions- och texturnodträd,
nodslutningar, modifierardata och F-kurvmodifierare. Den normaliserar
sammansättningar enligt Blender-termbasen, bland annat
*kompositionsnodträd*, *texturnodträd*, *modifierarstack* och
*F-kurvmodifierare*. Operatören *Split Normals* får den handlingsinriktade
översättningen *Dela normaler*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-946-node-and-modifier-terms.po` är
den separata manuella deltafilen med de nio rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-946.po` är den samlade
manuella deltafilen för batch 811–946. Den innehåller 922
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 947 — fjärranslutna resurser och cache

Batch 947 omfattar två synliga Asset Browser-strängar. *Asset downloads*
normaliseras till *resurshämtningar*, medan *download cache directory* använder
den idiomatiska formuleringen *cachekatalogen för nedladdning*, i enlighet med
den tidigare fastställda svenska formuleringen. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-947-remote-asset-cache.po` är den
separata manuella deltafilen med de två rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-947.po` är den samlade
manuella deltafilen för batch 811–947. Den innehåller 924
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 948 — färghanteringens visningstransformeringar

Batch 948 granskar tolv färghanteringssträngar. Den normaliserar *view
transform* till den etablerade Blender-termen *visningstransformering* i
ACES-, AgX-, Filmic- och Khronos-beskrivningar samt i färghanteringens
kompositörs- och sekvensredigerarinställningar. Format- och färgrymdsnamn
som ACES, AgX, Filmic, OpenEXR och sRGB bevaras. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-948-color-management-view-transforms.po`
är den separata manuella deltafilen med de tolv rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-948.po` är den samlade
manuella deltafilen för batch 811–948. Den innehåller 934
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 949 — nätåtkomst och utdatafilsökväg

Batch 949 granskar två inställningssträngar. *Online access* normaliseras
till *nätåtkomst* och *Output Filepath* till *utdatafilsökväg*, parallellt
med projektets etablerade term *inmatningsfilsökväg*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-949-network-and-output-path.po` är
den separata manuella deltafilen med de två rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-949.po` är den samlade
manuella deltafilen för batch 811–949. Den innehåller 936
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 950 — Action-datablockets RNA-egenskaper

Batch 950 granskar fyra RNA-beskrivningar för Action-slotar och
animationsdata. *Action* är här en namngiven Blender-datatyp, så formerna
*Actionen* och *Action* används i stället för det allmänna ordet *åtgärd*.
*Datablock* och *ID-typ* hålls samtidigt ihop enligt termbasen. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-950-action-datablock-rna.po` är den
separata manuella deltafilen med de fyra rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-950.po` är den samlade
manuella deltafilen för batch 811–950. Den innehåller 940
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 951 — Action och biblioteksåsidosättning

Batch 951 granskar fyra operator- och RNA-beskrivningar. Den behåller
produktnamnet *Action* i kommandot *Koppla bort Action* och normaliserar
Blenders funktion *Library Override* till *biblioteksåsidosättning*; den
felaktiga äldre formen *biblioteksöverskrivning* används inte. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-batch-951-action-and-library-override.po`
är den separata manuella deltafilen med de fyra rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-811-951.po` är den samlade
manuella deltafilen för batch 811–951. Den innehåller 944
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 977 — Mesh och Shrinkwrap

Batch 977 granskar åtta Mesh-poster för normaler, maskering, Shrinkwrap,
solidifiering och avfasning. Den använder *meshen*, *basmesh* och
*manifold-mesh*. I Shrinkwraps förklarande text används det idiomatiska
*anpassa meshen till målytan*, medan funktionsnamnet *Shrinkwrap* behålls.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-batch-977-mesh-shrinkwrap.po` är den separata
manuella deltafilen med de åtta rättningarna.

`blender-ui-sv-reviewed-20261108-pending-batches-957-977.po` är den samlade
manuella deltafilen för batch 957–977. Den innehåller 164
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 978 — Meshens färgattribut

Batch 978 granskar en feltext från baknings-API:t. Den ersätter *nätet* med
den projektkorrekta formen *meshen* och bevarar platshållaren `%s` samt de
typografiska citattecknen. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-978.po` är den samlade
manuella deltafilen för batch 957–978. Den innehåller 165
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 979 — Mesh och resursimport

Batch 979 granskar fyra RNA-beskrivningar för meshinställningar och
resursimport. Den använder *mesh*, *meshen* och *meshmålning* för den formella
Blender-datatypen och normaliserar den synliga Asset Browser-termen *asset* till
*resurs*. Batchen är lokalt granskad, men ännu inte verifierad som importerad i
Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-979.po` är den samlade
manuella deltafilen för batch 957–979. Den innehåller 168
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 980 — Meshbakning och ommeshning

Batch 980 granskar fyra beskrivningar för bakning, vätskeemission och
ommeshningsmodifieraren. Den använder konsekvent *mesh*, *meshens yta* och
*meshtopologi*, medan *domänrutnät* bevaras eftersom det betecknar det faktiska
simuleringsrutnätet. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-980.po` är den samlade
manuella deltafilen för batch 957–980. Den innehåller 172
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 981 — Meshdeformering

Batch 981 granskar fem modifierarbeskrivningar för utjämning, ytanpassning,
förvrängning, partiklar och deformeringsburar. Den använder de etablerade
sammansättningarna *meshyta* och *meshytor* samt böjningen *en annan mesh*.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-981.po` är den samlade
manuella deltafilen för batch 957–981. Den innehåller 177
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 982 — Multires och Quadriflow

Batch 982 granskar tolv beskrivningar för Multires och
Quadriflow-ommeshning. Den normaliserar *mesh*, *basmesh*, *utmesh* och
*meshnormaler* i den tekniska verktygskontexten, men behåller Quadriflow som
funktionsnamn. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-982.po` är den samlade
manuella deltafilen för batch 957–982. Den innehåller 189
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 983 — Meshsymmetri och synlighet

Batch 983 granskar åtta verktygsbeskrivningar för Quadriflow, voxelommeshning,
UV och synlighetsfilter. Den använder *mesh*, *manifold-mesh*,
*meshsymmetri* och *meshtopologi* i respektive Blender-kontext. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-983.po` är den samlade
manuella deltafilen för batch 957–983. Den innehåller 197
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 984 — Skulptering och meshtopologi

Batch 984 granskar åtta skulpteringsbeskrivningar för tygfilter, detaljnivå,
dynamisk topologi och ytuppsättningar. Den använder *meshen* och
*meshtopologi* för Blender-datatypen, men behåller det allmänna ordet
*åtgärd* för filteroperationen. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-984.po` är den samlade
manuella deltafilen för batch 957–984. Den innehåller 205
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 985 — Ytuppsättningar och maskering

Batch 985 granskar tio skulpteringsbeskrivningar för ytuppsättningar,
masker och extraktion. Den använder *meshobjekt*, *meshen*, *meshnormaler*
och *meshöar* enligt termbasen. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-985.po` är den samlade
manuella deltafilen för batch 957–985. Den innehåller 215
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 986 — Skulpteringsverktyg för mesh

Batch 986 granskar tio verktygsbeskrivningar för filter, maskextraktion,
detaljprovtagning och trimning. Den använder *meshen*, *meshyta*,
*meshobjekt* och *meshdetalj* samt den etablerade termen *boolesk operation*.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-986.po` är den samlade
manuella deltafilen för batch 957–986. Den innehåller 225
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 987 — Skulptering och UV-projektion

Batch 987 granskar åtta strängar för trimning och UV-projektion. Den använder
*meshen* konsekvent i skulpterings- och UV-kontext och behåller den exakta
facktermen *boolesk operation*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-987.po` är den samlade
manuella deltafilen för batch 957–987. Den innehåller 233
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 988 — UV och USD-import

Batch 988 granskar nio strängar för UV-projektion, export och USD-import. Den
normaliserar *meshen*, *meshsömmar*, *meshobjekt* och *meshattribut* samt
använder Blender-verbformen *veckla ut* för UV-utveckling. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-988.po` är den samlade
manuella deltafilen för batch 957–988. Den innehåller 242
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 989 — Meshdetalj och kollision

Batch 989 granskar tio strängar för dynamisk topologi, målningshåligheter,
kollision och visningsfilter. Den använder *meshgeometri*, *meshdetalj*,
*meshen* och *meshobjekt* i enlighet med termbasen. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-989.po` är den samlade
manuella deltafilen för batch 957–989. Den innehåller 252
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 990 — Meshobjekt i objektläget

Batch 990 granskar tio UI- och felsträngar för 3D-vyn och objektläget. Den
normaliserar den konkreta Blender-objekttypen till *meshobjekt* och använder
*meshen* där själva geometridatatypen avses. Batchen är lokalt granskad, men
ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-990.po` är den samlade
manuella deltafilen för batch 957–990. Den innehåller 262
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 991 — Meshredigering och dataöverföring

Batch 991 granskar tio strängar för meshredigering, verktygsfält och
dataöverföring. Den använder konsekvent *meshen*, *meshobjekt*, *källmesh*
och *dukmesh* i deras respektive Blender-kontext. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-991.po` är den samlade
manuella deltafilen för batch 957–991. Den innehåller 272
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 992 — Meshvalidering och fel

Batch 992 granskar tio fel- och valideringssträngar för meshdata, bakning,
dataöverföring och kurvskulptering. Den använder *hörnpunkt*, *meshslinga*,
*meshar*, *meshobjekt* och *ytmesh* i den exakta Blender-kontexten. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-992.po` är den samlade
manuella deltafilen för batch 957–992. Den innehåller 282
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 993 — Mesh-, UV- och importfel

Batch 993 granskar åtta verktygs- och importfel för ytnät, UV-utveckling,
instansrealisering och filformat. Den använder *ytmesh* och *meshen* för
Blenders datatyp och behåller kod- och formatnamn som STL och USD. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-993.po` är den samlade
manuella deltafilen för batch 957–993. Den innehåller 290
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 994 — Meshsimulering och geometri

Batch 994 granskar tio strängar för vätskesimulering, modifierare och
geometrinoder. Den normaliserar *meshen*, *meshobjekt*, *meshö* och
*meshens yta*, medan *rutnät* behålls när en volymgrid faktiskt avses.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-994.po` är den samlade
manuella deltafilen för batch 957–994. Den innehåller 300
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 995 — Geometrinoders meshutdata

Batch 995 granskar sex beskrivningar och fel för meshutdata i geometri-noder.
Den använder *meshen*, *indatameshen*, *källmeshen*, *målmeshen*, *meshöar*
och *yta* enligt Blenders datamodell. `sampled` är i detta sammanhang
översatt med det svenska fackspråkliga verbet *provta*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-957-995.po` är den samlade
manuella deltafilen för batch 957–995. Den innehåller 306
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 996 — Geometrinoders meshavfasning

Batch 996 granskar fem geometri-nodsträngar för avfasning och UV-sampling.
*Mesh* behandlas konsekvent som Blenders datatyp i formerna *meshen* och
*meshens*. Batchen är lokalt granskad, men ännu inte verifierad som importerad
i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-996.po är den samlade
manuella deltafilen för batch 957–996. Den innehåller 311
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 997 — Geometrinoders meshkonvertering

Batch 997 granskar tio korta hjälprader och etiketter för geometri-noder som
delar upp, konverterar, samplar och distribuerar en mesh. Termerna *mesh*,
*källgeometri*, *punktmoln*, *UV-karta* och *densitetsrutnät* följer
Blenders etablerade datatyper och gränssnittskontext. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-997.po är den samlade
manuella deltafilen för batch 957–997. Den innehåller 321
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 998 — Geometrinoders meshredigering

Batch 998 granskar åtta noder för att dela, extrudera, vända, sammanfoga och
triangulera meshdata samt ange normaler. Den tillämpar de böjda formerna
*meshen* och *meshar* där gränssnittstexten kräver dem. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-998.po är den samlade
manuella deltafilen för batch 957–998. Den innehåller 329
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 999 — Edit Mode och meshobjekt

Batch 999 granskar sju felmeddelanden och korta verktygstexter för
Edit Mode, hörnpunkter, formnycklar och sammanslagning av meshobjekt. Den
skiljer konsekvent mellan *mesh*, *meshen*, *meshar*, *meshobjekt*,
*källmeshobjekt* och *redigeringsmesh*. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-999.po är den samlade
manuella deltafilen för batch 957–999. Den innehåller 336
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 000 — Meshobjekt och modifierare

Batch 1 000 granskar nio felmeddelanden och verktygstexter för bakning,
dataöverföring, modifierare, QuadriFlow och hörnpunktsgrupper. Den använder
*meshen*, *meshar*, *burmesh* och *mesh* i enlighet med om texten anger en
specifik instans, flera datatyper eller en datatyp i en åtgärd. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1000.po är den samlade
manuella deltafilen för batch 957–1 000. Den innehåller 344
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 001 — Skulptering och ytmesh

Batch 1 001 granskar fem synliga termer för volymkonvertering, skulptering,
ytmesh, målningsmask och målmesh. De följer Blenders datatyper och
modifierarkontext i stället för den generiska betydelsen av *mesh*. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1001.po är den samlade
manuella deltafilen för batch 957–1 001. Den innehåller 349
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 002 — Meshöar och deformering

Batch 1 002 granskar fyra modifierar- och meshdatatexter för Skin, partiklar,
Screw och Simple Deform. Den använder *meshö*, *meshar* och *meshen* där
texten hänvisar till Blenders meshdatatyp. Batchen är lokalt granskad, men
ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1002.po är den samlade
manuella deltafilen för batch 957–1 002. Den innehåller 353
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 003 — Geometrinoders meshgeneratorer

Batch 1 003 granskar tolv synliga geometri-nod- och modifierartexter för
meshgeneratorer, konvertering, triangulering och meshöar. Den bevarar
*rutnät* för volymgriddar men använder *mesh*, *meshö* och
*kuboidmesh* för Blenders meshdatatyp. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1003.po är den samlade
manuella deltafilen för batch 957–1 003. Den innehåller 365
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 004 — Mesheditering och normaler

Batch 1 004 granskar åtta synliga texter för anpassade normaler,
skulpteringsdata och Edit Mode-verktyg. Den använder *meshen* i bestämd form
och bevarar den etablerade Blender-termen *kantloop*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1004.po är den samlade
manuella deltafilen för batch 957–1 004. Den innehåller 373
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 005 — glTF- och FBX-meshexport

Batch 1 005 granskar tolv texter för glTF- och FBX-import/export, komprimering
och materialgrupper. *Mesh*, *meshar*, *meshen* och *meshobjekt* behålls som
Blender- och filformatstermer; Draco, Meshopt, gltfpack och POINTS lämnas
oförändrade som produkt- och formatnamn. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1005.po är den samlade
manuella deltafilen för batch 957–1 005. Den innehåller 385
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 006 — Meshprimitiver och Edit Mode

Batch 1 006 granskar tjugo synliga Edit Mode-texter för primitiva meshar,
meshslingor, urval, omordning och utjämning. Den etablerar och följer
*cirkelmesh*, *kubmesh*, *meshslinga*, *meshelement*, *meshen* och
*meshens*. Batchen är lokalt granskad, men ännu inte verifierad som importerad
i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1006.po är den samlade
manuella deltafilen för batch 957–1 006. Den innehåller 405
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 007 — Meshobjekt och dataöverföring

Batch 1 007 granskar arton synliga texter för objektkonvertering,
dataöverföring, Mesh Deform, UV-data och partikelkonvertering. Den
normaliserar *meshobjekt*, *målmeshar*, *meshen*, *meshar*, *meshdata* och
*meshdeformering* i den konkreta UI-kontexten. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1007.po är den samlade
manuella deltafilen för batch 957–1 007. Den innehåller 423
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 008 — QuadriFlow och meshgränser

Batch 1 008 granskar fyra QuadriFlow-texter för slumpfrön, ommeshning,
meshsymmetri och meshgränser. Termbasen har utökats med *meshgräns* och
*meshsymmetri*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1008.po är den samlade
manuella deltafilen för batch 957–1 008. Den innehåller 427
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 009 — meshsymmetri och meshkanter

Batch 1 009 granskar fem UI-texter för vågor, öppna meshkanter och
meshsymmetri längs axlarna X, Y och Z. Den följer den etablerade
projektspecifika terminologin *meshsymmetri* och *meshkanter*. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1009.po är den samlade
manuella deltafilen för batch 957–1 009. Den innehåller 432
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 010 — meshytor och Geometry Nodes

Batch 1 010 granskar åtta tekniska texter för meshytor, meshkanter och
Geometry Nodes. Den ersätter de generiska orden *nätyta* och *nätkant* med
de korrekta Blender-sammansättningarna *meshyta* och *meshkant* där källan
avser datatypen *mesh*. Batchen är lokalt granskad, men ännu inte verifierad
som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1010.po är den samlade
manuella deltafilen för batch 957–1 010. Den innehåller 440
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 011 — QuadriFlow-status och meshkanter

Batch 1 011 granskar sju texter för QuadriFlow-ommeshning, statusmeddelanden
och vinkelbaserad skärpa. Den använder *ommeshning*, *meshen*, *meshyta* och
*meshkant* enligt Blenders datamodell. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1011.po är den samlade
manuella deltafilen för batch 957–1 011. Den innehåller 447
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 012 — centrala meshmodifierare

Batch 1 012 granskar Build-modifierarens text för omvänd konstruktion. Den
konsekventa terminologin är *meshen* när funktionen arbetar på Blenders
meshtyp. Batchen är lokalt granskad, men ännu inte verifierad som importerad
i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1012.po är den samlade
manuella deltafilen för batch 957–1 012. Den innehåller 448
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 013 — Data Transfer, Multires och partikelhår

Batch 1 013 granskar tretton texter för Data Transfer, kurvors ytmesh,
Multiresolution, formnycklar och partikelhår. Den skiljer *mesh* från
*rutnät* och använder bland annat *käll- och målmeshar*, *ytmesh*, *basmesh*
och *emittermesh*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1013.po är den samlade
manuella deltafilen för batch 957–1 013. Den innehåller 461
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 014 — Geometry Nodes och meshdatatyper

Batch 1 014 granskar nitton texter för Geometry Nodes, meshcache, hårdynamik,
formnycklar och USD-export. Där källan avser Blenders datatyp används
*mesh*, exempelvis *meshen*, *ytmesh*, *basmesh* och *meshcache*, medan
simuleringsrutnät fortsatt behandlas som *rutnät*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1014.po är den samlade
manuella deltafilen för batch 957–1 014. Den innehåller 480
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 015 — shadernoder

Batch 1 015 granskar tre synliga UI-texter för linjestilar, ljus och värld.
Den normaliserar den felaktigt avstavade formen *shader-noder* till
*shadernoder* enligt projektets terminologi. Batchen är lokalt granskad, men
ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1015.po är den samlade
manuella deltafilen för batch 957–1 015. Den innehåller 483
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 016 — shader- och meshsammansättningar

Batch 1 016 granskar sjutton UI- och tekniktexter för shadernoder,
shadernodträd och Blenders meshdatatyp. Felaktigt avstavade eller uppdelade
sammansättningar har normaliserats till bland annat *shadernoder*,
*shadernodträd*, *meshobjekt*, *meshdatablock*, *meshcache*, *meshindata*
och *meshhörnpunkt*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1016.po är den samlade
manuella deltafilen för batch 957–1 016. Den innehåller 500
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 017 — meshdomäner

Batch 1 017 granskar tre UI-etiketter för meshens topologiska domäner. Den
etablerar *meshkant*, *meshyta* och *meshytehörn* där texten avser Blenders
datatyp i stället för ett vanligt nät. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1017.po är den samlade
manuella deltafilen för batch 957–1 017. Den innehåller 503
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 018 — ommeshning och volym till mesh

Batch 1 018 granskar tre modifierar- och Geometry Nodes-etiketter. Den
normaliserar *Remesh* till *Ommeshning*, *Volume to Mesh* till *Volym till
mesh* och *Mesh Deform* till *Meshdeformering*. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1018.po är den samlade
manuella deltafilen för batch 957–1 018. Den innehåller 506
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 019 — manifoldmeshar och dataöverföring

Batch 1 019 granskar två modifierartexter för skulpteringsverktygets
manifoldlösare och Data Transfer. Den använder *manifoldmeshar* och
*källmesh* i stället för de generiska formerna *manifold-nät* och *källnät*.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1019.po är den samlade
manuella deltafilen för batch 957–1 019. Den innehåller 508
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 020 — meshmodifierare och Geometry Nodes

Batch 1 020 granskar arton texter för partikelmodifierare, Shrinkwrap,
meshcache, meshdeformering och Geometry Nodes. Den normaliserar bland annat
*målmesh*, *meshkomponent*, *meshavfasning*, *meshcirkel*, *meshlinje* och
*meshens ytor*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1020.po är den samlade
manuella deltafilen för batch 957–1 020. Den innehåller 526
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 021 — meshattribut och geometri

Batch 1 021 granskar elva texter för Geometry Nodes, shaderattribut och
bildimport. Den ersätter *nät* med kontextspecifika former som
*meshgeometri*, *meshattribut*, *meshnormal*, *meshelement*, *meshdatablock*,
*meshplan* och *torusmesh*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1021.po är den samlade
manuella deltafilen för batch 957–1 021. Den innehåller 537
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 022 — mesh vid export och import

Batch 1 022 granskar nitton export- och importtexter för FBX, glTF,
Meshopt och bildplan. Den normaliserar bland annat *meshkomprimering*,
*meshförenkling*, *meshinställningar*, *meshdata*, *meshplan* och pluralen
*meshar*. Batchen är lokalt granskad, men ännu inte verifierad som importerad
i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1022.po är den samlade
manuella deltafilen för batch 957–1 022. Den innehåller 556
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 023 — meshredigering och Alembic

Batch 1 023 granskar tjugo texter för skulptering, UV-redigering och
Alembic-/OBJ-export. Den ersätter de generiska formerna med *mesh*,
*meshaxel*, *meshar* och *meshens voxelstorlek* i rätt UI- och
datatypskontext. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1023.po är den samlade
manuella deltafilen för batch 957–1 023. Den innehåller 576
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 024 — USD-export och skulptering

Batch 1 024 granskar sjutton texter för USD-/STL-export, skulptering och
inställningar. Den använder bland annat *triangulerad mesh*, *basmesh*,
*meshar*, *meshdetaljer*, *meshredigeringsläge* och *meshdata*. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1024.po är den samlade
manuella deltafilen för batch 957–1 024. Den innehåller 593
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 025 — meshfel och dataöverföring

Batch 1 025 granskar tjugo interna status- och felmeddelanden för Data
Transfer, meshredigering och voxelommeshning. Den konsekventa terminologin
är *käll- och målmeshar*, *meshdata*, *meshelement*, *manifoldmesh* och
*voxelommeshare*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1025.po är den samlade
manuella deltafilen för batch 957–1 025. Den innehåller 613
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 026 — meshruntime och Geometry Nodes

Batch 1 026 granskar tjugofyra interna fel- och statustexter för fysik,
Alembic, USD och Geometry Nodes. Den använder bland annat *meshobjekt*,
*meshredigeringsvisning*, *meshprov*, *meshtyp*, *basmesh*, *kubmesh* och
*meshinstanser*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1026.po är den samlade
manuella deltafilen för batch 957–1 026. Den innehåller 637
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 027 — meshresurser för Geometry Nodes

Batch 1 027 granskar åtta resursbeskrivningar och uttag för dynamiskt tyg,
kurvrör och manifoldkanter. Den normaliserar *meshgeometri*, *rörmesh*,
*rörmeshar*, *meshgenerering*, *meshyta* och *ytmesh*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1027.po är den samlade
manuella deltafilen för batch 957–1 027. Den innehåller 645
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 028 — kärntermer för mesh

Batch 1 028 granskar åtta UI-texter för Blenders datatyp *Mesh*, modifierare
och Geometry Nodes. Den skiljer datatypen *mesh* från beräknings- och
volymrutnät, samt normaliserar *meshobjekt*, *meshveck*, *meshar*,
*meshhörnpunkter* och *ytmesh*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1028.po är den samlade
manuella deltafilen för batch 957–1 028. Den innehåller 653
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 029 — meshåtgärder och export

Batch 1 029 granskar sex status- och åtgärdstexter för Cycles, skulptering,
Freestyle och export. Den normaliserar pluralen *meshar* och uttrycken
*meshobjekt*, *meshredigeringslägen* och *meshliknande yta*. I den konkreta
skulpteringskontexten blir den oidiomatiska åtgärden *Relax mesh* till
*Jämna ut mesh*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1029.po är den samlade
manuella deltafilen för batch 957–1 029. Den innehåller 659
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 030 — meshverktyg och UV-val

Batch 1 030 granskar elva synliga verktygsnamn och beskrivningar för
meshredigering, skulptering och UV-val. Den normaliserar bland annat
*meshstatistik*, *meshval*, *meshhörnpunkt*, *redigeringsmesh* och
*meshfilter*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1030.po är den samlade
manuella deltafilen för batch 957–1 030. Den innehåller 670
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 031 — meshåtgärder, fel och noder

Batch 1 031 granskar sjutton direkta Mesh-etiketter, feltexter och
Geometry Nodes-uttag. Den normaliserar bland annat *meshplan*, *meshtyp*,
*Meshen*, *meshdata*, *redigeringsmesh*, *Meshar* och *Ommeshning*.
Oförändrade `Mesh 1` och `Mesh 2` är avsiktliga synliga datatypsnamn.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i
Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1031.po är den samlade
manuella deltafilen för batch 957–1 031. Den innehåller 687
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 032 — meshfysik och ytnoder

Batch 1 032 granskar sju texter för tyg- och vätskefysik, interaktiva verktyg
och Geometry Nodes. Den normaliserar *meshgräns*, *dynamisk mesh*,
*meshgenerator*, *meshelement* och *mesh* i ytnodernas konkreta kontext.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1032.po är den samlade
manuella deltafilen för batch 957–1 032. Den innehåller 694
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 033 — verktyg för meshredigering

Batch 1 033 granskar tolv namn på verktyg i 3D-vyn, inklusive
extrudering, infogning, avfasning och slingklipp. Den normaliserar den
synliga Blender-datatypen till *Redigera mesh* i både huvud- och
reservverktygen. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1033.po är den samlade
manuella deltafilen för batch 957–1 033. Den innehåller 706
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 034 — fler verktyg för meshredigering

Batch 1 034 granskar sexton ytterligare verktygsnamn för meshredigering,
med motsvarande reservverktyg. Det omfattar kniv, halvering, Poly Build,
snurrning, utjämning, slumpning samt kant- och hörnpunktsglidning.
Datatypen skrivs konsekvent som *mesh*. Batchen är lokalt granskad, men
ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1034.po är den samlade
manuella deltafilen för batch 957–1 034. Den innehåller 722
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 035 — avslutande grupp 3D-meshverktyg

Batch 1 035 granskar tio återstående namn på 3D-vyverktyg för meshredigering:
krympning/breddning, tryck/dra, till sfär och rivning av region eller kant.
Datatypen skrivs konsekvent som *mesh* i både huvud- och reservverktyg.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1035.po är den samlade
manuella deltafilen för batch 957–1 035. Den innehåller 732
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 036 — meshvisning och ommeshning

Batch 1 036 granskar nio texter för Fresnel-visning, normaler, urval och
ommeshning. Den normaliserar *meshöverlägg*, *meshar*, *basmesh*,
*meshelement*, *ythörnsnormaler* och *ommeshare*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1036.po är den samlade
manuella deltafilen för batch 957–1 036. Den innehåller 741
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 037 — Action-slotar och animationsdata

Batch 1 037 granskar tio tekniska texter för Blenders formella datatyp
*Action*, dess *Action-slotar* och tillhörande animationsdata. Den skiljer
dem från vanliga åtgärder i gränssnittet och använder bland annat
*Action-slotten*, *Actionen* och *Actioner* där API- och datatypkontexten
kräver det. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1037.po är den samlade
manuella deltafilen för batch 957–1 037. Den innehåller 751
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 038 — Action-constraints och NLA

Batch 1 038 granskar arton texter för Action-constraints, NLA-remsor och
animationsdatablock. Formella Blender-begrepp skrivs som *Action*,
*Action-slot*, *Action-kanal* och *Action-spår*, medan vanliga åtgärder
lämnas orörda. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1038.po är den samlade
manuella deltafilen för batch 957–1 038. Den innehåller 769
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 039 — Action-slotars tidslinje

Batch 1 039 granskar sex texter för en Action-slots tidslinje, korrigerande
Actioner och riggstyrning. Den använder de formella datatypsnamnen *Action*
och *Action-slot* i stället för det generella ordet ”åtgärd”. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1039.po är den samlade
manuella deltafilen för batch 957–1 039. Den innehåller 775
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 040 — NLA och Action-intervall

Batch 1 040 granskar tre återstående NLA-texter om Actionens intervall,
slutbildruta och tidsskalning. Den anger uttryckligen att det är Blenders
datatyp *Action* som avses. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1040.po är den samlade
manuella deltafilen för batch 957–1 040. Den innehåller 778
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 041 — Action-operatorer och animationsdata

Batch 1 041 granskar 22 operatorer, statusmeddelanden och animationstexter
för Blenders formella *Action*-datatyp. Den normaliserar bland annat
*Actioner*, *Action-slotar*, *Action-bibliotek* och NLA-hantering, utan att
ändra vanliga gränssnittsåtgärder. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1041.po är den samlade
manuella deltafilen för batch 957–1 041. Den innehåller 800
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 042 — Action-status och NLA-felmeddelanden

Batch 1 042 granskar 31 felmeddelanden, statusrader och Outliner-/NLA-
operatorer i Blenders animationskod. Alla avser den formella datatypen
*Action* och dess *Action-slotar*, inte vanliga användaråtgärder. Batchen är
lokalt granskad, men ännu inte verifierad som importerad i Blender Translate.
Terminologilistan har samtidigt kompletterats med böjning och sammansättningar
för *Action*.

blender-ui-sv-reviewed-20261108-pending-batches-957-1042.po är den samlade
manuella deltafilen för batch 957–1 042. Den innehåller 831
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 043 — Action-RNA och API-meddelanden

Batch 1 043 granskar sexton RNA- och API-nära meddelanden om Blenders
*Action*-datatyp, *Action-slotar*, NLA-klipp och resursbaserade Actioner.
Tre dubbletter mot tidigare deltafiler uteslöts. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1043.po är den samlade
manuella deltafilen för batch 957–1 043. Den innehåller 847
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 044 — Action-slotars validering

Batch 1 044 granskar sju RNA-valideringsmeddelanden för Action-slotar,
kanalsamlingar och datablockstyper. En tidigare arkiverad dubblett uteslöts.
Batchen är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1044.po är den samlade
manuella deltafilen för batch 957–1 044. Den innehåller 854
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 045 — Action-slot vid nyckelbildssättning

Batch 1 045 granskar två meddelanden för animering och nyckelbildssättning.
I båda fallen syftar *slot* på den formella Action-datamodellen och översätts
därför som *Action-slot*, inte som den generella UI-termen *plats*. Batchen
är lokalt granskad, men ännu inte verifierad som importerad i Blender
Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1045.po är den samlade
manuella deltafilen för batch 957–1 045. Den innehåller 856
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 046 — export av Actioner

Batch 1 046 granskar tolv FBX- och glTF-exportinställningar. *Action* avser
här Blenders formella animationsdatatyp, så singularformen behålls som
*Action* och pluralformen skrivs *Actioner*. Generella användaråtgärder har
inte ändrats. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1046.po är den samlade
manuella deltafilen för batch 957–1 046. Den innehåller 868
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 047 — Actionredigeraren

Batch 1 047 granskar fem inställningar och beskrivningar kring
Actionredigeraren, Action-markörer och kopplade datablock. Den skiljer den
formella *Action*-typen från en vanlig åtgärd och använder bland annat
*Actionen*, *Actioner* och *Actionredigeraren*. Batchen är lokalt granskad,
men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1047.po är den samlade
manuella deltafilen för batch 957–1 047. Den innehåller 873
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 048 — Action-UI-etiketter

Batch 1 048 granskar fem tidigare oarkiverade etiketter för den formella
Action-datatypen: aktiv slot, datablockfilter, slothandtag, lagring i
justeringsläge och senast tilldelad slotidentifierare. Tretton närliggande
etiketter var redan identiska med tidigare granskade deltafiler och har
medvetet inte dubblerats. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1048.po är den samlade
manuella deltafilen för batch 957–1 048. Den innehåller 878
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 049 — Action-slotars status och operatörer

Batch 1 049 granskar tolv statusetiketter och operatörsmeddelanden för
Action-slotar i animation, Rigify och Outliner. Termerna är normaliserade till
*Action-slot*, *Action-slotten* och *Action-slotar*. Kodidentifierare och
platshållare är oförändrade. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1049.po är den samlade
manuella deltafilen för batch 957–1 049. Den innehåller 890
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 050 — Actioner och NLA-remsor

Batch 1 050 granskar tolv UI- och RNA-texter för Actions, Action-slotar och
NLA-remsor. Den formella Blender-datatypen normaliseras till *Action*, med
svenska böjningar som *Actionen* och *Actioner*. En *slot* i denna datamodell
skrivs konsekvent *Action-slot*. Batchen är lokalt granskad, men ännu inte
verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1050.po är den samlade
manuella deltafilen för batch 957–1 050. Den innehåller 891
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 051 — Action-begränsningar och NLA

Batch 1 051 granskar 26 strängar för formella Action-objekt i
Action-begränsningar, NLA-remsor och NLA-operatörer. Här avser *Action* alltid
Blenders animationsdatatyp och skrivs därför som *Action*, inte *åtgärd*.
Vanliga användaråtgärder lämnas orörda. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1051.po är den samlade
manuella deltafilen för batch 957–1 051. Den innehåller 917
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 052 — Actioner i UI och Rigify

Batch 1 052 granskar 17 synliga Action-texter i NLA-temat, glTF-exporten,
Pose Library, Rigify och Dope Sheet. Den gör den formella datatypen
konsekvent i både etiketter och felmeddelanden: *Action*, *Actioner* och
*Action-slotar*. Batchen är lokalt granskad, men ännu inte verifierad som
importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1052.po är den samlade
manuella deltafilen för batch 957–1 052. Den innehåller 934
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 053 — Actionredigeraren och NLA-fel

Batch 1 053 granskar 16 operatörer och felmeddelanden från Actionredigeraren,
NLA och relaterade pose- och renderingsflöden. Formella Blender-objekt skrivs
konsekvent som *Action*, *Actioner* och *Action-slot*. Batchen är lokalt
granskad, men ännu inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1053.po är den samlade
manuella deltafilen för batch 957–1 053. Den innehåller 950
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 054 — Action-slotar, export och posebibliotek

Batch 1 054 granskar 33 UI- och RNA-texter för Action-slotar, NLA-remsor,
glTF- och FBX-export samt posebiblioteket. Den behåller kod- och
kontextpekarnamn oförändrade, men normaliserar den synliga svenska texten till
*Action*, *Actioner* och *Action-slot*. Batchen är lokalt granskad, men ännu
inte verifierad som importerad i Blender Translate.

blender-ui-sv-reviewed-20261108-pending-batches-957-1054.po är den samlade
manuella deltafilen för batch 957–1 054. Den innehåller 983
översättningsposter och ryms därför inom gränsen på 1 000 strängar för en
Blender Translate-import.

## Batch 1 055 — resursbläddrarens kärntermer

Batch 1 055 granskar sju Asset Browser-termer. *Asset* avser här en Blender-
resurs och normaliseras därför till *resurs*, *resursdata*,
*resursrepresentation*, *resursetikett* och *svag resursreferens*. Batchen
hålls separat, så att den importklara samlingsfilen för batch 957–1 054 inte
överskrider 1 000 poster. Den är lokalt granskad men ännu inte verifierad som
importerad i Blender Translate.

## Batch 1 056 — resursbläddrarens åtgärder och fel

Batch 1 056 granskar tolv synliga kommandon, hjälprader och felmeddelanden
för Asset Browser. Den ersätter återstående kontextbundna former av
*tillgång* med *resurs* och lämnar API-namn, filformat och kodidentiteter
oförändrade. Batchen är lokalt granskad men ännu inte verifierad som
importerad i Blender Translate.

## Batch 1 057 — resurskataloger

Batch 1 057 granskar fem katalog- och resurskommandon i Asset Browser. Den
rättar termen *tillgång* i nodgrupps-, modifierings- och effektnodgrupps-
resurser samt gör kommandot för att rensa en resurs entydigt i singular.
Batchen är lokalt granskad men ännu inte verifierad som importerad i Blender
Translate.

## Batch 1 058 — Asset Browser RNA

Batch 1 058 granskar 20 egenskaper och hjälprader för resursmetadata,
resurshyllan och importmetoder. Den normaliserar *asset* till *resurs* i
sammanhängande Asset Browser-kontext utan att ändra API-identifierare,
protokollnamn eller formatnamn. Batchen är lokalt granskad men ännu inte
verifierad som importerad i Blender Translate.

## Batch 1 059 — resursåtkomst och import

Batch 1 059 granskar 14 inställningar och hjälprader för resursåtkomst,
katalogfilter och importmetoder. Den använder *resurs* konsekvent och
bevarar Blenders skillnad mellan lokala och nätbaserade resurser. Batchen är
lokalt granskad men ännu inte verifierad som importerad i Blender Translate.

## Batch 1 060 — resursfiler och hämtning

Batch 1 060 granskar nio drifts- och felmeddelanden för resursfiler,
fjärrlistningar och resurshämtning. Den använder *resursfil*, *resurslista*
och *resursdata* konsekvent, samtidigt som protokoll- och fältnamnen `path`,
`hash` och `size_in_bytes` lämnas oförändrade. Batchen är lokalt granskad men
ännu inte verifierad som importerad i Blender Translate.

## Batch 1 061 — resursval och kataloger

Batch 1 061 granskar fem synliga status- och åtgärdstexter i Asset Browser.
Den gör skillnaden mellan en markerad resurs, en lokal resurs och en
resurssystemfil tydlig och använder genomgående *resurs* i denna
användargränssnittskontext. Batchen är lokalt granskad men ännu inte verifierad
som importerad i Blender Translate.

## Batch 1 062 — katalogstatus

Batch 1 062 granskar de återstående korta Asset Browser-statusraderna för en
tom resurskatalog och panelrubriken för resurskataloger. Batchen är lokalt
granskad men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1062.po` samlar batch
1 055–1 062 i en separat importfil med 74 översättningsposter. Den ska
importeras separat från batch 957–1 054, som redan innehåller 983 poster.

### Avslutat delpass: Asset Browser-terminologi

Den effektiva lokala katalogen, med de arkiverade deltorna ovanpå den senaste
exporten, har kontrollerats för tidigare former av *tillgång* i Asset Browser-
och resurshyllskontext. Inga sådana former återstår. Den enda träffen är den
orelaterade etiketten *Alt-verktygstillgång*. Detta verifierar endast det
tematiska resursarbetet, inte en fullständig radgranskning av hela Blender UI.

## Batch 1 063 — Shrinkwrap-mål

Batch 1 063 rättar en regression i hjälpraden för Shrinkwraps ytterligare
målmesh. Det tidigare verbet *krympinpacka* ersätts med den terminologiskt
och idiomatiskt korrekta formuleringen *anpassas tätt till*, i enlighet med
projektets etablerade Shrinkwrap-term. Batchen är lokalt granskad men ännu
inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1063.po` samlar batch
1 055–1 063 i en separat importfil med 75 översättningsposter. Den ska
importeras separat från batch 957–1 054, som redan innehåller 983 poster.

## Batch 1 064 — modifierarnodgruppsresurser

Batch 1 064 ersätter den tidigare, mindre precisa sammansättningen
*modifieringsnodgruppsresurser*. Texten gäller resurser för nodgrupper som
används av modifierare och skrivs därför *resurser för
modifierarnodgrupper*. Den ersätter en befintlig post och ändrar inte antalet
poster i den samlade importfilen. Batchen är lokalt granskad men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1064.po` samlar batch
1 055–1 064 i en separat importfil med 75 översättningsposter. Den ska
importeras separat från batch 957–1 054, som redan innehåller 983 poster.

## Batch 1 065 — Shrinkwrap-metoder

Batch 1 065 rättar fem sammanhängande etiketter och hjälprader för
Shrinkwrap-modifierarens metodval. Den ersätter *krympinpackningsmetod* och
*krympinpacka* med *Shrinkwrap-metod* respektive *anpassa* och använder
konsekvent *mesh*, *målyta* och *målhörnpunkt*. Hunspells två träffar,
*Shrinkwrap-metod* och *meshen*, är avsiktliga Blender-facktermer. Batchen är
lokalt granskad men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1065.po` samlar batch
1 055–1 065 i en separat importfil med 80 översättningsposter. Den ska
importeras separat från batch 957–1 054, som redan innehåller 983 poster.

## Batch 1 066 — Mesh-datatyp i objektfel

Batch 1 066 rättar den tekniska Blender-datatypen *Mesh* i ett objektfel från
*nät* till *mesh*. Formateringsplatshållarna bevaras oförändrade. Batchen är
lokalt granskad men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1066.po` samlar batch
1 055–1 066 i en separat importfil med 81 översättningsposter. Den ska
importeras separat från batch 957–1 054, som redan innehåller 983 poster.

Den 8 november 2026 kördes en samlad omvalidering av denna fil med `msgfmt`,
`svlang`, `l10n-lint` och diffkontroll. `msgfmt` gav endast förväntade
headervarningar för deltafilerna; `svlang`, `l10n-lint` och diffkontrollen
passerade. De två informationsnotiserna från `l10n-lint` gäller endast
sluttecknet i två tekniska fältnamnssträngar och är inte varningar eller fel.
Hunspell gav inga träffar i batch 1 062; samlingsfilens två träffar är de
förväntade tekniska formerna `.asset.blend-fil` och *resursdatablock*.

## Batch 1 067 — Light Probe-samling

Batch 1 067 rättar Light Probe-inställningen *Invert Collection*. Den gamla
översättningen *Inverterad kollektion* var både en missvisande participform
och fel term för Blenders `Collection`. Den nya etiketten är *Invertera
samling*, vilket följer inställningens verbform och terminologins term
*samling*. Batchen är lokalt granskad men ännu inte verifierad som importerad
i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1067.po` samlar batch
1 055–1 067 i en separat importfil med 82 översättningsposter (83 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 068 — Action-slotar

Batch 1 068 rättar etiketten *Slots* i Action-systemets API-kontext. Den
tidigare formen *Åtgärdsslotar* blandade ihop det formella Blender-namnet
*Action* med det vanliga ordet *åtgärd*. I den här kontexten används nu
*Action-slotar*, i linje med Action-, NLA- och animationsdokumentationen.
Batchen är lokalt granskad men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1068.po` samlar batch
1 055–1 068 i en separat importfil med 83 översättningsposter (84 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 069 — Action-datatypens huvudetiketter

Batch 1 069 rättar huvudetiketterna *Action* och *Actions* i Dope Sheet,
NLA, Action Constraints, resursfilter och datablockslistor. Eftersom de där
betecknar Blenders formella animationsdatatyp används *Action* och
*Actioner*, inte *Åtgärd* och *Åtgärder*. Batchen är lokalt granskad men ännu
inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1069.po` samlar batch
1 055–1 069 i en separat importfil med 85 översättningsposter (86 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 070 — Library Override-data

Batch 1 070 normaliserar sju etiketter och felmeddelanden för Library
Override. Den ersätter den äldre termen *överskrivning* med *åsidosättning*
i samlingsoperatorn, Outlinerns systemåsidosättningar och dialogerna för
åsidosättningsdata. Batchen är lokalt granskad men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1070.po` samlar batch
1 055–1 070 i en separat importfil med 92 översättningsposter (93 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 071 — geometrinodmodifierarens gränssnitt

Batch 1 071 normaliserar hjälpraden för uttag i Geometry Nodes Modifier. Den
använder den etablerade sammansättningen *geometrinodmodifierare* och
formuleringen *geometrinodmodifierarens gränssnitt* i stället för den
mindre precisa omskrivningen *modifieringsgränssnittet för geometrinoder*.
Batchen är lokalt granskad men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1071.po` samlar batch
1 055–1 071 i en separat importfil med 93 översättningsposter (94 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 072 — Rigid Body-meshkälla

Batch 1 072 rättar Rigid Body-inställningen `mesh_source` och dess
hjälprad. Den tidigare allmänna översättningen *Nätkälla* ersätts med
*Meshkälla*, och den kollisionsmesh som används beskrivs som *meshen*.
Batchen är lokalt granskad men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1072.po` samlar batch
1 055–1 072 i en separat importfil med 95 översättningsposter (96 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 073 — arbetsytetermer

Batch 1 073 normaliserar fyra arbetsytesträngar. Den ersätter den äldre
synonymen *arbetsutrymme*, rättar Window-API:ts grammatiska formulering för
det aktiva vylagret och gör länknings- och raderingsmeddelandena konsekventa
med UI-termen *arbetsyta*. Batchen är lokalt granskad men ännu inte verifierad
som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1073.po` samlar batch
1 055–1 073 i en separat importfil med 99 översättningsposter (100 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 074 — visningslager

Batch 1 074 normaliserar nio View Layer-strängar från den inkonsekventa
kortformen *vylager* till projektets etablerade term *visningslager*. Passet
omfattar Window- och Scene Strip-egenskaper, exporter, Material Override och
EEVEE-inställningar. Batchen är lokalt granskad men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1074.po` samlar batch
1 055–1 074 i en separat importfil med 108 översättningsposter (109 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 075 — visningslagrets renderingssampler

Batch 1 075 avslutar den lokala sökningen efter den äldre formen *vylager*.
Den normaliserar den återstående hjälpraden för antal renderingssampler till
*visningslager*. Batchen är lokalt granskad men ännu inte verifierad som
importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1075.po` samlar batch
1 055–1 075 i en separat importfil med 109 översättningsposter (110 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Releasefärskhet

Kontrollerad 8 november 2026 mot Blenders officiella releasesida:
**Blender 5.2 LTS** uppdaterades till **5.2.3** den 22 oktober 2026. Projektet
uppfyller därmed kravet på en aktuell release inom 48 månader.

## Batch 1 076 — Node Wrangler-shadernoder

Batch 1 076 rättar Node Wranglers meny för att sammanfoga valda noder. I
denna meny avser *Shaders* uttryckligen Blender-nodtypen `ShaderNode`, inte
den allmänna processen skuggning. Översättningen är därför *Sammanfoga valda
noder med shadernoder*. Kontexten har kontrollerats mot Blenders aktuella
Node Wrangler-manual och källans `ShaderNode`-typ. Batchen är lokalt
granskad men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1076.po` samlar batch
1 055–1 076 i en separat importfil med 110 översättningsposter (111 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 077 — shadernoder och shaderuttag

Batch 1 077 gör nodterminologin konsekvent: *ShaderNode* blir
*shadernod*, ett shaderuttag skiljs från den allmänna processen
*skuggning*, och felmeddelanden anger kompletta sammansättningar som
*shadernodträd* och *geometrinodträd*. Batchen är lokalt granskad men ännu
inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1077.po` samlar batch
1 055–1 077 i en separat importfil med 114 översättningsposter (115 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 078 — kompositörens visningsnoder

Batch 1 078 skiljer konsekvent mellan en vanlig visare och Blenders
nodbaserade *Viewer*. I kompositions-, geometri- och texturkontext blir det
*visningsnod*. Den rättar även den äldre formen *kompositor* till projektets
etablerade *kompositör* för sekvenserarens Compositor-typ. Batchen är lokalt
granskad men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1078.po` samlar batch
1 055–1 078 i en separat importfil med 122 översättningsposter (123 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 079 — bildredigerarens visningsnod

Batch 1 079 rättar Image Editor-källtypen *Viewer*. Den syftar i detta
sammanhang på data från en Blender-visningsnod, inte på en människa eller en
allmän visare. Etiketten blir därför *Visningsnod*. Batchen är lokalt
granskad men ännu inte verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1079.po` samlar batch
1 055–1 079 i en separat importfil med 123 översättningsposter (124 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 080 — Geometry Nodes-visningsnod

Batch 1 080 normaliserar tre status- och hjälprader för Geometry Nodes
*Viewer*. De avser en teknisk visningsnod och blir därför *visningsnod*, inte
den personbetecknande formen *visare*. VR- och glTF-visare berörs inte.
Batchen är lokalt granskad men ännu inte verifierad som importerad i Blender
Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1080.po` samlar batch
1 055–1 080 i en separat importfil med 126 översättningsposter (127 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 081 — View Layer-åsidosättningar

Batch 1 081 normaliserar View Layer-egenskapen *Material Override* till
*materialåsidosättning* och anpassar dess Library Override-felmeddelanden.
Den vanliga filfunktionen *Overwrite* berörs inte, eftersom den korrekt
översätts med *överskrivning*. Batchen är lokalt granskad men ännu inte
verifierad som importerad i Blender Translate.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1081.po` samlar batch
1 055–1 081 i en separat importfil med 129 översättningsposter (130 med
PO-huvudet). Den ska importeras separat från batch 957–1 054, som redan
innehåller 983 poster.

## Batch 1 082–1 086 — begränsningar, manifold, F-kurvor och Action-slotar

Batch 1 082 förtydligar egenskapsnamn för begränsningar. Batch 1 083 behåller
den topologiska termen *manifold* i extruderingsverktyget i stället för den
felaktiga allmänspråkliga tolkningen *mångfald*. Batch 1 084 normaliserar
F-Modifier till *F-kurvmodifierare* i graf- och NLA-redigeraren. Batch 1 085
normaliserar två återstående formuleringar till *i stället för*. Batch 1 086
anger uttryckligen *Action-slot* i de tre återstående animationsrader där
kontexten avser datatypen, utan att ändra den delade, generella etiketten
*Slot*. Batch 1 087 ersätter den återstående API-formen *Channelbag* i
verktygstipset med den projektspecifika termen *kanalbehållare*.

Batch 1 088 bevarar skiljetecknet i Geometry Nodes-felmeddelandet för det
saknade attributet `rest_position`. Batch 1 089 skriver om UIList-hjälptexten
för `bl_idname` till idiomatisk svenska, samtidigt som klassnamn och
identifierare behålls exakt. Batch 1 090 normaliserar versaliseringen i
inställningsetiketten *I18n-grenar*. Batch 1 091 översätter Soft
Body-egenskapen *Aero* till *Aerodynamik* efter kontroll mot Blenders API,
som beskriver den som luftmotstånds- och lyftkraftspåverkan på kanter.
Batch 1 092 återställer den etablerade betydelseskillnaden mellan
*Grease Pencil drawing* som *Grease Pencil-ritning* och operatorn *Draw* som
*Rita med Grease Pencil*.
Batch 1 093 normaliserar Face Sets till *ytuppsättningar* i skulpterings-,
automaskerings- och Dyntopo-kontext samt rättar ett återstående 3D-verktyg
från *nät* till den etablerade Blender-termen *mesh*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1093.po` samlar batch
1 055–1 093 i en separat importfil med 179 översättningsposter (180 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

## Batch 1 094 — Simple Deform-modifierarens koordinatrum

Batch 1 094 rättar *modifier space* i Simple Deform från den otydliga
sammanpressade formen *modifierarutrymmet* till *modifierarens koordinatrum*.
Det är modifierarens lokala koordinatsystem, inte ett allmänt arbetsutrymme.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1094.po` samlar batch
1 055–1 094 i en separat importfil med 180 översättningsposter (181 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

## Batch 1 095–1 096 — sekvensredigeraren

Batch 1 095 normaliserar 63 löpande förekomster av *Sequencer* i Video
Sequencer- och kompositionskontext till *sekvensredigerare*. Batch 1 096 tar
de 22 återstående versaliserade etikett-, verktygs- och genitivformerna.
Bildsekvenser, filformat och API-identifierare berörs inte. Efter båda
batcherna finns inga återstående svenska UI-översättningar med den äldre
formen *sekvenserare* i den effektiva lokala katalogen.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1096.po` samlar batch
1 055–1 096 i en separat importfil med 263 översättningsposter (264 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

## Batch 1 097 — 3D-vyport

Batch 1 097 normaliserar 19 tydliga *viewport*-referenser till Blenders
etablerade UI-term *3D-vyport*. När den engelska texten avser att dölja andra
objekt under glTF-export skrivs den svenska hjälpraden explicit som
*inaktivera visning i 3D-vyporten*, så att den inte kan misstolkas som att
redigeraren ska stängas. Efter batchen finns inga kvarvarande
*viewport*-källsträngar med den svenska formen *3D-vyn* i den effektiva
lokala katalogen.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1097.po` samlar batch
1 055–1 097 i en separat importfil med 281 översättningsposter (282 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

## Batch 1 098 — meshyta, inte ansikte

Batch 1 098 rättar nio mesh- och Shrinkwrap-termer där *face* felaktigt hade
blivit *ansikte*. Mesh-elementen heter *yta*, vilket ger bland annat
*ytdata*, *ytstyrka*, *ytgallringsläge*, *ytslinga* och *ythörn*. Rigifys
*face rig* behålls som *ansiktsrigg*, eftersom det avser en rigg för ett
mänskligt ansikte och inte mesh-topologi.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1098.po` samlar batch
1 055–1 098 i en separat importfil med 290 översättningsposter (291 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

## Batch 1 099 — aktiv Action

Batch 1 099 förtydligar en Action-feltext. I denna animationskontext är
*action* Blenders formella datatyp och ska därför vara *Action*, inte den
allmänna svenska betydelsen *åtgärd*. Feltexten blir *Ingen aktiv Action att
hantera*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1099.po` samlar batch
1 055–1 099 i en separat importfil med 291 översättningsposter (292 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

## Batch 1 100 — Viewport Compositor

Batch 1 100 rättar en feltext för Blenders namngivna, interaktiva *Viewport
Compositor*. Den tidigare formen *visningsområdeskompositorn* byts till den
konsekventa termen *vyportskompositören*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1100.po` samlar batch
1 055–1 100 i en separat importfil med 292 översättningsposter (293 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Den är lokalt validerad och väntar på manuell import i Blender Translate.

Den 8 november 2026 visade användarens importresultat 351 bearbetade poster,
39 överhoppade och 312 uppdaterade. Skärmbilden anger inte entydigt vilken
lokal importfil som användes, så den kan inte användas som bevis för att den
senaste samlingsfilen 1 055–1 100 är importerad.

## Batch 1 101–1 108 — fortsatt terminologigranskning

Batcherna 1 101–1 108 fortsätter granskningen i den befintliga, lokala
Blender UI-katalogen. De normaliserar *shader* i UI- och kompileringskontext,
*Vertex Paint* till *hörnpunktsmålning*, *modifier space* till
*modifierarens koordinatrum*, *Movie Clip Editor* till *klippredigerare*,
*Sequencer* till *sekvensredigerare*, *Object Solver* till *objektlösare* och
*pivot* till *vridpunkt*. Panelrubriken *Curves Sculpt Parameter Falloff* blir
*Avtagande längs kurvparametern*. Identifierare, formatnamn och formella
produktnamn har inte ändrats.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1108.po` samlar batch
1 055–1 108 i en separat importfil med 319 översättningsposter (320 med
PO-huvudet). Alla poster har kontrollerats med `msgfmt`, `l10n-lint`,
`svlang consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks.
Filen är lokalt validerad, arkiverad och pushad till `yeager/translations`,
men väntar på manuell import i Blender Translate. Det finns fortfarande inget
verifierat importresultat för den här senaste samlingsfilen.

## Batch 1 109–1 111 — Gizmo

Batcherna 1 109–1 111 gör en konsekvent terminologigenomgång av Blenders
Gizmo-funktion. I den här produktkontexten behålls *gizmo* enligt termbasen,
med svenska böjnings- och sammansättningsformer som *gizmor*,
*gizmostorlek*, *navigeringsgizmo* och *gizmons målegenskap*. De tidigare
formerna med *manöverdon* är borttagna för Gizmo-källsträngar. Rigifys
separata UI-begrepp *Widget* behåller däremot översättningen *manöverdon*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1111.po` samlar batch
1 055–1 111 i en separat importfil med 378 översättningsposter (379 med
PO-huvudet). Den är lokalt validerad med `msgfmt`, `l10n-lint`, `svlang
consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks, arkiverad
och pushad till `yeager/translations`. Manuell import i Blender Translate är
fortfarande inte verifierad för den senaste samlingsfilen.

## Batch 1 112–1 115 — ben, koordinatrymd och normalkartor

Batch 1 112 normaliserar armaturbenens ändpunkter till *benhuvud* och
*benspets*. Batch 1 113–1 114 gör Blenders koordinattermer konsekventa:
*indexrymd*, *tangentrymd*, *objektrymd* och *världsrymd* används där
funktionerna avser en matematisk koordinatrymd, medan verkliga
koordinatsystem fortfarande beskrivs som koordinatsystem. Batch 1 115 skiljer
datatypen *normalkarta* från processen *normalkartläggning* och gör även
Shader Node Normal Maps koordinatrymd tydlig.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1115.po` är den nya
samlade importfilen för batch 1 055–1 115. Den innehåller 399 unika
översättningsposter (400 med PO-huvudet), alltså klart under Blenders gräns
på 1 000 strängar per manuell import. Den har kontrollerats med `msgfmt`,
`l10n-lint`, `svlang consistency`, riktad Hunspell-kontroll, diffkontroll och
Gitleaks, och är arkiverad samt pushad till `yeager/translations`. Manuell
import i Blender Translate är inte verifierad här; den görs av användaren.

## Batch 1 116 — RNA-områden för redigerare

Batch 1 116 granskar 26 interna RNA-etiketter för Blenders redigerare. I den
här API-kontexten betyder *Space* inte ett allmänt utrymme eller en
koordinatrymd, utan det innehåll som visas i ett redigerarområde. Etiketterna
använder därför konsekvent *område* och *områdesdata*, exempelvis
*Grafredigerarens område*, *Områdesdata för 3D-vyn* och
*Klippredigerarens område*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1116.po` är nu den
senaste samlade importfilen. Den innehåller 426 unika översättningsposter
(427 med PO-huvudet), fortfarande klart under importgränsen på 1 000
strängar. Den är lokalt validerad med `msgfmt`, `l10n-lint`, `svlang
consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks, arkiverad
och pushad till `yeager/translations`. Den manuella importen i Blender
Translate är fortfarande inte verifierad här.

## Batch 1 117–1 118 — koordinatrymd i data och rutnätsvolymer

Batch 1 117 granskar tolv data- och hjälptexter för koordinatrymder i
partiklar, drivrutiner, Grease Pencil, shadernoder och hårnycklar. Batch
1 118 tar de fyra återstående, kontextkontrollerade formerna i tangent- och
OpenVDB-rutnätsvolymer. Termerna är nu *koordinatrymd*, *tangentrymd*,
*objektrymd* och *rutnätsindexrymd*, inte de otydliga formerna med
*utrymme* eller *rum*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1118.po` är den
senaste samlade importfilen med 441 unika översättningsposter (442 med
PO-huvudet). Den är klart mindre än 1 000 strängar och har passerat
`msgfmt`, `l10n-lint`, `svlang consistency`, riktad Hunspell-kontroll,
diffkontroll och Gitleaks. Den är arkiverad och pushad till
`yeager/translations`; manuell import i Blender Translate är ännu inte
verifierad här.

## Batch 1 119 — lokal och global koordinatrymd

Batch 1 119 granskar 17 texter i mesh-, armatur-, partikel-, Rigify- och
Geometry Nodes-kontext där *local space* eller *global space* avser ett
referenssystem för transformationer. De skrivs konsekvent som *lokal
koordinatrymd* respektive *global koordinatrymd*. Identifierare som `ctrl`
och `WGT` bevaras, eftersom de är synliga Rigify-namn snarare än svenska
allmänord.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1119.po` är den
senaste samlade importfilen med 458 unika översättningsposter (459 med
PO-huvudet). Den understiger 1 000 strängar och har passerat `msgfmt`,
`l10n-lint`, `svlang consistency`, riktad Hunspell-kontroll, diffkontroll och
Gitleaks. Den är arkiverad och pushad till `yeager/translations`; manuell
import i Blender Translate är inte verifierad här.

## Batch 1 120 — SDF-avstånd i objektrymd

Batch 1 120 korrigerar den sista funna `object-space`-formen i den aktuella
effektkatalogen. SDF-ytans avstånd anges i *objektrymd*, inte det otydliga
*objektutrymme*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1120.po` är den
senaste samlade importfilen med 459 unika översättningsposter (460 med
PO-huvudet). Den är under 1 000 strängar, lokalt validerad med `msgfmt`,
`l10n-lint`, `svlang consistency`, riktad Hunspell-kontroll, diffkontroll och
Gitleaks, samt arkiverad och pushad till `yeager/translations`. Manuell
import i Blender Translate är fortfarande inte verifierad här.

## Batch 1 121 — Line Art i skärmrymd

Batch 1 121 rättar en återstående Grease Pencil Line Art-hjälptext från
*skärmkoordinatrum* till den etablerade Blender-termen *skärmrymd*. Formen
är både kortare och konsekvent med den övriga koordinatterminologin.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1121.po` är den
senaste samlade importfilen med 460 unika översättningsposter (461 med
PO-huvudet). Den är lokalt validerad med `msgfmt`, `l10n-lint`, `svlang
consistency`, riktad Hunspell-kontroll, diffkontroll och Gitleaks, arkiverad
och pushad till `yeager/translations`. Manuell import i Blender Translate är
inte verifierad här.

## Batch 1 122 — bild- och filmklippsomfång

Batch 1 122 granskar bild- och filmklippsredigerarnas statistiska *Scopes*.
UI-termen normaliseras till *omfång* och *omfångspanel*, med histogram,
vågform och vektorskop som konkret kontext. GPU-felsökningens kodterm
`scope name` berörs inte.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1122.po` är den
senaste samlade importfilen med 464 unika översättningsposter (465 med
PO-huvudet). Den har passerat `msgfmt`, `l10n-lint`, `svlang consistency`,
riktad Hunspell-kontroll, diffkontroll och Gitleaks, och är arkiverad samt
pushad till `yeager/translations`. Manuell import i Blender Translate är inte
verifierad här.

## Katalogomfattande kontroll efter batch 1 122

Den 8 november kördes en ny strukturell genomgång av den virtuellt
sammanslagna arbetskatalogen. `svlang skrivregler` rapporterade sju träffar,
men de avser Blender-källans API-kommentarer och inte `msgstr`-innehåll.
`svlang svengelska` fann endast de bokstavliga katalognamnen `startup`,
`add-ons`, `modules` och `presets` i en beskrivning av Blenders
skriptkataloglayout; dessa namn ska behållas eftersom de är verkliga
undermappar. Den breda `svlang check`-rapporten innehåller många falska
V2-träffar för UI-etiketter, tekniska namn och imperativ, och används därför
inte som automatiskt beslutsunderlag.

En ny `l10n-lint`-genomgång kontrollerades manuellt. Dess varningar gäller
avsiktligt oförändrade format- och produktnamn, svenska datum- och
decimalformer, svensk interpunktion i *t.ex.*, samt källans metadata. Inga
ytterligare säkra ändringar skapades av denna kontroll. Detta är en
katalogomfattande verktygsgranskning, inte ett påstående om att samtliga
40 427 poster har fått en ny rad-för-rad-mänsklig bedömning.

## Batch 1 123 — sekvensurklipp och Principled Hair-transmission

Batch 1 123 gör felmeddelandet för inklistring från sekvensredigeraren
idiomatiskt: det saknas en *urklippsscen med data från sekvensredigeraren*,
inte en svårtolkad konstruktion med två *från*. Den korrigerar även
Principled Hair BSDF:s transmissionskomponent. Egenskapsbeskrivningen gäller
ett fortgående ljusförlopp och använder därför presens: ljuset *överförs in i
håret*, reflekteras mot baksidan och överförs ut igen. Den separata
renderingspassbeskrivningen för redan genomlöpta strålgångar berörs inte.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1123.po` är den senaste
samlade importfilen. Den innehåller 466 `msgid`-poster inklusive PO-huvudet,
alltså 465 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den är lokalt validerad med `msgfmt`,
`l10n-lint`, `svlang consistency`, riktad Hunspell-kontroll, diffkontroll och
Gitleaks. Den är ännu inte manuellt importerad eller upstream-verifierad.

## Batch 1 124 — Grease Pencil och begränsningar

Batch 1 124 lokaliserar två engelska Blendernamn som hade lämnats kvar i
svensk synlig text. Grease Pencil-hjälptexten återanvänder den svenska
objektetiketten *Framför*, i stället för att citera *In Front*. Det generella
felmeddelandet för Follow Path följer den etablerade Blenderformen *Följ
bana-begränsning*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1124.po` är den senaste
samlade importfilen. Den innehåller 468 `msgid`-poster inklusive PO-huvudet,
alltså 467 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 125 — lökskalning för rörelsebanor

Batch 1 125 lokaliserar lägesnamnen i fem hjälptexter för rörelsebanornas
lökskalning. *Around Frame* blir *Omkring bildrutan* och *On Keyframes* blir
*Vid nyckelbildrutor*, i linje med svenska UI-etiketter. Det gör att
hjälptexterna inte längre växlar till engelska mitt i svenska meningar.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1125.po` är den senaste
samlade importfilen. Den innehåller 473 `msgid`-poster inklusive PO-huvudet,
alltså 472 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 126 — Dopebladets synliga texter

Batch 1 126 normaliserar åtta kvarvarande UI- och feltexter till den
etablerade Blendertermen *dopeblad*. Äldre *exponeringsark* och engelska
*Dope Sheet* ersätts i svensk synlig text, medan Python-identifierare som
`DOPESHEET_EDITOR` lämnas orörda.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1126.po` är den senaste
samlade importfilen. Den innehåller 481 `msgid`-poster inklusive PO-huvudet,
alltså 480 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 127 — Falsk användare och scenlinjär färg

Batch 1 127 normaliserar den funktionella Blendertermen *Fake User* till
*falsk användare*. Tidigare blandades *fejkanvändare* och *fiktiv användare*
med den etablerade benämningen, vilket gjorde samma funktion inkonsekvent i
menyer, varningar och felmeddelanden. Den normaliserar också
*Scene linear* till *scenlinjär* i färghanteringssammanhang.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1127.po` är den senaste
samlade importfilen. Den innehåller 495 `msgid`-poster inklusive PO-huvudet,
alltså 494 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 128 — Visningslager

Batch 1 128 normaliserar fem kvarvarande förekomster av *View Layer* till
*visningslager*. Formen *vylager* blandade ihop den etablerade Blendertermen
med den generiska vyn och förekom i import-, beroendegrafs- och
arbetsytekontext.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1128.po` är den senaste
samlade importfilen. Den innehåller 498 `msgid`-poster inklusive PO-huvudet,
alltså 497 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 129 — Outliner, del 1

Batch 1 129 fortsätter normaliseringen av Blenders etablerade produktnamn
*Outliner*. Åtta RNA- och operatörstexter ersätter det generiska
*översikten* med det faktiska UI-namnet, inklusive de interna
`SpaceOutliner`-beskrivningarna där *område* och *områdesdata* följer den
etablerade RNA-terminologin.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1129.po` är den senaste
samlade importfilen. Den innehåller 504 `msgid`-poster inklusive PO-huvudet,
alltså 503 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 130 — Outliner, del 2

Batch 1 130 täcker tio ytterligare Outliner-åtgärder för datablock,
biblioteksåsidosättningar, material, modifierare och objekt. Den behåller
*Outliner* som det dokumenterade UI-namnet, medan tekniska sammansättningar
som *ID-data* och *biblioteksåsidosättning* behåller sina etablerade svenska
former.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1130.po` är den senaste
samlade importfilen. Den innehåller 514 `msgid`-poster inklusive PO-huvudet,
alltså 513 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 131 — Outliner, del 3

Batch 1 131 avslutar den aktuella funna gruppen med Outliner-hjälptexter,
synkronisering, tema och felmeddelanden. Termer som *Outliner-region* och
*Outliner-synkronisering* gör komponentreferensen tydlig även i tekniska
RNA-texter.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1131.po` är den senaste
samlade importfilen. Den innehåller 536 `msgid`-poster inklusive PO-huvudet,
alltså 535 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 132 — Partikelrutnät

Batch 1 132 rättar den sista funna sammanblandningen av den tekniska
Blendertermen *grid* med nätverkstermen *nät*. Partikelsystemets *Grid
Randomness* avser partiklarnas rutnät och blir därför *Slumpmässighet i
rutnätet*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1132.po` är den senaste
samlade importfilen. Den innehåller 537 `msgid`-poster inklusive PO-huvudet,
alltså 536 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Lokal kvalitetssvepning — effektiv katalog efter batch 1 132

Den sammanslagna lokala katalogen omfattar 40 429 översättningsposter och har
0 oöversatta samt 0 fuzzy-poster enligt `msgattrib`. Skillnaden mot den
senaste lokala Blender-exportens 40 427 översatta poster beror på att två
senare källsträngar förekommer i tidigare granskade deltafiler; den säger
inte att de är importerade på servern. `msgfmt`, l10n-lint, svlang och
Hunspell har körts på aktuella deltabatcher. L10n-lints kvarvarande
informationsposter avser format-/produktnamn och metadata, inte konstaterade
oöversatta svenska UI-texter.

## Batch 1 133 — Shader-AOV

Batch 1 133 normaliserar AOV-passens UI-term. Formen `Shader AOV` blandade
isärskrivning och bindestrecksform; svensk sammansättning med förkortningen
blir *shader-AOV* i löptext och *Shader-AOV* som fristående etikett.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1133.po` är den senaste
samlade importfilen. Den innehåller 540 `msgid`-poster inklusive PO-huvudet,
alltså 539 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 134 — Renderingslager

Batch 1 134 normaliserar en kvarvarande operatörstext från *renderlager* till
den etablerade Blendertermen *renderingslager*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1134.po` är den senaste
samlade importfilen. Den innehåller 541 `msgid`-poster inklusive PO-huvudet,
alltså 540 översättningsposter och klart under Blenders gräns på 1 000
strängar per manuell import. Den väntar på lokal validering, arkivering och
manuell import.

## Batch 1 135 — Library Override-kontext

Batch 1 135 rättar en hjälpttext för kamerans bakgrundsbild. Samma koncept
benämndes först *biblioteksåsidosättning* men förkortades därefter till bara
*åsidosättningen*. Texten använder nu den fullständiga och konsekventa termen
även i den andra hänvisningen.

## Batch 1 136 — ID-biblioteksåsidosättning

Batch 1 136 normaliserar RNA-typens sammansättning. *ID Library Override
Property* är en egenskap hos en ID-biblioteksåsidosättning, inte en egenskap
hos ett ID-bibliotek. Den svenska etiketten blir därför *Egenskap för
ID-biblioteksåsidosättning*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1136.po` är den senaste
samlade manuella importfilen. Den innehåller 543 `msgid`-poster inklusive
PO-huvudet, alltså 542 översättningsposter. Den är lokalt kontrollerad och
ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 137 — 3D-vyport

Batch 1 137 skiljer den namngivna Blender-redigeraren *3D Viewport* från
generisk *viewport*. Den förra normaliseras till *3D-vyport*, medan den
generiska formen *visningsområde* lämnas orörd. Detta rättar blandade former
som *3D-visningsområde*, *3D-visningsvy* och *3D-visningsfönster*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1137.po` är den senaste
samlade manuella importfilen. Den innehåller 556 `msgid`-poster inklusive
PO-huvudet, alltså 555 översättningsposter. Den är lokalt kontrollerad och
ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 138 — 3D-vyport, uppföljning

Batch 1 138 tar de kvarvarande synliga UI- och hjälptexterna med exakt
*3D Viewport* som missades av den första sökningen på gemen form. Denna
uppföljning normaliserar fem poster till *3D-vyport* utan att påverka
generisk *viewport*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1138.po` är den senaste
samlade manuella importfilen. Den innehåller 560 `msgid`-poster inklusive
PO-huvudet, alltså 559 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 139 — Bildredigerarens provtagning

Batch 1 139 rättar två kvarvarande tangentmappningsnamn i bildredigeraren.
Det engelskpåverkade verbet *sampla* ersätts med den fastställda Blendertermen
*provta*, även i reservmappningen.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1139.po` är den senaste
samlade manuella importfilen. Den innehåller 562 `msgid`-poster inklusive
PO-huvudet, alltså 561 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 140 — Provtagningsverktyg

Batch 1 140 rättar 15 återstående interaktiva provtagningssträngar i bland
annat bildanalys, viktmålning, sekvensredigerarens förhandsgranskning,
färgpaletter och Grease Pencil. Enligt terminologin används *provta* i dessa
verktyg i stället för det engelskpåverkade *sampla*. De tekniska begreppen för
exportens animationssampling och samplade F-kurvor lämnas orörda eftersom de
beskriver lagrade samples, inte interaktiva verktygsåtgärder.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1140.po` är den senaste
samlade manuella importfilen. Den innehåller 577 `msgid`-poster inklusive
PO-huvudet, alltså 576 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 141 — Provtagningsnoder och penslar

Batch 1 141 använder *provta* i en penselbeskrivning, miljötexturens
shadermodul, Dyntopos detaljprovtagning och en UV-texturhjälptext. Det följer
den etablerade termen för noder och interaktiva bild-/penselverktyg utan att
förändra renderarens tekniska sampling.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1141.po` är den senaste
samlade manuella importfilen. Den innehåller 581 `msgid`-poster inklusive
PO-huvudet, alltså 580 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 142 — Poseringsrymd

Batch 1 142 rättar en inkonsekvent förklarande Constraint-text. Den använder
*poseringsrymden*, i enlighet med den synliga Blender-etiketten *Pose Space*
och projektets fastställda term, i stället för *poseringsutrymmet*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1142.po` är den senaste
samlade manuella importfilen. Den innehåller 582 `msgid`-poster inklusive
PO-huvudet, alltså 581 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 143 — Shadernoder

Batch 1 143 normaliserar tre synliga shadernodetiketter. Här avser *Shader*
den formella Blender-nodtypen, inte processen skuggning; terminologin anger
därför *shader* och pluralformen *shaders*. Det rättar också den felaktiga
singularformen efter *valda*.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1143.po` är den senaste
samlade manuella importfilen. Den innehåller 585 `msgid`-poster inklusive
PO-huvudet, alltså 584 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 144 — 3D-vyverktyg, del A

Batch 1 144 rättar 21 tangentmappningsetiketter för meshredigering och
skulptering från *3D-visningsverktyg* till den konsekventa formen
*3D-vyverktyg*. Formerna efter kolon är samtidigt normaliserade till vanlig
svensk gemen begynnelsebokstav, i linje med angränsande reservmappningar.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1144.po` är den senaste
samlade manuella importfilen. Den innehåller 606 `msgid`-poster inklusive
PO-huvudet, alltså 605 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Batch 1 145 — 3D-vyverktyg, del B

Batch 1 145 avslutar det lokala svepet av den äldre formen
*3D-visningsverktyg* i 26 tangentmappningsetiketter för markering,
transformering, kurvredigering och skulptering. Samtliga använder nu
*3D-vyverktyg*, och sökningen i den sammanslagna lokala katalogen hittar inga
kvarvarande poster med den äldre formen.

`blender-ui-sv-reviewed-20261108-pending-batches-1055-1145.po` är den senaste
samlade manuella importfilen. Den innehåller 632 `msgid`-poster inklusive
PO-huvudet, alltså 631 unika översättningsposter. Den är lokalt kontrollerad
och ligger under gränsen på 1 000 strängar, men dess importstatus på Blender
Translate är inte verifierad här.

## Deltafil — senaste 24 timmarna

`blender-ui-sv-reviewed-20261108-changes-last24h.po` sammanför de 194
granskade Blender-deltabatcher som lades till i Git-historiken under de
senaste 24 timmarna vid filens skapande. Nyare batchar prioriteras när samma
källsträng förekommer i flera delbatcher. Filen innehåller 1 586 `msgid`-
poster inklusive PO-huvudet, alltså 1 585 unika översättningsposter. Den är
avsedd som en komplett lokal översikt över periodens ändringar, inte som en
enda Blender Translate-uppladdning eftersom den överskrider 1 000 strängar.

För manuell import finns samma perioddelta delat utan överlappning i
`blender-ui-sv-reviewed-20261108-changes-last24h-part-1.po` med 800
översättningsposter och
`blender-ui-sv-reviewed-20261108-changes-last24h-part-2.po` med 784
översättningsposter. Båda filerna ligger under uppladdningsgränsen; deras
importstatus på Blender Translate är inte verifierad här.

Batch 626 normaliserar koordinatrymd i tillgångsnoden *Screen to 3D Space*.
Den använder *skärmrymd* och *3D-rymd* konsekvent i nodnamnet och dess
beskrivning. Deltafilen
`blender-ui-sv-reviewed-20261108-batch-626-screen-to-3d-space.po` är lokalt
kontrollerad, arkiverad och väntar på manuell import till Blender Translate.

## Deltafiler — äldre än 24 timmar

Den 8 november skapades en separat lokal importuppsättning från 965
arkiverade Blender UI-filer vars senaste Git-ändring låg före den exakta
24-timmarsgränsen. När samma identitet förekom flera gånger prioriterades den
senaste äldre måltexten. Alla identiteter i
`blender-ui-sv-reviewed-20261108-changes-last24h*.po` exkluderades därefter
på `msgctxt`/`msgid`-nivå. Resultatet omfattar 8 490 äldre
översättningsposter och är delat utan överlappning i nio filer:
`blender-ui-sv-reviewed-20261108-changes-older-than-24h-part-01-of-09.po`
till `part-09-of-09.po`. Del 1–8 innehåller 1 000 poster vardera och del 9
innehåller 490 poster. Filerna är lokalt kontrollerade men deras
importstatus på Blender Translate är inte verifierad här.

## Verifiering mot användarhämtad export den 8 november

Användaren hämtade en ny Blender UI-export med filnamnet
`blender-ui-ui-sv (5).po`; dess lokala tidsstämpel är 8 november 2026
09:03:52. En skrivskyddad jämförelse mot de nio äldre deltadelarna och de
två 24-timmarsdelarna gjordes lokalt med identiteten `msgctxt`/`msgid` och
måltexten som jämförelsenyckel. De elva deltafilerna innehåller tillsammans
10 074 unika poster. Av dem förekommer 9 742 med exakt samma svenska måltext
i den hämtade exporten, 332 finns inte i exporten och ingen förekommande post
har en avvikande måltext.

Detta är verifierad förekomst i den användarhämtade exportfilen, inte ett
verifierat Blender Translate-importresultat: det finns inget kopplat
serverkvitto som anger vilken deltafil som importerades, antal uppdaterade
eller eventuell granskningsstatus. De 332 saknade posterna behandlas därför
som katalogskillnader tills en serverrapport eller en senare export ger mer
precis evidens. Användarens rapporterade uppladdning och den lokala
exportjämförelsen hålls därmed åtskilda.

## Batch 1 146 — Nyckelbildrutor och Action-data

Batch 1 146 normaliserar 23 oarkiverade UI- och hjälptexter för
nyckelbildrutor, F-kurvor, Keying Set, glTF/FBX-export och konvertering av
Actions. Den ersätter engelska *keyframe(s)* och den förkortade formen
*nyckelram(ar)* med *nyckelbildruta/-rutor*, inklusive den etablerade
sammansättningen *nyckelbildruteanimering*. Där *Action* uttryckligen är
Blenders datatyp bevaras namnet med stor bokstav, även i texten om att
konvertera en äldre Action till en skiktad Action. Denna avgränsning följer
terminologilistan och ändrar inte API-identifierare.

Deltafilen
`blender-ui-sv-reviewed-20261108-batch-1146-keyframe-action-terminology.po`
innehåller 23 poster (24 inklusive PO-huvudet), ligger under
uppladdningsgränsen och väntar på lokal QA, arkivering och manuell import i
Blender Translate.

## Batch 1 147 — Visningslager

Batch 1 147 normaliserar 26 oarkiverade UI- och hjälptexter för Blenders
*View Layer*. De använder konsekvent *visningslager* med korrekta böjningar i
Outlinern, sceninställningarna, renderingen, nodredigeraren och cacheläsning.
Även närliggande imperativ och samlingsnamn har rättats, till exempel *Rensa
maskeringen* och *Maskera samlingen*. Batchen förtydligar den redan belagda
terminologiposten men ändrar inte API-identifieraren `ViewLayer`.

Deltafilen
`blender-ui-sv-reviewed-20261108-batch-1147-view-layer-terminology.po`
innehåller 26 poster (27 inklusive PO-huvudet), har passerat `msgfmt`,
l10n-lint, svlang, Hunspell-kandidatsökning och diffkontroll och väntar på
arkivering samt manuell import i Blender Translate.

## Batch 1 149 — Kameravyer och beskärning

Batch 1 149 granskar 20 oarkiverade statusetiketter och hjälprader för
kameror, 3D-vyer och kameraspårning. Den gör riktningarna i ortografiska och
perspektiviska vyer idiomatiska, exempelvis *Ortografisk vy framifrån* och
*Perspektivisk vy från höger*. Den normaliserar även *kamerarymd* och
*beskärningsavstånd* i teknisk kamerakontext; *kamerarum* och *klippavstånd*
används inte. Terminologilistan har utökats med dessa återkommande termer.

Deltafilen
`blender-ui-sv-reviewed-20261108-batch-1149-camera-view-terminology.po`
innehåller 20 poster (21 inklusive PO-huvudet) och har passerat `msgfmt`,
l10n-lint, svlang, Hunspell-kandidatsökning och diffkontroll. Den väntar på
arkivering och manuell import i Blender Translate.

## Batch 1 150 — Bildrute- och förhandsgranskningsintervall

Batch 1 150 granskar åtta oarkiverade poster för uppspelning, animation och
förhandsgranskning. Den använder konsekvent *bildruta* och
*bildruteintervall* i stället för den tvetydiga formen *bild*, samt rättar
den felaktiga åtgärdsetiketten *Nodförhandsgranskning* till *Ta bort
förhandsgranskning*. Befintliga termposter för bildrute- och
förhandsgranskningsintervall räcker; ingen ny term har lagts till.

`blender-ui-sv-reviewed-20261108-batch-1150-frame-range-preview.po`
innehåller åtta poster (nio inklusive PO-huvudet), har passerat `msgfmt`,
l10n-lint, svlang, Hunspell-kandidatsökning, diffkontroll och Gitleaks. Den
är arkiverad och pushad i commit `0b87677d`; någon import till Blender
Translate är inte verifierad.

## Batch 1 151 — Tangentkonfigurationer och inställningar

Batch 1 151 granskar arton oarkiverade UI- och hjälpposter för Blenders
tangentkonfigurationer, tangentmappningar och närliggande
inställningsåtgärder. Den ersätter engelska och bokstavliga former som
*keyconfig*, *KeyConfigs*, *nyckelkartor* och *modal knappsats* med
*tangentkonfiguration*, *tangentmappning* och deras korrekta svenska
böjningar. Den rättar även två UI-etiketter till gemener samt åtgärden för att
kopiera inställningar för studioljus. Terminologilistan förtydligar att
API-namnet *KeyConfig* översätts i synlig UI-text.

`blender-ui-sv-reviewed-20261108-batch-1151-keymap-configuration.po`
innehåller arton poster (nitton inklusive PO-huvudet). Den har passerat
`msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning, diffkontroll och
Gitleaks, och är arkiverad och pushad i commit `8f45e373`. Någon import till
Blender Translate är inte verifierad.

## Batch 1 152 — Filbläddraren

Batch 1 152 granskar tretton oarkiverade poster i filbläddraren. Den ersätter
felöversättningar av snabbmenyn *Specials*, resursrensning och
katalogsökvägar, normaliserar *resursbläddring* och *filbläddrare* samt gör
listan över senast använda mappar idiomatisk. Terminologilistan fastställer
*senast använd mapp* för en enskild post i den listan.

`blender-ui-sv-reviewed-20261108-batch-1152-file-browser-terminology.po`
innehåller tretton poster (fjorton inklusive PO-huvudet), har passerat
`msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning, diffkontroll och
Gitleaks, och är arkiverad och pushad i commit `2f48995c`. Någon import till
Blender Translate är inte verifierad.

## Batch 1 252–1 257 — Action och gränssnittsterminologi

Sex små, kontextgranskade deltafiler korrigerar sammanlagt fjorton aktuella
Blender UI-strängar. De täcker den formella animationstypen *Action* och dess
slotar, kommandot *Baka Action*, mesh-flaggan *markerade kanter*, den
redigerarspecifika regionen *Sidofält* samt rubriker, vyetiketter och
nyckeluppsättningar. Ändringarna är avgränsade från vanliga generiska
betydelser av *action* och från användargenererade taggar.

Alla sex filer har passerat `msgfmt`, l10n-lint, svlang, hunspell-sv,
diffkontroll och Gitleaks. De är arkiverade och pushade i commits `2827b1dc`,
`8163c769`, `8af49123`, `74e29b4d`, `e4f428dc` och `600a8044`.
`swedish-tm` är uppdaterad för de nya måltexterna där TM:n tidigare innehöll
den äldre formuleringen. Den samlade importfilen
`blender-ui-sv-reviewed-import-20261108-batches-1252-1257.po` innehåller alla
fjorton strängar och har SHA-256
`5dc896e98ec401c8bc65ff6371aa4ad9a043ae0a77a96cf3735753ce1e6958d1`.

Ingen Weblate-import av dessa batcher är verifierad. De ska därför räknas som
lokalt färdiga och arkiverade, inte som upstream-inskickade, tills ett
importresultat visar antal uppdaterade, hoppade över och saknade strängar.

## Batch 1 258–1 259 — Kärnterminologi och intern datamarkering

Batch 1 258 korrigerar nio kontextbundna kärntermer: bland annat
*Benomslutning*, *punktcache för mjukkropp*, *Ommeshningsmodifierare*,
*kurvdeformeringsmodifierare*, *Voronoi-sprickmönster* och
*Stereoskopisk 3D*. Samtidigt rättades åtta äldre Blender-poster i
`swedish-tm`; redan korrekt *Linjekonst* behölls. Batch 1 259 skiljer den
interna API-flaggan `bpy.types.ID.tag` (*märka data*) från synliga
användarskapade taggar. Terminologilistan har den uttryckliga regeln så att
dessa två betydelser inte blandas ihop.

Alla kontroller passerade: `msgfmt`, l10n-lint, svlang (konsekvens,
skrivregler och svengelska), Hunspell-kandidatsökning, diffkontroll och
Gitleaks. Deltafilerna är arkiverade och pushade i commits `267509db` och
`c919f26b`; TM-uppdateringen är pushad i `swedish-tm`-commit `9df3557`.
Importfilen `blender-ui-sv-reviewed-import-20261108-batches-1258-1259.po`
innehåller tio unika poster och har SHA-256
`d59c3932957dbd53f3ca8ba6382bc09a023f5b7ac80628f5ac96bf3a71c8b5cf`.

Ingen Weblate-import av batch 1 258–1 259 är verifierad här. De är lokalt
färdiga, arkiverade och redo för manuell import, men inte upstream-inskickade
förrän importresultatet är bekräftat.

## Batch 1 260 — Hair Nodes-guidekurvor

Fyra Hair Nodes-poster från `node_geo_interpolate_curves.cc` blandade den
projektetablerade termen *guidekurva* med *styrkurva*. Batchen normaliserar
gruppen, interpoleringsbeskrivningen och de två närmaste guidekurvorna till
*guidekurva*. Terminologilistan förtydligar också att `Guide Group ID` skrivs
*guidekurvsgrupp-ID*.

Deltafilen `blender-ui-sv-reviewed-batch-1260-hair-guide-curves.po` innehåller
fyra poster och har SHA-256
`21ae94dc156afe32bcd3772ee6af8ea58d52013ba7a15223a15dea651ddb26a0`.
Den har passerat `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks. Den är arkiverad och pushad i commit `0f78885e`.
De fyra felaktiga TM-posterna är rättade och pushade i `swedish-tm`-commit
`8f5b2be`.

Ingen Weblate-import av batch 1 260 är verifierad. Den är lokalt färdig och
redo för manuell import, men inte upstream-inskickad förrän importresultatet
är bekräftat.

## Batch 1 261 — Hair Nodes-hårinfästning

Tre poster från nodgruppen *Attach Hair Curves to Surface* normaliserar
`Snap` till den etablerade Blender-termen *fäst* och anger att den befintliga
fästningen i denna nodkontext är en *hårinfästning*. Deltafilen
`blender-ui-sv-reviewed-batch-1261-hair-attachment.po` innehåller tre poster
och har SHA-256
`2f8057c124c96568c29a9ae00f252adf545cb0f5069378db414abed496f30f90`.

Alla kontroller passerade: `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks. Batchen är arkiverad och pushad i commit `a31ee460`.
TM-ändringen är pushad i `swedish-tm`-commit `03fe674`. Ingen Weblate-import
är verifierad; batchen är lokalt färdig och redo för manuell import.

## Batch 1 262 — Hair Nodes-guidekurvbeskrivning

En specifik beskrivning i `node_geo_interpolate_curves.cc` använde *guider*
i stället för den etablerade Hair Nodes-termen *guidekurvor*. Deltafilen
`blender-ui-sv-reviewed-batch-1262-hair-guide-description.po` innehåller en
post och har SHA-256
`7058eecc25776e702e126b484ae4c8fcb2d43bf872a14c31eb8dc5abb9622b7e`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är arkiverad och pushad i commit
`edc0e674`; TM-ändringen är pushad i `swedish-tm`-commit `e8096db`.
Ingen Weblate-import är verifierad; batchen är lokalt färdig och redo för
manuell import.

## Batch 1 264 — Sidofält

En separat `Sidebar`-post för Blenders UI-region i bland annat 3D-vyns
snabbmeny normaliserar *Sidopanel* till etablerade *Sidofält*. Deltafilen
`blender-ui-sv-reviewed-batch-1264-sidebar.po` innehåller en post och har
SHA-256 `590a7b34534c4ef30f67dddab37f2b973b7e1baac513b2eb9eb5763a57e19866`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är arkiverad och pushad i commit
`a5e9376a`. Ingen Weblate-import är verifierad; batchen är lokalt färdig och
redo för manuell import.

## Samlad import — batch 1 263–1 265

`blender-ui-sv-reviewed-import-20261108-batches-1263-1265.po` samlar åtta
unika UI-poster från batch 1 263–1 265 i en importbar deltafil. Den innehåller
inte hela Blender-katalogen och har SHA-256
`0fc507e95da4d21cf5122a93e8af48d76615ba03189e227cd0f450425e74ead3`.
Filen har verifierats med `msgfmt`, l10n-lint, svlang, diffkontroll och
Gitleaks, och är arkiverad och pushad i commit `74558e4e`.

Importstatus: redo för manuell Weblate-import; inget importresultat är
verifierat här.

## Samlad import — batch 1 271–1 274

`blender-ui-sv-reviewed-import-20261108-batches-1271-1274.po` samlar åtta
kontextgranskade UI-poster: transformation, metaklot, tomt objekt, mjukkropp,
underytsspridning, lökskal och viktmålning. Filen är en deltafil, inte en
fullständig Blender-export, och har SHA-256
`b2ac849a2e6befa19759446d7e8e41b6d642862d1e584b17a98775807477476b`.

`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Importfilen
och statusuppdateringen arkiverades och pushades i `yeager/translations` som
commit `a433fe51`. Importresultat i Blender Translate är inte verifierat av
arkivet. De fem entydiga generella termparen synkroniserades även till
`swedish-tm` (PO och TMX) i commit `1ea601c`; kontrollverktygets okända
sammansättningar *mjukkropp* och *underytsspridning* bedömdes manuellt som
korrekta Blender-termer.

## Batch 1 266 — Kompositör

I den nod- och 3D-vykontext där `Compositor` betyder Blenders
kompositör ersätts den äldre formen *kompositerare* med *kompositör*.
Deltafilen `blender-ui-sv-reviewed-batch-1266-compositor.po` innehåller en
post och har SHA-256
`b429f97931d2ba34d332de081cbb014a384971190099f5ed214b31f17f475280`.

Samma dag normaliserades tre historiska Blender-segment i `swedish-tm` från
*Kompositor* respektive oöversatta *Compositor* till *Kompositör*, efter
kontroll mot aktuell UI-, operatörs- och sekvenskontext. TM-uppdateringen
publicerades i `yeager/swedish-tm` som commit `7451ba7`; den innebär ingen
ytterligare import till Blender Translate.

## Batch 1 268 — Transformationsbegränsning

Batch 1 268 granskar etiketten för Blenders Transform-begränsning i objekt-
och posekontext. Den engelska formen *Transformation* får den etablerade
svenska Blender-termen *Transformation*, i linje med projektets befintliga
terminologi för position, rotation och skala. Deltafilen
`blender-ui-sv-reviewed-batch-1268-transformation-constraint.po` innehåller
en post och har SHA-256
`41e58b666457a8908660f57fb569e428af7c665b6ce0c2420f7c24bb09af52bc`.
Den är lokalt validerad men inte verifierad som importerad i Blender
Translate. Det historiska Blender-segmentet i `swedish-tm` normaliserades
samtidigt från *Transformering* till *Transformation* i commit `cb8f457`.

## Batch 1 269 — Voronoi Crackle

Batch 1 269 granskar beskrivningen av den äldre brusbasen *Voronoi Crackle*.
Den överflödiga upprepningen av *Voronoi* ersätts med den kortare och tydliga
formen *Brusalgoritm – spräckande Voronoi: tessellering med skarpa kanter*.
Tekniknamnet *Voronoi* bevaras. Deltafilen
`blender-ui-sv-reviewed-batch-1269-voronoi-crackle.po` innehåller en post och
har SHA-256
`53865b87a47c2eed2dcb9b3729aaf64ba336ddc8a208637c169ccd0d60f513a2`.
Den är lokalt validerad men ännu inte verifierad som importerad i Blender
Translate. Motsvarande Blender-segment i `swedish-tm` uppdaterades i commit
`e18096a`.

## Batch 1 270 — gammal biblioteksfil

Batch 1 270 granskar felmeddelandet vid länkning eller tillägg från ett
gammalt `.blend`-filformat. Den informella formen *lib-filen* ersätts med
projekttermen *biblioteksfilen*, och källans utropstecken bevaras. Deltafilen
`blender-ui-sv-reviewed-batch-1270-library-linking-message.po` innehåller en
post och har SHA-256
`e352c5fb6518c093a91e749034ab830f628edcb1883ab96459b2f6c41b28b9bf`.
Den är lokalt validerad men ännu inte verifierad som importerad i Blender
Translate. Motsvarande segment i `swedish-tm` uppdaterades i commit
`c084ad7`.

Importfilen `blender-ui-sv-reviewed-import-20261108-batches-1268-1270.po`
samlar batch 1 268–1 270 i tre poster för manuell Blender Translate-import.
Den är lokalt validerad men saknar fortfarande verifierat importresultat.

## Batch 1 332 — resurshyllans huvudrad

Batch 1 332 rättar regionetiketten *Asset Shelf Header* från den inkonsekventa
formen *Tillgångshyllans huvud* till *Resurshyllans huvudrad*. Översättningen
följer den etablerade termen *resurshylla* och skiljer UI-regionens huvudrad
från en dokumentrubrik. Deltafilen
`blender-ui-sv-reviewed-batch-1332-asset-shelf-header.po` innehåller en post
och har SHA-256
`47246cdfe33ae6896d933baaefdafbc268ccaa60bb47fdf2a121d70de18807b6`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv och Gitleaks passerade. Batchen är
lokalt färdig och arkiverad för manuell Blender Translate-import; inget
importresultat är ännu verifierat.

## Batch 1 333 — resurshyllans ID-beskrivning

Batch 1 333 normaliserar den återstående *asset*-referensen i
`AssetShelf.bl_idname`: *tillgången* blir *resursen*, i linje med synliga
Blender-etiketter som *resurshylla* och *resursbibliotek*. Kodnamn som
`OBJECT_AST_hello` och `bl_idname` lämnas naturligtvis oförändrade.
Deltafilen `blender-ui-sv-reviewed-batch-1333-asset-shelf-id.po` innehåller en
post och har SHA-256
`14c2332119a67b08434c6ec2ef088f06c4fcf10bb894d0d2aae1046a5e631813`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv och Gitleaks passerade. Batchen är
lokalt färdig och redo för manuell Blender Translate-import; inget
importresultat är ännu verifierat.

## Batch 1 271 — transformation och metaklot

Batch 1 271 normaliserar två separata UI-kontexter enligt Blenders
terminologifil: Geometry Nodes-etiketten *Transform* blir *Transformation*,
och datablockfiltret *Metaball* blir *Metaklot*. Deltafilen
`blender-ui-sv-reviewed-batch-1271-transform-and-metaball.po` innehåller två
poster och har SHA-256
`59f9f9e08b856d656a6ca2c3a927063e7fc4b2f84bacd2ef624cf28a7a92b85e`.
Den är lokalt validerad men ännu inte verifierad som importerad i Blender
Translate.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är arkiverad och pushad i den
verifierade committen `a8730dbb`. Den kontextberoende UI-deltan gav ingen
separat direkt TM-post; de entydiga Blender-termerna synkroniserades senare
samlat i `swedish-tm`-commit `1ea601c`. Ingen Weblate-import är verifierad;
batchen är lokalt färdig och redo för manuell import.

## Batch 1 265 — UI-regioner och animering

Tre etablerade begrepp normaliseras i den aktuella exporten:
*verktygsrubrik*, *fyrdelad vy* och *nyckeluppsättning*. Deltafilen
`blender-ui-sv-reviewed-batch-1265-ui-regions-animation.po` innehåller tre
poster och har SHA-256
`64570cf9d96b1768df0fb87148f74db25c5f782142dfbf9ce664b2993670da28`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är arkiverad och pushad i commit
`e7c135ce`. Ingen Weblate-import är verifierad; batchen är lokalt färdig och
redo för manuell import.

## Samlad import — batch 1 260–1 262

`blender-ui-sv-reviewed-import-20261108-batches-1260-1262.po` samlar de åtta
unika Hair Nodes-posterna i batch 1 260–1 262 i en importbar deltafil. Den
innehåller inte hela Blender-katalogen och har SHA-256
`dc76fd2740273a735cb1376b8f707a69d491f24395a8d3855b7c9369392636f0`.
Filen har verifierats med `msgfmt`, l10n-lint, svlang, diffkontroll och
Gitleaks, och är arkiverad och pushad i commit `7a33a7c2`.

Importstatus: redo för manuell Weblate-import; inget importresultat är
verifierat här.

## Batch 1 263 — 3D-vy: fästning

Fyra `space_view3d`-etiketter rättar den inkonsekventa termen *snäpp* till
*fäst/fästmål*, enligt Blenders etablerade betydelse för 3D-transformering.
Batchen ändrar inte sequencerns tidsbaserade snäppning. Deltafilen
`blender-ui-sv-reviewed-batch-1263-view3d-snapping.po` innehåller fyra poster
och har SHA-256
`e9cca2c215ee12c2f4868c3b9187b5d80e51135a6a73b1c88c583ab62e748059`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är arkiverad och pushad i commit
`265a0297`; TM-ändringen är pushad i `swedish-tm`-commit `31a85f8`.
Ingen Weblate-import är verifierad; batchen är lokalt färdig och redo för
manuell import.

## Batch 1 340 — Action-slotars handtag och identifierare

Batch 1 340 rättar fem återstående texter i Blenders Action-datamodell. Den
formella typen skrivs konsekvent *Action-slot*, medan *Action Slot Handle*
översätts till *Handtag för Action-slot*. Därmed undviks den krystade och
inkonsekventa sammansättningen *Action-slothandtag*. Vanliga slotar i exempelvis
material och noder omfattas inte.

Deltafilen `blender-ui-sv-reviewed-batch-1340-action-slot-handles.po`
innehåller fem poster och har SHA-256
`9eb9db22729203a2ded11e6732a1ea52cab8b699400a0ec47aa3e78796498a1e`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-sv kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och arkiverad
för manuell Blender Translate-import; inget importresultat är ännu verifierat.

## Batch 1 341 — F-kurvor för Action-slot

Batch 1 341 rättar en återstående kanalbeskrivning i Action-datamodellen.
Här avser *slot* uttryckligen den formella typen som animeras av F-kurvor,
alltså *Action-slotten*, inte en generell slot. Deltafilen
`blender-ui-sv-reviewed-batch-1341-action-slot-fcurve.po` innehåller en post
och har SHA-256
`c58fdaabf6af31470b941c79e838bf591110873682cd612174f68678240b511e`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-sv kandidatsökning,
diffkontroll och Gitleaks passerade. Batchen är lokalt färdig och arkiverad
för manuell Blender Translate-import; inget importresultat är ännu verifierat.

## Batch 1 342 — Action som datatyp

Batch 1 342 rättar två hjälptexter som avser Blenders formella
animationsdatatyp *Action*. Formen *åtgärden* ersätts därför med *Actionen*.
Vanliga användaråtgärder, exempelvis tangent- och musåtgärder, ingår inte i
ändringen. Deltafilen
`blender-ui-sv-reviewed-batch-1342-action-datatype-terms.po` innehåller två
poster och har SHA-256
`7a191e5d71536faafb1e7d8f0af5aa461d8d94ea3ef72140c1cdbc97e33846f0`.

Kontrollerna `msgfmt`, l10n-lint, svlang, Hunspell-sv kandidatsökning,
diffkontroll och Gitleaks passerade. Hunspell-sv markerar produktens formella
egennamn *Actionen*, vilket är en medveten projektspecifik term. Batchen är
lokalt färdig och arkiverad för manuell Blender Translate-import; inget
importresultat är ännu verifierat.

## Samlad import — batch 1 340–1 342

`blender-ui-sv-reviewed-manual-import-20261109-batches-1340-1342.po` samlar
åtta unika och radgranskade Action-/Action-slot-ändringar från batch 1 340–
1 342. Det är en deltafil, inte en full Blender-katalog, och den ligger långt
under Blender Translates rekommenderade gräns på 1 000 strängar per import.
SHA-256 är
`5992d73671b3f32733d461fc3a3fd56558bb80ca82b21e7c549079aec615a781`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv kandidatsökning, diffkontroll och
Gitleaks passerade. Filen är redo för manuell import; inget importresultat är
verifierat här.

## Manuell Blender Translate-import — 9 november 2026

En användarverifierad Blender Translate-import rapporterade **213 behandlade
strängar**, varav **111 uppdaterades**, **102 hoppades över** och **0 saknades**.
Resultatet visar att importen accepterade de matchande posterna utan saknade
källsträngar. Skärmbilden identifierar däremot inte vilka enskilda arkiverade
deltafiler som ingick, så den används inte som belägg för att en viss batch är
upstream-aktuell. Nya eller ännu ej matchade deltafiler behåller därför statusen
*redo för manuell import* tills deras eget resultat kan verifieras.

## Batch 1 343 — cachekatalog för nedladdning

En systeminställning för fjärranslutna resursbibliotek har normaliserats från
*cachekatalogen för nedladdningar* till den idiomatiska och mer precisa
*cachekatalogen för nedladdning*. Batchen innehåller en radgranskad post i
`blender-ui-sv-reviewed-batch-1343-download-cache-directory.po` och har
SHA-256 `4726a1369fdae05e26587321af82d2b5a5c419a7fe412f95f4e734b2e0e1bc2f`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade. Deltafilen är lokalt färdig och redo för manuell import; något
importresultat för just denna post är ännu inte verifierat.

## Lokal granskningsbas — 9 november 2026

Den nedladdade helfilen `blender-ui-ui-sv (5).po` är äldre än flera
arkiverade granskningsdeltan. Den lokala granskningsbasen byggs därför genom
att låta de **393** arkiverade deltafilerna få företräde framför helfilen. Den
resulterande arbetskopian innehåller **40 427** faktiska strängar och används
för fortsatt kontroll; den arkiveras inte som importfil.

`msgfmt`, l10n-lint, svlang konsistenskontroll och Gitleaks har körts på den
sammanslagna kopian. De kvarvarande l10n-lint-varningarna är under fortsatt
manuell bedömning; hittills verifierade exempel är formel-/platshållartext,
filnamnsexempel med *t.ex.* och avsiktliga dubbla fackord, inte säkra
massändringar.

## Batch 1 344 — biblioteksåsidosättning i Constraint

En kvarvarande äldre form, *biblioteksöverskrivning*, rättas i RNA-hjälptexten
för `Constraint.is_override_data`. Här avser *local override* uttryckligen
Blenders **Library Override**-funktion, därför används den etablerade termen
*lokal biblioteksåsidosättning* och den kortare hänvisningen
*åsidosättningen* i följdsatsen.

Deltafilen `blender-ui-sv-reviewed-batch-1344-library-override-constraint.po`
innehåller en radgranskad post och har SHA-256
`edd2d6cee41652263297e846ffd281c6ee55ea7372dd3b31c260fe853c30e036`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade för deltafilen. Den är redo för manuell import; dess eget
importresultat är ännu inte verifierat.

## Nästa samlade import — batch 1 370–1 373

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1373.po` ersätter
den tidigare samlingsfilen för batch 1 370–1 372. Den omfattar elva unika,
radgranskade poster: ActionChannelbags-syftning, hela UI-termen *Sequencer
Scene* samt kompositeringsnodgrupper för sekvensredigeraren. SHA-256 är
`3a97b02b106970305857c0c2bed35f4fc751c2174c68bb6340ebc3cd51b82fc1`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar; dess
importresultat är ännu inte verifierat.

## Nästa samlade import — batch 1 370–1 374

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1374.po` ersätter
den tidigare samlingsfilen för batch 1 370–1 373. Den omfattar tretton unika,
radgranskade poster: ActionChannelbags-syftning, UI-termen *Sequencer Scene*
och konsekvent svenska för kompositeringsnoder. SHA-256 är
`aec060ed8a511bd04e3294e2c37f30b552e6a9d0e2f71d93537951d10ad818ed`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar; dess
importresultat är ännu inte verifierat.

## Nästa samlade import — batch 1 370–1 375

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1375.po` ersätter
den tidigare samlingsfilen för batch 1 370–1 374. Den omfattar femton unika,
radgranskade poster: ActionChannelbags-syftning, UI-termen *Sequencer Scene*
och normaliserad terminologi för kompositeringsnoder och deras gruppnoder.
SHA-256 är `4c462eb384da0f594950a4b5f1bbfa2ab0c56725057fa10fda3639e2d25ad5cd`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar; dess
importresultat är ännu inte verifierat.

## Nästa samlade import — batch 1 370–1 376

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1376.po` ersätter
den tidigare samlingsfilen för batch 1 370–1 375. Den omfattar tjugo unika,
radgranskade poster: ActionChannelbags-syftning, UI-termen *Sequencer Scene*,
kompositeringsnoder samt avgränsad renderterminologi. SHA-256 är
`9340a8f620b7c8cf60d582e47e850b9ef56ab58c461a95fcd79bafca03611b85`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar; dess
importresultat är ännu inte verifierat.

## Nästa samlade import — batch 1 370–1 377

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1377.po` ersätter
den tidigare samlingsfilen för batch 1 370–1 376. Den omfattar 23 unika,
radgranskade poster: ActionChannelbags-syftning, UI-termen *Sequencer Scene*,
kompositeringsnoder, renderterminologi och koordinattermen *screen space*.
SHA-256 är `cb8a93cda42105b9b4644b35522671892a06b1f2c287363ffcf1f9a69aab6a26`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar; dess
importresultat är ännu inte verifierat.

## Katalogkontroll — senaste lokala underlag

Den senaste tillgängliga Blender UI-katalogen,
`Downloads/blender-ui-ui-sv (6).po`, har 40 427 översatta poster. `msgfmt`
och l10n-lint passerar katalogen utan träffar. Svlang ger sju
interpunktionsmarkeringar, samtliga i oförändrade bokstavliga koduttryck som
`(dot(B, C) < 0) ? A : -A`; de är inte svensk löptext och har därför inte
ändrats. Den här kontrollen bekräftar endast katalogens maskinella formalia,
inte att alla 40 427 poster är mänskligt slutgranskade.

## Batch 1 373 — återstående sekvensredigerarscener

Tre återstående referenser till samma *Sequencer Scene*-datablock använde
den oenhetliga formen *sekvensredigeringsscen* i en Workbench-inställning och
två OTIO-felmeddelanden. De normaliseras till den dokumenterade UI-termen
*sekvensredigerarscen*.

`blender-ui-sv-reviewed-batch-1373-sequencer-scene-consistency-20261109.po`
innehåller tre radgranskade poster med SHA-256
`a0d5fd98c6ace441e1d1246b9e1e6b9a34adb540c7acdd4913333706d31acd66`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Batchen är redo för manuell import; importresultatet är inte
verifierat.

## Samlad import — batch 1 343–1 344

`blender-ui-sv-reviewed-manual-import-20261109-batches-1343-1344.po` samlar
de två senast granskade, ännu inte individuellt verifierade ändringarna:
*cachekatalog för nedladdning* och *lokal biblioteksåsidosättning*. Det är en
deltafil med två poster och SHA-256
`5faed48bda1e33b687e4d2f0b5e0ad58eb84445603db3ed0f96f737fea84f539`.

`msgfmt`, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks
passerade. Filen är redo för manuell Blender Translate-import och innehåller
inga tidigare batchar.

## Batch 1 345 — shadernoder i AOV-utdata

Hjälptexten för nodtypen `ShaderNodeOutputAOV` avser uttryckligen utdata från
*shader nodes*. Den tidigare formen *skuggningsnoder* blandade ihop den
formella Blender-nodtypen med den vidare processen *skuggning*. Den rättas
till den etablerade termen *shadernoder*.

Deltafilen `blender-ui-sv-reviewed-batch-1345-shader-node-aov.po` innehåller
en radgranskad post och har SHA-256
`647dee6ec6debf2f45c5244020c564a055a69527041955721116e057c8cb6d70`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
saknar den korrekta projektspecifika sammansättningen `shadernoder`; den är
manuellt verifierad mot Blenders terminologi. Deltafilen är redo för manuell
import; något importresultat för just denna post är ännu inte verifierat.

## Batch 1 346 — shadernoder i färgrymdshjälptext

Färghanteringshjälptexten räknar upp tre konkreta Blender-nodtyper:
kompositerings-, shader- och geometrinoder. Formen *skuggningsnoder* ersätts
med *shadernoder*, eftersom det här är ett tekniskt namn på nodtypen och inte
en beskrivning av renderingsprocessen.

Deltafilen `blender-ui-sv-reviewed-batch-1346-color-space-node-types.po`
innehåller en radgranskad post och har SHA-256
`1a692afd8f2bf17375aa3dc1608ed9706e0d409fd1a0a0480bd67539e87ec40b`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
markerar den avsiktliga projektspecifika termen `shader`; den är verifierad i
den lokala Blender-terminologin. Deltafilen är redo för manuell import; dess
eget importresultat är ännu inte verifierat.

## Batch 1 348 — heltalsvektornoduttag

RNA-typen `NodeSocketIntVector` var den enda av syskonens grundtyper som
bröt mönstret `…noduttag`. Den omskrivna formen *heltalsvektoruttag för nod*
normaliseras till det konsekventa formella typnamnet *heltalsvektornoduttag*.

Deltafilen `blender-ui-sv-reviewed-batch-1348-integer-vector-node-socket.po`
innehåller en radgranskad post och har SHA-256
`0033882d12e4e2cf6cec3fd7c7cf4d6a8dba711aa482f1d4d65d919f513b83ac`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
saknar den korrekta facktermen `heltalsvektornoduttag`; termen är manuellt
verifierad mot närliggande Blender-typer och projektets terminologilista.
Deltafilen är redo för manuell import; dess eget importresultat är ännu inte
verifierat.

## Samlad import — batch 1 343–1 346

`blender-ui-sv-reviewed-manual-import-20261109-batches-1343-1346.po` samlar
fyra unika, radgranskade och ännu inte individuellt verifierade ändringar:
cachekatalog för nedladdning, biblioteksåsidosättning och två kontextspecifika
användningar av *shadernod*. Det är en deltafil med fyra poster, inte en
helkatalog, och den ligger långt under importgränsen på 1 000 strängar.
SHA-256 är
`5ff0e712105aecbf3a49acd362f1b95fd172e3cc314df49c5271580748938ad2`.

`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Filen är
redo för manuell Blender Translate-import; inget importresultat för dess fyra
poster är ännu verifierat.

## Batch 1 347 — shadernoder i förhandsgranskningsinställning

Inställningen `node_preview_resolution` styr förhandsgranskningar av den
formella nodtypen *Shader Node*. Den missvisande och inkonsekventa formen
*skuggarnoder* rättas därför till *shadernoder*.

Deltafilen `blender-ui-sv-reviewed-batch-1347-shader-node-preview-resolution.po`
innehåller en radgranskad post och har SHA-256
`215b45feab159f67ae37ec173ccc9e587e7d725aa1e3d3d3e3d1981f07e52255`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Hunspell-sv
markerar den avsiktliga projektspecifika sammansättningen `shadernoder`; den
är verifierad i Blender-terminologin. Deltafilen är redo för manuell import;
dess eget importresultat är ännu inte verifierat.

## Samlad import — batch 1 343–1 347

`blender-ui-sv-reviewed-manual-import-20261109-batches-1343-1347.po` ersätter
den tidigare samlade filen 1 343–1 346 när en enda importfil önskas. Den
innehåller fem unika, radgranskade och ännu inte individuellt verifierade
poster; den tidigare filen ligger kvar som ett oförändrat arkivunderlag.
SHA-256 är
`fdf2c804c5536aba79d219be82612236226eabe531e22a49b3f5ded12041a20d`.

`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Filen är
redo för manuell Blender Translate-import och ligger långt under 1 000
strängar; något importresultat för dess poster är ännu inte verifierat.

## Batch 1 370 — Action-kanalbehållarens syftning

ActionChannelbags-beskrivningen avslutades med den överlastade formuleringen
*avsedda för den slotten*. Eftersom *Action-slot* redan står i samma sats ger
pronomenet *den* en tydligare och mer idiomatisk svensk referens utan att
förändra Blenders term.

`blender-ui-sv-reviewed-batch-1370-action-channelbag-pronoun-20261109.po`
innehåller en radgranskad post med SHA-256
`a1673a4fcb06ee390a4b25805d8b63cbc521d33637f2f3dc7276915aca2e5836`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar bara engelsk källtext och PO-metadata.
Deltafilen är redo för manuell import; importresultatet är inte verifierat.

## Verifierad import — 38 ändringar sedan 07:00

Den 9 november bekräftades importen av
`blender-ui-sv-reviewed-since-0700-20261109-complete-v2.po` i Blender
Translate: **38 behandlade, 38 uppdaterade, 0 hoppade över och 0 saknade**.
Detta verifierar uppladdningen av de 38 deduplicerade posterna i samlingsfilen;
det är inte en generell markering av hela UI-katalogen som mänskligt granskad.

## Batch 1 371 — sekvensredigerarscen

Blenders manual beskriver *Sequencer Scene* som det särskilda scen-datablock
som innehåller redigeringen i Videosekvensredigeraren. Fyra UI-poster växlade
mellan *sekvenserscen*, *sekvensredigeringsscen* och den redan etablerade
formen *sekvensredigerarscen*. De normaliseras till den senare formen.

`blender-ui-sv-reviewed-batch-1371-sequencer-scene-terminology-20261109.po`
innehåller fyra radgranskade poster med SHA-256
`cdc05ab4d009f7d62f652e23c6aa77eb517ae6f4a00968b28efa099343954d14`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar bara engelsk källtext, API-namn och
PO-metadata. Batchen är redo för manuell import; importresultatet är inte
verifierat.

## Nästa samlade import — batch 1 370–1 371

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1371.po` samlar
fem nya, deduplicerade poster efter den verifierade 38-strängarsimporten:
en ActionChannelbags-formulering och fyra konsekventa UI-termer för
*Sequencer Scene*. SHA-256 är
`d32256943e9c48f876cc2882d99e8f4f82f887ce5cc2c86dcfb1175fe8db3014`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar. Den är redo
för manuell import; importresultatet är inte verifierat.

## Nästa samlade import — batch 1 370–1 372

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1372.po` ersätter
den tidigare samlingsfilen för batch 1 370–1 371. Den omfattar åtta unika,
radgranskade poster: ActionChannelbags-syftning, *Sequencer Scene* och
kompositeringsnodgrupper för sekvensredigeraren. SHA-256 är
`42bff427f73238af56b373d13eaab528ae856f4b8ce21cd84473156ad5ce15a1`.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Filen ligger långt under gränsen på 1 000 strängar; dess
importresultat är ännu inte verifierat.

## Batch 1 372 — kompositeringsnodgrupper i sekvensredigeraren

Blenders API beskriver dessa som *compositor node groups for sequencer*.
Tre rader blandade tidigare ihop den synliga miljön *Kompositör* med den
tekniska nodtypen. De använder nu *kompositeringsnodgrupp* respektive
*kompositeringsnoder*, i linje med projektets terminologi och Blender-manualens
beskrivning av kompositeringsnodgrupper i Videosekvensredigeraren.

`blender-ui-sv-reviewed-batch-1372-sequencer-compositing-node-groups-20261109.po`
innehåller tre radgranskade poster med SHA-256
`e481767d62ec2ba083d31b43459e099ca8e77b8e610c730063c4f9a7531c7bba`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast engelsk källtext, API-namn och
PO-metadata. Batchen är redo för manuell import; importresultatet är inte
verifierat.

## Samlad import — ändringar sedan 07:00 den 9 november

`blender-ui-sv-reviewed-since-0700-20261109-complete-v2.po` är en
deduplicerad importfil med 38 källmatchade poster från batch 1 353–1 359 och
1 362–1 368. Den tidigare samlingsfilen för batch 1 361 tas inte med, eftersom
den bara sammanfattar samma poster. Senare, mer specifika rättningar har
företräde när en sträng förekommer i flera batcher.

`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar enbart engelsk källtext, Blender-API-namn och
PO-metadata. Filen innehåller 38 strängar och ligger långt under Blenders
gräns på 1 000 strängar per import. Importresultatet är inte verifierat.

## Batch 1 364 — Dope Sheet-termer

Fyra återstående synliga formuleringar blandade den engelska arbetsbeteckningen
*Dopesheet* med den etablerade svenska UI-termen *Dopeblad*. De rättas till
*dopeblad*, *dopebladet*, *dopebladssortering* och *dopebladskanaler* enligt
omgivande UI- och animeringskontext. Python-identifierare lämnas orörda.

`blender-ui-sv-reviewed-batch-1364-dopeblad-terminology-20261109.po`
innehåller fyra radgranskade poster och har SHA-256
`903ad089a0f4e66700e4eb8b2d633f8edfc827342818b257d914c6d5de0e161d`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar tekniska källord och metadatarader i
deltafilen, men ingen svensk felstavning i de ändrade formuleringarna.
Deltafilen är redo för manuell import; dess importresultat är inte verifierat.

## Batch 1 365 — booleska värden i hjälptexter

Två hjälptexter hade kvar engelska booleska ord i i övrigt svensk löpande text.
De blir *falskt* och *sant*. Källornas Python-namn och andra identifierare
ändras inte.

`blender-ui-sv-reviewed-batch-1365-boolean-helptext-20261109.po` innehåller
två radgranskade poster och har SHA-256
`73478c24fb785013b800e80055a3da14065a4ef7f5c3fd3bf6f0e4601057de09`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, konsistenskontroll,
källmatchning och Gitleaks passerade. Hunspell-sv markerar endast tekniska
källord och PO-metadata, inte de svenska ändringarna. Filen är redo för manuell
import; dess importresultat är inte verifierat.

## Batch 1 366 — renderingsupplösning för proxy

I egenskapen `proxy_render_size` syftar *full render* på den fullständiga
renderingen i stället för en proxyupplösning. Den tidigare formen
*full återgivning* blandade ihop processens etablerade term med
visningsbetydelsen. Den rättas till *fullständig rendering*.

`blender-ui-sv-reviewed-batch-1366-proxy-render-terminology-20261109.po`
innehåller en radgranskad post och har SHA-256
`0eb0dcbb3b999698281b81d57667ccf8f49db753e2f81b1f6a07cb9be9c80f47`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, konsistenskontroll,
källmatchning och Gitleaks passerade. Hunspell-sv markerar endast källord
och PO-metadata. Deltafilen är redo för manuell import; importresultatet är
inte verifierat.

## Batch 1 367 — automatisk paketering

Tre synliga texter för samma Blenderfunktion växlade mellan det engelska
*Auto-Pack*, *automatisk packning* och den redan använda termen
*automatisk paketering av resurser*. De normaliseras till
*automatisk paketering*. Kodnamnet `use_autopack` berörs inte.

`blender-ui-sv-reviewed-batch-1367-autopack-terminology-20261109.po`
innehåller tre radgranskade poster och har SHA-256
`b7894726bac182e9591ca3bc6143299325bffc34023eb1ea4595b3addc01dd78`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, konsistenskontroll,
källmatchning och Gitleaks passerade. Hunspell-sv markerar endast engelska
källord och PO-metadata. Deltafilen är redo för manuell import; dess
importresultat är inte verifierat.

## Batch 1 368 — Action-slotfilter

Dope Sheets filter `show_only_slot_of_active_object` avser uttryckligen en
Action-slot, vilket den närliggande hjälptexten redan säger. Den korta
etiketten normaliseras från det otydliga *slot* till *Action-slot*.

`blender-ui-sv-reviewed-batch-1368-action-slot-filter-20261109.po`
innehåller en radgranskad post och har SHA-256
`4719c2f6349b0ddf1f3657a185d0ae83362f1423824d5b6c1fede50cd3a09f1f`.
`msgfmt`, l10n-lint, svlang, Hunspell-sv, konsistenskontroll,
källmatchning och Gitleaks passerade. Hunspell-sv markerar endast källord och
PO-metadata. Deltafilen är redo för manuell import; importresultatet är inte
verifierat.

## Samlad import — batch 1 362–1 367

`blender-ui-sv-reviewed-manual-import-20261109-batches-1362-1367.po`
samlar 16 unika, radgranskade poster: HDR-enheten *nit*, Dope Sheet-termer,
booleska hjälptexter, proxyrendering och automatisk paketering. Den ersätter
inte enskilda arkivfiler, utan är en praktisk importfil för Blender Translate.

SHA-256 är
`d96896143734b450758d540953dc2717021a89e9136ad18fa98a29adb8b529aa`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen har 16 poster och ligger långt under 1 000-strängarsgränsen.
Importresultatet för den samlade filen är inte verifierat.

## Batch 1 362 — HDR-enheten nit

Två beskrivningar av Rec.2100-visningar hade den engelska pluralformen
`nits`, trots att de andra HDR-posterna konsekvent använder den svenska
enhetsformen `nit`. Båda rättas utan att ändra färgrymdsnamn, siffror eller
annan UI-kontext.

`blender-ui-sv-reviewed-batch-1362-hdr-unit-terminology-20261109.po`
innehåller de två radgranskade posterna och har SHA-256
`cdfafe6720df8090e3f4847df86a6ed14e9b1266250f562642d33db2a3beda2a`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Hunspell-sv markerar projekt- och färgrymdsnamn, men ingen felstavning i de
ändrade formuleringarna. Deltafilen är redo för manuell import och omfattas
inte av något verifierat importresultat ännu.

## Batch 1 363 — HDR-etiketter med nit

Fyra återstående OCIO-etiketter för ACES använde `nits` trots samma svenska
enhetspolicy som övriga HDR-etiketter. De normaliseras till `nit`; ACES,
Rec.2100, HDR och färghanteringskontexten lämnas oförändrade.

`blender-ui-sv-reviewed-batch-1363-hdr-unit-labels-20261109.po` omfattar fyra
radgranskade poster och har SHA-256
`15dd13a9a1448c8340b967abeb7f36a9fa834203e6c5984d025d2c54290d7e4c`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Den är redo för manuell import; importen är inte verifierad.

## Batch 1 349 — kompositeringsnoder och nodgrupper

Tre UI-poster använde den oetablerade förkortningen *kompositnod* trots att
de uttryckligen avser nodtypen eller en nodgrupp för *compositing*. De
normaliseras till *kompositeringsnod* respektive *kompositeringsnodgrupp*.
Korrigeringen omfattar en operatörsrubrik, dess beskrivning och hjälpraden för
aktiv visarnod.

Deltafilen `blender-ui-sv-reviewed-batch-1349-compositing-node-terms.po`
innehåller tre radgranskade poster och har SHA-256
`17eb2a2e4566ee350c5112e637c8f5c1ed3bb697ae02e232a272893213034743`.
`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Blender-TM
synkroniseras med samma kontextbundna terminologi. Deltafilen är redo för
manuell import; dess eget importresultat är ännu inte verifierat.

## Samlad import — batch 1 343–1 349

`blender-ui-sv-reviewed-manual-import-20261109-batches-1343-1349.po` ersätter
samlad import 1 343–1 348 när en enda importfil önskas. Den innehåller nio
unika, radgranskade och ännu inte individuellt verifierade poster. SHA-256 är
`2844249cb6867b050b0007270d222a58edbd69fdb03a22f633296901f5fda77c`.

`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Filen är
redo för manuell Blender Translate-import och ligger långt under 1 000
strängar; något importresultat för dess poster är ännu inte verifierat.

## Samlad import — batch 1 343–1 348

`blender-ui-sv-reviewed-manual-import-20261109-batches-1343-1348.po` ersätter
samlad import 1 343–1 347 när en enda importfil önskas. Den innehåller sex
unika, radgranskade och ännu inte individuellt verifierade poster; äldre
samfiler ligger kvar oförändrade som arkivunderlag. SHA-256 är
`229865630748284df6c4783a1db3a44978664e4e24c209057e0ffc173e5c64f1`.

`msgfmt`, l10n-lint, svlang, diffkontroll och Gitleaks passerade. Filen är
redo för manuell Blender Translate-import och ligger långt under 1 000
strängar; något importresultat för dess poster är ännu inte verifierat.

## Batch 1 378 — Object Solver-begränsningar

Två åtgärdstexter för *Object Solver Constraint* hade återgått till engelska
funktionsnamnet i den svenska beskrivningen, trots att själva UI-namnet och
projektets terminologi använder *objektlösare* och *objektlösarbegränsning*.
De normaliseras till *Rensa inverskorrigering för objektlösarbegränsning* och
*Ange inverskorrigering för objektlösarbegränsning*.

`blender-ui-sv-reviewed-batch-1378-object-solver-constraint-20261109.po`
innehåller två radgranskade poster. SHA-256 är
`08def66f8a7d740da50310490633a84e5f34f1681d6d98ca63cec2f818c77888`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar enbart tekniska källord och PO-metadata.
Filen är redo för manuell import; importresultatet är ännu inte verifierat.

## Samlad import — batch 1 370–1 378

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1378.po` ersätter
den tidigare samlade 1 370–1 377-filen när samtliga ännu ej importverifierade
ändringar ska laddas upp tillsammans. Den innehåller 25 unika,
radgranskade poster och har SHA-256
`5be7281b0937e7f501b7466379aeb776851ef2cc6757a834c9c97424c251e862`.

Samtliga 25 poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och
Gitleaks passerade; standardvarningarna från `msgfmt` gäller enbart avsiktligt
minimal PO-metadata. Filen omfattar långt färre än 1 000 strängar och är redo
för manuell import. Importresultat för dessa 25 poster är inte verifierat.

## Batch 1 379 — konsekvent Action-slot

Två animationsbeskrivningar använde den avkortade formen *slotten* trots att
de enligt källan avser en `action slot`. Blenders dokumenterade svenska UI-term
är *Action-slot*, och därför används konsekvent *Action-slotten* även i löpande
hjälptext.

`blender-ui-sv-reviewed-batch-1379-action-slot-consistency-20261109.po`
innehåller två radgranskade poster. SHA-256 är
`0269015719393d1f09cd69b7ead0e0c6de9487f8c971aeef180d0c69e2f62777`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll, källmatchning och Gitleaks
passerade. Hunspell-sv markerar endast PO-metadata och tekniska källord.
Filen är redo för manuell import; importresultatet är ännu inte verifierat.

## Samlad import — batch 1 370–1 379

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1379.po` ersätter
den samlade 1 370–1 378-filen om alla ännu ej importverifierade ändringar ska
laddas upp tillsammans. Den innehåller 26 unika radgranskade poster och har
SHA-256 `a2f5fd3785b36b40b490135c451c0bca24a8a1e527ba4cbabe45f275ce9eadbf`.

Alla 26 poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. De förväntade `msgfmt`-varningarna gäller bara minimal PO-metadata.
Filen är långt under 1 000-strängarsgränsen och redo för manuell import;
importresultatet är inte verifierat.

## Batch 1 389 — planspår

I filmspårning är *Plane Track* ett spår för en plan yta i bildmaterialet,
inte ett spår för ett flygplan. MovieClip-etiketten normaliseras därför från
*Flygplansspår* till den etablerade termen **planspår**.

`blender-ui-sv-reviewed-batch-1389-plane-track-20261109.po` innehåller en
radgranskad post med SHA-256
`bc6166a2bd1d1ee87b2c8227e48c1c458cf1e962c384a185e2bca0c8de575c6c`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Filen är redo för manuell import;
importresultatet är inte verifierat.

## Batch 1 390 — Color Dodge

Blenders blandningsläge *Color Dodge* följer etablerad svensk grafikterminologi
med **Färgskugga**. Nodvarianten hade avvikelsen *Färgundvikning* och
normaliseras därför utan att ändra blandningslägets funktion.

`blender-ui-sv-reviewed-batch-1390-color-dodge-20261109.po` innehåller en
radgranskad post med SHA-256
`873f75faf0627b40d5f857f5af2f6136fb3240789fdb3c4e83346f6d853ecba9`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll, Hunspell-sv och Gitleaks passerade. Filen är redo för
manuell import; importresultatet är inte verifierat.

## Batch 1 388 — instanssamling

Operatörsetiketten *Instance Collection* var felaktigt särskriven som
*Instans Samling*, trots att den intilliggande beskrivningen använder verbet
*instansiera* och samma UI-katalog redan har termen *Instanssamling*.

`blender-ui-sv-reviewed-batch-1388-instance-collection-20261109.po`
innehåller en radgranskad post med SHA-256
`110dbd00f2191141a64b345d1bc6eecf721a724351a55ac231da3b24bbec93ad`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Filen är redo för manuell import;
importresultatet är inte verifierat.

## Batch 1 387 — tidsommappning

Blenders panel *Time Remapping* i modifieraren Mesh Cache styr hur den
cachelagrade animationens tid tolkas och spelas upp. Tidigare blandades
*Omtidning*, *tidsomappning* och *tidsommappning* i UI:t. Den korrekta
termen är **tidsommappning**: det är en ommappning av tiden, inte en allmän
ändring av tid. Tre berörda UI- och hjälprader har därför normaliserats.

`blender-ui-sv-reviewed-batch-1387-time-remapping-20261109.po` innehåller
tre radgranskade poster med SHA-256
`e3458a70eb7633f95e24e2e0f7891d13ee4c25b5745db5a2edbf7c65269b0a0d`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar den
projektspecifika sammansättningen *tidsommappning* samt metadata och
källord, men inga svenska stavfel identifierades. Filen är redo för manuell
import; importresultatet är inte verifierat.

## Batch 1 380 — ladda om remsor

Sequencerns korta åtgärdsetikett hade formuleringen *Läs in remsor igen*.
Övriga Blender-åtgärder, dess egen beskrivning och den närliggande etiketten
*Reload Strips and Adjust Length* använder konsekvent *Ladda om remsor*.
Den korta etiketten normaliseras därför till samma vedertagna UI-form.

`blender-ui-sv-reviewed-batch-1380-reload-strips-20261109.po` omfattar en
radgranskad post med kontexten `Operator`. SHA-256 är
`2001ac1b802f7dec4520b30e1958aa73ad8410dd9058ceb08eb0bbabf82dd41c`.
Källmatchning, `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Hunspell-sv rapporterar endast avsiktliga metadata- och källord.
Filen är redo för manuell import; importen är inte verifierad.

## Samlad import — batch 1 370–1 380

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1380.po` ersätter
den tidigare 1 370–1 379-filen vid en samlad manuell import. Den innehåller
27 unika radgranskade poster och har SHA-256
`400704612e4ddad45bca8e687832798e0ec810840999c718859acfae0d263384`.
Samtliga 27 poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade; `msgfmt` varnar enbart för det minimala deltahuvudet. Filen är långt
under 1 000 strängar och redo för manuell import. Importresultatet är inte
verifierat.

## Batch 1 381 — deltatransformering

En egenskap i slumpningsverktyget innehöll stavfelet
*deltatranformeringsvärden*. Sammansättningen ska följa Blenders etablerade
term *transformering* och rättas till *deltatransformeringsvärden*.

`blender-ui-sv-reviewed-batch-1381-delta-transform-spelling-20261109.po`
innehåller en radgranskad post med SHA-256
`019915e02d96725db30a15657ce45a1dda786952239f80b9916df7ea24d8d899`.
Källmatchning, `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Hunspell-sv rapporterar endast avsiktliga metadata- och källord.
Filen är redo för manuell import; importen är inte verifierad.

## Samlad import — batch 1 370–1 381

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1381.po` ersätter
den samlade 1 370–1 380-filen vid en manuell import. Den innehåller 28 unika
radgranskade poster och har SHA-256
`9a6d378e83e87538676685c32d95bfd04ac980645a4edff4685cfe2a2d7772cc`.
Samtliga poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade; `msgfmt`-varningarna gäller endast minimal delta-PO-metadata.
Filen är långt under 1 000 strängar och redo för manuell import.
Importresultatet är inte verifierat.

## Batch 1 382 — sekvensredigeraren

Åtgärden *Refresh the sequencer editor* hade den dubblerade formen
*sekvensredigerarredigeraren*. Den normaliseras till den etablerade
UI-termen *sekvensredigeraren*.

`blender-ui-sv-reviewed-batch-1382-sequencer-editor-duplication-20261109.po`
innehåller en radgranskad post med SHA-256
`5cb023e241c30289352ec098c7a2827c976ec2e1d9c6315a20217419f0b905ea`.
Källmatchning, `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Hunspell-sv markerar bara metadata- och källord. Filen är redo för
manuell import; importen är inte verifierad.

## Samlad import — batch 1 370–1 382

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1382.po` ersätter
den samlade 1 370–1 381-filen vid en manuell import. Den innehåller 29 unika
radgranskade poster och har SHA-256
`89108e071c70787fb239bb4a8206ae4cd21212397f846f560c69ab8b3ac324bc`.
Samtliga poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade; `msgfmt`-varningarna gäller endast minimal delta-PO-metadata. Filen
är långt under 1 000 strängar och redo för manuell import. Importresultatet är
inte verifierat.

## Batch 1 383 — remsor i sekvensredigeraren

Fem etiketter och beskrivningar använde de tunglästa formerna
*sekvensredigerarremsa/-remsor*. De uttrycker samma väldefinierade Blender-
begrepp som *Sequencer Strips* och skrivs därför konsekvent som *remsa* eller
*remsor i sekvensredigeraren*. Ändringen bevarar den tekniska betydelsen men
gör gränssnittstexten mer idiomatisk och följer terminologilistan.

`blender-ui-sv-reviewed-batch-1383-sequencer-strip-phrasing-20261109.po`
innehåller fem radgranskade poster med SHA-256
`f0f6334b13580f52fb92a09cd4dd75697d0a17823edfa2136e994dba87ec042c`.
Källmatchning, `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Hunspell-sv markerar tekniska källord, metadata och projektspecifika
sammansättningar; inga svenska stavfel identifierades i de fem måltexterna.
Filen är redo för manuell import; importen är inte verifierad.

## Samlad import — batch 1 370–1 383

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1383.po` ersätter
den samlade 1 370–1 382-filen vid en manuell import. Den innehåller 34 unika
radgranskade poster och har SHA-256
`5d072bd707755354f6d8f95a6d6782dd8347488aaa721c4a766f5d070feee343`.
Samtliga poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Den är långt under gränsen på 1 000 strängar och redo för manuell
import. Importresultatet är inte verifierat.

## Batch 1 384 — Kink i partikelhår

Blenders dokumentation beskriver *Kink* som formen på barnpartiklar i hår,
med varianter som lock, våg och fläta. Projektets terminologi fastställer
**nyck** för denna särskilda partikelterm. Två kvarvarande UI-etiketter med
*krökning* respektive *krustyp* normaliseras därför till **nyck** och
**nycktyp**. Övriga förekomster var redan korrekta och ändras inte.

`blender-ui-sv-reviewed-batch-1384-particle-kink-terminology-20261109.po`
innehåller två radgranskade poster med SHA-256
`80a59079e36183a64fbd0a2d1345d47deaf4f81bd2172b9965407149067a48f4`.
Källmatchning, `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Hunspell-sv markerar den projektspecifika sammansättningen
*nycktyp* samt metadata och källord. Filen är redo för manuell import;
importen är inte verifierad.

## Samlad import — batch 1 370–1 384

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1384.po` ersätter
den samlade 1 370–1 383-filen vid en manuell import. Den innehåller 36 unika
radgranskade poster och har SHA-256
`e81046cbe681beef58818636fdb562dd4ccee09e1d233c92eea1bf6dee00fce5`.
Samtliga poster matchar den lokala källkatalogen och skiljer sig från dess
nuvarande måltext. `msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks
passerade. Den är långt under gränsen på 1 000 strängar och redo för manuell
import. Importresultatet är inte verifierat.

## Batch 1 385 — sekvensredigerarscen i hjälptexter

Två hjälptexter för samma Blender-egenskap använde omskrivningarna
*sekvensredigerarens scen* och *sekvensscenen*, medan UI-etiketten och
terminologin använder den etablerade datatypstermen **sekvensredigerarscen**.
De normaliseras till de böjda formerna *sekvensredigerarscenen* utan att
ändra åtgärd eller renderingens innebörd.

`blender-ui-sv-reviewed-batch-1385-sequencer-scene-wording-20261109.po`
innehåller två radgranskade poster med SHA-256
`a65ae64ed9d17c0cee331fe47266adc0dd6c4ebd7b3b2b5d40b2c75bb2d50119`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Hunspell-sv markerar den projektspecifika böjningen *sekvensredigerarscenen*
samt metadata och källord, men inga svenska stavfel identifierades. Filen är
redo för manuell import; importen är inte verifierad.

## Samlad import — batch 1 370–1 385

`blender-ui-sv-reviewed-next-import-20261109-batches-1370-1385.po` ersätter
den samlade 1 370–1 384-filen vid en manuell import. Den innehåller 38 unika
radgranskade poster och har SHA-256
`c70c2b4692156a12c60accc5a7a14bce9a6441d11650429cdb2c58b03f9c276b`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade. Den är
långt under gränsen på 1 000 strängar och redo för manuell import.
En användarinskickad Weblate-bekräftelse visar att 38 strängar behandlades,
0 hoppades över, 0 saknades och alla 38 uppdaterades. Importen av den samlade
38-postersfilen är därmed verifierad.

## Batch 1 386 — bildruteintervall

Två hjälptexter för åtgärden *Jump to first/last frame* skrev den etablerade
termen *bildruteintervall* utan dess foge-`e`: *bildrutintervall*. Samma
egenskap och närliggande UI använder konsekvent **bildruteintervall**.
Rättelsen gäller endast stavningen i bestämd form, *bildruteintervallet*.

`blender-ui-sv-reviewed-batch-1386-frame-range-spelling-20261109.po`
innehåller två radgranskade poster med SHA-256
`55245b4ea8ef058cb1b6344ed19c5a663f4211bca16701418f5e16b1d00cbb44`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar den tekniska
sammansättningen *bildruteintervallet* samt metadata och källord, men inga
svenska stavfel identifierades. Filen är redo för manuell import;
importresultatet är inte verifierat.

## Batch 1 391 — målningsplats

Åtgärden *Add Paint Slot* tillhör Blenders Texture Paint-arbetsflöde. Den
tidigare formen *färgplats* är därför för snäv: det är en plats för målning,
inte en plats som har färgen som objekt. Etiketten normaliseras till
**målningsplats**, i linje med den närliggande UI-termen *Texture Paint Slot*.

`blender-ui-sv-reviewed-batch-1391-paint-slot-20261109.po` innehåller en
radgranskad post med SHA-256
`612fc042970bd6d8b9777fd4860491fd021de27f93887bf28d63927d77675e93`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Samlad importfil — batch 1 397–1 399

`blender-ui-sv-reviewed-next-import-20261109-batches-1397-1399.po` samlar
batch 1 397–1 399 i en importfil med **231 unika poster**. Tre överlappande
poster har avdubbletterats och den senast granskade formuleringen behålls.
Filen ersätter de tre enskilda batchfilerna som importunderlag; den ska inte
importeras utöver dem. SHA-256 är
`05b3ae4e330d3b75c1345b2f9cdfcdcfb15445e0abf1a86a8cc4dca014d7fd07`.

`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv har kontrollerats
för relevanta svenska ord; kvarvarande träffar är Blender-specifika termer,
metadata eller engelska källord. En användarinskickad Blender Translate-
bekräftelse visar att 231 strängar behandlades, 0 hoppades över, 0 saknades
och alla 231 uppdaterades. Importen är därmed verifierad.

## Batch 1 392 — nyckelbildrutetyp

Blenders *Keyframe Type* avser typen för en keyframe, som i den svenska
UI-terminologin konsekvent är en **nyckelbildruta**. Den förkortade formen
*nyckelbildstyp* gör sambandet otydligt och ersätts av
**nyckelbildrutetyp**.

`blender-ui-sv-reviewed-batch-1392-keyframe-type-20261109.po` innehåller en
radgranskad post med SHA-256
`ac3bd1af89b6d96e29b1ac8b17f3643f2683f0e84dbaa20d251706c78dbe3c21`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 393 — målningsplats i hjälptexter

Två beskrivningar för Texture Paint använde den missvisande formen
*färgplats*. Funktionen skapar dock en plats där texturer målas. De
normaliseras därför till **målningsplats**, samma term som UI-åtgärden
*Add Paint Slot* och den etablerade sammansättningen *texturmålningsplats*.

`blender-ui-sv-reviewed-batch-1393-paint-slot-wording-20261109.po` innehåller
två radgranskade poster med SHA-256
`ff7b15da5b57062446ebff39f462e2dba4cab8b24c937dac3525ebe9a9721f87`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 394 — automatisk nyckelbildsättning

Blenders *Keying* är insättning av nyckelbildrutor. Sex etiketter och
hjälptexter hade den avvikande formen *nyckelbildssättning*, medan samma
funktion i övriga UI:t använder **nyckelbildsättning**. De normaliseras till
den formen; ändringen gäller bara stavning och inte funktionsnamn, dataformat
eller API.

`blender-ui-sv-reviewed-batch-1394-keying-spelling-20261109.po` innehåller
sex radgranskade poster med SHA-256
`c53b6b0c707ab6a0980a9abf89644a2ee03f10937603fd7ce28833fd752a02b0`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 395 — duplicera nyckelbildrutor

Action- och grafredigerarens variant av *Duplicate Keyframes* hade den
förkortade formen *nyckelrutor*. Den identiska kommandotexten i den andra
UI-kontexten och projektets terminologi använder **nyckelbildrutor**, vilket
är den entydiga Blender-termen. Den avvikande dubbletten normaliseras.

`blender-ui-sv-reviewed-batch-1395-duplicate-keyframes-20261109.po` innehåller
en radgranskad post med SHA-256
`e68d0feaa1ac850dc1ad98f0891a8081eae6cc33cdad3858a4b9233a2155cab7`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 396 — nyckelbildrutor i visningsåtgärder

Två View3D-åtgärder för nästa respektive markerade keyframes använde
kortformen *nyckelbilder*. Samma kommandon och animeringstermer använder
annars **nyckelbildruta**. Operatöretiketterna normaliseras därför till
*Till nästa nyckelbildruta* och *På markerade nyckelbildrutor*.

`blender-ui-sv-reviewed-batch-1396-keyframe-label-consistency-20261109.po`
innehåller två radgranskade poster med SHA-256
`7c9f24418553b30941dc97b1f48b5a7a56af8f1b50bd7364f80652f29bda4469`.
`msgfmt`, l10n-lint, svlang, konsistenskontroll och Gitleaks passerade.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 397 — nyckelbildruta i animeringsredigerarna

En radgranskning av Action-, graf- och Dope Sheet-redigerarnas återstående
keyframe-etiketter och hjälptexter hittade 93 konsekventa förekomster av den
äldre formen *nyckelruta*. Samtliga beskriver Blenders animeringsdata och
åtgärder på keyframes, även där den engelska källtexten förkortar termen till
*keys*. De normaliseras därför till **nyckelbildruta** och böjda former som
*nyckelbildrutor* och *nyckelbildrutors*. Andra betydelser av *nyckel* har
inte ändrats.

`blender-ui-sv-reviewed-batch-1397-keyframe-term-consistency-20261109.po`
innehåller 93 radgranskade poster med SHA-256
`bfe5d829605a4e5dd5020228f31af44bef93e2509d52b6807b56e94e9de3ecd3`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar den tekniska
sammansättningen *tidsförskjutningsnyckelbildrutor*, metadata och källord,
men inga svenska stavfel identifierades. Filen är redo för manuell import;
importresultatet är inte verifierat.

## Batch 1 398 — fullständig keyframe-term i animerings-UI

En andra kontextkontroll av samma animeringsgränssnitt hittade 90 poster som
använde den kortare formen *nyckelbild* för Blenders keyframes. De omfattar
inmatning, infogning, Grease Pencil, NLA, Graph Editor och Dope Sheet. De
normaliseras till **nyckelbildruta** och böjda former. Funktionsrubrikerna
*Keyframing* och *Keyframing Settings* avser däremot processen och blir
**Nyckelbildsättning** respektive *Inställningar för nyckelbildsättning*.

`blender-ui-sv-reviewed-batch-1398-keyframe-full-term-consistency-20261109.po`
innehåller 90 radgranskade poster med SHA-256
`690c72560b8203581690e0941dddcfd63dcad4b5a4f8c6181530c8777d1762b0`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar bland annat
den projektspecifika sammansättningen *Bézier-nyckelbildrutor*, men inga
svenska stavfel identifierades. Filen är redo för manuell import;
importresultatet är inte verifierat.

## Batch 1 399 — enskild nyckelbildruta

51 återstående etiketter, meddelanden och färgteman använde den fristående
kortformen *nyckelbild* för en enskild Blender-keyframe. De omfattar bland
annat infogning, redigering, Graph Editor, NLA och Grease Pencil och
normaliseras till **nyckelbildruta** med korrekt bestämd form. Sammansatta
facktermer som *nyckelbildskant* ligger utanför denna batch och ändras inte
mekaniskt.

`blender-ui-sv-reviewed-batch-1399-keyframe-singular-consistency-20261109.po`
innehåller 51 radgranskade poster med SHA-256
`0188d895e37f80a5655e0c38d22c431b8567c7c1b84bb8d0bd4ea70c5f1a5358`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar enbart bland
annat projektnamnet *Grease Pencil*, NLA-termer samt metadata och källord.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 400 — nyckelbildrutenummer

Hjälptexten för Grease Pencil-modifierarens tidsförskjutning syftar på numret
på en keyframe. Den tidigare sammansättningen *nyckelbildnummer* förlorar
den etablerade huvudtermen *nyckelbildruta*. Den normaliseras därför till
**nyckelbildrutenummer**, i linje med *nyckelbildrutetyp* och
*nyckelbildruteintervall*.

`blender-ui-sv-reviewed-batch-1400-keyframe-number-consistency-20261109.po`
innehåller en radgranskad post med SHA-256
`e4eb8bb504235d144c3b5b26026098ff9da3997ebdc5996bc27419d524b378a5`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv markerar den långa,
projektspecifika sammansättningen men inga svenska stavfel identifierades.
Filen är redo för manuell import; importresultatet är inte verifierat.

## Batch 1 401 — Gör om-operatören

Två interna felmeddelanden använde *Återgör-operatören* för Blenders
*Operator redo*. Det avviker från projektets befintliga och idiomatiska
menyterm **Gör om**. De normaliseras till *Gör om-operatören* utan att ändra
API-namn, parameteridentifierare eller funktionsbeteende.

`blender-ui-sv-reviewed-batch-1401-redo-operator-wording-20261109.po`
innehåller två radgranskade poster med SHA-256
`e6f7f20ca5f6a7a85b7d44b19792551597fb4569bb82a2cc27f75d2f2df9eb07`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv har inga relevanta
svenska stavträffar. Filen är redo för manuell import; importresultatet är
inte verifierat.

## Batch 1 402 — Barn av-begränsning

Den synliga etiketten *Child Of* är namnet på en relationsbegränsning för
föräldra-/barnkoppling. Den svenska Blender-manualen använder **Barn av** för
samma begränsning. UI-etiketten normaliseras därför till *Barn av*, medan det
tekniska RNA-värdet `CHILD_OF` i referenskommentaren lämnas helt oförändrat.

`blender-ui-sv-reviewed-batch-1402-child-of-constraint-20261109.po`
innehåller en radgranskad post med SHA-256
`93da4af571273abb2688d064a6e2e1a82c751c2c20b79a811816a09de34893a5`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv hittar inga stavfel i
den svenska måltexten. Filen är redo för manuell import; importresultatet är
inte verifierat.

## Batch 1 403 — klippningsplan

En senare sammansättningsbatch hade ersatt **klippningsplan** med
*beskärningsplan* för RegionView3D och Grease Pencil Line Art. Det bröt mot
den redan dokumenterade CAD-/grafiktermen och den tidigare granskade UI-batchen
632. Tre strängar återställs till *klippningsplan*, inklusive den fullständiga
hjälptexten *när- eller fjärrklippningsplanet*. Kameraavgränsning kan fortsatt
ha den separata kontexttermen *beskärningsplan*.

`blender-ui-sv-reviewed-batch-1403-clipping-plane-regression-20261109.po`
innehåller tre radgranskade poster med SHA-256
`fb7c1e7e6580794dff15ad69a4a9df1726223cc9a7f932a77b586ef93dc3c6d2`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll och Gitleaks passerade. Hunspell-sv flaggar endast PO- och
källtextmetadata. Filen är redo för manuell import; importresultatet är inte
verifierat.

## Batch 1 404 — remsa/remsor

Två meddelanden från keyframing-koden innehöll ett mjukt bindestreck i
*rem­sor*. Ordet har ingen konsonantföljd som kräver avstavningsmarkering och
tecknet kan synas eller störa sökning och stavningskontroll. Former med
`strip(s)` skrivs därför läsbart som *remsa/remsor*.

`blender-ui-sv-reviewed-batch-1404-strip-plural-cleanup-20261109.po`
innehåller två radgranskade poster med SHA-256
`5785552389300000f9a532d0ab53bef35d7891e6d32e358c6845673b50cbb22f`.
`msgfmt`, l10n-lint, svlang (med och utan interpunktionskontroll),
konsistenskontroll, Hunspell-sv och Gitleaks passerade. Filen är redo för
manuell import; importresultatet är inte verifierat.

## Verifierad samlingsimport efter kl. 14 — 2026-11-09

Den manuellt importerade filen
`blender-ui-sv-reviewed-changes-since-1400-20261109.po` innehöll 256 unika
strängar från batch 1 387–1 404. Blender Translate bekräftade **256
bearbetade**, **237 hoppade över**, **0 saknade** och **19 uppdaterade**
strängar. Detta verifierar importen till Blender Translate; fortsatt
upstream-granskning eller eventuell senare ändring av källsträngar är en
separat status.

## Batch 1 405 — Textrendering

Inställningspanelen `bpy.types.USERPREF_PT_interface_text` märktes tidigare
*Textåtergivning*. Eftersom panelen styr Blenders funktion för att rendera text
normaliseras den till **Textrendering**. Termen *återgivning* reserveras för
visning eller reproduktion som inte namnger renderingsfunktionen.

`blender-ui-sv-reviewed-batch-1405-text-rendering-20261109.po` innehåller den
radgranskade posten. `msgfmt`, l10n-lint, svlang (med och utan
interpunktionskontroll), konsistenskontroll, Hunspell-sv och Gitleaks passerade.
Filen är lokalt granskat arkivmaterial och väntar på nästa manuella import.

## Batch 1 406 — serverunika poster

Exporten `blender-ui-ui-sv (7).po` innehåller 13 ofärdiga serverposter som
saknades i föregående lokala export. De omfattar Grease Pencil-varning,
samling, språkstatusrader, kurvtypsdiagnostik samt fel för poserings-,
allmänna och penselresurser. Felaktigt fuzzy-arv om *resursbiblioteket*
ersätts med de kontextuella termerna *resurs*, *poseringsresurs* och
*penselresurs*.

`blender-ui-sv-reviewed-batch-1406-server-only-completion-20261109.po`
innehåller 13 radgranskade poster med SHA-256
`ccd461521ac32a55b2f66d3e8d62399ac3ed23f36fc34ca487ee63851123a9a4`.
`msgfmt`, svlang (med och utan interpunktionskontroll),
konsistenskontroll, Hunspell-sv och Gitleaks passerade. l10n-lint passerade
för deltan; verktyget returnerar kod 1 utan diagnostik för den stora sammanslagna
katalogen, medan övriga helkatalogkontroller passerade. Deltan väntar på
manuell import.

## Batch 1 407 — terminologiska regressioner

Den nya exporten har jämförts rad för rad mot den föregående granskade
arbetskatalogen. Åtta säkra regressioner rättas: *Action-slotten* återställs
i stället för det otydliga pronomenet, `keymap` och Blender-operator blir
*tangentmappning* respektive *operatör*, och koordinatrymdsetiketterna använder
grundformerna *rutnätsindexrymd* och *världsrymd*. Den villkorliga
gizmo-hjälptexten bevarar booleska API-literalet `true`.

`blender-ui-sv-reviewed-batch-1407-terminology-regressions-20261109.po`
innehåller åtta radgranskade poster med SHA-256
`2c84cc3c89a02bc2d7d95bd3d4aab40c89c0856eb17aeb4c284eec8ee03a0d03`.
`msgfmt`, l10n-lint, svlangs konsistenskontroll och Gitleaks passerade.
Hunspell-sv och svlangs frekvensanalys flaggar endast *gizmon*, som är den
korrekt böjda Blender-termen i strängen. Deltan väntar på manuell import.

## Verifierad import av batch 1 406–1 407 — 2026-11-09

Den manuella importen av
`blender-ui-sv-reviewed-not-in-latest-export-20261109.po` bekräftades i
Blender Translate: **21 bearbetade**, **0 hoppade över**, **0 saknade** och
**21 uppdaterade** strängar. Komponenten visar därefter 40 434 av 40 434
översatta strängar. Detta bekräftar importen och fullständig
översättningstäckning, men inte att de 28 kvarvarande serverkontrollerna är
språkliga fel; de granskas mot nästa exporterade katalog.

## Batch 1 408 — versaler efter kolon

En oberoende genomgång av den tillgängliga exporten och Blenders källkontext
identifierade sex verkliga versalregressioner i diagnostiktext. Svenskan har
en ny fullständig sats efter kolon och använder därför liten bokstav:
*benhuvudet*, *namnet*, *endast* och *måste*. Kod- och enumvärdena `PRESS`,
`RELEASE` och `NOTHING` behålls oförändrade. Övriga aktuella kontroller för
flera versaler gäller format, standarder, API-namn eller produktnamn och är
inte säkra ändringskandidater.

`blender-ui-sv-reviewed-batch-1408-colon-capitalization-20261109.po`
innehåller sex radgranskade poster med SHA-256
`4ffdd8d37cb390969e4b8b7d2b776114406ce5904168b8964071853559ea603b`.
`msgfmt`, l10n-lint, svlangs konsistenskontroll och Gitleaks passerade.
Svlangs V2-varningar är falska positiva för satser efter kolon; Hunspell-sv
flaggar endast enumvärdet `NOTHING` och `unicode`. Batchen väntar på manuell
import.

## Batch 1 409–1 411 — terminologi och hjälptextformat

Fortsatt lokal radgranskning av den senaste tillgängliga exporten normaliserar
Blenders UI-term *operatör* i stället för engelska *operator*,
*poseringsläge*, *tangentmappning*, *Dopebladsredigeraren* och Blenders
etablerade ord för packade data. Hjälptexten för interaktiv geometri har också
återfått källans punktmarkörer och bindestreck. Kodidentifierare och
matematiska Laplaceoperatorer har lämnats orörda.

`blender-ui-sv-reviewed-batch-1409-operator-terminology-20261109.po`,
`blender-ui-sv-reviewed-batch-1410-terminology-consistency-20261109.po` och
`blender-ui-sv-reviewed-batch-1411-operator-helptext-format-20261109.po`
innehåller sammanlagt 24 granskade poster. `msgfmt`, l10n-lint, svlangs
konsistenskontroll och Gitleaks passerade. Hunspell-sv och svlangs vanliga
stilanalys rapporterar bara projektspecifika termer, kod och kända
heuristiska falska positiva. Batcherna väntar på manuell import.

## Batch 1 412–1 418 — konsekvent svensk Blenderterminologi

Den fortsatta radgranskningen normaliserar svensk interpunktion,
*nyckelbildruta* och *nyckelbildsättning*, resursnamn för poser och penslar
samt Blenders mesh-termer. Bland annat ersätts felaktiga eller otydliga
former med *poseringsresurs*, *meshcache*, *meshdeformering* och
*meshsekvenscache*. Tekniska produkt- och API-namn lämnas oförändrade.

Deltafilerna för batch 1 412–1 418 innehåller tillsammans 53 kontrollerade
poster. `msgfmt`, l10n-lint, svlangs konsistenskontroll och Gitleaks
passerade. Hunspell-sv och den generella svlang-analysen rapporterar endast
förväntade Blendertermer, källtext och tekniska identifierare. Batcherna är
lokalt arkiverade och väntar på manuell import.

## Batch 1 419 — animation och rendering

En ny kontextgranskning av animations- och renderingssträngar ersätter
*återges* med **renderas** när Blenders renderingsprocess avses, enligt
projektets terminologi. Två nyckelbildstyper normaliseras till *ytterläge*,
och gränssnittet använder *nyckelbildsättning* för *keyframing*. Dessutom
rättas en diagnostik till *posen på en bibliotekslänkad armatur*.

`blender-ui-sv-reviewed-batch-1419-animation-rendering-20261109.po`
innehåller nio granskade poster. `msgfmt`, l10n-lint och Gitleaks passerade.
Svlangs två V2-varningar är verifierade falska positiva; ordföljden i båda
satserna är korrekt. Hunspell-sv träffar endast PO-metadata, engelska
källsträngar och Blendernamn. Filen är lokalt granskad, arkiveras separat och
väntar på manuell import.

## Batch 1 420–1 430 — fortsatt kontext- och terminologigranskning

Batch 1 420–1 430 fortsätter den radvisa granskningen av animation,
geometri, rörelsespårning och tangentmappning. Terminologin har normaliserats
för mellanposer, posben, F-kurvmodifierare och Blenderoperatörer. Batch 1 430
rättar dessutom initial versal i en fullständig glTF-importhjälptext.

`blender-ui-sv-reviewed-batch-1430-gltf-tooltip-capitalization-20261109.po`
innehåller en granskad post med SHA-256
`8487c5be107dfcb4e96031035cdb8073a2b69ca9026866513d3c0540ebf46e36`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv träffar enbart
metadata, källtext och tekniska identifierare. Batchen är lokalt arkiverad
och väntar på manuell import.

## Batch 1 431 — verbet rendera

Fem hjälptexter och kommandon där engelska *render* tidigare hade översatts
med *återge* är normaliserade till **rendera**. De avser Blenders
renderingsprocess, inklusive förhandsgranskning, hårshader och UI-text, inte
en allmän återgivning av innehåll.

`blender-ui-sv-reviewed-batch-1431-render-verb-normalization-20261109.po`
innehåller fem granskade poster med SHA-256
`b85cf6b721a0412c7347435ddd0bc0ec0c8072bf56411766670b7f83429ecb6f`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv godkände samtliga
målspråksord. Svlangs V2-träff är en falsk positiv; satsen *så approximerar
skuggningen* har korrekt svensk ordföljd. Batchen är lokalt arkiverad och
väntar på manuell import.

## Batch 1 432 — constraints och skulpteringsmaskering

Två UI-etiketter har normaliserats mot den etablerade Blenderterminologin:
*Track To Constraint* är **Rikta mot-begränsning** och *Mask From Cavity* är
**Mask från hålighet**. Den senare termen följer den befintliga termen
*hålighetsmask* för samma skulpteringskontext.

`blender-ui-sv-reviewed-batch-1432-constraint-and-cavity-terminology-20261109.po`
innehåller två granskade poster med SHA-256
`ae208708d1c5e85de876bf5c14013ff12c3f6d968a677b74782b645df9c0ea28`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 450 — parallell form i fältvisning

Hjälptexten för att rendera ett simuleringsfält använder nu parallell form i
samordningen: **genom att färgkartlägga** eller **genom att använda**. Den
tidigare texten saknade *genom att* i den andra leden.

`blender-ui-sv-reviewed-batch-1450-fluid-field-rendering-grammar-20261109.po`
innehåller en granskad post med SHA-256
`3e81bc1b834a248b9163bc219e946df7ad2e47c27b1b8248df013b856ae1eed3`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Radgranskning — poster 1–1 280

Den systematiska radgranskningen av den lokala UI-exporten omfattar nu poster
1–1 280. Terminologin för animation, resurser, attribut, geometri, bakning och
B-Bone-parametrar kontrollerades mot UI-kontexten. Säkra rättelser har brutits
ut i separata deltafiler (senast batch 1 444); kontextberoende källsträngar
med flera oförenliga användningar har lämnats orörda i stället för att skapa
regressioner i andra delar av UI:t. Detta är lokal granskning, inte ett påstående
om att hela katalogen är manuellt radgranskad.

## Batch 1 443 — Action-slots utfällning

Action-slottens booleska *Show Expanded* använder nu **Visa utfälld**, i
stället för den tvetydiga formen *Visa utökad version*. Formen följer den
närliggande egenskapen *Expanded state of the slot* → *Utfällningsstatus*.

`blender-ui-sv-reviewed-batch-1443-action-slot-expansion-20261109.po`
innehåller en granskad post med SHA-256
`dda9d69840beb84b0b8b5bb930ba4d6ec98ddbf583a5f9fa34bfa95cd888ecdb`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Fullständig lokal QA-snapshot — 2026-11-09

Den aktuella lokala UI-exporten har kontrollerats med `msgfmt`, Gitleaks,
l10n-lint, svlang och hunspell-sv. `msgfmt` och Gitleaks passerar. l10n-lint
har 0 fel; dess kvarvarande varningar är granskade formatnamn, datumformat,
medvetet källspråkslika produktnamn och svensk interpunktion. Svlang rapporterar
konsekventa översättningar och inga skrivregelfel. Den enda anglicismträffen är
de avsiktliga katalognamnen `startup`, `add-ons`, `modules` och `presets` i en
skriptsökväg. Hunspell-sv används riktat: återstående träffar består främst av
Blenders projektspecifika tekniska termer, identifikatorer och formatnamn.

Snapshoten är en mekanisk och riktad terminologisk kvalitetskontroll, inte ett
påstående om att varenda av katalogens strängar redan har manuellt radgranskats.

## Batch 1 442 — metaklot i plural och renderingsvy

Datablock, filter och exporter använder nu pluralformen **metaklot** i stället
för den äldre formen *metabollar*. Den relaterade renderingsvyn är samtidigt
förtydligad till **Renderingsvy för stereoskopisk 3D och rendering med flera
vyer**.

`blender-ui-sv-reviewed-batch-1442-metaklot-plurals-and-render-view-20261109.po`
innehåller sju granskade poster med SHA-256
`d21c9e4784defd02a1acc2d12e6561d88759f604029ce8b2b90ced222065ab9e`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
enbart projektspecifika sammansättningar som ovanliga. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 441 — stereoskopisk 3D och metaklot

Sju återstående etiketter och hjälptexter för *Stereo 3D* använder nu
**stereoskopisk 3D**, exempelvis **Stereoskopisk 3D-visning** och
**Stereoskopiskt 3D-läge**. En diagnostikrad använder samtidigt
**Metaklot** i stället för den engelska objekttypen *Metaball*.

`blender-ui-sv-reviewed-batch-1441-stereoskopisk-3d-and-metaklot-20261109.po`
innehåller nio granskade poster med SHA-256
`de922007c60aa5b1716770429d97ace87e559cfd04a70d2dc747ae5294ed46e3`.
`msgfmt`, l10n-lint, svlang och Gitleaks passerade. Hunspell-sv markerar
enbart *splinen*, en etablerad teknisk Blenderterm. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 440 — metaklot

Äldre engelsknära former av *metaball* är normaliserade till **metaklot** i
fjorton UI- och diagnostiksträngar, bland annat *metaklotdatablock*,
*metaklottyp* och *metaklotrelaterade animeringsdata*. De följer den befintliga
Blendertermbasen och behåller *mesh* som Blenders avsiktliga datatypsnamn.

`blender-ui-sv-reviewed-batch-1440-metaklot-terminology-20261109.po`
innehåller fjorton granskade poster med SHA-256
`7cb0d110e600512b4e864cf514068d8f18c486b3a9e29756ca69435bce1fa692`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
vissa projektspecifika sammansättningar som ovanliga, men inte som sakfel.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 452 — Freestyle-ändlock

Freestyle-alternativet *Square cap* heter nu **Fyrkantigt ändlock**, i linje
med närliggande *Butt cap* och *Round cap*. Den tidigare översättningen
utelämnade huvudordet och var därför inkonsekvent.

`blender-ui-sv-reviewed-batch-1452-freestyle-square-cap-terminology-20261109.po`
innehåller en granskad post med SHA-256
`c65e3079c4320f42bdb107f32d028715b745baba77b7031e047acb5c422b2e81`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 453 — NDOF och interpolering

NDOF-kommandonas ordföljd har normaliserats, så att exempelvis
**Spara NDOF-vy 1** används. Tre felöversättningar av *easing* i
kurvinterpoleringen har också ersatts med projektets etablerade **mjuk
in-/utfasning** i stället för *lättnad*.

`blender-ui-sv-reviewed-batch-1453-keymap-easing-terminology-20261109.po`
innehåller nio granskade poster med SHA-256
`13c25c8f725d3e7d292b37db7a3dd05a64f21f6fce37d887dcbc68625ad2c2a7`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
NDOF samt de korrekta facktermerna *fjärdegradig* och *femtegradig* som
ovanliga; detta är granskade informationssignaler. Batchen är lokalt
arkiverad och väntar på manuell import.

## Radgranskning — poster 4 001–5 760

Fluiddomän, Freestyle, Grease Pencil, Gizmo, Actions, penslar, kameror,
samlingar och kurvor har granskats rad för rad i den lokala exporten. Två
säkra språkjusteringar skapade batch 1 450 och 1 451; övriga poster i
intervallet lämnades oförändrade efter kontext- och terminologikontroll.
Detta är lokal granskning, inte en verifiering av manuell Weblate-import.

## Verifierad import — 2026-11-09 efter kl. 16

Den manuella Weblate-importen av den samlade filen med batch 1 403–1 437 är
verifierad i Weblates importresultat: **169 behandlade**, **20 uppdaterade**,
**149 överhoppade** och **0 saknade** poster. Överhoppade poster var redan
identiska eller saknade en ändring att tillämpa. Detta bekräftar importen, men
inte någon separat upstream-granskning eller merge. Batch 1 438–1 439 skapades
efter den här importen och väntar fortfarande på manuell import.

## Batch 1 439 — primitiv-, ljud- och stereoformat

Tre synliga UI-etiketter följer nu den etablerade Blenderterminologin:
*Add Ico Sphere* är **Lägg till Icosfär**, mixningens *Sample format* är
**Ljudsamplingsformat**, och bildformatets *Stereo 3D Format* är
**Stereoskopiskt 3D-format**.

`blender-ui-sv-reviewed-batch-1439-primitive-audio-stereo-terminology-20261109.po`
innehåller tre granskade poster med SHA-256
`dc0ee4ee64ea45ce3f4fb626d159c0ea91b7b031c0be38e42947380f79fead62`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
*Icosfär* och *ljudsamplingsformat* som ovanliga allmänspråkliga ord, men
båda är fastställda Blendertermer. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 435 — Icosfär

Den triangulerade sfärprimitiven är nu konsekvent **Icosfär** i Geometry
Nodes och 3D-vyn. Formen följer Blenders svenska manual och skrivs utan
bindestreck.

`blender-ui-sv-reviewed-batch-1435-icosphere-terminology-20261109.po`
innehåller två granskade poster med SHA-256
`3e4b40a57e799a600322dab15c22c73446af93944460ce56077e7455a5025ccc`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
*icosfär* som ovanlig projektterm; den verifieras mot Blenders svenska
manual. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 436 — metaklot

Fyra UI-strängar följer nu den etablerade Blenderterminologin **metaklot**
och **metaklotelement**, i stället för engelska *metaball*-former.

`blender-ui-sv-reviewed-batch-1436-metaball-terminology-20261109.po`
innehåller fyra granskade poster med SHA-256
`20f92238b0a9a8c43dc5079192558b905533ebf30a75c07c99782a22ff111567`.
`msgfmt`, l10n-lint och Gitleaks passerade. Batchen är lokalt arkiverad och
väntar på manuell import.

## Batch 1 437 — ljudsamplingsformat

Systeminställningens *Sample Format* är normaliserad till
**Ljudsamplingsformat**, enligt den etablerade Blendertermen för ljudets
bitdjup och numeriska representation.

`blender-ui-sv-reviewed-batch-1437-audio-sample-format-20261109.po`
innehåller en granskad post med SHA-256
`f59aacf50405ca7b150812e647e528dbf4edb8f5be59650cbbe0f2d0a3ffa2b5`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 434 — transformation

Action-slotarnas *Transform channel* och två relaterade hjälptexter använder
nu **transformationskanal** och **transformationsvärde**, konsekvent med
Blenders etablerade term *transformation*.

`blender-ui-sv-reviewed-batch-1434-transformation-terminology-20261109.po`
innehåller tre granskade poster med SHA-256
`07bc497b7970dce83037ad3a40364503f6b79d024ea22ecea9cf8456c0e3670d`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 433 — teckensnitt

Det synliga filtret för Blenders fontdatablock använder nu **Teckensnitt**,
konsekvent med den etablerade UI-termen och övriga inställningar för
teckensnitt.

`blender-ui-sv-reviewed-batch-1433-font-terminology-20261109.po`
innehåller en granskad post med SHA-256
`be2fc2a3a07fa88de632d34524cf74fa8942e5dfc3061fcfe9a8636b04eba3e9`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 438 — stereoskopisk 3D

Bildinställningens *Settings for stereo 3d* följer nu samma etablerade
Blenderterm som motsvarande 3D-vyformat: **Inställningar för stereoskopisk
3D**. Ändringen begränsas till vyformatets inställningsetikett och ändrar inte
separata namn på operatörer eller visningslägen.

`blender-ui-sv-reviewed-batch-1438-stereo-3d-terminology-20261109.po`
innehåller en granskad post med SHA-256
`7ba6e9e25a3b3e5a53757f433f4868c710bd4606271b07e8c1b9d7a6ff92e7ba`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 444 — attributets array-lagring

I attributets lagringstyp används nu **Fält** för engelska *Array*. Det är
programmeringstermen för en elementvis samling och kan inte vara **Matris**,
som redan är en separat 4 × 4-datatyp i samma UI.

`blender-ui-sv-reviewed-batch-1444-attribute-array-terminology-20261109.po`
innehåller en granskad post med SHA-256
`794a17a36aae64033ea65c382ace585c1305a2b975c64ab6a50b4895fb09929c`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 445 — tygsimulering

I tygsimuleringens parametertext använder *cloth* nu konsekvent **tyg**.
Tidigare **duken** avvek från samtliga närliggande tyginställningar i samma
panel.

`blender-ui-sv-reviewed-batch-1445-cloth-terminology-20261109.po` innehåller
en granskad post med SHA-256
`f06398025e28f25090113569fc3b6c6967542c25c6e4752c56a2db11c232427a`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 446 — bestämd form av mesh

Den bestämda formen av **mesh** normaliseras till **meshen**, i linje med
övriga Blender-termer som *meshcache* och *meshdeformering*. Hunspell-sv
saknar sammansättningen och svlang markerar den som sällsynt, men båda är
informationssignaler; UI-kontexten och projektterminologin avgör formen.

`blender-ui-sv-reviewed-batch-1446-mesh-inflection-20261109.po` innehåller
en granskad post med SHA-256
`3ebe4100b209477ae50a47cf77c56ad670b5c2bbdbcac52e6f1c6681e6ceedc4`.
`msgfmt`, l10n-lint och Gitleaks passerade; Hunspell-sv och svlang
kontrollerades enligt ovan. Batchen är lokalt arkiverad och väntar på manuell
import.

## Batch 1 447 — hörnpunktsgrupp

Constraint-hjälptexten använder nu **hörnpunktsgrupp** i stället för det
onödiga engelska lånet *vertexgrupp*, i linje med övriga Blender-strängar.

`blender-ui-sv-reviewed-batch-1447-vertex-group-terminology-20261109.po`
innehåller en granskad post med SHA-256
`ccacfa9431a2a56e37e424570070f5c40c0efaf4a9bd71349baa87a0fb188476`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv saknar den korrekta
sammansättningen och svlang felmarkerar satsens V2-följd; båda signalerna är
granskade. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 448 — bestämd form av mesh i Dynamic Paint

Ett återstående **meshet** i Dynamic Paint har normaliserats till **meshen**.
Sökning i hela exporten bekräftar att ingen form *meshet* återstår.

`blender-ui-sv-reviewed-batch-1448-mesh-inflection-dynamic-paint-20261109.po`
innehåller en granskad post med SHA-256
`0cb0a05b5395586ccfccfc177e847e632e2390541f9ef8eb90bc2ba9e59d3a36`.
`msgfmt`, l10n-lint och Gitleaks passerade. Hunspell-sv och svlang markerar
den korrekta facktermen som sällsynt. Batchen är lokalt arkiverad och väntar på
manuell import.

## Batch 1 449 — miniatyrbilder

Filbläddrarens hjälptext använder **miniatyrbilderna**, konsekvent med den
övriga UI-terminologin, i stället för det otydliga *tumnaglarna*.

`blender-ui-sv-reviewed-batch-1449-thumbnail-terminology-20261109.po`
innehåller en granskad post med SHA-256
`17770e94f7d8261f85eff9241a136c34eecc14cee5d25644fdec333ef8764849`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 451 — widgetsamling

Rigify-hjälptexten använder bestämd form i satsen **i vilken samling
widgetobjekten ska placeras**, vilket gör den fullständig och idiomatisk.

`blender-ui-sv-reviewed-batch-1451-widget-collection-grammar-20261109.po`
innehåller en granskad post med SHA-256
`be1e4d4c15f9242b7859705da8894b2b83a9c3c4987698ea5999c8a79b230f53`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlang markerar den
korrekta indirekta frågesatsen som möjlig V2-avvikelse; det är en falsk positiv.
Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 481 — objekt kastar skuggor

Hjälptexten avser ett bestämt objekt: **Objektet kastar skuggor i 3D-vyporten**.

`blender-ui-sv-reviewed-batch-1481-object-casts-shadows-20261109.po`
innehåller en granskad post med SHA-256
`be64246e98ee15ac0ed31c1af9dcce8b341db36037280c3cf0a581e6ff16aa6d`.
`msgfmt`, l10n-lint, Hunspell-sv och Gitleaks passerade. svlang markerar
**vyporten** som sällsynt; termen används etablerat i Blender. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 482 — avaktivera sololäge

Kommandot använder den befintliga statusbenämningen **sololäge**:
**Avaktivera sololäge för alla**.

`blender-ui-sv-reviewed-batch-1482-clear-solo-mode-20261109.po` innehåller en
granskad post med SHA-256
`af6cd02ee1e151fc2f7b71033eedf050e9a334eb8d8e3eba34be072ec0dad20a`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang och Gitleaks passerade. Batchen är
lokalt arkiverad och väntar på manuell import.

## Batch 1 610 — sekvensredigerare och vyport

Sekvensredigerarens ljudremsor använder nu det etablerade verbet **fäst** i
stället för det tvetydiga *snäpp*. Effekten i 3D-gränssnittet använder den
projektspecifika termen **vyport**.

`blender-ui-sv-reviewed-batch-1610-sequencer-viewport-20261110.po` innehåller
två radgranskade poster med SHA-256
`40b2ed190bf414354830b2ed6335202b239f9bd88a4c0a6f38d676da0318c85d`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 618 — vokala formanter

Hjälptexten för tonhöjdsförskjutning använder nu samma etablerade term som
reglagets etikett: **vokala formanter**.

`blender-ui-sv-reviewed-batch-1618-vocal-formants-20261110.po` innehåller en
radgranskad post med SHA-256
`bec107bdcd5dbf7980c526d6e2d740891cda671acb019ed3bb53e10d952204a6`.
`msgfmt`, l10n-lint, Hunspell-sv, diffkontroll och Gitleaks passerade. svlang
gav en falsk V2-varning för den grammatiskt korrekta indirekta frågesatsen med
*om*. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 619 — partikelhårets krusning

Partikelhårens **Kink**-egenskaper använder nu den etablerade, begripliga
termen **krusning** i stället för den missvisande termen *nyck*. Fem
egenskapsrubriker har dessutom normaliserats till åtgärdsformen **Påverka**.

`blender-ui-sv-reviewed-batch-1619-particle-kink-terminology-20261110.po`
innehåller 13 radgranskade poster med SHA-256
`ee5b80d4abc604c158cf75603d28605476ba7fe073fd1278935d17e0a82d2768`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang, diffkontroll och Gitleaks passerade.
Hunspell-sv och svlang markerar bara den kontextkorrekta sammansättningen
*krusningsamplitudfaktor*. Batchen är lokalt arkiverad och väntar på manuell
import.

## Batch 1 611 — vyport, Action och armaturobjekt

Klippredigerarens interaktiva område är en **vyport**, Shape Keys avser
Blenders datatyp **Action**, och sammansättningen **armaturobjekt** följer
övriga träffar i exporten.

`blender-ui-sv-reviewed-batch-1611-viewport-action-armature-20261110.po`
innehåller tre radgranskade poster med SHA-256
`7ce7d316e6ffa897574941bfd52ea99039b097b6df422d2cd4689e28f8cf4c45`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang, diffkontroll och Gitleaks
passerade; Hunspell-sv och svlang markerar endast den etablerade termen
**vyporten** som sällsynt. Batchen är lokalt arkiverad och väntar på manuell
import.

## Batch 1 612 — textredigerarens rader

I textredigeraren är *line* en textrad, inte en grafisk linje. Etiketterna
använder därför **Översta raden** och **Översta synliga raden**.

`blender-ui-sv-reviewed-batch-1612-text-editor-lines-20261110.po` innehåller
två radgranskade poster med SHA-256
`9c3db8a96435bf7329a4fdb6b56e79d09012e967c37969109f37259c045a72fa`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 613 — vyport och virtuell verklighet

3D-vyportens hjälptexter använder konsekvent **vyport**. Den blandade engelska
formen *virtual reality-sessioner* normaliseras till **sessioner i virtuell
verklighet**.

`blender-ui-sv-reviewed-batch-1613-viewport-vr-terminology-20261110.po`
innehåller fyra radgranskade poster med SHA-256
`a7b7d5066c3cb802bf0a7bf12fe34a1ade9770ff25d71b1ef5e3f6a05056f181`.
`msgfmt`, l10n-lint, Hunspell-sv, svlang, diffkontroll och Gitleaks
passerade; Hunspell-sv och svlang markerar bara den etablerade Blender-termen
**vyport**. Batchen är lokalt arkiverad och väntar på manuell import.

## Batch 1 614 — UV-sträckning

UV-redigerarens hjälptext använder nu den befintliga UI-termen
**UV-sträckning** i stället för det onödiga engelska lånet *UV-stretch*.

`blender-ui-sv-reviewed-batch-1614-uv-stretch-terminology-20261110.po`
innehåller en radgranskad post med SHA-256
`ff5da06fbe5253a8243c369251219ffadca882c61fde59e9452603e2ed4d4905`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 615 — tillämpade remshandtag

Två parallella hjälprader i sekvensredigeraren använder konsekvent
**tillämpas/tillämpats** i stället för det avvikande *appliceras/applicerats*.

`blender-ui-sv-reviewed-batch-1615-sequencer-application-20261110.po`
innehåller två radgranskade poster med SHA-256
`9d812c1711a4d213419be4f28e7083213bbae5373970c58a7c8d4daeaf4d2cc1`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 616 — hastighetsremsans hjälptext

Hastighetsremsan återfår det tappade sakledet **ingångens** och stavfelet
*remans* rättas till **remsans**.

`blender-ui-sv-reviewed-batch-1616-speed-strip-wording-20261110.po`
innehåller två radgranskade poster med SHA-256
`e4902c7ba8c5fb957a98a305987646b0c5de051b588a94e278044855e572dfc4`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.

## Batch 1 617 — scenremsans tidslinje

Den krystade sammansättningen *sekvensredigerare-tidslinje* ersätts av den
idiomatiska satsdelen **tidslinjen i scenens sekvensredigerare**.

`blender-ui-sv-reviewed-batch-1617-scene-strip-timeline-20261110.po`
innehåller en radgranskad post med SHA-256
`f1de8b5ef7262d5845eea80aba98e24aded1884498064b1060fc3019cb8defb7`.
`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. Batchen är lokalt
arkiverad och väntar på manuell import.
