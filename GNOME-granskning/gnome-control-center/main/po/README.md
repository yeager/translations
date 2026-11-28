# gnome-control-center — main — svenska UI

- GNOME-status före granskning: 2 149 aktiva strängar, 0 fuzzy, 0 oöversatta (GNOME Git `cd52f56`, 2026-11-23).
- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnome-control-center/main/po/sv/>
- Åtgärd: Rättade två nordiska acceleratorer, en saknad accelerator, två procentformat och PIN-kodens intervallstreck.
- Ändringar: 0 nya översättningar, 6 rättade befintliga strängar.
- Validering: `msgfmt --check`; `l10n-lint` utan fel; C-format, pluraler, radbrytningar och acceleratorer kontrollerade.
- Dokumenterade undantag: `Wi-Fi`, `MAC`, `DNS`, `IPv4`, `IPv6`, radiostandarder och samma svenska pluralform för ”jobb” är etablerade tekniska eller språkliga uttryck.
- Översättarmetadata: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-23 12:00+0100.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
- Slutlig lokal status: 2 149 översatta, 0 fuzzy, 0 oöversatta.

## A11y-terminologi, 2026-11-28

I sökordslistan ändrades `Accessibility;Hjälpmedel;Tillgänglighet;` till `Hjälpmedel;`, så a11y-synonymerna följer termen *hjälpmedel*. POT har 2 172 poster. Den nedladdade aktuella PO-filen visar 2 115 översatta, 27 fuzzy och 31 tomma; aktivitetssidan visar 2 140/27/5. l10n-lint: 0 fel/varningar. Hunspell-undantag: `AccessX`, `a11y` och den etablerade gränssnittstermen `Mustangenter`. Katalogen är ofullständig mot senaste POT, därför kördes inte `msgfmt`. Ändringen skickades inte till GNOME. Se `gnome-control-center-main-a11y-terminology-2026-11-28.diff`.
