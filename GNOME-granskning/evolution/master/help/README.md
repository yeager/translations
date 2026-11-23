# Evolution — master/help

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/evolution/master/help/sv/>
- Granskad: 2026-11-23
- Lokal statistik: 2 068 aktiva strängar, 0 oöversatta och 0 fuzzy.
- Ändringar: Tre konkreta brister är rättade: en DocBook-formatbrist där skyddade `<code>`-värden hade översatts och gett obalanserade taggar, felaktigt singular i menytexten ”Visa borttagna meddelanden” samt det dubblerade ordet ”den”. Syntaxvärdena bevaras nu exakt som i källan.
- Validering: `msgfmt --check` godkänd. `l10n-lint` saknar fel; kvarvarande varningar gäller främst befintliga dokumentationsformuleringar, exempeldata och tekniska syntaxexempel som kräver separat radgranskning.
- Ingen ändring har skickats till GNOME.
