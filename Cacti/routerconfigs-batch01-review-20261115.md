# Cacti `routerconfigs`: svensk granskningsbatch 01, 2026-11-15

- Komponent: `cacti/routerconfigs` på Cacti Translate.
- Aktuell status före batchen: 79,2 % översatt, 67 tomma och 14 fuzzy
  poster enligt färsk svensk PO-export.
- Omfattning: 41 entydiga etiketter för massredigering, återkörning,
  schemaläggning, datum, konfigurationsskillnader och status.
- Källkontext: `includes/arrays.php`, `includes/functions.php` och
  `includes/scheduler.php`.
- Återstår efter denna lokala batch: längre instruktioner och säkerhetstexter,
  samt fuzzy-poster som måste jämföras med aktuell funktion.

## Kontroller

- `msgfmt --check`: syntaktiskt godkänd; den minimala deltafilen saknar
  frivilliga revisionsfält i headern.
- `l10n-lint`: inga fel; sju versalvarningar för veckodagar är medvetna,
  eftersom svenska veckodagsnamn skrivs med liten bokstav.
- `svlang`: 10,0/10.
- Hunspell svenska, Gitleaks och `git diff --check`: godkända.
- Weblate-import: 41 uppdaterade, 0 hoppade över och 0 saknade strängar.
  Den uppladdade deltafilen sammanfogades med läget ”Lägg till som
  översättning” och konflikthanteringen ”Ändra endast oöversatta strängar”.
- Direkt verifierad komponentstatus efter import: 343 av 381 strängar
  översatta (89,5 %); 38 är fortfarande ofärdiga, varav 25 tomma och 13
  behöver redigeras.
- Status: lokalt granskat, arkiverat, inskickat och importerat. Projektets
  fortsatta granskning och releasepublicering är inte verifierade.
