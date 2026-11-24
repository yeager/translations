# polkit — main — po — svenska

- Damned Lies: https://l10n.gnome.org/vertimus/polkit/main/po/sv/
- POT/PO-källa: https://l10n.gnome.org/POT/polkit.main/polkit.main.pot och https://l10n.gnome.org/POT/polkit.main/polkit.main.sv.po
- Senaste mall hämtad 2026-11-24; POT: 28 strängar.
- Upstream vid hämtning: 27 översatta, 1 fuzzy, 0 tomma.
- Slutlig lokal fil: 28 översatta, 0 fuzzy, 0 tomma.
- Ändrade aktiva poster: 11 rättelser, inklusive en fuzzy-sträng som hade fått fel översättning.
- Hela katalogen radgranskades. Rättelserna översätter beskrivande kommandoradsmetavariabler i pkcheck-hjälpen: ACTION, KEY, VALUE, START_TIME och BUS_NAME. Flaggar, PID och UID bevaras.
- Validering: msgfmt --check godkänd; msgcmp --use-fuzzy matchar senaste POT; l10n-lint --language sv utan fel eller varningar. Egen kontroll av formatplatshållare, radbrytningar, acceleratormarkörer och samtliga kommandotoken godkänd.
- hunspell-sv kördes. Rimliga undantag: kommandoradsflaggor, PID, FD och UID. Beskrivande metavariabler som START_TIME och BUS_NAME är översatta till STARTTID och BUSSNAMN., kod-/formatnamn (Frobnicate, gecos) och giltiga svenska sammansättningar.
- Original, granskad fil, POT, diff och rapport sparade. Ingenting har skickats till GNOME.

## Korrigering av kommandoradsmetavariabler (2026-11-24)

- 7 befintliga strängar korrigerade: beskrivande kommandoradsargument översatta till svenska.
- Validering: `msgfmt --check`; `l10n-lint`-regeln `metavariable-translation` ger inga kvarvarande träffar i de 295 granskade huvudgrenarnas kataloger.
- Ändringen är lokal och har inte skickats till GNOME.
