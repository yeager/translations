# Textredigerare — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnome-text-editor/main/po/sv/>
- Aktuell POT: 292 aktiva poster. Den hämtade svenska katalogen hade 6 oöversatta och 4 fuzzy-poster; den granskade filen har 0 oöversatta och 0 fuzzy.
- Granskning: hela katalogen är radgranskad. Sex nya översättningar har tillkommit och 52 befintliga poster har rättats för idiomatik, grammatik, teknisk betydelse och konsekvent GNOME-terminologi.
- Acceleratorer: inga `_ä`, `_å` eller `_ö`; acceleratorerna använder ASCII-bokstäver.
- Validering: `msgfmt --check` och `l10n-lint --check --language sv` utan fel. Aktuell POT och granskad katalog har samma uppsättning aktiva nycklar; pluralformen för `%u` har kontrollerats separat.
- Hunspell: tekniska identifierare och avsiktliga förkortningar är manuellt kontrollerade undantag, bland annat `GtkSourceView`, `NSURL`, `NULL`, `ILCreateFromPath`, `LF`, `CR`, `UTF-8`, `editorconfig` och kommandoflaggan `--ignore-session`. Fragment som uppstår när Hunspell delar acceleratorsträngar ignoreras.
- GNOME-inskick: uppladdad till Damned Lies 2026-11-23 efter reservation, med kommentaren `Granskad och klar` (`{"result":"OK"}).

## Korrigering av kommandoradsmetavariabler (2026-11-24)

- 1 befintlig sträng korrigerad: beskrivande kommandoradsargument översatta till svenska.
- Validering: `msgfmt --check`; `l10n-lint`-regeln `metavariable-translation` ger inga kvarvarande träffar i de 295 granskade huvudgrenarnas kataloger.
- Ändringen är lokal och har inte skickats till GNOME.

## Uppföljning efter tidigare uppladdning

En kommandoradsmetavariabel korrigerades 2026-11-24 efter uppladdningen 2026-11-23. Den aktuella katalogen är komplett mot POT; uppföljningsändringen väntar på inskickning.

`l10n-lint` ger 0 fel och 1 varning om identiska pluralformer för `About %u year(s) ago`; identiskt `år` är korrekt på svenska i singular och plural. Gränsnotiserna beror på giltigt flyttade ASCII-acceleratorer.

- Hunspell: `hunspell-unknown.txt` innehåller stavningslexikonets okända token från den aktuella granskade filen. Träffarna är kontrollerade: tekniska namn/flaggar och svenska sammansättningar, acceleratorfragment samt i Ptyxis den avsiktliga fontprovstexten `hwila` (pangram med bokstaven w). För GNOME Text Editor är pluralvarningen för `år` dokumenterad; samma form är korrekt på svenska.
