# GNOME Text Editor — gnome-51/help — svensk hjälp

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnome-text-editor/gnome-51/help/sv/>.
- Aktuell POT hämtad 2026-11-27: 65 poster; SHA-256 `85fa85773350aa842d31c5076de79168d0e1721465755e247e4857c6f29c0c39`.
- Aktuell upstream-statistik: 65 översatta, 0 fuzzy, 0 oöversatta. `msgcmp` bekräftar att PO-filen matchar POT.
- Jämförelse med radgranskad `main/help`: 64 översättningsbara strängar har samma källtext och svenska översättningar. Den enda skillnaden är MD5-värdet i en källmarkerad extern bildreferens; den är inte användarvisad.
- De 64 gemensamma strängarna granskades med `main/help` som kontrollmall och GNOME-TM som stöd. 24 befintliga översättningar har tydliga grammatiska, idiomatiska eller terminologiska brister och rättades. Inga nya strängar behövde fyllas i. Ändringslistan finns i unified diffen.
- Översättarmetadata uppdaterad till Daniel Nylander <gnome@danielnylander.se>.

## Validering

- `msgcmp --use-fuzzy` mot senaste POT: godkänd; 65 poster.
- `msgfmt --check --check-format`: godkänd.
- `l10n-lint --language sv`: 0 fel, 0 varningar.
- Egen kontroll av markup-taggar och platshållare: oförändrade. Inga fuzzy eller tomma översättningar.
- Verktyget `hunspell-sv` saknas; systemets Hunspell `sv_SE` kördes på 64 synliga översättningar. De 23 okända tokenen är dokumenterade i `hunspell-unknown.txt`: markup/attribut, nyckelnamn, egennamn, Creative Commons-licensterm och godtagbara svenska sammansättningar.

## Inskickning

Inskickning och kommentar är blockerade: Damned Lies visar `No current actions` och anger att inloggning samt medlemskap i svenska teamet krävs. Filen är komplett lokalt men har inte skickats in.
