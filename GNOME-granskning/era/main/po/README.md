# Era — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/era/main/po/sv/>
- Granskad: 2026-11-23
- Lokal statistik: 151 aktiva strängar, 0 oöversatta och 0 fuzzy.
- Ändringar: Den Damned-Lies-genererade katalogen saknade svensk text. 142 exakta träffar från Eras aktuella svenska Git-katalog har återanvänts och kontrollerats; nio nya strängar för kalenderborttagning, heldagshändelser och kalenderstartsida är översatta manuellt.
- Källavvikelse: Git `main` innehåller en äldre 143-strängars svensk fil som redan är komplett. Arkivets original är den nyare 151-strängarsfilen från Damned Lies.
- Validering: `msgfmt --check` godkänd; `l10n-lint` rapporterar 0 fel. Tre informationsnotiser gäller acceleratortecken, formatsträngen `%0B %Y` och tekniska identifierare. Hunspell-undantag: `caldav`, `Calendar` och formatvariabler.
- Ingen ändring har skickats till GNOME.
