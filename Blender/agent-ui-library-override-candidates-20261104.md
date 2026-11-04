# Kandidater: Blender UI — `Library Override` i RNA-beskrivningar

Datum: 2026-11-04
Källa: `exports/2026-11-04/blender-ui-ui-sv.po`.

## Termbeslut

Den synliga huvudetiketten `Library Override` översätts i den aktuella
UI-katalogen som `Biblioteksåsidosättning`. Samma form används även i
närliggande RNA-beskrivningar som `Library override data`, i
hierarkibeskrivningar och i felmeddelanden. Operatörernas avvikande form
`biblioteksöverskrivning` är därför inte relevant här: de tre posterna
nedan är sakbeskrivningar av `IDOverrideLibrary`, inte operatörsnamn.

## Säkra delta-kandidater

| Källreferens | Exakt `msgid` | Nuvarande måltext | Rekommenderad `msgstr` |
| --- | --- | --- | --- |
| `bpy.types.BlendImportContextItem.library_override_id` | `The library override of the linked ID. None until it has been created` | `Biblioteksöverstyrningen för det länkade ID:t. Den saknas tills den har skapats` | `Biblioteksåsidosättningen för det länkade ID:t. Den saknas tills den har skapats` |
| `bpy.types.IDOverrideLibrary.is_in_hierarchy` | `Whether this library override is defined as part of a library hierarchy, or as a single, isolated and autonomous override` | `Anger om denna biblioteksöverstyrning definieras som del av en bibliotekshierarki eller som en enskild, isolerad och autonom överstyrning` | `Anger om denna biblioteksåsidosättning ingår i en bibliotekshierarki eller är en enskild, isolerad och autonom åsidosättning` |
| `bpy.types.IDOverrideLibrary.is_system_override` | `Whether this library override exists only for the override hierarchy, or if it is actually editable by the user` | `Anger om denna biblioteksöverstyrning endast finns för överstyrningshierarkin eller om användaren faktiskt kan redigera den` | `Anger om denna biblioteksåsidosättning endast finns för åsidosättningshierarkin eller om användaren faktiskt kan redigera den` |

## Avgränsning

Förslagen ändrar enbart det icke-kodmässiga sakordet och bevarar ID, RNA- och
API-identifierare. De ska läggas i en separat UI-deltafil och granskas med
`msgfmt`, l10n-lint, svlang, Hunspell, Gitleaks och `git diff --check` innan
uppladdning.
