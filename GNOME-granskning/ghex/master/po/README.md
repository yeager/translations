# GHex — master — svenska UI

- GNOME-status före granskning: 260 översatta, 0 fuzzy, 0 oöversatta.
- Aktuell POT hämtad från Damned Lies: 260 meddelanden; POT-huvudets datum är 2026-10-14 18:41 UTC. Aktivitetssidan visar mallens senaste datum 10 november 2026.
- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/ghex/master/po/sv/>
- Källkontext: `src/preferences.ui` och hjälptexten för utskriftsinställningen bekräftar att “Span across lines” anger antalet rader som skuggas.
- Granskning: alla 260 aktiva strängar radgranskade. 60 befintliga översättningar rättade; 0 nya översättningar. Bland rättningarna finns ett Brasero-fel i licenstexten, felaktiga “flytande” taltyper, stavfelet “Klista”, terminologi för hexadecimalredigering och naturligare felmeddelanden.
- Slutlig lokal status: 260 översatta, 0 fuzzy, 0 oöversatta.
- Validering: `msgfmt --check --check-format` och `msgcmp --use-fuzzy` godkända. `l10n-lint --language sv --reference` rapporterar 0 fel och 1 varning: bindestrecket i det oförändrade amerikanska ZIP+4-postnumret `02110-1301` i Free Software Foundation-adressen. Informationsnotiser gäller godkända flyttade acceleratorer och oförändrat ASCII. Egen kontroll av platshållare, markup, radbrytningar och acceleratorantal godkänd; inga aktiva `_ä`, `_å` eller `_ö`.
- Hunspell-svenska: inga stavfel hittades. Dokumenterade undantag bland ändrade strängar: produktnamnet `GHex`; tekniska termer `ASCII`, `Quadword`, `little-endian`, `0x`, `fd`; samt korrekta sammansättningar som `hexdata`, `hexsiffra`, `byteintervall`, `byteposition` och `hexvyn`. Acceleratorn `_` delar upp `Å_ngra` och `Å_terställ` i ordfragment.
- Översättarmetadata: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-26.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
