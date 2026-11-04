# Motgranskning: Blender UI — `Library Override` i RNA-beskrivningar

Underlag: kandidatrapporten, UI-råexporten från 2026-11-04 och
`TERMINOLOGY.md`.

## Resultat

| Källreferens | Bedömning | Slutlig svensk form |
| --- | --- | --- |
| `bpy.types.BlendImportContextItem.library_override_id` | Godkänn | `Biblioteksåsidosättningen för det länkade ID:t. Den saknas tills den har skapats` |
| `bpy.types.IDOverrideLibrary.is_in_hierarchy` | Godkänn | `Anger om denna biblioteksåsidosättning ingår i en bibliotekshierarki eller är en enskild, isolerad och autonom åsidosättning` |
| `bpy.types.IDOverrideLibrary.is_system_override` | Godkänn | `Anger om denna biblioteksåsidosättning endast finns för åsidosättningshierarkin eller om användaren faktiskt kan redigera den` |

## Motivering

Den synliga UI-huvudformen är `Biblioteksåsidosättning`. Samma termfamilj
finns i aktuella UI-beskrivningar och felmeddelanden, bland annat
`biblioteksåsidosättnings-ID` och `åsidosättningshierarki`. De tre posterna
är RNA-sakbeskrivningar, inte operatörsetiketter. De ändras därför från
`biblioteksöverstyrning` till den belagda formen. Operatörernas avvikande
`biblioteksöverskrivning` omfattas inte.

Skrivregelskontrollen gav inga fel. Hunspell-resten
`åsidosättningshierarkin` är en korrekt facksammansättning. Ingen PO-fil har
ändrats.
