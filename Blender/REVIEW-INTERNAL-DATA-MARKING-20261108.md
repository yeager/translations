# Blender UI – intern datamarkering, batch 1 259

`bpy.types.ID.tag` beskriver en intern flaggning av data, inte användarskapade
resurs- eller tilläggstaggar. Därför ändras verbet *tagga* till det idiomatiska
*märka*; UI-etiketter för användarskapade taggar lämnas orörda.

| Källa | Tidigare | Granskad svensk text |
| --- | --- | --- |
| Tools can use this to tag data for their own purposes (initial state is undefined) | Verktyg kan använda detta för att tagga data för sina egna syften (standardvärdet är odefinierat) | Verktyg kan använda detta för att märka data för egna ändamål (ursprungligt tillstånd är odefinierat) |

Den granskade Blender-TM:n innehöll redan den valda formuleringen och behövde
inte ändras. `msgfmt`, l10n-lint, svlang (konsekvens, skrivregler och
svengelska), Hunspell och Gitleaks passerade utan avvikelser.

SHA-256: `f1532192ed2bbfb452b140dca48de06c7a50a297f5685ed67a282bda0d715ccd`.

Status: lokalt granskat och arkiverat. Weblate-import kräver separat verifiering.
