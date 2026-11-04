# Motgranskning: Blender Manual — fortsättning på `animation/actions.rst`

Underlag: `agent-animation-next-candidates-20261104.md`, råexporten
`blender-manual-manual-sv.po`, UI-exporten `blender-ui-ui-sv.po` och
`TERMINOLOGY.md`.

| Referens | Bedömning | Slutlig svensk form eller kommentar |
| --- | --- | --- |
| `actions.rst:201` | Godkänd | `För varje datablock i egenskapsredigeraren finns en animeringspanel med väljare för åtgärd och slot. Du kan använda dem för att tilldela åtgärder och slotar till ett datablock.` |
| `actions.rst:207` | Godkänd | `Väljaren för åtgärd och slot för kameradata i :doc:\`egenskapsredigeraren </editors/properties_editor>\`.` |
| `actions.rst:210` | Godkänd | `För det aktiva objektet kan du även tilldela dess åtgärd och slot i åtgärdsredigerarens rubrik.` |
| `actions.rst:220` | Godkänd | `:ref:\`Scenens animeringspanel <scene-properties-animation>\`` |
| `actions.rst:223` | Godkänd | `:ref:\`Maskens animeringspanel <mask-properties-animation>\`` |
| `actions.rst:243` | Godkänd | `Byta åtgärd för flera datablock` |
| `actions.rst:245` | Justera | `När du arbetar med en åtgärd som animerar flera datablock kan du behöva ersätta den med en annan åtgärd. Gör det samtidigt för alla dessa datablock, så att animering som hör ihop byts ut tillsammans. Det finns två alternativ för detta.` Den direkta uppmaningen återger källans avsedda samtidighet utan det ogrundade modala *bör*. |
| `actions.rst:250` | Godkänd | `Ersätt åtgärd` är exakt UI-etikett. |
| `actions.rst:251` | Godkänd | `Använder åtgärden för det aktiva objektet och ersätter den för alla objekt som animeras direkt av den. Användning i NLA-remsor och åtgärdsbegränsningar omfattas inte. Funktionen finns i :ref:\`Åtgärdsredigeraren <bpy.ops.anim.replace_action>\`.` |
| `actions.rst:255` | Godkänd | `Omdirigera användare` är exakt UI-etikett. |
| `actions.rst:256` | Justera | `Högerklicka på åtgärden i Outliner och välj :ref:\`Omdirigera användare <bpy.ops.outliner.id_operation>\`. Detta ersätter användningen för *alla* användare, även NLA-remsor och åtgärdsbegränsningar. Använd med försiktighet.` *För* beskriver här bättre Blenders datablocks-användare än kandidatens *hos*. |
| `actions.rst:263` | Godkänd | `Åtgärder kan även tilldelas NLA-remsor i ett datablocks NLA-system. Se dokumentationen för :doc:\`NLA-redigeraren </editors/nla/introduction>\` för information om hur du animerar datablock via NLA-systemet.` |

## Kontrollspår

- UI-exporten belägger `Rubrik`, `Åtgärdsredigerare`, `NLA-redigerare`,
  `Ersätt åtgärd` och `Omdirigera användare`.
- `slot`, `slotar`, `datablock` och `åtgärd` följer den projektspecifika
  terminologin och batch 25.
- Samtliga RST-roller och API-mål är bevarade. Råexport och deltafiler har
  inte ändrats i denna motgranskning.
