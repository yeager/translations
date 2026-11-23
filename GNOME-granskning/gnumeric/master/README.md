# Gnumeric — master — svenska gränssnitt och funktionshjälp

> **Komponentstatus.** `po-functions` är uppdaterad från aktuell Damned Lies-POT och svenska PO 2026-11-23: 2 183 aktiva poster, 0 oöversatta och 0 fuzzy. Arkivparet `gnumeric.master.po-functions.*` är den aktuella granskningen. `po` och hjälpfilen är separata kataloger och är fortfarande oavslutade; äldre Git-baserade filer i denna mapp får inte tolkas som deras aktuella status.

- GNOME-status före granskning: `po`: 3 974 översatta, 0 fuzzy, 0 oöversatta; `po-functions`: 2 157 översatta, 0 fuzzy, 0 oöversatta.
- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnumeric/master/po/sv/> och <https://l10n.gnome.org/vertimus/gnumeric/master/po-functions/sv/>.
- Åtgärd: Radgranskning av gränssnitt och funktionshjälp; 359 dokumentationsplatshållare `@{…}` återställdes exakt, svenska acceleratorer och tabellformat rättades samt tydliga formuleringar förbättrades.
- Ändringar: 0 nya översättningar, 29 korrigerade befintliga UI-poster och 376 korrigerade befintliga funktionshjälpposter.
- Validering: `msgfmt --check`, egen kontroll av platshållare, pluralformer, tabbar och radbrytningar samt `l10n-lint --language sv --skip-fuzzy`.
- Aktuell lokal status: `po-functions`: 2 183 översatta, 0 fuzzy och 0 oöversatta. `po`: tidigare Git-baserad status är inte verifierad mot aktuell POT-fil.
- Dokumenterade lint-undantag: `l10n-lint` misstolkar Gnumerics avsiktligt översatta `@{argument}` som Python-platshållare och rapporterar därför 367 felaktiga formatfel. Gnumerics `README.translators` kräver uttryckligen översättning av argumentnamn och konsekvent användning i `@{…}`. `msgfmt --check` samt egen kontroll av varje ändrad `@{…}` är den relevanta formatvalideringen här.
- Översättarmetadata: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-23 14:15+0100.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
