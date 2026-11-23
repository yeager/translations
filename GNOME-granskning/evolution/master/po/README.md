# Evolution — master/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/evolution/master/po/sv/>
- Delgranskad: 2026-11-23
- Lokal statistik: 6 389 aktiva strängar, 0 oöversatta och 0 fuzzy.
- Ändringar: 66 konkreta brister rättades: 39 nordiska acceleratorer, 13 datum-/tidsformat med saknade platshållare, en formatsträng med en extra radbrytning samt tretton språk- och formatdetaljer.
- Validering: `msgfmt --check` godkänd; `l10n-lint --language sv --skip-fuzzy` rapporterar 0 fel och 51 återstående varningar. Hunspell kräver separat, kontextuell hantering av tekniska termer och är inte skäl att ändra dem automatiskt.
- Katalogen är **inte klar**: alla 6 389 aktiva strängar återstår att radgranska. Ingen ändring har skickats till GNOME.
