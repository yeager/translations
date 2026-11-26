# Gcolor3 — master/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gcolor3/master/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 59 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 7

## Ändringar

Granskningen rättar ordagrann och oidiomatisk svenska i programmets
beskrivning, förtydligar texter om sparade färger och färgprover samt
normaliserar terminologin för utdata och färgnamn. PO-rubriken uppdateras med
Daniel Nylander som senaste översättare.

## Validering

- `msgfmt --check`: godkänd
- `msgcmp --use-fuzzy` mot den aktuella POT-filen: godkänd
- `l10n-lint`: 0 fel och 0 varningar. Informationsnotisen för `S_aturation:`
  gäller en avsiktlig, giltig svensk accelerator.
- `hunspell-sv`: rimliga undantag är GTK, Gcolor2, Christopher Davis och
  terminologin `färgvalsdialog`.

Den granskade filen är komplett och fuzzy-fri. Ingen inskickning till GNOME
har gjorts i detta steg.

- GNOME-inskick: 2026-11-26 via Damned Lies API; kommentaren `Granskad och klar` och aktivitetssidan verifierade; statistik 59/0/0.
