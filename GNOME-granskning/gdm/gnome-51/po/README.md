# GDM — gnome-51/po

- **GNOME-katalog:** [gdm/gnome-51/po/sv](https://l10n.gnome.org/vertimus/gdm/gnome-51/po/sv/)
- **Källor:** Damned Lies API och aktuell POT/PO hämtade 2026-11-28. POT skapades 2026-11-24 18:08 UTC.
- **Före granskning:** 118/118 aktiva poster översatta, 0 fuzzy, 0 oöversatta.
- **Efter granskning:** 118/118 aktiva poster översatta, 0 fuzzy, 0 oöversatta. 0 nya översättningar och 71 ändrade befintliga poster.
- **Omfattning:** samtliga 118 aktiva poster radgranskade mot senaste POT. Obsoleta poster lämnades orörda. `Last-Translator` är uppdaterat till Daniel Nylander <gnome@danielnylander.se>.
- **Aktivitet:** aktivitetsidan visar att `gnome-50` också har aktivitet i en annan gren. Den grenen har inte hämtats eller ändrats. Ingen uppladdning har gjorts.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd; samma 118 aktiva nycklar.
- Platshållare, radbrytningar och markup: jämförda; inga avvikelser. Kommandon, kommandonycklar och formatsträngar bevarade.
- Acceleratorer: inga i denna katalog.
- `l10n-lint --language sv`: 0 fel och 5 varningar. Varningarna gäller fullständiga svenska meningsgränser i felmeddelanden där källan har kommatecken, samt citattecken runt det tekniska värdet `%s` i root-felet. De är avsiktliga och meningsbevarande.
- `hunspell -d sv_SE -l`: alla flaggade ord granskades. Undantag är tekniska namn och identifierare (`GDM`, `GNOME`, `PAM`, `dconf`, `system-db`, `true`, `--help`), oförändrade CLI-kommandon (`help`, `password`, `fingerprint`, `reset`) samt korrekta tekniska termer och sammansättningar (`root`, `Anroparen`, `GDM-PAM-modul`, `Standardutdata`, `Felutdata`, `distributionshook`, `hookskript`). Inga ord lades till i ordlistan.

## Filer

- Original: `gdm.gnome-51.sv.original.po`
- Granskad: `gdm.gnome-51.sv.reviewed.po`
- Diff: `gdm.gnome-51.sv.diff`
- POT: `gdm.gnome-51.pot`
