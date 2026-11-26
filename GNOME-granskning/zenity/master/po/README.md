# Zenity — master/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/zenity/master/po/sv/>
- Granskad: 2026-11-26
- Aktuell POT: 203 aktiva strängar; 203 översatta, 0 fuzzy och 0 oöversatta. POT skapad 2026-11-25 21:43 UTC.
- Damned Lies markerar modulen som inaktiv och visar inga aktuella åtgärder. Den senaste POT-filen och svenska PO-filen är tillgängliga.
- Nya översättningar: 0
- Rättade befintliga översättningar: 63
- `Last-Translator` uppdaterad till Daniel Nylander <gnome@danielnylander.se>.

## Validering

- `msgfmt --check --statistics`: godkänd, 203 översatta meddelanden.
- `msgcmp --use-fuzzy` mot senaste POT: godkänd.
- `l10n-lint --language sv --reference zenity.master.po.pot`: 0 fel och 3 varningar. Samtliga tre gäller engelsk källmetadata med formen `(Since: 4.x)`, naturligt återgiven på svenska som `(från version 4.x)` utan kolon. Informationsnotiser gäller svensk procentplacering, acceleratorn för `_Cancel` och svensk formulering runt en kryssruteetikett.
- Egna kontroller: samtliga 203 nycklar matchar; C-platshållare, XML/HTML-markup, radbrytningar och antal acceleratorer matchar källan.
- `hunspell-sv` kördes på ändrade texter. Undantag: `Ikonfilen` (böjd form av den korrekta sammansättningen *ikonfil*) och `Zenity` (produktnamn). Se `hunspell-sv-undantag.txt`.

Ingen GNOME-inskickning har gjorts.
