# gdk-pixbuf — master/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gdk-pixbuf/master/po/sv/>
- Senaste POT hämtad 2026-11-24; mallen är daterad 2026-11-10 och innehåller 198 aktiva poster. Den svenska originalfilen hade 244 poster totalt; 46 är äldre poster utanför POT. Den granskade filen innehåller exakt POT:ens 198 nycklar.
- Granskning: samtliga 198 aktiva strängar är radgranskade. 62 poster har tydliga korrigeringar i bildterminologi, tekniska felmeddelanden, grammatik eller pluralformer. Alla 198 poster är ifyllda och 0 fuzzy återstår.
- Terminologi: `sample` återges som *värde* i pixbuf-egenskaper, `rowstride` som *radsteg*, `codec` som *kodek*, `chunk` som *block* och C-strukturer som *strukturer*. `pixbuf`, filformat, färgrymder och tekniska standardnamn behålls där de är identifierare.
- Formatkontroll: `msgfmt --check` och `msgcmp --use-fuzzy` mot senaste POT godkända. C-platshållare och pluralformer matchar; de fyra svenska pluraluppsättningarna är fullständiga. katalogen innehåller inga acceleratorer eller markup.
- `l10n-lint --language sv`: 0 fel och 1 varning för den upprepade platshållaren `%lu` i en dimensionssträng. Verktyget tolkar `u` i `%lu` som ett dubblerat ord; platshållarna är korrekta och måste bevaras.
- Hunspell-sv: kontrollerad. Undantag gäller tekniska namn och sammansättningar, bland annat `pixbuf`, `pixbufen`, `pixbufens`, `gdk-pixbuf`, `ikonblock`, `bitmappsbild`, `Mac OS X`, `PNG`, `JPEG`, `TIFF`, `BMP`, `GIF`, `ICNS`, `ICO`, `PNM`, `QTIF`, `TGA`, `XBM`, `XPM`, `GDI+`, `QuickTime`, `RGB`, `RGBA`, `ISO-8859-1`, `seek`, `NULL` och formatnamn med svenska ändelser samt `u` i `%lu`-platshållare.
- Upstream visar 198 översatta, 0 fuzzy och 0 oöversatta före denna lokala granskning. Inget har skickats till GNOME.
