# GNOME Calculator Hjälp — main/help (sv)

- Aktivitet: https://l10n.gnome.org/vertimus/gnome-calculator/main/help/sv/
- Käll-POT: `gnome-calculator-help.main.pot`, skapad 2026-11-25 16:17 UTC
- Utgångsstatus i Damned Lies: 398 översatta, 4 fuzzy, 1 oöversatt
- Slutstatus i granskad fil: 403 översatta, 0 fuzzy, 0 oöversatta
- Nya översättningar: 1
- Rättade befintliga strängar: 91 (däribland 4 fuzzy-poster)

Alla 403 aktiva poster jämfördes med senaste POT och granskades. Korrigeringarna
omfattar bland annat `cis` och polära komplexa tal, rötter och avrundning,
finansiella funktioner, procentberäkningar, vetenskaplig notation och
naturvetenskapliga konstanter. Exempel som består av inmatningsuttryck i
kalkylatorn lämnades i sin matematiska notation. `Last-Translator` uppdaterades
till Daniel Nylander <gnome@danielnylander.se>.

`msgfmt --check --check-format` och `msgcmp` passerar. `l10n-lint` har 0 fel
och 2 dokumenterade varningar för procenttecken utan mellanrum i de exakta
kalkylatoruttrycken `140+15%` och `25%×80`; mellanrum skulle ändra de visade
inmatningsexemplen. Övriga informationsnotiser gäller uttryck som avsiktligt
är identiska med källan. Egna kontroller av markup, URL:er och C-format har 0
avvikelser. `hunspell-sv` kördes på ändrade strängar; undantag för matematiska
funktionsnamn, symboler, personnamn och svenska facktermer/sammansättningar
listas i `hunspell-unknown.txt`.

Ingen ändring har skickats till GNOME.
