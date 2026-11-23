# Gitte — main — gränssnitt

- GNOME-status: [aktivitetssida](https://l10n.gnome.org/vertimus/gitte/main/po/sv/)
- Uppströmskälla: `https://codeberg.org/ckruse/Gitte`, gren `main`, hämtad 2026-11-22.
- Ursprunglig Damned Lies-katalog: 1 062 översatta, 2 fuzzy och 13 oöversatta efter synkronisering mot aktuell POT.
- Granskad katalog: 1 077 översatta, 0 fuzzy och 0 oöversatta.

13 verkligt oöversatta gränssnittstexter fylldes i och två fuzzy-poster granskades. Befintlig svenska rättades även där lint hittade verkliga problem i skiljetecken, typografiska citattecken, plural, tekniska globmönster och formuleringar.

Validering: `msgfmt --check`, plats- och formatkontroll mot aktuell POT samt `l10n-lint --language sv` gav 0 fel och 0 varningar. `hunspell-sv` har granskats; dess återstående träffar är produktnamn, Git-/CLI-syntax, protokoll, kod och tekniska sammansättningar.

Den svenska katalogen har därefter synkroniserats mot Damned Lies senaste POT: 1 133 aktiva strängar, 0 fuzzy och 0 oöversatta. Den uppdaterade granskningen innehåller nio faktiska svenska ändringar och klarar åter `msgfmt --check` samt `l10n-lint --check --language sv`. Den skickades 2026-11-23 via Damned Lies API med kommentaren `Granskad och klar`; API:t returnerade `{"result":"OK"}`.
