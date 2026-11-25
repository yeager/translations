# Highscore — main — svensk granskning

- Katalog: [Highscore i Damned Lies](https://l10n.gnome.org/vertimus/highscore/main/po/sv/)
- Källkod: [World/highscore](https://gitlab.gnome.org/World/highscore), revision `3d4689e24a0f79a05fe0d754d4988e44a9b938da` (main).
- Senaste POT hämtad 2026-11-25: `https://l10n.gnome.org/POT/highscore.main/highscore.main.pot`
- POT SHA-256: `e12a7666260eef6550cdfdf3730d241c8bbf540eb46ed2ce6d6e2eaaf184b8c5`
- Före granskning: 655 översatta, 56 fuzzy, 24 oöversatta (735 aktiva poster).
- Efter granskning: 735 översatta, 0 fuzzy, 0 oöversatta.
- Ändringar: 24 tomma strängar översatta, 56 fuzzy-rader granskade och lösta, 131 tydliga brister rättade i tidigare icke-fuzzy svenska. Totalt fick 211 aktiva poster en textändring.
- Last-Translator: Daniel Nylander <gnome@danielnylander.se>.

## Validering

- `msgfmt --check` och `msgcmp` mot senaste POT: godkända.
- `l10n-lint --language sv --reference highscore.main.pot`: 0 fel. Fyra varningar gäller pluralformer där svensk singular och plural medvetet har identisk form (`spel`); formerna är korrekta.
- Egen kontroll av formatplatshållare, markup och acceleratorer: 0 avvikelser.
- `hunspell-sv`: genomgången. Undantagen är officiella produkt- och plattformsnamn (bland annat Highscore, 8BitDo, Game Boy, Mega Drive, PlayStation, TurboGrafx och Xbox), personnamn, licensnamn, hårdvaruknappar och tekniska termer/förkortningar (ROM, BIOS, CRT, MIME, URI, QAM). Korrekt bildade sammansättningar som `handkontrollstyp`, `kamfilter`, `punktmask`, `spaltmask`, `färgkorrigeringsshaders` och verbet `snabbspara` kan saknas i ordlistan. Prefixen `företags-` och `produkt-` ingår i en korrekt samordnad uppräkning. Hunspell delar även ord vid gettext-acceleratorer och formatplatshållare.
- Talet 5 i uppgiften om automatiska ögonblicksbilder har skrivits idiomatiskt som *var femte minut*.

Ingen GNOME-inskickning har gjorts.

## Filer

- [Original PO](highscore.main.sv.original.po)
- [Granskad PO](highscore.main.sv.reviewed.po)
- [Diff](highscore.main.sv.diff)
- [Senaste POT](highscore.main.pot)
