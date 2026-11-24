# NetworkManager — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/networkmanager/main/po/sv/>
- Aktuell Damned Lies-status: 2 520 översatta, 15 fuzzy och 31 oöversatta av 2 566 strängar; senaste POT skapades 2026-11-20.
- Granskad: 2026-11-23
- Ursprunglig och slutlig lokal statistik: 2 534 aktiva strängar, 0 oöversatta och 0 fuzzy.
- Ändringar: sex `nmcli`-hjälptexter korrigerades. Samtliga radbrytningar i formatsträngarna matchar källtexten. Svenskan i hjälpen för `remove`, `checkpoint`, `hostname` och `reload` har förtydligats. De tre kvarvarande `ARGUMENTS`-etiketterna i grammatiken för `hostname`, `reload` och Wi-Fi-kommandon har ändrats till `ARGUMENT`, i linje med övriga hjälptexter.
- Validering: `msgfmt --check` godkänd; `l10n-lint --language sv --skip-fuzzy` rapporterar 0 fel och 77 befintliga varningar. Hunspell-utfallet omfattar tekniska identifierare, protokoll, kommandon och engelska källord och kräver ingen automatisk ändring.
- Arkivet bygger på en äldre POT och katalogen behöver fortsatt omgranskas mot den aktuella grenen. Damned Lies PO har redan `ARGUMENT` i de två första hjälptexterna; Wi-Fi-definitionen innehöll ytterligare ett oöversatt `ARGUMENTS`.
- `msgfmt --check` godkänd; metavariabelregeln ger 0 träffar i samtliga 307 granskade arkivkataloger. Ingen ändring har skickats till GNOME.
