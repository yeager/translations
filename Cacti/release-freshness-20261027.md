# Cacti: kontroll av aktuell release

Kontrollerad 2026-10-27 mot Cactis officiella GitHub-releaser.

Den senaste stabila releasen är `release/1.2.31`, publicerad 2026-06-15. Den
uppfyller 48-månadersregeln och Cacti-komponenterna kan därför granskas vidare.

## Routerconfigs

Den lokala komponentvisa filen
`cacti-routerconfigs-sv-basreparationer-20261027.po` innehåller 90 säkra
rättningar. Den passerar `msgfmt`, `l10n-lint` utan fel eller varningar,
`svlang` utan anglicismer och Gitleaks utan hemligheter. Hunspell träffar
endast produkt- och protokollnamnen Cacti, SCP och TFTP samt det korrekta
fackordet ”direktutdata”.

Terminologibanken stödjer bland annat ”säkerhetskopia” för *backup* och
”tidsgräns” för *timeout*. Kontexten motiverar den mer idiomatiska rubriken
”Standardtidsgräns” i stället för termbankens bokstavliga ”Standard timeout”.

Filen är fortfarande inte inskickad. Kontrollera den aktuella komponentens
käll- och målsträngar i Cacti Translate före en komponentvis import.

## Thold

Thold är ett separat Cacti-tillägg. Den senaste stabila releasen är `v1.8.2`,
publicerad 2024-10-16, och uppfyller därmed också 48-månadersregeln.

Den lokala filen `cacti-thold-meddelandemallar-20261027.po` innehåller åtta
rättningar i status- och e-postmallar. Den passerar `msgfmt`, `l10n-lint`,
`svlang`, Hunspell och Gitleaks. En separat kontroll bekräftar att varje
HTML-tagg och platshållare är identisk med respektive källsträng.

Termbanken föreslår ibland ”varning” för *alert*, men Tholds källtexter
skiljer uttryckligen på *alerts* och *warnings*. I den här komponenten är
”larm” respektive ”varning” därför avsiktliga och kontextkorrekta termer.
Filen är inte inskickad och ska jämföras med aktuell måltext före uppladdning.
