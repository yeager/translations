# Evolution — master/help

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/evolution/master/help/sv/>
- Granskad: 2026-11-23
- Lokal statistik: 2 068 aktiva strängar, 0 oöversatta och 0 fuzzy.
- Ändringar: Fem konkreta brister är rättade: en DocBook-formatbrist där skyddade `<code>`-värden hade översatts och gett obalanserade taggar, felaktigt singular i menytexten ”Visa borttagna meddelanden”, det dubblerade ordet ”den” samt två platser där skyddade variabel- och formatsträngar hade lokaliserats trots uttrycklig källkommentar.
- Validering: `msgfmt --check` godkänd. `l10n-lint` saknar fel och rapporterar 34 kvarvarande varningar; de gäller främst befintliga dokumentationsformuleringar, exempeldata och tekniska syntaxexempel som kräver separat radgranskning.
- Ingen ändring har skickats till GNOME.
