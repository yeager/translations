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
