# Telegnome — master — svensk dokumentation

- Katalog: [Telegnome Help i Damned Lies](https://l10n.gnome.org/vertimus/telegnome/master/help/sv/)
- Senaste POT hämtad 2026-11-25: `https://l10n.gnome.org/POT/telegnome.master/docs/telegnome-help.master.pot`
- POT SHA-256: `0385a8c4149512f73fe39cd7f6131fa1b948a214c47babaea25640d27d70c96b`
- Före granskning: 31/31 översatta, 0 fuzzy, 0 oöversatta.
- Efter granskning: 31/31 översatta, 0 fuzzy, 0 oöversatta.
- Ändringar: 12 befintliga strängar rättade; inga nya översättningar.
- Last-Translator i katalogen: Daniel Nylander <gnome@danielnylander.se>.

## Validering

- `msgfmt --check`: godkänd.
- `msgcmp` mot den senaste POT-filen: godkänd.
- `l10n-lint --language sv --reference telegnome-help.master.pot`: 0 fel, 1 varning. Varningen gäller kolon efter engelska `For example:`; den svenska meningen har omformulerats till `Om du till exempel …`, där kolon inte behövs. Två informationsnotiser gäller placeholdern `TBD.` (`Kommer senare.`) och DocBook-taggen `<application>` som står först i den svenska meningen.
- Egen kontroll: samtliga DocBook-taggar, formatmarkörer och radbrytningar är bevarade. Undantag för tagg-/radbrytningsjämförelsen: `translator-credits` är en dynamisk kreditering med avsiktligt annat innehåll än källnyckeln.
- `hunspell-sv`: kontrollerad. Kvarvarande träffar är författarnamn och produkt-/licensnamn (`TeleGNOME`, `GNU General Public License`, `Free Software Foundation`) samt den korrekta sammansättningen `undersidenummer`.

Ingen GNOME-inskickning har gjorts.

## Filer

- [Original PO](telegnome.master.help.sv.original.po)
- [Granskad PO](telegnome.master.help.sv.reviewed.po)
- [Diff](telegnome.master.help.sv.diff)
- [Senaste POT](telegnome-help.master.pot)

- GNOME-inskick: 2026-11-26 via Damned Lies API; kommentaren `Granskad och klar` och aktivitetssidan verifierade; statistik 31/0/0.
