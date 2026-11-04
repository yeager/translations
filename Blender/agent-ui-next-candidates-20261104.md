# Kandidater: Blender UI — action slots och datablock

Källa: `exports/2026-11-04/blender-ui-ui-sv.po`.
Avgränsning: Action Slots i `bpy.types.ActionSlot` och närliggande
animationsegenskaper. Kontrollerad mot `TERMINOLOGY.md`, där *slot* är den
fastställda Blender-termen, och mot tidigare UI-deltafiler.

Följande sex ändringar är inte upptagna i den befintliga UI-batchen och är
säkra kandidatposter för oberoende motgranskning.

| Referens | `msgid` | Nuvarande svensk text | Föreslagen svensk text | Skäl |
| --- | --- | --- | --- | --- |
| `ActionChannelbag.slot` m.fl. | `Slot` | `Slott` | `Slot` | *Slott* betyder byggnaden, medan det fastställda tekniska begreppet här är *slot*. |
| `ActionSlot.handle` | `Slot Handle` | `Slotthandtag` | `Slothandtag` | Utgår från det fastställda *slot*, inte substantivet *slott*. |
| `ActionSlot.identifier` | `Slot Identifier` | `Slottidentifierare` | `Slotidentifierare` | Samma terminologiska rättelse. |
| `ActionSlot.name_display` | `Slot Display Name` | `Slottvisningsnamn` | `Slotvisningsnamn` | Samma terminologiska rättelse. |
| `AnimData.action_slot_handle` m.fl. | `Action Slot Handle` | `Åtgärdsslotthandtag` | `Åtgärdsslothandtag` | Samma termstam i sammansatt UI-etikett. |
| `ActionSlot.target_id_type:'UNSPECIFIED'` | `Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block` | `Inte angiven ännu. När denna slot först tilldelas ett datablock anges den till datablokets typ` | `Inte angiven ännu. När denna slot först tilldelas ett datablock anges den till datablockets typ` | Ren stavningsrättelse: *datablokets* saknar `c`. |

## Avgränsningar

- Inga ändringar föreslås för *vertex*: den aktuella exporten använder redan
  den fastställda termen *hörnpunkt* i dessa UI-strängar.
- Flera `l10n-lint`-träffar är avsiktliga produktnamn, kodidentifierare,
  filformat eller källtextens egen interpunktion och tas inte med.
- Den felaktiga fallback-översättningen för `3D View Tool: Paint Grease
  Pencil, Trim (fallback)` föreslås inte här eftersom den redan ingår i
  `blender-ui-sv-review-batch-20261104-01.po`.
