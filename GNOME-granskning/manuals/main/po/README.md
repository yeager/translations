# Manuals — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/manuals/main/po/sv/>
- Granskad: 2026-11-24
- Aktuell status hämtad: 2026-11-27
- Aktuell POT: 51 aktiva strängar; POT-datum 2026-09-21, hämtad direkt från Damned Lies 2026-11-27; 51 översatta, 0 fuzzy och 0 oöversatta efter granskning.
- Nya översättningar: 0
- Rättade befintliga översättningar: 5

## Ändringar

Rättningar omfattar bestämd form, idiomatiskt gränssnittsspråk, *Fritextsökning*, korrekt livscykelstatus samt borttagning av en felaktigt tillagd accelerator i en sträng som saknar sådan i källan.

## Validering

`msgfmt --check`, `msgcmp --use-fuzzy` och `l10n-lint` har körts utan fel eller varningar. Informationsnotisen gäller Avbryt med avsiktligt svensk accelerator. Platshållare är korrekta; svenska acceleratorer använder enbart grundläggande latinska bokstäver.

Svensk Hunspell-kontroll flaggar bara produkt-/formatnamnen `Builder`, `GTK`, `SDK` och `devhelp`, nyckelordet `docs` samt delordet `vbryt` i acceleratorn `A_vbryt`; alla har kontrollerats i sitt sammanhang.

Uppladdad via Damned Lies API 2026-11-27 02:14 UTC med kommentaren ”Granskad och klar”. Aktivitetssidan bekräftar 51/0/0.
