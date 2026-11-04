# Införandeplan: Blender UI — åtgärdsslotar och datablock

Underlag: `agent-ui-next-candidates-20261104.md` och den oberoende
motgranskningen `agent-ui-next-review-20261104.md`. Planen är kontrollerad
mot råexporten `exports/2026-11-04/blender-ui-ui-sv.po`.

De sex posterna nedan är inte en dubblett av UI-batch 01 och kan läggas i en
separat deltafil. Inga markeringar, parametrar eller API-namn ändras.

| Referens i råexport | Exakt `msgid` | Slutlig `msgstr` |
| --- | --- | --- |
| `space_node.py:530` m.fl. | `Slot` | `Slot` |
| `bpy.types.ActionSlot.handle` | `Slot Handle` | `Slothandtag` |
| `bpy.types.ActionSlot.identifier` | `Slot Identifier` | `Slotidentifierare` |
| `bpy.types.ActionSlot.name_display` | `Slot Display Name` | `Slotvisningsnamn` |
| `bpy.types.AnimData.action_slot_handle` m.fl. | `Action Slot Handle` | `Åtgärdsslothandtag` |
| `bpy.types.ActionSlot.target_id_type:'UNSPECIFIED'` | `Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block` | `Inte angiven ännu. När denna slot först tilldelas ett datablock anges den till datablockets typ` |

## Terminologiskt beslut

*Slot* är den fastställda Blender-termen i denna animeringskontext.
`Slott` betyder en byggnad och är därför en sakfelaktig målform här.
Sammansättningarna använder samma stam: `Slothandtag`, `Slotidentifierare`,
`Slotvisningsnamn` och `Åtgärdsslothandtag`. Rättelsen `datablockets`
återställer det utelämnade `c` i den etablerade formen *datablock*.

Före införande i en PO-deltafil ska batchen kontrolleras med `msgfmt`,
`l10n-lint`, `svlang`, Hunspell, Gitleaks och `git diff --check`.
