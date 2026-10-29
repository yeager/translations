# Porpoise: kommatering och tydlighet, 29 oktober 2026

En ny radvis genomgång av den kompletta svenska katalogen hittade 21
kommavarningar före `och` i 20 poster. Varje träff granskades i sin
engelska källkontext.

Rättningen omfattar bland annat:

- samordnade gränssnittsrubriker och hjälptexter, där överflödiga komman
  har tagits bort;
- längre instruktioner för bredbild, Wii-online, Gecko-koder och
  bildgenerering, där självständiga satser har delats när det gör texten
  lättare att läsa;
- två sakförtydliganden: TV-utdata för menyer och spel samt exakta
  flyttalsberäkningar med multiplikation och addition.

`porpoise-sv-comma-and-clarity-20261029.json` är den kompletta svenska
katalogen efter rättningen. Den har 1 803 av 1 803 nycklar, inga tomma eller
extra nycklar och inga avvikande platsvariabler inom klammerparenteser.

Kontroller som passerar:

- `tools/make-i18n.py --check`;
- generering av `src/ui_i18n_table.inc`;
- `clang++ -std=c++17 -Wall -Wextra -Werror -Isrc -c src/ui_i18n.cpp`;
- `svlang skrivregler`, Git-whitespacekontroll och avgränsad Gitleaks.

Förändringen ska läggas till som en separat commit på den öppna svenska
lokaliserings-PR:n. Den ersätter inte ett PS5-körtest.
