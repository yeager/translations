# WirePlumber — svenska `master/po`

Katalogen hämtades från GNOME Damned Lies den 2026-11-28 och radgranskades mot aktuell POT.

- [GNOME-aktivitetssida](https://l10n.gnome.org/vertimus/wireplumber/master/po/sv/)
- [Aktuell POT](https://l10n.gnome.org/POT/WirePlumber.master/WirePlumber.master.pot)
- [Aktuell PO](https://l10n.gnome.org/POT/WirePlumber.master/WirePlumber.master.sv.po)
- POT SHA-256: `cfa4f3fff6adca7671c6c874e468f2f64bc2fa9a7f0ccc9250bd68b921f8ec9b`
- PO SHA-256: `e03c94993dbef460749b377087e3556a2f45b09d78c690da81f33fc75e1429d0`

## Resultat

| Mätning | Före | Efter lokal granskning |
|---|---:|---:|
| Aktiva strängar | 61 | 61 |
| Översatta | 50 | 61 |
| Fuzzy | 7 | 0 |
| Oöversatta | 4 | 0 |
| Nya översättningar | — | 4 |
| Rättade befintliga/fuzzy-texter | — | 33 |
| Fuzzy-poster granskade | — | 7 (7 rättade, 0 bekräftade) |
| Ändrade textvärden totalt | — | 37 |

Granskningen ersätter bland annat felaktiga auto-växlingsetiketter och oöversatta inställningsbeskrivningar. `sink`/`source` hanteras som ljudutgång/ljudkälla, `ducking` som automatisk volymsänkning och `media.role` bevaras som teknisk egenskap.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd.
- `l10n-lint --language sv --no-terminology`: 0 fel, 0 varningar.
- Egen POT-/formatkontroll: 0 saknade/extra källnycklar, 0 fuzzy, 0 tomma strängar, 0 avvikelser i platshållare, markup, URL:er eller acceleratorantal.
- `hunspell -d sv_SE -l`: 12 flaggade termer, samtliga manuellt bedömda och dokumenterade i [`hunspell-exceptions.md`](hunspell-exceptions.md). Full utdata finns i [`hunspell-output.txt`](hunspell-output.txt).
- `swedish-tm` konsulterades; se [`tm-check.md`](tm-check.md).

Ingen ändring har skickats till GNOME Damned Lies.
