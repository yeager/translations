# Hunspell-undantag

Kontrollerat med `hunspell -d sv_SE`. Flaggningarna är namn, kommandon, protokoll eller tekniska sammansättningar:

- `PackageKit`, `PackageKit-tjänst`, `PackageKits`, `pkgcli`, `pkgcli-version`: produkt- och kommandonamn.
- `--help`, `auto`, `details`, `group`, `name`, `prepare`, `trigger`, `update`, `update-packages`, `list-os-upgrades`: kommandoflagga, parametervärde eller kommandonamn; bevaras exakt.
- `CVE:er`, `GPG-verifiering`: etablerade säkerhetsförkortningar.
- `Paketmetadata`, `paketmetadata`, `paketmetadata.`: teknisk sammansättning; punkteringen i sista formen är meningsslut.
- `nätverksproxyn`: korrekt bestämd sammansättning.
