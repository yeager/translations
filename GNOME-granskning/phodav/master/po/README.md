# Phodav — master/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/phodav/master/po/sv/>
- Granskad: 2026-11-23
- Lokal statistik: 32 aktiva strängar, 0 oöversatta och 0 fuzzy.
- Ändringar: Den Damned-Lies-genererade svenska katalogen var helt oöversatt; 32 kommandorads- och diagnostiksträngar har översatts.
- Källavvikelse: aktuell Git `master` innehåller en äldre svensk fil med 19 översatta strängar (POT 2022-06-29), medan Damned Lies erbjuder den nyare 32-strängarsmallen (POT 2026-10-22). Arkivets original är därför exakt den aktuella Damned-Lies-filen, inte den äldre Git-filen.
- Validering: `msgfmt --check` godkänd; `l10n-lint` rapporterar 0 fel. Informationsnotisen gäller ett avsiktligt svenskt tankstreck i programmets kortbeskrivning. Hunspell-undantag: kommandoradsflaggor, `DIGEST`, `TLS`, `WebDAV`, `htdigest`, `mDNS` och `loopback`.
- Ingen ändring har skickats till GNOME.
