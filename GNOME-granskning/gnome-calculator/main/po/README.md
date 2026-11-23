# Kalkylator — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnome-calculator/main/po/sv/>
- Aktuell POT: 795 aktiva poster. Den hämtade svenska katalogen hade 2 oöversatta och 3 fuzzy-poster; den granskade filen har 0 oöversatta och 0 fuzzy.
- Granskning: hela katalogen är radgranskad. Två nya översättningar har tillkommit och 85 befintliga poster har rättats för matematisk och finansiell terminologi, valuta- och enhetsnamn, grammatik samt idiomatik.
- Acceleratorer: inga `_ä`, `_å` eller `_ö`; acceleratorerna använder ASCII-bokstäver.
- Validering: `msgfmt --check` utan fel; aktuell POT och granskad katalog har samma 795 aktiva nycklar, utan platshållaravvikelser. `l10n-lint` har inga fel; de två dokumenterade varningarna är `T&T Dollar`, där `&` är del av egennamnet men har översatts till ”och”, och svenskans identiska singular/plural för ”argument”.
- Hunspell: tekniska identifierare, enhetsalias, valuta- och egennamn är manuellt kontrollerade undantag, bland annat `MPFR`, `UTF-8`, `UTF-16`, `CFA`, `NAND`, `XNOR`, `XOR`, SI- och IEC-prefix samt kommandoflaggor. Fragment som uppstår när Hunspell delar acceleratorsträngar ignoreras.
- GNOME-inskick: inget.
