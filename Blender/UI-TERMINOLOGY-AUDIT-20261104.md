# Terminologikontroll: Blender UI

Datum: 2026-11-04

## Omfattning och metod

Granskningen omfattar den lokala UI-råexporten
`exports/2026-11-04/blender-ui-ui-sv.po` och de högprioriterade termerna
`data-block`, `slot`, `vertex`, `bevel`, `displacement`, `shader`, `Library
Override` och `Action`. Formen har jämförts med `TERMINOLOGY.md`, kontexten
i exportens källreferenser och den lokala terminologidatabasen.

Kontrollen är avsiktligt konservativ: en engelsk teknisk rest eller en annan
form räcker inte för ändring om den kan vara ett API-namn, en nodetikett eller
en kontextstyrd etablerad UI-form.

## Verifierade former

| Begrepp | Resultat | Belägg |
| --- | --- | --- |
| `data-block` | `datablock` | Huvudformen och sammansättningar som `datablocktyp` används konsekvent. |
| `slot` | `slot`, `sloten`, `slotten`, `slotar` | Grundformen i råexporten har den felaktiga formen `Slott`, men är redan täckt av UI-delta batch 02. Böjningen `slotten` har två t genom bestämd form och är inte ett stavfel. |
| `vertex` | `hörnpunkt` eller `hörn` | `Hörn` förekommer i korta vy-/nodetiketter och stämmer med termlistans kontextundantag. `Hörnpunktsgrupp`, `hörnpunktsnormal` och `hörnpunktsindex` är konsekventa. |
| `bevel` | `fasning` och `avfasningsmodifierare` | UI-formerna `Fasradie`, `Fasdjup`, `Fasningsläge` och modifierartermen är kontextuellt konsekventa. |
| `displacement` | `förskjutning` | UI använder bland annat `Förskjutning`, `Vektorförskjutning` och `Förskjutningsrymd` konsekvent. |
| `shader` | `shader` | Bevaras som Blender-fackterm. Varianter som `shadernod`, `shader-nod` och `shadernoder` måste bedömas per synlig nodetikett och ändras inte maskinellt. |
| `Action` | `åtgärd` | `Åtgärdsslot`, `Åtgärdsslotar` och relaterade animeringstermer följer termlistan. |

## Säkra rättelser, redan avgränsade i UI-batch 02

Följande sex råexportposter är redan dubbelgranskade och finns i
`blender-ui-sv-review-batch-20261104-02.po`:

| Källa | Råexportens fel | Godkänd form |
| --- | --- | --- |
| `Slot` | `Slott` | `Slot` |
| `Slot Handle` | `Slotthandtag` | `Slothandtag` |
| `Slot Identifier` | `Slottidentifierare` | `Slotidentifierare` |
| `Slot Display Name` | `Slottvisningsnamn` | `Slotvisningsnamn` |
| `Action Slot Handle` | `Åtgärdsslotthandtag` | `Åtgärdsslothandtag` |
| `Not yet specified … data-block` | `datablokets` | `datablockets` |

## Avvikelse som kräver riktad uppföljning

Tre beskrivande RNA-strängar använder `biblioteksöverstyrning`:

- `BlendImportContextItem.library_override_id` beskriver den länkade ID-postens
  biblioteksåsidosättning.
- `IDOverrideLibrary.is_in_hierarchy` beskriver en biblioteksåsidosättning i
  en hierarki.
- `IDOverrideLibrary.is_system_override` beskriver en åsidosättningshierarki.

`biblioteksöverstyrning` finns inte bland de dokumenterade projektformerna.
Termlistan belägger i stället `biblioteksåsidosättning` för generell UI och
`biblioteksöverskrivning` för vissa operatörer. Detta är därför en verklig
terminologikrock, men den ska rättas i en separat, kontextkontrollerad
deltafil eftersom orden förekommer i känsliga RNA-/hierarkibeskrivningar.

## Medvetet ej normaliserat

- `Biblioteksöverskrivning` behålls i befintliga operatornamn tills varje
  operatörsgrupp har bedömts tillsammans. Detta följer termlistans uttryckliga
  kontextregel.
- `Vertex Color` → `Hörnfärg` förekommer i Grease Pencil- och färgattribut-
  kontext. Den formen kan vara en UI-domänetikett, inte en felöversättning av
  meshtermen `hörnpunktsfärg`.
- Identifierare som `VertexGroup`, `ActionChannelbag`, `ShaderFX` och
  `liboverride` är kodnamn och lämnas exakt.

## Slutsats

De högprioriterade termerna är i huvudsak konsekventa. UI-batch 02 tar hand
om de sex säkra slot-/datablockrättelserna. Nästa termbatch ska isolera de
tre RNA-strängarna med `biblioteksöverstyrning` och kontrollera deras
fullständiga grannkontext före ändring.
