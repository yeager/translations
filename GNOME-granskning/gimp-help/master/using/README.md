# GIMP Help — master — using — svenska

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/master/using/sv/>.
- Aktuell källfil: GNOME POT skapad 2026-11-24 22:45 UTC; katalogen omfattar 1 105 aktiva poster.
- Status före och efter lokal granskning: 1 105 översatta, 0 fuzzy, 0 oöversatta enligt GNOME Damned Lies.
- Genomgång: samtliga 1 040 aktiva textsträngar radgranskade. Rättade 630 befintliga översättningar. Inga nya översättningar behövdes och 0 strängar återstår.
- Icke översättbara poster: 65 aktiva bildhashreferenser (`@@image:`), synkroniserade exakt mot POT. 87 inaktuella/obsolete poster behölls oförändrade.
- Terminologi: GIMP:s verktygsetikett `Bucket Fill` återges som **Fyll**; i löptext används ”verktyget Fyll”. `tile` = **bricka**, `tile cache` = **brickcache**. Kod, funktionsnamn, filnamn och UI-etiketter har granskats i sitt sammanhang.
- Översättarmetadata: Daniel Nylander <gnome@danielnylander.se>, 2026-11-26.

## Validering

- `msgfmt --check --statistics`: godkänd; 1 105 översatta meddelanden.
- `msgcmp` mot senaste POT: godkänd.
- XML-markup, formatplatshållare och nyckel-/musknappsinnehåll: egen kontroll godkänd för alla 1 040 aktiva textsträngar.
- `l10n-lint --language sv --reference gimp-help.master.using.master.pot`: 0 fel, 36 varningar. 23 gäller interpunktion, 7 meningsslut, 2 upprepat ord i gränssnittstext, 2 interpunktionskonsistens, 1 skyddad DocBook-text och 1 falsk-vän-träff. De kvarvarande skillnaderna är granskade: svenska interpunktioner är naturliga i sammanhanget; ”Inmatningsenheter” motsvarar samma etablerade GIMP-term för både *Input Devices* och *Input Controllers* i den aktuella GNOME-TM:n; bildens genererade XCF-titel är lokaliserad; *current* har korrekt återgetts som ”aktuell”.
- `hunspell-sv`: körd på ändrade svenska texter efter att PO-markup, filvägar och kod har tagits bort. Ordlistan flaggar tekniska identifierare, GIMP- och Scheme-termer samt giltiga sammansättningar; de har granskats manuellt. Exempel på dokumenterade undantag: Bézierkurva, alfagenomskinlighet, brickcache, flikmenyknapp, indataljusstyrka, penselrörspensel, snabbmaskläge, toningslängd, `caadr`, `cddr`, `Gimp.ImageProcedure.new` och `--no-fonts`. Den fullständiga rålistan finns i `hunspell-sv-okända-ord.txt`.

## Arkivfiler

- Original före ändring: `gimp-help.master.using.sv.original.po`
- Granskad fil: `gimp-help.master.using.sv.reviewed.po`
- Diff: `gimp-help.master.using.sv.review.diff`
- POT: `gimp-help.master.using.master.pot`
- Lintresultat: `l10n-lint.json`
- Hunspell-ord att beakta: `hunspell-sv-okända-ord.txt`

Inget har skickats in till GNOME Damned Lies.
