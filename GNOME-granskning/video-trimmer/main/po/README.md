# Video Trimmer — main/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/video-trimmer/main/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 69 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 7

## Ändringar

Granskningen rättar konsekvent terminologi för utdatafiler och tidsstämplar,
en svensk verbform samt några korta, användarvisade formuleringar. Rubriken
anger Daniel Nylander som senaste översättare enligt den överenskomna
metadataregeln.

## Validering

- `msgfmt --check`: godkänd
- `msgcmp --use-fuzzy` mot den aktuella POT-filen: godkänd
- `l10n-lint`: 0 fel, 0 varningar; en informationsnotis gäller den giltiga
  acceleratorn i `A_vbryt`.
- `hunspell-sv`: tekniska undantag är Flatpak, Identity, ffmpeg-underprocess
  och den korrekta sammansättningen `standardutdatafilens`.

Den granskade filen är komplett och fuzzy-fri. Ingen inskickning till GNOME
har gjorts i detta steg.
