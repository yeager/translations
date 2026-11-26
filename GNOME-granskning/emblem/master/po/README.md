# Emblem — master/po — svensk granskning

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/emblem/master/po/sv/>
- Granskad: 2026-11-23
- Aktuell POT: 39 aktiva strängar
- Nya översättningar: 0
- Korrigerade befintliga översättningar: 3

Hela katalogen är radgranskad mot senaste POT. `Git-smedjor` har korrekt
produktnamnskapitalisering och de två färgåtgärderna använder den etablerade
termen `toning` på naturlig svenska.

`msgfmt --check` och `msgcmp --use-fuzzy` är godkända. `l10n-lint` har inga
fel eller varningar; dess två informationsnotiser är kontrollerade: de tre
svenska söktermerna för `logo;` och en avsiktligt flyttad accelerator i
`S_quare` → `_Kvadrat`. Hunspell-sv-undantagen är produktnamn, filnamn och
tekniska format. Ingen inskickning till GNOME har gjorts i detta steg.

- GNOME-inskick: 2026-11-26 via Damned Lies API; kommentaren `Granskad och klar` och aktivitetssidan verifierade; statistik 39/0/0.
