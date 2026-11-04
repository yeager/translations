# Terminologikontroll: Blender Manual

Datum: 2026-11-04

## Underlag och metod

Kontrollen omfattar råexporten
`exports/2026-11-04/blender-manual-manual-sv.po`, projektets
`TERMINOLOGY.md`, tidigare lokala Blender-batcher och den projektbundna
termdatamängden `swedish-foss-terminology/reviewed/data/blender.jsonl`.
Sökningarna har riktats mot `data-block`, `slot`, `vertex`, `bevel`,
`displacement`, `shader`, `Library Override`, `Action` och `USD`.

Råexporten är oförändrad. Rapporten skiljer medvetet mellan verifierade
termbeslut, konkreta granskade rättelser och stora kontextberoende restmängder.

## Verifierade termbeslut

| Källa | Rekommenderad svensk form | Evidens och avgränsning |
| --- | --- | --- |
| `data-block` | `datablock` | Termlistan och Blender-projektets termdata belägger sammansättningen, exempelvis `Action data-blocks` → `Åtgärdsdatablock`. API- och RST-identifierare lämnas oförändrade. |
| `slot` i Action-systemet | `slot`, plural `slotar` | Aktuell UI- och manualkontext använder den tekniska termen. Den får inte förväxlas med renderings-, material- eller maskinplatser. Batch 25 och UI-batch 02 rättar en avgränsad del. |
| `vertex` i meshtext | `hörnpunkt` och sammansättningen `hörnpunkts-` | Termlistan begränsar beslutet till mesh- och verktygskontext. `Hörn` kan vara korrekt för korta visnings- eller orienteringsetiketter, och API-namnet `VertexGroup` är orört. |
| `Bevel` | `avfasning`, verb `fasa` | UI och termdata bekräftar `Avfasning` som operator/egenskap och `Fasa hörnpunkter/kanter` som kommandon. `fasning` kan användas i löpande bildtexter när den beskriver resultatet. |
| `Displacement` | `förskjutning`; `Vector Displacement` → `vektorförskjutning` | Bevarat i manualens USD- och materialkontext. Terminologin skiljer detta från allmän betydelse av *displacement*. |
| `shader` | `shader` | Etablerad Blender-form. Produkt- och nodnamn, till exempel `Principled BSDF`, bevaras enligt UI-källan. |
| `Library Override` | kontextstyrt `biblioteksåsidosättning` eller `biblioteksöverskrivning` | UI och termdata innehåller båda formerna. Ingen global normalisering är säker; varje menytext, operatör och löptext måste jämföras med närliggande UI. |
| `Action` | `åtgärd` i förklarande animationstext | Datatyp-/API-namn `Action` behålls. Batch 25 använder formen genomgående i de tolv granskade posterna. |
| USD, `UsdGeom*`, `Scope`, `allPurpose`, `preview` | behåll tekniska identifierare | Export- och importbatcherna 18–23 verifierar att endast den omgivande förklarande texten lokaliseras. `USD-scen`, `rotprim`, `standardprim` och `punktmoln` har separata, belagda betydelser. |

## Säkerställda rättelser i aktuella batcher

- `link_append.rst`: batch 24 har 22 dubbelgranskade ändringar och använder
  bland annat `datablock`, `biblioteksåsidosättanden`, `samlingsinstans`,
  `Instanssamlingar`, `Instansobjektdata`, `Flytta` och `Gör lokalt` i
  UI-belagd kontext.
- `animation/actions.rst`: batch 25 har 12 dubbelgranskade ändringar med
  `åtgärd`, `slot`, `F-kurva`, `Grafredigeraren` och `Dopebladet`.
- `edge/bevel.rst`: den dubbelgranskade införandeplanen omfattar 12
  UI-belägda mesh- och avfasningsposter. De är ännu inte deltafil eller
  uppladdning.
- rendering: den dubbelgranskade kandidatgranskningen fastställer
  `Materialutdata`, `Adaptiv underindelning` och `Äldre texturtyper` för tre
  avgränsade poster. De är ännu inte deltafil eller uppladdning.

## Avvikelser som kräver fortsatt radgranskning

Följande träffar är verkliga arbetsköer men får inte massändras:

1. Manualens äldre Action-avsnitt innehåller kvarvarande engelska former som
   `action`, `slots`, `Action Redigerare` och `spelaautomaten`. Några ingår i
   batch 25 eller den senare kandidatgranskningen, men övriga kan vara
   datatyper, produktetiketter eller föråldrad text och måste tas med full
   RST- och UI-kontext.
2. Manualens äldre `Library Override`-text växlar mellan oöversatt engelska,
   `biblioteksöverskrivning` och närliggande operatornamn. Eftersom UI självt
   har konkurrerande belagda former är detta en kontextkö, inte ett globalt
   ersättningsjobb.
3. `vertex` har äldre engelska måltexter i flera manualdelar, men även
   API-namn och korta etiketter där *hörn* snarare än *hörnpunkt* kan vara
   korrekt. En enkel global ersättning skulle skada källan.
4. `Bevel` förekommer som funktionsnamn, modifierare, nod och allmän
   geometri. `Avfasning`, `fasning`, `fasa` och engelska nodnamn måste väljas
   efter den enskilda strängens funktion.
5. Glossary och versionerade manualexporter finns lokalt, men den aktuella
   råexporten har inte använts som underlag för en rad-för-rad-omskrivning av
   dessa komponenter. De ska jämföras med den aktuella manualen på nyckel- och
   termnivå för att undvika duplicerat arbete.

## Verktygsresultat och tolkning

- Projektets termlista och Blender-posterna i `swedish-foss-terminology`
  styrde termjämförelsen; äldre termposter användes inte som ensamma beslut
  när de motsade den aktuella UI-källan.
- `rg` användes för fulltextsindexering av högprioritetstermer och för att
  kontrollera batchtäckning.
- Varje färdig deltafil går fortfarande genom `msgfmt`, `l10n-lint`,
  `svlang`, Hunspell, sekretesskanning med Gitleaks och `git diff --check`.
  Denna rapport ersätter inte de filspecifika kontrollerna.

## Slutsats

Termbasen är tillräckligt verifierad för fortsatt snabb batchgranskning, men
manualens och UI:ts fullständiga terminologiarbete är inte klart. Endast
belagda, kontextkontrollerade former ska läggas i nya deltafiler.
